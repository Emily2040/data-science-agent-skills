---
name: experiment-provenance-ledger
description: Capture cryptographic dataset hashes, git commit state, environment manifests, random seeds, and decision history for ML experiments. Use when building an auditable provenance ledger so model results can be reproduced or traced back to exact inputs.
---

# Experiment Provenance Ledger

## Mission

Preserve experiment provenance across code, data, environment, parameters, metrics, artifacts, and human decisions.

Primary failure mode prevented: teams cannot explain which model, data, code, or parameters produced a result after the fact.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`repo path, dataset identifiers, environment files, training command`) must be audited for red flags such as `unversioned dataset`, `dirty code used for final metric`, `missing seed`, `manual artifact rename`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/capture_provenance.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`unversioned dataset`, `dirty code used for final metric`, `missing seed`, `manual artifact rename`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Experiment Provenance Ledger decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `provenance ledger`, `artifact manifest`, `decision log`, `tool mapping`, `audit gaps`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/capture_provenance.py path/to/train.csv path/to/config.yaml --seed 42
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Capture code version, dirty state, environment, data references, parameters, seeds, and runtime.
2. Record metrics and artifacts with owner, purpose, and retention expectation.
3. Link human decisions, exclusions, and model-selection rationale.
4. Map entries to MLflow, DVC, W&B, or plain JSON depending on the stack.
5. Return a ledger and missing-provenance risk list.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Experiment Provenance Ledger — Record SHA-256 dataset hashes, git commit state, seeds, and hyperparameters per run.
- **简体中文**: 实验血缘与溯源账本 — 记录每次实验的数据集 SHA-256 摘要、Git 提交状态、脏工作区标记、随机种子与超参（参见 `references/multilingual-guide.md`）。
- **日本語**: 実験プロヴェナンス台帳（来歴管理） — データセットのSHA-256ハッシュ・Gitコミット状態・乱数シード・設定を実行ごとに記録（`references/multilingual-guide.md` を参照）。
- **한국어**: 실험 프로비넌스(출처) 원장 — 실험별 데이터셋 SHA-256 해시, Git 커밋·더티 상태, 난수 시드, 하이퍼파라미터를 기록 (`references/multilingual-guide.md` 참조).

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
