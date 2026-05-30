---
name: cost-aware-compute-planner
description: Plan compute use so data science experiments, model training, and inference stay within budget and latency constraints. Use when Codex needs to handle data science workflows involving plan gpu, cloud, and sampling costs, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Cost Aware Compute Planner

## Mission

Plan compute use so data science experiments, model training, and inference stay within budget and latency constraints.

Current pain point: Teams burn budget on full-data experiments, oversized GPUs, idle notebooks, and unbounded inference before learning if the work matters.

Why this skill exists: Compute planning forces sample-first learning, stop rules, and explicit cost-quality tradeoffs.


## What This Skill Must Do

- Convert the request into an explicit Cost Aware Compute Planner decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: task type, data size, model candidates, cloud or local options.
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

- full-data first run
- no budget owner
- idle GPU notebooks
- inference cost ignored
- training cheaper than monitoring is assumed

## Required Inputs

- task type
- data size
- model candidates
- cloud or local options
- budget
- deadline
- latency needs

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Estimate minimum useful experiment scale and define sample-first gates.
2. Compare local CPU, local GPU, cloud CPU, cloud GPU, batch, and spot options.
3. Plan caching, early stopping, checkpointing, and parallelism.
4. Set budget guardrails and cost per experiment or inference unit.
5. Return a compute plan with stop rules and escalation thresholds.

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
