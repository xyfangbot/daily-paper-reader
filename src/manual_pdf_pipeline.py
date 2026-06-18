#!/usr/bin/env python3
"""Manual PDF/ZIP ingestion pipeline for Daily Paper Reader."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitz

try:
    from llm import DeepSeekClient
except ModuleNotFoundError:  # pragma: no cover
    from src.llm import DeepSeekClient  # type: ignore


ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"


def log(message: str) -> None:
    print(message, flush=True)


def safe_slug(value: str, fallback: str = "paper") -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9._-]+", "-", text)
    text = text.strip("-._")
    return text or fallback


def short_hash(path: Path) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def extract_pdf_text(path: Path, max_pages: int | None = None) -> str:
    doc = fitz.open(str(path))
    parts: list[str] = []
    try:
        for idx, page in enumerate(doc):
            if max_pages is not None and idx >= max_pages:
                break
            parts.append(page.get_text("text"))
    finally:
        doc.close()
    return "\n\n".join(part for part in parts if part).strip()


def normalize_pdf_text(text: str) -> str:
    normalized = str(text or "").replace("\r", "\n")
    normalized = re.sub(r"-\n(?=[a-z])", "", normalized)
    normalized = re.sub(r"[ \t]+", " ", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def single_line(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def extract_abstract_from_text(text: str) -> str:
    normalized = normalize_pdf_text(text)
    if not normalized:
        return ""
    pattern = re.compile(
        r"\bAbstract\s*(?:[—:\-]\s*)?(.*?)(?=\n\s*(?:I\.|1\.?)\s*INTRODUCTION\b|\n\s*(?:I\.|1\.?)\s*Introduction\b|\n\s*INTRODUCTION\b|\n\s*Introduction\b|\n\s*Index Terms\b|\n\s*Keywords\b)",
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(normalized)
    if not match:
        return ""
    abstract = single_line(match.group(1))
    abstract = re.sub(r"\barXiv:\S+.*$", "", abstract, flags=re.IGNORECASE).strip()
    return abstract[:3200]


def extract_title_and_authors_from_text(path: Path, text: str) -> tuple[str, list[str]]:
    lines = [line.strip() for line in str(text or "").splitlines() if line.strip()]
    if not lines:
        return re.sub(r"[-_]+", " ", path.stem).strip() or "Uploaded PDF", []

    title_lines: list[str] = []
    for line in lines[:8]:
        if re.search(r"\bFig\.\s*\d+|^Abstract\b|^\d", line, re.IGNORECASE):
            break
        if re.search(r"[,{}@]|\b(university|institute|department|school|laboratory|lab)\b", line, re.IGNORECASE):
            break
        title_lines.append(line)
        if len(" ".join(title_lines)) >= 40 and not line.endswith(("-", ":")):
            break
    title = single_line(" ".join(title_lines)) or re.sub(r"[-_]+", " ", path.stem).strip() or "Uploaded PDF"

    authors: list[str] = []
    title_end = max(len(title_lines), 1)
    for line in lines[title_end:title_end + 6]:
        if re.search(r"\bFig\.\s*\d+|^Abstract\b", line, re.IGNORECASE):
            break
        if "@" in line or re.search(r"\b(university|institute|department|school|laboratory|lab)\b", line, re.IGNORECASE):
            continue
        cleaned = re.sub(r"\d+", "", line)
        cleaned = re.sub(r"[*†‡§]+", "", cleaned)
        candidates = [single_line(part) for part in re.split(r",| and ", cleaned) if single_line(part)]
        for candidate in candidates:
            if len(candidate) < 3 or len(candidate) > 80:
                continue
            if re.search(r"\b(Fig|Abstract|arXiv)\b", candidate, re.IGNORECASE):
                continue
            authors.append(candidate)
        if authors:
            break
    return title[:240], authors[:20]


def iter_pdf_paths(input_paths: list[Path], temp_dir: Path) -> list[Path]:
    out: list[Path] = []
    for raw in input_paths:
        path = raw.expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(path)
        if path.is_dir():
            out.extend(sorted(p for p in path.rglob("*.pdf") if p.is_file()))
            out.extend(iter_pdf_paths(sorted(p for p in path.rglob("*.zip") if p.is_file()), temp_dir))
            continue
        if path.suffix.lower() == ".pdf":
            out.append(path)
            continue
        if path.suffix.lower() == ".zip":
            extract_root = temp_dir / f"zip-{safe_slug(path.stem)}-{short_hash(path)}"
            extract_root.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(path) as zf:
                for info in zf.infolist():
                    if info.is_dir() or not info.filename.lower().endswith(".pdf"):
                        continue
                    name = Path(info.filename).name
                    if not name:
                        continue
                    target = extract_root / f"{safe_slug(Path(name).stem)}-{hashlib.sha1(info.filename.encode('utf-8')).hexdigest()[:8]}.pdf"
                    with zf.open(info) as src, target.open("wb") as dst:
                        shutil.copyfileobj(src, dst)
                    out.append(target)
            continue
        log(f"[WARN] 跳过非 PDF/ZIP 文件：{path}")
    seen: set[str] = set()
    unique: list[Path] = []
    for path in out:
        key = str(path.resolve())
        if key in seen:
            continue
        seen.add(key)
        unique.append(path)
    return unique


def create_llm_client() -> DeepSeekClient | None:
    api_key = os.getenv("SUMMARY_API_KEY") or os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        return None
    model = os.getenv("SUMMARY_MODEL") or os.getenv("DEEPSEEK_MODEL") or "deepseek-v4-flash"
    base_url = os.getenv("SUMMARY_BASE_URL") or os.getenv("DEEPSEEK_BASE_URL") or "https://api.deepseek.com"
    return DeepSeekClient(api_key=api_key, model=model, base_url=base_url)


def infer_metadata_with_llm(client: DeepSeekClient | None, filename: str, sample_text: str) -> dict[str, Any] | None:
    if client is None or not sample_text.strip():
        return None
    schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "authors": {"type": "array", "items": {"type": "string"}},
            "abstract": {"type": "string"},
            "keywords": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["title", "authors", "abstract", "keywords"],
        "additionalProperties": False,
    }
    messages = [
        {
            "role": "system",
            "content": "You extract faithful paper metadata from PDF text. Return only information present or strongly implied by the text.",
        },
        {
            "role": "user",
            "content": json.dumps(
                {
                    "filename": filename,
                    "pdf_text_sample": sample_text[:24000],
                },
                ensure_ascii=False,
            ),
        },
        {
            "role": "user",
            "content": (
                "Extract the paper title, authors, abstract, and 3-8 short research keywords. "
                "If authors or abstract are unclear, return the best concise fallback based on the text."
            ),
        },
    ]
    try:
        resp = client.chat_structured(
            messages=messages,
            schema_name="manual_pdf_metadata",
            schema=schema,
            strict=True,
            allow_json_object_fallback=True,
        )
        parsed = resp.get("parsed")
        return parsed if isinstance(parsed, dict) else None
    except Exception as exc:
        log(f"[WARN] LLM 元数据提取失败，将使用文件名兜底：{filename}: {exc}")
        return None


def fallback_metadata(path: Path, text: str) -> dict[str, Any]:
    title, authors = extract_title_and_authors_from_text(path, text)
    first_lines = [line.strip() for line in text.splitlines() if line.strip()]
    abstract = extract_abstract_from_text(text)
    if not abstract:
        abstract = " ".join(first_lines[:8])[:1800] if first_lines else "This PDF was uploaded manually and no abstract could be extracted."
    return {
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "keywords": ["manual upload", "pdf"],
    }


def normalize_metadata(path: Path, text: str, inferred: dict[str, Any] | None) -> dict[str, Any]:
    fallback = fallback_metadata(path, text)
    data = inferred if isinstance(inferred, dict) else {}
    title = str(data.get("title") or "").strip() or fallback["title"]
    abstract = str(data.get("abstract") or "").strip() or fallback["abstract"]
    authors_raw = data.get("authors")
    authors = [str(x).strip() for x in authors_raw if str(x).strip()] if isinstance(authors_raw, list) else []
    if not authors:
        authors = list(fallback.get("authors") or [])
    keywords_raw = data.get("keywords")
    keywords = [str(x).strip() for x in keywords_raw if str(x).strip()] if isinstance(keywords_raw, list) else []
    if not keywords:
        keywords = fallback["keywords"]
    return {
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "keywords": keywords[:8],
    }


def build_paper_items(
    pdf_paths: list[Path],
    *,
    batch_token: str,
    docs_dir: Path,
    section: str,
    tag: str,
) -> list[dict[str, Any]]:
    asset_dir = docs_dir / "assets" / "manual-pdfs" / batch_token
    asset_dir.mkdir(parents=True, exist_ok=True)
    client = create_llm_client()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    papers: list[dict[str, Any]] = []
    for index, pdf_path in enumerate(pdf_paths, start=1):
        digest = short_hash(pdf_path)
        safe_name = f"{index:03d}-{safe_slug(pdf_path.stem)}-{digest}.pdf"
        copied_pdf = asset_dir / safe_name
        shutil.copy2(pdf_path, copied_pdf)
        relative_pdf = copied_pdf.relative_to(docs_dir).as_posix()
        text = extract_pdf_text(pdf_path)
        inferred = infer_metadata_with_llm(client, pdf_path.name, text)
        meta = normalize_metadata(pdf_path, text, inferred)
        paper_id = f"manual-{index:03d}-{digest}"
        tags = [f"query:{tag or '手动上传'}", "paper:PDF"]
        tags.extend(f"query:{kw}" for kw in meta["keywords"][:5] if kw)
        item = {
            "id": paper_id,
            "paper_id": paper_id,
            "title": meta["title"],
            "authors": meta["authors"],
            "abstract": meta["abstract"],
            "published": today,
            "link": relative_pdf,
            "pdf_url": relative_pdf,
            "source": "manual",
            "selection_source": "manual_upload",
            "llm_score": 10.0,
            "canonical_evidence": "用户手动上传 PDF",
            "llm_tldr_cn": "",
            "llm_tags": tags,
            "_local_pdf_path": str(copied_pdf),
            "_original_filename": pdf_path.name,
        }
        papers.append(item)
        log(f"[OK] PDF queued: {pdf_path.name} -> {paper_id} ({section})")
    return papers


def write_recommend_file(batch_token: str, papers: list[dict[str, Any]], section: str) -> Path:
    recommend_dir = ROOT_DIR / "archive" / batch_token / "recommend"
    recommend_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "manual_pdf_upload",
        "deep_dive": papers if section == "deep" else [],
        "quick_skim": papers if section == "quick" else [],
    }
    path = recommend_dir / f"arxiv_papers_{batch_token}.standard.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def snapshot_paths(paths: list[Path], snapshot_root: Path) -> list[tuple[Path, Path, bool]]:
    snapshot_root.mkdir(parents=True, exist_ok=True)
    snapshots: list[tuple[Path, Path, bool]] = []
    for index, path in enumerate(paths):
        backup = snapshot_root / f"{index:02d}-{safe_slug(path.name, 'path')}"
        exists = path.exists()
        snapshots.append((path, backup, exists))
        if not exists:
            continue
        if path.is_dir():
            shutil.copytree(path, backup)
        else:
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, backup)
    return snapshots


def restore_paths(snapshots: list[tuple[Path, Path, bool]]) -> None:
    for path, backup, existed in reversed(snapshots):
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
        if not existed:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        if backup.is_dir():
            shutil.copytree(backup, path)
        elif backup.exists():
            shutil.copy2(backup, path)


def find_manual_media_paths(docs_dir: Path, batch_token: str) -> list[Path]:
    token = safe_slug(batch_token, "manual")
    out: list[Path] = []
    for base in [
        docs_dir / "assets" / "figures" / "manual",
        docs_dir / "assets" / "tables" / "manual",
    ]:
        if not base.exists():
            continue
        out.extend(sorted(p for p in base.glob(f"*{token}*") if p.exists()))
    return out


def cleanup_manual_media_for_batch(docs_dir: Path, batch_token: str) -> None:
    for path in find_manual_media_paths(docs_dir, batch_token):
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()


def run_step6(batch_token: str, label: str, docs_dir: Path, docs_concurrency: int) -> None:
    cmd = [
        sys.executable,
        str(SRC_DIR / "6.generate_docs.py"),
        "--date",
        batch_token,
        "--mode",
        "standard",
        "--docs-dir",
        str(docs_dir),
        "--sidebar-date-label",
        label,
        "--docs-concurrency",
        str(max(int(docs_concurrency or 1), 1)),
        "--force-glance",
    ]
    log(f"[INFO] Step6: {' '.join(cmd)}")
    subprocess.run(cmd, cwd=str(ROOT_DIR), check=True)


def validate_generated_docs(batch_token: str, docs_dir: Path, section: str, require_quality: bool) -> None:
    if not require_quality or section != "deep":
        return
    batch_dir = docs_dir / "manual" / batch_token
    md_paths = sorted(p for p in batch_dir.glob("*.md") if p.name != "README.md")
    if not md_paths:
        raise RuntimeError(f"严格质量检查失败：未生成论文 Markdown：{batch_dir}")
    failures: list[str] = []
    for md_path in md_paths:
        text = md_path.read_text(encoding="utf-8")
        checks = [
            ("中文摘要", "## 摘要" in text),
            ("详细总结", "## 论文详细总结（自动生成）" in text),
            ("完整结束标记", "（完）" in text),
            ("作者", "authors: Unknown" not in text),
        ]
        missing = [name for name, ok in checks if not ok]
        if missing:
            failures.append(f"{md_path.name}: 缺少 {', '.join(missing)}")
    if failures:
        joined = "\n".join(failures)
        raise RuntimeError(
            "严格质量检查失败：手动上传精读页没有达到每日精读区标准。\n"
            f"{joined}\n"
            "请检查 SUMMARY_API_KEY/DEEPSEEK_API_KEY、SUMMARY_BASE_URL/DEEPSEEK_BASE_URL 与网络连通性。"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse uploaded PDFs/ZIPs and generate DPR docs.")
    parser.add_argument("--input", action="append", required=True, help="PDF, ZIP, or directory path. Repeatable.")
    parser.add_argument("--batch-token", default="", help="Unique batch token. Default: manual-YYYYMMDD-HHMMSS.")
    parser.add_argument("--label", default="", help="Sidebar/report label.")
    parser.add_argument("--section", choices=("deep", "quick"), default="deep", help="Output section.")
    parser.add_argument("--tag", default="手动上传", help="Query tag shown in cards/sidebar.")
    parser.add_argument("--docs-dir", default=str(ROOT_DIR / "docs"))
    parser.add_argument("--docs-concurrency", type=int, default=2)
    parser.add_argument(
        "--require-quality",
        action="store_true",
        help="精读区必须生成中文摘要、完整详细总结和作者信息，否则返回失败。",
    )
    args = parser.parse_args()

    batch_token = (args.batch_token or "").strip()
    if not batch_token:
        batch_token = "manual-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    batch_token = safe_slug(batch_token, "manual")
    label = (args.label or "").strip() or f"{batch_token}"
    docs_dir = Path(args.docs_dir).expanduser()
    if not docs_dir.is_absolute():
        docs_dir = ROOT_DIR / docs_dir

    with tempfile.TemporaryDirectory(prefix="dpr-manual-pdf-") as temp:
        temp_dir = Path(temp)
        protected_paths = [
            docs_dir / "README.md",
            docs_dir / "_sidebar.md",
            docs_dir / "manual" / batch_token,
            docs_dir / "assets" / "manual-pdfs" / batch_token,
            ROOT_DIR / "archive" / batch_token,
        ]
        protected_paths.extend(find_manual_media_paths(docs_dir, batch_token))
        snapshots = snapshot_paths(protected_paths, temp_dir / "snapshots")
        try:
            pdf_paths = iter_pdf_paths([Path(p) for p in args.input], temp_dir)
            if not pdf_paths:
                raise RuntimeError("未找到可解析的 PDF 文件。")
            log(f"[INFO] Found {len(pdf_paths)} PDF(s). batch={batch_token}")
            papers = build_paper_items(
                pdf_paths,
                batch_token=batch_token,
                docs_dir=docs_dir,
                section=args.section,
                tag=args.tag,
            )
            recommend_path = write_recommend_file(batch_token, papers, args.section)
            log(f"[OK] recommend saved: {recommend_path}")
            run_step6(batch_token, label, docs_dir, args.docs_concurrency)
            validate_generated_docs(batch_token, docs_dir, args.section, args.require_quality)
        except Exception:
            cleanup_manual_media_for_batch(docs_dir, batch_token)
            restore_paths(snapshots)
            raise
        log("[OK] manual PDF docs generated.")


if __name__ == "__main__":
    main()
