#!/usr/bin/env python3
"""Compute two-arm minimum detectable effect (MDE), sample-per-arm requirement, and events-per-variable ratio."""
from __future__ import annotations

import argparse
import json
import math


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-per-arm", type=int, required=True)
    parser.add_argument("--baseline-std", type=float, default=1.0)
    parser.add_argument("--features", type=int, default=5)
    parser.add_argument("--events", type=int, default=100)
    args = parser.parse_args()

    if args.n_per_arm < 2 or args.baseline_std <= 0 or args.features < 1:
        print(json.dumps({"status": "invalid_input"}, indent=2))
        return 2

    # Normal approximation for alpha=0.05 (two-sided z=1.96) and power=0.80 (z=0.84) -> factor 2.80
    mde = 2.80 * args.baseline_std * math.sqrt(2.0 / args.n_per_arm)
    epv = args.events / args.features
    issues: list[str] = []
    if epv < 10.0:
        issues.append("events_per_variable_below_10_overfitting_risk")
    if args.n_per_arm < 30:
        issues.append("small_arm_sample_use_exact_or_hierarchical_test")

    status = "adequately_powered" if not issues else "high_overfit_or_underpowered_risk"
    print(
        json.dumps(
            {
                "n_per_arm": args.n_per_arm,
                "mde_80pct_power_alpha_05": round(mde, 4),
                "events_per_variable": round(epv, 2),
                "issues": issues,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "adequately_powered" else 2


if __name__ == "__main__":
    raise SystemExit(main())
