---
name: data-question-framing
description: Turn ambiguous business, product, policy, or research asks into decision-ready data science problem statements. Use when Codex needs to handle data science workflows involving turn vague asks into measurable ds problems, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Data Question Framing

## Mission

Turn ambiguous business, product, policy, or research asks into decision-ready data science problem statements.

Current pain point: Teams waste cycles modeling the wrong target, optimizing vanity metrics, or answering questions that no owner can act on.

Why this skill exists: A framing skill closes the gap before analysis starts: outcome, unit, target, metric, constraints, and decision owner are made explicit.

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
