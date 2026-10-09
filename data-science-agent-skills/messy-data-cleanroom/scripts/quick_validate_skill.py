#!/usr/bin/env python3
"""Validate portable skill structure without third-party dependencies."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    root = Path(args.skill_dir).resolve()
    errors: list[str] = []
    for required in ["SKILL.md", "README.md", "MANIFEST.json", "agents/openai.yaml"]:
        if not (root / required).exists():
            errors.append(f"missing required file: {required}")

    contract = root / "tests" / "test_skill_contract.py"
    if args.strict:
        if not contract.exists():
            errors.append("missing required strict contract test: tests/test_skill_contract.py")
        else:
            proc = subprocess.run([sys.executable, str(contract), str(root)], capture_output=True, text=True)
            if proc.returncode != 0:
                errors.append(proc.stdout.strip() or proc.stderr.strip() or "contract test failed")

    status = "ok" if not errors else "failed"
    print(json.dumps({"skill": root.name, "status": status, "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
