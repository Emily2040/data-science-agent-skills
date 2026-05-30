---
name: notebook-repro-packager
description: Package notebooks so another machine or teammate can reproduce their results with known data, environment, seeds, and order. Use when Codex needs to handle data science workflows involving make notebooks runnable elsewhere, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Notebook Repro Packager

## Mission

Package notebooks so another machine or teammate can reproduce their results with known data, environment, seeds, and order.

Current pain point: Notebooks break because execution order, hidden state, local paths, package versions, and data provenance are not captured.

Why this skill exists: Reproducibility requires a small set of mechanical checks plus a clear run contract.


## What This Skill Must Do

- Convert the request into an explicit Notebook Repro Packager decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: notebook files, data dependencies, environment files, expected outputs.
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

- out-of-order execution
- local absolute paths
- unseeded randomness
- implicit data downloads
- manual cell edits required

## Required Inputs

- notebook files
- data dependencies
- environment files
- expected outputs
- runtime constraints

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Audit execution order, hidden state, hard-coded paths, missing seeds, and external dependencies.
2. Capture environment, data manifest, run command, and expected output checks.
3. Separate exploratory cells from required run path.
4. Add smoke-test guidance and failure messages.
5. Return a reproducibility package checklist and patch plan.

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
