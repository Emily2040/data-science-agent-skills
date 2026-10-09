#!/usr/bin/env python3
"""Evaluate model governance risk tier and release readiness from a structured risk memo JSON."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_CONTROLS = ("rollback_owner", "fallback_policy", "affected_population", "monitoring_sla", "fairness_eval_completed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("risk_json")
    args = parser.parse_args()

    data = json.loads(Path(args.risk_json).read_text(encoding="utf-8"))
    missing = [k for k in REQUIRED_CONTROLS if not data.get(k)]
    automated_high_impact = bool(data.get("automated_high_impact_decision", False))
    human_override = bool(data.get("human_override_enabled", False))

    blockers: list[str] = list(missing)
    if automated_high_impact and not human_override:
        blockers.append("high_impact_automation_without_human_override")

    status = "go" if not blockers else "blocked"
    print(
        json.dumps(
            {
                "risk_tier": "high" if automated_high_impact else "standard",
                "missing_or_failed_controls": blockers,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "go" else 2


if __name__ == "__main__":
    raise SystemExit(main())
