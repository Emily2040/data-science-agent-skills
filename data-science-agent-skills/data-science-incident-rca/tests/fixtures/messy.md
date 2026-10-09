# Messy Fixture: `data-science-incident-rca`

Prompt:

```text
Use $data-science-incident-rca on a messy project where incident symptom, time first observed are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: no timestamped evidence.
```

Expected deterministic check:

```bash
python scripts/incident_timeline_correlator.py path/to/incident_events.json
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `no timestamped evidence` in `Findings` and `Risks`).
