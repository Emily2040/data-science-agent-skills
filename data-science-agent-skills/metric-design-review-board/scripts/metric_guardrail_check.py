#!/usr/bin/env python3
"""Audit a metric architecture JSON specification for denominator clarity, gaming vectors, and guardrails."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("metric_spec_json")
    args = parser.parse_args()

    spec = json.loads(Path(args.metric_spec_json).read_text(encoding="utf-8"))
    primary = spec.get("primary_metric", {})
    guardrails = list(spec.get("guardrail_metrics", []))

    issues: list[str] = []
    if not primary.get("name") or not primary.get("denominator") or not primary.get("window"):
        issues.append("primary_metric_missing_denominator_or_window")
    if not primary.get("decision_owner"):
        issues.append("primary_metric_missing_owner")
    if len(guardrails) < 1:
        issues.append("no_guardrail_metrics_defined")
    if not spec.get("gaming_scenarios"):
        issues.append("gaming_scenarios_not_documented")

    status = "pass" if not issues else "needs_metric_revision"
    print(
        json.dumps(
            {
                "primary_metric": primary.get("name"),
                "guardrail_count": len(guardrails),
                "issues": issues,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
