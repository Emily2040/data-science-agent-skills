# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `metric-design-review-board`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$metric-design-review-board` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 4: Eval & Governance | **Metric Design Review Board** | Stress-test primary metrics, denominators, time windows, and anti-gaming guardrails | `"Run a metric design review on our primary KPI and propose anti-gaming guardrail metrics."` |
| **简体中文** | 阶段 4：评估、治理与专家协同 | **指标设计评审委员会** | 对核心北极星指标的分母口径、时间窗口、护栏指标与古德哈特（Goodhart）作弊路径开展压力测试 | `"评审这套实验与业务指标体系，核查分母漂移风险、时间窗口与反作弊护栏指标。"` |
| **日本語** | ステージ 4：評価・ガバナンス・SME協働 | **指標設計レビューボード** | 主要KPIの分母定義・集計期間・ガードレール指標・Goodhartの法則によるハック耐性を審査 | `"主要KPIとガードレール指標の設計を審査し、指標ハック（ゲーミング）の抜け道を洗い出してください。"` |
| **한국어** | 4단계: 평가, 거버넌스 및 전문가 루프 | **지표 설계 리뷰 보드** | 핵심 KPI의 분모 정의, 집계 윈도우, 가드레일 지표, 굿하트 법칙(게이밍) 취약점을 심사 | `"핵심 성과지표(KPI)의 분모·윈도우 정의를 검토하고 지표 게이밍을 막을 가드레일 지표를 설계해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Optimizing a single ratio or click metric without guardrails invites Goodhart's law gaming and harms user experience.
- **简体中文**: 单一比例指标或点击率指标缺乏护栏约束，导致算法或业务通过改变分母、牺牲长效留存来刷高短期指标。
- **日本語**: ガードレール指標なしに単一の比率や短期指標を最適化し、分母の歪みやユーザー体験の悪化を招く。
- **한국어**: 가드레일 없이 단일 비율이나 단기 클릭 지표만 최적화하다가 분모 왜곡과 장기 사용자 경험 훼손을 초래함.

Inspected red flags across all locales: `metric not tied to action`, `proxy metric can be gamed`, `threshold chosen after results`, `guardrails missing`, `average hides subgroup harm`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/metric_guardrail_check.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/metric_guardrail_check.py`.
