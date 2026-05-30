#!/usr/bin/env python3
"""Extract likely lineage references from SQL, Python, notebooks, and config-like text files."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PATTERNS = {
    "sql_from_join": re.compile(r"\b(?:from|join)\s+([A-Za-z0-9_.`\"-]+)", re.IGNORECASE),
    "python_read": re.compile(r"read_(?:csv|parquet|json|sql|excel)\(([^)]*)\)", re.IGNORECASE),
    "model_file": re.compile(r"['\"]([^'\"]+\.(?:pkl|joblib|onnx|pt|pth|safetensors|h5))['\"]", re.IGNORECASE),
    "data_file": re.compile(r"['\"]([^'\"]+\.(?:csv|parquet|jsonl|json|xlsx|feather))['\"]", re.IGNORECASE),
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract likely lineage tokens from files.")
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()
    findings = []
    for item in args.paths:
        path = Path(item)
        if path.is_dir():
            files = [p for p in path.rglob("*") if p.suffix.lower() in {".sql", ".py", ".ipynb", ".yaml", ".yml", ".json"}]
        else:
            files = [path]
        for file_path in files:
            try:
                text = file_path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for kind, pattern in PATTERNS.items():
                for match in pattern.finditer(text):
                    findings.append({"file": str(file_path), "kind": kind, "reference": match.group(1)[:240]})
    print(json.dumps({"findings": findings, "count": len(findings)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
