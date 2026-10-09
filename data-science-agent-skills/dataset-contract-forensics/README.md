# Dataset Contract Forensics

![Dataset Contract Forensics Hero Shot](assets/hero-shot.png)

![Dataset Contract Forensics Infographic](assets/reddit-infographic.png)

## Executive Summary

**Dataset Contract Forensics** is a portable, provider-neutral data science agent skill designed to infer practical data contracts, schema expectations, and validation tests from messy real datasets.

> **Core pain solved:** Data breaks downstream because implicit assumptions about schema, meaning, ranges, uniqueness, and freshness are never written down.

> **Proof callout:** Makes hidden assumptions executable.

## Research-Informed Design Standard

This skill follows reproducible data science and portable agent-skill standards:

- **Cookiecutter Data Science**: immutable raw data, clear artifact layout, and repeatable command entrypoints.
- **Kedro**: explicit input/output data contracts and modular workflow boundaries.
- **MLflow**: traceable parameters, metrics, provenance hashes, and governance-ready evaluation records.
- **Anthropic & Open Agent Skills**: concise `SKILL.md` frontmatter, progressive disclosure via `references/`, and deterministic local scripts in `scripts/`.
- **CfRR Reproducible Research**: deterministic verification, explicit uncertainty, and zero hidden state.

## Problem It Solves

Data breaks downstream because implicit assumptions about schema, meaning, ranges, uniqueness, and freshness are never written down. Without a structured gate, teams routinely discover `sample too small` or `IDs not unique when assumed unique` only after engineering effort or executive credibility has already been spent.

## What This Skill Should Do

- Transform a vague request into an explicit Dataset Contract Forensics decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Preserve raw evidence and never silently mutate data, notebooks, model artifacts, or production configs.
- Return a decision artifact that can be handed to a data scientist, ML engineer, governance reviewer, or stakeholder without hidden context.

## Required Inputs

- CSV, Parquet, JSONL, SQL schema, or sample extracts
- downstream use case
- known business rules
- refresh cadence

## Operating Workflow

1. Profile columns, nulls, uniqueness, cardinality, ranges, formats, and candidate keys.
2. Identify semantic expectations that cannot be inferred mechanically and mark them for owner confirmation.
3. Draft tests for schema, freshness, distribution, referential integrity, and accepted values.
4. Map each test to Great Expectations, Pandera, dbt, or plain SQL where appropriate.
5. Return a contract draft with confidence levels and confirmation questions.

## Expected Outputs

- contract draft
- test inventory
- confidence labels
- owner questions
- tool-specific implementation hints

All outputs are delivered inside the eight-section decision contract: `Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, and `Artifacts`.

## Concrete Use Cases

- **Pre-commit readiness gate**: Run `scripts/profile_table.py` on `CSV, Parquet, JSONL, SQL schema, or sample extracts` to produce a `contract draft` before approving engineering scope.
- **Adversarial review**: Challenge a proposed `go` recommendation when `sample too small` or `IDs not unique when assumed unique` is suspected in `downstream use case`.
- **Cross-team handoff**: Generate `test inventory` and `tool-specific implementation hints` so ML engineers, governance reviewers, or downstream agents can act without re-running discovery.
- **Regression audit**: Score completed review checklists with `scripts/checklist_score.py --strict` inside CI to prevent unverified artifacts from shipping.

## Red Flags

- sample too small
- IDs not unique when assumed unique
- silent enum expansion
- date freshness inconsistent
- meaning cannot be inferred from name

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
python scripts/profile_table.py path/to/extract.csv --max-rows 10000
python scripts/quick_validate_skill.py . --strict
python tests/test_skill_contract.py .
```

## Visual Assets

- Hero shot (`1600x900`): [assets/hero-shot.png](assets/hero-shot.png) (`https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/main/data-science-agent-skills/dataset-contract-forensics/assets/hero-shot.png`)
- Reddit infographic (`1080x1350`): [assets/reddit-infographic.png](assets/reddit-infographic.png) (`https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/main/data-science-agent-skills/dataset-contract-forensics/assets/reddit-infographic.png`)
