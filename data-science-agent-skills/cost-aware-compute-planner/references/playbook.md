# Cost Aware Compute Planner Playbook

## Core Checklist

- [ ] Estimate minimum useful experiment scale and define sample-first gates.
- [ ] Compare local CPU, local GPU, cloud CPU, cloud GPU, batch, and spot options.
- [ ] Plan caching, early stopping, checkpointing, and parallelism.
- [ ] Set budget guardrails and cost per experiment or inference unit.
- [ ] Return a compute plan with stop rules and escalation thresholds.

## Expected Deliverables

- compute option matrix
- sample-first plan
- budget guardrails
- stop rules
- cost-risk memo

## Red Flags

- full-data first run
- no budget owner
- idle GPU notebooks
- inference cost ignored
- training cheaper than monitoring is assumed

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
