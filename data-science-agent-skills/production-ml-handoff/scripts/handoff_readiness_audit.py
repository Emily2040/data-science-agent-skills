#!/usr/bin/env python3
"""Verify that a production ML handoff bundle manifest contains schema, SLA, rollback, and owner contracts."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_KEYS = (
    "model_artifact_sha256",
    "input_schema",
    "output_schema",
    "latency_p99_ms_budget",
    "fallback_baseline",
    "oncall_owner",
    "rollback_trigger",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("handoff_json")
    args = parser.parse_args()

    bundle = json.loads(Path(args.handoff_json).read_text(encoding="utf-8"))
    missing = [k for k in REQUIRED_KEYS if bundle.get(k) in (None, "", [], {})]
    notebook_only = bool(bundle.get("notebook_is_only_artifact", False))
    if notebook_only:
        missing.append("notebook_only_no_packaged_entrypoint")

    status = "ready_for_handoff" if not missing else "fix-first"
    print(
        json.dumps(
            {
                "missing_handoff_requirements": missing,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "ready_for_handoff" else 2


if __name__ == "__main__":
    raise SystemExit(main())
