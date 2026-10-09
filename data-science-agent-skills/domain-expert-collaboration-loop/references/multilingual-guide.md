# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `domain-expert-collaboration-loop`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$domain-expert-collaboration-loop` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 4: Eval & Governance | **Domain Expert Collaboration Loop** | Measure inter-annotator agreement (Cohen's kappa) and resolve SME label taxonomy disputes | `"Calculate SME inter-annotator agreement and design a label adjudication rubric for disputed rows."` |
| **简体中文** | 阶段 4：评估、治理与专家协同 | **领域专家协同与标注仲裁环** | 量化领域专家标注一致性（Cohen's Kappa），制定边界样本仲裁准则与标签口径说明 | `"计算专家标注结果的 Cohen's Kappa 一致性系数，并梳理分歧样本的仲裁规则。"` |
| **日本語** | ステージ 4：評価・ガバナンス・SME協働 | **ドメインエキスパート協働ループ** | 専門家のアノテーション一致度（Cohenのκ係数）を計測し、境界事例の裁定基準を整備 | `"SMEアノテーションの一致率とCohenのκ係数を算出し、判断が割れた事例の裁定ルーブリックを作成してください。"` |
| **한국어** | 4단계: 평가, 거버넌스 및 전문가 루프 | **도메인 전문가(SME) 협업 루프** | 전문가 간 라벨 일치도(Cohen's Kappa)를 측정하고 경계 사례에 대한 라벨 조정 루브릭 수립 | `"도메인 전문가 라벨링의 일치율과 Cohen's Kappa를 계산하고 불일치 샘플 조정 기준을 설계해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Models train on noisy labels because domain experts interpret edge cases differently without an adjudication rubric.
- **简体中文**: 多位业务专家对疑难样本的判定标准不一，团队在未做一致性检验（Kappa）的情况下直接拿分歧标签训练模型。
- **日本語**: 複数のドメイン専門家間で判断基準が揃っていないまま不整合なラベルで学習し、モデルの天井が下がる。
- **한국어**: 현업 전문가마다 경계 사례 해석 기준이 다른데도 일치도 검증 없이 노이즈가 섞인 라벨로 모델을 학습함.

Inspected red flags across all locales: `SME asked to rubber-stamp`, `domain constraints undocumented`, `agent inference treated as fact`, `feedback not linked to changes`, `signoff missing`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/sme_label_agreement.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/sme_label_agreement.py`.
