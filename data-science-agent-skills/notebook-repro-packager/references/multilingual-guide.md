# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `notebook-repro-packager`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$notebook-repro-packager` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 3: Repro & Pipelines | **Notebook Repro Packager** | Audit Jupyter notebooks for out-of-order cells, unseeded RNG, hardcoded paths, and lockfiles | `"Audit this Jupyter notebook for reproducibility hazards and package it for a clean top-to-bottom run."` |
| **简体中文** | 阶段 3：可复现性与工程管道 | **Notebook 可复现性打包器** | 审计 Jupyter Notebook 的乱序执行、未固定随机种子、硬编码绝对路径与依赖锁定 | `"审计这份 Notebook 的乱序执行、随机种子与硬编码路径隐患，并生成可复现打包清单。"` |
| **日本語** | ステージ 3：再現性・パイプライン化 | **Notebook再現性パッケージャー** | Jupyter Notebookのセル実行順序の乱れ・未固定シード・絶対パス・依存ロック漏れを監査 | `"このNotebookの実行順序・乱数シード・ハードコードされたパスを監査し、再現可能な形にパッケージ化してください。"` |
| **한국어** | 3단계: 재현성 및 파이프라인 엔지니어링 | **노트북 재현성 패키저** | Jupyter 노트북의 셀 역순 실행, 미고정 난수 시드, 절대 경로, 의존성 잠금 누락을 감사 | `"이 Jupyter 노트북의 역순 실행, 난수 시드 누락, 절대 경로 문제를 감사하고 재현 가능하게 패키징해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Notebooks that 'worked on my machine' fail on clean reruns due to hidden cell state, missing seeds, and local paths.
- **简体中文**: Notebook 依赖跨单元格隐式内存状态、本地硬编码路径或未锁定的包版本，换机重跑即报错或结果漂移。
- **日本語**: 手元では動いたNotebookが、セルの順不同実行や固定されていない乱数シード、ローカル絶対パスのせいで再実行できない。
- **한국어**: 숨겨진 셀 상태나 하드코딩된 로컬 경로, 고정되지 않은 시드 때문에 클린 환경에서 처음부터 다시 실행하면 실패함.

Inspected red flags across all locales: `out-of-order execution`, `local absolute paths`, `unseeded randomness`, `implicit data downloads`, `manual cell edits required`.

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
