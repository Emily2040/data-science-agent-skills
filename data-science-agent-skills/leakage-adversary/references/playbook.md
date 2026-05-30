# Leakage Adversary Playbook

## Core Checklist

- [ ] Restate what information is available at decision time.
- [ ] Probe features, joins, encoders, aggregations, and preprocessing for post-outcome information.
- [ ] Check split logic for temporal bleed, group overlap, duplicated entities, and near-duplicates.
- [ ] Review suspiciously strong features and validation performance jumps.
- [ ] Return leakage findings with severity, evidence, and safer split or feature alternatives.

## Expected Deliverables

- leakage attack report
- feature risk table
- split risk table
- safe evaluation recommendation
- blocker list

## Red Flags

- feature timestamp after target
- same user in train and test
- global preprocessing before split
- leaky aggregate
- near-perfect simple model

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
