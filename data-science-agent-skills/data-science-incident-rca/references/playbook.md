# Data Science Incident RCA Playbook

## Core Checklist

- [ ] Define symptom, detection path, start time, severity, and affected users or decisions.
- [ ] Build timeline across data sources, pipelines, code, model, dashboard, and human changes.
- [ ] Separate root cause, contributing factors, detection gaps, and impact.
- [ ] Recommend immediate mitigation, durable prevention, monitoring, and ownership updates.
- [ ] Return an RCA memo with evidence and countermeasures.

## Expected Deliverables

- incident timeline
- blast radius
- root cause memo
- countermeasure plan
- monitoring changes

## Red Flags

- no timestamped evidence
- only one layer investigated
- impact not quantified
- human process omitted
- countermeasure lacks owner

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
