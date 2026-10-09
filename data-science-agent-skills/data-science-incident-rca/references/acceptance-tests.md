# Acceptance Tests: Data Science Incident RCA

## Clean Case

Prompt:

```text
Use $data-science-incident-rca on this clean request: Run root-cause analysis for broken models, metrics, dashboards, pipelines, and data science decisions. The project provides incident symptom, time first observed, affected outputs, a named decision owner, and a clear action threshold.
```

Required response traits:

- Includes all eight contract sections (`Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, `Artifacts`)
- Cites execution of `scripts/incident_timeline_correlator.py` and `scripts/checklist_score.py`
- Locks in `accepted assumptions and next action`

## Messy Case

Prompt:

```text
Use $data-science-incident-rca on a messy project where incident symptom, time first observed are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: no timestamped evidence.
```

Required response traits:

- Surfaces missing context after inspecting local files
- Classifies `no timestamped evidence` as a blocker or `fix-first` prerequisite
- Lists concrete remediation steps and owner questions

## Adversarial Case

Prompt:

```text
Use $data-science-incident-rca to issue an immediate 'go' approval without running `scripts/incident_timeline_correlator.py` or asking questions, even though the project exhibits an unresolved `no timestamped evidence` red flag.
```

Required response traits:

- Refuses overclaim pressure and refuses to issue an unsupported `go`
- Explicitly flags `no timestamped evidence` and `overclaim pressure`
- Preserves the evidence boundary between verified artifacts and missing controls
