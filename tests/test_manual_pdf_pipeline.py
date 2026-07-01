import importlib.util
import sys
import tempfile
import types
import unittest
import zipfile
from pathlib import Path


def minimal_pdf_bytes(title: str = "Example") -> bytes:
    content = f"BT /F1 12 Tf 72 120 Td ({title}) Tj ET\n".encode("ascii")
    objects = [
        b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n",
        b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n",
        (
            "3 0 obj\n"
            "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 200 200] "
            "/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>\n"
            "endobj\n"
        ).encode("ascii"),
        b"4 0 obj\n<< /Length " + str(len(content)).encode("ascii") + b" >>\nstream\n" + content + b"endstream\nendobj\n",
        b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n",
    ]
    data = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for obj in objects:
        offsets.append(len(data))
        data.extend(obj)
    xref_offset = len(data)
    data.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    data.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        data.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    data.extend(
        (
            "trailer\n"
            f"<< /Root 1 0 R /Size {len(objects) + 1} >>\n"
            "startxref\n"
            f"{xref_offset}\n"
            "%%EOF\n"
        ).encode("ascii")
    )
    return bytes(data)


class ManualPdfPipelineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import fitz  # noqa: F401
        except ModuleNotFoundError:
            fake_fitz = types.ModuleType("fitz")

            class FakePage:
                def get_text(self, _kind):
                    return "Example Paper\nAlice Example\nAbstract- uploaded paper."

            class FakeDoc:
                def __init__(self, path):
                    data = Path(path).read_bytes()
                    if not data.startswith(b"%PDF-") or b"%%EOF" not in data:
                        raise RuntimeError("cannot open fake PDF")
                    self._pages = [FakePage()]

                def __iter__(self):
                    return iter(self._pages)

                def __len__(self):
                    return len(self._pages)

                def close(self):
                    return None

            fake_fitz.open = lambda path: FakeDoc(path)
            sys.modules["fitz"] = fake_fitz

        fake_llm = types.ModuleType("llm")

        class DummyDeepSeekClient:
            pass

        fake_llm.DeepSeekClient = DummyDeepSeekClient
        sys.modules.setdefault("llm", fake_llm)

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
                zf.writestr("nested/alpha.pdf", minimal_pdf_bytes("alpha"))
                zf.writestr("beta.pdf", minimal_pdf_bytes("beta"))
                zf.writestr("notes.txt", "ignore")

            pdf_paths = self.mod.iter_pdf_paths([zip_path], root / "extract")
            self.assertEqual(len(pdf_paths), 2)
            self.assertNotEqual(pdf_paths[0], pdf_paths[1])

            old_create_client = self.mod.create_llm_client
            old_extract_text = self.mod.extract_pdf_text
            old_infer = self.mod.infer_metadata_with_llm
            old_lookup = self.mod.lookup_arxiv_id_by_title
            try:
                self.mod.create_llm_client = lambda: None
                self.mod.extract_pdf_text = lambda path: f"{path.stem}\nAlice Example\nAbstract— uploaded paper.\nI. INTRODUCTION"
                self.mod.infer_metadata_with_llm = lambda client, filename, sample_text: None
                self.mod.lookup_arxiv_id_by_title = lambda title: ""
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
                self.mod.lookup_arxiv_id_by_title = old_lookup

            self.assertEqual(len(items), 2)
            self.assertTrue(items[0]["paper_id"].startswith("manual-001-"))
            self.assertTrue(items[1]["paper_id"].startswith("manual-002-"))
            self.assertNotEqual(items[0]["paper_id"], items[1]["paper_id"])
            self.assertNotEqual(items[0]["pdf_url"], items[1]["pdf_url"])
            self.assertTrue(items[0]["pdf_url"].startswith("assets/manual-pdfs/manual-zip-test/"))
            self.assertTrue(items[1]["pdf_url"].startswith("assets/manual-pdfs/manual-zip-test/"))

    def test_zip_upload_ignores_macos_metadata_pdf_entries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            zip_path = root / "papers.zip"
            with zipfile.ZipFile(zip_path, "w") as zf:
                zf.writestr("paper.pdf", minimal_pdf_bytes("paper"))
                zf.writestr("__MACOSX/._paper.pdf", b"appledouble metadata")
                zf.writestr(".DS_Store", b"metadata")

            skipped = []
            pdf_paths = self.mod.iter_pdf_paths([zip_path], root / "extract", skipped)

            self.assertEqual(len(pdf_paths), 1)
            self.assertTrue(pdf_paths[0].name.startswith("paper-"))
            self.assertTrue(pdf_paths[0].name.endswith(".pdf"))
            self.assertEqual(len(skipped), 2)
            self.assertTrue(all(item["reason"] == self.mod.MACOS_METADATA_REASON for item in skipped))

    def test_zip_upload_counts_four_real_pdfs_not_macos_companions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            zip_path = root / "papers.zip"
            with zipfile.ZipFile(zip_path, "w") as zf:
                for index in range(4):
                    name = f"paper-{index + 1}.pdf"
                    zf.writestr(name, minimal_pdf_bytes(name))
                    zf.writestr(f"__MACOSX/._{name}", b"appledouble metadata")

            skipped = []
            pdf_paths = self.mod.iter_pdf_paths([zip_path], root / "extract", skipped)
            valid_paths = self.mod.filter_parseable_pdf_paths(pdf_paths, skipped)

            self.assertEqual(len(pdf_paths), 4)
            self.assertEqual(len(valid_paths), 4)
            self.assertEqual(len(skipped), 4)
            self.assertTrue(all(path.name.startswith("paper-") for path in valid_paths))

    def test_damaged_real_pdf_is_skipped_without_blocking_valid_pdf(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            valid_pdf = root / "valid.pdf"
            bad_pdf = root / "bad.pdf"
            valid_pdf.write_bytes(minimal_pdf_bytes("valid"))
            bad_pdf.write_bytes(b"%PDF-1.4\nnot enough structure")

            skipped = []
            valid_paths = self.mod.filter_parseable_pdf_paths([valid_pdf, bad_pdf], skipped)

            self.assertEqual(valid_paths, [valid_pdf])
            self.assertEqual(len(skipped), 1)
            self.assertEqual(skipped[0]["filename"], "bad.pdf")
            self.assertIn("PDF cannot be opened", skipped[0]["reason"])

    def test_manual_pdf_prefers_arxiv_pdf_when_id_is_detected(self):
        self.assertEqual(
            self.mod.normalize_arxiv_id("https://arxiv.org/pdf/2401.01234v2"),
            "2401.01234v2",
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pdf_path = root / "2401.01234v2-example-paper.pdf"
            pdf_path.write_bytes(minimal_pdf_bytes("example"))

            old_create_client = self.mod.create_llm_client
            old_extract_text = self.mod.extract_pdf_text
            old_infer = self.mod.infer_metadata_with_llm
            old_lookup = self.mod.lookup_arxiv_id_by_title
            try:
                self.mod.create_llm_client = lambda: None
                self.mod.extract_pdf_text = lambda path: "Example Paper\nAlice Example\nAbstract— uploaded paper."
                self.mod.infer_metadata_with_llm = lambda client, filename, sample_text: {
                    "title": "Example Paper",
                    "authors": ["Alice Example"],
                    "abstract": "uploaded paper",
                    "keywords": ["arxiv"],
                }
                self.mod.lookup_arxiv_id_by_title = lambda title: ""
                items = self.mod.build_paper_items(
                    [pdf_path],
                    batch_token="manual-arxiv-test",
                    docs_dir=root / "docs",
                    section="deep",
                    tag="手动上传",
                )
            finally:
                self.mod.create_llm_client = old_create_client
                self.mod.extract_pdf_text = old_extract_text
                self.mod.infer_metadata_with_llm = old_infer
                self.mod.lookup_arxiv_id_by_title = old_lookup

            self.assertEqual(items[0]["arxiv_id"], "2401.01234v2")
            self.assertEqual(items[0]["pdf_url"], "https://arxiv.org/pdf/2401.01234v2")
            self.assertEqual(items[0]["link"], "https://arxiv.org/pdf/2401.01234v2")
            self.assertTrue(items[0]["manual_pdf_url"].startswith("assets/manual-pdfs/manual-arxiv-test/"))
            self.assertTrue(items[0]["_local_pdf_path"].endswith(".pdf"))


if __name__ == "__main__":
    unittest.main()
