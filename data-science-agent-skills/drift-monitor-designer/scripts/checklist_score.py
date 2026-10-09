#!/usr/bin/env python3
"""Compute a weighted readiness or review score from a JSON checklist."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

STATUS_POINTS = {"pass": 1.0, "warn": 0.5, "partial": 0.5, "fail": 0.0, "blocked": 0.0, "unknown": 0.0}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", help="JSON file with an items list: [{id, weight, status, blocker}]")
    parser.add_argument("--strict", action="store_true", help="Return non-zero unless status is pass.")
    args = parser.parse_args()

    data = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    items = data.get("items", data if isinstance(data, list) else [])
    if not items:
        print(json.dumps({"status": "blocked", "reason": "no_checklist_items"}))
        return 2

    total_weight = 0.0
    earned = 0.0
    blockers: list[str] = []
    failed_items: list[str] = []
    unknowns: list[str] = []

    for idx, item in enumerate(items, 1):
        item_id = str(item.get("id", f"item_{idx}"))
        weight = float(item.get("weight", 1.0))
        if weight <= 0:
            continue
        status = str(item.get("status", "unknown")).lower()
        points = STATUS_POINTS.get(status, 0.0)
        total_weight += weight
        earned += weight * points
        if status in {"fail", "blocked"}:
            failed_items.append(item_id)
        if item.get("blocker") and status in {"fail", "blocked", "unknown"}:
            blockers.append(item_id)
        if status == "unknown":
            unknowns.append(item_id)

    score = round((earned / total_weight) if total_weight else 0.0, 4)
    if blockers:
        verdict = "blocked"
    elif score >= 0.85 and not failed_items:
        verdict = "pass"
    elif score >= 0.65:
        verdict = "fix-first"
    else:
        verdict = "needs_work"

    result = {
        "score": score,
        "status": verdict,
        "blockers": blockers,
        "failed_items": failed_items,
        "unknown_items": unknowns,
        "item_count": len(items),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if blockers or verdict == "needs_work":
        return 2
    if args.strict and verdict != "pass":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
