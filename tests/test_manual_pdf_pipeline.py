import importlib.util
import unittest
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


if __name__ == "__main__":
    unittest.main()
