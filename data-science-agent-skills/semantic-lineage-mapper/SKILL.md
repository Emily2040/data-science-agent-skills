---
name: semantic-lineage-mapper
description: Reconstruct end-to-end table, file, column, and metric lineage across SQL queries, Python scripts, notebooks, and BI configs. Use when tracing upstream sources and downstream blast radius before refactoring pipelines or deprecating fields.
---

# Semantic Lineage Mapper

## Mission

Reconstruct practical lineage across SQL, notebooks, scripts, dashboards, model artifacts, and pipeline configs.

Primary failure mode prevented: teams cannot explain where a metric, feature, or model input came from after it breaks or is challenged.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`SQL files, notebooks, pipeline configs, dashboard definitions`) must be audited for red flags such as `dashboard-only metric logic`, `manual spreadsheet hop`, `feature generated outside pipeline`, `PII source unclear`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/extract_lineage_tokens.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`dashboard-only metric logic`, `manual spreadsheet hop`, `feature generated outside pipeline`, `PII source unclear`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Semantic Lineage Mapper decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `lineage graph outline`, `risk nodes`, `owner questions`, `unknown dependency list`, `audit narrative`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/extract_lineage_tokens.py sql/ pipelines/ notebooks/
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Extract table, column, file, feature, model, and artifact references.
2. Group references into sources, transforms, outputs, and decision surfaces.
3. Mark unknown or manually managed dependencies instead of dropping them.
4. Identify high-risk nodes: ownerless, PII, stale, reused, or weakly documented.
5. Return a lineage map, risk register, and confirmation checklist.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Semantic Lineage Mapper — Trace table, column, and metric definitions across SQL, notebooks, and pipelines.
- **简体中文**: 语义血缘与口径映射 — 跨 SQL、Notebook 与数据管道追踪表、字段与指标的真实语义口径（参见 `references/multilingual-guide.md`）。
- **日本語**: セマンティック系譜マッパー — SQL・Notebook・パイプラインを横断してテーブル・列・指標の意味論的系譜を追跡（`references/multilingual-guide.md` を参照）。
- **한국어**: 시맨틱 리니지 매퍼 — SQL, 노트북, 파이프라인 전반에서 테이블·컬럼·지표의 의미론적 계보 추적 (`references/multilingual-guide.md` 참조).

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
