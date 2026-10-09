# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `leakage-adversary`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$leakage-adversary` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 2: Validity & Leakage | **Leakage Adversary** | Red-team ML datasets and pipelines for target, temporal, group, and preprocessing leakage | `"Red-team this train/validation split and feature set for entity overlap and temporal target leakage."` |
| **简体中文** | 阶段 2：有效性验证与防泄漏 | **数据泄漏红队审计** | 对机器学习数据集与特征管道开展标签泄漏、时间穿越与实体重叠红队排查 | `"对训练集与验证集做泄漏红队审计，排查实体交叉、时间穿越和目标泄漏特征。"` |
| **日本語** | ステージ 2：妥当性・リーク検証 | **リーケージ・アドバーサリ（データ漏洩レッドチーム）** | 目的変数・時系列・グループ・前処理のデータリーケージを敵対的視点で徹底検証 | `"学習・検証分割と特徴量パイプラインに対して、エンティティ重複や時系列リークの監査を実行してください。"` |
| **한국어** | 2단계: 타당성 및 누수 검증 | **데이터 누수(Leakage) 레드팀** | 타깃·시계열·그룹·전처리 데이터 누수를 적대적(Red-team) 관점에서 탐지 및 차단 | `"학습·검증 데이터 분할과 피처 파이프라인에서 개체 중복 및 시계열 타깃 누수를 점검해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Models post near-perfect offline validation scores and collapse in production because future or outcome information leaked.
- **简体中文**: 模型离线验证指标虚高，上线后却断崖式下跌，根源在于未来信息、全局统计量或同一实体跨集泄漏。
- **日本語**: 未来情報やターゲット由来の特徴量が学習に混入し、オフライン精度だけが高く本番で破綻する。
- **한국어**: 미래 시점 정보나 타깃 파생 변수가 학습에 유입되어 오프라인 검증 성능만 높고 운영 환경에서 폭락함.

Inspected red flags across all locales: `feature timestamp after target`, `same user in train and test`, `global preprocessing before split`, `leaky aggregate`, `near-perfect simple model`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/split_leakage_probe.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/split_leakage_probe.py`.
