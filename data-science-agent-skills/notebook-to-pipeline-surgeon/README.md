# Notebook To Pipeline Surgeon

![Notebook To Pipeline Surgeon hero shot](assets/hero-shot.png)

![Notebook To Pipeline Surgeon Reddit infographic](assets/reddit-infographic.png)

## Summary

`notebook-to-pipeline-surgeon` is an independent Agent/Codex skill for: Convert exploratory notebooks into modular, parameterized scripts or orchestrated pipeline tasks.

It exists because Production workflows inherit notebook state, copy-pasted cells, and manual execution steps. A surgical refactor preserves analytical intent while separating parameters, pure transforms, IO, tests, and orchestration.

The skill is not a generic data-analysis helper. It is a judgment workflow: it tells the agent what evidence to gather, what checks to run, what assumptions to expose, and what decision-ready artifact to return.

## Problem It Solves

The current data science pain is not that there are no notebooks, dashboards, profilers, or MLOps tools. The pain is that teams still lose trust at the handoff points: unclear questions, weak data readiness, hidden leakage, missing provenance, fragile notebooks, vague ownership, and model work that cannot be defended.

This skill targets one of those gaps directly:

- Primary pain: Production workflows inherit notebook state, copy-pasted cells, and manual execution steps.
- Why existing tools are not enough: tools can inspect fragments, but they rarely force the agent to connect evidence, owner decisions, risk, and next action in one repeatable workflow.
- What this skill adds: A surgical refactor preserves analytical intent while separating parameters, pure transforms, IO, tests, and orchestration.

## What This Skill Should Do

- Convert the request into an explicit Notebook To Pipeline Surgeon decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: notebook, target runtime, data locations, expected outputs.
- Separate mechanical checks from judgment calls so another reviewer can audit the result.
- Return a decision-ready artifact with risks, owner questions, and the smallest next action.
- Refuse to hide uncertainty. Mark unknown, not applicable, and needs human owner review as separate states.

## Required Inputs

- notebook
- target runtime
- data locations
- expected outputs
- orchestration preference if any

If an input is missing, the agent should inspect local files, schemas, notebooks, configs, or reports first. It should ask the user only for information that cannot be recovered and would materially change the decision.

## Operating Workflow

1. Identify notebook sections: config, IO, transforms, modeling, evaluation, visualization, and side effects.
2. Extract reusable functions and isolate parameters.
3. Define CLI or config file and deterministic outputs.
4. Choose simple scripts first; use Dagster, Kedro, Prefect, or Airflow only when orchestration value is clear.
5. Return a refactor plan with tests and migration steps.

## Expected Outputs

- pipeline extraction map
- module boundaries
- parameter contract
- test plan
- orchestrator recommendation

Every final answer produced with this skill should use this output contract:

- `Problem`: the decision, artifact, model, data source, or workflow being handled.
- `Inputs`: files, data, stakeholder context, assumptions, and missing context used.
- `Checks performed`: concrete inspections, scripts, and reasoning checks.
- `Findings`: prioritized observations with evidence.
- `Decision`: go, fix-first, stop, proceed-with-risk, or needs-owner-review.
- `Risks`: unresolved blockers, caveats, and owner decisions.
- `Next actions`: the smallest useful follow-up steps.
- `Artifacts`: generated files, specs, scripts, reports, or links.

## Concrete Use Cases

- Before a project starts: decide whether to proceed with notebook to pipeline surgeon work or fix prerequisites first.
- During review: challenge the work when a red flag appears, such as global mutable state.
- Before handoff: package the findings so another agent, data scientist, engineer, or stakeholder can act without rereading the whole investigation.

## Red Flags

- global mutable state
- manual cell ordering
- plot-only outputs used downstream
- external calls in transform functions
- orchestrator added without need

When one of these appears, the skill should slow down, preserve evidence, and name the risk in the final decision. A red flag does not always mean stop, but it must be visible.

## How To Use With OpenAI Agents

Copy this whole folder into the configured skills directory. Invoke it with `$notebook-to-pipeline-surgeon` or let the frontmatter description trigger it. Keep `references/`, `scripts/`, and `assets/` beside `SKILL.md`.

For Codex, use it when the task involves local evidence, file inspection, validation, implementation planning, or PR-ready artifacts. The helper scripts should run only against local files or explicit user-provided data.

## How To Use With Claude, Cursor, Windsurf, Copilot, LangGraph, CrewAI, Or AutoGen

Use `SKILL.md` as the role instruction for a specialist agent. Attach `references/playbook.md` for the checklist, `references/acceptance-tests.md` for forward tests, and `references/provider-interop.md` for provider-specific adaptation.

For multi-agent systems, route this skill as a specialist reviewer. It should receive evidence from collector agents, run local scripts where available, then return a decision artifact rather than unstructured advice.

## Data Providers And Platforms

Use exported metadata, schemas, samples, logs, lineage files, model cards, metric reports, or experiment records from Snowflake, BigQuery, Databricks, Postgres, dbt, Dagster, MLflow, DVC, W&B, SageMaker, Vertex AI, Azure ML, or local files.

Do not upload private data to external providers unless the user explicitly approves that environment. Provider output is evidence, not authority.

## Included Files

- `SKILL.md`: trigger metadata and core execution workflow.
- `README.md`: this independent GitHub skill page.
- `agents/openai.yaml`: OpenAI-facing metadata and invocation defaults.
- `.gitignore`: local noise filter for this skill.
- `references/playbook.md`: skill-specific checklist, decisions, red flags, and evidence discipline.
- `references/acceptance-tests.md`: clean, messy, and adversarial forward tests.
- `references/evidence-map.md`: public evidence and non-duplication rationale.
- `references/infographic-spec.md`: social visual brief.
- `references/provider-interop.md`: provider and agent usage guide.
- `scripts/`: deterministic local helper scripts where this skill benefits from checks.
- `assets/hero-shot.png`: 1600x900 hero image.
- `assets/reddit-infographic.png`: 1080x1350 Reddit-ready infographic.

## Validation

Run `python scripts/quick_validate_skill.py .` inside this folder. For script-backed skills, run the relevant helper script on a tiny local fixture and one messy example.

Before merging or installing the skill, verify:

- The README renders both images at the top.
- `SKILL.md` has the correct trigger name and output contract.
- The helper scripts return clear errors for missing or invalid inputs.
- The skill does not silently mutate raw data.
- The final response names assumptions and next actions.

## GitHub PR Visual Links

These links are useful when reviewing the independent PR before merge:

- Hero shot: https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/add-data-science-skill-notebook-to-pipeline-surgeon/data-science-agent-skills/notebook-to-pipeline-surgeon/assets/hero-shot.png
- Reddit infographic: https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/add-data-science-skill-notebook-to-pipeline-surgeon/data-science-agent-skills/notebook-to-pipeline-surgeon/assets/reddit-infographic.png
