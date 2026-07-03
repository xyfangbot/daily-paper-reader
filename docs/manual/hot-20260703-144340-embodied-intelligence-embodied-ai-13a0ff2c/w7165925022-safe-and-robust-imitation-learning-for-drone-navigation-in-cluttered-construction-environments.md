---
title: Safe and Robust Imitation Learning for Drone Navigation in Cluttered Construction Environments
title_zh: 杂乱施工环境下无人机导航的安全且鲁棒模仿学习
authors: "Yun Seok Gwon, Heung Jin Oh"
date: 2026-06-22
pdf: "https://www.iaarc.org/./publications/fulltext/ISARC2026_1456.pdf"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:covariant"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=covariant; relation_source=abstract; query=robot foundation model"
tldr: "杂乱建筑环境中的无人机导航面临非结构化障碍物和GPS缺失等挑战。本文提出结合残差策略学习和条件风险价值正则化的安全模仿学习框架。实验表明仅安全损失塑形无法解决协变量偏移，而引入DAgger数据聚合可学习有效恢复行为，导航成功率提升至80%。贡献在于证明了数据聚合而非安全正则化是实现稳健模仿学习的关键。"
source: openalex
selection_source: hot_paper_scout
motivation: 杂乱建筑环境中优化型规划器计算成本高且易陷入局部最优，需要轻量级策略。
method: 提出安全正则化模仿学习框架，集成残差策略学习、概率安全评判器和条件风险价值正则化，并结合DAgger数据聚合。
result: "在模拟杂乱建筑环境中，DAgger使导航成功率提升至80%，且安全裕度与专家规划器相当。"
conclusion: 数据集聚合（DAgger）是实现鲁棒模仿学习的关键因素，而安全正则化本身不足以解决协变量偏移。
---

## 摘要
在杂乱施工环境中进行自主导航极具挑战性，原因包括非结构化障碍物、GPS拒止条件以及机载计算的操作限制。基于优化的规划器（如协变哈密顿运动优化方法，CHOMP）具备避障能力，但由于计算成本高且对局部最小值敏感，通常不适用于高频控制。本研究探究了一种安全正则化的模仿学习框架，该框架融合了残差策略学习、提供概率风险估计的学习型安全评判器以及条件风险价值（CVaR）正则化。在程序化生成的PyBullet施工环境（具有密集脚手架和碎片）中进行系统评估后，我们发现仅靠面向安全的损失塑造不足以缓解行为克隆中的协变量偏移，导致尽管轨迹保守，但任务成功率仍较低。相比之下，引入数据集聚合（DAgger）使学习到的策略能够获得有效的恢复行为，将导航成功率提升至80%，同时保持与专家规划器相当的安全裕度。本研究的主要贡献在于通过实验证明，在杂乱施工环境中，数据集聚合（而非单独的安全正则化）对于鲁棒模仿学习至关重要。所提出的框架为将基于优化的规划器蒸馏为轻量级、响应式策略奠定了基础，适用于类施工环境中的模拟空中导航，而实际部署仍是未来工作。

## Abstract
Autonomous navigation in cluttered constructionenvironments is challenging due to unstructured obstacles, GPS-denied conditions, and operational constraints on onboard computation.Optimization-based planners such as Covariant Hamiltonian Optimization for Motion Planning (CHOMP) offer obstacle-avoidance capabilities but are often unsuitable for high-frequency control due to their computational cost and sensitivity to local minima.This study investigates a safety-regularized imitation learning framework that integrates residual policy learning, a learned safety critic providing probabilistic risk estimates, and Conditional Value-at-Risk (CVaR) regularization.Through systematic evaluation in a procedurally generated PyBullet construction environment featuring dense scaffolding and debris, we show that safety-oriented loss shaping alone is insufficient to mitigate covariate shift in behavioral cloning, resulting in low task success despite conservative trajectories.In contrast, incorporating Dataset Aggregation (DAgger) enables the learned policy to acquire effective recovery behaviors, improving navigation success to 80% while maintaining safety margins comparable to the expert planner.The primary contribution of this work is an empirical demonstration that dataset aggregation, rather than safety regularization alone, is critical for robust imitation learning in cluttered construction environments.The proposed framework provides a foundation for distilling optimization-based planners into lightweight, reactive policies suitable for simulated aerial navigation in construction-like environments, while real-world deployment remains future work.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- **研究背景**：施工环境（如脚手架、散落杂物等）杂乱、非结构化且GPS拒止，给无人机自主导航带来严峻挑战。
- **核心问题**：传统的优化型运动规划器（如CHOMP）虽能生成可行轨迹，但计算成本高，难以满足无人机高频控制（通常>50Hz）需求；而简单的行为克隆（BC）模仿学习易受协变量偏移影响，导致策略在未见状态下失效。
- **研究动机**：探索一种安全正则化的模仿学习框架，将重计算量的专家规划器蒸馏为轻量级、响应式的神经网络策略，同时解决协变量偏移和安全隐患。
- **整体含义**：本文旨在证明，在杂乱施工环境中，数据集聚合（DAgger）比单纯的安全损失正则化对实现鲁棒模仿学习更为关键。

## 二、论文提出的方法论

- **核心思想**：构建一个安全正则化的模仿学习框架，结合残差策略学习、学习型安全评判器和风险敏感损失函数，并通过DAgger算法解决协变量偏移。
- **关键技术细节与流程**：
    1. **残差策略学习（Residual Policy Learning, RPL）**：最终控制指令为 `u_t = v_curr + π_θ(f(s_t)) + u_z_PID`，即当前速度加上所学神经网络预测的xy平面速度增量，外加固定PID高度控制器。
    2. **特征提取网络**：将LiDAR原始点云转换为局部占据网格，再处理成7×7的欧几里得符号距离场（ESDF）patch，与当前速度向量、目标偏差向量拼接作为策略网络输入。策略网络为MLP（256×256，LeakyReLU激活）。
    3. **学习型安全评判器（Safety Critic）**：训练一个神经网络来近似状态风险值，其真值定义为 `R_gt(s) = exp(-γ · d_min)`，其中 `d_min` 为LiDAR最小测距。评判器网络结构与策略网络相似，输出经Sigmoid激活的[0,1]标量，通过MSE损失训练。
    4. **损失函数（安全正则化损失）**：`L_total = BC损失 + λ1 × E[屏障成本] + λ2 × CVaR_0.1(屏障成本)`。其中屏障成本定义为 `B(s,u)= r_φ(s) · ||u_final||^2`（高风险状态下惩罚高速），CVaR项取batch内成本最高的10%的平均值。参数λ1=0.01，λ2=0.05。
    5. **DAgger算法流程**：
        - ① 使用CHOMP专家收集初始轨迹。
        - ② 在专家数据上预训练策略和安全评判器。
        - ③ 迭代：使用当前策略在环境中执行，收集学生状态。
        - ④ 查询专家在这些新状态下的最优动作。
        - ⑤ 将新的(状态, 动作)对加入数据集，重新训练策略和安全评判器。

## 三、实验设计

- **模拟环境**：使用PyBullet物理引擎搭建的“Construction Site”环境，面积22m×22m。包含15×15的脚手架网格（管径0.06m）、40个木质托盘、80个随机散落障碍物。无人机与目标常生成于脚手架内部或杂物堆上，场景具挑战性。
- **机器人与传感器模型**：模拟四旋翼（半径0.18m，半径0.18m），搭载LiDAR传感器（10m量程、72×5=360个射线、60Hz更新率）。输入为7×7 ESDF patch。
- **专家规划器**：基于CHOMP（协变哈密顿运动优化），轨迹代价函数包含障碍项、光滑项和吸引项，参数 `k_att=1.5`，`k_rep=0.8`。
- **对比方法（五组基线）**：
    1. **Teacher (CHOMP)**：优化型专家规划器，100%成功率。
    2. **Vanilla BC**：仅在专家数据集上进行行为克隆。
    3. **BC + CVaR**：行为克隆基础上加入条件风险价值正则化。
    4. **BC + CVaR + CBF**：完整的损失函数（含安全评判器），但仅在静态专家数据集上训练。
    5. **Ours (BC + CVaR + CBF + DAgger)**：完整方法，含数据集聚合。

## 四、资源与算力

- **论文未明确提及**：文中没有报告使用了什么GPU型号、数量以及具体的训练时长。仅提到策略网络为两个256单元的MLP层，计算开销低。
- 仅提到“constant-time inference O(1)”，说明推理效率高，适合嵌入式硬件，但训练资源未被量化。

## 五、实验数量与充分性

- **实验数量**：每组方法均在15个评估episode上取平均结果。此外还展示了飞行日志（漂移模式分析）、平均急动度对比图、最小安全距离分布图。
- **充分性分析**：
    - **优点**：对比了从简单BC到完整DAgger的5种消融设置，清晰分离了安全正则化vs.数据集聚合的效果，实验设计有逻辑层次。
    - **不足**：
        - 每个条件仅15个episode，样本量偏少，可能存在随机性影响。
        - 未报告多次重复种子的统计结果（如标准差），实验结果可靠性待加强。
        - 仅在单一环境布局（脚手架+杂物）下评估，缺乏对不同杂乱程度或动态障碍物的测试。
        - 缺乏与更多模仿学习方法（如GAIL、扩散策略）的横向对比。

## 六、论文的主要结论与发现

- **核心发现1**：单纯的安全损失正则化（BC + CVaR + CBF，方法2-4）**无法解决协变量偏移**，尽管轨迹平滑（急动度低）且安全裕度高，但成功率<15%，主要失败模式为“漂移”导致无人机停住或超时。
- **核心发现2**：引入DAgger后，**导航成功率提升至80%**，策略学会了主动纠正错误，急动度从~7.8升至~30.2 m/s³，接近专家水平（42.4），说明鲁棒性需要主动校正行为，而被动保守策略难以胜任。
- **核心发现3**：带有DAgger的策略在安全裕度（最小间隙0.07m）上与专家（0.06m）相当，基本保持了专家级别的避碰性能。
- **结论**：在杂乱施工环境中，**数据集聚合（DAgger）是关键因素**，而安全正则化本身不足以解决分布偏移。

## 七、优点

- **实验设计清晰**：通过逐步添加组件（BC → CVaR → CBF → DAgger）进行消融，明确区分了安全正则化与数据聚合各自的作用。
- **环境逼真**：程序化生成的PyBullet环境能够模拟脚手架结构、散落杂物等真实施工场景，具有一定代表性。
- **框架完整**：残差策略学习、学习型安全评判器、CVaR正则化三者有机融合，形成了一套既考虑安全又解决协变量偏移的仿照学习框架。
- **有实际意义**：证明轻量级策略可以蒸馏重计算专家规划器，且保持可比的安全水平，对于嵌入式硬件部署有参考价值。

## 八、不足与局限

- **实验数量不足**：每个条件仅15个episode，没有报告多次重复种子的统计分布，结论的统计显著性存疑。
- **未与其他模仿学习方法对比**：未与GAIL、NC、扩散策略等常见RL方法对比，难以判断该方法是否超出SOTA。
- **静态世界假设**：当前方法假设障碍物静止，未考虑动态障碍（如移动工人、设备），离真实施工环境仍有差距。
- **缺乏形式化安全保证**：学习到的安全评判器仅提供概率估计，没有控制屏障函数（CBF）的严格不变性保证。
- **部署限制**：所有实验均基于PyBullet仿真，未涉及真实无人机硬件验证，方法在真实场景中的鲁棒性未知。
- **资源与算力不可复现**：未公开训练算力消耗（GPU型号/时长/批次大小），影响可复现性评估。

（完）
