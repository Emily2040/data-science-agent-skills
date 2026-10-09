# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `messy-data-cleanroom`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$messy-data-cleanroom` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 1: Framing & Triage | **Messy Data Cleanroom** | Design reversible, auditable cleaning and quarantine rules without mutating raw data | `"Design a reversible cleanroom pipeline with quarantine tables and row-count reconciliation."` |
| **简体中文** | 阶段 1：问题界定与数据初筛 | **脏数据净室治理** | 在不篡改原始数据的前提下设计可逆、可审计的清洗与隔离规则 | `"为这批脏数据设计可逆的净室清洗规则、异常隔离表与行数勾稽校验。"` |
| **日本語** | ステージ 1：課題定義・データ診断 | **メッシーデータ・クリーンルーム** | 生データを破壊せず、可逆かつ監査可能なクレンジング・隔離ルールを設計 | `"生データを保持したまま、隔離テーブルと件数突合を備えた可逆なクレンジング手順を設計してください。"` |
| **한국어** | 1단계: 문제 정의 및 데이터 트리아지 | **메시 데이터 클린룸** | 원본 데이터를 훼손하지 않고 가역적·감사가능한 정제 및 격리(Quarantine) 규칙 설계 | `"원본 데이터를 보존하면서 격리 테이블과 행 수 대사(Reconciliation)를 포함한 정제 파이프라인을 설계해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Ad-hoc notebook drops and silent coercions erase edge-case signals and make data cleaning impossible to reproduce.
- **简体中文**: 脚本中随手丢弃异常行或静默强制转型，抹杀了关键边缘信号并导致清洗过程无法复现。
- **日本語**: 場当たり的なレコード削除や暗黙の型変換により、重要な異常シグナルが消え、前処理の再現性が失われる。
- **한국어**: 임의의 행 삭제나 암묵적 형변환으로 인해 중요한 이상 징후가 사라지고 전처리 재현성이 깨짐.

Inspected red flags across all locales: `overwriting raw data`, `dropping rows without impact analysis`, `unit conversion not documented`, `outlier removal tied to desired result`.

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
