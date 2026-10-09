# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `oss-ds-supply-chain-auditor`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$oss-ds-supply-chain-auditor` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 3: Repro & Pipelines | **OSS DS Supply Chain Auditor** | Audit Python/DS dependency manifests for unpinned packages, URL installs, and pickle risks | `"Audit our requirements.txt, pyproject.toml, and notebooks for supply-chain and serialization risks."` |
| **简体中文** | 阶段 3：可复现性与工程管道 | **开源数据科学供应链审计** | 审计 Python 与数据科学依赖清单中的未锁定版本、裸 URL 安装及不安全反序列化风险 | `"审计项目中的依赖清单与 Notebook，排查未锁定依赖、裸 URL 引用及不安全模型加载风险。"` |
| **日本語** | ステージ 3：再現性・パイプライン化 | **OSSデータサイエンス・サプライチェーン監査** | 依存定義ファイルの未固定バージョン・直接URL参照・危険なpickle読み込みを監査 | `"requirements.txtやpyproject.toml、Notebookの依存関係とモデル読み込みのサプライチェーンリスクを監査してください。"` |
| **한국어** | 3단계: 재현성 및 파이프라인 엔지니어링 | **오픈소스 DS 공급망 감사기** | Python·DS 의존성 매니페스트의 버전 미고정, 직접 URL 설치, 안전하지 않은 피클(Pickle) 로드를 감사 | `"requirements.txt, pyproject.toml, 노트북의 의존성 버전 고정 여부와 공급망 보안 리스크를 감사해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Unpinned requirements, direct GitHub URLs, and untrusted pickle/checkpoint loads expose ML pipelines to breakage and RCE.
- **简体中文**: 未锁定依赖版本、直接从 Git URL 安装包或加载不可信的 pickle 模型权重，极易引发线上构建崩溃与远程代码执行。
- **日本語**: バージョン未固定のパッケージやGit URL直指定、信頼できないpickleファイルの読み込みが環境破損や脆弱性を招く。
- **한국어**: 버전이 고정되지 않은 패키지, 직접 Git URL 설치, 신뢰할 수 없는 체크포인트 로드로 인해 빌드 깨짐과 보안 취약점이 발생함.

Inspected red flags across all locales: `pip install from unpinned URL`, `unknown model weights`, `dataset license absent`, `notebook output leaks secrets`, `native binary dependency unreviewed`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/dependency_surface.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/dependency_surface.py`.
