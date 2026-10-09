#!/usr/bin/env python3
"""Extract rough table, file, and metric lineage tokens from SQL, Python, YAML, JSON, or notebooks."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SQL_PATTERNS = {
    "sql_from_join": re.compile(r"(?i)\b(?:from|join)\s+([A-Za-z_][A-Za-z0-9_.$`\"'-]*)"),
    "sql_write": re.compile(r"(?i)\b(?:into|table|view)\s+([A-Za-z_][A-Za-z0-9_.$`\"'-]*)"),
}
CODE_PATTERNS = {
    "file_path": re.compile(r"['\"]([^'\"]+\.(?:csv|tsv|parquet|feather|json|jsonl|db|sqlite|duckdb|sql))['\"]", re.IGNORECASE),
    "pandas_read": re.compile(r"\b(?:read_csv|read_parquet|read_sql|read_table|read_json)\s*\(\s*['\"]?([^'\"),\s]+)"),
}
SQL_STOPWORDS = {"select", "where", "unnest", "lateral", "values", "dual", "stdin", "stdout"}
PYTHON_IMPORT_LINE = re.compile(r"^\s*from\s+[A-Za-z0-9_.]+\s+import\b")
EMBEDDED_SQL_HINT = re.compile(r"(?i)\bSELECT\b[\s\S]+?\bFROM\b")


def scan_text(text: str, suffix: str, hits: dict[str, set[str]]) -> None:
    for kind, pattern in CODE_PATTERNS.items():
        for match in pattern.findall(text):
            hits[kind].add(match.strip())

    is_sql_context = suffix == ".sql" or bool(EMBEDDED_SQL_HINT.search(text))
    if not is_sql_context:
        return

    for line in text.splitlines():
        if PYTHON_IMPORT_LINE.match(line):
            continue
        if suffix in {".md", ".yaml", ".yml"} and not re.search(r"(?i)\b(?:select|insert|create|merge|update)\b", line):
            continue
        for kind, pattern in SQL_PATTERNS.items():
            for match in pattern.findall(line):
                token = match.strip("`\"'.,:;()[]")
                if token and token.lower() not in SQL_STOPWORDS and not token.startswith("-"):
                    hits[kind].add(token)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    args = parser.parse_args()

    files: list[Path] = []
    for raw in args.paths:
        path = Path(raw)
        if path.is_dir():
            for ext in ("*.sql", "*.py", "*.ipynb", "*.yaml", "*.yml", "*.json"):
                files.extend(path.rglob(ext))
        elif path.exists():
            files.append(path)

    hits: dict[str, set[str]] = {k: set() for k in (*SQL_PATTERNS, *CODE_PATTERNS)}
    for file in sorted(set(files)):
        suffix = file.suffix.lower()
        text = file.read_text(encoding="utf-8", errors="replace")
        if suffix == ".ipynb":
            try:
                nb = json.loads(text)
                for cell in nb.get("cells", []):
                    if cell.get("cell_type") == "code":
                        src = "".join(cell.get("source", []))
                        scan_text(src, ".py", hits)
                continue
            except Exception:
                pass
        scan_text(text, suffix, hits)

    print(
        json.dumps(
            {
                "files_scanned": [str(f) for f in sorted(set(files))],
                "tokens": {k: sorted(v) for k, v in hits.items()},
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
