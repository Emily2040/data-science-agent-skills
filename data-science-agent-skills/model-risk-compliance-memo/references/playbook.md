# Model Risk Compliance Memo Playbook

## Core Checklist

- [ ] Define model purpose, non-goals, user impact, and decision authority.
- [ ] Summarize data, training, evaluation, fairness, privacy, explainability, and limitations.
- [ ] Classify risks by severity, likelihood, detectability, and owner.
- [ ] Document controls, monitoring, rollback, and approval conditions.
- [ ] Return a memo with open blockers and required signoffs.

## Expected Deliverables

- model risk memo
- risk register
- control map
- approval conditions
- signoff checklist

## Red Flags

- affected users undefined
- no rollback owner
- fairness not evaluated where relevant
- privacy basis unclear
- monitoring absent

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
