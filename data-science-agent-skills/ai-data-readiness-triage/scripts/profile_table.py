#!/usr/bin/env python3
"""Profile a local CSV/TSV file using only the Python standard library."""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import statistics
from collections import Counter
from pathlib import Path

PII_NAME_RE = re.compile(
    r"(?:^|_)(?:first_?name|last_?name|full_?name|user_?name|person_?name|customer_?name|client_?name|patient_?name|employee_?name|name)(?:$|_)",
    re.IGNORECASE,
)
SAFE_NAME_PREFIXES = (
    "model_name",
    "feature_name",
    "table_name",
    "column_name",
    "metric_name",
    "file_name",
    "dataset_name",
    "experiment_name",
    "pipeline_name",
    "branch_name",
    "stage_name",
    "host_name",
)


def parse_finite_floats(values: list[str]) -> tuple[list[float], int]:
    parsed: list[float] = []
    non_numeric = 0
    for value in values:
        text = value.strip()
        if not text:
            continue
        try:
            num = float(text)
            if math.isfinite(num):
                parsed.append(num)
            else:
                non_numeric += 1
        except ValueError:
            non_numeric += 1
    return parsed, non_numeric


def is_pii_name_column(column: str) -> bool:
    lower = column.strip().lower()
    if any(lower == safe or lower.endswith("_" + safe) for safe in SAFE_NAME_PREFIXES):
        return False
    return bool(PII_NAME_RE.search(lower))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="CSV or TSV path to inspect")
    parser.add_argument("--delimiter", default=None, help="Optional delimiter override")
    parser.add_argument("--max-rows", type=int, default=10000, help="Row cap for fast local triage")
    args = parser.parse_args()

    path = Path(args.path)
    delimiter = args.delimiter or ("\t" if path.suffix.lower() in {".tsv", ".tab"} else ",")
    with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        columns = reader.fieldnames or []
        rows: list[dict[str, str]] = []
        for idx, row in enumerate(reader):
            if idx >= args.max_rows:
                break
            rows.append(row)

    total = len(rows)
    DuplicateCounter = Counter(tuple((col, row.get(col, "")) for col in columns) for row in rows)
    duplicate_rows = sum(count - 1 for count in DuplicateCounter.values() if count > 1)

    profile: dict[str, object] = {}
    for col in columns:
        raw = [(row.get(col) or "").strip() for row in rows]
        non_empty = [value for value in raw if value not in {"", "null", "NULL", "None", "NA", "nan", "NaN"}]
        missing = total - len([v for v in non_empty if v != "N/A"])
        numeric_vals, non_numeric_count = parse_finite_floats(non_empty)
        sample_non_null = len(non_empty)
        is_numeric = sample_non_null > 0 and (len(numeric_vals) / sample_non_null) >= 0.90
        col_summary: dict[str, object] = {
            "missing": missing,
            "missing_rate": round(missing / total, 4) if total else 0.0,
            "distinct_sampled": len(set(non_empty[:2000])),
            "inferred_type": "numeric" if is_numeric else "string_or_mixed",
            "pii_email_hint": any(re.search(r"[^@\s]+@[^@\s]+\.[^@\s]+", value) for value in non_empty[:200]),
            "pii_name_hint": is_pii_name_column(col),
        }
        if is_numeric and numeric_vals:
            col_summary["min"] = min(numeric_vals)
            col_summary["max"] = max(numeric_vals)
            col_summary["mean"] = round(statistics.fmean(numeric_vals), 4)
            col_summary["non_numeric_coerced_or_skipped"] = non_numeric_count
        profile[col] = col_summary

    print(
        json.dumps(
            {
                "path": str(path),
                "rows_sampled": total,
                "duplicate_rows_sampled": duplicate_rows,
                "columns": profile,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
