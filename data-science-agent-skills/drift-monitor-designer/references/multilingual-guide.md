# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `drift-monitor-designer`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$drift-monitor-designer` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 5: Ops & Storytelling | **Drift Monitor Designer** | Detect mean shifts, variance explosions, constant-column breaks, NaNs, and missing-rate spikes | `"Compare baseline and current production feature distributions and design actionable drift alerts."` |
| **简体中文** | 阶段 5：生产交付、监控与叙事 | **数据与概念漂移监控设计** | 检测均值偏移、方差暴增、常量列突变、NaN 污染与缺失率飙升，设计分级告警动作 | `"对比基线与当前线上特征分布，排查均值、方差、常量列与缺失率漂移并设计告警门限。"` |
| **日本語** | ステージ 5：本番運用・監視・意思決定伝達 | **ドリフトモニター設計** | 平均シフト・分散爆発・定数列の崩壊・NaN混入・欠損率急増を検知し実践的なアラートを設計 | `"ベースラインと現在の特徴量分布を比較し、平均・分散・欠損率ドリフトの監視ルールを設計してください。"` |
| **한국어** | 5단계: 프로덕션 운영 및 인사이트 전달 | **드리프트 모니터 디자이너** | 평균 이동, 분산 폭증, 상수 컬럼 깨짐, NaN 오염, 결측률 급증을 탐지하고 실행 가능한 알림 설계 | `"베이스라인과 현재 운영 피처 분포를 비교해 평균·분산·결측률 드리프트를 진단하고 알림 기준을 설계해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Uncalibrated drift alerts either flood on-call engineers with false alarms or miss variance explosions and NaN corruption.
- **简体中文**: 监控只看均值不看方差与缺失率，或者阈值未校准导致告警风暴，掩盖了真正的上游字段损坏与分布漂移。
- **日本語**: 平均値だけを見て分散爆発やNaN汚染を見逃したり、閾値が未調整でオオカミ少年アラートを連発してしまう。
- **한국어**: 평균만 보다가 분산 폭증이나 NaN 오염을 놓치거나, 임계값 미조정으로 온콜 알림 피로도만 높임.

Inspected red flags across all locales: `alerts with no owner`, `thresholds copied from defaults`, `label delay ignored`, `no baseline window`, `retrain triggered without evaluation`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/drift_probe.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/drift_probe.py`.
