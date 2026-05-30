# Small Data Power Planner Playbook

## Core Checklist

- [ ] Identify the decision and minimum useful effect size.
- [ ] Estimate signal limits, imbalance, uncertainty, and variance risks.
- [ ] Recommend descriptive, Bayesian, resampling, regularized, or data-collection paths.
- [ ] Define validation limits and language for uncertainty.
- [ ] Return a do-model, simplify, or collect-more recommendation.

## Expected Deliverables

- power and uncertainty note
- baseline plan
- validation limits
- collection recommendation
- safe communication text

## Red Flags

- more features than observations
- rare outcome with random split
- single holdout set only
- unreported uncertainty
- high-stakes decision from tiny sample

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
