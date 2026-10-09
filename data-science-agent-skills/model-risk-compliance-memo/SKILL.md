---
name: model-risk-compliance-memo
description: Produce governance-ready model risk assessments covering blast radius, affected populations, fairness slices, fallback policies, and rollback owners. Use when preparing high-impact ML or AI systems for compliance, legal, or release gate review.
---

# Model Risk Compliance Memo

## Mission

Create concise model risk and compliance memos for review, audit, launch, or executive approval.

Primary failure mode prevented: data science teams often lack a crisp artifact that explains model purpose, risk, evidence, limits, and controls.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`model purpose, data sources, users affected, evaluation evidence`) must be audited for red flags such as `affected users undefined`, `no rollback owner`, `fairness not evaluated where relevant`, `privacy basis unclear`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/risk_tier_gate.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`affected users undefined`, `no rollback owner`, `fairness not evaluated where relevant`, `privacy basis unclear`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Model Risk Compliance Memo decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `model risk memo`, `risk register`, `control map`, `approval conditions`, `signoff checklist`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/risk_tier_gate.py path/to/risk_memo.json
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Define model purpose, non-goals, user impact, and decision authority.
2. Summarize data, training, evaluation, fairness, privacy, explainability, and limitations.
3. Classify risks by severity, likelihood, detectability, and owner.
4. Document controls, monitoring, rollback, and approval conditions.
5. Return a memo with open blockers and required signoffs.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Model Risk Compliance Memo — Document blast radius, human-in-the-loop override, fallback policy, and governance gates.
- **简体中文**: 模型风险与合规备忘录 — 界定模型爆炸半径、人工复核兜底机制、回滚责任人与合规上线门禁（参见 `references/multilingual-guide.md`）。
- **日本語**: モデルリスク・コンプライアンスメモ — 影響範囲（ブラスト半径）・人間による介入（HITL）・フォールバック・ロールバック責任者を審査（`references/multilingual-guide.md` を参照）。
- **한국어**: 모델 리스크 및 컴플라이언스 메모 — 모델 영향 범위(Blast Radius), 인간 개입(HITL) 통제, 폴백 정책, 롤백 책임자를 검증 및 문서화 (`references/multilingual-guide.md` 참조).

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
