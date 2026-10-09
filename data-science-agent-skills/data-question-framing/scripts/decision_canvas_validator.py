#!/usr/bin/env python3
"""Validate that a problem-framing JSON canvas has an owner, action threshold, unit, target, and guardrails."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_FIELDS = ("decision_owner", "decision_action", "analysis_unit", "target_definition", "time_horizon", "primary_metric", "action_threshold")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("canvas_json", help="Path to decision canvas JSON")
    args = parser.parse_args()

    data = json.loads(Path(args.canvas_json).read_text(encoding="utf-8"))
    missing = [f for f in REQUIRED_FIELDS if not str(data.get(f, "")).strip()]
    guardrails = list(data.get("guardrail_metrics", []))
    target_available = bool(data.get("target_available_at_decision_time", True))

    issues: list[str] = []
    if missing:
        issues.append("missing_required_framing_fields")
    if not guardrails:
        issues.append("missing_guardrail_metrics")
    if not target_available:
        issues.append("target_unavailable_at_decision_time")

    status = "go" if not issues else ("stop" if not target_available or "decision_owner" in missing else "fix-first")
    print(
        json.dumps(
            {
                "missing_fields": missing,
                "guardrail_count": len(guardrails),
                "target_available_at_decision_time": target_available,
                "issues": issues,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "go" else 2


if __name__ == "__main__":
    raise SystemExit(main())
