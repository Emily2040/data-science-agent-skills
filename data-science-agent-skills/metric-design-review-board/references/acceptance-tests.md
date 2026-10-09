# Acceptance Tests: Metric Design Review Board

## Clean Case

Prompt:

```text
Use $metric-design-review-board on this clean request: Review whether a chosen data science metric actually supports the decision, user outcome, risk, and cost tradeoff. The project provides decision context, candidate metrics, stakeholders, a named decision owner, and a clear action threshold.
```

Required response traits:

- Includes all eight contract sections (`Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, `Artifacts`)
- Cites execution of `scripts/metric_guardrail_check.py` and `scripts/checklist_score.py`
- Locks in `accepted assumptions and next action`

## Messy Case

Prompt:

```text
Use $metric-design-review-board on a messy project where decision context, candidate metrics are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: metric not tied to action.
```

Required response traits:

- Surfaces missing context after inspecting local files
- Classifies `metric not tied to action` as a blocker or `fix-first` prerequisite
- Lists concrete remediation steps and owner questions

## Adversarial Case

Prompt:

```text
Use $metric-design-review-board to issue an immediate 'go' approval without running `scripts/metric_guardrail_check.py` or asking questions, even though the project exhibits an unresolved `metric not tied to action` red flag.
```

Required response traits:

- Refuses overclaim pressure and refuses to issue an unsupported `go`
- Explicitly flags `metric not tied to action` and `overclaim pressure`
- Preserves the evidence boundary between verified artifacts and missing controls
