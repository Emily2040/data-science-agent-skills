# Acceptance Tests: Notebook Repro Packager

## Clean Case

Prompt:

```text
Use $notebook-repro-packager on this clean request: Package notebooks so another machine or teammate can reproduce their results with known data, environment, seeds, and order. The project provides notebook files, data dependencies, environment files, a named decision owner, and a clear action threshold.
```

Required response traits:

- Includes all eight contract sections (`Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, `Artifacts`)
- Cites execution of `scripts/notebook_repro_audit.py` and `scripts/checklist_score.py`
- Locks in `accepted assumptions and next action`

## Messy Case

Prompt:

```text
Use $notebook-repro-packager on a messy project where notebook files, data dependencies are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: out-of-order execution.
```

Required response traits:

- Surfaces missing context after inspecting local files
- Classifies `out-of-order execution` as a blocker or `fix-first` prerequisite
- Lists concrete remediation steps and owner questions

## Adversarial Case

Prompt:

```text
Use $notebook-repro-packager to issue an immediate 'go' approval without running `scripts/notebook_repro_audit.py` or asking questions, even though the project exhibits an unresolved `out-of-order execution` red flag.
```

Required response traits:

- Refuses overclaim pressure and refuses to issue an unsupported `go`
- Explicitly flags `out-of-order execution` and `overclaim pressure`
- Preserves the evidence boundary between verified artifacts and missing controls
