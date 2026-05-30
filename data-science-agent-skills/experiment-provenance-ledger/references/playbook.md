# Experiment Provenance Ledger Playbook

## Core Checklist

- [ ] Capture code version, dirty state, environment, data references, parameters, seeds, and runtime.
- [ ] Record metrics and artifacts with owner, purpose, and retention expectation.
- [ ] Link human decisions, exclusions, and model-selection rationale.
- [ ] Map entries to MLflow, DVC, W&B, or plain JSON depending on the stack.
- [ ] Return a ledger and missing-provenance risk list.

## Expected Deliverables

- provenance ledger
- artifact manifest
- decision log
- tool mapping
- audit gaps

## Red Flags

- unversioned dataset
- dirty code used for final metric
- missing seed
- manual artifact rename
- model chosen without logged rationale

## Decision Rules

- `go`: critical evidence is available, risks are owned, and the next action is reversible or monitored.
- `fix-first`: the work is valuable but at least one blocker must be remediated before modeling, launch, or stakeholder use.
- `stop`: the request is misframed, unsafe, untestable, or materially misleading with available evidence.
- `proceed-with-risk`: the user accepts named risks and the report includes monitoring or rollback conditions.

## Evidence Discipline

- Tie every recommendation to a file, metric, stakeholder claim, or explicit assumption.
- Separate mechanically observed facts from expert judgment.
- Use uncertainty language when the evidence is partial.
- Record unresolved owner questions rather than filling gaps with confident guesses.
