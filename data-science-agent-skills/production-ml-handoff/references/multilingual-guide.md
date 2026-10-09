# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `production-ml-handoff`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$production-ml-handoff` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 5: Ops & Storytelling | **Production ML Handoff** | Verify model SHA-256, input/output contracts, p99 latency SLA, fallback, and rollback readiness | `"Run a production ML handoff audit on this model spec before platform engineering accepts deployment."` |
| **简体中文** | 阶段 5：生产交付、监控与叙事 | **机器学习生产交付门禁** | 核验模型制品 SHA-256、输入输出契约、p99 延迟 SLA、降级基线与自动回滚触发器 | `"在工程团队接手上线前，对该模型执行生产交付门禁审计，核验延迟 SLA 与回滚预案。"` |
| **日本語** | ステージ 5：本番運用・監視・意思決定伝達 | **本番MLハンドオフ（運用引き継ぎ監査）** | モデルSHA-256・入出力スキーマ・p99レイテンシSLA・フォールバック・ロールバック条件を検証 | `"MLエンジニアリングチームへの引き継ぎ前に、このモデルの本番ハンドオフ準備度を監査してください。"` |
| **한국어** | 5단계: 프로덕션 운영 및 인사이트 전달 | **프로덕션 ML 핸드오프** | 모델 SHA-256 해시, 입출력 스키마, p99 지연시간 SLA, 폴백 베이스라인, 롤백 트리거를 검증 | `"플랫폼 엔지니어링 팀에 배포를 이관하기 전에 이 모델의 프로덕션 핸드오프 준비 상태를 감사해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Data scientists hand over a notebook and weights file without input validation, latency profiling, or a rollback trigger.
- **简体中文**: 算法团队仅移交一份模型权重与 Notebook，缺乏输入字段校验、p99 延迟压测、兜底策略与故障回滚阈值。
- **日本語**: 学習済み重みとNotebookだけが渡され、入力バリデーションやp99レイテンシ検証、ロールバック条件がないまま本番化される。
- **한국어**: 입출력 스키마 검증, p99 지연시간 측정, 장애 시 폴백·롤백 기준 없이 모델 가중치와 노트북만 운영팀에 넘김.

Inspected red flags across all locales: `notebook is only artifact`, `feature definitions ambiguous`, `no rollback plan`, `latency unknown`, `owner unclear after launch`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/handoff_readiness_audit.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/handoff_readiness_audit.py`.
