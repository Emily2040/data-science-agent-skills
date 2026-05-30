---
name: data-science-incident-rca
description: Run root-cause analysis for broken models, metrics, dashboards, pipelines, and data science decisions. Use when Codex needs to handle data science workflows involving diagnose broken models and dashboards, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Data Science Incident RCA

## Mission

Run root-cause analysis for broken models, metrics, dashboards, pipelines, and data science decisions.

Current pain point: Data incidents become blame hunts because evidence, timelines, blast radius, and controls are scattered.

Why this skill exists: A DS incident RCA connects data, code, model, metric, and decision layers into one timeline.


## What This Skill Must Do

- Convert the request into an explicit Data Science Incident RCA decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: incident symptom, time first observed, affected outputs, recent changes.
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

- no timestamped evidence
- only one layer investigated
- impact not quantified
- human process omitted
- countermeasure lacks owner

## Required Inputs

- incident symptom
- time first observed
- affected outputs
- recent changes
- logs or metrics
- owners

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Define symptom, detection path, start time, severity, and affected users or decisions.
2. Build timeline across data sources, pipelines, code, model, dashboard, and human changes.
3. Separate root cause, contributing factors, detection gaps, and impact.
4. Recommend immediate mitigation, durable prevention, monitoring, and ownership updates.
5. Return an RCA memo with evidence and countermeasures.

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
