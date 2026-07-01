import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


class GenerateDocsMetaParseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[1]
        if "fitz" not in sys.modules:
            import types

            fitz_stub = types.ModuleType("fitz")
            fitz_stub.open = lambda *args, **kwargs: None
            sys.modules["fitz"] = fitz_stub
        if "llm" not in sys.modules:
            import types

            llm_stub = types.ModuleType("llm")

            class DummyDeepSeekClient:
                def __init__(self, *args, **kwargs):
                    pass

            llm_stub.DeepSeekClient = DummyDeepSeekClient
            llm_stub.resolve_max_output_tokens = lambda default=393216: default
            sys.modules["llm"] = llm_stub

        src_path = root / "src" / "6.generate_docs.py"
        spec = importlib.util.spec_from_file_location("gen6_mod", src_path)
        cls.mod = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(cls.mod)

    def test_parse_meta_from_front_matter(self):
        md_path = Path("docs/201706/12/1706.03762v1-attention-is-all-you-need.md")
        item = self.mod._parse_generated_md_to_meta(str(md_path), "pid", "quick")
        self.assertEqual(item["title_en"], "Attention Is All You Need")
        self.assertTrue(item["authors"].startswith("Ashish Vaswani"))
        self.assertIn("query:transformer", item["tags"])
        self.assertEqual(item["date"], "20170612")
        self.assertIn("https://arxiv.org/pdf", item["pdf"])
        self.assertEqual(item["selection_source"], "fresh_fetch")

    def test_parse_fallback_to_legacy_meta_lines(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "paper.md"
            path.write_text(
                "\n".join(
                    [
                        "---",
                        "selection_source: fresh_fetch",
                        "title: Legacy title",
                        "---",
                        "**Authors**: Legacy A, Legacy B",
                        "**Date**: 20260301",
                        "**PDF**: https://example.com/paper.pdf",
                        "**TLDR**: legacy tldr text",
                        "",
                        "## Abstract",
                        "abstract body",
                    ]
                ),
                encoding="utf-8",
            )
            item = self.mod._parse_generated_md_to_meta(
                str(path),
                "legacy",
                "deep",
                "cache_hint",
            )
            self.assertEqual(item["authors"], "Legacy A, Legacy B")
            self.assertEqual(item["date"], "20260301")
            self.assertEqual(item["pdf"], "https://example.com/paper.pdf")
            self.assertEqual(item["tldr"], "legacy tldr text")
            self.assertEqual(item["selection_source"], "cache_hint")

    def test_parse_source_from_front_matter(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "paper.md"
            path.write_text(
                "\n".join(
                    [
                        "---",
                        "title: Test title",
                        "source: biorxiv",
                        "selection_source: fresh_fetch",
                        "---",
                        "## Abstract",
                        "abstract body",
                    ]
                ),
                encoding="utf-8",
            )
            item = self.mod._parse_generated_md_to_meta(str(path), "pid", "quick")
            self.assertEqual(item["source"], "biorxiv")
            self.assertEqual(item["selection_source"], "fresh_fetch")

    def test_extract_sidebar_tags_hides_composite_suffix(self):
        paper = {
            "llm_score": 8.0,
            "llm_tags": [
                "query:sr:composite",
                "query:sr",
                "keyword:equation-discovery",
            ],
        }
        tags = self.mod.extract_sidebar_tags(paper)
        self.assertEqual(tags[0], ("score", "8.0"))
        self.assertIn(("query", "sr"), tags)
        self.assertIn(("query", "equation-discovery"), tags)
        self.assertNotIn(("query", "sr:composite"), tags)
        self.assertEqual(tags.count(("query", "sr")), 1)

    def test_build_markdown_content_writes_media_json_front_matter(self):
        paper = {
            "title": "Figure Test",
            "authors": ["Ada Lovelace"],
            "published": "2026-03-26T00:00:00+00:00",
            "link": "https://arxiv.org/pdf/1234.5678",
            "abstract": "abstract body",
            "source": "arxiv",
            "_figure_assets": [
                {
                    "url": "assets/figures/arxiv/1234.5678/fig-001.webp",
                    "caption": "",
                    "page": 2,
                    "index": 1,
                    "width": 1280,
                    "height": 720,
                }
            ],
            "_table_assets": [
                {
                    "url": "assets/tables/arxiv/1234.5678/table-001.webp",
                    "caption": "",
                    "page": 3,
                    "index": 1,
                    "width": 1000,
                    "height": 560,
                }
            ],
        }
        md = self.mod.build_markdown_content(paper, "quick", "", "", [])
        meta = self.mod._parse_front_matter(md)
        self.assertIn("figures_json", meta)
        self.assertIn("tables_json", meta)
        figures = json.loads(meta["figures_json"])
        tables = json.loads(meta["tables_json"])
        self.assertEqual(len(figures), 1)
        self.assertEqual(figures[0]["url"], "assets/figures/arxiv/1234.5678/fig-001.webp")
        self.assertEqual(len(tables), 1)
        self.assertEqual(tables[0]["url"], "assets/tables/arxiv/1234.5678/table-001.webp")

    def test_build_markdown_content_writes_manual_arxiv_links(self):
        paper = {
            "title": "Manual arXiv Test",
            "authors": ["Ada Lovelace"],
            "published": "2026-06-19",
            "link": "https://arxiv.org/pdf/2401.01234v2",
            "manual_pdf_url": "assets/manual-pdfs/manual-test/001.pdf",
            "arxiv_id": "2401.01234v2",
            "arxiv_url": "https://arxiv.org/abs/2401.01234v2",
            "abstract": "abstract body",
            "source": "manual",
        }
        md = self.mod.build_markdown_content(paper, "deep", "", "", [])
        meta = self.mod._parse_front_matter(md)
        self.assertEqual(meta["pdf"], "https://arxiv.org/pdf/2401.01234v2")
        self.assertEqual(meta["arxiv_id"], "2401.01234v2")
        self.assertEqual(meta["arxiv_url"], "https://arxiv.org/abs/2401.01234v2")
        self.assertEqual(meta["manual_pdf_url"], "assets/manual-pdfs/manual-test/001.pdf")

    def test_maybe_generate_paper_media_accepts_biorxiv(self):
        calls = []

        def fake_ensure_paper_media(**kwargs):
            calls.append(kwargs)
            return (
                [{"url": "assets/figures/biorxiv/pid/fig-001.webp"}],
                [{"url": "assets/tables/biorxiv/pid/table-001.webp"}],
            )

        original = self.mod.ensure_paper_media
        self.mod.ensure_paper_media = fake_ensure_paper_media
        try:
            figures, tables = self.mod.maybe_generate_paper_media(
                {
                    "id": "biorxiv-abc",
                    "source": "biorxiv",
                },
                docs_dir="docs",
                paper_id="202603/26/biorxiv-abc",
                pdf_url="https://www.biorxiv.org/content/test.full.pdf",
            )
        finally:
            self.mod.ensure_paper_media = original

        self.assertEqual(len(figures), 1)
        self.assertEqual(len(tables), 1)
        self.assertEqual(calls[0]["source_key"], "biorxiv")

    def test_maybe_generate_paper_media_accepts_manual_local_pdf(self):
        calls = []

        def fake_ensure_paper_media(**kwargs):
            calls.append(kwargs)
            return (
                [{"url": "assets/figures/manual/manual-001/fig-001.webp"}],
                [{"url": "assets/tables/manual/manual-001/table-001.webp"}],
            )

        original = self.mod.ensure_paper_media
        self.mod.ensure_paper_media = fake_ensure_paper_media
        try:
            figures, tables = self.mod.maybe_generate_paper_media(
                {
                    "id": "manual-001",
                    "source": "manual",
                    "_local_pdf_path": "/tmp/uploaded.pdf",
                },
                docs_dir="docs",
                paper_id="manual/manual-batch/manual-001",
                pdf_url="assets/manual-pdfs/manual-batch/001.pdf",
            )
        finally:
            self.mod.ensure_paper_media = original

        self.assertEqual(len(figures), 1)
        self.assertEqual(len(tables), 1)
        self.assertEqual(calls[0]["source_key"], "manual")
        self.assertEqual(calls[0]["pdf_url"], "/tmp/uploaded.pdf")
        self.assertEqual(
            calls[0]["asset_key"],
            "manual-manual-batch-manual-001",
        )

    def test_process_paper_glance_only_skips_text_and_media_generation(self):
        calls = []

        def fail_ensure_text(*args, **kwargs):
            calls.append(("text", args, kwargs))
            raise AssertionError("glance_only must not fetch or extract PDF text")

        def fail_media(*args, **kwargs):
            calls.append(("media", args, kwargs))
            raise AssertionError("glance_only must not generate figures or tables")

        def fake_glance(*args, **kwargs):
            return "\n".join(
                [
                    "**TLDR**：基于摘要生成的真实速览。 \\",
                    "**Motivation**：研究机器人策略迁移问题。 \\",
                    "**Method**：使用具身智能策略学习方法。 \\",
                    "**Result**：摘要显示策略可迁移到机器人。 \\",
                    "**Conclusion**：该工作适合后续速读评估。",
                ]
            )

        original_ensure = self.mod.ensure_text_content
        original_media = self.mod.maybe_generate_paper_media
        original_glance = self.mod.generate_glance_overview
        self.mod.ensure_text_content = fail_ensure_text
        self.mod.maybe_generate_paper_media = fail_media
        self.mod.generate_glance_overview = fake_glance
        try:
            with tempfile.TemporaryDirectory() as d:
                paper_id, _title = self.mod.process_paper(
                    {
                        "id": "2606.12345v1",
                        "title": "Unitree Humanoid Robot Learning",
                        "authors": ["Alice Example"],
                        "abstract": "We study embodied AI policies with Unitree robots.",
                        "published": "2026-06-30",
                        "link": "https://arxiv.org/pdf/2606.12345v1",
                        "source": "arxiv",
                        "selection_source": "hot_paper_scout",
                        "llm_score": 8.0,
                        "llm_tags": ["query:热点论文筛选"],
                    },
                    "quick",
                    "hot-step6-test",
                    d,
                    glance_only=True,
                    force_glance=True,
                )
                md_path = Path(d) / f"{paper_id}.md"
                txt_path = Path(d) / f"{paper_id}.txt"
                text = md_path.read_text(encoding="utf-8")
                txt_exists = txt_path.exists()
        finally:
            self.mod.ensure_text_content = original_ensure
            self.mod.maybe_generate_paper_media = original_media
            self.mod.generate_glance_overview = original_glance

        self.assertEqual(calls, [])
        self.assertIn("selection_source: hot_paper_scout", text)
        self.assertIn("motivation:", text)
        self.assertIn("## Abstract", text)
        self.assertNotIn("figures_json", text)
        self.assertFalse(txt_exists)

    def test_glance_fallback_does_not_fabricate_detail_fields(self):
        glance = self.mod.build_glance_fallback(
            {
                "abstract": "We study embodied AI policies with Unitree robots.",
                "canonical_evidence": "筛选最近 30 天内由 Unitree 相关文本命中的具身智能论文。",
            }
        )

        self.assertIn("**TLDR**", glance)
        self.assertNotIn("**Motivation**", glance)
        self.assertNotIn("**Method**", glance)
        self.assertNotIn("**Result**", glance)
        self.assertNotIn("**Conclusion**", glance)
        self.assertNotIn("方法与实现细节", glance)
        self.assertNotIn("结果与对比结论", glance)
        self.assertNotIn("适合纳入热点论文", glance)
        self.assertNotIn("总体而言", glance)

    def test_glance_retry_count_can_be_overridden_by_env(self):
        old = os.environ.get("STEP6_GLANCE_MAX_RETRIES")
        try:
            os.environ["STEP6_GLANCE_MAX_RETRIES"] = "1"
            self.assertEqual(self.mod.resolve_step6_glance_max_retries(), 1)
        finally:
            if old is None:
                os.environ.pop("STEP6_GLANCE_MAX_RETRIES", None)
            else:
                os.environ["STEP6_GLANCE_MAX_RETRIES"] = old

    def test_daily_brief_does_not_recommend_empty_deep_section(self):
        original_client = self.mod.LLM_CLIENT
        self.mod.LLM_CLIENT = None
        try:
            brief = self.mod.build_daily_brief_summary(
                "热点论文筛选 · 最近 30 天 · 具身智能公司领衔",
                [],
                [("paper-1", "Robot Foundation Model", [("score", "8.0")])],
                1,
                "success",
            )
        finally:
            self.mod.LLM_CLIENT = original_client

        self.assertIn("精读 0 篇，速读 1 篇", brief)
        self.assertIn("速读区高分论文", brief)
        self.assertNotIn("建议先看精读区", brief)

    def test_maybe_generate_paper_figures_keeps_legacy_return(self):
        original = self.mod.ensure_paper_media
        self.mod.ensure_paper_media = lambda **kwargs: (
            [{"url": "assets/figures/arxiv/pid/fig-001.webp"}],
            [{"url": "assets/tables/arxiv/pid/table-001.webp"}],
        )
        try:
            figures = self.mod.maybe_generate_paper_figures(
                {"id": "1234.5678", "source": "arxiv"},
                docs_dir="docs",
                paper_id="1234.5678",
                pdf_url="https://arxiv.org/pdf/1234.5678",
            )
        finally:
            self.mod.ensure_paper_media = original

        self.assertEqual(figures, [{"url": "assets/figures/arxiv/pid/fig-001.webp"}])

    def test_manual_upload_date_uses_manual_docs_folder(self):
        md_path, txt_path, paper_id = self.mod.prepare_paper_paths(
            "docs",
            "manual-20260618-153000",
            "Uploaded Control Paper",
            "manual-abc123",
        )
        self.assertEqual(md_path, "docs/manual/manual-20260618-153000/manual-abc123-uploaded-control-paper.md")
        self.assertEqual(txt_path, "docs/manual/manual-20260618-153000/manual-abc123-uploaded-control-paper.txt")
        self.assertEqual(paper_id, "manual/manual-20260618-153000/manual-abc123-uploaded-control-paper")
        day_dir, day_readme = self.mod.prepare_day_report_paths("docs", "manual-20260618-153000")
        self.assertEqual(day_dir, "docs/manual/manual-20260618-153000")
        self.assertEqual(day_readme, "docs/manual/manual-20260618-153000/README.md")
        self.assertEqual(self.mod.format_date_str("manual-20260618-153000"), "手动上传 · 2026-06-18 15:30")
        self.assertEqual(
            self.mod.build_day_report_href("manual-20260618-153000"),
            "/manual/manual-20260618-153000/README",
        )
        with tempfile.TemporaryDirectory() as d:
            out_path = self.mod.write_day_meta_index_json(
                d,
                "manual-20260618-153000",
                "手动上传 · 2026-06-18 15:30",
                [],
                [],
            )
            self.assertEqual(
                out_path,
                str(Path(d) / "manual" / "manual-20260618-153000" / "papers.meta.json"),
            )
            self.assertTrue(Path(out_path).exists())

    def test_ensure_text_content_prefers_local_pdf_path(self):
        with tempfile.TemporaryDirectory() as d:
            pdf_path = Path(d) / "paper.pdf"
            txt_path = Path(d) / "paper.txt"
            pdf_path.write_bytes(b"%PDF-1.4\n")
            original = self.mod.extract_pdf_text
            self.mod.extract_pdf_text = lambda path: f"local text from {Path(path).name}"
            try:
                text = self.mod.ensure_text_content("", str(txt_path), local_pdf_path=str(pdf_path))
            finally:
                self.mod.extract_pdf_text = original
            self.assertEqual(text, "local text from paper.pdf")
            self.assertEqual(txt_path.read_text(encoding="utf-8"), "local text from paper.pdf")

    def test_generate_glance_prompt_requires_richer_fields(self):
        captured = {}

        def fake_call_llm_structured_json(client, messages, **kwargs):
            captured["client"] = client
            captured["messages"] = messages
            captured["kwargs"] = kwargs
            return {
                "tldr": "这是一段足够长的中文速览摘要，用于覆盖研究背景、核心方法和主要贡献。",
                "motivation": "这是一段研究动机说明。",
                "method": "这是一段方法说明。",
                "result": "这是一段结果说明。",
                "conclusion": "这是一段结论说明。",
            }

        fallback_client = object()
        original_client = self.mod.LLM_CLIENT
        original_call = self.mod.call_llm_structured_json
        self.mod.LLM_CLIENT = fallback_client
        self.mod.call_llm_structured_json = fake_call_llm_structured_json
        try:
            out = self.mod.generate_glance_overview("Title", "Abstract")
        finally:
            self.mod.LLM_CLIENT = original_client
            self.mod.call_llm_structured_json = original_call

        self.assertIn("**TLDR**", out)
        self.assertIs(captured["client"], fallback_client)
        self.assertEqual(captured["kwargs"]["max_tokens"], 16 * 1024)
        prompt = captured["messages"][2]["content"]
        self.assertIn("150-220个中文字符", prompt)
        self.assertIn("30-70个中文字符", prompt)
        self.assertIn("问题背景→核心方法→关键结果→贡献意义", prompt)
        self.assertNotIn("每个字段一句话概括", prompt)

    def test_structured_max_tokens_env_override(self):
        old = os.environ.get("STEP6_STRUCTURED_MAX_TOKENS")
        try:
            os.environ["STEP6_STRUCTURED_MAX_TOKENS"] = "2048"
            self.assertEqual(self.mod.resolve_step6_structured_max_tokens(), 2048)
        finally:
            if old is None:
                os.environ.pop("STEP6_STRUCTURED_MAX_TOKENS", None)
            else:
                os.environ["STEP6_STRUCTURED_MAX_TOKENS"] = old

    def test_generate_glance_uses_explicit_client(self):
        explicit_client = object()
        global_client = object()
        captured = {}

        def fake_call_llm_structured_json(client, messages, **kwargs):
            captured["client"] = client
            return {
                "tldr": "这是一段足够长的中文速览摘要，用于覆盖研究背景、核心方法和主要贡献。",
                "motivation": "这是一段研究动机说明。",
                "method": "这是一段方法说明。",
                "result": "这是一段结果说明。",
                "conclusion": "这是一段结论说明。",
            }

        original_client = self.mod.LLM_CLIENT
        original_call = self.mod.call_llm_structured_json
        self.mod.LLM_CLIENT = global_client
        self.mod.call_llm_structured_json = fake_call_llm_structured_json
        try:
            out = self.mod.generate_glance_overview("Title", "Abstract", client=explicit_client)
        finally:
            self.mod.LLM_CLIENT = original_client
            self.mod.call_llm_structured_json = original_call

        self.assertIn("**TLDR**", out)
        self.assertIs(captured["client"], explicit_client)

    def test_translate_uses_16k_and_explicit_client(self):
        explicit_client = object()
        global_client = object()
        captured = {}

        def fake_call_llm_structured_json(client, messages, **kwargs):
            captured["client"] = client
            captured["kwargs"] = kwargs
            return {"title_zh": "中文标题", "abstract_zh": "中文摘要"}

        original_client = self.mod.LLM_CLIENT
        original_call = self.mod.call_llm_structured_json
        self.mod.LLM_CLIENT = global_client
        self.mod.call_llm_structured_json = fake_call_llm_structured_json
        try:
            title_zh, abstract_zh = self.mod.translate_title_and_abstract_to_zh(
                "Title",
                "Abstract",
                client=explicit_client,
            )
        finally:
            self.mod.LLM_CLIENT = original_client
            self.mod.call_llm_structured_json = original_call

        self.assertEqual(title_zh, "中文标题")
        self.assertEqual(abstract_zh, "中文摘要")
        self.assertIs(captured["client"], explicit_client)
        self.assertEqual(captured["kwargs"]["max_tokens"], 16 * 1024)


if __name__ == "__main__":
    unittest.main()
