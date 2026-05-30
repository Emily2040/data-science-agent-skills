---
name: data-question-framing
description: Turn ambiguous business, product, policy, or research asks into decision-ready data science problem statements. Use when Codex needs to handle data science workflows involving turn vague asks into measurable ds problems, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Data Question Framing

## Mission

Turn ambiguous business, product, policy, or research asks into decision-ready data science problem statements.

Current pain point: Teams waste cycles modeling the wrong target, optimizing vanity metrics, or answering questions that no owner can act on.

Why this skill exists: A framing skill closes the gap before analysis starts: outcome, unit, target, metric, constraints, and decision owner are made explicit.


## What This Skill Must Do

- Convert the request into an explicit Data Question Framing decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: raw stakeholder request, available decision or business context, known data sources or constraints, deadline and decision owner.
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

- no decision owner
- target unavailable at decision time
- metric can improve while user outcome worsens
- causal claim hidden inside prediction wording

## Required Inputs

- raw stakeholder request
- available decision or business context
- known data sources or constraints
- deadline and decision owner

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Extract the decision, action, and user or entity affected.
2. Define the analysis unit, target, time horizon, and comparison baseline.
3. Separate prediction, causal, descriptive, and operational questions.
4. Choose success, guardrail, and decision metrics before any modeling plan.
5. Return a decision canvas with assumptions and unresolved questions.

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
