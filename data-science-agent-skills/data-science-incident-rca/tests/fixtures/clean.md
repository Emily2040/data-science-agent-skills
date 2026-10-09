# Clean Fixture: `data-science-incident-rca`

Prompt:

```text
Use $data-science-incident-rca on this clean request: Run root-cause analysis for broken models, metrics, dashboards, pipelines, and data science decisions. The project provides incident symptom, time first observed, affected outputs, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/incident_timeline_correlator.py path/to/incident_events.json
```

Expected decision: `go` (with documented assumptions and next action).
