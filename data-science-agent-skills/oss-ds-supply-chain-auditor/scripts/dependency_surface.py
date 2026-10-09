#!/usr/bin/env python3
"""Inspect common Python and data-science dependency files for unpinned or risky entries."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MANIFEST_NAMES = {"requirements.txt", "pyproject.toml", "environment.yml", "environment.yaml", "pipfile", "uv.lock", "poetry.lock"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.root)
    manifests = [p for p in root.rglob("*") if p.is_file() and p.name.lower() in MANIFEST_NAMES]
    notebooks = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() == ".ipynb"]
    risky: list[dict[str, object]] = []
    for path in manifests:
        for line_no, raw in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if any(token in line for token in ["git+", "http://", "https://"]):
                risky.append({"file": str(path), "line": line_no, "issue": "direct_url_dependency", "value": line})
            elif path.name.lower() == "requirements.txt" and not re.search(r"(==|~=|>=|<=)", line) and not line.startswith("-"):
                risky.append({"file": str(path), "line": line_no, "issue": "unpinned_requirement", "value": line})

    print(
        json.dumps(
            {
                "manifests": [str(p) for p in sorted(manifests)],
                "notebooks": [str(p) for p in sorted(notebooks)],
                "risk_count": len(risky),
                "risks": risky,
                "status": "review_required" if risky else "no_manifest_red_flags_detected",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 2 if risky else 0


if __name__ == "__main__":
    raise SystemExit(main())
