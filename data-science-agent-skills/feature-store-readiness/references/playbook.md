# Feature Store Readiness Playbook

## Core Checklist

- [ ] Assess whether features need online serving, reuse, point-in-time correctness, or shared governance.
- [ ] Check training-serving skew, freshness, TTL, backfill, and ownership risks.
- [ ] Recommend no store, lightweight registry, batch feature table, or full feature store.
- [ ] Define feature contracts and lineage requirements.
- [ ] Return a readiness decision and migration plan.

## Expected Deliverables

- feature-store decision
- skew risk table
- feature contract outline
- TTL and freshness plan
- migration steps

## Red Flags

- same feature computed differently online
- freshness unknown
- no point-in-time join
- feature owner unclear
- feature store proposed without reuse

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
