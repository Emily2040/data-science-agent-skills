---
name: messy-data-cleanroom
description: Design reversible, auditable data-cleaning pipelines that quarantine corrupt records without mutating raw source extracts. Use when standardizing schemas, deduplicating entities, and logging row-level exclusion impact.
---

# Messy Data Cleanroom

## Mission

Design transparent, reversible cleaning plans for messy datasets without silently mutating evidence.

Primary failure mode prevented: cleaning decisions get buried in notebooks, making results impossible to audit or reproduce.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`raw dataset, data dictionary if available, analysis goal, allowed transformation constraints`) must be audited for red flags such as `overwriting raw data`, `dropping rows without impact analysis`, `unit conversion not documented`, `outlier removal tied to desired result`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/profile_table.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`overwriting raw data`, `dropping rows without impact analysis`, `unit conversion not documented`, `outlier removal tied to desired result`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Messy Data Cleanroom decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `cleaning ledger`, `transformation plan`, `row impact summary`, `reversal plan`, `review questions`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/profile_table.py path/to/raw_extract.csv --max-rows 10000
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Profile missingness, duplicates, outliers, types, formats, units, and conflicting records.
2. Separate factual corrections, normalization, exclusions, imputations, and unresolved anomalies.
3. For each proposed transformation, record rationale, affected rows, risk, and reversal method.
4. Prefer derived clean columns or versioned outputs over overwriting raw evidence.
5. Return a cleaning ledger and transformed-data acceptance criteria.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Messy Data Cleanroom — Design reversible, auditable cleaning and quarantine rules without mutating raw data.
- **简体中文**: 脏数据净室治理 — 在不篡改原始数据的前提下设计可逆、可审计的清洗与隔离规则（参见 `references/multilingual-guide.md`）。
- **日本語**: メッシーデータ・クリーンルーム — 生データを破壊せず、可逆かつ監査可能なクレンジング・隔離ルールを設計（`references/multilingual-guide.md` を参照）。
- **한국어**: 메시 데이터 클린룸 — 원본 데이터를 훼손하지 않고 가역적·감사가능한 정제 및 격리(Quarantine) 규칙 설계 (`references/multilingual-guide.md` 참조).

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
