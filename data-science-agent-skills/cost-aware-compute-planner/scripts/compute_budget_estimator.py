#!/usr/bin/env python3
"""Estimate staged experiment compute cost and budget status."""
from __future__ import annotations

import argparse
import json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--hourly-rate", type=float, required=True)
    parser.add_argument("--runs", type=int, default=1)
    parser.add_argument("--failure-rate", type=float, default=0.15)
    parser.add_argument("--budget", type=float, default=None)
    args = parser.parse_args()

    if args.hours < 0 or args.hourly_rate < 0 or args.runs < 1 or not (0.0 <= args.failure_rate < 0.95):
        print(
            json.dumps(
                {
                    "status": "invalid_input",
                    "reason": "hours and hourly_rate must be >= 0, runs >= 1, and 0.0 <= failure_rate < 0.95",
                },
                indent=2,
            )
        )
        return 2

    base = args.hours * args.hourly_rate * args.runs
    retry_multiplier = 1.0 / (1.0 - args.failure_rate)
    expected = round(base * retry_multiplier, 2)
    sample_stage = round(expected * 0.1, 2)
    status = "within_budget"
    if args.budget is not None and expected > args.budget:
        status = "exceeds_budget"
    elif args.budget is not None and expected > args.budget * 0.8:
        status = "near_budget_limit"

    print(
        json.dumps(
            {
                "base_cost": round(base, 2),
                "expected_cost_with_retries": expected,
                "retry_multiplier": round(retry_multiplier, 4),
                "recommended_10pct_pilot_cost": sample_stage,
                "budget": args.budget,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 2 if status == "exceeds_budget" else 0


if __name__ == "__main__":
    raise SystemExit(main())
