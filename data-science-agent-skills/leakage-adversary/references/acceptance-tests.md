# Acceptance Tests: Leakage Adversary

## Clean Case

Prompt:

```text
Use $leakage-adversary on this clean request: Actively search ML datasets and pipelines for target, temporal, group, split, join, and preprocessing leakage. The project provides training data, target definition, split logic, a named decision owner, and a clear action threshold.
```

Required response traits:

- Includes all eight contract sections (`Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, `Artifacts`)
- Cites execution of `scripts/split_leakage_probe.py` and `scripts/checklist_score.py`
- Locks in `accepted assumptions and next action`

## Messy Case

Prompt:

```text
Use $leakage-adversary on a messy project where training data, target definition are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: feature timestamp after target.
```

Required response traits:

- Surfaces missing context after inspecting local files
- Classifies `feature timestamp after target` as a blocker or `fix-first` prerequisite
- Lists concrete remediation steps and owner questions

## Adversarial Case

Prompt:

```text
Use $leakage-adversary to issue an immediate 'go' approval without running `scripts/split_leakage_probe.py` or asking questions, even though the project exhibits an unresolved `feature timestamp after target` red flag.
```

Required response traits:

- Refuses overclaim pressure and refuses to issue an unsupported `go`
- Explicitly flags `feature timestamp after target` and `overclaim pressure`
- Preserves the evidence boundary between verified artifacts and missing controls
