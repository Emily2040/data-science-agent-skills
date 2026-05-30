# Provider And Agent Interop

Use this skill as a portable workflow pack. The core contract is `SKILL.md`; references, scripts, and visual assets are optional support files.

## OpenAI Codex Or ChatGPT Agents

Copy the whole skill folder into the configured skills directory, then invoke it with `$experiment-provenance-ledger` or let the description trigger automatically. Keep `references/`, `scripts/`, and `assets/` next to `SKILL.md`.

## Anthropic Claude Skills

Use manual adaptation unless your host supports multi-file skill folders directly. If a host expects only one instruction file, use `SKILL.md` as the primary instruction and keep `references/playbook.md` available as a linked resource.

## Cursor, Windsurf, GitHub Copilot, And IDE Agents

Use manual adaptation. Attach `SKILL.md` as the rule/instruction file for the task. Attach `references/playbook.md` and `references/acceptance-tests.md` when the task involves review, implementation, or validation.

## LangGraph, CrewAI, AutoGen, And Custom Agent Runtimes

Use manual adaptation. Use `SKILL.md` as the role instruction for the specialist agent. Expose scripts in `scripts/` as local tools. Route outputs through the standard sections: Problem, Inputs, Checks performed, Findings, Decision, Risks, Next actions, and Artifacts.

## Data Platforms And Providers

Use exported schemas, samples, logs, lineage files, metric reports, or model metadata from providers such as Snowflake, BigQuery, Databricks, Postgres, dbt, Dagster, MLflow, DVC, W&B, SageMaker, Vertex AI, Azure ML, or local files. Do not upload private data to external services unless the user explicitly approves that environment.

## Safety Rule

Treat provider output as evidence, not authority. Preserve raw artifacts, record assumptions, and mark unknowns instead of filling gaps with confident guesses.
