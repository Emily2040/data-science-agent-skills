# Leakage Adversary

![Hero shot](assets/hero-shot.png)

## What This Skill Solves

Actively search ML datasets and pipelines for target, temporal, group, split, join, and preprocessing leakage.

Pain point: Models look excellent offline and fail in production because future or target information leaked into training.

Why it matters: Leakage must be attacked like a failure mode; ordinary metric review usually detects it too late.

## When To Use It

Use `$leakage-adversary` when the task is to actively search ML datasets and pipelines for target, temporal, group, split, join, and preprocessing leakage. It is built for judgment-heavy work where the agent must inspect evidence, name assumptions, and produce a decision-ready artifact.

## When Not To Use It

- Do not use this skill for generic spreadsheet editing, chart styling, or file conversion unless the data science decision workflow is the main task.
- Do not use it as a substitute for legal, medical, financial, or compliance approval.
- Do not use helper scripts as proof by themselves; scripts provide evidence checks, not full expert judgment.

## Inputs

- training data
- target definition
- split logic
- feature list
- pipeline code or notebook

## Workflow

1. Restate what information is available at decision time.
2. Probe features, joins, encoders, aggregations, and preprocessing for post-outcome information.
3. Check split logic for temporal bleed, group overlap, duplicated entities, and near-duplicates.
4. Review suspiciously strong features and validation performance jumps.
5. Return leakage findings with severity, evidence, and safer split or feature alternatives.

## Outputs

- leakage attack report
- feature risk table
- split risk table
- safe evaluation recommendation
- blocker list

Every final response should include: Problem, Inputs, Checks performed, Findings, Decision, Risks, Next actions, and Artifacts.

## Use With Other Agents And Providers

![Infographic](assets/reddit-infographic.png)

### OpenAI Codex Or ChatGPT Agents

Copy this whole folder into the configured skills directory. Invoke it with `$leakage-adversary` or let the frontmatter description trigger it. Keep `references/`, `scripts/`, and `assets/` beside `SKILL.md`.

### Anthropic Claude Skills

Use manual adaptation unless the host supports multi-file skill folders directly. Use `SKILL.md` as the primary skill instruction. Keep `references/playbook.md` and `references/acceptance-tests.md` attached as supporting resources when possible.

### Cursor, Windsurf, GitHub Copilot, And IDE Agents

Use manual adaptation. Attach `SKILL.md` as the task rule. Attach `references/playbook.md` for review or implementation work, and run helper scripts locally when file evidence is available.

### LangGraph, CrewAI, AutoGen, And Custom Runtimes

Use manual adaptation. Treat this folder as a specialist-agent role pack. Expose scripts in `scripts/` as local tools and route results through the standard output contract.

### Data Providers And Platforms

Use local exports or metadata from Snowflake, BigQuery, Databricks, Postgres, dbt, Dagster, MLflow, DVC, W&B, SageMaker, Vertex AI, Azure ML, or local files. Do not upload private data to external providers unless the user explicitly approves that environment.

## Included Files

- `SKILL.md`: trigger metadata and core workflow.
- `agents/openai.yaml`: OpenAI UI metadata and invocation defaults.
- `.gitignore`: keeps Python bytecode caches and local OS files out of PR payloads.
- `references/playbook.md`: checklist, decision rules, red flags, and evidence discipline.
- `references/acceptance-tests.md`: clean, messy, and adversarial forward tests.
- `references/evidence-map.md`: public evidence and non-duplication rationale.
- `references/infographic-spec.md`: Reddit visual brief.
- `references/provider-interop.md`: provider and agent usage guide.
- `scripts/`: deterministic local helper scripts.
- `assets/hero-shot.png`: wide hero image for PRs and docs.
- `assets/reddit-infographic.png`: 1080x1350 Reddit-ready infographic.

## Helper Scripts

Run scripts locally against explicit user-provided artifacts. They are support checks, not complete replacements for expert review.

- `scripts/quick_validate_skill.py .`: validate this standalone skill folder. Exit `0` means the package is structurally complete.
- `scripts/checklist_score.py checklist.json --strict`: score pass/partial/fail/blocker checklist JSON. Exit nonzero when strict mode finds anything below ready.
- `scripts/split_leakage_probe.py --train train.csv --test test.csv --key entity_id --target target`: detect entity overlap and suspicious target-like feature names.

## Red Flags

- feature timestamp after target
- same user in train and test
- global preprocessing before split
- leaky aggregate
- near-perfect simple model

## Validation

Run `python scripts/quick_validate_skill.py .` inside this folder. For script-backed checks, run the relevant script on local fixture data or user-provided artifacts. Validate the result against `references/acceptance-tests.md`.

## Completeness Checklist

- [x] Independent `SKILL.md` with specific trigger metadata.
- [x] README page with problem, use cases, inputs, workflow, outputs, provider guidance, and validation.
- [x] Provider and multi-agent interoperability guide.
- [x] Skill-specific playbook and acceptance tests.
- [x] Hero shot and Reddit infographic assets.
- [x] Local deterministic helper scripts where useful.
- [x] Explicit red flags and evidence discipline.
