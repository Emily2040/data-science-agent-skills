# Missingness Mechanism Investigator

![Missingness Mechanism Investigator Hero Shot](assets/hero-shot.png)

![Missingness Mechanism Investigator Infographic](assets/reddit-infographic.png)

## Executive Summary

**Missingness Mechanism Investigator** is a portable, provider-neutral data science agent skill designed to diagnose missing-data mechanisms and design imputation, exclusion, or sensitivity plans.

> **Core pain solved:** Missing values are filled or dropped mechanically, creating bias and false confidence.

> **Proof callout:** Turns blanks into explicit assumptions.

## Research-Informed Design Standard

This skill follows reproducible data science and portable agent-skill standards:

- **Cookiecutter Data Science**: immutable raw data, clear artifact layout, and repeatable command entrypoints.
- **Kedro**: explicit input/output data contracts and modular workflow boundaries.
- **MLflow**: traceable parameters, metrics, provenance hashes, and governance-ready evaluation records.
- **Anthropic & Open Agent Skills**: concise `SKILL.md` frontmatter, progressive disclosure via `references/`, and deterministic local scripts in `scripts/`.
- **CfRR Reproducible Research**: deterministic verification, explicit uncertainty, and zero hidden state.

## Problem It Solves

Missing values are filled or dropped mechanically, creating bias and false confidence. Without a structured gate, teams routinely discover `target-dependent missingness` or `structural missing treated as random` only after engineering effort or executive credibility has already been spent.

## What This Skill Should Do

- Transform a vague request into an explicit Missingness Mechanism Investigator decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Preserve raw evidence and never silently mutate data, notebooks, model artifacts, or production configs.
- Return a decision artifact that can be handed to a data scientist, ML engineer, governance reviewer, or stakeholder without hidden context.

## Required Inputs

- dataset
- analysis goal
- column meanings
- collection process
- known reasons for missingness

## Operating Workflow

1. Profile missingness by column, row, group, time, and target relationship.
2. Classify likely mechanisms as MCAR, MAR, MNAR, structural missing, or unknown.
3. Identify whether missingness itself should be a feature, exclusion reason, or bias warning.
4. Recommend complete-case, imputation, indicator, model-based, or sensitivity strategy.
5. Return a missingness report with assumptions and impact on claims.

## Expected Outputs

- missingness heat map summary
- mechanism labels
- imputation plan
- sensitivity plan
- claim limitations

All outputs are delivered inside the eight-section decision contract: `Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, and `Artifacts`.

## Concrete Use Cases

- **Pre-commit readiness gate**: Run `scripts/profile_table.py` on `dataset` to produce a `missingness heat map summary` before approving engineering scope.
- **Adversarial review**: Challenge a proposed `go` recommendation when `target-dependent missingness` or `structural missing treated as random` is suspected in `analysis goal`.
- **Cross-team handoff**: Generate `mechanism labels` and `claim limitations` so ML engineers, governance reviewers, or downstream agents can act without re-running discovery.
- **Regression audit**: Score completed review checklists with `scripts/checklist_score.py --strict` inside CI to prevent unverified artifacts from shipping.

## Red Flags

- target-dependent missingness
- structural missing treated as random
- imputed identifiers
- dropped rows change population
- no collection-process explanation

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
- `scripts/profile_table.py`
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
python scripts/profile_table.py path/to/dataset.csv --max-rows 10000
python scripts/quick_validate_skill.py . --strict
python tests/test_skill_contract.py .
```

## Visual Assets

- Hero shot (`1600x900`): [assets/hero-shot.png](assets/hero-shot.png) (`https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/main/data-science-agent-skills/missingness-mechanism-investigator/assets/hero-shot.png`)
- Reddit infographic (`1080x1350`): [assets/reddit-infographic.png](assets/reddit-infographic.png) (`https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/main/data-science-agent-skills/missingness-mechanism-investigator/assets/reddit-infographic.png`)
