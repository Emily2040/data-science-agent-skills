# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `experiment-provenance-ledger`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$experiment-provenance-ledger` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 3: Repro & Pipelines | **Experiment Provenance Ledger** | Record SHA-256 dataset hashes, git commit state, seeds, and hyperparameters per run | `"Capture a cryptographic provenance ledger for this experiment's data files, code state, and seed."` |
| **简体中文** | 阶段 3：可复现性与工程管道 | **实验血缘与溯源账本** | 记录每次实验的数据集 SHA-256 摘要、Git 提交状态、脏工作区标记、随机种子与超参 | `"为本次实验的数据文件、配置文件、Git 提交状态与随机种子生成加密溯源账本。"` |
| **日本語** | ステージ 3：再現性・パイプライン化 | **実験プロヴェナンス台帳（来歴管理）** | データセットのSHA-256ハッシュ・Gitコミット状態・乱数シード・設定を実行ごとに記録 | `"この実験のデータファイル・設定・Git状態・乱数シードの暗号学的プロヴェナンス台帳を生成してください。"` |
| **한국어** | 3단계: 재현성 및 파이프라인 엔지니어링 | **실험 프로비넌스(출처) 원장** | 실험별 데이터셋 SHA-256 해시, Git 커밋·더티 상태, 난수 시드, 하이퍼파라미터를 기록 | `"이번 실험에 사용된 데이터 파일, 설정, Git 상태, 시드에 대한 프로비넌스 원장을 생성해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Teams cannot reproduce last week's best model because data extracts, git working trees, and configs were never hashed.
- **简体中文**: 最优实验结果无法复现，因为训练时未锁定数据快照哈希、代码工作区存在未提交改动或超参散落在手工记录中。
- **日本語**: 学習データやコードの未コミット変更、ハイパーパラメータの記録漏れにより、最良モデルの再現や監査対応ができなくなる。
- **한국어**: 학습 데이터 스냅샷 해시와 Git 작업 트리 상태, 설정값을 기록하지 않아 최고 성능 모델을 재현하거나 감사할 수 없음.

Inspected red flags across all locales: `unversioned dataset`, `dirty code used for final metric`, `missing seed`, `manual artifact rename`, `model chosen without logged rationale`.

---

## 3. Eight-Section Output Contract (Localized Section Headers)

Always emit all eight sections in order. When responding in Chinese, Japanese, or Korean, include the canonical English section key in parentheses so both human stakeholders and automated contract validators can parse the memo:

| # | Canonical Key | English Header | 简体中文标题 | 日本語見出し | 한국어 섹션 제목 |
| --- | --- | --- | --- | --- | --- |
| 1 | `Problem` | `1. Problem` | `1. 问题定义 (Problem)` | `1. 課題定義 (Problem)` | `1. 문제 정의 (Problem)` |
| 2 | `Inputs` | `2. Inputs` | `2. 输入与数据契约 (Inputs)` | `2. 入力データと前提 (Inputs)` | `2. 입력 및 전제 조건 (Inputs)` |
| 3 | `Checks performed` | `3. Checks performed` | `3. 已执行的确定性检查 (Checks performed)` | `3. 実行済み検証 (Checks performed)` | `3. 수행된 검증 (Checks performed)` |
| 4 | `Findings` | `4. Findings` | `4. 关键发现与证据 (Findings)` | `4. 検証結果と根拠 (Findings)` | `4. 주요 발견 및 근거 (Findings)` |
| 5 | `Decision` | `5. Decision` | `5. 决策结论 (Decision)` | `5. 意思決定 (Decision)` | `5. 의사결정 (Decision)` |
| 6 | `Risks` | `6. Risks` | `6. 风险与阻塞项 (Risks)` | `6. リスクとブロッカー (Risks)` | `6. 리스크 및 차단 요인 (Risks)` |
| 7 | `Next actions` | `7. Next actions` | `7. 下一步行动 (Next actions)` | `7. 次のアクション (Next actions)` | `7. 후속 조치 (Next actions)` |
| 8 | `Artifacts` | `8. Artifacts` | `8. 交付物与产物 (Artifacts)` | `8. 成果物 (Artifacts)` | `8. 산출물 및 아티팩트 (Artifacts)` |

---

## 4. Five-State Decision Enum (Canonical Token + Native Verdict)

Always include the exact canonical token (`go`, `fix-first`, `stop`, `proceed-with-risk`, or `needs-owner-review`) alongside the localized verdict:

| Canonical Token | English Verdict | 简体中文判定 | 日本語判定 | 한국어 판정 | Operational Meaning |
| --- | --- | --- | --- | --- | --- |
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/capture_provenance.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/capture_provenance.py`.
