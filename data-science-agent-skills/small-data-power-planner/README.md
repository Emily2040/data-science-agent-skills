# Small Data Power Planner

![Small Data Power Planner Hero Shot](assets/hero-shot.png)

![Small Data Power Planner Infographic](assets/reddit-infographic.png)

## Executive Summary

**Small Data Power Planner** is a portable, provider-neutral data science agent skill designed to help teams decide what can be learned responsibly from small, imbalanced, expensive, or scarce datasets.

> **Core pain solved:** Small datasets are forced through high-capacity methods, producing unstable conclusions and overconfident narratives.

> **Proof callout:** Prevents small data from sounding bigger than it is.

## Research-Informed Design Standard

This skill follows reproducible data science and portable agent-skill standards:

- **Cookiecutter Data Science**: immutable raw data, clear artifact layout, and repeatable command entrypoints.
- **Kedro**: explicit input/output data contracts and modular workflow boundaries.
- **MLflow**: traceable parameters, metrics, provenance hashes, and governance-ready evaluation records.
- **Anthropic & Open Agent Skills**: concise `SKILL.md` frontmatter, progressive disclosure via `references/`, and deterministic local scripts in `scripts/`.
- **CfRR Reproducible Research**: deterministic verification, explicit uncertainty, and zero hidden state.

## Problem It Solves

Small datasets are forced through high-capacity methods, producing unstable conclusions and overconfident narratives. Without a structured gate, teams routinely discover `more features than observations` or `rare outcome with random split` only after engineering effort or executive credibility has already been spent.

## What This Skill Should Do

- Transform a vague request into an explicit Small Data Power Planner decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Preserve raw evidence and never silently mutate data, notebooks, model artifacts, or production configs.
- Return a decision artifact that can be handed to a data scientist, ML engineer, governance reviewer, or stakeholder without hidden context.

## Required Inputs

- sample size
- outcome rate
- candidate features
- effect size of interest
- cost of errors
- collection options

## Operating Workflow

1. Identify the decision and minimum useful effect size.
2. Estimate signal limits, imbalance, uncertainty, and variance risks.
3. Recommend descriptive, Bayesian, resampling, regularized, or data-collection paths.
4. Define validation limits and language for uncertainty.
5. Return a do-model, simplify, or collect-more recommendation.

## Expected Outputs

- power and uncertainty note
- baseline plan
- validation limits
- collection recommendation
- safe communication text

All outputs are delivered inside the eight-section decision contract: `Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, and `Artifacts`.

## Concrete Use Cases

- **Pre-commit readiness gate**: Run `scripts/power_sample_size.py` on `sample size` to produce a `power and uncertainty note` before approving engineering scope.
- **Adversarial review**: Challenge a proposed `go` recommendation when `more features than observations` or `rare outcome with random split` is suspected in `outcome rate`.
- **Cross-team handoff**: Generate `baseline plan` and `safe communication text` so ML engineers, governance reviewers, or downstream agents can act without re-running discovery.
- **Regression audit**: Score completed review checklists with `scripts/checklist_score.py --strict` inside CI to prevent unverified artifacts from shipping.

## Red Flags

- more features than observations
- rare outcome with random split
- single holdout set only
- unreported uncertainty
- high-stakes decision from tiny sample

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
- `scripts/power_sample_size.py`
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
python scripts/power_sample_size.py --n-per-arm 120 --baseline-std 1.0 --features 6 --events 90
python scripts/quick_validate_skill.py . --strict
python tests/test_skill_contract.py .
```

## Visual Assets

- Hero shot (`1600x900`): [assets/hero-shot.png](assets/hero-shot.png) (`https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/main/data-science-agent-skills/small-data-power-planner/assets/hero-shot.png`)
- Reddit infographic (`1080x1350`): [assets/reddit-infographic.png](assets/reddit-infographic.png) (`https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/main/data-science-agent-skills/small-data-power-planner/assets/reddit-infographic.png`)
