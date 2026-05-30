# Missingness Mechanism Investigator Playbook

## Core Checklist

- [ ] Profile missingness by column, row, group, time, and target relationship.
- [ ] Classify likely mechanisms as MCAR, MAR, MNAR, structural missing, or unknown.
- [ ] Identify whether missingness itself should be a feature, exclusion reason, or bias warning.
- [ ] Recommend complete-case, imputation, indicator, model-based, or sensitivity strategy.
- [ ] Return a missingness report with assumptions and impact on claims.

## Expected Deliverables

- missingness heat map summary
- mechanism labels
- imputation plan
- sensitivity plan
- claim limitations

## Red Flags

- target-dependent missingness
- structural missing treated as random
- imputed identifiers
- dropped rows change population
- no collection-process explanation

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
