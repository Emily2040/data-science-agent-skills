# AI Data Readiness Triage Playbook

## Core Checklist

- [ ] Inventory access, ownership, lineage, refresh cadence, privacy, and retention constraints.
- [ ] Profile quality, missingness, duplication, outliers, type drift, and label coverage.
- [ ] Score readiness across governance, quality, representativeness, reproducibility, and operational fit.
- [ ] Classify blockers as stop, fix-first, monitor, or accepted risk.
- [ ] Return a readiness scorecard with the smallest credible next action.

## Expected Deliverables

- readiness scorecard
- blocker register
- minimum remediation plan
- label and privacy notes
- go/no-go recommendation

## Red Flags

- unknown owner
- no label source
- PII without approved use
- high missingness in core fields
- freshness mismatched to decision cycle

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
