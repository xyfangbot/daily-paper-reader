import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


class ManualPdfPipelineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[1]
        src_path = root / "src" / "manual_pdf_pipeline.py"
        spec = importlib.util.spec_from_file_location("manual_pdf_pipeline_mod", src_path)
        cls.mod = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(cls.mod)

    def test_ieee_front_page_metadata_fallback(self):
        text = """
VLFM: Vision-Language Frontier Maps
for Zero-Shot Semantic Navigation
Naoki Yokoyama1,2, Sehoon Ha2, Dhruv Batra2, Jiuguang Wang1, Bernadette Bucher1
Fig. 1: VLFM achieves state-of-the-art semantic Object Goal Navigation performance.
Abstract— Understanding how humans leverage semantic
knowledge to navigate unfamiliar environments and decide
where to explore next is pivotal for developing robots capable
of human-like search behaviors. We introduce a zero-shot
navigation approach, Vision-Language Frontier Maps (VLFM),
which is inspired by human reasoning and designed to navigate
towards unseen semantic objects in novel environments.
I. INTRODUCTION
How do humans navigate in novel environments?
"""
        meta = self.mod.fallback_metadata(Path("vlfm.pdf"), text)

        self.assertEqual(
            meta["title"],
            "VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation",
        )
        self.assertIn("Naoki Yokoyama", meta["authors"])
        self.assertIn("Sehoon Ha", meta["authors"])
        self.assertTrue(meta["abstract"].startswith("Understanding how humans leverage semantic knowledge"))
        self.assertNotIn("Fig. 1", meta["abstract"])

    def test_zip_upload_builds_separate_paper_items(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            zip_path = root / "papers.zip"
            with zipfile.ZipFile(zip_path, "w") as zf:
                zf.writestr("nested/alpha.pdf", b"%PDF-1.4\nalpha")
                zf.writestr("beta.pdf", b"%PDF-1.4\nbeta")
                zf.writestr("notes.txt", "ignore")

            pdf_paths = self.mod.iter_pdf_paths([zip_path], root / "extract")
            self.assertEqual(len(pdf_paths), 2)
            self.assertNotEqual(pdf_paths[0], pdf_paths[1])

            old_create_client = self.mod.create_llm_client
            old_extract_text = self.mod.extract_pdf_text
            old_infer = self.mod.infer_metadata_with_llm
            try:
                self.mod.create_llm_client = lambda: None
                self.mod.extract_pdf_text = lambda path: f"{path.stem}\nAlice Example\nAbstract— uploaded paper.\nI. INTRODUCTION"
                self.mod.infer_metadata_with_llm = lambda client, filename, sample_text: None
                items = self.mod.build_paper_items(
                    pdf_paths,
                    batch_token="manual-zip-test",
                    docs_dir=root / "docs",
                    section="deep",
                    tag="手动上传",
                )
            finally:
                self.mod.create_llm_client = old_create_client
                self.mod.extract_pdf_text = old_extract_text
                self.mod.infer_metadata_with_llm = old_infer

            self.assertEqual(len(items), 2)
            self.assertTrue(items[0]["paper_id"].startswith("manual-001-"))
            self.assertTrue(items[1]["paper_id"].startswith("manual-002-"))
            self.assertNotEqual(items[0]["paper_id"], items[1]["paper_id"])
            self.assertNotEqual(items[0]["pdf_url"], items[1]["pdf_url"])
            self.assertTrue(items[0]["pdf_url"].startswith("assets/manual-pdfs/manual-zip-test/"))
            self.assertTrue(items[1]["pdf_url"].startswith("assets/manual-pdfs/manual-zip-test/"))


if __name__ == "__main__":
    unittest.main()
