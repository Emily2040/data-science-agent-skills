---
name: experiment-provenance-ledger
description: Preserve experiment provenance across code, data, environment, parameters, metrics, artifacts, and human decisions. Use when Codex needs to handle data science workflows involving capture code, data, env, and decision history, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Experiment Provenance Ledger

## Mission

Preserve experiment provenance across code, data, environment, parameters, metrics, artifacts, and human decisions.

Current pain point: Teams cannot explain which model, data, code, or parameters produced a result after the fact.

Why this skill exists: A provenance ledger creates an immutable audit trail independent of any single tracking tool.


## What This Skill Must Do

- Convert the request into an explicit Experiment Provenance Ledger decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: repo path, dataset identifiers, environment files, training command.
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

- unversioned dataset
- dirty code used for final metric
- missing seed
- manual artifact rename
- model chosen without logged rationale

## Required Inputs

- repo path
- dataset identifiers
- environment files
- training command
- metrics
- artifact paths
- decision notes

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Capture code version, dirty state, environment, data references, parameters, seeds, and runtime.
2. Record metrics and artifacts with owner, purpose, and retention expectation.
3. Link human decisions, exclusions, and model-selection rationale.
4. Map entries to MLflow, DVC, W&B, or plain JSON depending on the stack.
5. Return a ledger and missing-provenance risk list.

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
