# TargetLens

**面向蛋白靶点的小分子药物发现与设计 Agent**

TargetLens 目标是协同完成靶点分析、候选分子发现、结构评估与分子优化，并以文献和计算证据支撑设计决策。


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

