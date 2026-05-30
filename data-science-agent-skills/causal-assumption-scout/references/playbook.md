# Causal Assumption Scout Playbook

## Core Checklist

- [ ] Rewrite the claim as prediction, association, or causal effect.
- [ ] Define treatment, outcome, population, time window, and estimand.
- [ ] Draft a DAG-level assumption map and confounder inventory.
- [ ] Recommend experiment, quasi-experiment, matching, weighting, regression, or do-not-claim-causality.
- [ ] Return language that is safe for stakeholders and a sensitivity plan.

## Expected Deliverables

- causal claim rewrite
- assumption map
- confounder checklist
- method recommendation
- safe-language memo

## Red Flags

- no intervention
- post-treatment controls
- selection bias
- unmeasured confounders
- effect framed after seeing results

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
