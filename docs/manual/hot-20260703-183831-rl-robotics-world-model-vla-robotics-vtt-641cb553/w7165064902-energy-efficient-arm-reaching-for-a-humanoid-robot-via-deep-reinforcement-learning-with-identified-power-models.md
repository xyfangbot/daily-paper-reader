---
title: Energy-Efficient Arm Reaching for a Humanoid Robot via Deep Reinforcement Learning with Identified Power Models
title_zh: 通过深度强化学习与辨识功率模型实现仿人机器人的能效臂部伸展
authors: "Nestor N. Deniz, Simon Parsons, Fernando Auat Cheein"
date: 2026-06-14
pdf: "https://arxiv.org/pdf/2606.15918"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: "人形机器人在野外作业如苹果采摘时面临严重能量约束，影响每次充电的到达次数。本文提出端到端节能强化学习框架，结合实验识别的电功率模型与SAC策略，在Pinocchio仿真器中训练，使用增量关节位置动作空间和混合星座奖励。仿真训练后达到69.9%成功率、平均98.16焦；物理Unitree G1上验证平均71.5焦，位置误差2.64cm、方向误差6.92°，均在训练容忍度内。该工作首次实现基于强化学习的节能手臂到达，为电池续航优化奠定基础。"
source: openalex
selection_source: hot_paper_scout
motivation: 人形机器人在野外操作（如苹果采摘）能量受限，直接限制每次充电可执行的到达运动次数。
method: 提出基于实验识别电功率模型的SAC强化学习框架，采用增量关节位置动作空间和混合星座奖励（含末端距离与能耗代理）进行训练。
result: "仿真实现69.9%成功率、平均98.16焦；物理实验平均71.5±48.3焦、位置误差2.64±1.04cm、方向误差6.92±1.33°。"
conclusion: 此为首次基于节能强化学习的人形机器人手臂到达验证，展示了方法在实际平台上的可行性和有效性。
---

## 摘要
仿人机器人在现场操作任务（如机器人苹果采摘）中面临严峻的能源约束，直接限制了每次充电可执行的臂部伸展运动次数。本文针对Unitree G1仿人机器人7自由度左臂，提出了一种端到端的能量感知强化学习框架，该框架将基于物理学的实验辨识电功率模型与基于Pinocchio的刚体动力学模拟器中训练的软演员-评论家（SAC）策略相结合。该强化学习策略在增量关节位置动作空间上运行，并采用混合星座奖励进行训练，该奖励将四点末端执行器星座距离与扭矩范数能量代理相结合；在运动学模拟中对1000个随机目标进行5×10^6次训练后，成功率达到69.9%，成功回合的平均能量为98.16焦耳。最后，在实际Unitree G1上，该策略在三个独立的10目标批次上进行了验证，平均能量为71.5±48.3焦耳，末端执行器位置误差为2.64±1.04厘米，姿态误差为6.92±1.33度——均在4厘米/8.6度的训练容差范围内。这些结果为基于能量感知强化学习的仿人机器人臂部伸展迈出了第一步。

## Abstract
Humanoid robots performing in-field manipulation tasks, such as robotic apple harvesting, face severe energy constraints that directly limit the number of reaching motions that can be executed per battery charge. This paper presents an end-to-end, energy-aware reinforcement learning framework for the 7-degree-of-freedom left arm of the Unitree~G1 humanoid robot, combining a physics-based, experimentally identified electrical power model with a Soft Actor-Critic (SAC) policy trained in a Pinocchio-based rigid-body dynamics simulator. The RL policy operates on an incremental joint-position action space and is trained with a Hybrid Constellation Reward that combines a four-point end-effector constellation distance with a torque-norm energy proxy; after % $5\times10^6$ training it reaches a $69.9\%$ success rate over $1\,000$ random targets in kinematic simulation, at a mean energy of \SI{98.16}{\joule} on successful episodes. Finally, on the physical Unitree~G1, the policy is validated over three independent 10-target batches, achieving a mean energy of $71.5 \pm 48.3$\,J, an end-effector position error of $2.64 \pm 1.04$\,cm, and an orientation error of $6.92 \pm 1.33^\circ$ -- within the \SI{4}{\centi\metre}/$8.6^\circ$ training tolerance. These results constitute a first step toward energy-aware reinforcement-learning-based arm reaching for humanoid robots.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：仿人机器人在野外作业（如苹果采摘）中，臂部重复运动能耗高、变化大，严重限制了单次充电可执行的动作次数，延长工作时间的核心在于降低每次伸臂的能量消耗。
- **核心问题**：如何在不牺牲任务成功率的前提下，制定一种节能且能从仿真迁移到真实硬件的臂部伸展控制策略。
- **整体含义**：本文首次在仿人机器人物理平台上验证了基于深度强化学习（RL）的能量感知臂部伸展框架：将实验辨识的电功率模型嵌入RL奖励设计（作为评估指标），通过模拟到现实的迁移，在受限但代表性的采摘任务空间内实现了低于训练容差的末端精度和大幅节能。

## 二、论文提出的方法论
- **核心思想**：采用**软演员-评论家（SAC）** 算法，在基于Pinocchio的运动学仿真环境中训练策略；利用**增量关节位置动作空间**和**混合星座奖励**实现节能与精度的权衡；将**实验辨识的物理电功率模型**作为统一评估指标（而非训练奖励），保持训练流畅性。
- **关键技术细节**：
    - **状态空间（状态 $s_t \in \mathbb{R}^{21}$）**：包含归一化关节角度、归一化关节速度、归一化末端位置误差、归一化旋转误差（用转动向量表示）、以及剩余时间比例。
    - **增量关节位置动作空间**：动作 $a_t \in [-1,1]^7$ 表示增量位移，生成关节目标位置 $q^{\text{tgt}}_t = \text{clip}(q_t + a_t \odot \Delta q_{\max})$，再由比例控制器计算期望速度并限幅，保证实际速度不超限，避免连续饱和。
    - **混合星座奖励**：定义4个虚拟点刚性地附着在末端坐标系，计算当前位置与目标位置的均方距离 $d^{\text{con}}_t$。该距离同时敏感于位置误差和旋转误差。总奖励包含：密集进度奖励（$d^{\text{con}}$ 的减少量）、残差位置惩罚、指数星座奖励、恒定步代价、速度平滑惩罚、**扭矩范数能量代理**（$\lambda_\tau \|\tau_t\|_2$）以及稀疏成功奖励（$R_{\text{success}}=700$）。**注意**：完整电功率模型仅用于事后评估，不参与梯度更新。
    - **能量代理与评估分离**：奖励中唯一节能项是扭矩范数代理；实验辨识的完整电功率模型 $P_{\text{net}}(\tau, \dot{q})$（含机械功率、铜损、库仑摩擦、黏性摩擦及相互作用项）仅用于所有实验（仿真和硬件）的耗能统计，保证公平性。
    - **SAC算法细节**：自动调节温度参数 $\alpha_{\text{ent}}$ 以维持探索，特别是靠近目标时，充分探索成功区域；采用离线策略、最大化熵目标函数。

## 三、实验设计
- **数据集与场景**：
    - **训练场景**：在Pinocchio刚体动力学模拟器中，随机生成目标位姿（通过均匀采样关节角度并前向运动学映射，排除距肩关节过近点）。
    - **评估场景**（四级验证弧）：
        1. **运动学仿真评估**（n=1000目标）：冻结策略直接运行，与**最小加加速度轨迹**（闭环解析轨迹，基于已知目标关节角度）进行能量对比。
        2. **动力学验证**（MuJoCo，n=200）：使用完整Unitree G1 MJCF模型，对冻结策略进行PD增益扫描（$k_p \in \{30,50,100,400\}$）。
        3. **工作空间可达性分析**（n=80）：在名义“苹果采摘边界盒”内随机抽样，解位置逆运动学检查可达性。
        4. **受限任务空间动力学筛选**（MuJoCo，n=20）：仅保留满足 $x \geq 0.1$ m 且IK残差小于2cm的目标。
        5. **真实硬件验证**（n=30，分3批次，每批10个目标）：直接部署相同策略。
    - **基准方法**：**最小加加速度轨迹规划器**（需要特权信息，即目标关节角度 $q^*$，RL策略只观察 Cartesian 位姿）。

## 四、资源与算力
- **训练算力**：使用了**8个并行环境**（SubprocVecEnv）在桌面级GPU（NVIDIA RTX系列）上训练约1000-1700 step/s，总环境步 $5\times10^6$。
- **未明确说明**：具体GPU型号、训练总时间、激活函数等细节未在摘要中给出，需要查阅正文。

## 五、实验数量与充分性
- **实验数量**：
    - 主实验：1组（运动学仿真评估，n=1000；硬件验证，n=30）。
    - 消融实验：无（奖励设计、动作空间等未进行交叉验证）。
    - 辅助实验：3组（MuJoCo PD增益扫描 n=100/200；工作空间可达性分析 n=80；受限空间动力学筛选 n=20）。
- **充分性评价**：
    - **优点**：实验覆盖从纯运动学到完整动力学、从仿真到真实硬件的完整验证弧，特别是通过PD增益扫描和工作空间可达性分析解释了仿真与现实差距的根源（完美跟踪假设偏差与几何不可达性）。
    - **不足**：缺乏消融实验（如是否使用扭矩惩罚、不同奖励权重的影响）；真实硬件样本量仅30，不足以报告统计显著的二进制成功率，仅报告误差分布；基线（最小加加速度）作为“特权信息”基准，可比性有限。

## 六、论文的主要结论与发现
- **核心结论**：所提出的SAC策略在使用增量关节位置动作空间和混合星座奖励训练后，能在**受限的采摘任务空间**（通过工作空间可达性分析筛选）内实现**端到端能量感知臂部伸展**。在真实Unitree G1上，一次充电可执行约**54.9 J/次**的节能伸展，同时末端斥候误差保持在**2.64±1.04 cm、6.92±1.33°** 的精度容差内。
- **关键发现**：
    1. **仿真到现实的差距主要由“完美跟踪假设”而非控制器缺陷导致**：MuJoCo中PD增益变化无法消除20-25%成功率差，说明训练环境假设的瞬时速度跟踪过于理想。
    2. **工作空间几何可达性是主导因素**：仅30%的随机采样点可通过IK达到2 cm以内，剩余点中位数偏差约10 cm；排除不可达点后，MuJoCo成功率回升至95%。
    3. **硬件能耗低于仿真**：由于实际控制器限制（软PD增益+扭矩钳位），实际扭矩最大20.9 Nm，远小于仿真199 Nm，能耗分布明显下移（中位数54.9 J vs 仿真成功平均98.16 J）。

## 七、优点
- **方法设计亮点**：
    - **奖励设计的分离原则**：将能耗评估函数（完整电功率模型）与训练代理（扭矩范数）分离，既保持了训练奖励的平滑性和计算效率，又确保所有实验使用同一个物理校准的度量标准，避免作弊。
    - **增量关节位置动作空间**：巧妙地通过位置增量限制从根源上避免关节速度饱和，消除训练和部署间因饱和引起的分布偏移。
    - **混合星座奖励**：通过引入虚拟的“星座点”将位置误差和姿态误差融合为一个几何量，无需手动调整位置/姿态权重。
- **实验设计亮点**：
    - **系统性的PD增益扫描**：揭示仿真-现实差距根源，指导实际部署中选择低增益/低能耗的控制器。
    - **工作空间可达性分析**：量化任务的几何可行性，证明大部分失败源于目标本身无法到达，而非策略缺陷。

## 八、不足与局限
- **实验覆盖不足**：缺乏消融实验，例如能量代理权重 $\lambda_\tau$、增量位置步长、星座半径的敏感性分析；基线（最小加加速度）需要特权关节角度信息，公平性值得考量。
- **验证规模限制**：真实硬件仅30个样本，不足以建立统计显著的成功率，只能报告均值和分布；动态验证（MuJoCo受限空间）仅20样本，代表性有限。
- **策略局限性**：
    - 策略仅针对部分可达任务空间有效，当目标位于躯干附近或更复杂几何位置时，性能骤降。
    - 未与在线优化方法（如MPC）进行直接能耗对比。
    - 能量代理（扭矩范数）与完整功率模型的相关性未在训练尺度下验证（α=0意味着梯度从未见过完整模型）。
- **应用限制**：仅在孤立臂部伸展任务上验证，未集成感知、抓取和躯干/底座重定位，距离完整采摘系统尚有差距。

（完）
