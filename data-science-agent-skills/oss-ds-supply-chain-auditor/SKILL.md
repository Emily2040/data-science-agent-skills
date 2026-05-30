---
name: oss-ds-supply-chain-auditor
description: Audit open-source packages, notebooks, model weights, datasets, licenses, and provenance used in data science work. Use when Codex needs to handle data science workflows involving audit ds dependencies, models, data, and licenses, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# OSS Data Science Supply Chain Auditor

## Mission

Audit open-source packages, notebooks, model weights, datasets, licenses, and provenance used in data science work.

Current pain point: Data science supply chains include packages, model files, datasets, and notebooks that standard app audits often miss.

Why this skill exists: A DS-specific audit catches model/data provenance and notebook execution risks alongside dependency risk.


## What This Skill Must Do

- Convert the request into an explicit OSS Data Science Supply Chain Auditor decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: repo path, environment files, notebooks, model artifact paths.
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

- pip install from unpinned URL
- unknown model weights
- dataset license absent
- notebook output leaks secrets
- native binary dependency unreviewed

## Required Inputs

- repo path
- environment files
- notebooks
- model artifact paths
- dataset sources
- license expectations

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Inventory Python, R, system, notebook, model, and dataset dependencies.
2. Flag unknown sources, unsafe install patterns, large binary artifacts, and license uncertainty.
3. Review notebooks for shell execution, remote downloads, credential exposure, and hidden outputs.
4. Create a DS SBOM-style summary with risk levels and remediation priorities.
5. Return a supply-chain risk report and minimum cleanup plan.

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
