import importlib.util
import pathlib
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET


ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "hot_paper_scout",
    ROOT / "src" / "hot_paper_scout.py",
)
hot_paper_scout = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = hot_paper_scout
SPEC.loader.exec_module(hot_paper_scout)


def build_config() -> dict:
    return {
        "subscriptions": {
            "intent_profiles": [
                {
                    "tag": "rl-robotics",
                    "enabled": True,
                    "intent_queries": [{"query": "reinforcement learning robotics"}],
                    "keywords": [{"keyword": "robot learning", "query": "robot learning policy"}],
                }
            ]
        }
    }


def make_work(
    idx: int,
    *,
    doi=None,
    title=None,
    cited_by_count: int = 0,
    institution_name: str = "OpenAI",
    institution_type: str = "company",
    author_position: str = "first",
) -> dict:
    return {
        "id": f"https://openalex.org/W{idx}",
        "ids": {
            "openalex": f"https://openalex.org/W{idx}",
            "doi": doi or f"https://doi.org/10.1234/hot.{idx}",
        },
        "doi": doi or f"https://doi.org/10.1234/hot.{idx}",
        "display_name": title or f"Hot Paper {idx}",
        "publication_date": "2026-06-30",
        "publication_year": 2026,
        "cited_by_count": cited_by_count,
        "abstract_inverted_index": {
            "policy": [0],
            "learning": [1],
            "works": [2],
        },
        "authorships": [
            {
                "author_position": author_position,
                "author": {"display_name": f"Author {idx}"},
                "institutions": [
                    {
                        "id": f"https://openalex.org/I{idx}",
                        "display_name": institution_name,
                        "type": institution_type,
                    }
                ],
            }
        ],
        "primary_location": {
            "landing_page_url": f"https://example.org/papers/{idx}",
            "pdf_url": f"https://example.org/papers/{idx}.pdf",
        },
    }


class FakeClient:
    def __init__(self, works=None, *, exc=None):
        self.works = list(works or [])
        self.exc = exc
        self.calls = []

    def list_works(self, query, from_date, institution_filter, per_page):
        self.calls.append(("filtered", query, from_date, institution_filter, per_page))
        if self.exc:
            raise self.exc
        return self.works

    def list_unfiltered_works(self, query, from_date, per_page):
        self.calls.append(("unfiltered", query, from_date, "all", per_page))
        if self.exc:
            raise self.exc
        return self.works


class HotPaperScoutTest(unittest.TestCase):
    def test_inverted_index_and_work_parse(self):
        self.assertEqual(
            hot_paper_scout.inverted_index_to_text({"hello": [0], "world": [1]}),
            "hello world",
        )
        work = make_work(
            1,
            doi="https://doi.org/10.5555/demo",
            institution_name="Stanford University",
            institution_type="education",
        )
        parsed = hot_paper_scout.normalize_work(work, "rl-robotics", "robotics")

        self.assertEqual(parsed["abstract"], "policy learning works")
        self.assertEqual(parsed["authors"], ["Author 1"])
        self.assertEqual(parsed["doi"], "https://doi.org/10.5555/demo")
        self.assertEqual(parsed["link"], "https://example.org/papers/1")
        self.assertEqual(parsed["pdf_url"], "https://example.org/papers/1.pdf")
        self.assertEqual(parsed["institution_names"], ["Stanford University"])
        self.assertEqual(parsed["lead_institution_names"], ["Stanford University"])
        self.assertEqual(parsed["institution_types"], ["education"])

    def test_institution_filters_company_university_all(self):
        company = make_work(1, institution_name="Figure AI", institution_type="company")
        alias_company = make_work(2, institution_name="Unitree Robotics", institution_type="facility")
        generic_company = make_work(5, institution_name="OpenAI", institution_type="company")
        university = make_work(3, institution_name="Tsinghua University", institution_type="education")
        company_not_lead = make_work(4, institution_name="Tsinghua University", institution_type="education")
        company_not_lead["authorships"].append(
            {
                "author_position": "middle",
                "author": {"display_name": "Industry Coauthor"},
                "institutions": [
                    {
                        "id": "https://openalex.org/I999",
                        "display_name": "OpenAI",
                        "type": "company",
                    }
                ],
            }
        )

        self.assertTrue(hot_paper_scout.work_matches_institution_filter(company, "company"))
        self.assertTrue(hot_paper_scout.work_matches_institution_filter(alias_company, "company"))
        self.assertFalse(hot_paper_scout.work_matches_institution_filter(generic_company, "company"))
        self.assertFalse(hot_paper_scout.work_matches_institution_filter(university, "company"))
        self.assertFalse(hot_paper_scout.work_matches_institution_filter(company_not_lead, "company"))
        self.assertTrue(hot_paper_scout.work_matches_institution_filter(university, "university"))
        self.assertFalse(hot_paper_scout.work_matches_institution_filter(company, "university"))
        self.assertTrue(hot_paper_scout.work_matches_institution_filter(university, "all"))

    def test_openalex_failure_returns_warning_result(self):
        result = hot_paper_scout.scout_hot_papers(
            build_config(),
            profile_tag="rl-robotics",
            domain_query="",
            days_window=14,
            institution_filter="all",
            max_results=30,
            client=FakeClient(exc=TimeoutError("OpenAlex timed out")),
        )

        self.assertEqual(result.papers, [])
        self.assertTrue(any("OpenAlex 查询失败" in warning for warning in result.warnings))
        self.assertTrue(any("TimeoutError" in warning for warning in result.warnings))

    def test_dedupe_and_cap_to_30(self):
        works = [
            make_work(1, doi="https://doi.org/10.1234/dup", cited_by_count=5),
            make_work(2, doi="https://doi.org/10.1234/dup", cited_by_count=80),
        ]
        works.extend(make_work(idx, cited_by_count=idx) for idx in range(3, 40))
        result = hot_paper_scout.scout_hot_papers(
            build_config(),
            profile_tag="rl-robotics",
            domain_query="embodied intelligence; robot foundation model",
            days_window=14,
            institution_filter="all",
            max_results=30,
            client=FakeClient(works),
        )

        self.assertEqual(len(result.papers), 30)
        self.assertEqual(result.domain_queries, ["embodied intelligence", "robot foundation model"])
        dois = [paper["doi"] for paper in result.papers]
        self.assertEqual(dois.count("https://doi.org/10.1234/dup"), 1)
        duplicate = next(paper for paper in result.papers if paper["doi"] == "https://doi.org/10.1234/dup")
        self.assertEqual(duplicate["cited_by_count"], 80)

    def test_arxiv_fallback_entry_parse_marks_company_source(self):
        xml = """
        <entry xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
          <id>http://arxiv.org/abs/2606.12345v1</id>
          <published>2026-06-30T00:00:00Z</published>
          <title>Unitree Humanoid Robot Learning</title>
          <summary>We study embodied AI policies with Unitree robots.</summary>
          <author><name>Alice Example</name></author>
          <link href="http://arxiv.org/abs/2606.12345v1" rel="alternate" type="text/html"/>
          <link title="pdf" href="http://arxiv.org/pdf/2606.12345v1" rel="related" type="application/pdf"/>
        </entry>
        """
        entry = ET.fromstring(xml)
        paper = hot_paper_scout.arxiv_entry_to_paper(
            entry,
            'all:"Unitree" AND all:"embodied AI"',
            "2026-06-01",
            "company",
        )

        self.assertIsNotNone(paper)
        self.assertEqual(paper["source"], "arxiv_fallback")
        self.assertEqual(paper["company_match"], "unitree")
        self.assertEqual(paper["lead_institution_names"], ["unitree"])
        self.assertEqual(paper["pdf_url"], "http://arxiv.org/pdf/2606.12345v1")

    def test_hot_outputs_follow_daily_paper_format(self):
        paper = {
            "id": "http://arxiv.org/abs/2606.12345v1",
            "arxiv_id": "2606.12345v1",
            "arxiv_url": "http://arxiv.org/abs/2606.12345v1",
            "doi": "",
            "title": "Unitree Humanoid Robot Learning",
            "publication_date": "2026-06-30",
            "authors": ["Alice Example"],
            "abstract": "We study embodied AI policies with Unitree robots. The policy transfers to humanoids.",
            "link": "http://arxiv.org/abs/2606.12345v1",
            "pdf_url": "http://arxiv.org/pdf/2606.12345v1",
            "openalex_id": "",
            "cited_by_count": 0,
            "source": "arxiv_fallback",
            "profile_tag": "embodied-ai",
            "matched_query": 'all:"Unitree" AND all:"embodied AI"',
            "company_match": "unitree",
            "institution_names": ["unitree"],
            "lead_institution_names": ["unitree"],
        }
        result = hot_paper_scout.ScoutResult(
            papers=[paper],
            warnings=["OpenAlex 查询失败：demo"],
            profiles=[],
            domain_queries=["embodied AI"],
            queries=[],
            from_date="2026-06-01",
            run_token="hot-test",
        )

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = pathlib.Path(tmp)
            readme_path = tmp_path / "README.md"
            paper_path = tmp_path / "paper.md"

            hot_paper_scout.write_readme(readme_path, result, 30, "company")
            hot_paper_scout.write_paper_markdown(paper_path, paper, 1, "company")

            readme = readme_path.read_text(encoding="utf-8")
            paper_md = paper_path.read_text(encoding="utf-8")

        self.assertIn("# 日报 · 热点论文筛选", readme)
        self.assertIn("- 当次推荐总数：1", readme)
        self.assertIn("## 今日简报（AI）", readme)
        self.assertIn("## 精读区", readme)
        self.assertIn("## 速读区", readme)
        self.assertIn("使用键盘方向键可在日报/论文之间快速切换。", readme)
        self.assertNotIn("## Warning", readme)
        self.assertNotIn("## 结果", readme)
        self.assertNotIn("论文数：1", readme)

        self.assertIn("selection_source: hot_paper_scout", paper_md)
        self.assertIn("source: arxiv", paper_md)
        self.assertIn("score: 9.0", paper_md)
        self.assertIn('arxiv_id: "2606.12345v1"', paper_md)
        self.assertIn("tldr:", paper_md)
        self.assertIn("motivation:", paper_md)
        self.assertIn("method:", paper_md)
        self.assertIn("result:", paper_md)
        self.assertIn("conclusion:", paper_md)
        self.assertIn("## 摘要", paper_md)
        self.assertIn("## Abstract", paper_md)
        self.assertNotIn("## 领衔机构", paper_md)
        self.assertNotIn("## 机构", paper_md)
        self.assertNotIn("## 来源信息", paper_md)


if __name__ == "__main__":
    unittest.main()
