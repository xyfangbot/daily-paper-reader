import importlib.util
import pathlib
import sys
import unittest


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
        self.assertEqual(parsed["institution_types"], ["education"])

    def test_institution_filters_company_university_all(self):
        company = make_work(1, institution_name="OpenAI", institution_type="company")
        alias_company = make_work(2, institution_name="Microsoft Research", institution_type="facility")
        university = make_work(3, institution_name="Tsinghua University", institution_type="education")

        self.assertTrue(hot_paper_scout.work_matches_institution_filter(company, "company"))
        self.assertTrue(hot_paper_scout.work_matches_institution_filter(alias_company, "company"))
        self.assertFalse(hot_paper_scout.work_matches_institution_filter(university, "company"))
        self.assertTrue(hot_paper_scout.work_matches_institution_filter(university, "university"))
        self.assertFalse(hot_paper_scout.work_matches_institution_filter(company, "university"))
        self.assertTrue(hot_paper_scout.work_matches_institution_filter(university, "all"))

    def test_openalex_failure_returns_warning_result(self):
        result = hot_paper_scout.scout_hot_papers(
            build_config(),
            profile_tag="rl-robotics",
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
            days_window=14,
            institution_filter="all",
            max_results=30,
            client=FakeClient(works),
        )

        self.assertEqual(len(result.papers), 30)
        dois = [paper["doi"] for paper in result.papers]
        self.assertEqual(dois.count("https://doi.org/10.1234/dup"), 1)
        duplicate = next(paper for paper in result.papers if paper["doi"] == "https://doi.org/10.1234/dup")
        self.assertEqual(duplicate["cited_by_count"], 80)


if __name__ == "__main__":
    unittest.main()
