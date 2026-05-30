---
name: data-science-incident-rca
description: Run root-cause analysis for broken models, metrics, dashboards, pipelines, and data science decisions. Use when an agent needs a judgment-heavy data science workflow for diagnose broken models and dashboards, including evidence review, local artifact inspection, risk classification, stakeholder-ready decisions, reproducibility, governance, or agent-to-agent handoff. Trigger for Codex, Claude, Gemini, Copilot, Cursor, Windsurf, Gravity, LangGraph, CrewAI, AutoGen, or local agents when this exact workflow is needed.
---

# Data Science Incident RCA

## Mission

Run root-cause analysis for broken models, metrics, dashboards, pipelines, and data science decisions.

Current pain point: Data incidents become blame hunts because evidence, timelines, blast radius, and controls are scattered.

Why this skill exists: A DS incident RCA connects data, code, model, metric, and decision layers into one timeline.

## Operating Rules

- Start by restating the decision this skill is supporting.
- Inspect local artifacts first before asking for context.
- Treat scripts as evidence collectors, not as substitutes for judgment.
- Preserve raw data, notebooks, configs, and model artifacts unless the user explicitly asks for mutation.
- Mark missing context as `unknown`, `not provided`, or `owner decision`; do not invent it.
- Classify each blocker as `stop`, `fix-first`, `monitor`, `accepted risk`, or `owner decision`.
- Use the output contract exactly unless the user asks for a different format.
- Keep final recommendations auditable: every important claim needs evidence, assumption, or caveat.

## What This Skill Must Do

- Transform a vague request into an explicit Data Science Incident RCA decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Preserve raw evidence and never silently mutate data, notebooks, model artifacts, or production configs.
- Return a decision artifact that can be handed to a data scientist, ML engineer, governance reviewer, or stakeholder without hidden context.

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

## Red Flags

- no timestamped evidence
- only one layer investigated
- impact not quantified
- human process omitted
- countermeasure lacks owner

When a red flag appears, slow down and surface it in `Risks`. A red flag does not always mean stop, but it must change the recommendation or the confidence level.

## Resources

- Read `references/playbook.md` for the skill-specific checklist, scoring rubric, and failure modes.
- Read `references/acceptance-tests.md` before forward-testing clean, messy, and adversarial requests.
- Read `references/agent-portability.md` when adapting this skill to Claude, Gemini, Copilot, Cursor, Windsurf, Gravity, LangGraph, CrewAI, AutoGen, or local agents.
- Read `references/quality-rubric.md` when reviewing whether the output meets senior data-science standards.
- Use `scripts/quick_validate_skill.py . --strict` before publishing or installing the skill.

Use only the specific reference file needed for the task; keep context small.

## Output Contract

Return these sections unless the user requests another format:

- `Problem`: the decision, artifact, model, data source, or workflow being handled.
- `Inputs`: files, data, stakeholder context, assumptions, and missing context used.
- `Checks performed`: concrete inspections, scripts, and reasoning checks.
- `Findings`: prioritized observations with evidence.
- `Decision`: go, fix-first, stop, proceed-with-risk, or needs-owner-review.
- `Risks`: unresolved blockers, caveats, and owner decisions.
- `Next actions`: smallest useful follow-up steps.
- `Artifacts`: generated files, specs, reports, scripts, or links.

## Final Checks

- Did the response answer the actual decision, not just analyze data?
- Did it preserve evidence and avoid silent mutation?
- Did it name unknowns and owner decisions?
- Did it include at least one concrete next action?
- Did it avoid overclaiming causality, readiness, compliance, or production safety?
