# Privacy Preserving Data Science Playbook

## Core Checklist

- [ ] Identify direct identifiers, quasi-identifiers, sensitive attributes, and linkage risks.
- [ ] Minimize fields and rows to the decision need.
- [ ] Choose local-first, aggregated, redacted, synthetic, federated, differential privacy, or secure enclave path.
- [ ] Define what can be exported, logged, cached, or shared.
- [ ] Return a privacy-safe analysis plan and residual risk note.

## Expected Deliverables

- PII and sensitivity inventory
- minimization plan
- safe-compute recommendation
- export rules
- residual-risk note

## Red Flags

- raw PII in notebook output
- unapproved cloud copy
- identifier kept for convenience
- synthetic data claimed risk-free
- exports not reviewed

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
