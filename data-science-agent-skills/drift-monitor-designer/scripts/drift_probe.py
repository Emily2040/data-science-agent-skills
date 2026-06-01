#!/usr/bin/env python3
"""Compare baseline and current numeric CSV distributions with simple drift signals."""
from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path


def read_column(path, column):
    values = []
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            try:
                values.append(float(row[column]))
            except Exception:
                pass
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare simple numeric drift.")
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--current", required=True)
    parser.add_argument("--column", required=True)
    args = parser.parse_args()
    base = read_column(args.baseline, args.column)
    cur = read_column(args.current, args.column)
    if not base or not cur:
        raise SystemExit("column must contain numeric values in both files")
    b_mean = statistics.mean(base)
    c_mean = statistics.mean(cur)
    b_std = statistics.pstdev(base) or 1.0
    z = abs(c_mean - b_mean) / b_std
    result = {
        "baseline_count": len(base),
        "current_count": len(cur),
        "baseline_mean": round(b_mean, 6),
        "current_mean": round(c_mean, 6),
        "mean_shift_std_units": round(z, 3),
        "status": "investigate" if z >= 2 else "watch" if z >= 1 else "stable",
    }
    print(json.dumps(result, indent=2))
    return 2 if result["status"] == "investigate" else 0


if __name__ == "__main__":
    raise SystemExit(main())
