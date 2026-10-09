#!/usr/bin/env python3
"""Compute pairwise agreement and Cohen's kappa between two SME label columns in a CSV file."""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("labels_csv")
    parser.add_argument("--rater-a", default="sme_a")
    parser.add_argument("--rater-b", default="sme_b")
    args = parser.parse_args()

    with Path(args.labels_csv).open("r", encoding="utf-8", errors="replace", newline="") as f:
        rows = list(csv.DictReader(f))

    pairs = [
        ((r.get(args.rater_a) or "").strip(), (r.get(args.rater_b) or "").strip())
        for r in rows
        if (r.get(args.rater_a) or "").strip() and (r.get(args.rater_b) or "").strip()
    ]
    n = len(pairs)
    if n == 0:
        print(json.dumps({"status": "blocked", "reason": "no_paired_labels"}, indent=2))
        return 2

    agree = sum(1 for a, b in pairs if a == b)
    p_o = agree / n
    counts_a = Counter(a for a, _ in pairs)
    counts_b = Counter(b for _, b in pairs)
    labels = sorted(set(counts_a) | set(counts_b))
    p_e = sum((counts_a[k] / n) * (counts_b[k] / n) for k in labels)
    kappa = 1.0 if p_e == 1.0 else (p_o - p_e) / (1.0 - p_e)
    disagreements = [idx for idx, (a, b) in enumerate(pairs) if a != b]

    status = "pass" if kappa >= 0.7 else ("needs_adjudication" if kappa >= 0.4 else "rubric_ambiguous")
    print(
        json.dumps(
            {
                "paired_items": n,
                "raw_agreement": round(p_o, 4),
                "cohens_kappa": round(kappa, 4),
                "disagreement_count": len(disagreements),
                "disagreement_row_indices": disagreements[:20],
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
