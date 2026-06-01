---
name: stakeholder-insight-storyteller
description: Convert analysis into stakeholder-ready insight narratives that state decisions, evidence, uncertainty, and recommended action without overclaiming. Use when an agent needs a judgment-heavy data science workflow for convert analysis into decision-grade narrative, including evidence review, local artifact inspection, risk classification, stakeholder-ready decisions, reproducibility, governance, or agent-to-agent handoff. Trigger for Codex, Claude, Gemini, Copilot, Cursor, Windsurf, Gravity, LangGraph, CrewAI, AutoGen, or local agents when this exact workflow is needed.
---

# Stakeholder Insight Storyteller

## Mission

Convert analysis into stakeholder-ready insight narratives that state decisions, evidence, uncertainty, and recommended action without overclaiming.

Current pain point: Good analysis fails when stakeholders receive charts without a decision, caveats without priority, or claims beyond evidence.

Why this skill exists: Insight storytelling is not decoration; it is the bridge from evidence to responsible action.

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

- Transform a vague request into an explicit Stakeholder Insight Storyteller decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Preserve raw evidence and never silently mutate data, notebooks, model artifacts, or production configs.
- Return a decision artifact that can be handed to a data scientist, ML engineer, governance reviewer, or stakeholder without hidden context.

## Required Inputs

- analysis results
- stakeholder audience
- decision needed
- uncertainties
- charts or tables
- recommended action

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Identify the single decision or belief update the audience needs.
2. Separate finding, implication, action, confidence, and caveat.
3. Choose chart and narrative order based on stakeholder task, not analyst chronology.
4. Remove unsupported causal, universal, or precision claims.
5. Return an executive memo or slide narrative with caveats and next actions.

## Red Flags

- chart has no action
- claim exceeds design
- too many caveats with no priority
- audience not named
- uncertainty hidden

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
