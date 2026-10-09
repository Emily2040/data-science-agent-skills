# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `model-risk-compliance-memo`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$model-risk-compliance-memo` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 4: Eval & Governance | **Model Risk Compliance Memo** | Document blast radius, human-in-the-loop override, fallback policy, and governance gates | `"Draft a model risk and compliance gate memo with blast-radius classification and rollback controls."` |
| **简体中文** | 阶段 4：评估、治理与专家协同 | **模型风险与合规备忘录** | 界定模型爆炸半径、人工复核兜底机制、回滚责任人与合规上线门禁 | `"针对该模型编写风险分级与合规门禁备忘录，核查人工复核机制与回滚预案。"` |
| **日本語** | ステージ 4：評価・ガバナンス・SME協働 | **モデルリスク・コンプライアンスメモ** | 影響範囲（ブラスト半径）・人間による介入（HITL）・フォールバック・ロールバック責任者を審査 | `"このモデルのリスク階層ゲートを審査し、影響範囲・人間によるオーバーライド・ロールバック体制を文書化してください。"` |
| **한국어** | 4단계: 평가, 거버넌스 및 전문가 루프 | **모델 리스크 및 컴플라이언스 메모** | 모델 영향 범위(Blast Radius), 인간 개입(HITL) 통제, 폴백 정책, 롤백 책임자를 검증 및 문서화 | `"이 모델의 리스크 등급 게이트를 점검하고 영향 범위, 수동 오버라이드, 롤백 통제 계획을 작성해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: High-impact models reach launch review without documented failure modes, appeal paths, or rollback owners.
- **简体中文**: 高影响面的自动化决策模型在缺乏失败降级策略、人工接管通道与明确回滚责任人的情况下仓促上线。
- **日本語**: 高リスクな自動判定モデルが、失敗時の縮退運転ルールや異議申し立て経路、ロールバック責任者なしにリリースされる。
- **한국어**: 고위험 자동 의사결정 모델이 장애 시 폴백 기준, 수동 제어권, 롤백 책임자 없이 배포 심사에 올라옴.

Inspected red flags across all locales: `affected users undefined`, `no rollback owner`, `fairness not evaluated where relevant`, `privacy basis unclear`, `monitoring absent`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/risk_tier_gate.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/risk_tier_gate.py`.
