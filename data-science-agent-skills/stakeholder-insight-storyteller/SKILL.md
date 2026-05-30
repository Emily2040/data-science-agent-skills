---
name: stakeholder-insight-storyteller
description: Convert analysis into stakeholder-ready insight narratives that state decisions, evidence, uncertainty, and recommended action without overclaiming. Use when Codex needs to handle data science workflows involving convert analysis into decision-grade narrative, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Stakeholder Insight Storyteller

## Mission

Convert analysis into stakeholder-ready insight narratives that state decisions, evidence, uncertainty, and recommended action without overclaiming.

Current pain point: Good analysis fails when stakeholders receive charts without a decision, caveats without priority, or claims beyond evidence.

Why this skill exists: Insight storytelling is not decoration; it is the bridge from evidence to responsible action.


## What This Skill Must Do

- Convert the request into an explicit Stakeholder Insight Storyteller decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: analysis results, stakeholder audience, decision needed, uncertainties.
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

- chart has no action
- claim exceeds design
- too many caveats with no priority
- audience not named
- uncertainty hidden

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
