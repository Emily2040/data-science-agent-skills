#!/usr/bin/env python3
"""Audit a causal specification JSON for post-treatment controls, colliders, and unmeasured confounders."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec_json", help="JSON with treatment, outcome, controls, post_treatment, colliders, unmeasured_confounders")
    args = parser.parse_args()

    spec = json.loads(Path(args.spec_json).read_text(encoding="utf-8"))
    controls = set(spec.get("controls", []))
    post_treatment = set(spec.get("post_treatment", []))
    colliders = set(spec.get("colliders", []))
    unmeasured = list(spec.get("unmeasured_confounders", []))
    design = str(spec.get("design", "observational")).lower()

    bad_post = sorted(controls & post_treatment)
    bad_colliders = sorted(controls & colliders)
    issues: list[str] = []
    if not spec.get("treatment") or not spec.get("outcome"):
        issues.append("missing_treatment_or_outcome")
    if bad_post:
        issues.append("post_treatment_variables_in_controls")
    if bad_colliders:
        issues.append("collider_conditioning_detected")
    if design == "observational" and unmeasured:
        issues.append("unmeasured_confounders_present")

    status = "blocked" if (bad_post or bad_colliders or "missing_treatment_or_outcome" in issues) else ("associational_only" if issues else "causal_identification_plausible")
    print(
        json.dumps(
            {
                "design": design,
                "post_treatment_conditioned": bad_post,
                "colliders_conditioned": bad_colliders,
                "unmeasured_confounders": unmeasured,
                "issues": issues,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "causal_identification_plausible" else 2


if __name__ == "__main__":
    raise SystemExit(main())
