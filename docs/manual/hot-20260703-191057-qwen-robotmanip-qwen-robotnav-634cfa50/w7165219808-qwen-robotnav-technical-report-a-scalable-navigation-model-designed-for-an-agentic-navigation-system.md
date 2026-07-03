---
title: "Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System"
title_zh: Qwen-RobotNav技术报告：为智能体导航系统设计的可扩展导航模型
authors: "Jiazhao Zhang, Gengze Zhou, Hale Yin, Yiyang Huang, Zixing Lei, Qihang Peng, Haoqi Yuan, Jie Zhang, Xiang Guo, Xiaoyue Chen, An Yang, Fei Huang, J X C Lin, D Liu, Jie Zhou, Zhuoyuan Yu, Jiahao Fan, Zhixuan Liang, Pei Lin, Ye Wang"
date: 2026-06-16
pdf: "https://arxiv.org/pdf/2606.18112"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:alibaba group"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=alibaba group; relation_source=branded-title; query=Qwen-RobotNav"
tldr: 智能体导航系统需要一个基础模型，其观察策略能在推理时由外部重配置，因为指令跟随、物体搜索、目标跟踪、自动驾驶共享感知骨干但需要不同视觉消费策略。Qwen-RobotNav通过参数化接口（多个任务模式+可控观察参数如token预算和相机权重）实现，训练时随机化所有参数确保鲁棒性，无需改骨干架构。在1560万样本上联合视觉语言数据训练防止崩溃为动作序列映射器。该模型在主要导航基准上取得新SOTA，从2B到8B参数扩展良好，零样本泛化到真实世界机器人。
source: openalex
selection_source: hot_paper_scout
motivation: 现有导航模型观察策略固定，无法满足不同任务对视觉流消费策略的差异化需求。
method: 设计参数化接口含任务模式和观察参数，训练时随机化配置，联合视觉语言数据训练避免崩溃。
result: 在主要导航基准上实现新SOTA，模型规模从2B扩展到8B性能提升，零样本泛化真实机器人。
conclusion: Qwen-RobotNav作为可扩展基础模型，支持动态切换任务模式，适用于智能体导航系统。
---

## 摘要
智能体导航系统需要一个基础导航模型，其观察策略可以在推理时从外部重新配置，因为指令跟随、物体搜索、目标跟踪和自动驾驶共享相同的感知-规划主干，却需要根本不同的策略来消费视觉流。我们提出Qwen-RobotNav，这是一个基于Qwen-RobotNav构建的可扩展导航模型，通过一个参数化接口来解决此问题，该接口包含两个互补维度：选择导航行为的多种任务模式，以及控制视觉历史如何编码的可控观察参数（例如，令牌预算、每摄像头权重）。通过在训练时对所有参数进行随机化，Qwen-RobotNav对任何推理时配置都具有鲁棒性，且无需对Qwen-RobotNav主干进行任何架构修改。我们在1560万样本上训练Qwen-RobotNav；与视觉-语言数据联合训练可防止在仅轨迹训练中观察到的退化为反应式动作序列映射器。参数化接口也使Qwen-RobotNav成为智能体系统的自然构建模块：对于长周期场景，上层规划器将目标分解为子任务，并在情节中动态切换Qwen-RobotNav的任务模式和上下文策略，通过对同一模型的重复调用来组合复杂行为。大量实验表明，Qwen-RobotNav在主要导航基准上取得了新的最先进结果。模型从2B到8B参数表现出良好的可扩展性，联合多任务训练发展出一个共享的空间规划基板，该基板可在任务族间转移，并在多种环境下的真实世界机器人上展现出强大的零样本泛化能力。

## Abstract
Agentic navigation systems require a base navigation model whose observation strategy can be externally reconfigured at inference time, because instruction following, object search, target tracking, and autonomous driving share the same perception-planning backbone yet demand fundamentally different strategies for consuming the visual stream. We present Qwen-RobotNav, a scalable navigation model built on Qwen-RobotNav that addresses it through a parameterised interface with two complementary dimensions: multiple task modes that select the navigation behaviour, and controllable observation parameters (e.g., token budget, per-camera weights) that govern how visual history is encoded. With training-time randomization over all parameters, Qwen-RobotNav is robust to any inference-time configuration requiring zero architectural modification to the Qwen-RobotNav backbone. We train Qwen-RobotNav on 15.6M samples; co-training with vision-language data prevents the collapse into reactive action-sequence mappers observed in trajectory-only training. The parameterised interface also makes Qwen-RobotNav a natural building block for agentic systems: for long-horizon scenarios, an upper-level planner decomposes goals into sub-tasks and dynamically switches Qwen-RobotNav's task mode and context strategy mid-episode, composing complex behaviours from repeated calls to the same model. Extensive experiments show that Qwen-RobotNav sets new state-of-the-art results across major navigation benchmarks. The model exhibits favourable scaling from 2B to 8B parameters, with joint multi-task training developing a shared spatial-planning substrate that transfers across task families, and demonstrates strong zero-shot generalisation to real-world robots across diverse environments.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 智能体导航系统需要一个基础导航模型，其视觉观察策略能在推理时由外部重新配置。
- 现有导航模型观察策略固定，无法满足不同任务（指令跟随、物体搜索、目标跟踪、自动驾驶）对视觉流消费策略的差异化需求——这些任务共享感知-规划骨干，但需要完全不同的策略来消费视觉历史。
- 因此，作者提出Qwen-RobotNav，旨在构建一个可扩展、可通过参数化接口动态调整观察策略的基础导航模型。

## 二、论文提出的方法论
- **核心思想**：设计一个参数化接口，包含两个互补维度：
  1. **任务模式**：选择导航行为（如指令跟随、物体搜索等）。
  2. **可控观察参数**：控制视觉历史如何编码（如token预算、每摄像头权重）。
- **关键实现**：
  - 在训练时对所有参数进行随机化，使模型对任意推理时配置具有鲁棒性，无需修改Qwen-RobotNav骨干架构。
  - 训练样本量：1560万样本；联合视觉-语言数据训练，防止仅轨迹训练导致的退化为反应式动作序列映射器。
- **算法流程**：
  - 上层规划器（agentic system）将长周期目标分解为子任务，并在情节中动态切换Qwen-RobotNav的任务模式和上下文策略，通过对同一模型的重复调用来组合复杂行为。
  - 模型基于Qwen-RobotNav（论文中提及多次，疑似为Qwen系列模型的一部分）构建，参数化接口不需要架构修改。

## 三、实验设计
- **数据集/场景**：使用了主要导航基准（如Habitat等常见仿真环境），以及真实世界机器人环境。
- **Benchmark**：在多个主流导航基准上评测，包括指令跟随、物体搜索等任务。
- **对比方法**：与现有SOTA导航模型对比（未列出具体方法名称，但声称取得新SOTA）。
- **零样本泛化**：在真实世界机器人多样化环境中测试。

## 四、资源与算力
- 论文未明确说明使用的GPU型号、数量、训练时长等具体算力信息。

## 五、实验数量与充分性
- **实验数量**：包括在主要导航基准上的对比实验、模型规模扩展实验（2B→8B参数）、零样本真实机器人实验，以及消融实验（联合训练 vs 仅轨迹训练）等。
- **充分性**：实验覆盖了多种任务模态、不同模型规模、多环境泛化，且通过消融验证了联合训练的必要性，较为充分。
- **公平性**：未详细说明与对比方法的超参数是否一致，但声称使用标准benchmark评估，具有一定客观性。

## 六、论文的主要结论与发现
- Qwen-RobotNav在主要导航基准上取得新的SOTA结果。
- 模型从2B到8B参数表现出良好的可扩展性，性能随规模提升。
- 联合多任务训练发展出共享的空间规划基板，该基板可在任务族间转移。
- 零样本泛化到真实世界机器人，在不同环境中表现强大。
- 参数化接口使模型成为智能体系统的自然构建模块，支持动态切换任务模式。

## 七、优点
- **创新性**：提出参数化接口概念，统一了多种导航任务的观察策略配置，未改变骨干架构。
- **实用性**：适合嵌入上层规划器，实现长周期复杂行为组合。
- **鲁棒性**：训练时随机化参数，确保推理时任意配置下稳定。
- **规模效应**：验证了从2B到8B参数的扩展性。
- **泛化能力**：零样本迁移到真实机器人场景。

## 八、不足与局限
- **算力信息缺失**：未披露训练资源，影响可复现性评估。
- **对比方法细节不足**：未列出具体对比的方法名称和性能数值，削弱了结论的可验证性。
- **实验覆盖范围**：主要基于仿真benchmark，真实世界测试种类和难度有限。
- **潜在偏差**：仅使用1560万样本，数据多样性可能受限；联合训练配方未完全公开。
- **应用限制**：模型依赖于上层规划器分解任务，在无规划器辅助的端到端场景中可能效果下降。

（完）
