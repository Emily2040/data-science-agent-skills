#!/usr/bin/env python3
"""Probe split files for overlap and suspicious target-like feature names."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

LEAKY_TOKENS = ["target", "label", "outcome", "future", "after", "post", "churned", "converted", "approved"]


def load_keys(path, key):
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        values = {row.get(key, "").strip() for row in reader if row.get(key, "").strip()}
    return fields, values


def main() -> int:
    parser = argparse.ArgumentParser(description="Check train/test overlap and leaky feature names.")
    parser.add_argument("--train", required=True)
    parser.add_argument("--test", required=True)
    parser.add_argument("--key", required=True)
    parser.add_argument("--target", default="")
    args = parser.parse_args()
    train_fields, train_keys = load_keys(args.train, args.key)
    test_fields, test_keys = load_keys(args.test, args.key)
    overlap = sorted(train_keys & test_keys)
    target = args.target.lower()
    suspicious = []
    for field in sorted(set(train_fields) | set(test_fields)):
        lower = field.lower()
        if field == args.key:
            continue
        if target and target in lower and lower != target:
            suspicious.append(field)
        elif any(token in lower for token in LEAKY_TOKENS):
            suspicious.append(field)
    result = {
        "train_keys": len(train_keys),
        "test_keys": len(test_keys),
        "overlap_count": len(overlap),
        "overlap_examples": overlap[:20],
        "suspicious_feature_names": suspicious,
        "status": "blocked" if overlap or suspicious else "no_obvious_leakage",
    }
    print(json.dumps(result, indent=2))
    return 2 if result["status"] == "blocked" else 0


if __name__ == "__main__":
    raise SystemExit(main())
