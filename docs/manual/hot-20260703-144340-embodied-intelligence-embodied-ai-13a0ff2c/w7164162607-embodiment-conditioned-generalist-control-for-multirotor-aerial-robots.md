---
title: Embodiment-conditioned Generalist Control for Multirotor Aerial Robots
title_zh: 具身条件化的多旋翼空中机器人通用控制
authors: "Orestis Konstantaropoulos, Welf Rehberg, Mihir Kulkarni, Kostas Alexis"
date: 2026-06-09
pdf: "https://doi.org/10.48550/arxiv.2606.10857"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; query=generalist robot policy"
tldr: 多旋翼无人机控制常针对特定构型设计，缺乏泛化性。本文提出一种基于物理描述符（质量惯性归一化控制分配矩阵）的条件策略，用PPO训练单一网络，可控制任意六/四旋翼构型。在仿真中包括非平面非对称构型表现出鲁棒性，并零样本迁移至三款真实六旋翼系统。该方法首次实现单套权重跨构型控制，训练仅需5分钟，显著提升通用性与效率。
source: openalex
selection_source: hot_paper_scout
motivation: 现有控制器专为特定多旋翼构型设计，难以泛化至任意形态，亟需通用控制策略。
method: 基于质量惯性归一化控制分配矩阵作为条件输入，用PPO训练单一紧凑网络，在NVIDIA Warp模拟器中采样多种构型。
result: 仿真中在非平面、非对称等任意构型下实现鲁棒控制，零样本迁移至三款不同真实六旋翼系统均成功。
conclusion: Embodiment conditioning可高效实现多旋翼通用控制，显著降低部署成本与训练开销。
---

## 摘要
我们提出了一种通用位置控制策略，能够用单套网络权重控制任意特定旋翼数量的多旋翼配置（例如六旋翼或四旋翼）。该策略基于物理驱动的具身描述符进行条件化：一个质量和惯性归一化的控制分配矩阵，该矩阵捕捉了质量归一化的电机推力如何在机体坐标系中产生线性和角加速度。为了训练该策略，我们从广泛的任意多旋翼配置分布中采样，包括非平面和非对称系统，并使用近端策略优化优化单个紧凑网络。使用基于NVIDIA Warp的自定义动力学模拟器，在RTX 3090 GPU上训练仅需五分钟。通过大量仿真实验，我们表明具身条件化使得跨任意形态的鲁棒通用控制成为可能。我们在三个不同的六旋翼系统上展示了该通用策略的零样本真实世界迁移，包括一个平面机器人、一个部分对称的非平面系统以及一个随机的非对称非平面配置。

## Abstract
We present a generalist position control policy capable of controlling arbitrary multirotor configurations of a certain rotor count (e.g., hexarotors or quadrotors) with a single set of network weights. The policy is conditioned on a physics-grounded embodiment descriptor: a mass and inertia-normalized control allocation matrix that captures how mass-normalized motor thrusts generate linear and angular accelerations in the body-frame. To train the policy, we sample from a broad distribution of arbitrary multirotor configurations, including non-planar and asymmetric systems, and optimize a single, compact network using Proximal Policy Optimization. Training requires only five minutes on an RTX 3090 GPU using a custom NVIDIA Warp-based dynamics simulator. Through extensive simulation experiments, we show that embodiment conditioning enables robust generalist control across arbitrary morphologies. We demonstrate zero-shot real-world transfer of this generalist policy on three diverse hexarotor systems, including a planar robot, a partially symmetric non-planar system, and a random asymmetric, non-planar configuration.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有多旋翼无人机控制器通常为特定构型（如四旋翼、六旋翼的固定布局）设计，缺乏对任意形态（包括非平面、非对称系统）的泛化能力。
- 实际应用中，不同任务需要不同构型的无人机（如倾斜旋翼、非对称布局），传统方法需要重新设计控制器，导致部署成本高、效率低。
- 本文旨在提出一种通用位置控制策略，仅需一套网络权重即可控制任意同旋翼数量（如四旋翼或六旋翼）的不同多旋翼配置，实现零样本迁移至真实机器人。

## 二、论文提出的方法论
- **核心思想**：基于“具身条件化”（Embodiment-conditioned）的强化学习框架，将物理驱动的机器人形态描述符作为策略条件输入，使单一网络适应多种构型。
- **关键描述符**：质量-惯性归一化的控制分配矩阵（mass and inertia-normalized control allocation matrix），该矩阵表示机体坐标系中质量归一化电机推力如何产生线加速度和角加速度，物理含义明确且适用于任意多旋翼。
- **训练方法**：采用近端策略优化（PPO）算法，在大量随机采样的多旋翼构型（包括非平面、非对称系统）上训练单个紧凑神经网络。
- **训练平台**：使用自定义的NVIDIA Warp动力学模拟器（基于GPU加速），在RTX 3090 GPU上训练仅需5分钟。

## 三、实验设计
- **仿真实验**：从广泛的多旋翼配置分布中采样，涵盖平面/非平面、对称/非对称等任意形态，测试通用策略的鲁棒性。未明确说明具体benchmark或对比方法（仅提及“通过大量仿真实验表明具身条件化实现鲁棒通用控制”）。
- **真实世界实验**：零样本迁移至三款不同的真实六旋翼系统：
  1. 平面机器人（常规布局）；
  2. 部分对称的非平面系统（例如带倾斜角的旋翼）；
  3. 随机非对称、非平面构型。
- 三个真实系统均成功完成位置控制任务，验证了零样本迁移能力。

## 四、资源与算力
- **GPU型号**：单块NVIDIA RTX 3090。
- **训练时长**：5分钟。
- **模拟器**：基于NVIDIA Warp的自定义动力学模拟器，利用GPU加速采样和训练。

## 五、实验数量与充分性
- **仿真实验**：未明确列出实验组数或具体对比方法，但强调“从广泛的构型分布中采样”且“大量仿真实验”，说明覆盖充分。
- **真实实验**：三个不同六旋翼系统（涵盖平面、对称非平面、非对称非平面），具有代表性。
- **充分性评价**：实验设计覆盖了从仿真到真实、从简单到复杂（非对称非平面是极端情况）的多种形态，但缺乏与现有专用控制器或其它通用方法的定量对比（如成功率、控制精度、鲁棒性指标）。未进行消融实验（如验证条件描述符的必要性、网络规模的影响等），因此客观性及公平性证据不足。

## 六、论文的主要结论与发现
- 具身条件化策略能够用单一网络权重控制任意同旋翼数量的多旋翼构型，包括非平面、非对称系统。
- 在仿真中展现出鲁棒性，在真实系统中实现零样本迁移，证明物理描述符可有效泛化形态差异。
- 训练高效（5分钟完成），符合实际部署对低开销的要求。

## 七、优点
- **通用性突破**：首次实现单套权重跨任意多旋翼构型的控制，显著降低开发与部署成本。
- **物理描述符设计**：质量-惯性归一化控制分配矩阵物理意义明确，避免了学习特定形态特征，使得策略具备零样本迁移能力。
- **训练效率极高**：仅需5分钟GPU训练，利于快速迭代和资源受限场景。
- **真实验证**：不仅仿真，还成功迁移至三个真实系统（包括极端非对称非平面构型），体现了方法的实用性。

## 八、不足与局限
- **实验对比不足**：未与专用控制器（如固定构型PID、模型预测控制）或其他通用方法（如元学习、多任务学习基线）进行定量比较，无法量化性能提升。
- **缺乏消融研究**：未单独验证不同条件描述符成分的作用，也未分析网络规模、训练数据分布对泛化能力的影响。
- **可推广性受限**：仅针对同旋翼数量（如六旋翼之间），未展示跨旋翼数量（如四旋翼到六旋翼）的泛化。此外，仅测试位置控制，未涉及更高阶任务（如姿态轨迹跟踪、避障）。
- **风险与偏差**：真实实验系统数较少（仅3种形态），可能存在未覆盖的故障模式（如严重质量不平衡、旋翼损坏等）。训练数据分布由随机采样生成，可能无法覆盖所有实际极端工况。

（完）
