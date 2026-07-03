#!/usr/bin/env python3
"""Scout recent high-citation papers from OpenAlex for selected DPR profiles."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None


ROOT_DIR = Path(__file__).resolve().parents[1]
OPENALEX_WORKS_URL = "https://api.openalex.org/works"
ARXIV_API_URL = "http://export.arxiv.org/api/query"
ARXIV_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}
OPENALEX_USER_AGENT = "daily-paper-reader-hot-paper-scout/1.0"
DEFAULT_DOMAIN_QUERY = (
    "embodied intelligence; embodied AI; embodied agents; "
    "vision-language-action model; robot foundation model; "
    "generalist robot policy; humanoid robot policy; robot learning foundation model"
)
RETRYABLE_HTTP_STATUS = {429, 500, 502, 503, 504}
EMBODIED_AI_COMPANY_ALIASES = {
    "1x technologies",
    "agibot",
    "agility robotics",
    "agile robots",
    "apptronik",
    "boston dynamics",
    "covariant",
    "deepmind",
    "engineai",
    "everyday robots",
    "field ai",
    "figure ai",
    "fourier intelligence",
    "galbot",
    "google deepmind",
    "google robotics",
    "intrinsic ai",
    "nvidia",
    "nvidia research",
    "physical intelligence",
    "sanctuary ai",
    "skild",
    "skild ai",
    "tesla",
    "tesla bot",
    "ubtech",
    "unitree",
    "unitree robotics",
    "xiaomi robotics",
    "xpeng robotics",
    "zhiyuan robotics",
}
ARXIV_COMPANY_QUERY_NAMES = [
    "Physical Intelligence",
    "Figure AI",
    "Skild AI",
    "Covariant",
    "Boston Dynamics",
    "Agility Robotics",
    "Unitree",
    "Apptronik",
    "1X Technologies",
    "Sanctuary AI",
    "Field AI",
    "Intrinsic",
    "Google DeepMind",
    "NVIDIA",
    "Tesla",
    "Fourier Intelligence",
    "UBTECH",
    "Xiaomi Robotics",
    "XPeng Robotics",
    "Zhiyuan Robotics",
]
ARXIV_DOMAIN_FALLBACK_TERMS = [
    "embodied AI",
    "embodied intelligence",
    "robot foundation model",
    "vision-language-action",
    "humanoid robot",
    "robot learning",
    "physical AI",
]


def log(message: str) -> None:
    print(message, flush=True)


def safe_slug(value: str, fallback: str = "paper") -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9._-]+", "-", text)
    text = text.strip("-._")
    return text[:120].strip("-._") or fallback


def single_line(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def parse_csv(value: str) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for raw in str(value or "").split(","):
        item = raw.strip()
        key = item.lower()
        if not item or key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def parse_query_list(value: str) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for raw in re.split(r"[\n;,，；]+", str(value or "")):
        item = single_line(raw)
        key = item.lower()
        if not item or key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def inverted_index_to_text(index: Any) -> str:
    if not isinstance(index, dict):
        return ""
    words: list[tuple[int, str]] = []
    for word, positions in index.items():
        if not isinstance(positions, list):
            continue
        for pos in positions:
            try:
                words.append((int(pos), str(word)))
            except Exception:
                continue
    return " ".join(word for _, word in sorted(words)).strip()


def load_config(path: Path) -> dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML is required to read config.yaml")
    if not path.exists():
        raise FileNotFoundError(path)
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else {}


def iter_profiles(config: dict[str, Any], profile_tags: list[str]) -> list[dict[str, Any]]:
    subs = config.get("subscriptions") if isinstance(config.get("subscriptions"), dict) else {}
    profiles = subs.get("intent_profiles") if isinstance(subs.get("intent_profiles"), list) else []
    wanted = {tag.lower() for tag in profile_tags}
    out: list[dict[str, Any]] = []
    for profile in profiles:
        if not isinstance(profile, dict):
            continue
        tag = str(profile.get("tag") or "").strip()
        if not tag:
            continue
        if wanted and tag.lower() not in wanted:
            continue
        if not wanted and profile.get("enabled") is False:
            continue
        out.append(profile)
    return out


def profile_queries(profile: dict[str, Any], limit: int = 8) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []

    def add(value: Any) -> None:
        text = single_line(str(value or ""))
        key = text.lower()
        if not text or key in seen or len(out) >= limit:
            return
        seen.add(key)
        out.append(text)

    for item in profile.get("intent_queries") or []:
        if not isinstance(item, dict):
            continue
        if item.get("enabled") is False:
            continue
        add(item.get("query"))
    for item in profile.get("keywords") or []:
        if not isinstance(item, dict):
            continue
        add(item.get("query") or item.get("keyword"))
    return out


def normalize_institution_filter(value: str) -> str:
    text = str(value or "").strip().lower()
    return text if text in {"all", "company", "university"} else "all"


def institution_filter_label(value: str) -> str:
    return {
        "all": "全部机构",
        "company": "具身智能公司相关",
        "university": "高校",
    }.get(normalize_institution_filter(value), "全部机构")


def normalize_institution_type(value: Any) -> str:
    text = str(value or "").strip().lower()
    if text in {"education", "university", "college", "school"}:
        return "education"
    if text in {"company", "facility"}:
        return text
    return text


def extract_institutions(work: dict[str, Any], *, lead_only: bool = False) -> list[dict[str, str]]:
    institutions: list[dict[str, str]] = []
    seen: set[str] = set()
    for authorship in work.get("authorships") or []:
        if not isinstance(authorship, dict):
            continue
        author_position = str(authorship.get("author_position") or "").strip().lower()
        if lead_only and author_position not in {"first", "last"}:
            continue
        for inst in authorship.get("institutions") or []:
            if not isinstance(inst, dict):
                continue
            name = single_line(str(inst.get("display_name") or ""))
            inst_id = str(inst.get("id") or "").strip()
            inst_type = normalize_institution_type(inst.get("type"))
            key = (inst_id or name).lower()
            if not key or key in seen:
                continue
            seen.add(key)
            institutions.append({
                "id": inst_id,
                "name": name,
                "type": inst_type,
                "author_position": author_position,
            })
    return institutions


def text_matches_embodied_ai_company_alias(text: str) -> bool:
    normalized = re.sub(r"[^a-z0-9]+", " ", str(text or "").lower())
    padded = f" {normalized} "
    return any(f" {alias} " in padded for alias in EMBODIED_AI_COMPANY_ALIASES)


def matched_embodied_ai_company_name(text: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", " ", str(text or "").lower())
    padded = f" {normalized} "
    for alias in sorted(EMBODIED_AI_COMPANY_ALIASES, key=len, reverse=True):
        if f" {alias} " in padded:
            return alias
    return ""


def work_company_relation(work: dict[str, Any]) -> tuple[str, str]:
    lead_institutions = extract_institutions(work, lead_only=True)
    lead_names = " ".join(inst.get("name") or "" for inst in lead_institutions)
    match = matched_embodied_ai_company_name(lead_names)
    if match:
        return match, "lead-affiliation"

    institutions = extract_institutions(work)
    institution_names = " ".join(inst.get("name") or "" for inst in institutions)
    match = matched_embodied_ai_company_name(institution_names)
    if match:
        return match, "affiliation"

    title = single_line(str(work.get("display_name") or ""))
    match = matched_embodied_ai_company_name(title)
    if match:
        return match, "title"

    abstract = inverted_index_to_text(work.get("abstract_inverted_index"))
    match = matched_embodied_ai_company_name(abstract)
    if match:
        return match, "abstract"

    return "", ""


def work_matches_institution_filter(work: dict[str, Any], mode: str) -> bool:
    normalized = normalize_institution_filter(mode)
    if normalized == "all":
        return True
    institutions = extract_institutions(work)
    if normalized == "university":
        return any(inst.get("type") == "education" for inst in institutions)
    if normalized == "company":
        company, _source = work_company_relation(work)
        return bool(company)
    return True


def chunked(values: list[str], size: int) -> list[list[str]]:
    return [values[idx : idx + size] for idx in range(0, len(values), size)]


def authors_for_work(work: dict[str, Any]) -> list[str]:
    authors: list[str] = []
    for authorship in work.get("authorships") or []:
        if not isinstance(authorship, dict):
            continue
        author = authorship.get("author") if isinstance(authorship.get("author"), dict) else {}
        name = single_line(str(author.get("display_name") or ""))
        if name:
            authors.append(name)
    return authors[:20]


def landing_url_for_work(work: dict[str, Any]) -> str:
    for loc_key in ["primary_location", "best_oa_location"]:
        loc = work.get(loc_key) if isinstance(work.get(loc_key), dict) else {}
        for key in ["landing_page_url", "pdf_url"]:
            value = str(loc.get(key) or "").strip()
            if value:
                return value
    ids = work.get("ids") if isinstance(work.get("ids"), dict) else {}
    return str(ids.get("doi") or ids.get("openalex") or work.get("doi") or work.get("id") or "").strip()


def pdf_url_for_work(work: dict[str, Any]) -> str:
    for loc_key in ["primary_location", "best_oa_location"]:
        loc = work.get(loc_key) if isinstance(work.get(loc_key), dict) else {}
        value = str(loc.get("pdf_url") or "").strip()
        if value:
            return value
    return ""


def normalize_work(work: dict[str, Any], profile_tag: str, query: str) -> dict[str, Any]:
    ids = work.get("ids") if isinstance(work.get("ids"), dict) else {}
    doi = str(work.get("doi") or ids.get("doi") or "").strip()
    openalex_id = str(work.get("id") or ids.get("openalex") or "").strip()
    title = single_line(str(work.get("display_name") or "Untitled work"))
    institutions = extract_institutions(work)
    lead_institutions = extract_institutions(work, lead_only=True)
    abstract = inverted_index_to_text(work.get("abstract_inverted_index"))
    company_match, company_relation_source = work_company_relation(work)
    return {
        "id": openalex_id,
        "openalex_id": openalex_id,
        "doi": doi,
        "title": title,
        "authors": authors_for_work(work),
        "institutions": institutions,
        "lead_institutions": lead_institutions,
        "institution_names": [inst["name"] for inst in institutions if inst.get("name")],
        "lead_institution_names": [inst["name"] for inst in lead_institutions if inst.get("name")],
        "institution_types": sorted({inst["type"] for inst in institutions if inst.get("type")}),
        "publication_date": str(work.get("publication_date") or "").strip(),
        "publication_year": work.get("publication_year"),
        "cited_by_count": int(work.get("cited_by_count") or 0),
        "abstract": abstract,
        "link": landing_url_for_work(work),
        "pdf_url": pdf_url_for_work(work),
        "profile_tag": profile_tag,
        "matched_query": query,
        "source": "openalex",
        "company_match": company_match,
        "company_relation_source": company_relation_source,
    }


def arxiv_pdf_url(entry: ET.Element) -> str:
    for link in entry.findall("atom:link", ARXIV_NS):
        if link.get("title") == "pdf" or link.get("type") == "application/pdf":
            href = str(link.get("href") or "").strip()
            if href:
                return href
    entry_id = single_line(entry.findtext("atom:id", default="", namespaces=ARXIV_NS))
    if "arxiv.org/abs/" in entry_id:
        return entry_id.replace("/abs/", "/pdf/")
    return ""


def arxiv_id_from_url(value: str) -> str:
    text = single_line(value)
    match = re.search(r"arxiv\.org/(?:abs|pdf)/([^?#\s/]+)", text, flags=re.IGNORECASE)
    if not match:
        return ""
    return match.group(1).removesuffix(".pdf")


def arxiv_author_records(entry: ET.Element) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for author in entry.findall("atom:author", ARXIV_NS):
        name = single_line(author.findtext("atom:name", default="", namespaces=ARXIV_NS))
        affiliation = single_line(author.findtext("arxiv:affiliation", default="", namespaces=ARXIV_NS))
        if name or affiliation:
            records.append({"name": name, "affiliation": affiliation})
    return records


def arxiv_lead_affiliation_company_match(author_records: list[dict[str, str]]) -> str:
    if not author_records:
        return ""
    lead_records = [author_records[0]]
    if len(author_records) > 1:
        lead_records.append(author_records[-1])
    affiliation_text = " ".join(record.get("affiliation") or "" for record in lead_records)
    return matched_embodied_ai_company_name(affiliation_text)


def arxiv_company_relation(title: str, abstract: str, author_records: list[dict[str, str]]) -> tuple[str, str]:
    match = arxiv_lead_affiliation_company_match(author_records)
    if match:
        return match, "lead-affiliation"
    match = matched_embodied_ai_company_name(title)
    if match:
        return match, "title"
    match = matched_embodied_ai_company_name(abstract)
    if match:
        return match, "abstract"
    return "", ""


def arxiv_entry_to_paper(entry: ET.Element, query: str, from_date: str, institution_filter: str) -> dict[str, Any] | None:
    title = single_line(entry.findtext("atom:title", default="", namespaces=ARXIV_NS))
    abstract = single_line(entry.findtext("atom:summary", default="", namespaces=ARXIV_NS))
    published = single_line(entry.findtext("atom:published", default="", namespaces=ARXIV_NS))[:10]
    if from_date and published and published < from_date:
        return None
    author_records = arxiv_author_records(entry)
    authors = [record["name"] for record in author_records if record.get("name")]
    entry_id = single_line(entry.findtext("atom:id", default="", namespaces=ARXIV_NS))
    arxiv_id = arxiv_id_from_url(entry_id)
    doi = single_line(entry.findtext("arxiv:doi", default="", namespaces=ARXIV_NS))
    mode = normalize_institution_filter(institution_filter)
    matched_company, relation_source = arxiv_company_relation(title, abstract, author_records)
    if mode == "company":
        # Query text is never evidence.  Accept arXiv fallback items only when
        # the entry's own metadata (title/abstract/lead affiliation) names a
        # relevant embodied-AI company or robot platform.
        if not matched_company:
            return None
    company_label = matched_company or "arXiv metadata"
    return {
        "id": entry_id,
        "arxiv_id": arxiv_id,
        "arxiv_url": entry_id,
        "openalex_id": "",
        "doi": doi,
        "title": title or "Untitled arXiv work",
        "authors": authors[:20],
        "institutions": [{"id": "", "name": company_label, "type": "company", "author_position": "inferred"}] if matched_company else [],
        "lead_institutions": [{"id": "", "name": company_label, "type": "company", "author_position": "inferred"}] if matched_company else [],
        "institution_names": [company_label] if matched_company else [],
        "lead_institution_names": [company_label] if matched_company else [],
        "institution_types": ["company"] if matched_company else [],
        "publication_date": published,
        "publication_year": int(published[:4]) if published[:4].isdigit() else None,
        "cited_by_count": 0,
        "abstract": abstract,
        "link": entry_id,
        "pdf_url": arxiv_pdf_url(entry),
        "profile_tag": "具身智能",
        "matched_query": query,
        "source": "arxiv_fallback",
        "company_match": matched_company,
        "company_relation_source": relation_source,
        "institution_source": f"arxiv-{relation_source}" if matched_company else "",
    }


def fetch_arxiv_fallback(
    domain_queries: list[str],
    *,
    from_date: str,
    institution_filter: str,
    max_results: int,
    timeout: int = 25,
) -> tuple[list[dict[str, Any]], list[str]]:
    mode = normalize_institution_filter(institution_filter)
    if mode == "university":
        return [], ["arXiv fallback 不含可靠机构类型，已跳过高校筛选兜底。"]
    domain_terms = domain_queries or ARXIV_DOMAIN_FALLBACK_TERMS
    domain_terms = list(dict.fromkeys([*domain_terms[:8], *ARXIV_DOMAIN_FALLBACK_TERMS]))
    domain_clause = "(" + " OR ".join(f'all:"{term}"' for term in domain_terms[:12]) + ")"
    company_batches = chunked(ARXIV_COMPANY_QUERY_NAMES, 5) if mode == "company" else [[]]
    papers: dict[str, dict[str, Any]] = {}
    warnings: list[str] = []

    for batch_idx, company_batch in enumerate(company_batches, start=1):
        if company_batch:
            company_clause = "(" + " OR ".join(f'all:"{name}"' for name in company_batch) + ")"
            search_query = f"{company_clause} AND {domain_clause}"
        else:
            search_query = domain_clause
        params = {
            "search_query": search_query,
            "start": "0",
            "max_results": str(max(1, min(int(max_results or 30) * 2, 50))),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = f"{ARXIV_API_URL}?{urllib.parse.urlencode(params)}"
        try:
            request = urllib.request.Request(url, headers={"User-Agent": OPENALEX_USER_AGENT})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                payload = response.read().decode("utf-8", errors="replace")
            root = ET.fromstring(payload)
        except Exception as exc:
            warnings.append(f"arXiv fallback 查询失败 batch {batch_idx}: {type(exc).__name__}: {single_line(str(exc))[:200]}")
            continue
        for entry in root.findall("atom:entry", ARXIV_NS):
            paper = arxiv_entry_to_paper(entry, search_query, from_date, mode)
            if not paper:
                continue
            key = (paper.get("doi") or paper.get("id") or paper.get("title") or "").lower()
            if key:
                papers[key] = paper
        if len(company_batches) > 1:
            time.sleep(3.0)
    if mode == "company" and not papers:
        warnings.append(
            "arXiv fallback 未发现 title/abstract/first-last author affiliation 明确匹配具身智能公司或平台的论文；"
            "已拒绝 search query 本身命中，避免把检索词误当作论文证据。"
        )
    return list(papers.values()), warnings


class OpenAlexClient:
    def __init__(self, timeout: int = 20, mailto: str = "", retries: int = 3) -> None:
        self.timeout = timeout
        self.mailto = mailto.strip()
        self.retries = max(int(retries or 1), 1)

    def list_works(self, query: str, from_date: str, institution_filter: str, per_page: int) -> list[dict[str, Any]]:
        filters = [f"from_publication_date:{from_date}", "has_abstract:true"]
        mode = normalize_institution_filter(institution_filter)
        if mode == "company":
            filters.append("authorships.institutions.type:company")
        elif mode == "university":
            filters.append("authorships.institutions.type:education")
        return self._request(query, filters, per_page)

    def list_unfiltered_works(self, query: str, from_date: str, per_page: int) -> list[dict[str, Any]]:
        filters = [f"from_publication_date:{from_date}", "has_abstract:true"]
        return self._request(query, filters, per_page)

    def _request(self, query: str, filters: list[str], per_page: int) -> list[dict[str, Any]]:
        params = {
            "search": query,
            "filter": ",".join(filters),
            "sort": "cited_by_count:desc",
            "per-page": str(max(1, min(int(per_page or 25), 100))),
        }
        if self.mailto:
            params["mailto"] = self.mailto
        url = f"{OPENALEX_WORKS_URL}?{urllib.parse.urlencode(params)}"
        last_error: Exception | None = None
        for attempt in range(1, self.retries + 1):
            request = urllib.request.Request(url, headers={"User-Agent": OPENALEX_USER_AGENT})
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    payload = json.loads(response.read().decode("utf-8"))
                break
            except urllib.error.HTTPError as exc:
                last_error = exc
                if exc.code not in RETRYABLE_HTTP_STATUS or attempt >= self.retries:
                    raise
            except (TimeoutError, urllib.error.URLError) as exc:
                last_error = exc
                if attempt >= self.retries:
                    raise
            time.sleep(min(1.5 * attempt, 5.0))
        else:
            raise last_error or RuntimeError("OpenAlex request failed")
        results = payload.get("results") if isinstance(payload, dict) else []
        return [item for item in results if isinstance(item, dict)]


@dataclass
class ScoutResult:
    papers: list[dict[str, Any]]
    warnings: list[str]
    profiles: list[dict[str, Any]]
    domain_queries: list[str]
    queries: list[dict[str, str]]
    from_date: str
    run_token: str


def scout_hot_papers(
    config: dict[str, Any],
    *,
    profile_tag: str,
    domain_query: str,
    days_window: int,
    institution_filter: str,
    max_results: int,
    client: OpenAlexClient,
) -> ScoutResult:
    requested_tags = parse_csv(profile_tag)
    domain_queries = parse_query_list(domain_query)
    profiles = iter_profiles(config, requested_tags) if requested_tags or not domain_queries else []
    now = datetime.now(timezone.utc)
    from_date = (now - timedelta(days=max(int(days_window or 30), 1))).strftime("%Y-%m-%d")
    domain_token = safe_slug("-".join(domain_queries[:2]), "domain")[:40]
    tags_token = "-".join(requested_tags or [str(p.get("tag") or "all") for p in profiles[:3]]) or domain_token or "all"
    token_hash = hashlib.sha1(f"{tags_token}|{domain_query}|{days_window}|{institution_filter}|{now.isoformat()}".encode("utf-8")).hexdigest()[:8]
    run_token = f"hot-{now.strftime('%Y%m%d-%H%M%S')}-{safe_slug(tags_token, 'all')[:40]}-{token_hash}"
    warnings: list[str] = []
    query_specs: list[dict[str, str]] = []
    candidates: dict[str, dict[str, Any]] = {}
    per_page = max(25, min(100, int(max_results or 30) * 3))

    if requested_tags and not profiles:
        warnings.append(f"未找到匹配词条：{', '.join(requested_tags)}")
    if not profiles and not domain_queries:
        warnings.append("没有可用词条，已生成空结果页。")

    mode = normalize_institution_filter(institution_filter)
    query_groups: list[tuple[str, list[str]]] = []
    if domain_queries:
        query_groups.append(("具身智能", domain_queries[:8]))
    for profile in profiles:
        tag = str(profile.get("tag") or "").strip()
        queries = profile_queries(profile, limit=8)
        if not queries:
            warnings.append(f"词条 {tag} 没有可用 query，已跳过。")
            continue
        query_groups.append((tag, queries))

    for tag, queries in query_groups:
        for query in queries:
            query_specs.append({"profile_tag": tag, "query": query})
            requests_to_try = [(True, "all")] if mode == "company" else [(False, mode)]
            for unfiltered, request_mode in requests_to_try:
                try:
                    works = (
                        client.list_unfiltered_works(query, from_date, per_page)
                        if unfiltered
                        else client.list_works(query, from_date, request_mode, per_page)
                    )
                except Exception as exc:
                    warnings.append(f"OpenAlex 查询失败：{tag} / {query}: {type(exc).__name__}: {single_line(str(exc))[:200]}")
                    continue
                for work in works:
                    if not work_matches_institution_filter(work, mode):
                        continue
                    item = normalize_work(work, tag, query)
                    key = (item.get("doi") or item.get("openalex_id") or item.get("title") or "").lower()
                    if not key:
                        continue
                    existing = candidates.get(key)
                    if existing is None or (
                        int(item.get("cited_by_count") or 0),
                        str(item.get("publication_date") or ""),
                    ) > (
                        int(existing.get("cited_by_count") or 0),
                        str(existing.get("publication_date") or ""),
                    ):
                        candidates[key] = item
                time.sleep(0.08)

    if not candidates and domain_queries:
        fallback_papers, fallback_warnings = fetch_arxiv_fallback(
            domain_queries,
            from_date=from_date,
            institution_filter=mode,
            max_results=max_results,
        )
        warnings.extend(fallback_warnings)
        if fallback_papers:
            warnings.append(
                "OpenAlex 当前无可用候选，已启用 arXiv fallback；"
                "具身智能公司相关模式仅接受论文 title/abstract/first-last author affiliation 明确匹配的条目。"
            )
        for item in fallback_papers:
            key = (item.get("doi") or item.get("id") or item.get("title") or "").lower()
            if key:
                candidates[key] = item

    papers = sorted(
        candidates.values(),
        key=lambda item: (int(item.get("cited_by_count") or 0), str(item.get("publication_date") or "")),
        reverse=True,
    )[: max(1, min(int(max_results or 30), 30))]
    if not papers:
        warnings.append("OpenAlex 返回 0 篇匹配论文。")
    return ScoutResult(
        papers=papers,
        warnings=warnings,
        profiles=profiles,
        domain_queries=domain_queries,
        queries=query_specs,
        from_date=from_date,
        run_token=run_token,
    )


def paper_display_score(paper: dict[str, Any]) -> float:
    if paper.get("source") == "arxiv_fallback":
        return 8.0
    cited = int(paper.get("cited_by_count") or 0)
    if cited >= 100:
        return 10.0
    if cited >= 50:
        return 9.5
    if cited >= 20:
        return 9.0
    if cited >= 10:
        return 8.5
    if cited >= 5:
        return 8.0
    return 7.5


def paper_identifier(paper: dict[str, Any], index: int) -> str:
    arxiv_id = str(paper.get("arxiv_id") or "").strip()
    if arxiv_id:
        return arxiv_id
    openalex_id = str(paper.get("openalex_id") or paper.get("id") or "").strip()
    if openalex_id:
        tail = openalex_id.rstrip("/").rsplit("/", 1)[-1]
        if tail:
            return safe_slug(tail, f"hot-{index:03d}")
    doi = str(paper.get("doi") or "").strip()
    if doi:
        return safe_slug(doi.replace("https://doi.org/", ""), f"hot-{index:03d}")
    return f"hot-{index:03d}"


def paper_recommend_tags(paper: dict[str, Any], institution_filter: str) -> list[str]:
    paper_source = str(paper.get("source") or "openalex")
    tags = [
        "query:热点论文筛选",
        f"query:{paper.get('profile_tag') or 'hot'}",
        f"query:{institution_filter_label(institution_filter)}",
    ]
    if paper_source == "arxiv_fallback":
        arxiv_id = str(paper.get("arxiv_id") or "").strip()
        tags.append(f"paper:arXiv:{arxiv_id}" if arxiv_id else "paper:arXiv")
    else:
        tags.append("paper:OpenAlex")
    company = str(paper.get("company_match") or "").strip()
    if company:
        tags.append(f"company:{company}")
    return list(dict.fromkeys(tag for tag in tags if tag))


def paper_recommend_evidence(paper: dict[str, Any], institution_filter: str, days_window: int) -> str:
    matched_query = single_line(str(paper.get("matched_query") or ""))
    cited = int(paper.get("cited_by_count") or 0)
    if paper.get("source") == "arxiv_fallback":
        company = str(paper.get("company_match") or "").strip()
        relation_source = str(paper.get("company_relation_source") or "").strip()
        parts = [f"hot-paper-scout: arXiv fallback", f"window={days_window}d"]
        if company:
            parts.append(f"company_relation_match={company}")
        if relation_source:
            parts.append(f"relation_source={relation_source}")
        if matched_query:
            parts.append(f"query={matched_query}")
        parts.append(f"institution_source=arxiv-{relation_source}" if relation_source else "institution_source=arxiv-metadata")
    else:
        institutions = ", ".join((paper.get("lead_institution_names") or paper.get("institution_names") or [])[:3])
        company = str(paper.get("company_match") or "").strip()
        relation_source = str(paper.get("company_relation_source") or "").strip()
        parts = [
            "hot-paper-scout: OpenAlex",
            f"window={days_window}d",
            f"cited_by_count={cited}",
            f"institution_filter={normalize_institution_filter(institution_filter)}",
        ]
        if company:
            parts.append(f"company_relation_match={company}")
        if relation_source:
            parts.append(f"relation_source={relation_source}")
        if institutions:
            parts.append(f"institutions={institutions}")
        if matched_query:
            parts.append(f"query={matched_query}")
    return "; ".join(parts)


def paper_to_recommend_item(
    paper: dict[str, Any],
    index: int,
    *,
    institution_filter: str,
    days_window: int,
) -> dict[str, Any]:
    paper_source = str(paper.get("source") or "openalex")
    source_label = "arxiv" if paper_source == "arxiv_fallback" else "openalex"
    pdf_or_link = (
        str(paper.get("pdf_url") or "").strip()
        or str(paper.get("link") or "").strip()
        or str(paper.get("doi") or "").strip()
        or str(paper.get("openalex_id") or "").strip()
    )
    item = {
        "id": paper_identifier(paper, index),
        "paper_id": paper_identifier(paper, index),
        "title": single_line(str(paper.get("title") or f"Hot Paper {index}")),
        "authors": [str(author).strip() for author in paper.get("authors") or [] if str(author).strip()],
        "abstract": str(paper.get("abstract") or "").strip(),
        "published": str(paper.get("publication_date") or "").strip(),
        "link": pdf_or_link,
        "pdf_url": str(paper.get("pdf_url") or pdf_or_link).strip(),
        "arxiv_id": str(paper.get("arxiv_id") or "").strip(),
        "arxiv_url": str(paper.get("arxiv_url") or "").strip(),
        "doi": str(paper.get("doi") or "").strip(),
        "source": source_label,
        "selection_source": "hot_paper_scout",
        "llm_score": paper_display_score(paper),
        "canonical_evidence": paper_recommend_evidence(paper, institution_filter, days_window),
        "llm_tldr_cn": "",
        "llm_tags": paper_recommend_tags(paper, institution_filter),
        "hot_paper_metadata": {
            "source": paper_source,
            "openalex_id": paper.get("openalex_id") or "",
            "cited_by_count": int(paper.get("cited_by_count") or 0),
            "matched_query": paper.get("matched_query") or "",
            "company_match": paper.get("company_match") or "",
            "company_relation_source": paper.get("company_relation_source") or "",
            "institution_names": paper.get("institution_names") or [],
            "lead_institution_names": paper.get("lead_institution_names") or [],
        },
    }
    return item


def write_recommend_file(
    result: ScoutResult,
    *,
    days_window: int,
    institution_filter: str,
    section: str = "deep",
) -> Path:
    recommend_dir = ROOT_DIR / "archive" / result.run_token / "recommend"
    recommend_dir.mkdir(parents=True, exist_ok=True)
    items = [
        paper_to_recommend_item(
            paper,
            index,
            institution_filter=institution_filter,
            days_window=days_window,
        )
        for index, paper in enumerate(result.papers, start=1)
    ]
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "hot_paper_scout",
        "run_token": result.run_token,
        "from_date": result.from_date,
        "days_window": days_window,
        "institution_filter": normalize_institution_filter(institution_filter),
        "profiles": [p.get("tag") for p in result.profiles],
        "domain_queries": result.domain_queries,
        "queries": result.queries,
        "warnings": result.warnings,
        "deep_dive": items if section == "deep" else [],
        "quick_skim": items if section != "deep" else [],
    }
    path = recommend_dir / f"arxiv_papers_{result.run_token}.standard.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def write_outputs(
    result: ScoutResult,
    *,
    docs_dir: Path,
    days_window: int,
    institution_filter: str,
) -> None:
    del docs_dir
    recommend_path = write_recommend_file(
        result,
        days_window=days_window,
        institution_filter=institution_filter,
        section="deep",
    )
    archive_dir = ROOT_DIR / "archive" / datetime.now(timezone.utc).strftime("%Y%m%d") / "hot"
    archive_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "run_token": result.run_token,
        "from_date": result.from_date,
        "days_window": days_window,
        "institution_filter": normalize_institution_filter(institution_filter),
        "profiles": [p.get("tag") for p in result.profiles],
        "domain_queries": result.domain_queries,
        "queries": result.queries,
        "warnings": result.warnings,
        "recommend_path": str(recommend_path.relative_to(ROOT_DIR)),
        "report_route": f"/manual/{result.run_token}/README",
        "papers": result.papers,
    }
    (archive_dir / f"{result.run_token}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Find recent hot papers from OpenAlex for DPR profiles.")
    parser.add_argument("--profile-tag", default="", help="Comma-separated profile tags. Empty means all enabled profiles.")
    parser.add_argument("--domain-query", default=DEFAULT_DOMAIN_QUERY, help="Semicolon/comma separated domain queries.")
    parser.add_argument("--days-window", type=int, choices=(7, 14, 30), default=30)
    parser.add_argument("--institution-filter", choices=("all", "company", "university"), default="company")
    parser.add_argument("--max-results", type=int, default=30)
    parser.add_argument("--config", default=os.environ.get("DPR_CONFIG_FILE") or str(ROOT_DIR / "config.yaml"))
    parser.add_argument("--docs-dir", default=str(ROOT_DIR / "docs"))
    parser.add_argument("--openalex-timeout", type=int, default=20)
    parser.add_argument("--openalex-retries", type=int, default=3)
    args = parser.parse_args()

    try:
        config = load_config(Path(args.config))
    except Exception as exc:
        log(f"[WARN] config load failed: {exc}")
        config = {"subscriptions": {"intent_profiles": []}}

    client = OpenAlexClient(
        timeout=max(int(args.openalex_timeout or 20), 1),
        mailto=os.environ.get("OPENALEX_MAILTO", ""),
        retries=max(int(args.openalex_retries or 3), 1),
    )
    result = scout_hot_papers(
        config,
        profile_tag=args.profile_tag,
        domain_query=args.domain_query,
        days_window=args.days_window,
        institution_filter=args.institution_filter,
        max_results=args.max_results,
        client=client,
    )
    write_outputs(
        result,
        docs_dir=Path(args.docs_dir),
        days_window=args.days_window,
        institution_filter=args.institution_filter,
    )
    for warning in result.warnings:
        log(f"[WARN] {warning}")
    log(f"[OK] Hot paper scout generated {len(result.papers)} paper(s).")
    log(f"HOT_RUN_TOKEN={result.run_token}")
    log(f"HOT_REPORT_ROUTE=/manual/{result.run_token}/README")


if __name__ == "__main__":
    main()
