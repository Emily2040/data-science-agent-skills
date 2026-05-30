#!/usr/bin/env python3
"""Estimate rough compute cost from hourly rates and planned runtime."""
from __future__ import annotations

import argparse
import json


def main() -> int:
    parser = argparse.ArgumentParser(description="Estimate experiment compute budget.")
    parser.add_argument("--hourly-rate", type=float, required=True)
    parser.add_argument("--hours-per-run", type=float, required=True)
    parser.add_argument("--runs", type=int, required=True)
    parser.add_argument("--failure-rate", type=float, default=0.15, help="Expected failed/retry fraction, 0 to 1.")
    parser.add_argument("--storage-monthly", type=float, default=0.0)
    args = parser.parse_args()
    retry_multiplier = 1.0 + max(0.0, min(args.failure_rate, 1.0))
    compute = args.hourly_rate * args.hours_per_run * args.runs * retry_multiplier
    total = compute + args.storage_monthly
    result = {
        "compute_cost": round(compute, 2),
        "storage_monthly": round(args.storage_monthly, 2),
        "total_estimate": round(total, 2),
        "retry_multiplier": round(retry_multiplier, 2),
        "cost_per_successful_run": round(total / max(args.runs, 1), 2),
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
