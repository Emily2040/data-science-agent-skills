---
name: ai-data-readiness-triage
description: Assess whether a dataset or data domain is ready for AI, analytics, or modeling before committing project budget. Use when triaging table schemas, missingness, label coverage, ownership, freshness, and PII risk to issue a go, fix-first, or stop decision.
---

# AI Data Readiness Triage

## Mission

Assess whether a dataset or data domain is ready for AI, analytics, or modeling before a project commits time and budget.

Primary failure mode prevented: ai projects stall because access, freshness, quality, lineage, privacy, labels, and ownership are discovered too late.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`dataset paths or schemas, data owner, intended use case, privacy or compliance constraints`) must be audited for red flags such as `unknown owner`, `no label source`, `PII without approved use`, `high missingness in core fields`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/profile_table.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`unknown owner`, `no label source`, `PII without approved use`, `high missingness in core fields`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit AI Data Readiness Triage decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `readiness scorecard`, `blocker register`, `minimum remediation plan`, `label and privacy notes`, `go/no-go recommendation`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/profile_table.py path/to/dataset.csv --max-rows 10000
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Inventory access, ownership, lineage, refresh cadence, privacy, and retention constraints.
2. Profile quality, missingness, duplication, outliers, type drift, and label coverage.
3. Score readiness across governance, quality, representativeness, reproducibility, and operational fit.
4. Classify blockers as stop, fix-first, monitor, or accepted risk.
5. Return a readiness scorecard with the smallest credible next action.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: AI Data Readiness Triage — Score whether datasets are ready for AI, analytics, or modeling.
- **简体中文**: AI 数据就绪度评估 — 在投入研发预算前评估数据集是否具备 AI、分析或建模条件（参见 `references/multilingual-guide.md`）。
- **日本語**: AIデータ準備度トリアージ — AI・分析・モデリング着手前にデータの利用可能性と品質を判定（`references/multilingual-guide.md` を参照）。
- **한국어**: AI 데이터 준비도 트리아지 — 예산과 엔지니어링 투입 전 AI·분석·모델링용 데이터 준비 상태 진단 (`references/multilingual-guide.md` 참조).

## Progressive References

- Read `references/multilingual-guide.md` when the user prompts in Simplified Chinese (简体中文), Japanese (日本語), or Korean (한국어), or requests a bilingual/multilingual decision memo.

- Read `references/playbook.md` for detailed step-by-step execution rules and escalation criteria.
- Read `references/quality-rubric.md` to score the output and verify that dataset red flags are separated from agent failure conditions.
- Read `references/acceptance-tests.md` and `references/benchmark-plan.md` when forward-testing clean, messy, and adversarial cases.
- Read `references/provider-interop.md` and `references/agent-portability.md` when adapting across cloud providers or agent hosts.

## Output Contract

Always return these exact eight sections in order:

1. `Problem`
2. `Inputs`
3. `Checks performed`
4. `Findings`
5. `Decision` (`go` | `fix-first` | `stop` | `proceed-with-risk` | `needs-owner-review`)
6. `Risks`
7. `Next actions`
8. `Artifacts`

## Final Checks

- Verify that every factual finding cites the exact file, column, metric, or script output that produced it.
- Run `python scripts/quick_validate_skill.py . --strict` after modifying any file in this skill package.
