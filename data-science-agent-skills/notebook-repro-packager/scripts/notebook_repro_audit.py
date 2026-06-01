#!/usr/bin/env python3
"""Audit notebooks for reproducibility and pipeline-refactor risk."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit .ipynb files for reproducibility risk.")
    parser.add_argument("notebooks", nargs="+")
    args = parser.parse_args()
    findings = []
    for item in args.notebooks:
        path = Path(item)
        nb = json.loads(path.read_text(encoding="utf-8"))
        exec_counts = []
        for idx, cell in enumerate(nb.get("cells", []), start=1):
            if cell.get("cell_type") != "code":
                continue
            source = "".join(cell.get("source", []))
            count = cell.get("execution_count")
            if count is not None:
                exec_counts.append(count)
            checks = {
                "shell_command": bool(re.search(r"^\s*!", source, re.MULTILINE)),
                "absolute_path": bool(re.search(r"[A-Za-z]:\\\\|/Users/|/home/", source)),
                "random_without_seed_hint": "random" in source.lower() and "seed" not in source.lower(),
                "network_download": any(token in source.lower() for token in ["requests.get", "wget", "curl ", "download"]),
            }
            for kind, present in checks.items():
                if present:
                    findings.append({"notebook": str(path), "cell": idx, "risk": kind})
        if exec_counts and exec_counts != sorted(exec_counts):
            findings.append({"notebook": str(path), "cell": None, "risk": "out_of_order_execution_counts"})
    print(json.dumps({"findings": findings, "risk_count": len(findings)}, indent=2))
    return 2 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
