---
name: notebook-to-pipeline-surgeon
description: Convert exploratory notebooks into modular, parameterized scripts or orchestrated pipeline tasks. Use when Codex needs to handle data science workflows involving refactor notebooks into maintainable pipelines, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Notebook To Pipeline Surgeon

## Mission

Convert exploratory notebooks into modular, parameterized scripts or orchestrated pipeline tasks.

Current pain point: Production workflows inherit notebook state, copy-pasted cells, and manual execution steps.

Why this skill exists: A surgical refactor preserves analytical intent while separating parameters, pure transforms, IO, tests, and orchestration.

## Required Inputs

- notebook
- target runtime
- data locations
- expected outputs
- orchestration preference if any

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Identify notebook sections: config, IO, transforms, modeling, evaluation, visualization, and side effects.
2. Extract reusable functions and isolate parameters.
3. Define CLI or config file and deterministic outputs.
4. Choose simple scripts first; use Dagster, Kedro, Prefect, or Airflow only when orchestration value is clear.
5. Return a refactor plan with tests and migration steps.

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
