#!/usr/bin/env python3
"""Check that relative links in Markdown files point to files that exist.

External (http/https/mailto) links and pure #anchors are skipped.
Usage: python3 scripts/check_links.py [repo_root]
"""

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def broken_links(root):
    root = Path(root)
    broken = []
    for md in sorted(root.rglob("*.md")):
        if any(part.startswith(".") and part != ".github" for part in md.relative_to(root).parts):
            continue
        text = FENCE_RE.sub("", md.read_text(encoding="utf-8"))
        for target in LINK_RE.findall(text):
            if target.startswith(SKIP_PREFIXES):
                continue
            path = target.split("#", 1)[0]
            if path and not (md.parent / path).exists():
                broken.append((md.relative_to(root), target))
    return broken


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    broken = broken_links(root)
    for md, target in broken:
        print(f"BROKEN {md}: {target}")
    print(f"{len(broken)} broken relative link(s)")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
