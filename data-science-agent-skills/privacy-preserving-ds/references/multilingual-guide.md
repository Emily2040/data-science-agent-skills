# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `privacy-preserving-ds`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$privacy-preserving-ds` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 4: Eval & Governance | **Privacy Preserving DS** | Audit direct PII, quasi-identifiers, k-anonymity risks, and retention boundaries | `"Audit this dataset and analytics workflow for PII exposure and quasi-identifier re-identification risk."` |
| **简体中文** | 阶段 4：评估、治理与专家协同 | **隐私保护数据科学审计** | 审计直接个人身份信息（PII）、准标识符重识别风险、最小化原则与数据留存边界 | `"对数据集开展隐私合规审计，排查直接 PII 字段、准标识符重识别风险与脱敏策略。"` |
| **日本語** | ステージ 4：評価・ガバナンス・SME協働 | **プライバシー保護データサイエンス** | 直接PII・準識別子による再識別リスク・データ最小化・保持期限ルールを監査 | `"このデータセットの直接PIIと準識別子による再識別リスクを監査し、匿名化・最小化対策を設計してください。"` |
| **한국어** | 4단계: 평가, 거버넌스 및 전문가 루프 | **프라이버시 보호 데이터 사이언스** | 직접 개인정보(PII), 준식별자(Quasi-identifier) 재식별 위험, 최소 수집 및 보존 기한을 감사 | `"이 데이터셋과 분석 파이프라인에서 직접 PII 노출과 준식별자 재식별 리스크를 감사해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Removing names or emails while keeping narrow zip-age-timestamp combinations leaves records re-identifiable.
- **简体中文**: 仅删去姓名与手机号，却保留了高精度的地理位置、时间戳与稀有属性组合，导致用户仍可被轻易重识别。
- **日本語**: 氏名やメールを削除しただけで、郵便番号・年齢・タイムスタンプの組み合わせから個人が再識別されるリスクが残る。
- **한국어**: 이름·이메일만 제거하고 우편번호·연령·타임스탬프 조합을 그대로 두어 개인 재식별 위험이 남음.

Inspected red flags across all locales: `raw PII in notebook output`, `unapproved cloud copy`, `identifier kept for convenience`, `synthetic data claimed risk-free`, `exports not reviewed`.

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
