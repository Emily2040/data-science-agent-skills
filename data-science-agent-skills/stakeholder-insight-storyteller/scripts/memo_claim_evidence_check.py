#!/usr/bin/env python3
"""Audit an executive insight memo JSON for decision ask, uncertainty bounds, caveats, and evidence links."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = ("decision_ask", "decision_owner", "headline_finding", "uncertainty_interval", "key_caveat", "supporting_artifacts")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("memo_json")
    args = parser.parse_args()

    memo = json.loads(Path(args.memo_json).read_text(encoding="utf-8"))
    missing = [k for k in REQUIRED if not memo.get(k)]
    causal_wording = any(w in str(memo.get("headline_finding", "")).lower() for w in ("caused", "proves that", "guaranteed"))
    observational = str(memo.get("study_design", "observational")).lower() == "observational"

    issues = list(missing)
    if causal_wording and observational:
        issues.append("causal_claim_from_observational_design")

    status = "decision_memo_ready" if not issues else "revise_before_executive_readout"
    print(
        json.dumps(
            {
                "missing_elements": missing,
                "issues": issues,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "decision_memo_ready" else 2


if __name__ == "__main__":
    raise SystemExit(main())
