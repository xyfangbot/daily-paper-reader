---
title: Safe and Robust Imitation Learning for Drone Navigation in Cluttered Construction Environments
title_zh: 杂乱建筑环境中无人机导航的安全鲁棒模仿学习
authors: "Yun Seok Gwon, Heung Jin Oh"
date: 2026-06-22
pdf: "https://www.iaarc.org/./publications/fulltext/ISARC2026_1456.pdf"
tags: ["query:热点论文筛选", "query:VLA方向", "query:具身智能公司相关", "paper:OpenAlex", "company:covariant"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=covariant; relation_source=abstract; query=robot foundation model action prediction"
tldr: "杂乱建筑环境中无人机自主导航面临非结构障碍、GPS缺失及计算限制，优化规划器如CHOMP虽能避障但计算成本高、易陷局部最优。本文提出安全正则化模仿学习框架，结合残差策略学习、概率安全批评器和条件风险价值正则化，并通过数据集聚合（DAgger）策略改进行为克隆（BC）。实验表明仅安全损失整形无法缓解BC的协变量偏移，而DAgger使导航成功率提升至80%且保持安全裕度。主要贡献在于实证证明数据集聚合而非安全正则化对鲁棒模仿学习至关重要，为将优化规划器蒸馏成轻量反应式策略奠定基础。"
source: openalex
selection_source: hot_paper_scout
motivation: 优化规划器难以满足杂乱建筑环境中高频控制需求，需轻量策略同时保证安全。
method: 采用安全正则化模仿学习，含残差策略、概率安全批评器及CVaR正则化，对比BC与DAgger训练。
result: "DAgger使成功率达80%，而仅安全正则化的BC成功率低，无法规避协变量偏移。"
conclusion: 数据集聚合是鲁棒模仿学习的关键，安全正则化单独不足，为轻量策略蒸馏提供实证基础。
---

## 摘要
由于非结构化障碍物、GPS受限条件以及机载计算的操作约束，在杂乱的建筑环境中进行自主导航极具挑战性。基于优化的规划器（如协变哈密顿运动规划优化算法CHOMP）具备避障能力，但由于计算成本高且对局部极小值敏感，通常不适合高频控制。本研究探讨了一种安全正则化的模仿学习框架，该框架集成了残差策略学习、提供概率风险估计的学习型安全评判器以及条件风险价值（CVaR）正则化。通过在程序化生成的、包含密集脚手架和碎片的PyBullet建筑环境中进行系统评估，我们发现仅靠面向安全的损失塑形不足以缓解行为克隆中的协变量偏移，尽管轨迹保守，但任务成功率较低。相比之下，融入数据集聚合（DAgger）使得学习到的策略能够获得有效的恢复行为，将导航成功率提升至80%，同时保持与专家规划器相当的安全裕度。本研究的主要贡献在于实证证明，在杂乱建筑环境中，数据集聚合而非单独的安全正则化对于鲁棒模仿学习至关重要。所提出的框架为将基于优化的规划器蒸馏为适用于类建筑环境模拟空中导航的轻量级反应式策略奠定了基础，而实际部署仍有待未来研究。

## Abstract
Autonomous navigation in cluttered constructionenvironments is challenging due to unstructured obstacles, GPS-denied conditions, and operational constraints on onboard computation.Optimization-based planners such as Covariant Hamiltonian Optimization for Motion Planning (CHOMP) offer obstacle-avoidance capabilities but are often unsuitable for high-frequency control due to their computational cost and sensitivity to local minima.This study investigates a safety-regularized imitation learning framework that integrates residual policy learning, a learned safety critic providing probabilistic risk estimates, and Conditional Value-at-Risk (CVaR) regularization.Through systematic evaluation in a procedurally generated PyBullet construction environment featuring dense scaffolding and debris, we show that safety-oriented loss shaping alone is insufficient to mitigate covariate shift in behavioral cloning, resulting in low task success despite conservative trajectories.In contrast, incorporating Dataset Aggregation (DAgger) enables the learned policy to acquire effective recovery behaviors, improving navigation success to 80% while maintaining safety margins comparable to the expert planner.The primary contribution of this work is an empirical demonstration that dataset aggregation, rather than safety regularization alone, is critical for robust imitation learning in cluttered construction environments.The proposed framework provides a foundation for distilling optimization-based planners into lightweight, reactive policies suitable for simulated aerial navigation in construction-like environments, while real-world deployment remains future work.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 研究动机：杂乱建筑环境中无人机自主导航面临非结构障碍、GPS缺失及机载计算资源有限等挑战，传统优化规划器如CHOMP虽能生成可行轨迹，但计算成本高、易陷入局部极小值，难以满足高频控制需求。
- 整体含义：提出一种安全正则化模仿学习框架，通过将优化规划器蒸馏为轻量神经策略，在保持安全性的同时实现实时反应式避障，重点验证数据集对齐机制（DAgger）相对于纯损失整形对鲁棒性的关键作用。

## 二、论文提出的方法论
- 核心思想：采用残差策略学习（RPL）架构，在经典标称控制器基础上叠加神经校正项；引入学习型安全评判器（Latent Safety Critic）近似控制障碍函数；使用条件风险价值（CVaR）增强对罕见碰撞案例的敏感性；并通过数据集聚合（DAgger）解决行为克隆的协变量偏移。
- 关键技术细节：
  - 残差策略：最终控制命令 `u_t = v_curr + π_θ(f(s_t)) + u_z_PID`，其中π_θ输出xy平面速度残差。
  - 特征提取：LiDAR点云转换为局部占据网格并生成7×7欧几里得符号距离场（ESDF）补丁，结合当前速度和目标方向向量作为输入。
  - 网络架构：策略网络为两层256单元MLP，激活函数LeakyReLU；安全评判器网络结构与策略相同，输出经Sigmoid激活的单一风险标量。
  - 安全评判器训练：真实风险 `R_gt(s)=exp(-γ·d_min)`，γ=2.0，通过MSE损失训练。
  - 总损失函数：`L_total = BC项 + λ1·E[Barrier] + λ2·CVaR_α(Barrier)`，Barrier成本定义为 `B(s,u)=r_φ(s)·‖u_final‖²`，λ1=0.01，λ2=0.05，α=0.1。
- 训练流程（DAgger）：
  1. 收集CHOMP专家轨迹。
  2. 预训练策略和安全评判器。
  3. 迭代式学生策略部署，收集新状态。
  4. 查询专家在这些状态下的最优动作。
  5. 将新数据加入数据集并重新训练。

## 三、实验设计
- 仿真环境：基于PyBullet的定制建筑工地环境，22m×22m区域，包含15×15网格脚手架（立杆和横杆半径0.06m）、40个木托盘、80个随机杂物（钢梁、圆柱、管道）。无人机和起点/目标位置常置于脚手架内部或杂物堆上。
- 传感器与机器人：四旋翼半径0.18m，模拟LiDAR范围10m，72方位×5俯仰层（共360射线），更新率60Hz，特征空间为7×7 ESDF补丁。
- 专家规划器：基于CHOMP，目标吸引增益k_att=1.5，障碍排斥增益k_rep=0.8。
- 对比方法：
  - 教师（CHOMP）：优化规划器基线。
  - Vanilla BC：标准行为克隆。
  - BC + CVaR：BC加风险敏感损失。
  - BC + CVaR + CBF：完整安全损失函数但使用静态专家数据。
  - 本文方法（BC + CVaR + CBF + DAgger）：完整框架。

## 四、资源与算力
- 论文未明确提及所使用的GPU型号、数量、训练时长等算力信息。仿真平台基于PyBullet，策略网络为两层MLP，推测计算需求较低，但具体硬件配置未报告。

## 五、实验数量与充分性
- 实验数量：每个方法在15个评估片段（episodes）上取平均结果，共5种方法，总计约75次评估。未提及训练/验证集划分或统计显著性检验。
- 充分性评价：
  - 优点：消融实验设计合理，逐步剔除DAgger、CVaR、CBF等组件，清晰显示各模块贡献；使用程序化生成环境增加场景多样性。
  - 不足：样本量较小（15 episodes），未报告多次随机种子下的统计波动；仅测试短程导航任务，未涉及长时间任务或多目标；环境仅限于模拟PyBullet，未验证真实场景泛化性。

## 六、论文的主要结论与发现
- 仅靠安全正则化损失整形（CVaR + CBF）无法缓解行为克隆中的协变量偏移，静态专家数据训练的方法成功率低于15%，尽管轨迹平滑、安全裕度高，但策略倾向于被动漂移或冻结。
- 引入DAgger后成功率提升至80%，同时最小间隙保持0.07m与教师相当，但轨迹抖动（jerk）显著增加（从7.8升至30.2 m/s³），表明主动校正行为替代了保守被动策略。
- 主要结论：数据集聚合（分布对齐机制）是杂乱建筑环境中鲁棒模仿学习的关键，安全正则化单独不足以解决分布偏移问题。

## 七、优点
- 方法设计亮点：将控制障碍函数（CBF）思想转化为可学习的安全评判器，直接从LiDAR观测输出概率风险估计，无需显式建模；采用残差策略保持名义控制器的基础行为，降低学习难度；CVaR损失聚焦极端情况，增强鲁棒性。
- 实验设计亮点：逐步消融实验清晰揭示了DAgger的关键作用；程序化生成场景增加了环境结构变异性，提升了结论可信度。
- 框架实用性：推理常数的复杂度适合部署于机载嵌入式设备，且不依赖视觉纹理，仅使用深度特征，有利于sim-to-real迁移。

## 八、不足与局限
- 实验覆盖有限：仅测试模拟环境PyBullet，未涉及真实世界无人机实验；环境仅包含静态障碍物，未考虑动态障碍（如移动设备、人员）；任务为短程单目标导航，未评估多目标或复杂任务。
- 偏差风险：每个方法仅评估15次，未报告置信区间，统计可靠性存疑；教师规划器本身存在局部极小问题，可能引入偏见；学生策略在DAgger训练后jerk较高，可能对机体机械造成负担，未评估机械性能影响。
- 安全保证局限：学习型安全评判器仅提供概率估计，不具备形式化安全保证；CVaR项在模型训练中可能无法充分覆盖所有极端情况。
- 实际部署障碍：未考虑建筑工地的灰尘、遮挡、传感器噪声以及BIM信息融合；未讨论与施工工作流（进度监测、安全检查）的集成。

（完）
