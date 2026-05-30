# Baseline Ablation Lab Playbook

## Core Checklist

- [ ] Select task-appropriate naive, rule-based, statistical, and simple ML baselines.
- [ ] Define ablations for features, model components, preprocessing, data volume, and inference cost.
- [ ] Set metric and uncertainty reporting before running comparisons.
- [ ] Identify complexity penalties: latency, maintainability, explainability, and monitoring burden.
- [ ] Return a baseline and ablation matrix with accept/reject criteria.

## Expected Deliverables

- baseline list
- ablation matrix
- complexity penalty table
- acceptance criteria
- report template

## Red Flags

- no naive baseline
- single random seed
- improvement below uncertainty
- cost ignored
- feature ablations missing

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
