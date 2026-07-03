---
title: "Training and Simulation of Quadrupedal Robot in Adaptive Stair Climbing and Descending for Indoor Firefighting: An End-to-End Reinforcement Learning Approach"
title_zh: 面向室内消防的自适应上下楼梯四足机器人训练与仿真：一种端到端强化学习方法
authors: "Baixiao Huang, Baiyu Huang, Yu Hou"
date: 2026-06-22
pdf: "https://www.iaarc.org/./publications/fulltext/ISARC2026_1270.pdf"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning for drone navigation in dynamic environments"
tldr: 四足机器人在室内火灾搜索中面临复杂楼梯环境挑战。本文提出两阶段端到端强化学习方法：先于抽象金字塔地形训练攀爬技能，再迁移至直梯、L型与螺旋梯等真实场景。机器人仅凭局部高度图感知即可泛化，成功完成攀爬与下梯任务。该方法统一导航与运动学习，无需分层规划，显著提升适应性。
source: openalex
selection_source: hot_paper_scout
motivation: 解决四足机器人在室内火灾搜索中快速适应不同形状楼梯的挑战，实现导航与运动的联合学习。
method: 两阶段端到端强化学习：第一阶段在金字塔地形训练基础攀爬技能，第二阶段迁移至Isaac Lab中的直梯、L型及螺旋梯场景，并采用中心线导航公式统一学习。
result: 机器人成功在三种真实楼梯形状上自适应攀爬与下梯，仅依赖局部高度图感知，成功率和效率在复杂楼梯中表现良好。
conclusion: 验证了端到端RL框架可使四足机器人有效适应多样楼梯，贡献了统一的导航-运动学习方法与失败模式经验分析。
---

## 摘要
四足机器人被用于室内火灾初期的初步搜索。典型的初步搜索包括在危险条件下快速彻底地寻找受害者并监测可燃材料。然而，复杂室内环境中的态势感知以及跨不同楼梯的快速上下楼梯仍然是机器人辅助初步搜索的主要挑战。在本项目中，我们设计了一种两阶段端到端深度强化学习方法，以优化导航和运动。第一阶段，四足机器人Unitree Go2在Isaac Lab的金字塔楼梯地形上训练上下楼梯。第二阶段，四足机器人在Isaac Lab引擎中训练爬上和爬下各种真实的室内楼梯，并迁移前一阶段学习到的策略。这些室内楼梯包括直梯、L形梯和螺旋梯，以支持复杂环境中的上下楼梯任务。本项目探讨了如何平衡导航与运动，以及端到端强化学习方法如何使四足机器人适应不同的楼梯形状。我们的主要贡献包括：(1) 一种两阶段端到端强化学习框架，将上下楼梯技能从抽象的金字塔地形迁移到真实的室内楼梯拓扑结构；(2) 一种基于中心线的导航公式，无需分层规划即可实现导航与运动的统一学习；(3) 仅使用局部高度图感知即可展示策略在多种楼梯上的泛化能力；(4) 在楼梯难度增加时对成功率、效率和失败模式的实证分析。

## Abstract
Quadruped robots are used for primary searches during the early stages of indoor fires.A typical primary search involves quickly and thoroughly looking for victims under hazardous conditions and monitoring flammable materials.However, situational awareness in complex indoor environments and rapid stair climbing and descending across different staircases remain the main challenges for robot-assisted primary searches.In this project, we designed a two-stage end-to-end deep reinforcement learning (RL) approach to optimize both navigation and locomotion.In the first stage, the quadrupeds, Unitree Go2, were trained to climb and descend stairs in Isaac Lab's pyramid-stair terrain.In the second stage, the quadrupeds were trained to climb and descend various realistic indoor staircases in the Isaac Lab engine, with the learned policy transferred from the previous stage.These indoor staircases are straight, L-shaped, and spiral, to support climbing and descending tasks in complex environments.This project explores how to balance navigation and locomotion and how end-to-end RL methods can enable quadrupeds to adapt to different stair shapes.Our main contributions are: (1) A two-stage end-to-end RL framework that transfers climbing/descending skills from abstract pyramid terrain to realistic indoor stair topologies.( 2) A centerline-based navigation formulation that enables unified learning of navigation and locomotion without hierarchical planning.(3) Demonstration of policy generalization across diverse staircases using only local height-map perception.(4) An empirical analysis of success, efficiency, and failure modes under increasing stair difficulty.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 研究动机：四足机器人在室内火灾初期搜索中具有优势（成本低、适应性强、稳定性好），但在复杂室内环境下的态势感知和跨多种楼梯（直梯、L形梯、螺旋梯）的快速上下楼梯能力仍是主要技术挑战。
- 背景：现有研究多使用轮式/履带式UGV（仅限单层）或无人机（无法处理障碍），四足机器人虽潜力大但缺乏统一的端到端导航-运动学习框架；已有分层方法增加系统复杂度，且楼梯形状多为简化直梯。
- 整体含义：本文旨在通过端到端强化学习方法，使四足机器人能从抽象地形迁移技能至真实复杂楼梯，实现导航与运动的统一学习，支撑高效室内消防搜索。

## 二、论文提出的方法论
- 核心思想：提出两阶段端到端深度强化学习框架，第一阶段在抽象金字塔地形上训练基础上下楼梯技能，第二阶段将策略迁移至三种真实室内楼梯（直梯、L形、螺旋梯）进行微调，实现导航与运动的联合学习，无需分层规划。
- 关键技术细节：
  - 神经网络结构：策略网络由CNN编码器（21×21高度图输入，输出128维特征）和三层MLP（128,128,64）组成；评论家网络共享CNN编码器但有独立MLP。
  - 观测输入：包括本体线速度、角速度、重力矢量、12个关节位置/速度、上一时刻动作、目标位姿（x,y,z,yaw）、脚底地形高度（32个点）和周围网格高度图（21×21，0.2m分辨率）。
  - 动作输出：12个关节位置命令，由PD控制器转换为扭矩。
  - 训练算法：近端策略优化（PPO），采用on-policy方式。
  - 奖励设计：分为任务奖励和正则化惩罚。
    - 第一阶段：粗导航奖励（σ=5.0）和细导航奖励（σ=1.0），基于距离的tanh函数。
    - 第二阶段：替换粗导航奖励为中心线奖励和路径奖励，鼓励沿楼梯中心前进；同时加入航向跟踪惩罚。
  - 正则化惩罚：包括功率、静态扭矩、动作变化率、关节极限、关节速度/加速度、碰撞（身体/头部/髋/大腿碰撞-8.0，小腿接触-0.2）、飞腿姿态（-0.1）、步幅奖励（+0.2）等。
  - 课程学习：每个地形分10个难度等级，逐步增加台阶高度（0cm→12cm）和楼梯宽度/长度；通过成功/失败决定升级/降级，完成所有等级后随机选难度继续训练防止遗忘。

## 三、实验设计
- 实验场景：使用NVIDIA Isaac Lab仿真平台，三种室内楼梯地形：直梯、L形梯、螺旋梯（相对于训练时参数有所变化）。测试时每个地形分6个难度等级（台阶高度4cm至14cm）。
- 基准测试与对比：
  - 评估指标：目标到达成功率、平均线速度、平均攀爬/下降速率、位置误差、航向误差、平均功率输出。
  - 对比方法：将两阶段训练后的模型与仅进行第一阶段训练的模型在第三难度等级下比较成功率。
  - 消融分析：对比不同楼梯形状（直、L、螺旋）和不同难度等级的性能，以及上下行方向差异。
- 实验设置：每个测试场景运行300个episode，机器人起始位置距楼梯0.5m，具有±0.3m横向偏移和±45°航向偏移，目标位姿从地形中随机采样。

## 四、资源与算力
- 论文中未明确说明使用的GPU型号、数量、训练时长等具体算力信息。
- 训练平台为NVIDIA Isaac Lab，属于仿真训练环境，推断需要一定算力支持大规模并行仿真（但未量化）。

## 五、实验数量与充分性
- 实验数量：每个楼梯类型测试6个难度等级，共6×3=18个场景组，每组300个episode。
- 消融实验：比较了阶段1模型与阶段2模型在第三难度下的成功率（图4），覆盖三种地形。
- 充分性分析：实验设计较充分——覆盖了三种典型楼梯形状、多个难度层级、上下行两个方向，评估了成功率、速度、误差、功率等多个维度。但缺乏与已有方法（如分层框架、模型控制）的直接定量对比，仅内部消融。此外未进行Sim-to-Real实验验证。
- 客观性：评估指标定义明确，随机初始化偏移保证了测试多样性，结果呈现了均值（未给出方差或置信区间），客观性尚可。

## 六、论文的主要结论与发现
- 两阶段训练显著提升了性能：第二阶段训练后，模型在直梯、L形梯、螺旋梯上的成功率均相比仅第一阶段训练有大幅提升（图4），L形梯改进最明显。
- 螺旋梯是最困难的地形：随着难度等级增加，螺旋梯成功率下降最快（尤其第6级），机器人常采取保守策略（停留而非冒险攀爬）。
- 平均线速度随难度增加而下降，但攀爬/下降速率反而略有上升，说明机器人以更高效的方式完成垂直移动。
- 位置误差和航向误差随难度增加而增大，L形和螺旋梯上的误差迅速增加（第5-6级突增）。
- 功率消耗随难度增大而增加，但第6级时功率下降，因为机器人采用更保守、更慢的动作以避免失败。
- 仅使用局部高度图感知（无全局地图）即可实现复杂楼梯导航，证明了策略对部分可观性的鲁棒性。

## 七、优点
- 端到端框架简洁高效：无需分层规划，统一学习导航与运动，降低了系统复杂度，且自然处理感知-控制反馈。
- 两阶段迁移学习设计：从抽象金字塔地形迁移至真实楼梯，减少直接训练复杂地形所需样本，提升了泛化能力。
- 中心线导航公式：使机器人沿楼梯中心行进，同时追踪目标，有效解决了转弯问题。
- 课程学习策略：逐步增加楼梯高度和长度，加速学习且防止遗忘。
- 实验覆盖全面：涵盖三种典型楼梯、多个难度、上下行两个方向，分析维度丰富（成功率、速度、误差、功率）。
- 开源性：使用Isaac Lab和Unitree Go2，具实用性和可复现性。

## 八、不足与局限
- 未公开算力细节：缺少GPU型号、数量、训练时长等，影响复现和公平比较。
- 仅仿真验证：未进行真机实验（Sim-to-Real），虽提到未来计划，但当前结果在真实环境中的鲁棒性未知。
- 缺少与已有方法的定量对比：未与分层方法[10][11]或模型控制[7][8]进行同场景性能对比，消融仅内部。
- 成功率波动未报告：300个episode下未给出方差/置信区间，无法评估稳定性。
- 适用范围有限：假设楼梯完整无损坏，未考虑火灾中可能出现的障碍、烟尘视觉遮挡、温度影响。
- 高难度下成功率骤降：第6级螺旋梯成功率极低，说明算法在处理极端楼梯时仍有不足；作者提出探索奖励可能缓解但未验证。
- 仅使用局部高度图：虽然展现鲁棒性，但在需要全局规划（如多层建筑搜索）时可能不足。

（完）
