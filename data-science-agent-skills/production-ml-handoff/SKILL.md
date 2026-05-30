---
name: production-ml-handoff
description: Convert data science prototypes into engineering-ready ML handoffs with contracts, artifacts, SLOs, monitoring, and ownership. Use when Codex needs to handle data science workflows involving turn prototypes into engineering handoffs, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Production ML Handoff

## Mission

Convert data science prototypes into engineering-ready ML handoffs with contracts, artifacts, SLOs, monitoring, and ownership.

Current pain point: Engineering teams receive notebooks and model files without enough interface, operational, or rollback detail.

Why this skill exists: A handoff package prevents prototype ambiguity from becoming production fragility.


## What This Skill Must Do

- Convert the request into an explicit Production ML Handoff decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: prototype repo or notebook, model artifact, feature inputs, serving pattern.
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

- notebook is only artifact
- feature definitions ambiguous
- no rollback plan
- latency unknown
- owner unclear after launch

## Required Inputs

- prototype repo or notebook
- model artifact
- feature inputs
- serving pattern
- SLOs
- owners
- monitoring needs

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Define inference contract: inputs, outputs, types, thresholds, errors, latency, and privacy constraints.
2. Package artifacts, versioning, environment, and reproducibility evidence.
3. Specify deployment path, rollback, monitoring, alerting, and ownership.
4. Identify engineering blockers and unresolved research assumptions.
5. Return a handoff brief and acceptance checklist.

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
