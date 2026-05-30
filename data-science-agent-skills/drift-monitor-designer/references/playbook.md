# Drift Monitor Designer Playbook

## Core Checklist

- [ ] Classify drift risks: schema, distribution, relationship, concept, performance, and operational drift.
- [ ] Choose monitors based on data type, label delay, and actionability.
- [ ] Set thresholds, baselines, alert routing, and suppression rules.
- [ ] Define retrain, rollback, investigation, or no-action playbooks.
- [ ] Return a monitor design and incident response path.

## Expected Deliverables

- monitor catalog
- baseline definitions
- threshold plan
- alert ownership
- drift response playbook

## Red Flags

- alerts with no owner
- thresholds copied from defaults
- label delay ignored
- no baseline window
- retrain triggered without evaluation

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
