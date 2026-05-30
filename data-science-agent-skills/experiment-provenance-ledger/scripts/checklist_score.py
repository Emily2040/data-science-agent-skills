#!/usr/bin/env python3
"""Score a workflow checklist from JSON.

Input format:
{
  "items": [
    {"name": "owner confirmed", "status": "pass", "weight": 2},
    {"name": "privacy reviewed", "status": "blocker", "weight": 3}
  ]
}

Statuses: pass, partial, fail, blocker, unknown.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

SCORES = {"pass": 1.0, "partial": 0.5, "unknown": 0.0, "fail": 0.0, "blocker": 0.0}


def main() -> int:
    parser = argparse.ArgumentParser(description="Score a data science skill checklist.")
    parser.add_argument("input", help="Path to checklist JSON.")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero for needs_work as well as blocked.")
    args = parser.parse_args()
    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    items = payload.get("items", [])
    total_weight = 0.0
    earned = 0.0
    blockers = []
    unknown = []
    for item in items:
        name = str(item.get("name", "unnamed item"))
        status = str(item.get("status", "unknown")).lower()
        weight = float(item.get("weight", 1))
        if status not in SCORES:
            status = "unknown"
        total_weight += weight
        earned += SCORES[status] * weight
        if status == "blocker":
            blockers.append(name)
        if status == "unknown":
            unknown.append(name)
    score = round((earned / total_weight) * 100, 1) if total_weight else 0.0
    result = {
        "score": score,
        "status": "blocked" if blockers else ("ready" if score >= 80 else "needs_work"),
        "blockers": blockers,
        "unknowns": unknown,
        "item_count": len(items),
    }
    print(json.dumps(result, indent=2))
    if args.strict and result["status"] != "ready":
        return 1
    return 2 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())
