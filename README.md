# TargetLens

**面向蛋白靶点的小分子药物发现与设计 Agent**

TargetLens 是一个与毕业论文对应的开源研究原型，目标是协同完成靶点分析、候选分子发现、结构评估与分子优化，并以文献和计算证据支撑设计决策。

本仓库的 `0.1.0` 版本先冻结公开的领域契约和可复现工作流边界。它不是已经完成的药物设计平台，也不声称已经接通通用 DTI、AlphaFold、docking 或分子生成模型。

## 当前状态

当前已实现：

- `Target`、`Molecule`、`Evidence`、`AnalysisRun`、`CandidateDecision` 领域对象；
- 对结构来源、证据类型、工具版本、输入哈希和候选决策的显式记录；
- 不依赖外部服务的离线任务规划器；
- 最小公开示例和契约测试。

当前未实现：

- LLM 或多 Agent 运行时；
- ESM 推理服务；
- AlphaFold 结构检索／预测；
- 分子对接、分子动力学和真实虚拟筛选；
- 受约束分子优化；
- 生产级 API、前端和数据库。

## 与既有资产的关系

植物和类黄酮数据、ESM 类黄酮生物合成酶分类器、AlphaFold 结构和现有文献证据能力可以作为后续案例或适配器，但不定义 TargetLens 的产品范围。

- ESM 分类器只能用于其已经定义和验证的特定酶分类任务，不能写成通用蛋白靶点识别、DTI 或小分子活性模型。
- AlphaFold 结构是预测结构；docking 输出是结构计算证据。二者都不能单独证明真实结合、药效、安全性或临床价值。
- 文献检索、关系探索和网络／通路分析作为证据与机制上下文能力迁移，不等于靶点验证或疗效证明。

## 快速开始

需要 Python 3.11 或更高版本。仓库核心代码不依赖外部服务。

```powershell
python scripts/validate_example.py
python -m pytest -q
```

预期输出包含：

```text
TargetLens example is valid
normalize_target -> collect_target_evidence -> standardize_candidates -> evaluate_structure_compatibility -> review_literature_and_computational_evidence -> write_decision_record
```

## 研究路线

详见 [`docs/ROADMAP.md`](docs/ROADMAP.md)、[`docs/OPEN_SOURCE_SCOPE.md`](docs/OPEN_SOURCE_SCOPE.md) 和上级项目中的 TargetLens 规划文档。

推荐的后续顺序是：资产与许可证审计、固定首个靶点任务、打通候选与结构评估基线、接入受约束优化方法、最后再让模型根据真实工具结果驱动 Agent 闭环。

## 免责声明

TargetLens 仅用于软件工程、计算生物学和药物发现研究，不提供诊断、处方、治疗或临床决策。任何计算结果都需要合适的人工审查和实验验证。

## 许可证

代码暂按 MIT License 发布。数据、模型权重、第三方工具和外部数据库可能适用不同许可证，不能因为代码采用 MIT 就推断这些资产可自由再分发。

