---
name: baseline-ablation-lab
description: Design honest naive, rule-based, and linear baselines alongside feature and component ablations before accepting complex ML models. Use when challenging model complexity against latency, cost, seed stability, and minimum required lift.
---

# Baseline Ablation Lab

## Mission

Design honest baselines and ablations before complex models are accepted.

Primary failure mode prevented: teams ship complex models without proving they outperform simple, cheaper, or safer alternatives.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`task type, dataset summary, candidate model, metric`) must be audited for red flags such as `no naive baseline`, `single random seed`, `improvement below uncertainty`, `cost ignored`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/ablation_delta_audit.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`no naive baseline`, `single random seed`, `improvement below uncertainty`, `cost ignored`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Baseline Ablation Lab decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `baseline list`, `ablation matrix`, `complexity penalty table`, `acceptance criteria`, `report template`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/ablation_delta_audit.py path/to/comparison.json
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Select task-appropriate naive, rule-based, statistical, and simple ML baselines.
2. Define ablations for features, model components, preprocessing, data volume, and inference cost.
3. Set metric and uncertainty reporting before running comparisons.
4. Identify complexity penalties: latency, maintainability, explainability, and monitoring burden.
5. Return a baseline and ablation matrix with accept/reject criteria.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Baseline Ablation Lab — Require naive/simple baselines and controlled ablations before accepting complex models.
- **简体中文**: 基线对标与消融实验室 — 在接纳复杂模型前强制开展简单基线对标、多随机种子复现与特征消融实验（参见 `references/multilingual-guide.md`）。
- **日本語**: ベースライン＆アブレーション実験室 — 複雑なモデルを採用する前に単純ベースラインとの比較・複数シード検証・アブレーションを徹底（`references/multilingual-guide.md` を参照）。
- **한국어**: 베이스라인 및 어블레이션 랩 — 복잡한 모델 채택 전 단순 베이스라인 비교, 다중 시드 검증, 피처 어블레이션을 강제 (`references/multilingual-guide.md` 참조).

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
