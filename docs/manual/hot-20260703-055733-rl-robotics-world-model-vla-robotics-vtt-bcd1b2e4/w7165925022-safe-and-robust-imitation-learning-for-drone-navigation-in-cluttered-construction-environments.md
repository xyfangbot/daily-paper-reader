---
title: Safe and Robust Imitation Learning for Drone Navigation in Cluttered Construction Environments
title_zh: 杂乱建筑环境中无人机导航的安全稳健模仿学习
authors: "Yun Seok Gwon, Heung Jin Oh"
date: 2026-06-22
pdf: "https://www.iaarc.org/./publications/fulltext/ISARC2026_1456.pdf"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:covariant"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=covariant; relation_source=abstract; query=reinforcement learning for drone navigation in dynamic environments"
tldr: "在杂乱建筑环境中，无人机自主导航面临非结构化障碍和GPS拒止挑战，基于优化的运动规划器计算成本高且易陷入局部最优。本文提出一种安全正则化模仿学习框架，结合残差策略学习、安全评判器和条件风险价值正则化。实验表明，仅靠安全导向的损失整形无法有效缓解行为克隆的协变量偏移，而引入数据集聚合（DAgger）后策略成功学习恢复行为，导航成功率提升至80%且安全边际与专家相当。核心贡献在于实证证明数据集聚合而非安全正则化本身对鲁棒模仿学习的关键作用。"
source: openalex
selection_source: hot_paper_scout
motivation: 优化规划器不适用于高频控制，行为克隆因协变量偏移在杂乱环境中成功率低，需探索安全正则化与交互式学习的结合。
method: 构建安全正则化模仿学习框架，含残差策略、安全评判器和CVaR正则化，并对比行为克隆与DAgger训练策略。
result: "仅安全损失整形无法提升行为克隆成功率；DAgger将成功率从低水平提升至80%，安全边际与专家相当。"
conclusion: 数据集聚合是实现杂乱环境鲁棒模仿学习的核心，安全正则化单独作用有限。
---

## 摘要
在杂乱建筑环境中进行自主导航具有挑战性，原因在于非结构化障碍物、GPS拒止条件以及机载计算的操作限制。基于优化的规划器（如协变哈密顿运动优化，CHOMP）提供了避障能力，但由于计算成本高且对局部极小值敏感，通常不适合高频控制。本研究探讨了一种安全正则化的模仿学习框架，该框架整合了残差策略学习、提供概率风险估计的学习型安全评判器以及条件风险价值（CVaR）正则化。通过在程序生成的PyBullet建筑环境（具有密集脚手架和碎片）中进行系统评估，我们发现仅依靠面向安全的损失整形不足以缓解行为克隆中的协变量偏移，尽管轨迹保守，但任务成功率仍然较低。相比之下，引入数据集聚合（DAgger）使学习到的策略能够获得有效的恢复行为，将导航成功率提升至80%，同时保持与专家规划器相当的安全裕度。本工作的主要贡献在于：通过实证表明，数据集聚合（而非单纯的安全正则化）对于杂乱建筑环境中的稳健模仿学习至关重要。所提出的框架为将基于优化的规划器提炼为轻量级、反应式策略奠定了基础，这些策略适用于类似建筑环境的模拟空中导航，而实际部署仍有待未来工作。

## Abstract
Autonomous navigation in cluttered constructionenvironments is challenging due to unstructured obstacles, GPS-denied conditions, and operational constraints on onboard computation.Optimization-based planners such as Covariant Hamiltonian Optimization for Motion Planning (CHOMP) offer obstacle-avoidance capabilities but are often unsuitable for high-frequency control due to their computational cost and sensitivity to local minima.This study investigates a safety-regularized imitation learning framework that integrates residual policy learning, a learned safety critic providing probabilistic risk estimates, and Conditional Value-at-Risk (CVaR) regularization.Through systematic evaluation in a procedurally generated PyBullet construction environment featuring dense scaffolding and debris, we show that safety-oriented loss shaping alone is insufficient to mitigate covariate shift in behavioral cloning, resulting in low task success despite conservative trajectories.In contrast, incorporating Dataset Aggregation (DAgger) enables the learned policy to acquire effective recovery behaviors, improving navigation success to 80% while maintaining safety margins comparable to the expert planner.The primary contribution of this work is an empirical demonstration that dataset aggregation, rather than safety regularization alone, is critical for robust imitation learning in cluttered construction environments.The proposed framework provides a foundation for distilling optimization-based planners into lightweight, reactive policies suitable for simulated aerial navigation in construction-like environments, while real-world deployment remains future work.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 建筑工地环境具有动态、危险、杂乱的特点（如窄走廊、悬挂脚手架、散落的钢梁和管道），对无人机自主导航构成巨大挑战。
- 标准GPS导航和地图驱动的全局规划器在此类环境中效果不佳，而基于优化的运动规划器（如CHOMP）虽然可行，但计算成本高、易陷入局部极小值，难以满足无人机高频控制（>50 Hz）需求。
- 模仿学习（IL）被视为将重型规划器蒸馏为轻量级反应式策略的替代方案，但行为克隆（BC）存在严重的协变量偏移问题：累积的小误差将机器人推向未见过的状态，而学生策略在这些状态下无法有效行动。
- 核心研究问题：是否可以通过安全正则化的损失函数（如控制障碍函数CBF和条件风险价值CVaR）在静态专家数据上训练出安全的模仿学习策略？还是必须依赖数据集聚合（DAgger）来解决分布偏移？

## 二、论文提出的方法论
- 核心思想：构建一个安全正则化的模仿学习框架，将残差策略学习、学习型安全评判器（安全批评器）和风险敏感性损失相结合，并引入DAgger迭代数据聚合。
- **系统架构**：由全局规划器（提供目标）、局部专家规划器（CHOMP）和学习型学生策略组成。学生策略处理原始LiDAR数据和状态信息以生成速度命令。
- **残差策略学习（RPL）**：最终控制命令为`u_t = v_curr + π_θ(f(s_t)) + u_z_PID`，即当前速度加上神经网络预测的xy平面delta-速度校正，加上固定PID高度维持。输入特征包括7×7 ESDF补丁（49维）、当前速度向量（3维）和目标增量向量（3维）。网络为两层256单元MLP，LeakyReLU激活。
- **学习型安全批评器（Safety Critic）**：神经网络`r_φ(s)`近似风险状态，使用LiDAR最小距离的指数衰减`R_gt(s) = exp(-γ·d_min)`（γ=2.0）作为真值，通过MSE损失训练。
- **损失函数**：`L_total = BC损失 + λ1·E[B(s,u)]（平均壁垒成本） + λ2·CVaR_α(B(s,u))（顶部10%壁垒成本均值）`。壁垒成本`B(s,u) = r_φ(s)·||u_final||²`，在估计风险高时惩罚高动能。超参数λ1=0.01，λ2=0.05。
- **训练流程（DAgger）**：1) 使用CHOMP专家收集初始轨迹；2) 在专家数据上预训练π_θ和r_φ；3) 迭代执行学生策略收集新状态，并在这些新状态上查询专家最优动作；4) 将新数据对添加到数据集中并重新训练。

## 三、实验设计
- **模拟环境**：使用PyBullet物理引擎，构建22m×22m“Construction Site”环境，包含15×15网格脚手架（垂直立柱和水平管道）、40个木质托盘和80个随机碎片（钢梁、圆筒、管道）。无人机和起点/终点常生成在脚手架内部或碎片堆上。
- **传感器与机器人**：模拟四旋翼（半径0.18m），LiDAR传感器：10米范围、72方位×5仰角共360条射线、60Hz更新率。特征空间为7×7 ESDF补丁。
- **专家规划器**：基于CHOMP，使用ESDF梯度最小化`U(traj) = w_obs·U_obs + w_smooth·U_smooth + w_att·U_att`，参数`k_att=1.5`，`k_rep=0.8`。
- **对比基线**：1) 教师（CHOMP）专家；2) 基础行为克隆（Vanilla BC）；3) BC + CVaR；4) BC + CVaR + CBF（全损失函数在静态专家数据上训练）；5) 全方法 + DAgger（本文方法）。
- **评估指标**：成功率、平均Jerk（平滑度，m/s³）、最小安全距离（安全裕度，m）。

## 四、资源与算力
- 论文中**未明确提及**所使用的GPU型号、数量、训练时长或任何具体算力资源指标。
- 由于模拟环境基于PyBullet，策略网络为小型MLP（2个隐藏层，每层256单元），可以推断该实验的计算需求相对适中，但未提供量化数据。

## 五、实验数量与充分性
- **实验数量**：每个方法在15个评估episode上取平均值。此样本量（n=15）对于统计显著性而言偏小，可能不足以捕捉性能的全面分布。
- **消融实验**：覆盖了从基础BC到完整方法（全损失+DAgger）的5个系统消融步骤，对比清晰，能够有效分离每个组件（CVaR、CBF、DAgger）的贡献。
- **公平性**：所有基线在相同的模拟环境和起始/目标分布下测试，评估标准一致。但是，未报告置信区间或统计显著性检验（如t检验），且未进行多次随机种子实验，实验的充分性存在一定局限。
- **场景多样性**：环境生成是程序化的，但评估集中于单一类型的杂乱布局（密集型脚手架+碎片），缺少对跨场景泛化能力的测试。

## 六、论文的主要结论与发现
- **核心结论**：数据集聚合（DAgger）是解决杂乱环境中模仿学习鲁棒性的关键因素，单纯的安全正则化损失整形不足以克服协变量偏移。
- **具体发现**：
    - 静态数据训练的方法（Vanilla BC、BC+CVaR、BC+CVaR+CBF）成功率极低（<15%），尽管轨迹平滑且安全裕度大，但失败模式为“漂移冻结”或超时。
    - 引入DAgger后，策略学会主动恢复行为，成功率提升至80%，安全裕度（0.07m）与专家（0.06m）相当，但Jerk显著增加（从7.8增至30.2 m/s³），反映出从被动保守行为到主动纠错的转变。
    - 学习到的策略有效过滤了专家规划器的高频优化噪声（Jerk从42.4降至30.2），在保持轨迹意图的同时更平滑。

## 七、优点
- **实证对比清晰**：系统性地展示了安全正则化（CVaR+CBF）与数据聚合（DAgger）各自的独立作用，揭示了“损失整形”与“分布对齐”之间的关键差异，具有重要的实践指导意义。
- **有意义的负面结果与见解**：明确指出“安全损失无法替代交互式数据收集”，发现保守行为源于协变量偏移而非策略过于激进，这一洞见对相关领域有启发价值。
- **方法组合合理**：将残差策略学习、学习型CBF和CVaR风险敏感损失有机融合，结构理论上合理，为轻量级策略蒸馏提供了可行的技术方案。
- **应用场景聚焦**：针对建筑工地这一特殊且具有挑战性的环境，提供了针对性的解决方案和性能基准。

## 八、不足与局限
- **实验局限性**：仅使用15个episode评估，样本量小，缺乏统计显著性检验和多次随机种子实验，结果的稳定性和可推广性存疑。
- **环境抽象简化**：ESDF假设静态世界，未考虑动态障碍物（如移动设备、工人）；LiDAR传感器在模拟中理想化，未模拟真实工地常见的灰尘、遮挡、噪声等退化条件。环境仅覆盖“密集型脚手架+碎片”场景，泛化性有限。
- **模拟到现实鸿沟**：论文明确承认实验仅在PyBullet模拟中进行，未进行真实无人机部署，所有结论仅限于模拟环境。
- **安全保证不严格**：学习型CBF只提供概率性风险估计，无法提供控制理论上的正式安全保证（无形式化验证）。
- **理论分析缺失**：未讨论为何安全正则化在静态数据上无效的理论原因（如梯度消失、损失景观），也未分析DAgger在嘈杂环境中的安全性保证。
- **计算资源未报告**：未提供任何算力资源指标（GPU类型、训练时间、内存消耗），不利于复现和资源评估。
- **未考虑多模态或多任务**：仅关注单一导航任务（从起点到终点），未探索在真实工地中的多任务能力（如进展监控、安全巡检）。

（完）
