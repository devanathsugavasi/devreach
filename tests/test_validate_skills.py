"""Tests for scripts/validate_skills.py and scripts/check_links.py.

Run: python3 -m unittest discover -s tests
"""

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_links  # noqa: E402
import validate_skills  # noqa: E402

SECTIONS = "\n".join(
    f"## {s}\ntext\n"
    for s in ["When to Use", "Workflow", "Output Format", "Quality Checklist", "Safety", "Examples"]
)


def make_skill(root, dirname, frontmatter, body=SECTIONS):
    d = Path(root) / dirname
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(f"{frontmatter}\n# Title\n{body}", encoding="utf-8")
    return d


VALID_FM = "---\nname: good-skill\ndescription: Does a thing. Use when testing.\n---"


class ValidateSkillTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_valid_skill(self):
        d = make_skill(self.root, "good-skill", VALID_FM)
        self.assertEqual(validate_skills.validate_skill(d), [])

    def test_missing_skill_md(self):
        d = self.root / "empty"
        d.mkdir()
        self.assertEqual(validate_skills.validate_skill(d), ["missing SKILL.md"])

    def test_no_frontmatter(self):
        d = make_skill(self.root, "good-skill", "no frontmatter here")
        self.assertIn("must start with", validate_skills.validate_skill(d)[0])

    def test_unclosed_frontmatter(self):
        d = make_skill(self.root, "good-skill", "---\nname: good-skill")
        self.assertIn("not closed", validate_skills.validate_skill(d)[0])

    def test_name_mismatch(self):
        d = make_skill(self.root, "other-dir", VALID_FM)
        self.assertTrue(any("does not match" in e for e in validate_skills.validate_skill(d)))

    def test_bad_name_format(self):
        fm = "---\nname: Bad_Name\ndescription: x\n---"
        d = make_skill(self.root, "Bad_Name", fm)
        self.assertTrue(any("lowercase" in e for e in validate_skills.validate_skill(d)))

    def test_missing_description(self):
        d = make_skill(self.root, "good-skill", "---\nname: good-skill\n---")
        self.assertIn("frontmatter missing 'description'", validate_skills.validate_skill(d))

    def test_long_description(self):
        fm = f"---\nname: good-skill\ndescription: {'a' * 1025}\n---"
        d = make_skill(self.root, "good-skill", fm)
        self.assertTrue(any("longer than 1024" in e for e in validate_skills.validate_skill(d)))

    def test_angle_brackets_in_description(self):
        fm = "---\nname: good-skill\ndescription: Use <tag> here\n---"
        d = make_skill(self.root, "good-skill", fm)
        self.assertTrue(any("angle brackets" in e for e in validate_skills.validate_skill(d)))

    def test_duplicate_key(self):
        fm = "---\nname: good-skill\nname: good-skill\ndescription: x\n---"
        d = make_skill(self.root, "good-skill", fm)
        self.assertIn("duplicate", validate_skills.validate_skill(d)[0])

    def test_missing_section(self):
        body = SECTIONS.replace("## Safety", "## Notes")
        d = make_skill(self.root, "good-skill", VALID_FM, body)
        self.assertIn("missing section '## Safety'", validate_skills.validate_skill(d))

    def test_too_long(self):
        body = SECTIONS + "line\n" * 600
        d = make_skill(self.root, "good-skill", VALID_FM, body)
        self.assertTrue(any("over 500 lines" in e for e in validate_skills.validate_skill(d)))

    def test_validate_all_empty_root(self):
        self.assertEqual(list(validate_skills.validate_all(self.root).values()), [["no skills found"]])

    def test_main_exit_codes(self):
        make_skill(self.root, "good-skill", VALID_FM)
        self.assertEqual(validate_skills.main(["x", str(self.root)]), 0)
        (self.root / "broken").mkdir()
        self.assertEqual(validate_skills.main(["x", str(self.root)]), 1)


class RepoSkillsTests(unittest.TestCase):
    def test_all_repo_skills_valid(self):
        results = validate_skills.validate_all(ROOT / "skills")
        self.assertEqual(len(results), 12)
        self.assertEqual({k: v for k, v in results.items() if v}, {})


class CheckLinksTests(unittest.TestCase):
    def test_detects_broken_and_ignores_external(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "exists.md").write_text("ok", encoding="utf-8")
            (root / "README.md").write_text(
                "[a](exists.md) [b](missing.md) [c](https://x.y) [d](#anchor)\n"
                "```\n[e](in-code-block.md)\n```\n",
                encoding="utf-8",
            )
            self.assertEqual(check_links.broken_links(root), [(Path("README.md"), "missing.md")])

    def test_repo_has_no_broken_links(self):
        self.assertEqual(check_links.broken_links(ROOT), [])


if __name__ == "__main__":
    unittest.main()
