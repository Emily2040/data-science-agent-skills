# 数据科学智能体技能库 (Data Science Agent Skills)

**Language / 语言 / 言語 / 언어**: [English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

![数据科学智能体技能库主图](assets/repo-hero.png)

![数据科学全生命周期工作流](assets/repo-workflow-hero.png)

一套面向生产实践的 **25 项高判断力数据科学与机器学习工程 Agent 技能库（Skill Catalog）**。每个技能均内置**零第三方依赖的 Python 标准库确定性核验脚本**、**八段式结构化决策契约**，并原生支持**英文（English）、简体中文、日文（日本語）与韩文（한국어）**四语种专业语境执行。

所有技能统一输出八段式审计备忘录（`Problem / 问题定义`、`Inputs / 输入与数据契约`、`Checks performed / 已执行的确定性检查`、`Findings / 关键发现与证据`、`Decision / 决策结论`、`Risks / 风险与阻塞项`、`Next actions / 下一步行动`、`Artifacts / 交付物与产物`），并强制给出五态枚举结论之一：`go`（通过）、`fix-first`（先修复再推进）、`stop`（终止/拦截）、`proceed-with-risk`（带风险放行）或 `needs-owner-review`（需责任人裁决）。

---

## 按数据科学全生命周期查找技能

![25项技能全生命周期图谱](assets/repo-skill-map-infographic.png)

| 生命周期阶段 | 技能包 (`slug`) | 核心审计职责与防范痛点 | 确定性核验脚本 |
| --- | --- | --- | --- |
| 阶段 1：问题界定与数据初筛 | [数据问题界定与拆解 (`data-question-framing`)](data-science-agent-skills/data-question-framing/) | 将模糊的业务或科研诉求转化为可量化的数据科学问题定义 | `scripts/decision_canvas_validator.py` |
| 阶段 1：问题界定与数据初筛 | [AI 数据就绪度评估 (`ai-data-readiness-triage`)](data-science-agent-skills/ai-data-readiness-triage/) | 在投入研发预算前评估数据集是否具备 AI、分析或建模条件 | `scripts/profile_table.py` |
| 阶段 1：问题界定与数据初筛 | [数据契约取证与核验 (`dataset-contract-forensics`)](data-science-agent-skills/dataset-contract-forensics/) | 逆向推导并校验表结构、主键粒度、唯一性、时效与空值契约 | `scripts/profile_table.py` |
| 阶段 1：问题界定与数据初筛 | [语义血缘与口径映射 (`semantic-lineage-mapper`)](data-science-agent-skills/semantic-lineage-mapper/) | 跨 SQL、Notebook 与数据管道追踪表、字段与指标的真实语义口径 | `scripts/extract_lineage_tokens.py` |
| 阶段 1：问题界定与数据初筛 | [脏数据净室治理 (`messy-data-cleanroom`)](data-science-agent-skills/messy-data-cleanroom/) | 在不篡改原始数据的前提下设计可逆、可审计的清洗与隔离规则 | `scripts/profile_table.py` |
| 阶段 2：有效性验证与防泄漏 | [数据泄漏红队审计 (`leakage-adversary`)](data-science-agent-skills/leakage-adversary/) | 对机器学习数据集与特征管道开展标签泄漏、时间穿越与实体重叠红队排查 | `scripts/split_leakage_probe.py` |
| 阶段 2：有效性验证与防泄漏 | [因果假设与识别侦察 (`causal-assumption-scout`)](data-science-agent-skills/causal-assumption-scout/) | 审查因果推断诉求中的混杂偏倚、对撞因子、干预后控制变量与可识别性假设 | `scripts/confounder_backdoor_check.py` |
| 阶段 2：有效性验证与防泄漏 | [小样本统计功效与容量规划 (`small-data-power-planner`)](data-science-agent-skills/small-data-power-planner/) | 计算最小可检测效应（MDE）、统计功效与小样本过拟合边界 | `scripts/power_sample_size.py` |
| 阶段 2：有效性验证与防泄漏 | [缺失机制诊断（MCAR / MAR / MNAR） (`missingness-mechanism-investigator`)](data-science-agent-skills/missingness-mechanism-investigator/) | 诊断完全随机、随机与非随机缺失机制，防范盲目均值插补或删行偏倚 | `scripts/profile_table.py` |
| 阶段 2：有效性验证与防泄漏 | [基线对标与消融实验室 (`baseline-ablation-lab`)](data-science-agent-skills/baseline-ablation-lab/) | 在接纳复杂模型前强制开展简单基线对标、多随机种子复现与特征消融实验 | `scripts/ablation_delta_audit.py` |
| 阶段 3：可复现性与工程管道 | [Notebook 可复现性打包器 (`notebook-repro-packager`)](data-science-agent-skills/notebook-repro-packager/) | 审计 Jupyter Notebook 的乱序执行、未固定随机种子、硬编码绝对路径与依赖锁定 | `scripts/notebook_repro_audit.py` |
| 阶段 3：可复现性与工程管道 | [Notebook 转生产管道重构师 (`notebook-to-pipeline-surgeon`)](data-science-agent-skills/notebook-to-pipeline-surgeon/) | 将探索性 Notebook 拆解重构为模块化、幂等、可单测的生产数据与训练管道 | `scripts/notebook_repro_audit.py` |
| 阶段 3：可复现性与工程管道 | [实验血缘与溯源账本 (`experiment-provenance-ledger`)](data-science-agent-skills/experiment-provenance-ledger/) | 记录每次实验的数据集 SHA-256 摘要、Git 提交状态、脏工作区标记、随机种子与超参 | `scripts/capture_provenance.py` |
| 阶段 3：可复现性与工程管道 | [开源数据科学供应链审计 (`oss-ds-supply-chain-auditor`)](data-science-agent-skills/oss-ds-supply-chain-auditor/) | 审计 Python 与数据科学依赖清单中的未锁定版本、裸 URL 安装及不安全反序列化风险 | `scripts/dependency_surface.py` |
| 阶段 3：可复现性与工程管道 | [成本感知算力规划师 (`cost-aware-compute-planner`)](data-science-agent-skills/cost-aware-compute-planner/) | 测算含重试期望的 GPU/云算力成本，并在全量训练前强制执行 10% 小样本先导门禁 | `scripts/compute_budget_estimator.py` |
| 阶段 4：评估、治理与专家协同 | [指标设计评审委员会 (`metric-design-review-board`)](data-science-agent-skills/metric-design-review-board/) | 对核心北极星指标的分母口径、时间窗口、护栏指标与古德哈特（Goodhart）作弊路径开展压力测试 | `scripts/metric_guardrail_check.py` |
| 阶段 4：评估、治理与专家协同 | [模型评估真实性核查 (`evaluation-reality-check`)](data-science-agent-skills/evaluation-reality-check/) | 审计分群切片误差（Slice Error）、概率校准度（Brier）与离线指标到业务收益的映射 | `scripts/slice_error_auditor.py` |
| 阶段 4：评估、治理与专家协同 | [模型风险与合规备忘录 (`model-risk-compliance-memo`)](data-science-agent-skills/model-risk-compliance-memo/) | 界定模型爆炸半径、人工复核兜底机制、回滚责任人与合规上线门禁 | `scripts/risk_tier_gate.py` |
| 阶段 4：评估、治理与专家协同 | [隐私保护数据科学审计 (`privacy-preserving-ds`)](data-science-agent-skills/privacy-preserving-ds/) | 审计直接个人身份信息（PII）、准标识符重识别风险、最小化原则与数据留存边界 | `scripts/profile_table.py` |
| 阶段 4：评估、治理与专家协同 | [领域专家协同与标注仲裁环 (`domain-expert-collaboration-loop`)](data-science-agent-skills/domain-expert-collaboration-loop/) | 量化领域专家标注一致性（Cohen's Kappa），制定边界样本仲裁准则与标签口径说明 | `scripts/sme_label_agreement.py` |
| 阶段 5：生产交付、监控与叙事 | [机器学习生产交付门禁 (`production-ml-handoff`)](data-science-agent-skills/production-ml-handoff/) | 核验模型制品 SHA-256、输入输出契约、p99 延迟 SLA、降级基线与自动回滚触发器 | `scripts/handoff_readiness_audit.py` |
| 阶段 5：生产交付、监控与叙事 | [特征平台就绪度与在线离线一致性 (`feature-store-readiness`)](data-science-agent-skills/feature-store-readiness/) | 审计离线训练与在线服务特征的逐实体一致性（Train-Serve Skew）、时间点关联与 TTL 时效 | `scripts/online_offline_skew_check.py` |
| 阶段 5：生产交付、监控与叙事 | [数据与概念漂移监控设计 (`drift-monitor-designer`)](data-science-agent-skills/drift-monitor-designer/) | 检测均值偏移、方差暴增、常量列突变、NaN 污染与缺失率飙升，设计分级告警动作 | `scripts/drift_probe.py` |
| 阶段 5：生产交付、监控与叙事 | [数据科学事故根因分析（RCA） (`data-science-incident-rca`)](data-science-agent-skills/data-science-incident-rca/) | 跨数据接入、表结构、特征计算、模型版本与指标口径五层关联时间线，定位线上异常根因 | `scripts/incident_timeline_correlator.py` |
| 阶段 5：生产交付、监控与叙事 | [业务干系人洞察叙事与决策备忘录 (`stakeholder-insight-storyteller`)](data-science-agent-skills/stakeholder-insight-storyteller/) | 将经核验的技术证据转化为结论先行、含置信区间与前提边界的高管决策备忘录 | `scripts/memo_claim_evidence_check.py` |

---

## 快速上手：全量校验、四语种检索与扁平化安装

所有核验脚本与契约测试均仅使用 Python 3 标准库编写，无需安装任何第三方依赖即可直接运行：

```bash
# 对全部 25 个技能执行严格契约校验与脚本行为冒烟测试
python scripts/catalog_cli.py validate

# 按简体中文、英文、日文或韩文列出技能目录
python scripts/catalog_cli.py list --lang zh-CN
python scripts/catalog_cli.py list --lang en
python scripts/catalog_cli.py list --lang ja
python scripts/catalog_cli.py list --lang ko

# 将 25 个技能扁平化安装至各大 Agent 的单层技能发现目录
python scripts/catalog_cli.py install --target ~/.codex/skills
python scripts/catalog_cli.py install --target ~/.claude/skills
python scripts/catalog_cli.py install --target ~/.gemini/config/skills

# 运行端到端多技能串联与边界回归测试套件
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 跨智能体运行时与数据平台互操作性

![跨平台与运行时兼容性](assets/repo-provider-compatibility.png)

- **支持 18 种主流 Agent 运行时**：OpenAI Codex、ChatGPT Agents、Anthropic Claude、Claude Code、Google Gemini、Gravity / Antigravity、GitHub Copilot、Cursor、Windsurf、Goose、OpenCode、OpenHands、LangGraph、CrewAI、AutoGen、LlamaIndex、Semantic Kernel 及本地大模型智能体。
- **原生四语种专业术语支持**：每个技能均配备 `references/multilingual-guide.md`，拒绝生硬机翻，提供地道的中文、英文、日文、韩文数据科学与 MLOps 专业术语及双语契约表头。
