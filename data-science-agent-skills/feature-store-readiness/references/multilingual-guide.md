# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `feature-store-readiness`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$feature-store-readiness` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 5: Ops & Storytelling | **Feature Store Readiness** | Audit online-offline feature parity, point-in-time joins, and serving TTL freshness | `"Check offline training and online serving feature extracts for entity-level parity and skew."` |
| **简体中文** | 阶段 5：生产交付、监控与叙事 | **特征平台就绪度与在线离线一致性** | 审计离线训练与在线服务特征的逐实体一致性（Train-Serve Skew）、时间点关联与 TTL 时效 | `"比对离线训练特征与在线服务特征抽样表，排查训练-服务不一致性（Skew）与时效滞后。"` |
| **日本語** | ステージ 5：本番運用・監視・意思決定伝達 | **特徴量ストア準備度＆オンライン／オフライン整合性** | 学習用バッチ特徴量と推論用オンライン特徴量の一致性（Train-Serve Skew）・時点結合・TTLを監査 | `"オフライン学習用とオンライン推論用の特徴量CSVを突合し、エンティティ単位のスキューを検査してください。"` |
| **한국어** | 5단계: 프로덕션 운영 및 인사이트 전달 | **피처 스토어 준비도 및 온라인·오프라인 정합성** | 오프라인 학습 피처와 온라인 서빙 피처 간 정합성(Train-Serve Skew), 시점 정합 조인, TTL을 감사 | `"오프라인 학습 피처와 온라인 서빙 피처 추출본을 비교해 엔티티 단위 스큐(Skew)를 점검해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Batch training SQL and real-time serving code compute the same feature differently, causing silent training-serving skew.
- **简体中文**: 离线批处理 SQL 与线上实时服务代码对同一特征的计算口径或窗口存在细微差异，造成隐蔽的线上预测偏移。
- **日本語**: オフラインSQLとオンライン推論コードで特徴量の計算ロジックが微妙に異なり、本番推論時に精度が劣化する。
- **한국어**: 배치 학습 SQL과 실시간 서빙 코드의 피처 계산 로직이 미묘하게 달라 운영 환경에서 조용한 예측 왜곡이 발생함.

Inspected red flags across all locales: `same feature computed differently online`, `freshness unknown`, `no point-in-time join`, `feature owner unclear`, `feature store proposed without reuse`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/online_offline_skew_check.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/online_offline_skew_check.py`.
