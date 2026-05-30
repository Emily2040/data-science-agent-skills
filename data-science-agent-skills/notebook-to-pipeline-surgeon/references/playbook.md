# Notebook To Pipeline Surgeon Playbook

## Core Checklist

- [ ] Identify notebook sections: config, IO, transforms, modeling, evaluation, visualization, and side effects.
- [ ] Extract reusable functions and isolate parameters.
- [ ] Define CLI or config file and deterministic outputs.
- [ ] Choose simple scripts first; use Dagster, Kedro, Prefect, or Airflow only when orchestration value is clear.
- [ ] Return a refactor plan with tests and migration steps.

## Expected Deliverables

- pipeline extraction map
- module boundaries
- parameter contract
- test plan
- orchestrator recommendation

## Red Flags

- global mutable state
- manual cell ordering
- plot-only outputs used downstream
- external calls in transform functions
- orchestrator added without need

## Decision Rules

- `go`: critical evidence is available, risks are owned, and the next action is reversible or monitored.
- `fix-first`: the work is valuable but at least one blocker must be remediated before modeling, launch, or stakeholder use.
- `stop`: the request is misframed, unsafe, untestable, or materially misleading with available evidence.
- `proceed-with-risk`: the user accepts named risks and the report includes monitoring or rollback conditions.

## Evidence Discipline

- Tie every recommendation to a file, metric, stakeholder claim, or explicit assumption.
- Separate mechanically observed facts from expert judgment.
- Use uncertainty language when the evidence is partial.
- Record unresolved owner questions rather than filling gaps with confident guesses.
