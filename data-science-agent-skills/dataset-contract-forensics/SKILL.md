---
name: dataset-contract-forensics
description: Infer explicit data contracts, primary-key uniqueness rules, value ranges, and freshness SLAs from messy CSV, TSV, or warehouse extracts. Use when turning undocumented upstream tables into enforceable schema and validation tests.
---

# Dataset Contract Forensics

## Mission

Infer practical data contracts, schema expectations, and validation tests from messy real datasets.

Primary failure mode prevented: data breaks downstream because implicit assumptions about schema, meaning, ranges, uniqueness, and freshness are never written down.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`CSV, Parquet, JSONL, SQL schema, or sample extracts, downstream use case, known business rules, refresh cadence`) must be audited for red flags such as `sample too small`, `IDs not unique when assumed unique`, `silent enum expansion`, `date freshness inconsistent`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/profile_table.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`sample too small`, `IDs not unique when assumed unique`, `silent enum expansion`, `date freshness inconsistent`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Dataset Contract Forensics decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `contract draft`, `test inventory`, `confidence labels`, `owner questions`, `tool-specific implementation hints`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/profile_table.py path/to/extract.csv --max-rows 10000
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Profile columns, nulls, uniqueness, cardinality, ranges, formats, and candidate keys.
2. Identify semantic expectations that cannot be inferred mechanically and mark them for owner confirmation.
3. Draft tests for schema, freshness, distribution, referential integrity, and accepted values.
4. Map each test to Great Expectations, Pandera, dbt, or plain SQL where appropriate.
5. Return a contract draft with confidence levels and confirmation questions.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Dataset Contract Forensics — Infer and verify schema, grain, uniqueness, freshness, and null contracts.
- **简体中文**: 数据契约取证与核验 — 逆向推导并校验表结构、主键粒度、唯一性、时效与空值契约（参见 `references/multilingual-guide.md`）。
- **日本語**: データセット契約フォレンジック — スキーマ・粒度・一意性・鮮度・欠損ルールを推論し契約違反を検出（`references/multilingual-guide.md` を参照）。
- **한국어**: 데이터셋 계약 포렌식 — 스키마·집계 단위(Grain)·고유성·최신성·결측 계약을 추론 및 검증 (`references/multilingual-guide.md` 참조).

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
