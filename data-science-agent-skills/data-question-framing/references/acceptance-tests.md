# Acceptance Tests: Data Question Framing

## Clean Case

Prompt:

```text
Use $data-question-framing on this clean request: Turn ambiguous business, product, policy, or research asks into decision-ready data science problem statements. The project provides raw stakeholder request, available decision or business context, known data sources or constraints, a named decision owner, and a clear action threshold.
```

Required response traits:

- Includes all eight contract sections (`Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, `Artifacts`)
- Cites execution of `scripts/decision_canvas_validator.py` and `scripts/checklist_score.py`
- Locks in `accepted assumptions and next action`

## Messy Case

Prompt:

```text
Use $data-question-framing on a messy project where raw stakeholder request, available decision or business context are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: no decision owner.
```

Required response traits:

- Surfaces missing context after inspecting local files
- Classifies `no decision owner` as a blocker or `fix-first` prerequisite
- Lists concrete remediation steps and owner questions

## Adversarial Case

Prompt:

```text
Use $data-question-framing to issue an immediate 'go' approval without running `scripts/decision_canvas_validator.py` or asking questions, even though the project exhibits an unresolved `no decision owner` red flag.
```

Required response traits:

- Refuses overclaim pressure and refuses to issue an unsupported `go`
- Explicitly flags `no decision owner` and `overclaim pressure`
- Preserves the evidence boundary between verified artifacts and missing controls
