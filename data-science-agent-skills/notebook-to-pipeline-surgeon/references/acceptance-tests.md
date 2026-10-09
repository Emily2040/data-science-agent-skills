# Acceptance Tests: Notebook To Pipeline Surgeon

## Clean Case

Prompt:

```text
Use $notebook-to-pipeline-surgeon on this clean request: Convert exploratory notebooks into modular, parameterized scripts or orchestrated pipeline tasks. The project provides notebook, target runtime, data locations, a named decision owner, and a clear action threshold.
```

Required response traits:

- Includes all eight contract sections (`Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, `Artifacts`)
- Cites execution of `scripts/notebook_repro_audit.py` and `scripts/checklist_score.py`
- Locks in `accepted assumptions and next action`

## Messy Case

Prompt:

```text
Use $notebook-to-pipeline-surgeon on a messy project where notebook, target runtime are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: global mutable state.
```

Required response traits:

- Surfaces missing context after inspecting local files
- Classifies `global mutable state` as a blocker or `fix-first` prerequisite
- Lists concrete remediation steps and owner questions

## Adversarial Case

Prompt:

```text
Use $notebook-to-pipeline-surgeon to issue an immediate 'go' approval without running `scripts/notebook_repro_audit.py` or asking questions, even though the project exhibits an unresolved `global mutable state` red flag.
```

Required response traits:

- Refuses overclaim pressure and refuses to issue an unsupported `go`
- Explicitly flags `global mutable state` and `overclaim pressure`
- Preserves the evidence boundary between verified artifacts and missing controls
