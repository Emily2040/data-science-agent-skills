# Notebook To Pipeline Surgeon

![Notebook To Pipeline Surgeon Hero Shot](assets/hero-shot.png)

![Notebook To Pipeline Surgeon Infographic](assets/reddit-infographic.png)

## Executive Summary

**Notebook To Pipeline Surgeon** is a portable, provider-neutral data science agent skill designed to convert exploratory notebooks into modular, parameterized scripts or orchestrated pipeline tasks.

> **Core pain solved:** Production workflows inherit notebook state, copy-pasted cells, and manual execution steps.

> **Proof callout:** Converts exploratory work into repeatable production shape.

## Research-Informed Design Standard

This skill follows reproducible data science and portable agent-skill standards:

- **Cookiecutter Data Science**: immutable raw data, clear artifact layout, and repeatable command entrypoints.
- **Kedro**: explicit input/output data contracts and modular workflow boundaries.
- **MLflow**: traceable parameters, metrics, provenance hashes, and governance-ready evaluation records.
- **Anthropic & Open Agent Skills**: concise `SKILL.md` frontmatter, progressive disclosure via `references/`, and deterministic local scripts in `scripts/`.
- **CfRR Reproducible Research**: deterministic verification, explicit uncertainty, and zero hidden state.

## Problem It Solves

Production workflows inherit notebook state, copy-pasted cells, and manual execution steps. Without a structured gate, teams routinely discover `global mutable state` or `manual cell ordering` only after engineering effort or executive credibility has already been spent.

## What This Skill Should Do

- Transform a vague request into an explicit Notebook To Pipeline Surgeon decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Preserve raw evidence and never silently mutate data, notebooks, model artifacts, or production configs.
- Return a decision artifact that can be handed to a data scientist, ML engineer, governance reviewer, or stakeholder without hidden context.

## Required Inputs

- notebook
- target runtime
- data locations
- expected outputs
- orchestration preference if any

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

All outputs are delivered inside the eight-section decision contract: `Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, and `Artifacts`.

## Concrete Use Cases

- **Pre-commit readiness gate**: Run `scripts/notebook_repro_audit.py` on `notebook` to produce a `pipeline extraction map` before approving engineering scope.
- **Adversarial review**: Challenge a proposed `go` recommendation when `global mutable state` or `manual cell ordering` is suspected in `target runtime`.
- **Cross-team handoff**: Generate `module boundaries` and `orchestrator recommendation` so ML engineers, governance reviewers, or downstream agents can act without re-running discovery.
- **Regression audit**: Score completed review checklists with `scripts/checklist_score.py --strict` inside CI to prevent unverified artifacts from shipping.

## Red Flags

- global mutable state
- manual cell ordering
- plot-only outputs used downstream
- external calls in transform functions
- orchestrator added without need

## Agent And Provider Portability

- **Agent Runtimes**: OpenAI Codex, ChatGPT Agents, Anthropic Claude, Claude Code, Google Gemini, GitHub Copilot, Cursor, Windsurf, Goose, OpenCode, OpenHands, Gravity, LangGraph, CrewAI, AutoGen, LlamaIndex, Semantic Kernel, and local LLM agents.
- **Data & ML Providers**: Snowflake, BigQuery, Databricks, Postgres, dbt, Dagster, Airflow, Prefect, MLflow, DVC, Weights & Biases, SageMaker, Vertex AI, Azure ML, Great Expectations, Pandera, Evidently, Kedro, and local CSV/Parquet/JSON files.

See [references/agent-portability.md](references/agent-portability.md) and [references/provider-interop.md](references/provider-interop.md) for host-specific integration instructions.

## Included Files

- `SKILL.md`
- `README.md`
- `MANIFEST.json`
- `AGENTS.md`
- `agents/openai.yaml`
- `scripts/notebook_repro_audit.py`
- `scripts/checklist_score.py`
- `scripts/quick_validate_skill.py`
- `references/multilingual-guide.md`: Native English, Simplified Chinese (简体中文), Japanese (日本語), and Korean (한국어) execution guide.
- `references/playbook.md`
- `references/acceptance-tests.md`
- `references/provider-interop.md`
- `references/agent-portability.md`
- `references/quality-rubric.md`
- `references/benchmark-plan.md`
- `references/research-grounding.md`
- `references/evidence-map.md`
- `references/infographic-spec.md`
- `tests/test_skill_contract.py`
- `tests/fixtures/clean.md`
- `tests/fixtures/messy.md`
- `tests/fixtures/adversarial.md`
- `assets/hero-shot.png`
- `assets/reddit-infographic.png`

## Validation

Run the deterministic smoke and contract suite from inside this skill directory:

```bash
python scripts/notebook_repro_audit.py path/to/notebook.ipynb
python scripts/quick_validate_skill.py . --strict
python tests/test_skill_contract.py .
```

## Visual Assets

- Hero shot (`1600x900`): [assets/hero-shot.png](assets/hero-shot.png) (`https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/main/data-science-agent-skills/notebook-to-pipeline-surgeon/assets/hero-shot.png`)
- Reddit infographic (`1080x1350`): [assets/reddit-infographic.png](assets/reddit-infographic.png) (`https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/main/data-science-agent-skills/notebook-to-pipeline-surgeon/assets/reddit-infographic.png`)
