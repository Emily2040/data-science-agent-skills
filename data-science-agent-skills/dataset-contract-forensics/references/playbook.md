# Dataset Contract Forensics Playbook

## Core Checklist

- [ ] Profile columns, nulls, uniqueness, cardinality, ranges, formats, and candidate keys.
- [ ] Identify semantic expectations that cannot be inferred mechanically and mark them for owner confirmation.
- [ ] Draft tests for schema, freshness, distribution, referential integrity, and accepted values.
- [ ] Map each test to Great Expectations, Pandera, dbt, or plain SQL where appropriate.
- [ ] Return a contract draft with confidence levels and confirmation questions.

## Expected Deliverables

- contract draft
- test inventory
- confidence labels
- owner questions
- tool-specific implementation hints

## Red Flags

- sample too small
- IDs not unique when assumed unique
- silent enum expansion
- date freshness inconsistent
- meaning cannot be inferred from name

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
