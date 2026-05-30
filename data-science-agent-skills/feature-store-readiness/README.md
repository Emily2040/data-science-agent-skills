# Feature Store Readiness

![Feature Store Readiness hero shot](assets/hero-shot.png)

![Feature Store Readiness Reddit infographic](assets/reddit-infographic.png)

## Executive Summary

`feature-store-readiness` is a portable, independent data-science agent skill for: Decide whether a feature store is needed and design features to avoid training-serving skew, staleness, and reuse confusion.

It solves a real operating problem: Teams either overbuild feature stores too early or underbuild shared feature governance until skew breaks models. Feature-store readiness should be based on reuse, freshness, online serving, lineage, ownership, and skew risk.

The design target is the level expected by senior data scientists, staff ML engineers, and governance reviewers: explicit evidence, reproducible checks, decision-grade output, clear owner questions, and enough structure for another agent to run the same workflow without hidden context.

## Research-Informed Design Standard

This skill was redesigned against patterns from high-quality public data-science and agent-skill repositories:

- Cookiecutter Data Science: predictable folders, immutable raw evidence, project docs, tests, and dependency discipline.
- Kedro: modular, reproducible, maintainable pipeline thinking.
- MLflow: lifecycle tracking, evaluations, registry/deployment awareness, and broad integration posture.
- Anthropic-style skills: portable folder with `SKILL.md`, scripts, references, and resources.
- Reproducible-research guidance: documentation, dependency management, version control, testing, collaboration, and transparency.

## Problem It Solves

Decide whether a feature store is needed and design features to avoid training-serving skew, staleness, and reuse confusion.

- Primary pain: Teams either overbuild feature stores too early or underbuild shared feature governance until skew breaks models.
- Why generic tools are not enough: generic notebooks, profilers, dashboards, and MLOps tools inspect pieces of the problem; this skill forces the agent to connect evidence, assumptions, owner decisions, risk, and next action.
- What the skill adds: Feature-store readiness should be based on reuse, freshness, online serving, lineage, ownership, and skew risk.

## What This Skill Should Do

- Transform a vague request into an explicit Feature Store Readiness decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Preserve raw evidence and never silently mutate data, notebooks, model artifacts, or production configs.
- Return a decision artifact that can be handed to a data scientist, ML engineer, governance reviewer, or stakeholder without hidden context.

## Required Inputs

- feature list
- training data flow
- serving flow
- latency needs
- reuse demand
- ownership model

If an input is missing, the agent should inspect local files, schemas, notebooks, SQL, configs, reports, tickets, model artifacts, or metadata first. It should ask the user only when missing context would materially change the decision.

## Operating Workflow

1. Assess whether features need online serving, reuse, point-in-time correctness, or shared governance.
2. Check training-serving skew, freshness, TTL, backfill, and ownership risks.
3. Recommend no store, lightweight registry, batch feature table, or full feature store.
4. Define feature contracts and lineage requirements.
5. Return a readiness decision and migration plan.

## Expected Outputs

- feature-store decision
- skew risk table
- feature contract outline
- TTL and freshness plan
- migration steps

Every final answer should include:

- `Problem`
- `Inputs`
- `Checks performed`
- `Findings`
- `Decision`
- `Risks`
- `Next actions`
- `Artifacts`

## Concrete Use Cases

- Project intake: decide whether to proceed, fix prerequisites, or stop before time is wasted.
- Review gate: challenge a result when evidence is weak, assumptions are hidden, or a red flag appears.
- Handoff: create an artifact an engineer, analyst, governance reviewer, or another agent can continue from.
- Incident prevention: catch the workflow failure before it becomes a bad model, broken dashboard, or misleading executive claim.

## Red Flags

- same feature computed differently online
- freshness unknown
- no point-in-time join
- feature owner unclear
- feature store proposed without reuse

When one appears, the agent must surface it, classify its severity, and tie it to a next action or owner decision.

## Agent And Provider Portability

This skill is designed for OpenAI Codex, ChatGPT Agents, Anthropic Claude, Claude Code, Google Gemini, GitHub Copilot, Cursor, Windsurf, Goose, OpenCode, OpenHands, Gravity, LangGraph, CrewAI, AutoGen, LlamaIndex, Semantic Kernel, and local LLM agents.

Use `SKILL.md` as the primary instruction. Use `references/agent-portability.md` for provider-specific adaptation and `MANIFEST.json` for machine-readable package expectations.

## Data Platforms

Use exported metadata, schemas, samples, logs, lineage files, model cards, metric reports, experiment records, or incident notes from Snowflake, BigQuery, Databricks, Postgres, dbt, Dagster, MLflow, DVC, W&B, SageMaker, Vertex AI, Azure ML, local files, or equivalent systems.

Provider output is evidence, not authority. Do not upload private data to external services unless the user explicitly approves that environment.

## Included Files

- `SKILL.md`: trigger metadata and core execution workflow.
- `README.md`: this independent GitHub skill page.
- `MANIFEST.json`: machine-readable contract for portability checks.
- `AGENTS.md`: local agent instructions for editing or validating this skill folder.
- `agents/openai.yaml`: OpenAI-facing metadata and invocation defaults.
- `references/playbook.md`: operational checklist and failure modes.
- `references/acceptance-tests.md`: clean, messy, and adversarial forward tests.
- `references/provider-interop.md`: provider and data-platform guidance.
- `references/agent-portability.md`: Codex, Claude, Gemini, Copilot, Cursor, Windsurf, Gravity, and multi-agent adaptation.
- `references/quality-rubric.md`: senior-review scoring rubric.
- `references/benchmark-plan.md`: expanded test plan.
- `references/research-grounding.md`: source-informed design rationale.
- `tests/test_skill_contract.py`: portable stdlib contract tests.
- `tests/fixtures/`: clean, messy, and adversarial prompt fixtures.
- `scripts/`: deterministic helper scripts where useful.
- `assets/hero-shot.png`: 1600x900 hero image.
- `assets/reddit-infographic.png`: 1080x1350 Reddit-ready infographic.

## Validation

Run these from inside the skill folder:

```bash
python scripts/quick_validate_skill.py . --strict
python tests/test_skill_contract.py .
```

Then run at least one clean, messy, and adversarial forward test from `tests/fixtures/`.

## GitHub PR Visual Links

- Hero shot: https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/add-data-science-skill-feature-store-readiness/data-science-agent-skills/feature-store-readiness/assets/hero-shot.png
- Reddit infographic: https://raw.githubusercontent.com/Emily2040/data-science-agent-skills/add-data-science-skill-feature-store-readiness/data-science-agent-skills/feature-store-readiness/assets/reddit-infographic.png
