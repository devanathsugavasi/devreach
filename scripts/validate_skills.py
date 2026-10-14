#!/usr/bin/env python3
"""Validate DevReach skill directories.

Checks every directory under skills/ for:
  - a SKILL.md file
  - YAML frontmatter with `name` and `description`
  - `name` matching the directory, lowercase-hyphenated, <= 64 chars
  - `description` non-empty, <= 1024 chars, no angle brackets
  - the section headings every DevReach skill must have
  - SKILL.md under 500 lines (keep long material in references/)

Usage: python3 scripts/validate_skills.py [skills_dir]
Exits 1 if any skill has errors. Standard library only.
"""

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_LINES = 500
REQUIRED_SECTIONS = [
    "When to Use",
    "Workflow",
    "Output Format",
    "Quality Checklist",
    "Safety",
    "Example",  # prefix match, so "Examples" also passes
]


def parse_frontmatter(text):
    """Return (fields, body) or raise ValueError.

    shortcut: handles single-line `key: value` pairs only, which is all DevReach
    skills use; switch to a YAML parser if multi-line values are ever needed.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with '---' frontmatter")
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        raise ValueError("frontmatter is not closed with '---'")
    fields = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line or line.startswith((" ", "\t")):
            raise ValueError(f"unsupported frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        if key in fields:
            raise ValueError(f"duplicate frontmatter key: {key}")
        value = value.strip()
        if value[:1] not in ("'", '"') and (": " in value or " #" in value):
            raise ValueError(f"unquoted value for '{key}' contains ': ' or ' #' (invalid YAML); quote it or reword")
        fields[key] = value.strip("'\"")
    return fields, "\n".join(lines[end + 1 :])


def validate_skill(skill_dir):
    """Return a list of error strings for one skill directory."""
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return ["missing SKILL.md"]
    text = skill_file.read_text(encoding="utf-8")
    try:
        fields, body = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    errors = []
    name = fields.get("name", "")
    if not name:
        errors.append("frontmatter missing 'name'")
    else:
        if name != skill_dir.name:
            errors.append(f"name '{name}' does not match directory '{skill_dir.name}'")
        if not NAME_RE.match(name):
            errors.append(f"name '{name}' must be lowercase letters, digits, and single hyphens")
        if len(name) > MAX_NAME:
            errors.append(f"name longer than {MAX_NAME} characters")

    description = fields.get("description", "")
    if not description:
        errors.append("frontmatter missing 'description'")
    else:
        if len(description) > MAX_DESCRIPTION:
            errors.append(f"description longer than {MAX_DESCRIPTION} characters")
        if "<" in description or ">" in description:
            errors.append("description must not contain angle brackets")

    headings = [h.strip() for h in re.findall(r"^##\s+(.+)$", body, re.MULTILINE)]
    for section in REQUIRED_SECTIONS:
        if not any(h.startswith(section) for h in headings):
            errors.append(f"missing section '## {section}'")

    if len(text.splitlines()) > MAX_LINES:
        errors.append(f"SKILL.md over {MAX_LINES} lines; move detail into references/")
    return errors


def validate_all(skills_root):
    """Return {skill_name: [errors]} for every skill directory."""
    skills_root = Path(skills_root)
    if not skills_root.is_dir():
        return {str(skills_root): ["skills directory not found"]}
    dirs = sorted(p for p in skills_root.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not dirs:
        return {str(skills_root): ["no skills found"]}
    return {d.name: validate_skill(d) for d in dirs}


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent / "skills"
    results = validate_all(root)
    failed = 0
    for name, errors in results.items():
        if errors:
            failed += 1
            print(f"FAIL {name}")
            for err in errors:
                print(f"     - {err}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(results) - failed}/{len(results)} skills valid")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
