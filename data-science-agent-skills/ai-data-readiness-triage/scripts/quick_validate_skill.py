#!/usr/bin/env python3
"""Validate a standalone skill folder for portable use."""
from __future__ import annotations

import argparse
import re
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a standalone skill folder.")
    parser.add_argument("skill_dir", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.skill_dir)
    errors = []
    skill = root / "SKILL.md"
    if not skill.exists():
        errors.append("missing SKILL.md")
    else:
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append("SKILL.md missing YAML frontmatter")
        match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", text, re.MULTILINE)
        if not match:
            errors.append("frontmatter missing lowercase hyphenated name")
        if not re.search(r"^description:\s*.+", text, re.MULTILINE):
            errors.append("frontmatter missing description")
    for rel in ["README.md", "references/playbook.md", "references/acceptance-tests.md", "references/provider-interop.md", "agents/openai.yaml", "assets/hero-shot.png", "assets/reddit-infographic.png"]:
        if not (root / rel).exists():
            errors.append(f"missing {rel}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("standalone-skill-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
