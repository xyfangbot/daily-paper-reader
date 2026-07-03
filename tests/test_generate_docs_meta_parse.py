import importlib.util
import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timezone
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

    def test_company_tags_are_exposed_for_reports(self):
        paper = {
            "llm_score": 8.0,
            "llm_tags": [
                "query:热点论文筛选",
                "query:具身智能公司相关",
                "company:unitree",
                "paper:arXiv:2606.12345v1",
            ],
        }
        tags = self.mod.extract_sidebar_tags(paper)

        self.assertIn(("company", "unitree"), tags)
        self.assertIn("公司：unitree", self.mod._format_entry_tags(tags))
        self.assertEqual(self.mod._entry_company_text(tags), "unitree")

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

    def test_process_paper_deep_hot_fallback_writes_full_glance_fields(self):
        def fake_generate_glance(*args, **kwargs):
            return None

        def fake_ensure_text(_pdf_url, txt_path, **kwargs):
            Path(txt_path).parent.mkdir(parents=True, exist_ok=True)
            Path(txt_path).write_text("full text placeholder", encoding="utf-8")

        def fake_media(*args, **kwargs):
            return [], []

        def fake_translate(*args, **kwargs):
            return "中文标题", "中文摘要"

        def fake_deep_summary(*args, **kwargs):
            return None

        original_glance = self.mod.generate_glance_overview
        original_ensure = self.mod.ensure_text_content
        original_media = self.mod.maybe_generate_paper_media
        original_translate = self.mod.translate_title_and_abstract_to_zh
        original_deep = self.mod.generate_deep_summary
        self.mod.generate_glance_overview = fake_generate_glance
        self.mod.ensure_text_content = fake_ensure_text
        self.mod.maybe_generate_paper_media = fake_media
        self.mod.translate_title_and_abstract_to_zh = fake_translate
        self.mod.generate_deep_summary = fake_deep_summary
        try:
            with tempfile.TemporaryDirectory() as d:
                paper_id, _title = self.mod.process_paper(
                    {
                        "id": "2606.54321v1",
                        "title": "Fast Loco-Manipulation for Humanoid Robots",
                        "authors": ["Alice Example"],
                        "abstract": (
                            "Robot foundation models promise generalizable control but struggle "
                            "with real-world humanoid deployment. This paper presents a fast "
                            "loco-manipulation system for Unitree G1 robots. Experiments "
                            "demonstrate robust walking and object interaction on hardware. "
                            "The results show improved adaptation under disturbances."
                        ),
                        "published": "2026-06-30",
                        "link": "https://arxiv.org/pdf/2606.54321v1",
                        "source": "arxiv",
                        "selection_source": "hot_paper_scout",
                        "llm_score": 8.0,
                        "llm_tags": ["query:热点论文筛选", "query:具身智能公司相关"],
                        "canonical_evidence": "company_relation_match=unitree; relation_source=abstract",
                    },
                    "deep",
                    "hot-step6-test",
                    d,
                    force_glance=True,
                )
                text = (Path(d) / f"{paper_id}.md").read_text(encoding="utf-8")
        finally:
            self.mod.generate_glance_overview = original_glance
            self.mod.ensure_text_content = original_ensure
            self.mod.maybe_generate_paper_media = original_media
            self.mod.translate_title_and_abstract_to_zh = original_translate
            self.mod.generate_deep_summary = original_deep

        self.assertIn("selection_source: hot_paper_scout", text)
        self.assertIn("tldr:", text)
        self.assertIn("motivation:", text)
        self.assertIn("method:", text)
        self.assertIn("result:", text)
        self.assertIn("conclusion:", text)
        self.assertIn("## 摘要", text)
        self.assertIn("## Abstract", text)
        self.assertIn("## 论文详细总结（自动生成）", text)
        self.assertIn("## 八、不足与局限", text)

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

    def test_glance_fallback_can_fill_hot_deep_detail_fields_from_abstract(self):
        glance = self.mod.build_glance_fallback(
            {
                "abstract": (
                    "Robot foundation models promise generalizable control but struggle with "
                    "real-world humanoid deployment. This paper presents a fast "
                    "loco-manipulation system for Unitree G1 robots that combines whole-body "
                    "control with policy learning. Experiments demonstrate robust walking, "
                    "recovery, and object interaction on hardware. The results show that the "
                    "system improves adaptation under disturbances."
                ),
                "canonical_evidence": "company_relation_match=unitree; relation_source=abstract",
            },
            include_detail_fields=True,
        )

        self.assertIn("**TLDR**", glance)
        self.assertIn("**Motivation**：摘要线索：Robot foundation models promise", glance)
        self.assertIn("**Method**：摘要线索：This paper presents", glance)
        self.assertIn("**Result**：摘要线索：Experiments demonstrate", glance)
        self.assertIn("**Conclusion**：摘要线索：The results show", glance)
        self.assertNotIn("Robot foundation models promise generalizable control but struggle with real-world humanoid deployment. This paper presents a fast loco-manipulation system for Unitree G1 robots that combines whole-body control with policy learning. Experiments demonstrate", glance)
        self.assertNotIn("方法与实现细节", glance)
        self.assertNotIn("结果与对比结论", glance)

    def test_sync_front_matter_glance_fields_updates_existing_page(self):
        updated, changed = self.mod.sync_front_matter_glance_fields(
            "---\ntitle: Existing Hot Paper\n---\n\n## 速览\n**TLDR**：旧内容。\n",
            "\n".join(
                [
                    "**TLDR**：新的完整速览。 \\",
                    "**Motivation**：研究动机。 \\",
                    "**Method**：方法概括。 \\",
                    "**Result**：结果概括。 \\",
                    "**Conclusion**：结论概括。",
                ]
            ),
        )

        self.assertTrue(changed)
        self.assertIn("tldr: 新的完整速览。", updated)
        self.assertIn("motivation: 研究动机。", updated)
        self.assertIn("method: 方法概括。", updated)
        self.assertIn("result: 结果概括。", updated)
        self.assertIn("conclusion: 结论概括。", updated)

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
                "热点论文筛选 · 最近 30 天 · 具身智能公司相关",
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

    def test_day_report_displays_recommend_warnings(self):
        md = self.mod.build_day_report_markdown(
            "hot-20260701-test",
            "热点论文筛选 · 最近 30 天 · 具身智能公司相关",
            [],
            [],
            True,
            [
                "OpenAlex 查询失败：具身智能 / embodied AI: HTTPError: HTTP Error 503",
                "arXiv fallback 未发现 title/abstract/first-last author affiliation 明确匹配具身智能公司或平台的论文；已拒绝 search query 本身命中，避免把检索词误当作论文证据。",
            ],
        )

        self.assertIn("## 运行提示", md)
        self.assertIn("OpenAlex 查询失败", md)
        self.assertIn("已拒绝 search query 本身命中", md)
        self.assertIn("> 本次触发没有产出可推荐论文。", md)

    def test_day_report_displays_company_per_paper(self):
        original_client = self.mod.LLM_CLIENT
        self.mod.LLM_CLIENT = None
        try:
            md = self.mod.build_day_report_markdown(
                "hot-20260701-test",
                "热点论文筛选 · 最近 30 天 · 具身智能公司相关",
                [
                    (
                        "manual/hot-20260701-test/paper",
                        "Unitree Humanoid Robot Learning",
                        [("score", "8.0"), ("company", "unitree"), ("query", "具身智能公司相关")],
                    )
                ],
                [],
                True,
            )
        finally:
            self.mod.LLM_CLIENT = original_client

        self.assertIn("## 精读区", md)
        self.assertIn("- 相关公司：unitree", md)
        self.assertIn("公司：unitree", md)
        self.assertIn("《Unitree Humanoid Robot Learning》（8.0/10，公司：unitree）", md)

    def test_hot_daily_brief_uses_deterministic_counts(self):
        original_client = self.mod.LLM_CLIENT
        self.mod.LLM_CLIENT = object()
        try:
            brief = self.mod.build_daily_brief_summary(
                "热点论文筛选 · 最近 30 天 · 具身智能公司相关 · VLA方向",
                [
                    ("paper-1", "Paper One", [("score", "8.0"), ("company", "unitree")]),
                    ("paper-2", "Paper Two", [("score", "7.0"), ("company", "physical intelligence")]),
                    ("paper-3", "Paper Three", [("score", "6.0"), ("company", "covariant")]),
                ],
                [],
                3,
                "成功",
            )
        finally:
            self.mod.LLM_CLIENT = original_client

        self.assertIn("今日共生成 3 篇推荐（精读 3 篇，速读 0 篇）", brief)
        self.assertIn("公司：unitree", brief)

    def test_deep_summary_fallback_preserves_expected_sections(self):
        summary = self.mod.build_deep_summary_fallback(
            {
                "canonical_evidence": "company_relation_match=unitree; relation_source=abstract",
                "_glance_overview": "\n".join(
                    [
                        "**TLDR**：本文研究人形机器人操作系统。 \\",
                        "**Motivation**：现有系统适应复杂任务较慢。 \\",
                        "**Method**：结合行为树和全身控制。 \\",
                        "**Result**：可部署到真实机器人。 \\",
                        "**Conclusion**：系统提升行为开发效率。",
                    ]
                ),
            },
            "Robot System",
            "This paper studies humanoid robot behavior systems.",
        )

        self.assertIn("# 论文详细中文总结", summary)
        self.assertIn("## 一、论文的核心问题与整体含义", summary)
        self.assertIn("## 八、不足与局限", summary)
        self.assertIn("基于论文摘要、速览字段与检索证据", summary)
        self.assertIn("company_relation_match=unitree", summary)
        self.assertIn("（完）", summary)

    def test_format_run_timestamp_uses_shanghai_timezone(self):
        old_tz = os.environ.get("DPR_TIMEZONE")
        os.environ["DPR_TIMEZONE"] = "Asia/Shanghai"
        try:
            text = self.mod.format_run_timestamp(datetime(2026, 7, 1, 17, 30, tzinfo=timezone.utc))
        finally:
            if old_tz is None:
                os.environ.pop("DPR_TIMEZONE", None)
            else:
                os.environ["DPR_TIMEZONE"] = old_tz

        self.assertEqual(text, "2026-07-02 01:30:00 Asia/Shanghai")

    def test_update_sidebar_links_empty_hot_run_and_prunes_old_hot_runs(self):
        with tempfile.TemporaryDirectory() as d:
            sidebar = Path(d) / "_sidebar.md"
            sidebar.write_text(
                "\n".join(
                    [
                        "* [首页](/)",
                        "* Hot Papers",
                        "  * 热点论文 · 2026-07-01 <!--dpr-hot:hot-old-legacy-->",
                        "    * [Legacy Hot](/hot/hot-old-legacy/README)",
                        "* Daily Papers",
                        "  * 旧热点 <!--dpr-date:hot-old-->",
                        "    * 速读区",
                        "      * [Wrong Paper](/manual/hot-old/wrong)",
                        "  * 2026-06-30 <!--dpr-date:20260630-->",
                        "    * [Valid Paper](/202606/30/valid)",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            self.mod.update_sidebar(
                str(sidebar),
                "hot-20260701-test",
                [],
                [],
                {},
                date_label="热点论文筛选 · 最近 30 天 · 具身智能公司相关",
            )
            text = sidebar.read_text(encoding="utf-8")

        self.assertIn("<!--dpr-date:hot-20260701-test-->", text)
        self.assertIn("[运行结果](/manual/hot-20260701-test/README)", text)
        self.assertNotIn("hot-old", text)
        self.assertNotIn("* Hot Papers", text)
        self.assertNotIn("Legacy Hot", text)
        self.assertIn("<!--dpr-date:20260630-->", text)

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
