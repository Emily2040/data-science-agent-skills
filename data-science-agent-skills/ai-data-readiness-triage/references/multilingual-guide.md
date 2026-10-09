# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `ai-data-readiness-triage`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$ai-data-readiness-triage` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 1: Framing & Triage | **AI Data Readiness Triage** | Score whether datasets are ready for AI, analytics, or modeling | `"Triage whether our tables and labels are ready for AI modeling before we commit engineering budget."` |
| **简体中文** | 阶段 1：问题界定与数据初筛 | **AI 数据就绪度评估** | 在投入研发预算前评估数据集是否具备 AI、分析或建模条件 | `"在立项建模前，评估这批数据表的质量、标签覆盖率与合规就绪度。"` |
| **日本語** | ステージ 1：課題定義・データ診断 | **AIデータ準備度トリアージ** | AI・分析・モデリング着手前にデータの利用可能性と品質を判定 | `"モデリングに着手する前に、このデータセットの品質・ラベル・ガバナンス準備度を評価してください。"` |
| **한국어** | 1단계: 문제 정의 및 데이터 트리아지 | **AI 데이터 준비도 트리아지** | 예산과 엔지니어링 투입 전 AI·분석·모델링용 데이터 준비 상태 진단 | `"모델링 예산을 투입하기 전에 이 데이터셋의 품질, 라벨 커버리지, 거버넌스 준비도를 점검해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: AI projects stall mid-flight because missing labels, stale tables, PII exposure, and unknown ownership surface too late.
- **简体中文**: 项目启动后才发现数据权属不清、标签缺失、核心字段高缺失率、更新时效滞后或存在 PII 合规隐患。
- **日本語**: 開発予算を投じた後になって、データオーナー不明・教師ラベル不足・欠損過多・PIIリスク・鮮度不足が発覚する。
- **한국어**: 프로젝트 착수 후에야 데이터 오너 불명, 라벨 부재, 핵심 컬럼 결측, 갱신 주기 불일치, 개인정보(PII) 리스크가 드러남.

Inspected red flags across all locales: `unknown owner`, `no label source`, `PII without approved use`, `high missingness in core fields`, `freshness mismatched to decision cycle`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/profile_table.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/profile_table.py`.
