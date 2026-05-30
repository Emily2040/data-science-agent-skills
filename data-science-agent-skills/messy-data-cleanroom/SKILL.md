---
name: messy-data-cleanroom
description: Design transparent, reversible cleaning plans for messy datasets without silently mutating evidence. Use when Codex needs to handle data science workflows involving design reversible data cleaning plans, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Messy Data Cleanroom

## Mission

Design transparent, reversible cleaning plans for messy datasets without silently mutating evidence.

Current pain point: Cleaning decisions get buried in notebooks, making results impossible to audit or reproduce.

Why this skill exists: A cleanroom workflow treats every transformation as a logged proposal with reason, risk, and reversal path.

## Required Inputs

- raw dataset
- data dictionary if available
- analysis goal
- allowed transformation constraints

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Profile missingness, duplicates, outliers, types, formats, units, and conflicting records.
2. Separate factual corrections, normalization, exclusions, imputations, and unresolved anomalies.
3. For each proposed transformation, record rationale, affected rows, risk, and reversal method.
4. Prefer derived clean columns or versioned outputs over overwriting raw evidence.
5. Return a cleaning ledger and transformed-data acceptance criteria.

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
