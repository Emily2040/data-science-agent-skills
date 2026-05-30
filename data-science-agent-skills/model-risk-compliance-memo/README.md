# Model Risk Compliance Memo

![Hero shot](assets/hero-shot.png)

## What This Skill Solves

Create concise model risk and compliance memos for review, audit, launch, or executive approval.

Pain point: Data science teams often lack a crisp artifact that explains model purpose, risk, evidence, limits, and controls.

Why it matters: A standard memo turns model risk from scattered notes into an approval-ready record.

## When To Use It

Use `$model-risk-compliance-memo` when the task is to create concise model risk and compliance memos for review, audit, launch, or executive approval. It is built for judgment-heavy work where the agent must inspect evidence, name assumptions, and produce a decision-ready artifact.

## When Not To Use It

- Do not use this skill for generic spreadsheet editing, chart styling, or file conversion unless the data science decision workflow is the main task.
- Do not use it as a substitute for legal, medical, financial, or compliance approval.
- Do not use helper scripts as proof by themselves; scripts provide evidence checks, not full expert judgment.
- Escalate to the responsible privacy, security, legal, or model-risk owner when policy approval is required.

## Inputs

- model purpose
- data sources
- users affected
- evaluation evidence
- privacy and fairness concerns
- monitoring plan

## Workflow

1. Define model purpose, non-goals, user impact, and decision authority.
2. Summarize data, training, evaluation, fairness, privacy, explainability, and limitations.
3. Classify risks by severity, likelihood, detectability, and owner.
4. Document controls, monitoring, rollback, and approval conditions.
5. Return a memo with open blockers and required signoffs.

## Outputs

- model risk memo
- risk register
- control map
- approval conditions
- signoff checklist

Every final response should include: Problem, Inputs, Checks performed, Findings, Decision, Risks, Next actions, and Artifacts.

## Use With Other Agents And Providers

![Infographic](assets/reddit-infographic.png)

### OpenAI Codex Or ChatGPT Agents

Copy this whole folder into the configured skills directory. Invoke it with `$model-risk-compliance-memo` or let the frontmatter description trigger it. Keep `references/`, `scripts/`, and `assets/` beside `SKILL.md`.

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

## Red Flags

- affected users undefined
- no rollback owner
- fairness not evaluated where relevant
- privacy basis unclear
- monitoring absent

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
