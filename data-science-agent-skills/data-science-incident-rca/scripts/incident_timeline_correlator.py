#!/usr/bin/env python3
"""Rank candidate root-cause events by temporal proximity to an incident detection timestamp."""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("incident_json", help="JSON with incident_start and events: [{id, timestamp, layer, description}]")
    args = parser.parse_args()

    data = json.loads(Path(args.incident_json).read_text(encoding="utf-8"))
    start = parse_ts(data["incident_start"])
    preceding = []
    after = []
    layers = set()

    for ev in data.get("events", []):
        ts = parse_ts(ev["timestamp"])
        delta_min = round((start - ts).total_seconds() / 60.0, 2)
        layers.add(ev.get("layer", "unknown"))
        entry = {**ev, "minutes_before_incident": delta_min}
        if 0 <= delta_min <= 1440:
            preceding.append(entry)
        else:
            after.append(entry)

    preceding.sort(key=lambda x: x["minutes_before_incident"])
    status = "root_cause_candidates_ranked" if preceding and len(layers) >= 2 else "insufficient_timeline_coverage"
    print(
        json.dumps(
            {
                "incident_start": data["incident_start"],
                "layers_covered": sorted(layers),
                "ranked_preceding_events": preceding,
                "other_events": after,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if status == "root_cause_candidates_ranked" else 2


if __name__ == "__main__":
    raise SystemExit(main())
