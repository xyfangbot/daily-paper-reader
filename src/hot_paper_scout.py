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
import urllib.parse
import urllib.request
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
OPENALEX_USER_AGENT = "daily-paper-reader-hot-paper-scout/1.0"
TECH_COMPANY_ALIASES = {
    "adobe",
    "ai2",
    "allen institute for ai",
    "amazon",
    "anthropic",
    "apple",
    "baidu",
    "bytedance",
    "deepmind",
    "google",
    "huawei",
    "ibm",
    "intel",
    "meta",
    "microsoft",
    "nvidia",
    "openai",
    "qualcomm",
    "salesforce",
    "samsung",
    "sony",
    "tencent",
    "tesla",
    "xai",
}


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
        "company": "科技公司",
        "university": "高校",
    }.get(normalize_institution_filter(value), "全部机构")


def normalize_institution_type(value: Any) -> str:
    text = str(value or "").strip().lower()
    if text in {"education", "university", "college", "school"}:
        return "education"
    if text in {"company", "facility"}:
        return text
    return text


def extract_institutions(work: dict[str, Any]) -> list[dict[str, str]]:
    institutions: list[dict[str, str]] = []
    seen: set[str] = set()
    for authorship in work.get("authorships") or []:
        if not isinstance(authorship, dict):
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
            institutions.append({"id": inst_id, "name": name, "type": inst_type})
    return institutions


def text_matches_company_alias(text: str) -> bool:
    normalized = re.sub(r"[^a-z0-9]+", " ", str(text or "").lower())
    padded = f" {normalized} "
    return any(f" {alias} " in padded for alias in TECH_COMPANY_ALIASES)


def work_matches_institution_filter(work: dict[str, Any], mode: str) -> bool:
    normalized = normalize_institution_filter(mode)
    if normalized == "all":
        return True
    institutions = extract_institutions(work)
    if normalized == "university":
        return any(inst.get("type") == "education" for inst in institutions)
    if normalized == "company":
        if any(inst.get("type") == "company" for inst in institutions):
            return True
        names = " ".join(inst.get("name") or "" for inst in institutions)
        return text_matches_company_alias(names)
    return True


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
    abstract = inverted_index_to_text(work.get("abstract_inverted_index"))
    return {
        "id": openalex_id,
        "openalex_id": openalex_id,
        "doi": doi,
        "title": title,
        "authors": authors_for_work(work),
        "institutions": institutions,
        "institution_names": [inst["name"] for inst in institutions if inst.get("name")],
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


class OpenAlexClient:
    def __init__(self, timeout: int = 20, mailto: str = "") -> None:
        self.timeout = timeout
        self.mailto = mailto.strip()

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
        request = urllib.request.Request(url, headers={"User-Agent": OPENALEX_USER_AGENT})
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
        results = payload.get("results") if isinstance(payload, dict) else []
        return [item for item in results if isinstance(item, dict)]


@dataclass
class ScoutResult:
    papers: list[dict[str, Any]]
    warnings: list[str]
    profiles: list[dict[str, Any]]
    queries: list[dict[str, str]]
    from_date: str
    run_token: str


def scout_hot_papers(
    config: dict[str, Any],
    *,
    profile_tag: str,
    days_window: int,
    institution_filter: str,
    max_results: int,
    client: OpenAlexClient,
) -> ScoutResult:
    requested_tags = parse_csv(profile_tag)
    profiles = iter_profiles(config, requested_tags)
    now = datetime.now(timezone.utc)
    from_date = (now - timedelta(days=max(int(days_window or 14), 1))).strftime("%Y-%m-%d")
    tags_token = "-".join(requested_tags or [str(p.get("tag") or "all") for p in profiles[:3]]) or "all"
    token_hash = hashlib.sha1(f"{tags_token}|{days_window}|{institution_filter}|{now.isoformat()}".encode("utf-8")).hexdigest()[:8]
    run_token = f"hot-{now.strftime('%Y%m%d-%H%M%S')}-{safe_slug(tags_token, 'all')[:40]}-{token_hash}"
    warnings: list[str] = []
    query_specs: list[dict[str, str]] = []
    candidates: dict[str, dict[str, Any]] = {}
    per_page = max(25, min(100, int(max_results or 30) * 3))

    if requested_tags and not profiles:
        warnings.append(f"未找到匹配词条：{', '.join(requested_tags)}")
    if not profiles:
        warnings.append("没有可用词条，已生成空结果页。")

    mode = normalize_institution_filter(institution_filter)
    for profile in profiles:
        tag = str(profile.get("tag") or "").strip()
        queries = profile_queries(profile, limit=8)
        if not queries:
            warnings.append(f"词条 {tag} 没有可用 query，已跳过。")
            continue
        for query in queries:
            query_specs.append({"profile_tag": tag, "query": query})
            requests_to_try = [(False, mode)]
            if mode == "company":
                requests_to_try.append((True, "all"))
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

    papers = sorted(
        candidates.values(),
        key=lambda item: (int(item.get("cited_by_count") or 0), str(item.get("publication_date") or "")),
        reverse=True,
    )[: max(1, min(int(max_results or 30), 30))]
    if not papers and not warnings:
        warnings.append("OpenAlex 返回 0 篇匹配论文。")
    return ScoutResult(
        papers=papers,
        warnings=warnings,
        profiles=profiles,
        queries=query_specs,
        from_date=from_date,
        run_token=run_token,
    )


def paper_slug(paper: dict[str, Any], index: int) -> str:
    base = paper.get("doi") or paper.get("openalex_id") or paper.get("title") or f"paper-{index}"
    base = str(base).replace("https://doi.org/", "").replace("https://openalex.org/", "")
    return f"{index:03d}-{safe_slug(base, f'paper-{index}')}"


def write_paper_markdown(path: Path, paper: dict[str, Any], index: int, institution_filter: str) -> None:
    tags = [
        f"query:{paper.get('profile_tag') or 'hot'}",
        "paper:OpenAlex",
        "paper:Hot",
        f"institution:{institution_filter_label(institution_filter)}",
    ]
    abstract = str(paper.get("abstract") or "").strip()
    authors = ", ".join(paper.get("authors") or []) or "Unknown"
    source_link = paper.get("pdf_url") or paper.get("link") or paper.get("doi") or paper.get("openalex_id") or ""
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
            "source: OpenAlex Hot",
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
            "## OpenAlex 信息",
            "",
            f"- Citations: {paper.get('cited_by_count') or 0}",
            f"- Matched query: {paper.get('matched_query') or ''}",
            f"- DOI: {paper.get('doi') or ''}",
            f"- OpenAlex: {paper.get('openalex_id') or ''}",
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
        f"- 词条：{', '.join(str(p.get('tag')) for p in result.profiles) or '无'}",
        f"- 查询数：{len(result.queries)}",
        f"- 论文数：{len(result.papers)}",
        "",
    ]
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
            lines.extend(
                [
                    f"### {index}. [{title}]({slug})",
                    "",
                    f"- Citations: {cited}",
                    f"- Date: {date}",
                    f"- Authors: {authors or 'Unknown'}",
                    f"- Institutions: {institutions or 'Unknown'}",
                    f"- Query: {paper.get('matched_query') or ''}",
                    "",
                ]
            )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def sidebar_payload(title: str, href: str, paper: dict[str, Any] | None = None) -> str:
    tags = [{"kind": "paper", "label": "Hot"}, {"kind": "paper", "label": "OpenAlex"}]
    score = "-"
    evidence = ""
    link = href
    if paper:
        score = str(paper.get("cited_by_count") or 0)
        evidence = f"OpenAlex cited_by_count={score}"
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
    parser.add_argument("--days-window", type=int, choices=(7, 14), default=14)
    parser.add_argument("--institution-filter", choices=("all", "company", "university"), default="all")
    parser.add_argument("--max-results", type=int, default=30)
    parser.add_argument("--config", default=os.environ.get("DPR_CONFIG_FILE") or str(ROOT_DIR / "config.yaml"))
    parser.add_argument("--docs-dir", default=str(ROOT_DIR / "docs"))
    parser.add_argument("--openalex-timeout", type=int, default=20)
    args = parser.parse_args()

    try:
        config = load_config(Path(args.config))
    except Exception as exc:
        log(f"[WARN] config load failed: {exc}")
        config = {"subscriptions": {"intent_profiles": []}}

    client = OpenAlexClient(
        timeout=max(int(args.openalex_timeout or 20), 1),
        mailto=os.environ.get("OPENALEX_MAILTO", ""),
    )
    result = scout_hot_papers(
        config,
        profile_tag=args.profile_tag,
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
