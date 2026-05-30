---
name: missingness-mechanism-investigator
description: Diagnose missing-data mechanisms and design imputation, exclusion, or sensitivity plans. Use when Codex needs to handle data science workflows involving diagnose missing data before imputation, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Missingness Mechanism Investigator

## Mission

Diagnose missing-data mechanisms and design imputation, exclusion, or sensitivity plans.

Current pain point: Missing values are filled or dropped mechanically, creating bias and false confidence.

Why this skill exists: MCAR, MAR, and MNAR require different assumptions; the skill forces mechanism thinking before imputation.

## Required Inputs

- dataset
- analysis goal
- column meanings
- collection process
- known reasons for missingness

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Profile missingness by column, row, group, time, and target relationship.
2. Classify likely mechanisms as MCAR, MAR, MNAR, structural missing, or unknown.
3. Identify whether missingness itself should be a feature, exclusion reason, or bias warning.
4. Recommend complete-case, imputation, indicator, model-based, or sensitivity strategy.
5. Return a missingness report with assumptions and impact on claims.

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
