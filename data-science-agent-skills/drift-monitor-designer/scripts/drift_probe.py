#!/usr/bin/env python3
"""Compare baseline and current CSV distributions with simple stdlib drift signals."""
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path


def parse_column(rows: list[dict[str, str]], col: str) -> tuple[list[float], int, int]:
    vals: list[float] = []
    missing = 0
    invalid = 0
    for row in rows:
        raw = (row.get(col) or "").strip()
        if raw in {"", "null", "NULL", "None", "NA", "N/A"}:
            missing += 1
            continue
        try:
            num = float(raw)
            if math.isfinite(num):
                vals.append(num)
            else:
                invalid += 1
        except ValueError:
            invalid += 1
    return vals, missing, invalid


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline_csv", nargs="?")
    parser.add_argument("current_csv", nargs="?")
    parser.add_argument("--baseline", dest="baseline_flag", default=None)
    parser.add_argument("--current", dest="current_flag", default=None)
    parser.add_argument("--column", default=None, help="Optional single column filter")
    args = parser.parse_args()

    base_path = args.baseline_flag or args.baseline_csv
    cur_path = args.current_flag or args.current_csv
    if not base_path or not cur_path:
        parser.error("both baseline_csv and current_csv are required")

    with Path(base_path).open("r", encoding="utf-8", errors="replace", newline="") as f:
        base_rows = list(csv.DictReader(f))
    with Path(cur_path).open("r", encoding="utf-8", errors="replace", newline="") as f:
        cur_rows = list(csv.DictReader(f))

    cols = sorted(set(base_rows[0].keys() if base_rows else []) & set(cur_rows[0].keys() if cur_rows else []))
    if args.column:
        cols = [c for c in cols if c == args.column]

    report: dict[str, object] = {}
    for col in cols:
        base, b_miss, b_inv = parse_column(base_rows, col)
        cur, c_miss, c_inv = parse_column(cur_rows, col)
        if not base and not cur:
            continue
        if not base or not cur or b_inv > 0 or c_inv > 0:
            report[col] = {
                "baseline_valid_n": len(base),
                "current_valid_n": len(cur),
                "baseline_invalid": b_inv,
                "current_invalid": c_inv,
                "status": "investigate",
                "reason": "non_finite_or_empty_numeric_slice",
            }
            continue

        b_mean, c_mean = statistics.fmean(base), statistics.fmean(cur)
        b_std = statistics.pstdev(base) if len(base) > 1 else 0.0
        c_std = statistics.pstdev(cur) if len(cur) > 1 else 0.0
        b_miss_rate = b_miss / max(1, len(base_rows))
        c_miss_rate = c_miss / max(1, len(cur_rows))
        miss_delta = abs(c_miss_rate - b_miss_rate)

        if b_std == 0.0:
            mean_z = 0.0 if c_mean == b_mean else 999.0
            std_ratio = 1.0 if c_std == 0.0 else 999.0
        else:
            mean_z = abs(c_mean - b_mean) / b_std
            std_ratio = c_std / b_std

        std_log_shift = abs(math.log(max(std_ratio, 1e-6))) if std_ratio > 0 else (0.0 if c_std == b_std else 999.0)

        if mean_z >= 2.0 or std_log_shift >= math.log(2.0) or miss_delta >= 0.10:
            status = "investigate"
        elif mean_z >= 1.0 or std_log_shift >= math.log(1.35) or miss_delta >= 0.05:
            status = "watch"
        else:
            status = "stable"

        report[col] = {
            "baseline_mean": round(b_mean, 4),
            "current_mean": round(c_mean, 4),
            "baseline_std": round(b_std, 4),
            "current_std": round(c_std, 4),
            "mean_shift_z": round(mean_z, 4),
            "std_ratio": round(std_ratio, 4),
            "missing_rate_delta": round(miss_delta, 4),
            "status": status,
        }
    print(json.dumps({"columns": report}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
