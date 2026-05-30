---
name: dataset-contract-forensics
description: Infer practical data contracts, schema expectations, and validation tests from messy real datasets. Use when Codex needs to handle data science workflows involving infer contracts and tests from messy data, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Dataset Contract Forensics

## Mission

Infer practical data contracts, schema expectations, and validation tests from messy real datasets.

Current pain point: Data breaks downstream because implicit assumptions about schema, meaning, ranges, uniqueness, and freshness are never written down.

Why this skill exists: Forensic contract inference converts observed data behavior into explicit tests that can be reviewed and automated.


## What This Skill Must Do

- Convert the request into an explicit Dataset Contract Forensics decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: CSV, Parquet, JSONL, SQL schema, or sample extracts, downstream use case, known business rules, refresh cadence.
- Separate mechanical checks from judgment calls so another reviewer can audit the result.
- Return a decision-ready artifact with risks, owner questions, and the smallest next action.
- Refuse to hide uncertainty. Mark unknown, not applicable, and needs human owner review as separate states.

## Detailed Execution Rules

- Start by restating the decision this skill is meant to support.
- Inspect local artifacts before asking the user for missing context.
- Treat script output as evidence, not as the full answer.
- Preserve raw evidence and avoid silent mutation.
- Classify each blocker as stop, fix-first, monitor, accepted risk, or owner decision.
- Produce an artifact that another agent or human can review without hidden context.

## Red Flags

- sample too small
- IDs not unique when assumed unique
- silent enum expansion
- date freshness inconsistent
- meaning cannot be inferred from name

## Required Inputs

- CSV, Parquet, JSONL, SQL schema, or sample extracts
- downstream use case
- known business rules
- refresh cadence

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Profile columns, nulls, uniqueness, cardinality, ranges, formats, and candidate keys.
2. Identify semantic expectations that cannot be inferred mechanically and mark them for owner confirmation.
3. Draft tests for schema, freshness, distribution, referential integrity, and accepted values.
4. Map each test to Great Expectations, Pandera, dbt, or plain SQL where appropriate.
5. Return a contract draft with confidence levels and confirmation questions.

## Resources

- Read `references/playbook.md` for the skill-specific checklist, decision rules, and failure modes.
- Read `references/acceptance-tests.md` when validating or forward-testing the skill.
- Read `references/infographic-spec.md` when creating the Reddit visual or social post.
- Use scripts in `scripts/` only on local files or explicit user-provided artifacts. Do not upload private data to external services.

## Output Contract

Return these sections unless the user requests another format:

- `Problem`: the decision, artifact, or workflow being handled.
- `Inputs`: files, data, assumptions, and missing context used.
- `Checks performed`: concrete inspections, scripts, and reasoning checks.
- `Findings`: prioritized observations with evidence.
- `Decision`: go, fix-first, stop, or proceed-with-risk recommendation.
- `Risks`: unresolved blockers, caveats, and owner decisions.
- `Next actions`: smallest useful follow-up steps.
- `Artifacts`: generated files, specs, or scripts.

## Final Checks

- Do not overclaim beyond available evidence.
- Mark assumptions explicitly instead of hiding them in prose.
- Prefer simple, auditable recommendations over impressive but fragile tooling.
- Preserve raw data and original artifacts unless the user explicitly asks for mutation.
- Keep the final answer short enough for a decision owner to act on.
