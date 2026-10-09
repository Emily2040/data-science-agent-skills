#!/usr/bin/env python3
"""Compare candidate model metrics and latency against simple baselines and ablations."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("comparison_json", help="JSON with baseline_score, candidate_score, min_lift, latency_ratio")
    args = parser.parse_args()

    data = json.loads(Path(args.comparison_json).read_text(encoding="utf-8"))
    base = float(data.get("baseline_score", 0.0))
    cand = float(data.get("candidate_score", 0.0))
    min_lift = float(data.get("min_lift", 0.01))
    latency_ratio = float(data.get("latency_ratio", 1.0))
    max_latency_ratio = float(data.get("max_latency_ratio", 3.0))
    seeds = int(data.get("seeds_evaluated", 1))

    lift = round(cand - base, 6)
    reasons: list[str] = []
    if lift < min_lift:
        reasons.append("lift_below_minimum_threshold")
    if latency_ratio > max_latency_ratio:
        reasons.append("latency_overhead_exceeds_budget")
    if seeds < 3:
        reasons.append("insufficient_seed_replicates")

    status = "go" if not reasons else ("fix-first" if lift >= min_lift else "stop")
    print(
        json.dumps(
            {
                "baseline_score": base,
                "candidate_score": cand,
                "observed_lift": lift,
                "min_required_lift": min_lift,
                "latency_ratio": latency_ratio,
                "seeds_evaluated": seeds,
                "reasons": reasons,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "go" else 2


if __name__ == "__main__":
    raise SystemExit(main())
