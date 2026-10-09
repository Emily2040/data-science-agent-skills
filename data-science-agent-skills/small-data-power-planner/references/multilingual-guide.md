# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `small-data-power-planner`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$small-data-power-planner` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 2: Validity & Leakage | **Small Data Power Planner** | Calculate minimum detectable effect (MDE), sample power, and low-N overfitting bounds | `"Check statistical power, MDE, and events-per-variable limits for this small-sample study."` |
| **简体中文** | 阶段 2：有效性验证与防泄漏 | **小样本统计功效与容量规划** | 计算最小可检测效应（MDE）、统计功效与小样本过拟合边界 | `"核算当前样本量下的最小可检测效应（MDE）、统计功效以及每变量事件数（EPV）上限。"` |
| **日本語** | ステージ 2：妥当性・リーク検証 | **小標本検出力・MDEプランナー** | 最小検出可能効果（MDE）・統計的検出力・少数サンプルでの過学習境界を算出 | `"この小標本実験の統計的検出力、MDE、および変数あたりイベント数（EPV）の上限を計算してください。"` |
| **한국어** | 2단계: 타당성 및 누수 검증 | **소표본 검정력·MDE 플래너** | 최소감지효과(MDE), 통계적 검정력, 소표본 과적합 경계(EPV)를 산출 | `"이 소표본 실험의 통계적 검정력, 최소감지효과(MDE), 변수당 이벤트 수(EPV) 한계를 계산해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Teams run underpowered A/B tests or fit high-dimensional models on tiny cohorts where noise dominates signal.
- **简体中文**: 在样本量严重不足的场景下强行开展 A/B 实验或拟合高维复杂模型，将随机噪声当成显著结论。
- **日本語**: 検出力不足のA/Bテストや、イベント数に対して次元が高すぎるモデルを学習し、ノイズを有意差と誤認する。
- **한국어**: 검정력이 부족한 A/B 테스트를 강행하거나 표본 대비 고차원 모델을 학습해 노이즈를 유의미한 신호로 오인함.

Inspected red flags across all locales: `more features than observations`, `rare outcome with random split`, `single holdout set only`, `unreported uncertainty`, `high-stakes decision from tiny sample`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/power_sample_size.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/power_sample_size.py`.
