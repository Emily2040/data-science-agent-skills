# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `data-science-incident-rca`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$data-science-incident-rca` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 5: Ops & Storytelling | **Data Science Incident RCA** | Correlate broken dashboards or model drops across ingestion, schema, feature, model, and metric layers | `"Correlate this incident timeline against upstream pipeline, schema, feature, and deployment events."` |
| **简体中文** | 阶段 5：生产交付、监控与叙事 | **数据科学事故根因分析（RCA）** | 跨数据接入、表结构、特征计算、模型版本与指标口径五层关联时间线，定位线上异常根因 | `"将本次线上事故时间点与上游数据管道、Schema、特征和发布事件做时间线关联，定位根因。"` |
| **日本語** | ステージ 5：本番運用・監視・意思決定伝達 | **データサイエンス・インシデント根本原因分析（RCA）** | データ取込・スキーマ・特徴量・モデル・指標定義の5層でイベント時系列を相関させ原因を特定 | `"インシデント発生時刻と上流パイプライン・スキーマ・デプロイのイベント時系列を突合し、根本原因を特定してください。"` |
| **한국어** | 5단계: 프로덕션 운영 및 인사이트 전달 | **데이터 사이언스 인시던트 근본원인분석(RCA)** | 데이터 수집·스키마·피처·모델·지표 5개 계층의 이벤트 타임라인을 상관 분석해 장애 원인 규명 | `"인시던트 발생 시각과 업스트림 파이프라인·스키마·피처·배포 이벤트 타임라인을 대조해 근본 원인을 찾아 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Teams retrain models during an incident when the real root cause is an upstream schema change or deployment config shift.
- **简体中文**: 线上指标或模型预测突降时盲目重训模型，却忽略了故障前刚发生的上游字段变更、时区改动或发布配置漂移。
- **日本語**: 上流のスキーマ変更やデプロイ設定ミスが原因なのに、現象だけを見てモデルの再学習に時間を浪費してしまう。
- **한국어**: 실제 원인은 업스트림 스키마 변경이나 배포 설정 오류인데 현상만 보고 모델 재학습에 시간을 허비함.

Inspected red flags across all locales: `no timestamped evidence`, `only one layer investigated`, `impact not quantified`, `human process omitted`, `countermeasure lacks owner`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/incident_timeline_correlator.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/incident_timeline_correlator.py`.
