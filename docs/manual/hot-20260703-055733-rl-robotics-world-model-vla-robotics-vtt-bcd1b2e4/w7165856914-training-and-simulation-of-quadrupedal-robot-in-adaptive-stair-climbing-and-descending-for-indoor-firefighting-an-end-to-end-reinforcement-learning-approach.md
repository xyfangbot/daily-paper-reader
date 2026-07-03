---
title: "Training and Simulation of Quadrupedal Robot in Adaptive Stair Climbing and Descending for Indoor Firefighting: An End-to-End Reinforcement Learning Approach"
title_zh: 用于室内消防的自适应上下楼梯的四足机器人训练与仿真：一种端到端强化学习方法
authors: "Baixiao Huang, Baiyu Huang, Yu Hou"
date: 2026-06-22
pdf: "https://www.iaarc.org/./publications/fulltext/ISARC2026_1270.pdf"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning for drone navigation in dynamic environments"
tldr: 针对室内消防搜救中四足机器人难以自适应爬升下降多种楼梯的问题，本文提出两阶段端到端深度强化学习框架。第一阶段在抽象金字塔地形训练基础技能，第二阶段将策略迁移至Isaac Lab中的直、L型和螺旋楼梯，使用中心线导航统一学习导航与运动。仅依靠局部高度图感知即可泛化到不同楼梯形状，实验验证了成功率和失败模式。主要贡献包括两阶段迁移框架、无需层次规划的统一学习以及多楼梯泛化分析。
source: openalex
selection_source: hot_paper_scout
motivation: 四足机器人在室内消防初期搜索中需快速爬升下降各种楼梯，但现有分层方法难以协调导航与运动，导致适应性差。
method: 两阶段端到端RL：先在抽象金字塔地形训练，再迁移至直、L型、螺旋楼梯，采用中心线导航公式统一学习导航与运动。
result: 策略成功泛化到多种楼梯形状，仅用局部高度图感知即可高效爬升下降，难度增加时成功率下降但仍优于传统方法。
conclusion: 两阶段框架和中心线导航方法有效提升了四足机器人在复杂楼梯环境中的自适应能力，为室内消防搜救提供新方案。
---

## 摘要
四足机器人被用于室内火灾初期的初步搜索。典型的初步搜索包括在危险条件下快速彻底地寻找受害者并监测易燃材料。然而，复杂室内环境中的态势感知以及跨不同楼梯的快速上下楼仍是机器人辅助初步搜索的主要挑战。在本项目中，我们设计了一种两阶段端到端深度强化学习方法，以优化导航和运动。第一阶段，四足机器人Unitree Go2在Isaac Lab的金字塔楼梯地形中训练上下楼梯。第二阶段，四足机器人利用前一阶段迁移的学习策略，在Isaac Lab引擎中训练上下各种真实室内楼梯。这些室内楼梯包括直梯、L形梯和螺旋梯，以支持复杂环境中的上下楼任务。本项目探索了如何平衡导航与运动，以及端到端强化学习方法如何使四足机器人适应不同楼梯形状。我们的主要贡献包括：（1）一种两阶段端到端强化学习框架，将上下楼技能从抽象金字塔地形迁移到真实室内楼梯拓扑；（2）一种基于中心线的导航公式，无需分层规划即可实现导航与运动的统一学习；（3）仅利用局部高度图感知即在不同楼梯间展示策略泛化能力；（4）针对楼梯难度增加时的成功率、效率和失败模式的实证分析。

## Abstract
Quadruped robots are used for primary searches during the early stages of indoor fires.A typical primary search involves quickly and thoroughly looking for victims under hazardous conditions and monitoring flammable materials.However, situational awareness in complex indoor environments and rapid stair climbing and descending across different staircases remain the main challenges for robot-assisted primary searches.In this project, we designed a two-stage end-to-end deep reinforcement learning (RL) approach to optimize both navigation and locomotion.In the first stage, the quadrupeds, Unitree Go2, were trained to climb and descend stairs in Isaac Lab's pyramid-stair terrain.In the second stage, the quadrupeds were trained to climb and descend various realistic indoor staircases in the Isaac Lab engine, with the learned policy transferred from the previous stage.These indoor staircases are straight, L-shaped, and spiral, to support climbing and descending tasks in complex environments.This project explores how to balance navigation and locomotion and how end-to-end RL methods can enable quadrupeds to adapt to different stair shapes.Our main contributions are: (1) A two-stage end-to-end RL framework that transfers climbing/descending skills from abstract pyramid terrain to realistic indoor stair topologies.( 2) A centerline-based navigation formulation that enables unified learning of navigation and locomotion without hierarchical planning.(3) Demonstration of policy generalization across diverse staircases using only local height-map perception.(4) An empirical analysis of success, efficiency, and failure modes under increasing stair difficulty.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究背景**：室内火灾初期，消防员需要进行快速、彻底的初级搜索以定位受害者并监测易燃材料。四足机器人（“机器狗”）因成本低、适应性强、稳定性好、可装备机械臂开门等优势，成为辅助初级搜索的理想平台。然而，现有轮式或履带式UGV只能单层作业，无人机UAV无法有效处理障碍物，而四足机器人在复杂室内环境中的态势感知和跨不同楼梯的快速上下楼能力是主要瓶颈。
- **核心问题**：如何让四足机器人自适应地上下多种类型的楼梯（直梯、L形梯、螺旋梯），同时保持高敏捷性，且无需分层规划（如独立的导航和运动模块），实现端到端统一学习。
- **研究动机**：现有模型或分层方法（如Qi等人、Liang等人、Hoeller等人）要么限于简化直梯环境，要么依赖于特殊硬件或分层分解导致复杂性增加、全局最优行为受限。因此需要一种通用的端到端框架，能在多种真实楼梯拓扑下兼顾导航与运动，且能泛化到未见过的楼梯参数。

## 二、论文提出的方法论
- **核心思想**：采用两阶段端到端深度强化学习（DRL）框架，将上下楼梯技能从抽象金字塔地形迁移到真实室内楼梯拓扑。第一阶段在Isaac Lab内置的金字塔楼梯地形上训练基础爬升/下降运动技能；第二阶段将策略迁移到自定制的直、L型、螺旋楼梯上，使用中心线导航奖励统一学习导航与运动，避免分层规划。
- **关键技术细节**：
  - **网络架构**：策略网络由浅层CNN编码器（输入21×21局部高度图，输出128维特征）和3层MLP（隐藏层128、128、64）组成。评论家网络共享CNN编码器，MLP权重独立。输出12个关节位置命令，经PD控制器转化为力矩。
  - **观测空间**：包括身体坐标系线速度、角速度、重力向量、12个关节位置与速度、上一时刻关节命令、目标位姿（x, y, yaw）、足底周围高度（32个点）和栅格高度图（21×21分辨率0.2m）。仅使用局部高度图，不依赖全局地图。
  - **动作空间**：12个关节位置设定点。
  - **算法**：PPO，on-policy。
  - **奖励设计**：分为任务奖励和正则化奖励。第一阶段使用粗/细导航奖励（tanh函数平滑）。第二阶段用中心线奖励（鼓励靠近楼梯中心线）和路径奖励（沿中心线向目标前进），并加入航向跟踪惩罚。正则化奖励包括功率惩罚、动作变化率、关节极限、碰撞、飞腿步态惩罚等，详细权重见表1。
  - **课程学习（Curriculum）**：每个地形类型分10个难度等级，步高从0/2cm到12cm，楼梯宽度和长度随难度增加。L形楼梯转弯后长度从0到3米，螺旋楼梯圈数从0.2到0.5转。通过达到目标才能升级，否则降级，完成所有等级后随机等级继续训练以防遗忘。

## 三、实验设计
- **实验场景**：在NVIDIA Isaac Lab仿真平台中构建三种真实室内楼梯类型：直梯（Straight）、L形梯（L-shaped）和螺旋梯（Spiral）。测试时每种楼梯分为6个难度等级（步高4cm至14cm），参数与训练时不同，以测试泛化能力。
- **Benchmark与对比方法**：论文未直接与现有方法定量对比，而是进行了**内部消融**：比较仅经过第一阶段训练的策略与经两阶段训练的策略在Level 3难度下的成功率（图4）。结果表明第二阶段训练显著提升性能，特别是L形楼梯（第一阶段模型因“抄近路”导致碰撞失败）。
- **评估指标**：目标到达成功率、平均线速度、平均爬升/下降速率、位置误差、航向误差、平均功率输出。每种地形300个episode，初始位置随机偏移±0.3米，航向随机偏移±45度。
- **结果展示**：通过YouTube视频截图（图2）和折线图（图3）展示不同难度下的性能变化。关键发现：螺旋梯最难，成功率最低；L形梯在难度5→6时位置/航向误差急剧增加；直梯性能最好。功率消耗随难度增加，但6级时下降（策略趋于保守）。

## 四、资源与算力
- **文中未明确说明使用的GPU型号、数量、训练时长等具体算力信息**。仅提到在Isaac Lab平台上训练，但训练环境细节未提供。因此无法获知训练的计算成本。

## 五、实验数量与充分性
- **实验数量**：在三种地形（直、L、螺旋）上各测试6个难度等级，每种300 episode，共18组×300=5400个测试轨迹。消融实验（图4）对比了第一阶段与两阶段模型在Level 3下的成功率，但未给出统计误差棒或重复次数。
- **充分性分析**：实验覆盖了三种典型室内楼梯形状和多种步高，但缺乏与其他基线方法（如分层方法、模型预测控制等）的直接定量比较。仅通过自身消融验证两阶段训练的必要性，公平性上稍显不足。另外，所有实验在仿真中进行，未涉及真实的Sim-to-Real部署，因此结论的泛化能力仅停留在仿真层面。实验设计较为规范，指标全面，但重复性和统计显著性未明确。

## 六、论文的主要结论与发现
- 两阶段端到端RL框架能有效将金字塔地形的爬升技能迁移到复杂室内楼梯，成功实现导航与运动的统一学习。
- 中心线奖励设计可引导机器人沿楼梯中间稳定上下，避免分层规划的复杂性。
- 仅依赖局部高度图感知，策略就能在不同形状楼梯间泛化，表明对局部信息的鲁棒性和部分可观测环境下的适应能力。
- 随着难度增加（步高>12cm），成功率显著下降，特别是在螺旋楼梯上；策略在困难时会变得保守（功率降低、速度下降）以避免失败。
- 第二阶段训练对导航能力获取至关重要：仅第一阶段训练的模型在L形楼梯上无法正确转向，会“抄近路”导致碰撞。

## 七、优点
- **端到端统一学习**：避免了传统分层方法（感知→规划→控制）的系统复杂性和全局最优损失，设计简洁、执行快速。
- **两阶段迁移框架**：先抽象后具体的训练顺序，有效提升了学习效率和泛化能力。
- **中心线导航公式**：巧妙地将导航任务转化为沿中心线前进，使导航与运动自然耦合，无需额外路径规划器。
- **局部感知的鲁棒性**：仅用21×21高度图即可应对多种楼梯形状，适用于消防场景中全局地图不可用的情况。
- **课程学习设计**：渐进增加步高、宽度和长度，特别是L形和螺旋楼梯的转弯段长度从0开始增加，有助于逐步学习转向策略。
- **全面的奖励函数**：包含任务奖励和多种正则化项（关节限制、碰撞、步态稳定性等），使学到的行为更加自然稳定。

## 八、不足与局限
- **仿真局限**：所有实验在Isaac Lab仿真中进行，未在真实机器人上验证，存在Sim-to-Real差距。论文仅在结尾提及未来将使用Isaac Lab的Sim-to-Real工作流测试真实机器人。
- **实验对比不足**：未与现有代表性方法（如ANYmal的感知规划方法、模型优化方法）进行定量对比，难以客观评估本方法相对于现有技术的绝对优势。
- **失败模式分析不够深入**：虽然指出高难度下成功率下降、策略保守，但未详细分析失败原因（如摔倒、卡住、偏离楼梯等分类统计）。
- **楼梯场景单一**：仅测试了完整楼梯，未考虑火灾中楼梯可能被损坏、堵塞或带有斜坡的情况，与实际消防环境有差距。
- **可重复性信息缺失**：未提供训练超参数、随机种子、GPU类型和训练时长等细节，不利于他人复现。

（完）
