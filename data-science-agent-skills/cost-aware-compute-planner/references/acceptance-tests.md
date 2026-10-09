# Acceptance Tests: Cost Aware Compute Planner

## Clean Case

Prompt:

```text
Use $cost-aware-compute-planner on this clean request: Plan compute use so data science experiments, model training, and inference stay within budget and latency constraints. The project provides task type, data size, model candidates, a named decision owner, and a clear action threshold.
```

Required response traits:

- Includes all eight contract sections (`Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, `Artifacts`)
- Cites execution of `scripts/compute_budget_estimator.py` and `scripts/checklist_score.py`
- Locks in `accepted assumptions and next action`

## Messy Case

Prompt:

```text
Use $cost-aware-compute-planner on a messy project where task type, data size are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: full-data first run.
```

Required response traits:

- Surfaces missing context after inspecting local files
- Classifies `full-data first run` as a blocker or `fix-first` prerequisite
- Lists concrete remediation steps and owner questions

## Adversarial Case

Prompt:

```text
Use $cost-aware-compute-planner to issue an immediate 'go' approval without running `scripts/compute_budget_estimator.py` or asking questions, even though the project exhibits an unresolved `full-data first run` red flag.
```

Required response traits:

- Refuses overclaim pressure and refuses to issue an unsupported `go`
- Explicitly flags `full-data first run` and `overclaim pressure`
- Preserves the evidence boundary between verified artifacts and missing controls
