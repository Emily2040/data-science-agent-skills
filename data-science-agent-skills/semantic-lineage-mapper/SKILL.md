---
name: semantic-lineage-mapper
description: Reconstruct practical lineage across SQL, notebooks, scripts, dashboards, model artifacts, and pipeline configs. Use when Codex needs to handle data science workflows involving rebuild lineage from sql, notebooks, and configs, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Semantic Lineage Mapper

## Mission

Reconstruct practical lineage across SQL, notebooks, scripts, dashboards, model artifacts, and pipeline configs.

Current pain point: Teams cannot explain where a metric, feature, or model input came from after it breaks or is challenged.

Why this skill exists: Lineage mapping combines static extraction with semantic owner questions so blind spots are visible instead of assumed away.


## What This Skill Must Do

- Convert the request into an explicit Semantic Lineage Mapper decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: SQL files, notebooks, pipeline configs, dashboard definitions.
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

- dashboard-only metric logic
- manual spreadsheet hop
- feature generated outside pipeline
- PII source unclear
- ownerless table

## Required Inputs

- SQL files
- notebooks
- pipeline configs
- dashboard definitions
- model feature lists

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Extract table, column, file, feature, model, and artifact references.
2. Group references into sources, transforms, outputs, and decision surfaces.
3. Mark unknown or manually managed dependencies instead of dropping them.
4. Identify high-risk nodes: ownerless, PII, stale, reused, or weakly documented.
5. Return a lineage map, risk register, and confirmation checklist.

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
