---
name: drift-monitor-designer
description: Design drift monitoring for production models and data products across data, concept, performance, and operational signals. Use when Codex needs to handle data science workflows involving design data, concept, and performance drift monitors, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Drift Monitor Designer

## Mission

Design drift monitoring for production models and data products across data, concept, performance, and operational signals.

Current pain point: Models degrade silently because teams monitor uptime but not input, label, behavior, or outcome change.

Why this skill exists: Monitoring must match label delay, business risk, retraining options, and alert ownership.


## What This Skill Must Do

- Convert the request into an explicit Drift Monitor Designer decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: model purpose, features, prediction logs, label availability.
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

- alerts with no owner
- thresholds copied from defaults
- label delay ignored
- no baseline window
- retrain triggered without evaluation

## Required Inputs

- model purpose
- features
- prediction logs
- label availability
- risk tolerance
- owners
- retrain process

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Classify drift risks: schema, distribution, relationship, concept, performance, and operational drift.
2. Choose monitors based on data type, label delay, and actionability.
3. Set thresholds, baselines, alert routing, and suppression rules.
4. Define retrain, rollback, investigation, or no-action playbooks.
5. Return a monitor design and incident response path.

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
