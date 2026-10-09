# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `notebook-to-pipeline-surgeon`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$notebook-to-pipeline-surgeon` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 3: Repro & Pipelines | **Notebook To Pipeline Surgeon** | Refactor exploratory notebooks into modular, testable, idempotent pipeline stages | `"Refactor this exploratory notebook into modular, idempotent pipeline stages with unit tests."` |
| **简体中文** | 阶段 3：可复现性与工程管道 | **Notebook 转生产管道重构师** | 将探索性 Notebook 拆解重构为模块化、幂等、可单测的生产数据与训练管道 | `"将这份探索性 Notebook 重构为职责清晰、幂等且带契约测试的生产流水线模块。"` |
| **日本語** | ステージ 3：再現性・パイプライン化 | **Notebook・トゥ・パイプライン・サージョン** | 探索的Notebookをモジュール化・べき等・テスト可能な本番パイプラインへ外科的に再構築 | `"この探索的Notebookを、べき等性と単体テストを備えたモジュール型パイプラインへ設計し直してください。"` |
| **한국어** | 3단계: 재현성 및 파이프라인 엔지니어링 | **노트북-파이프라인 리팩터링 서전** | 탐색적 노트북을 모듈화·멱등성·단위 테스트를 갖춘 프로덕션 파이프라인으로 전환 | `"이 탐색적 노트북을 멱등성과 계약 테스트를 갖춘 모듈형 프로덕션 파이프라인으로 리팩터링해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Scheduling raw exploratory notebooks in production causes brittle failures, untestable side effects, and silent overwrites.
- **简体中文**: 直接把包含探索性图表、硬编码配置与副作用的整本 Notebook 挂上生产调度，导致故障频发且无法回滚。
- **日本語**: 探索用Notebookをそのまま定期バッチに乗せることで、副作用や途中失敗時のデータ破損、テスト不能な負債が生じる。
- **한국어**: 탐색용 노트북을 그대로 운영 스케줄러에 올려 부작용, 부분 실패 시 데이터 오염, 테스트 불가능한 기술 부채가 발생함.

Inspected red flags across all locales: `global mutable state`, `manual cell ordering`, `plot-only outputs used downstream`, `external calls in transform functions`, `orchestrator added without need`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/notebook_repro_audit.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/notebook_repro_audit.py`.
