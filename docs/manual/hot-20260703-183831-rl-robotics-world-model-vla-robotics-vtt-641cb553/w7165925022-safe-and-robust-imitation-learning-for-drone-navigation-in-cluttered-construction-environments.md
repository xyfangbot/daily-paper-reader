---
title: Safe and Robust Imitation Learning for Drone Navigation in Cluttered Construction Environments
title_zh: 杂乱建筑环境中无人机导航的安全稳健模仿学习
authors: "Yun Seok Gwon, Heung Jin Oh"
date: 2026-06-22
pdf: "https://www.iaarc.org/./publications/fulltext/ISARC2026_1456.pdf"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:covariant"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=covariant; relation_source=abstract; query=reinforcement learning for drone navigation in dynamic environments"
tldr: "在杂乱建筑环境中，无人机自主导航面临非结构化障碍和GPS缺失等挑战，优化规划器如CHOMP虽能避障但计算成本高且易陷入局部极小。本文提出一种安全正则化模仿学习框架，结合残差策略学习、概率安全批评器和CVaR正则化，并通过DAgger数据集聚合训练。实验表明，仅靠安全损失整形无法缓解协变量偏移，导致任务成功率低；而引入DAgger后策略学会有效恢复行为，导航成功率提升至80%，同时保持与专家相当的安全裕度。核心贡献是实证发现数据集聚合而非安全正则化是鲁棒模仿学习的关键，为将优化规划器蒸馏为轻量反应式策略奠定了基础。"
source: openalex
selection_source: hot_paper_scout
motivation: 优化规划器难以满足高频控制需求，模仿学习面临协变量偏移，需探究安全正则化与数据聚合对鲁棒导航的影响。
method: 提出融合残差策略学习、概率安全批评器与CVaR正则化的模仿学习框架，并采用DAgger进行交互式数据聚合训练。
result: "单纯安全正则化导致低任务成功率；加入DAgger后策略获得恢复能力，导航成功率80%，安全裕度与专家规划器相当。"
conclusion: 数据集聚合是杂乱环境下鲁棒模仿学习的关键，为将优化规划器蒸馏为轻量反应式策略提供了有效基础。
---

## 摘要
在杂乱建筑环境中进行自主导航面临挑战，原因包括非结构化障碍物、GPS拒止条件以及机载计算的操作约束。基于优化的规划器（如协变哈密顿优化运动规划（CHOMP））具备避障能力，但由于计算成本高且对局部极小值敏感，通常不适合高频控制。本研究探索了一种安全正则化的模仿学习框架，该框架融合了残差策略学习、提供概率风险估计的学习安全评判器以及条件风险价值（CVaR）正则化。通过在程序生成的PyBullet建筑环境（包含密集脚手架和碎片）中进行系统评估，我们表明仅依靠面向安全的损失塑造不足以缓解行为克隆中的协变量偏移，尽管轨迹保守，但任务成功率较低。相比之下，引入数据集聚合（DAgger）使学习到的策略能够获得有效的恢复行为，将导航成功率提升至80%，同时保持与专家规划器相当的安全裕度。本研究的主要贡献在于通过实证表明，对于杂乱建筑环境中的稳健模仿学习，数据集聚合（而非单独的安全正则化）至关重要。所提出的框架为将基于优化的规划器提炼成轻量级、反应性策略奠定了基础，适用于类似建筑环境中的模拟空中导航，而实际部署仍有待未来工作。

## Abstract
Autonomous navigation in cluttered constructionenvironments is challenging due to unstructured obstacles, GPS-denied conditions, and operational constraints on onboard computation.Optimization-based planners such as Covariant Hamiltonian Optimization for Motion Planning (CHOMP) offer obstacle-avoidance capabilities but are often unsuitable for high-frequency control due to their computational cost and sensitivity to local minima.This study investigates a safety-regularized imitation learning framework that integrates residual policy learning, a learned safety critic providing probabilistic risk estimates, and Conditional Value-at-Risk (CVaR) regularization.Through systematic evaluation in a procedurally generated PyBullet construction environment featuring dense scaffolding and debris, we show that safety-oriented loss shaping alone is insufficient to mitigate covariate shift in behavioral cloning, resulting in low task success despite conservative trajectories.In contrast, incorporating Dataset Aggregation (DAgger) enables the learned policy to acquire effective recovery behaviors, improving navigation success to 80% while maintaining safety margins comparable to the expert planner.The primary contribution of this work is an empirical demonstration that dataset aggregation, rather than safety regularization alone, is critical for robust imitation learning in cluttered construction environments.The proposed framework provides a foundation for distilling optimization-based planners into lightweight, reactive policies suitable for simulated aerial navigation in construction-like environments, while real-world deployment remains future work.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 建筑工地环境杂乱（狭窄走廊、悬挂脚手架、散落碎片等）、GPS拒止，标准全局规划器难以应用，需要轻量级反应式控制器。
- 优化规划器（如CHOMP）能生成可行轨迹，但计算成本高且易陷入局部极小，不适合高频控制（>50 Hz）。
- 模仿学习（IL）可用于将重型规划器蒸馏为轻量神经网络策略，但标准行为克隆（BC）存在协变量偏移问题，且会继承专家靠近障碍物的“擦边”行为。
- 本研究旨在探索安全正则化（CBF、CVaR）能否单独解决协变量偏移，并验证数据集聚合（DAgger）的关键作用。

## 二、论文提出的方法论
- **核心思想**：提出安全正则化模仿学习框架，结合残差策略学习、学习的安全批评器（近似控制障碍函数）和CVaR风险敏感损失，并通过DAgger对齐状态分布。
- **关键技术细节**：
  - **残差策略学习**：最终控制命令 = 当前速度 + 神经网络预测的Δv(xy平面) + 固定PID高度控制，输入为7×7 ESDF补丁(49维)、当前速度(3维)、目标方向矢量(3维)。
  - **安全批评器**：基于LiDAR特征训练神经网络 \( r_{\phi}(s) \)，输出状态风险（0~1），真实标签为 \( R_{gt}(s) = \exp(-\gamma \cdot d_{\min}) \)（γ=2.0），使用MSE训练。
  - **损失函数**：\( L_{\text{total}} = \text{BC项} + \lambda_1 \mathbb{E}[B(s,u)] + \lambda_2 \text{CVaR}_{0.1}(B(s,u)) \)，其中障碍成本 \( B(s,u) = r_{\phi}(s) \cdot \| u_{\text{final}} \|^2 \)，\(\lambda_1=0.01, \lambda_2=0.05\)。
  - **DAgger流程**：初始用CHOMP收集专家数据→预训练策略和安全批评器→迭代使用学生策略 rollout→在访问的新状态上查询专家动作→聚合数据并重新训练。

## 三、实验设计
- **环境**：基于PyBullet定制的“Construction Site”模拟环境，面积22m×22m，包含15×15脚手架网格（间距1m）、40个木托盘和80个随机碎片，无人机和起点/目标随机生成在脚手架内部或碎片堆上。
- **传感器与机器人**：模拟四旋翼（半径0.18m），LiDAR 72个方位角×5个仰角层（共360条射线），范围10m，60Hz。状态表示为7×7 ESDF补丁（无相机输入）。
- **专家规划器**：CHOMP，参数 \( k_{\text{att}}=1.5, k_{\text{rep}}=0.8 \)。
- **对比方法**：共5个基线（均基于15个评估回合的平均值）：
  1. Teacher (CHOMP)：优化专家。
  2. Vanilla BC：纯行为克隆。
  3. BC + CVaR：加风险敏感损失。
  4. BC + CVaR + CBF：完整损失函数但无DAgger（静态专家数据）。
  5. Ours (BC + CVaR + CBF + DAgger)：完整方法。

## 四、资源与算力
- 论文未明确报告使用的GPU型号、数量或训练时长。仅提及“在模拟中训练”，未提供计算资源细节。

## 五、实验数量与充分性
- **实验数量**：每个方法在15个评估回合上报告了成功率、平均加加速度和最小安全距离。此外，有加加速度对比图和最小距离分布图（图4、图5）。
- **消融研究**：通过逐步添加CVaR、CBF、DAgger组件进行了系统性消融，对比了5个变体。
- **充分性与公平性**：
  - 实验覆盖了不同安全正则化组合，并明确对比了有无DAgger的差异，结论清晰。
  - 但仅使用15个回合，随机性可能较大（特别是低成功率方法），且未提供置信区间或统计显著性检验。
  - 环境是程序化生成，但未跨不同场景种子进行系统验证，泛化性验证不足。

## 六、论文的主要结论与发现
- **安全正则化单独不足**：仅靠BC+CVaR+CBF在静态专家数据上训练，成功率低于15%，虽然轨迹平滑且安全边际高（>0.3m），但失败源于协变量偏移（策略在未访问状态缺乏纠正行为）。
- **DAgger是关键**：加入DAgger后成功率提升至80%，同时加加速度从7.8增加到30.2 m/s³（表明从保守被动变为积极纠正），最小安全距离接近专家（0.07m vs 0.06m）。
- **神经网络过滤优化噪声**：DAgger策略的加加速度（30.2）低于专家（42.4），表明网络平滑了CHOMP的高频振荡。
- 数据集聚合（而非单纯安全损失）是杂乱环境下鲁棒模仿学习的核心驱动因素。

## 七、优点
- 实验设计清晰，系统消融了CVaR、CBF和DAgger各自贡献，结论有说服力。
- 方法设计合理：残差策略保留标称控制器的基座，安全批评器将CBF思想扩展到点云输入，CVaR侧重最危险情况。
- 在程序化生成的杂乱场景中进行评估，环境复杂性较高（脚手架网格+碎片），贴近真实建筑工地。
- 明确指出“安全正则化不足以解决分布偏移”这一反直觉发现，具有实践指导意义。
- 讨论了从优化规划器蒸馏为轻量策略的部署前景（O(1)推理）。

## 八、不足与局限
- **实验充分性**：仅15个评估回合，低成功率方法的统计误差可能较大；未报告多次重复或置信区间。
- **场景覆盖**：环境为程序化生成，但未在不同随机种子上系统评估泛化性；仅包含静态障碍，未验证动态障碍。
- **安全保证**：学习的安全批评器仅提供概率估计，不具备形式化控制-理论安全保证；最小安全距离0.07m接近碰撞，实际部署风险高。
- **未使用真实世界数据**：所有实验在PyBullet模拟中进行，未涉及物理无人机或真实建筑工地，sim-to-real差距未探讨。
- **计算资源缺失**：未报告训练所用GPU型号、训练时长，影响可复现性评估。
- **专家依赖**：依赖CHOMP专家的完美演示，但在真实复杂环境中构建高质量专家示范本身具有难度。

（完）
