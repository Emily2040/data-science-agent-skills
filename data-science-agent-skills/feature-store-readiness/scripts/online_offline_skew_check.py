#!/usr/bin/env python3
"""Compare offline training features and online serving features keyed by entity ID for skew."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("offline_csv")
    parser.add_argument("online_csv")
    parser.add_argument("--key", default="entity_id")
    parser.add_argument("--tolerance", type=float, default=1e-4)
    args = parser.parse_args()

    with Path(args.offline_csv).open("r", encoding="utf-8", errors="replace", newline="") as f:
        off_rows = {r[args.key]: r for r in csv.DictReader(f) if args.key in r}
    with Path(args.online_csv).open("r", encoding="utf-8", errors="replace", newline="") as f:
        on_rows = {r[args.key]: r for r in csv.DictReader(f) if args.key in r}

    shared_keys = sorted(set(off_rows) & set(on_rows))
    if not shared_keys:
        print(json.dumps({"status": "blocked", "reason": "no_matching_entity_keys"}, indent=2))
        return 2

    feature_cols = [c for c in off_rows[shared_keys[0]].keys() if c != args.key and c in on_rows[shared_keys[0]]]
    mismatches: dict[str, int] = {c: 0 for c in feature_cols}
    for k in shared_keys:
        for c in feature_cols:
            v1, v2 = (off_rows[k].get(c) or "").strip(), (on_rows[k].get(c) or "").strip()
            try:
                if abs(float(v1) - float(v2)) > args.tolerance:
                    mismatches[c] += 1
            except ValueError:
                if v1 != v2:
                    mismatches[c] += 1

    skewed = {c: cnt for c, cnt in mismatches.items() if cnt > 0}
    status = "parity_verified" if not skewed else "online_offline_skew_detected"
    print(
        json.dumps(
            {
                "entities_compared": len(shared_keys),
                "features_checked": feature_cols,
                "skewed_feature_counts": skewed,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "parity_verified" else 2


if __name__ == "__main__":
    raise SystemExit(main())
