# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `evaluation-reality-check`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$evaluation-reality-check` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 4: Eval & Governance | **Evaluation Reality Check** | Audit subgroup slice errors, probability calibration, and offline-to-business translation | `"Audit these model predictions for subgroup slice accuracy gaps and probability calibration error."` |
| **简体中文** | 阶段 4：评估、治理与专家协同 | **模型评估真实性核查** | 审计分群切片误差（Slice Error）、概率校准度（Brier）与离线指标到业务收益的映射 | `"对模型预测结果开展分群切片误差审计与概率校准检验，评估其真实业务可用性。"` |
| **日本語** | ステージ 4：評価・ガバナンス・SME協働 | **モデル評価リアリティチェック** | サブグループ別のスライス誤差・確率キャリブレーション・ビジネス価値への換算を監査 | `"予測結果のサブグループ間精度格差とBrierキャリブレーション誤差を監査してください。"` |
| **한국어** | 4단계: 평가, 거버넌스 및 전문가 루프 | **모델 평가 리얼리티 체크** | 세부 집단(Slice)별 오차 격차, 확률 보정(Calibration), 오프라인 지표의 비즈니스 전환 타당성 감사 | `"모델 예측값의 서브그룹 슬라이스별 정확도 격차와 확률 보정(Brier 점수) 오차를 감사해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Aggregate AUC or accuracy hides severe degradation on critical customer slices, cold-start cohorts, or tail events.
- **简体中文**: 全局平均 AUC 或准确率掩盖了核心客群、冷启动用户或高价值长尾切片上的严重性能塌陷与概率失准。
- **日本語**: 全体の平均AUCや正解率だけでは、重要セグメントやコールドスタート層での重大な精度劣化を見落とす。
- **한국어**: 전체 평균 AUC나 정확도 뒤에 핵심 고객군, 콜드스타트 집단, 고위험 구간에서의 심각한 성능 저하가 가려짐.

Inspected red flags across all locales: `random split for temporal deployment`, `test set reused for tuning`, `no external validation for domain shift`, `single aggregate metric`, `label delay ignored`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/slice_error_auditor.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/slice_error_auditor.py`.
