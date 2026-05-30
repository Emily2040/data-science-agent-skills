# Playbook

## Decision This Skill Supports

Infer practical data contracts, schema expectations, and validation tests from messy real datasets.

## Evidence Checklist

- CSV, Parquet, JSONL, SQL schema, or sample extracts
- downstream use case
- known business rules
- refresh cadence

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Profile columns, nulls, uniqueness, cardinality, ranges, formats, and candidate keys.
2. Identify semantic expectations that cannot be inferred mechanically and mark them for owner confirmation.
3. Draft tests for schema, freshness, distribution, referential integrity, and accepted values.
4. Map each test to Great Expectations, Pandera, dbt, or plain SQL where appropriate.
5. Return a contract draft with confidence levels and confirmation questions.

## Decision Ladder

- `go`: evidence is sufficient and red flags are absent or accepted by the owner.
- `fix-first`: a concrete blocker can be remediated before continuing.
- `stop`: the work would be misleading, unsafe, unlawful, or untestable.
- `proceed-with-risk`: the owner accepts named risks and monitoring is specified.
- `needs-owner-review`: the agent cannot decide without a human owner.

## Evidence Table Template

| Finding | Evidence | Confidence | Owner action |
| --- | --- | --- | --- |
| Fill this row | File, query, metric, or observation | high/medium/low | go/fix/stop/review |

## Red Flags

- sample too small
- IDs not unique when assumed unique
- silent enum expansion
- date freshness inconsistent
- meaning cannot be inferred from name

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
