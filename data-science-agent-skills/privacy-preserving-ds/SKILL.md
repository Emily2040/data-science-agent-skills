---
name: privacy-preserving-ds
description: Assess PII exposure, re-identification risk, and quasi-identifier linkage in analytics and ML datasets. Use when designing redaction, aggregation, k-anonymity, differential privacy, or clean-room controls before sharing or modeling sensitive data.
---

# Privacy Preserving Data Science

## Mission

Guide data science work on sensitive data using minimization, local-first analysis, de-identification, synthetic data, or privacy-preserving methods.

Primary failure mode prevented: teams copy sensitive data into notebooks and tools without a minimization or privacy strategy.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`data schema or sample, sensitive fields, analysis goal, approved environment`) must be audited for red flags such as `raw PII in notebook output`, `unapproved cloud copy`, `identifier kept for convenience`, `synthetic data claimed risk-free`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/profile_table.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`raw PII in notebook output`, `unapproved cloud copy`, `identifier kept for convenience`, `synthetic data claimed risk-free`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Privacy Preserving Data Science decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `PII and sensitivity inventory`, `minimization plan`, `safe-compute recommendation`, `export rules`, `residual-risk note`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/profile_table.py path/to/sensitive_extract.csv --max-rows 10000
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Identify direct identifiers, quasi-identifiers, sensitive attributes, and linkage risks.
2. Minimize fields and rows to the decision need.
3. Choose local-first, aggregated, redacted, synthetic, federated, differential privacy, or secure enclave path.
4. Define what can be exported, logged, cached, or shared.
5. Return a privacy-safe analysis plan and residual risk note.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Privacy Preserving DS — Audit direct PII, quasi-identifiers, k-anonymity risks, and retention boundaries.
- **简体中文**: 隐私保护数据科学审计 — 审计直接个人身份信息（PII）、准标识符重识别风险、最小化原则与数据留存边界（参见 `references/multilingual-guide.md`）。
- **日本語**: プライバシー保護データサイエンス — 直接PII・準識別子による再識別リスク・データ最小化・保持期限ルールを監査（`references/multilingual-guide.md` を参照）。
- **한국어**: 프라이버시 보호 데이터 사이언스 — 직접 개인정보(PII), 준식별자(Quasi-identifier) 재식별 위험, 최소 수집 및 보존 기한을 감사 (`references/multilingual-guide.md` 참조).

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
