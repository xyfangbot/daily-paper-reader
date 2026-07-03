---
title: "RGB: RL Guided Whole-Body MPPI for Humanoid Control"
title_zh: "RGB: 强化学习引导的人形机器人全身MPPI控制"
authors: "Yunsoo Seo, Sol Choi, Euncheol Im, Myo Taeg Lim, Yisoo Lee"
date: 2026-06-23
pdf: "https://arxiv.org/pdf/2606.25123"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; institutions=Korea Institute of Science and Technology, The University of Texas at Austin; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 人形机器人全身控制器需兼具鲁棒性与精度，但深度强化学习策略难以在不重训的情况下添加新目标。本文提出RL引导的全身模型预测路径积分框架，将预训练RL策略作为采样先验，通过MPPI在线校正以满足模块化成本项。在Unitree G1人形机器人仿真中实现280Hz稳定控制，相比纯RL基线在直线行走和全身参考跟踪上显著提升精度，无需重训策略。
source: openalex
selection_source: hot_paper_scout
motivation: 现有深度RL全身控制器难以灵活添加新反馈目标，需重新训练，限制了实用性。
method: 将预训练RL策略作为采样先验，通过MPPI在线校正其输出以优化模块化成本项，实现闭环控制。
result: 在MuJoCo仿真中29自由度Unitree G1人形机器人实现280Hz稳定控制，直线行走漂移校正和全身参考跟踪精度优于纯RL基线。
conclusion: RL引导的MPPI框架在不重训策略前提下，有效提升任务级精度，适用于接触丰富的全身控制场景。
---

## 摘要
人形机器人在接触丰富的环境中需要既鲁棒又精确的全身控制器。虽然深度强化学习（RL）实现了鲁棒稳定性，但其行为与训练目标和命令接口紧密耦合，使得在不重新训练的情况下难以添加新的反馈目标。在本研究中，我们提出了一个强化学习引导的全身模型预测路径积分（MPPI）框架，该框架作为预训练RL策略之上的附加反馈控制器。我们不将RL策略作为最终控制器，而是将其用作采样先验，使MPPI的滚动偏向于动态可行的行为。任务目标通过模块化的MPPI成本项指定，MPPI通过在线持续校正RL先验来满足这些目标，而无需重新训练策略，从而形成闭环。在MuJoCo中对29自由度的宇树G1人形机器人进行的仿真证明了稳定的高速控制（平均280 Hz）。在相同的命令接口下，所提方法相比纯RL基线提高了任务级精度。这是通过校正直行过程中的系统性漂移以及跟踪通过成本施加的额外全身参考信号来实现的。

## Abstract
Humanoid robots require whole-body controllers that are both robust and precise in contact-rich environments. While deep reinforcement learning (RL) achieves robust stability, its behavior is tightly coupled to the training objective and command interface, making it difficult to add new feedback objectives without retraining. In this study, we propose an RL guided whole-body model predictive path integral (MPPI) framework that acts as an add-on feedback controller on top of a pretrained RL policy. Instead of using RL policy as the final controller, we use it as a sampling prior that biases MPPI rollouts toward dynamically feasible behaviors. Task objectives are specified through modular MPPI cost terms, and MPPI closes the loop by continuously correcting the RL prior online to satisfy these objectives without retraining the policy. Simulations on a 29-DoF Unitree G1 humanoid in MuJoCo demonstrate stable high-rate control (average 280~Hz). The proposed method improves task-level precision over a pure RL baseline under the same command interface. This is achieved by correcting systematic drift during straight walking and tracking additional whole-body reference signals imposed through the cost.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 人形机器人需要在接触丰富的环境中实现既鲁棒又精确的全身控制。
- 现有方法分为两大范式：模型控制（可解释、稳定，但难以处理高维行为）和深度强化学习（RL，鲁棒且适应性强）。但RL策略的行为与训练目标和命令接口高度绑定，若要添加新的反馈目标（如调节摆脚高度、骨盆高度等），通常需要重新设计奖励并重新训练，导致开发成本高、任务扩展性差。
- 此外，RL策略天然不强制满足严格的约束（如力矩限制），且纯RL策略在对称性动作（如直线行走）中可能因随机优化而产生系统性漂移。
- 基于采样的模型预测控制（如MPPI）能够在线优化复杂目标并显式处理约束，但标准MPPI对初始化和采样分布敏感，在高自由度人形机器人上性能易退化。
- 因此，本文的目标是结合两者的优势：利用RL提供鲁棒行为先验，同时通过MPPI在线修正并添加模块化任务目标，实现无需重新训练的任务增强。

## 二、论文提出的方法论
- **核心思想**：提出一个RL引导的全身MPPI框架（RGB），将预训练的RL策略作为采样先验，而不是最终控制器。MPPI作为附加反馈控制器，通过物理引擎滚动优化来校正RL先验输出，以满足通过模块化成本项指定的新任务目标。
- **关键技术细节**：
  - **整体架构**：控制栈分为三层：
    1. RL策略（50 Hz）：输出名义关节位置参考 q_RL。
    2. MPPI模块（异步重规划，平均280 Hz）：以q_RL为采样均值，通过高斯扰动生成候选轨迹，利用物理引擎（MuJoCo）进行滚动模拟，计算任务成本，并通过重要性加权更新得到最优控制序列。
    3. 底层PD控制器（500 Hz）：跟踪MPPI输出的期望关节位置，计算关节力矩。
  - **RL策略作为采样先验**：框架与具体RL算法无关。本文使用预训练的步行速度跟踪策略（在IsaacLab中使用PPO训练）。RL策略输出12个下肢自由度目标位置。MPPI采样时，扰动以RL输出为中心，从而将探索限制在动态可行区域。
  - **Knot-based插值**：为降低优化维度，采用H个节点（本文H=2）参数化控制序列，通过三次插值得到全分辨率控制输入。采样噪声加在节点上。
  - **成本函数设计**：任务目标通过模块化的MPPI运行成本 ℓ 表示。本文展示了两种任务：
    - 直线行走漂移抑制：添加成本 ℓ = β_y ||y_base - y_des||² + β_ψ ||ψ_base - ψ_des||²，β_y=25, β_ψ=25。
    - 深蹲任务（基础高度跟踪）：添加成本 ℓ = β_z ||z_base - z_des(t)||²，β_z=100。
  - **更新规则**：使用重要性权重公式（公式8）聚合采样轨迹，得到更新后的节点向量，再插值后取第一个控制命令执行。
- **算法流程**（Algorithm 1）：初始化节点；每个控制循环中，如果RL策略更新则获取新先验；如果MPPI完成一次规划，则采样N条轨迹，计算成本与重要性权重，更新节点；最后PD控制器跟踪期望位置。

## 三、实验设计
- **仿真平台与机器人**：MuJoCo仿真环境，使用宇树G1人形机器人模型（29个自由度，其中12个下肢自由度被控制）。
- **滚动模拟工具**：使用MJPC（MuJoCo MPC）进行物理引擎前向模拟和并行滚动。
- **对比基线**：纯RL策略（相同预训练策略，不经过MPPI修正）作为主要对比基线。
- **任务与指标**：
  - **直线行走漂移抑制任务**：给定速度命令 (v_x=1 m/s, v_y=0, ψ=0)，比较两种方法在11.265秒内基座横向位置误差（RMSE）、前进速度跟踪RMSE、横向速度跟踪RMSE。
  - **深蹲任务**：给定分段线性基座高度参考（0.71–0.78 m），比较两种方法是否能跟踪高度变化。
- **未提及**：未使用外部数据集，也未与其他现有MPPI方法或模型控制方法进行比较。仅在仿真中测试两个任务。

## 四、资源与算力
- **文中说明**：所有验证使用一台工作站，配置为Intel Core i9-14900KF CPU、32 GB RAM、NVIDIA GeForce RTX 4070 Ti GPU。但注意，滚动模拟是在CPU上并行计算的（MJPC基于CPU并行），GPU仅用于常规计算环境。
- **训练部分**：RL策略在IsaacLab中使用PPO训练，但未说明训练时长、GPU型号或训练具体资源开销。本文重点在预训练策略的集成，不报告训练资源。

## 五、实验数量与充分性
- **实验数量**：仅进行了两个定性定量任务实验：
  1. 直线行走漂移抑制：一个11.265秒的单一试验，报告RMSE指标。
  2. 深蹲任务：一个约12秒的试验，展示基座高度跟踪曲线和快照。
- **消融实验**：无。作者未比较不同节点数H、不同样本数N、不同噪声标准差等超参数的影响，也未进行跨多种命令或干扰条件的鲁棒性测试。
- **公平性与客观性**：对比基线为纯RL，在相同命令输入下测试。但未与其他混合方法（如模型MPC+RL、不同MPPI初始化方式）对比。结果图表显示清晰，但缺乏多次试验的统计误差条。
- **充分性评价**：实验较为初步，仅验证了框架能在两个特定任务中改善纯RL性能，但实验覆盖不足，缺乏对控制频率、样本效率、泛化性等更全面的评估。

## 六、论文的主要结论与发现
- RL引导的MPPI框架作为附加反馈控制器，在保持RL策略鲁棒性的同时，显著改善了任务精度：
  - 直线行走中，基座横向漂移RMSE从纯RL的0.339 m降到0.022 m（改善14倍）；横向速度跟踪RMSE从0.046 m/s降到0.021 m/s；前进速度跟踪精度相当（RMSE 0.773 vs 0.806）。
  - 深蹲任务中，MPPI能准确跟踪时变基座高度参考（0.71–0.78 m），而纯RL策略保持名义高度不变，无法跟随。
- 通过MPPI成本项添加新目标无需重新训练RL策略，实现了任务增强。
- 实现了CPU并行下的平均280 Hz控制频率，证明了实时可行性。

## 七、优点
- **方法创新性**：将RL策略作为MPPI的采样先验而非最终控制器，巧妙结合了学习方法的鲁棒性和模型预测控制的灵活性。
- **模块化与可扩展**：任务目标通过成本项模块化添加，无需修改或重训RL策略，降低了任务迁移成本。
- **实际可行性**：在29自由度人形机器人仿真中达到280 Hz有效更新率，满足实时控制要求；框架对物理引擎依赖低，可推广。
- **解释性强**：通过成本设计明确指定期望行为（如漂移抑制、高度跟踪），便于调试和理解。
- **实验验证清晰**：两个任务直观展示了改进，其中直线行走漂移问题常见于实际部署，该方法的校正效果显著。

## 八、不足与局限
- **实验不足**：仅两个仿真任务，缺乏在更多动态动作、复杂地形、外部扰动下的测试。未进行消融研究分析关键超参数影响。
- **对比不够全面**：仅与纯RL对比，未与标准MPPI（无RL先验）、其他混合控制方法（如MPC+RL）或模型MPC比较，因此无法证明所提方法的综合优势。
- **泛化性疑问**：行为受限于RL先验的范围，当需要大幅偏离先验行为时（如学习新技能），框架可能失效。作者也承认这一点。
- **无硬件实验**：只在仿真中验证，实际部署仍需处理模型误差、接触估计误差、同步延迟等问题。
- **对RL策略的依赖**：虽然不需要重新训练，但RL策略本身的质量对系统性能有决定性影响。若RL策略本身不稳定或存在严重缺陷，MPPI可能无法充分补偿。
- **缺乏统计严谨性**：直线行走实验仅展示单个轨迹和RMSE，未报告多次试验的均值和方差，可能存在偶然性。

（完）
