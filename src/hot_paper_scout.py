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
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

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
DEFAULT_UI_DOMAIN_QUERY = (
    "embodied intelligence; embodied AI; embodied agents; "
    "vision-language-action model; robot foundation model"
)
TOPIC_DIRECTION_LABELS = {
    "all": "综合方向",
    "vln": "VLN方向",
    "vla": "VLA方向",
    "world-model": "世界模型方向",
}
TOPIC_DIRECTION_QUERIES = {
    "vln": [
        "vision language navigation robot",
        "VLN embodied navigation",
        "language guided robot navigation",
        "zero-shot semantic navigation robot",
        "visual language navigation embodied AI",
    ],
    "vla": [
        "vision-language-action model robot",
        "VLA model robot policy",
        "generalist robot policy vision language action",
        "robot foundation model action prediction",
        "multimodal robot manipulation policy",
    ],
    "world-model": [
        "robot world model",
        "embodied world model",
        "predictive world model robotics",
        "spatial world model robot learning",
        "generative world model embodied AI",
    ],
}
RETRYABLE_HTTP_STATUS = {429, 500, 502, 503, 504}
EMBODIED_AI_COMPANY_ALIASES = {
    "1x technologies",
    "agibot",
    "agility robotics",
    "agile robots",
    "alibaba",
    "alibaba cloud",
    "alibaba group",
    "amazon",
    "amazon robotics",
    "amazon science",
    "apptronik",
    "apple",
    "baidu",
    "baidu research",
    "boston dynamics",
    "bytedance",
    "covariant",
    "deepmind",
    "engineai",
    "everyday robots",
    "facebook ai research",
    "field ai",
    "figure ai",
    "fourier intelligence",
    "galbot",
    "google deepmind",
    "google research",
    "google robotics",
    "huawei",
    "huawei noah",
    "huawei noah's ark lab",
    "intrinsic ai",
    "meta ai",
    "microsoft",
    "microsoft research",
    "nvidia",
    "nvidia research",
    "openai",
    "physical intelligence",
    "qwen",
    "qwen team",
    "sanctuary ai",
    "skild",
    "skild ai",
    "tesla",
    "tesla bot",
    "tencent",
    "tencent ai lab",
    "ubtech",
    "unitree",
    "unitree robotics",
    "xiaomi robotics",
    "xpeng robotics",
    "zhiyuan robotics",
}
ARXIV_COMPANY_QUERY_NAMES = [
    "Alibaba",
    "Alibaba Cloud",
    "Qwen",
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
    "Microsoft Research",
    "Meta AI",
    "OpenAI",
    "Baidu",
    "Huawei",
    "Tencent",
    "ByteDance",
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
EMBODIED_AI_SIGNAL_RE = re.compile(
    r"\b("
    r"robot|robotic|robotics|humanoid|quadruped|locomotion|manipulation|manipulator|"
    r"embodied|physical ai|vision language action|vision-language-action|vla|"
    r"navigation|autonomous driving|autonomous vehicle|self driving|world model"
    r")\b",
    flags=re.IGNORECASE,
)
BRANDED_COMPANY_TITLE_PATTERNS = [
    (
        re.compile(
            r"(?:^|\b)qwen[\w.-]*(?:\b.*\btechnical report\b|[-:]\s*robot\w*)",
            flags=re.IGNORECASE,
        ),
        "alibaba group",
    ),
]


def run_timezone_name() -> str:
    return (os.getenv("DPR_TIMEZONE") or "Asia/Shanghai").strip() or "Asia/Shanghai"


def run_timezone() -> timezone | ZoneInfo:
    try:
        return ZoneInfo(run_timezone_name())
    except ZoneInfoNotFoundError:
        return timezone.utc


def run_now() -> datetime:
    return datetime.now(timezone.utc).astimezone(run_timezone())


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


def normalize_topic_directions(value: str) -> list[str]:
    aliases = {
        "all": "all",
        "general": "all",
        "default": "all",
        "综合": "all",
        "综合方向": "all",
        "vln": "vln",
        "vision-language-navigation": "vln",
        "vision-language navigation": "vln",
        "visual-language-navigation": "vln",
        "视觉语言导航": "vln",
        "导航": "vln",
        "vla": "vla",
        "vision-language-action": "vla",
        "vision-language action": "vla",
        "视觉语言动作": "vla",
        "world-model": "world-model",
        "world model": "world-model",
        "worldmodel": "world-model",
        "wm": "world-model",
        "世界模型": "world-model",
    }
    selected: list[str] = []
    seen: set[str] = set()
    for raw in re.split(r"[\n;,，；]+", str(value or "")):
        item = single_line(raw).lower().replace("_", "-")
        item = re.sub(r"\s+", " ", item)
        key = aliases.get(item) or aliases.get(item.replace(" ", "-"))
        if not key or key in seen:
            continue
        seen.add(key)
        selected.append(key)
    if not selected:
        return ["all"]
    if "all" in seen and len(selected) > 1:
        selected = [item for item in selected if item != "all"]
    return selected or ["all"]


def topic_direction_label(value: str) -> str:
    return "、".join(TOPIC_DIRECTION_LABELS.get(item, item) for item in normalize_topic_directions(value))


def is_default_domain_query(value: str) -> bool:
    raw = [item.lower() for item in parse_query_list(value)]
    defaults = [
        [item.lower() for item in parse_query_list(DEFAULT_DOMAIN_QUERY)],
        [item.lower() for item in parse_query_list(DEFAULT_UI_DOMAIN_QUERY)],
    ]
    return raw in defaults


def build_domain_query_groups(domain_query: str, topic_direction: str) -> tuple[list[tuple[str, list[str]]], list[str], list[str]]:
    directions = normalize_topic_directions(topic_direction)
    custom_queries = parse_query_list(domain_query)
    use_direction_queries = any(item != "all" for item in directions)
    groups: list[tuple[str, list[str]]] = []
    all_queries: list[str] = []
    seen: set[str] = set()

    def add_group(label: str, queries: list[str]) -> None:
        group_queries: list[str] = []
        for query in queries:
            clean = single_line(query)
            key = clean.lower()
            if not clean or key in seen:
                continue
            seen.add(key)
            group_queries.append(clean)
            all_queries.append(clean)
        if group_queries:
            groups.append((label, group_queries))

    if use_direction_queries:
        for direction in directions:
            if direction == "all":
                continue
            add_group(TOPIC_DIRECTION_LABELS.get(direction, direction), TOPIC_DIRECTION_QUERIES.get(direction, []))
        if custom_queries and not is_default_domain_query(domain_query):
            add_group("自定义方向", custom_queries[:8])
    else:
        add_group("综合方向", custom_queries[:8])
    return groups, all_queries, directions


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


def normalize_alias_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(text or "").lower()).strip()


def text_matches_embodied_ai_company_alias(text: str) -> bool:
    padded = f" {normalize_alias_text(text)} "
    return any(f" {normalize_alias_text(alias)} " in padded for alias in EMBODIED_AI_COMPANY_ALIASES)


def matched_embodied_ai_company_name(text: str) -> str:
    padded = f" {normalize_alias_text(text)} "
    for alias in sorted(EMBODIED_AI_COMPANY_ALIASES, key=lambda item: len(normalize_alias_text(item)), reverse=True):
        normalized_alias = normalize_alias_text(alias)
        if normalized_alias and f" {normalized_alias} " in padded:
            return normalized_alias
    return ""


def company_name_from_institutions(institutions: list[dict[str, str]]) -> str:
    for inst in institutions:
        name = single_line(inst.get("name") or "")
        if not name:
            continue
        match = matched_embodied_ai_company_name(name)
        if match:
            return match
    return ""


def weak_company_mention_for_work(work: dict[str, Any]) -> tuple[str, str]:
    title = single_line(str(work.get("display_name") or ""))
    match = matched_embodied_ai_company_name(title)
    if match:
        return match, "title"

    abstract = inverted_index_to_text(work.get("abstract_inverted_index"))
    match = matched_embodied_ai_company_name(abstract)
    if match:
        return match, "abstract"
    return "", ""


def branded_company_from_title(title: str) -> str:
    text = single_line(title)
    for pattern, company in BRANDED_COMPANY_TITLE_PATTERNS:
        if pattern.search(text):
            return company
    return ""


def text_has_embodied_ai_signal(text: str) -> bool:
    return bool(EMBODIED_AI_SIGNAL_RE.search(str(text or "")))


def work_has_embodied_ai_signal(work: dict[str, Any]) -> bool:
    title = single_line(str(work.get("display_name") or ""))
    abstract = inverted_index_to_text(work.get("abstract_inverted_index"))
    return text_has_embodied_ai_signal(f"{title} {abstract}")


def arxiv_entry_has_embodied_ai_signal(title: str, abstract: str) -> bool:
    return text_has_embodied_ai_signal(f"{title} {abstract}")


def work_company_relation(work: dict[str, Any]) -> tuple[str, str]:
    lead_institutions = extract_institutions(work, lead_only=True)
    match = company_name_from_institutions(lead_institutions)
    if match:
        return match, "lead-affiliation"

    institutions = extract_institutions(work)
    match = company_name_from_institutions(institutions)
    if match:
        return match, "affiliation"

    match = branded_company_from_title(str(work.get("display_name") or ""))
    if match:
        return match, "branded-title"

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


def candidate_keys_for_paper(item: dict[str, Any]) -> list[str]:
    keys: list[str] = []

    def add(value: str) -> None:
        if value and value not in keys:
            keys.append(value)

    doi = str(item.get("doi") or "").strip().lower()
    if doi:
        add(f"doi:{doi}")
    arxiv_id = str(item.get("arxiv_id") or "").strip().lower()
    if arxiv_id:
        add(f"arxiv:{arxiv_id}")
    title_key = normalize_alias_text(str(item.get("title") or item.get("display_name") or ""))
    if title_key:
        add(f"title:{title_key}")
    fallback_id = str(item.get("openalex_id") or item.get("id") or "").strip().lower()
    if fallback_id:
        add(f"id:{fallback_id}")
    return keys


def paper_rank_tuple(item: dict[str, Any]) -> tuple[int, str]:
    return int(item.get("cited_by_count") or 0), str(item.get("publication_date") or "")


def upsert_candidate(
    candidates: dict[str, dict[str, Any]],
    candidate_aliases: dict[str, str],
    item: dict[str, Any],
) -> None:
    keys = candidate_keys_for_paper(item)
    if not keys:
        return
    primary_key = next((candidate_aliases[key] for key in keys if key in candidate_aliases), keys[0])

    for key in keys:
        other_key = candidate_aliases.get(key)
        if not other_key or other_key == primary_key:
            continue
        other_item = candidates.pop(other_key, None)
        if other_item and (primary_key not in candidates or paper_rank_tuple(other_item) > paper_rank_tuple(candidates[primary_key])):
            candidates[primary_key] = other_item
        for alias, mapped_key in list(candidate_aliases.items()):
            if mapped_key == other_key:
                candidate_aliases[alias] = primary_key

    existing = candidates.get(primary_key)
    if existing is None or paper_rank_tuple(item) > paper_rank_tuple(existing):
        candidates[primary_key] = item
    for key in keys:
        candidate_aliases[key] = primary_key


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
    company_mention, company_mention_source = weak_company_mention_for_work(work)
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
        "company_mention": company_mention,
        "company_mention_source": company_mention_source,
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


def arxiv_affiliation_company_match(author_records: list[dict[str, str]]) -> str:
    affiliation_text = " ".join(record.get("affiliation") or "" for record in author_records)
    return matched_embodied_ai_company_name(affiliation_text)


def arxiv_weak_company_mention(title: str, abstract: str) -> tuple[str, str]:
    match = matched_embodied_ai_company_name(title)
    if match:
        return match, "title"
    match = matched_embodied_ai_company_name(abstract)
    if match:
        return match, "abstract"
    return "", ""


def arxiv_company_relation(title: str, abstract: str, author_records: list[dict[str, str]]) -> tuple[str, str]:
    match = arxiv_lead_affiliation_company_match(author_records)
    if match:
        return match, "lead-affiliation"
    match = arxiv_affiliation_company_match(author_records)
    if match:
        return match, "affiliation"
    match = branded_company_from_title(title)
    if match:
        return match, "branded-title"
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
    company_mention, company_mention_source = arxiv_weak_company_mention(title, abstract)
    if mode == "company":
        # Query/title/abstract product mentions are not authorship evidence.
        # Accept arXiv fallback items only when author affiliation names a
        # company/lab, or when the title matches a narrow company-branded
        # technical-report pattern such as Qwen-Robot*.
        if not matched_company:
            return None
        if not arxiv_entry_has_embodied_ai_signal(title, abstract):
            return None
    company_label = matched_company or "arXiv metadata"
    inferred_institutions = [{"id": "", "name": company_label, "type": "company", "author_position": "inferred"}] if matched_company else []
    inferred_lead_institutions = inferred_institutions if relation_source == "lead-affiliation" else []
    return {
        "id": entry_id,
        "arxiv_id": arxiv_id,
        "arxiv_url": entry_id,
        "openalex_id": "",
        "doi": doi,
        "title": title or "Untitled arXiv work",
        "authors": authors[:20],
        "institutions": inferred_institutions,
        "lead_institutions": inferred_lead_institutions,
        "institution_names": [company_label] if matched_company else [],
        "lead_institution_names": [company_label] if inferred_lead_institutions else [],
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
        "company_mention": company_mention,
        "company_mention_source": company_mention_source,
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
    paper_aliases: dict[str, str] = {}
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
            upsert_candidate(papers, paper_aliases, paper)
        if len(company_batches) > 1:
            time.sleep(3.0)
    if mode == "company" and not papers:
        warnings.append(
            "arXiv fallback 未发现作者 affiliation 或公司品牌技术报告标题明确匹配公司的论文；"
            "已拒绝 search query/title/abstract 的普通公司名命中，避免把设备、产品或检索词误当作公司产出证据。"
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
    topic_directions: list[str]
    queries: list[dict[str, str]]
    from_date: str
    run_token: str


def scout_hot_papers(
    config: dict[str, Any],
    *,
    profile_tag: str,
    domain_query: str,
    topic_direction: str,
    days_window: int,
    institution_filter: str,
    max_results: int,
    client: OpenAlexClient,
) -> ScoutResult:
    requested_tags = parse_csv(profile_tag)
    domain_query_groups, domain_queries, topic_directions = build_domain_query_groups(domain_query, topic_direction)
    profiles = iter_profiles(config, requested_tags) if requested_tags or not domain_queries else []
    now = run_now()
    from_date = (now - timedelta(days=max(int(days_window or 30), 1))).strftime("%Y-%m-%d")
    domain_token = safe_slug("-".join(domain_queries[:2]), "domain")[:40]
    tags_token = "-".join(requested_tags or [str(p.get("tag") or "all") for p in profiles[:3]]) or domain_token or "all"
    if not requested_tags and not profiles and any(item != "all" for item in topic_directions):
        tags_token = "-".join(topic_directions)
    token_hash = hashlib.sha1(f"{tags_token}|{domain_query}|{topic_direction}|{days_window}|{institution_filter}|{now.isoformat()}".encode("utf-8")).hexdigest()[:8]
    run_token = f"hot-{now.strftime('%Y%m%d-%H%M%S')}-{safe_slug(tags_token, 'all')[:40]}-{token_hash}"
    warnings: list[str] = []
    query_specs: list[dict[str, str]] = []
    candidates: dict[str, dict[str, Any]] = {}
    candidate_aliases: dict[str, str] = {}
    per_page = max(25, min(100, int(max_results or 30) * 3))

    if requested_tags and not profiles:
        warnings.append(f"未找到匹配词条：{', '.join(requested_tags)}")
    if not profiles and not domain_queries:
        warnings.append("没有可用词条，已生成空结果页。")

    mode = normalize_institution_filter(institution_filter)
    query_groups: list[tuple[str, list[str]]] = []
    query_groups.extend(domain_query_groups)
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
                    if mode == "company" and not work_has_embodied_ai_signal(work):
                        continue
                    if not work_matches_institution_filter(work, mode):
                        continue
                    item = normalize_work(work, tag, query)
                    upsert_candidate(candidates, candidate_aliases, item)
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
                "公司相关模式仅接受作者 affiliation 或公司品牌技术报告标题明确匹配公司的条目。"
            )
        for item in fallback_papers:
            upsert_candidate(candidates, candidate_aliases, item)

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
        topic_directions=topic_directions,
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
            "company_mention": paper.get("company_mention") or "",
            "company_mention_source": paper.get("company_mention_source") or "",
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
        "generated_at": run_now().isoformat(),
        "source": "hot_paper_scout",
        "run_token": result.run_token,
        "from_date": result.from_date,
        "days_window": days_window,
        "institution_filter": normalize_institution_filter(institution_filter),
        "profiles": [p.get("tag") for p in result.profiles],
        "domain_queries": result.domain_queries,
        "topic_directions": result.topic_directions,
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
    archive_dir = ROOT_DIR / "archive" / run_now().strftime("%Y%m%d") / "hot"
    archive_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": run_now().isoformat(),
        "run_token": result.run_token,
        "from_date": result.from_date,
        "days_window": days_window,
        "institution_filter": normalize_institution_filter(institution_filter),
        "profiles": [p.get("tag") for p in result.profiles],
        "domain_queries": result.domain_queries,
        "topic_directions": result.topic_directions,
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
    parser.add_argument("--topic-direction", default="all", help="Comma-separated topic directions: all, vln, vla, world-model.")
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
        topic_direction=args.topic_direction,
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
