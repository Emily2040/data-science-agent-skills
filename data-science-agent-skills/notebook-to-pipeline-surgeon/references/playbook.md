# Playbook

## Decision This Skill Supports

Convert exploratory notebooks into modular, parameterized scripts or orchestrated pipeline tasks.

## Evidence Checklist

- notebook
- target runtime
- data locations
- expected outputs
- orchestration preference if any

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Identify notebook sections: config, IO, transforms, modeling, evaluation, visualization, and side effects.
2. Extract reusable functions and isolate parameters.
3. Define CLI or config file and deterministic outputs.
4. Choose simple scripts first; use Dagster, Kedro, Prefect, or Airflow only when orchestration value is clear.
5. Return a refactor plan with tests and migration steps.

## Decision Ladder

- `go`: evidence is sufficient and red flags are absent or accepted by the owner.
- `fix-first`: a concrete blocker can be remediated before continuing.
- `stop`: the work would be misleading, unsafe, unlawful, or untestable.
- `proceed-with-risk`: the owner accepts named risks and monitoring is specified.
- `needs-owner-review`: the agent cannot decide without a human owner.

## Evidence Table Template

| Finding | Evidence | Confidence | Owner action |
| --- | --- | --- | --- |
| Fill this row | File, query, metric, or observation | high/medium/low | go/fix/stop/review |

## Red Flags

- global mutable state
- manual cell ordering
- plot-only outputs used downstream
- external calls in transform functions
- orchestrator added without need

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
