#!/usr/bin/env python3
"""Profile CSV data for DS readiness, contracts, cleaning, privacy, or missingness review."""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


def looks_numeric(values):
    seen = 0
    ok = 0
    for value in values:
        if value == "":
            continue
        seen += 1
        try:
            float(value)
            ok += 1
        except ValueError:
            pass
    return seen > 0 and ok / seen >= 0.95


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a compact CSV profile.")
    parser.add_argument("csv_path")
    parser.add_argument("--max-rows", type=int, default=100000)
    args = parser.parse_args()
    path = Path(args.csv_path)
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        rows = []
        for index, row in enumerate(reader):
            if index >= args.max_rows:
                break
            rows.append({key: (value or "").strip() for key, value in row.items()})
    stats = {}
    for column in columns:
        values = [row.get(column, "") for row in rows]
        non_null = [value for value in values if value != ""]
        counts = Counter(non_null)
        inferred = "numeric" if looks_numeric(non_null) else "string"
        numeric = []
        if inferred == "numeric":
            numeric = [float(value) for value in non_null if value != ""]
        pii_hint = any(token in column.lower() for token in ["email", "phone", "ssn", "name", "address", "dob", "birth"])
        stats[column] = {
            "inferred_type": inferred,
            "missing": len(values) - len(non_null),
            "missing_rate": round((len(values) - len(non_null)) / len(values), 4) if values else 0,
            "unique": len(counts),
            "top_values": counts.most_common(5),
            "min": min(numeric) if numeric else None,
            "max": max(numeric) if numeric else None,
            "pii_name_hint": pii_hint,
        }
    output = {"path": str(path), "rows_profiled": len(rows), "columns": stats}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
