#!/usr/bin/env python3
"""Scout recent high-citation papers from OpenAlex for selected DPR profiles."""

from __future__ import annotations

import argparse
import hashlib
import html
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
    "1x",
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
    "figure",
    "figure ai",
    "fourier intelligence",
    "galbot",
    "google deepmind",
    "google robotics",
    "intrinsic",
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


def yaml_escape(value: Any) -> str:
    text = str(value or "")
    if not text:
        return "''"
    return json.dumps(text, ensure_ascii=False)


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
        "company": "具身智能公司领衔",
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


def work_matches_institution_filter(work: dict[str, Any], mode: str) -> bool:
    normalized = normalize_institution_filter(mode)
    if normalized == "all":
        return True
    institutions = extract_institutions(work)
    if normalized == "university":
        return any(inst.get("type") == "education" for inst in institutions)
    if normalized == "company":
        lead_institutions = extract_institutions(work, lead_only=True)
        company_scope = lead_institutions or institutions
        names = " ".join(inst.get("name") or "" for inst in company_scope)
        return bool(matched_embodied_ai_company_name(names))
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


def arxiv_entry_to_paper(entry: ET.Element, query: str, from_date: str, institution_filter: str) -> dict[str, Any] | None:
    title = single_line(entry.findtext("atom:title", default="", namespaces=ARXIV_NS))
    abstract = single_line(entry.findtext("atom:summary", default="", namespaces=ARXIV_NS))
    published = single_line(entry.findtext("atom:published", default="", namespaces=ARXIV_NS))[:10]
    if from_date and published and published < from_date:
        return None
    authors = [
        single_line(author.findtext("atom:name", default="", namespaces=ARXIV_NS))
        for author in entry.findall("atom:author", ARXIV_NS)
    ]
    authors = [author for author in authors if author]
    entry_id = single_line(entry.findtext("atom:id", default="", namespaces=ARXIV_NS))
    doi = single_line(entry.findtext("arxiv:doi", default="", namespaces=ARXIV_NS))
    searchable = " ".join([title, abstract, " ".join(authors), query])
    matched_company = matched_embodied_ai_company_name(searchable)
    if normalize_institution_filter(institution_filter) == "company" and not matched_company:
        return None
    company_label = matched_company or "arXiv metadata"
    return {
        "id": entry_id,
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
            warnings.append("OpenAlex 当前无可用候选，已启用 arXiv fallback；arXiv 不提供可靠机构归属，具身智能公司按元数据文本匹配。")
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


def paper_slug(paper: dict[str, Any], index: int) -> str:
    base = paper.get("doi") or paper.get("openalex_id") or paper.get("title") or f"paper-{index}"
    base = str(base).replace("https://doi.org/", "").replace("https://openalex.org/", "")
    return f"{index:03d}-{safe_slug(base, f'paper-{index}')}"


def write_paper_markdown(path: Path, paper: dict[str, Any], index: int, institution_filter: str) -> None:
    paper_source = str(paper.get("source") or "openalex")
    source_label = "arXiv fallback" if paper_source == "arxiv_fallback" else "OpenAlex Hot"
    tags = [
        f"query:{paper.get('profile_tag') or 'hot'}",
        "paper:arXiv" if paper_source == "arxiv_fallback" else "paper:OpenAlex",
        "paper:Hot",
        f"institution:{institution_filter_label(institution_filter)}",
    ]
    abstract = str(paper.get("abstract") or "").strip()
    authors = ", ".join(paper.get("authors") or []) or "Unknown"
    source_link = paper.get("pdf_url") or paper.get("link") or paper.get("doi") or paper.get("openalex_id") or ""
    if paper_source == "arxiv_fallback":
        evidence = f"arXiv fallback; company_match={paper.get('company_match') or ''}; query={paper.get('matched_query') or ''}"
    else:
        evidence = f"OpenAlex cited_by_count={paper.get('cited_by_count') or 0}; query={paper.get('matched_query') or ''}"
    lines = [
        "---",
        f"title: {yaml_escape(paper.get('title'))}",
        f"authors: {yaml_escape(authors)}",
        f"date: {yaml_escape(paper.get('publication_date') or 'Unknown')}",
    ]
    if source_link:
        lines.append(f"pdf: {yaml_escape(source_link)}")
    if paper.get("doi"):
        lines.append(f"doi: {yaml_escape(paper.get('doi'))}")
    lines.extend(
        [
            f"source: {source_label}",
            "selection_source: hot_paper_scout",
            f"tags: [{', '.join(yaml_escape(tag) for tag in tags)}]",
            f"score: {paper.get('cited_by_count') or 0}",
            f"evidence: {yaml_escape(evidence)}",
            f"abstract: {yaml_escape(abstract)}",
            "---",
            "",
            "## 摘要",
            "",
            abstract or "OpenAlex 未提供可用摘要。",
            "",
            "## 领衔机构",
            "",
        ]
    )
    lead_institutions = paper.get("lead_institution_names") or []
    if lead_institutions:
        lines.extend(f"- {name}" for name in lead_institutions[:10])
    else:
        lines.append("- Unknown")
    lines.extend(
        [
            "",
            "## 机构",
            "",
        ]
    )
    institutions = paper.get("institution_names") or []
    if institutions:
        lines.extend(f"- {name}" for name in institutions[:20])
    else:
        lines.append("- Unknown")
    lines.extend(
        [
            "",
            "## 来源信息",
            "",
            f"- Citations: {paper.get('cited_by_count') or 0}",
            f"- Source: {source_label}",
            f"- Matched query: {paper.get('matched_query') or ''}",
            f"- Company match: {paper.get('company_match') or ''}",
            f"- DOI: {paper.get('doi') or ''}",
            f"- Source ID: {paper.get('openalex_id') or paper.get('id') or ''}",
            f"- Link: {paper.get('link') or ''}",
        ]
    )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_readme(path: Path, result: ScoutResult, days_window: int, institution_filter: str) -> None:
    label = institution_filter_label(institution_filter)
    lines = [
        f"# 热点论文筛选 · {label}",
        "",
        f"- 时间范围：最近 {days_window} 天（from_publication_date >= {result.from_date}）",
        f"- 机构筛选：{label}",
        f"- 领域查询：{'; '.join(result.domain_queries) or '无'}",
        f"- 词条：{', '.join(str(p.get('tag')) for p in result.profiles) or '无'}",
        f"- 查询数：{len(result.queries)}",
        f"- 论文数：{len(result.papers)}",
        "",
    ]
    if normalize_institution_filter(institution_filter) == "company":
        lines.extend([
            "> 具身智能公司领衔按第一/末位作者机构判断；若 OpenAlex 缺少作者位置，则回退到任意作者机构，并要求机构名命中内置具身智能公司名单。",
            "",
        ])
    if result.warnings:
        lines.extend(["## Warning", ""])
        lines.extend(f"- {warning}" for warning in result.warnings)
        lines.append("")
    if not result.papers:
        lines.extend(["## 结果", "", "没有筛选到符合条件的论文。", ""])
    else:
        lines.extend(["## 结果", ""])
        for index, paper in enumerate(result.papers, start=1):
            slug = paper_slug(paper, index)
            title = paper.get("title") or f"Paper {index}"
            authors = ", ".join((paper.get("authors") or [])[:4])
            cited = paper.get("cited_by_count") or 0
            date = paper.get("publication_date") or "Unknown"
            institutions = ", ".join((paper.get("institution_names") or [])[:3])
            source = "arXiv fallback" if paper.get("source") == "arxiv_fallback" else "OpenAlex"
            lines.extend(
                [
                    f"### {index}. [{title}]({slug})",
                    "",
                    f"- Citations: {cited}",
                    f"- Date: {date}",
                    f"- Source: {source}",
                    f"- Authors: {authors or 'Unknown'}",
                    f"- Institutions: {institutions or 'Unknown'}",
                    f"- Query: {paper.get('matched_query') or ''}",
                    "",
                ]
            )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def sidebar_payload(title: str, href: str, paper: dict[str, Any] | None = None) -> str:
    source_tag = "arXiv" if paper and paper.get("source") == "arxiv_fallback" else "OpenAlex"
    tags = [{"kind": "paper", "label": "Hot"}, {"kind": "paper", "label": source_tag}]
    score = "-"
    evidence = ""
    link = href
    if paper:
        score = str(paper.get("cited_by_count") or 0)
        evidence = (
            f"arXiv fallback; company_match={paper.get('company_match') or ''}"
            if paper.get("source") == "arxiv_fallback"
            else f"OpenAlex cited_by_count={score}"
        )
        link = str(paper.get("link") or href)
        if paper.get("profile_tag"):
            tags.insert(0, {"kind": "query", "label": str(paper.get("profile_tag"))})
    payload = {
        "title": title,
        "link": link,
        "score": score,
        "tags": tags,
    }
    if evidence:
        payload["evidence"] = evidence
    return html.escape(json.dumps(payload, ensure_ascii=False), quote=True)


def update_hot_sidebar(sidebar_path: Path, result: ScoutResult, days_window: int, institution_filter: str) -> None:
    sidebar_path.parent.mkdir(parents=True, exist_ok=True)
    lines = sidebar_path.read_text(encoding="utf-8").splitlines(keepends=True) if sidebar_path.exists() else []
    if not lines:
        lines = ['* <a class="dpr-sidebar-root-link" href="#/">首页</a>\n']
    section_idx = -1
    for idx, line in enumerate(lines):
        if line.strip().startswith("* Hot Papers"):
            section_idx = idx
            break
    if section_idx == -1:
        insert_idx = len(lines)
        for idx, line in enumerate(lines):
            if line.strip().startswith("* Daily Papers"):
                insert_idx = idx
                break
        lines[insert_idx:insert_idx] = ["* Hot Papers\n"]
        section_idx = insert_idx

    marker = f"<!--dpr-hot:{result.run_token}-->"
    block_idx = -1
    for idx in range(section_idx + 1, len(lines)):
        if lines[idx].startswith("* "):
            break
        if marker in lines[idx]:
            block_idx = idx
            break
    if block_idx != -1:
        end = block_idx + 1
        while end < len(lines):
            if lines[end].startswith("  * ") and not lines[end].startswith("    * "):
                break
            if lines[end].startswith("* "):
                break
            end += 1
        del lines[block_idx:end]

    title = f"热点论文 · {datetime.now(timezone.utc).strftime('%Y-%m-%d')} · {days_window}天 · {institution_filter_label(institution_filter)}"
    block = [f"  * {title} {marker}\n"]
    readme_href = f"#/hot/{result.run_token}/README"
    block.append(
        "    * "
        f'<a class="dpr-sidebar-item-link dpr-sidebar-item-structured" href="{readme_href}" '
        f'data-sidebar-item="{sidebar_payload(title, readme_href)}">结果概览</a>\n'
    )
    for index, paper in enumerate(result.papers, start=1):
        slug = paper_slug(paper, index)
        href = f"#/hot/{result.run_token}/{slug}"
        safe_title = html.escape(str(paper.get("title") or slug))
        block.append(
            "    * "
            f'<a class="dpr-sidebar-item-link dpr-sidebar-item-structured" href="{href}" '
            f'data-sidebar-item="{sidebar_payload(str(paper.get("title") or slug), href, paper)}">{safe_title}</a>\n'
        )

    lines[section_idx + 1 : section_idx + 1] = block
    sidebar_path.write_text("".join(lines), encoding="utf-8")


def write_outputs(
    result: ScoutResult,
    *,
    docs_dir: Path,
    days_window: int,
    institution_filter: str,
) -> None:
    run_dir = docs_dir / "hot" / result.run_token
    run_dir.mkdir(parents=True, exist_ok=True)
    write_readme(run_dir / "README.md", result, days_window, institution_filter)
    for index, paper in enumerate(result.papers, start=1):
        write_paper_markdown(run_dir / f"{paper_slug(paper, index)}.md", paper, index, institution_filter)
    update_hot_sidebar(docs_dir / "_sidebar.md", result, days_window, institution_filter)
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


if __name__ == "__main__":
    main()
