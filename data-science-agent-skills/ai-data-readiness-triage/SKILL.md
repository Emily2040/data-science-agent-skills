---
name: ai-data-readiness-triage
description: Assess whether a dataset or data domain is ready for AI, analytics, or modeling before a project commits time and budget. Use when Codex needs to handle data science workflows involving score whether data is usable for ai work, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# AI Data Readiness Triage

## Mission

Assess whether a dataset or data domain is ready for AI, analytics, or modeling before a project commits time and budget.

Current pain point: AI projects stall because access, freshness, quality, lineage, privacy, labels, and ownership are discovered too late.

Why this skill exists: Readiness scoring gives leaders a hard go, fix-first, or stop decision instead of optimistic prototype theater.

## Required Inputs

- dataset paths or schemas
- data owner
- intended use case
- privacy or compliance constraints
- label or ground-truth plan

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Inventory access, ownership, lineage, refresh cadence, privacy, and retention constraints.
2. Profile quality, missingness, duplication, outliers, type drift, and label coverage.
3. Score readiness across governance, quality, representativeness, reproducibility, and operational fit.
4. Classify blockers as stop, fix-first, monitor, or accepted risk.
5. Return a readiness scorecard with the smallest credible next action.

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
