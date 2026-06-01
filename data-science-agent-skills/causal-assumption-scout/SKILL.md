---
name: causal-assumption-scout
description: Clarify when a data science request needs causal reasoning, what assumptions are required, and what evidence is missing. Use when an agent needs a judgment-heavy data science workflow for stop predictive work from pretending causality, including evidence review, local artifact inspection, risk classification, stakeholder-ready decisions, reproducibility, governance, or agent-to-agent handoff. Trigger for Codex, Claude, Gemini, Copilot, Cursor, Windsurf, Gravity, LangGraph, CrewAI, AutoGen, or local agents when this exact workflow is needed.
---

# Causal Assumption Scout

## Mission

Clarify when a data science request needs causal reasoning, what assumptions are required, and what evidence is missing.

Current pain point: Teams overclaim causal impact from observational models, dashboards, or correlations.

Why this skill exists: Causal claims need explicit estimand, intervention, confounders, assumptions, and sensitivity checks.

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

- Transform a vague request into an explicit Causal Assumption Scout decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Preserve raw evidence and never silently mutate data, notebooks, model artifacts, or production configs.
- Return a decision artifact that can be handed to a data scientist, ML engineer, governance reviewer, or stakeholder without hidden context.

## Required Inputs

- proposed claim
- treatment or intervention
- outcome
- population
- available covariates
- study design

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Rewrite the claim as prediction, association, or causal effect.
2. Define treatment, outcome, population, time window, and estimand.
3. Draft a DAG-level assumption map and confounder inventory.
4. Recommend experiment, quasi-experiment, matching, weighting, regression, or do-not-claim-causality.
5. Return language that is safe for stakeholders and a sensitivity plan.

## Red Flags

- no intervention
- post-treatment controls
- selection bias
- unmeasured confounders
- effect framed after seeing results

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
