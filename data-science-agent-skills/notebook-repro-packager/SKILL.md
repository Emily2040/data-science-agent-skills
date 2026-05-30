---
name: notebook-repro-packager
description: Package notebooks so another machine or teammate can reproduce their results with known data, environment, seeds, and order. Use when Codex needs to handle data science workflows involving make notebooks runnable elsewhere, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Notebook Repro Packager

## Mission

Package notebooks so another machine or teammate can reproduce their results with known data, environment, seeds, and order.

Current pain point: Notebooks break because execution order, hidden state, local paths, package versions, and data provenance are not captured.

Why this skill exists: Reproducibility requires a small set of mechanical checks plus a clear run contract.

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
