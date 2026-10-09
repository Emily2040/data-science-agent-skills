---
name: domain-expert-collaboration-loop
description: Structure subject-matter expert (SME) annotation, rubric calibration, and edge-case adjudication for data science workflows. Use when measuring inter-rater agreement (Cohen's kappa), resolving label ambiguity, and encoding domain constraints.
---

# Domain Expert Collaboration Loop

## Mission

Structure collaboration between data scientists, AI agents, and domain experts when domain judgment is required.

Primary failure mode prevented: agents and analysts can produce plausible work that misses domain constraints, tacit knowledge, and operational reality.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`analysis or model plan, domain experts, known constraints, critical assumptions`) must be audited for red flags such as `SME asked to rubber-stamp`, `domain constraints undocumented`, `agent inference treated as fact`, `feedback not linked to changes`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/sme_label_agreement.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`SME asked to rubber-stamp`, `domain constraints undocumented`, `agent inference treated as fact`, `feedback not linked to changes`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Domain Expert Collaboration Loop decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `SME interview guide`, `assumption ledger`, `challenge-question list`, `evidence log`, `signoff and open-risk record`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/sme_label_agreement.py path/to/sme_labels.csv --rater-a sme_a --rater-b sme_b
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. List assumptions that require domain validation.
2. Prepare SME questions tied to decisions, not generic review.
3. Capture evidence, objections, corrections, and unresolved uncertainty.
4. Update analysis plan or model design based on review.
5. Return an assumption ledger and signoff record.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Domain Expert Collaboration Loop — Measure inter-annotator agreement (Cohen's kappa) and resolve SME label taxonomy disputes.
- **简体中文**: 领域专家协同与标注仲裁环 — 量化领域专家标注一致性（Cohen's Kappa），制定边界样本仲裁准则与标签口径说明（参见 `references/multilingual-guide.md`）。
- **日本語**: ドメインエキスパート協働ループ — 専門家のアノテーション一致度（Cohenのκ係数）を計測し、境界事例の裁定基準を整備（`references/multilingual-guide.md` を参照）。
- **한국어**: 도메인 전문가(SME) 협업 루프 — 전문가 간 라벨 일치도(Cohen's Kappa)를 측정하고 경계 사례에 대한 라벨 조정 루브릭 수립 (`references/multilingual-guide.md` 참조).

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
