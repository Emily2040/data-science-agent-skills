# Production ML Handoff Playbook

## Core Checklist

- [ ] Define inference contract: inputs, outputs, types, thresholds, errors, latency, and privacy constraints.
- [ ] Package artifacts, versioning, environment, and reproducibility evidence.
- [ ] Specify deployment path, rollback, monitoring, alerting, and ownership.
- [ ] Identify engineering blockers and unresolved research assumptions.
- [ ] Return a handoff brief and acceptance checklist.

## Expected Deliverables

- API or batch contract
- artifact manifest
- SLO and monitoring plan
- rollback plan
- handoff acceptance checklist

## Red Flags

- notebook is only artifact
- feature definitions ambiguous
- no rollback plan
- latency unknown
- owner unclear after launch

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
