# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `missingness-mechanism-investigator`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$missingness-mechanism-investigator` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 2: Validity & Leakage | **Missingness Mechanism Investigator** | Diagnose MCAR, MAR, and MNAR missingness and block naive imputation traps | `"Diagnose whether missing values in our core features are MCAR, MAR, or MNAR before imputing."` |
| **简体中文** | 阶段 2：有效性验证与防泄漏 | **缺失机制诊断（MCAR / MAR / MNAR）** | 诊断完全随机、随机与非随机缺失机制，防范盲目均值插补或删行偏倚 | `"在插补缺失值之前，诊断核心特征属于 MCAR、MAR 还是 MNAR，并给出稳健处理方案。"` |
| **日本語** | ステージ 2：妥当性・リーク検証 | **欠測メカニズム調査（MCAR / MAR / MNAR）** | 欠測がMCAR・MAR・MNARのいずれかを診断し、安易な平均値補完や行削除によるバイアスを防止 | `"欠損値補完を行う前に、主要カラムの欠測メカニズム（MCAR/MAR/MNAR）を診断してください。"` |
| **한국어** | 2단계: 타당성 및 누수 검증 | **결측 메커니즘 조사기 (MCAR / MAR / MNAR)** | 결측치의 MCAR·MAR·MNAR 메커니즘을 진단하고 단순 평균 대체·행 삭제 편향을 방지 | `"결측치를 대체하기 전에 핵심 변수의 결측 메커니즘이 MCAR, MAR, MNAR 중 무엇인지 진단해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Mean-imputing or dropping missing rows when absence itself carries clinical, financial, or behavioral signal biases the model.
- **简体中文**: 当字段缺失本身隐含业务或风险信号（MNAR）时，简单删行或均值填充会引入严重选择偏倚。
- **日本語**: 欠測そのものに業務上の意味（MNAR）があるにもかかわらず、単純な行削除や平均値補完を行ってモデルを歪める。
- **한국어**: 결측 자체에 비즈니스·행동 신호(MNAR)가 담겨 있는데도 단순 평균 대체나 행 삭제를 수행해 모델을 왜곡함.

Inspected red flags across all locales: `target-dependent missingness`, `structural missing treated as random`, `imputed identifiers`, `dropped rows change population`, `no collection-process explanation`.

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
