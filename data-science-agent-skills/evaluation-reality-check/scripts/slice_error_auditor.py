#!/usr/bin/env python3
"""Audit model predictions across subgroup slices for accuracy disparity and calibration error."""
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("predictions_csv", help="CSV with y_true, y_pred, y_prob, slice")
    parser.add_argument("--max-slice-gap", type=float, default=0.10)
    args = parser.parse_args()

    with Path(args.predictions_csv).open("r", encoding="utf-8", errors="replace", newline="") as f:
        rows = list(csv.DictReader(f))

    by_slice: dict[str, list[tuple[int, int, float]]] = defaultdict(list)
    for r in rows:
        s = (r.get("slice") or "default").strip()
        yt = int(float(r["y_true"]))
        yp = int(float(r["y_pred"]))
        prob = float(r.get("y_prob", yp))
        by_slice[s].append((yt, yp, prob))

    slice_metrics = {}
    accs = []
    for s, items in sorted(by_slice.items()):
        acc = sum(1 for yt, yp, _ in items if yt == yp) / len(items)
        brier = sum((prob - yt) ** 2 for yt, _, prob in items) / len(items)
        accs.append(acc)
        slice_metrics[s] = {"n": len(items), "accuracy": round(acc, 4), "brier_score": round(brier, 4)}

    gap = (max(accs) - min(accs)) if len(accs) >= 2 else 0.0
    status = "pass" if gap <= args.max_slice_gap else "slice_disparity_exceeded"
    print(
        json.dumps(
            {
                "slices": slice_metrics,
                "max_accuracy_gap": round(gap, 4),
                "threshold": args.max_slice_gap,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
