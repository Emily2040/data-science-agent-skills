#!/usr/bin/env python3
"""Check train/validation/test CSV files for key overlap and suspicious target-leakage column names."""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

LEAKY_TOKEN_RE = re.compile(
    r"(?:^|_)(?:target|label|outcome|future|after|post_(?:event|treatment|outcome|label|churn|signup)|refund|chargeback|cancel|churned|resolved|actual|ground_truth|leak)(?:$|_)",
    re.IGNORECASE,
)
SAFE_COLUMN_SUBSTRINGS = ("postal", "postcode", "post_code", "post_id", "blog_post", "forum_post")


def load_keys(path: Path, key: str) -> tuple[set[str], list[str], bool]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        if key not in headers:
            return set(), headers, False
        values = {(row.get(key) or "").strip() for row in reader if (row.get(key) or "").strip()}
        return values, headers, True


def is_leaky_feature_name(col: str, target: str) -> bool:
    lower = col.strip().lower()
    if lower == target:
        return False
    if any(safe in lower for safe in SAFE_COLUMN_SUBSTRINGS):
        return False
    if target and target in lower and lower != target:
        return True
    return bool(LEAKY_TOKEN_RE.search(lower))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("train_csv", nargs="?")
    parser.add_argument("eval_csv", nargs="?")
    parser.add_argument("--train", dest="train_flag", default=None)
    parser.add_argument("--test", "--eval", dest="eval_flag", default=None)
    parser.add_argument("--key", default="id", help="Entity or group key column")
    parser.add_argument("--target", default="", help="Target column name")
    args = parser.parse_args()

    train_path = args.train_flag or args.train_csv
    eval_path = args.eval_flag or args.eval_csv
    if not train_path or not eval_path:
        parser.error("both train_csv and eval_csv are required")

    train_keys, train_headers, train_has_key = load_keys(Path(train_path), args.key)
    eval_keys, eval_headers, eval_has_key = load_keys(Path(eval_path), args.key)
    overlap = sorted(train_keys & eval_keys)
    target = args.target.strip().lower()

    missing_key_files: list[str] = []
    if not train_has_key:
        missing_key_files.append("train_csv")
    if not eval_has_key:
        missing_key_files.append("eval_csv")

    suspicious_columns = []
    for col in sorted(set(train_headers) | set(eval_headers)):
        if is_leaky_feature_name(col, target):
            suspicious_columns.append(col)

    if overlap or missing_key_files:
        status = "blocked"
    elif suspicious_columns:
        status = "needs_review"
    else:
        status = "no_obvious_leakage"

    result = {
        "key": args.key,
        "key_present_in_both": not missing_key_files,
        "missing_key_in": missing_key_files,
        "train_distinct_keys": len(train_keys),
        "eval_distinct_keys": len(eval_keys),
        "overlap_count": len(overlap),
        "overlap_examples": overlap[:20],
        "suspicious_columns": suspicious_columns,
        "status": status,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 2 if status != "no_obvious_leakage" else 0


if __name__ == "__main__":
    raise SystemExit(main())
