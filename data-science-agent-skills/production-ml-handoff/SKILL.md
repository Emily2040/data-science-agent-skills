---
name: production-ml-handoff
description: Convert data science prototypes into engineering-ready ML handoffs with contracts, artifacts, SLOs, monitoring, and ownership. Use when an agent needs a judgment-heavy data science workflow for turn prototypes into engineering handoffs, including evidence review, local artifact inspection, risk classification, stakeholder-ready decisions, reproducibility, governance, or agent-to-agent handoff. Trigger for Codex, Claude, Gemini, Copilot, Cursor, Windsurf, Gravity, LangGraph, CrewAI, AutoGen, or local agents when this exact workflow is needed.
---

# Production ML Handoff

## Mission

Convert data science prototypes into engineering-ready ML handoffs with contracts, artifacts, SLOs, monitoring, and ownership.

Current pain point: Engineering teams receive notebooks and model files without enough interface, operational, or rollback detail.

Why this skill exists: A handoff package prevents prototype ambiguity from becoming production fragility.

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

- Transform a vague request into an explicit Production ML Handoff decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Preserve raw evidence and never silently mutate data, notebooks, model artifacts, or production configs.
- Return a decision artifact that can be handed to a data scientist, ML engineer, governance reviewer, or stakeholder without hidden context.

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

## Red Flags

- notebook is only artifact
- feature definitions ambiguous
- no rollback plan
- latency unknown
- owner unclear after launch

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
