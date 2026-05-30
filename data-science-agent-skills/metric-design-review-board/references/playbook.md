# Metric Design Review Board Playbook

## Core Checklist

- [ ] Map metrics to the real decision and affected user or entity.
- [ ] Separate primary, diagnostic, fairness, reliability, and guardrail metrics.
- [ ] Review threshold effects, class imbalance, cost asymmetry, and gaming risk.
- [ ] Check offline-online and proxy-outcome mismatch.
- [ ] Return a metric board decision with acceptance and monitoring criteria.

## Expected Deliverables

- metric tree
- cost curve notes
- guardrail list
- threshold recommendation
- metric risk memo

## Red Flags

- metric not tied to action
- proxy metric can be gamed
- threshold chosen after results
- guardrails missing
- average hides subgroup harm

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
