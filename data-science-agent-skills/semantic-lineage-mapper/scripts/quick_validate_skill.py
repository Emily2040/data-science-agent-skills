#!/usr/bin/env python3
"""Validate a standalone skill folder for portable use."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a standalone skill folder.")
    parser.add_argument("skill_dir", nargs="?", default=".")
    parser.add_argument("--strict", action="store_true", help="Run full portability contract tests.")
    parser.add_argument("--json", action="store_true", help="Emit JSON status.")
    args = parser.parse_args()

    root = Path(args.skill_dir).resolve()
    contract = root / "tests" / "test_skill_contract.py"
    errors = []
    for rel in ["SKILL.md", "README.md", "MANIFEST.json", "references/playbook.md", "references/acceptance-tests.md", "references/provider-interop.md", "agents/openai.yaml", "assets/hero-shot.png", "assets/reddit-infographic.png"]:
        if not (root / rel).exists():
            errors.append(f"missing {rel}")

    if args.strict and contract.exists():
        proc = subprocess.run([sys.executable, str(contract), str(root)], text=True, capture_output=True)
        if proc.returncode != 0:
            errors.extend(line.replace("ERROR: ", "") for line in proc.stdout.splitlines() if line.strip())
            if proc.stderr.strip():
                errors.append(proc.stderr.strip())

    ok = not errors
    if args.json:
        print(json.dumps({"ok": ok, "skill": root.name, "errors": errors}, indent=2))
    elif ok:
        print("standalone-skill-ok")
    else:
        for error in errors:
            print(f"ERROR: {error}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
