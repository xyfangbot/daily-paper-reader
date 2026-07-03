---
title: Safe and Robust Imitation Learning for Drone Navigation in Cluttered Construction Environments
title_zh: 杂乱建筑环境中无人机导航的安全鲁棒模仿学习
authors: "Yun Seok Gwon, Heung Jin Oh"
date: 2026-06-22
pdf: "https://www.iaarc.org/./publications/fulltext/ISARC2026_1456.pdf"
tags: ["query:热点论文筛选", "query:VLA方向", "query:具身智能公司相关", "paper:OpenAlex", "company:covariant"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=covariant; relation_source=abstract; query=robot foundation model action prediction"
tldr: "无人机在杂乱建筑环境中的自主导航面临非结构化障碍、GPS缺失和计算资源受限等挑战。优化规划器如CHOMP虽能避障，但计算成本高且易陷入局部最优。本研究提出安全正则化模仿学习框架，融合残差策略学习、概率安全批判和CVaR正则化，并引入DAgger数据集聚合。实验表明，仅靠安全损失约束无法缓解行为克隆的协变量偏移，任务成功率低；而加入DAgger后，策略学会有效恢复行为，导航成功率达80%，同时保持安全裕度。核心贡献在于实证证明数据集聚合而非安全正则化本身是实现鲁棒模仿学习的关键，为将优化规划器蒸馏为轻量级反应式策略奠定了基础。"
source: openalex
selection_source: hot_paper_scout
motivation: 优化规划器不适用于高频控制，而模仿学习在杂乱建筑环境易因协变量偏移导致失败，需探索安全正则化与数据聚合的结合效果。
method: 构建安全正则化模仿学习框架，包含残差策略学习、概率安全批判提供风险估计及CVaR正则化，并通过DAgger迭代收集专家数据以缓解分布偏移。
result: "DAgger使导航成功率从低值提升至80%，且安全裕度接近专家；而仅用安全损失正则化的策略轨迹保守但任务成功低。"
conclusion: 数据集聚合是提升模仿学习在杂乱建筑环境中鲁棒性的关键，为轻量级无人机自主导航策略的蒸馏提供了实证基础。
---

## 摘要
在杂乱建筑环境中实现自主导航具有挑战性，原因在于非结构化障碍物、无GPS条件以及机载计算的操作限制。基于优化的规划器（如用于运动规划的协变哈密顿优化，CHOMP）具备避障能力，但由于计算成本高且对局部极小值敏感，通常不适用于高频控制。本研究探索了一种安全正则化的模仿学习框架，该框架融合了残差策略学习、提供概率风险评估的学习安全批评器以及条件风险价值（CVaR）正则化。在程序化生成的PyBullet建筑环境中（包含密集脚手架与碎片）进行系统评估后，我们发现：仅靠面向安全的损失塑造不足以缓解行为克隆中的协变量偏移，尽管轨迹保守，但仍导致任务成功率低。相比之下，引入数据集聚合（DAgger）使学习策略能够获得有效的恢复行为，将导航成功率提升至80%，同时保持与专家规划器相当的安全裕度。本研究的主要贡献在于通过实证表明：在杂乱建筑环境中，实现鲁棒模仿学习的关键在于数据集聚合，而非单纯的安全正则化。所提出的框架为将基于优化的规划器蒸馏为轻量级、反应式策略奠定了基础，适用于类建筑环境中的模拟空中导航，而实际部署仍有待未来研究。

## Abstract
Autonomous navigation in cluttered constructionenvironments is challenging due to unstructured obstacles, GPS-denied conditions, and operational constraints on onboard computation.Optimization-based planners such as Covariant Hamiltonian Optimization for Motion Planning (CHOMP) offer obstacle-avoidance capabilities but are often unsuitable for high-frequency control due to their computational cost and sensitivity to local minima.This study investigates a safety-regularized imitation learning framework that integrates residual policy learning, a learned safety critic providing probabilistic risk estimates, and Conditional Value-at-Risk (CVaR) regularization.Through systematic evaluation in a procedurally generated PyBullet construction environment featuring dense scaffolding and debris, we show that safety-oriented loss shaping alone is insufficient to mitigate covariate shift in behavioral cloning, resulting in low task success despite conservative trajectories.In contrast, incorporating Dataset Aggregation (DAgger) enables the learned policy to acquire effective recovery behaviors, improving navigation success to 80% while maintaining safety margins comparable to the expert planner.The primary contribution of this work is an empirical demonstration that dataset aggregation, rather than safety regularization alone, is critical for robust imitation learning in cluttered construction environments.The proposed framework provides a foundation for distilling optimization-based planners into lightweight, reactive policies suitable for simulated aerial navigation in construction-like environments, while real-world deployment remains future work.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：无人机在杂乱建筑环境中自主导航面临三大挑战：非结构化障碍物（脚手架、碎片等）、GPS信号缺失、机载计算资源受限。优化型运动规划器（如CHOMP）虽能避障，但因计算成本高、易陷入局部极小值，难以满足无人机高频（>50Hz）控制需求。
- **核心问题**：如何利用模仿学习将重型优化规划器蒸馏为轻量级反应式策略，同时保证安全性与鲁棒性？标准行为克隆易因协变量偏移（covariate shift）导致失败，且直接模仿专家可能继承其危险边界行为。
- **整体含义**：本文通过实证表明，仅靠安全正则化损失（如CVaR、CBF）无法弥补分布偏移，而数据集聚合（DAgger）是提升鲁棒性的关键。这为将优化规划器转化为适用于实际部署的轻量级策略提供了基础。

## 二、论文提出的方法论
- **核心思想**：构建安全正则化的模仿学习框架，由三部分组成：残差策略学习、学习型安全批评器（近似控制障碍函数）、基于条件风险价值（CVaR）的风险敏感损失。关键创新在于通过DAgger迭代聚合专家在策略诱导状态下的标签，缓解分布偏移。
- **关键技术细节**：
  - **残差策略学习（RPL）**：最终控制命令为当前速度 \(v_{curr}\) 加上策略输出的增量修正 \(\pi_\theta(s)\)（xy平面），再加上固定PID高度控制 \(u_z^{PID}\)：\(u_t = v_{curr} + \pi_\theta(f(s_t)) + u_z^{PID}\)。
  - **特征提取**：将LiDAR点云栅格化为局部占据网格，再转换为7×7的欧几里得符号距离场（ESDF）patch，与当前速度向量（3维）和目标差值向量（3维）拼接构成输入。
  - **网络架构**：策略网络为两层MLP（每层256个神经元），激活函数LeakyReLU（斜率0.2）；安全批评器结构相同，输出通过Sigmoid映射到[0,1]。
  - **安全批评器训练**：以真实风险 \(R_{gt}(s) = \exp(-\gamma \cdot d_{min})\)（γ=2.0）为目标，通过MSE损失训练。
  - **损失函数**：总损失 = 行为克隆损失 + λ₁×屏障损失均值 + λ₂×CVaR₀.₁（屏障损失 = 批评器输出×动作范数平方）。λ₁=0.01，λ₂=0.05。
  - **DAgger流程**：先收集专家演示 → 预训练策略与批评器 → 学生策略在环境中 rollout → 在每个学生状态查询专家最优动作 → 将新数据加入数据集重新训练。
- **公式/算法逻辑**：未直接列出完整算法伪代码，但文字描述了上述流程。

## 三、实验设计
- **仿真环境**：基于PyBullet自建“Construction Site”环境，面积22m×22m，包含15×15网格脚手架（钢管半径0.06m）、40个木托盘、80个随机碎片（钢梁、圆柱、管道）。无人机与目标常随机生成在脚手架内部或碎片堆上。
- **传感器与机器人**：模拟四旋翼（半径0.18m），LiDAR：10米范围，72方位×5高度层（共360射线），60Hz更新率；特征空间为7×7 ESDF patch（不使用相机）。
- **专家规划器**：基于CHOMP，使用瞬时ESDF计算速度梯度，优化目标包含障碍物代价、平滑代价和目标吸引力代价（参数：\(k_{att}=1.5, k_{rep}=0.8\)）。
- **对比方法**：共5种基线：
  1. Teacher (CHOMP)：优化型专家。
  2. Vanilla BC：标准行为克隆（仅使用专家数据）。
  3. BC + CVaR：添加风险敏感损失。
  4. BC + CVaR + CBF：添加完整安全正则化损失（仍仅使用静态专家数据）。
  5. Ours (with DAgger)：完整方法 + DAgger迭代聚合。
- **评价指标**：任务成功率（是否到达目标）、平均急动度（Jerk，m/s³）、最小障碍物距离（m）。每个方法在15个评估片段上取平均值。

## 四、资源与算力
- **未明确说明**：论文未提及使用的GPU型号、数量、训练时长、CPU等信息。仅提到在PyBullet仿真中运行，但未给出具体硬件配置或计算时间统计。
- **推测**：由于策略网络为两层256的MLP，训练计算量较小，可能单GPU（如RTX 3060或更高）即可完成。但缺乏明确记录。

## 五、实验数量与充分性
- **实验数量**：
  - 主要定量比较：5种方法，每种在15个评估片段上取均值（共75次评估）。
  - 未报告多次随机种子下的重复实验（如5次独立种子），仅一次评估结果。
  - 无跨环境变体（如不同障碍物密度、动态障碍物、传感器噪声）的消融。
  - 提供Figure 4（急动度对比）和Figure 5（最小间隙分布），但仅基于15个片段。
- **充分性评价**：实验设计基本合理，验证了DAgger的关键作用，但样本量偏小（15个片段），且缺乏统计显著性检验。未考虑仿真到现实（sim-to-real）的迁移实验。结论虽明确，但充分性有限，存在因随机性导致结果偏差的风险。

## 六、论文的主要结论与发现
- **核心发现**：仅靠安全正则化损失（CVaR + CBF）无法缓解行为克隆的协变量偏移，导致任务成功率低于15%（尽管轨迹平滑、安全裕度高）。而引入DAgger后，成功率提升至80%，急动度从7.8增加到30.2 m/s³，安全裕度（0.07m）与专家（0.06m）相当。
- **“漂移”失效模式**：静态数据训练的策略在状态漂移后输出被动行为（如悬停或漂移），由于缺乏恢复数据；DAgger使策略学会主动修正错误。
- **急动度权衡**：平滑性来自保守（不主动避开），而鲁棒性需要积极的修正动作，导致控制更为急促。
- **结论**：数据聚合（DAgger）而非安全正则化是杂乱环境中鲁棒模仿学习的关键。

## 七、优点
- **问题定义清晰**：聚焦于建筑环境导航的独特挑战（非结构化、GPS缺失），目标明确。
- **系统性消融**：从Vanilla BC逐步添加CVaR、CBF再到DAgger，清晰地分离了各组件贡献。
- **方法组合具有创新性**：将残差策略学习、学习型CBF和DAgger结合，并引入CVaR处理尾部风险。
- **仿真环境设计贴近实际**：程序化生成脚手架、碎片，随机起点和目标，模拟建筑现场杂乱度。
- **定量与定性分析结合**：不仅报告成功率，还分析急动度、最小间隙以及“漂移”失效模式，解释原理。

## 八、不足与局限
- **静态世界假设**：环境中的障碍物（脚手架、碎片）是固定的，未考虑动态障碍物（如移动设备、工人）。
- **安全保证非正式**：学习型安全批评器提供概率风险估计，而非控制理论严格的安全保证（如CBF的在线QP滤波）。
- **实验规模有限**：仅15个片段/方法，未做多随机种子重复，统计可靠性存疑；未测试不同环境参数（障碍物密度、布局变化）。
- **缺乏真实世界验证**：仅在PyBullet仿真中评估，未进行任何真实无人机实验，实际部署的鲁棒性未知。
- **传感器退化未模拟**：未考虑尘土、遮挡、噪声等实际建筑现场的传感干扰。
- **任务范围有限**：仅考虑短航程导航，未涉及长时间任务或复杂目标追踪。
- **超参数仅一组合格**：λ₁、λ₂、γ等未经系统调优，可能非最优。

（完）
