---
title: "ADAPT: Analytical Disturbance-Aware Policy Training for Humanoid Locomotion"
title_zh: ADAPT：面向人形机器人运动的分析扰动感知策略训练
authors: "Bofan Lyu, Jindou Jia, Kuangji Zuo, Yanshuo Lu, Shijia Han, Gen Li, B Y Ma, Jingliang Li, Geng Li, Jie Yang"
date: 2026-06-15
pdf: "https://arxiv.org/pdf/2606.16542"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 人形机器人面临外力扰动影响运动稳定性，现有方法在准确性、泛化性和鲁棒性上存在局限。ADAPT框架引入分析性全身扰动观测器，利用机器人动力学在线估计残余力/力矩，无需传感器，直接馈入策略。在Unitree G1上实验，ADAPT实现精确扰动预测，在躯干扰动、站立推挤和非对称负载下鲁棒性显著优于仅本体感知基线，且分布外速度跟踪改善。该方法提供物理可解释的扰动感知能力，并通过惩罚下体关节扰动鼓励轻快运动。
source: openalex
selection_source: hot_paper_scout
motivation: 现有基于学习的方法依赖广泛的域随机化或任务特定目标，导致准确性、可迁移性或分布外鲁棒性不足，需要物理驱动的扰动感知方法。
method: 提出ADAPT，核心是分析性全身扰动观测器，利用机器人动力学在线估计外部残余力/力矩，无需传感器，并将估计值直接输入策略网络。
result: 在Unitree G1上，ADAPT在多种扰动下实现精确扰动预测，鲁棒性优于本体感觉基线，在分布外场景中速度跟踪误差显著降低。
conclusion: ADAPT通过物理扰动观测器提升人形机器人运动鲁棒性，并可利用估计扰动惩罚实现更轻快的运动。
---

## 摘要
部署在人类中心环境中的人形机器人必须处理力交互任务，其中外部接触会引入意外扰动，破坏运动精度与稳定性。现有基于学习的方法依赖于广泛的域随机化、特定任务力目标或基于运动历史的学习型力估计器，这些方法在精度、任务迁移性或分布外鲁棒性上均存在不足。我们提出分析扰动感知策略训练框架，该框架为人体策略配备物理基础的扰动观测器。ADAPT的核心是一种分析型全身扰动观测器，它利用可获取的机器人动力学在线估计残余力/力矩，无需力/力矩传感器。将估计的扰动直接输入策略，使人形机器人获得显式的、源自物理的外力/力矩感知，从而能泛化至各种未见场景。在宇树G1人形机器人上的实验表明，相较于仅依赖本体感受的基线方法，ADAPT在躯干扰动、站立推力和非对称手持载荷下实现了更准确的扰动预测和更强的鲁棒性，即使在分布外扰动下也能改善速度跟踪。此外，ADAPT能够惩罚下肢关节的推断扰动，以鼓励更轻盈的运动。

## Abstract
Humanoids deployed in human-centered environments must handle force-interactive tasks, where external contacts introduce unexpected disturbances that disrupt locomotion accuracy and stability. Existing learning-based approaches rely on broad domain randomization, task-specific force objectives, or learning-based force estimators from motion history, each of which compromises accuracy, task transferability, or out-of-distribution (OOD) robustness. We present Analytical Disturbance-Aware Policy Training (ADAPT), a framework that equips humanoid policies with a physically grounded disturbance observer. The core of ADAPT is an analytical whole-body disturbance observer that estimates residual force/torque online with the accessible robot dynamics, without requiring force/torque sensors. Fed directly into the policy, the estimated disturbances give the humanoid an explicit, physics-derived sense of external force/torque that can generalize across diverse unseen scenes. Experiments on a Unitree G1 humanoid show that ADAPT achieves accurate disturbance prediction and stronger robustness than a proprioception-only baseline under torso perturbations, standing pushes, and asymmetric hand payloads, with improved velocity tracking even on OOD disturbances. Moreover, ADAPT enables penalizing inferred disturbances at lower-body joints to encourage lighter locomotion.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 人形机器人部署在人类中心环境时，必须处理力交互任务（如搬运、推车、开门等），这些任务会引入意外外力扰动，破坏运动精度与稳定性。
- 现有基于学习的方法存在三种主要路径，但各有缺陷：
  - 广泛域随机化：提升鲁棒性但牺牲跟踪精度。
  - 任务特定力目标：缺乏通用性，需针对每类任务重新设计。
  - 学习型力估计器（从运动历史推断）：在分布外（OOD）扰动下泛化能力差。
- 因此需要一种**物理驱动、无需传感器、能跨任务泛化**的扰动感知方法，以提升人形机器人策略的鲁棒性和通用性。

## 二、论文提出的方法论
- **核心思想**：在强化学习（RL）策略中引入**分析性全身扰动观测器**，利用可获取的机器人动力学（状态、控制指令）在线估计外部力/力矩，作为显式的感知输入馈入策略，并支持基于扰动的奖励塑形。
- **关键技术细节**：
  - **全身扰动观测器**：基于广义动量（\(p = M(q)v\)）推导，避免直接计算加速度（易受噪声影响）。观测器方程为：
    \[
    \dot{z} = -K_o(\beta + \tau_m + \hat{\tau}_e),\quad \hat{\tau}_e = z + K_o p
    \]
    其中 \(\beta = C^\top v - g\)，用 MuJoCo 的偏置力近似（引入可忽略的速度相关误差）。观测器增益 \(K_o = 3.0\) 的对角矩阵，输出经 1Hz 低通滤波。
  - **策略训练**：使用 PPO（近端策略优化），Actor 与 Critic 均为三层 MLP（512-256-128），Actor 输入包含五步历史的本体感知和归一化的扰动估计（共 554 维）。Critic 额外使用特权脚接触信息（仅训练时用）。
  - **两阶段课程训练**：阶段1在无扰动下训练基础步态（15000 迭代）；阶段2引入外部力扰动课程（20000 迭代），逐步增加强度。
  - **归一化策略**：扰动通道采用**统一缩放**（除以质量、重力、参考长度或关节力矩极限），而非标准统计归一化，以适应两阶段扰动幅度差异。
  - **轻步奖励塑形**：基于下肢关节扰动残差的包络定义惩罚项（高尾均值与峰值超过阈值时惩罚），鼓励更轻柔的落地。
  - **状态估计**：使用 FAST-LIO（激光雷达惯性里程计）获取根线速度，通过雅可比补偿转换为根帧速度，作为策略和观测器输入。

## 三、实验设计
- **机器人平台**：宇树 G1 人形机器人（26个自由度）。
- **场景与扰动类型**：
  - 躯干扰动：仿真中前后方向（0~60 N，训练最大 40 N）及多水平方向（8个方向，40/60 N）；真机中向前拉动测试。
  - 站立推扰：真机中实验人员对躯干和肩部施加推力，观察姿态调整。
  - 不对称手负载：仿真中向单手施加向下力（10~40 N）；真机中挂载 1~4 kg 重物（4 kg 为 OOD）。
  - 轻步奖励：仿真和真机中比较足迹扰动包络和步态。
- **对比方法**：仅使用本体感知的基线（相同架构但不输入扰动估计），未与其他学习型力估计或域随机化方法直接对比。
- **评估指标**：前向速度跟踪误差（RMSE）、侧向漂移（dy）、偏航漂移（dψ）。
- **训练设置**：使用 mjlab 仿真器，4096 个并行环境，策略更新频率 50 Hz，仿真步长 5 ms，控制降采样 4 倍。

## 四、资源与算力
- **训练 GPU**：NVIDIA RTX 5090（未明确型号是桌面版还是数据中心版，但推断为 RTX 5090）。
- **并行环境**：4096 个并行仿真环境。
- **训练迭代**：共 35000 次迭代（阶段1 15000 + 阶段2 20000）。
- **未提及**：训练总耗时、单个迭代时间、GPU 个数或集群配置。文中仅称“训练在单张 RTX 5090 上完成”，未详细说明时间。

## 五、实验数量与充分性
- **仿真实验**：躯干扰动测试覆盖 3 种速度（0.5/0.8/1.1 m/s）× 7 种力幅值（±60/±40/±20/0 N）× 10 个随机种子，共 210 组；方向测试覆盖 8 个方向× 2 种力幅× 10 种子；手负载测试覆盖 3 种力× 3 种速度× 10 种子。
- **真机实验**：轻步奖励实验 7 次重复；不对称负载实验 3 次重复（每策略每负荷）；站立推扰为定性展示，未定量。
- **消融实验**：在附录中测试了统一归一化 vs 标准归一化（基于躯干扰动任务），验证了缩放策略有效性；在附录中还对比了 MuJoCo 近似与精密 Pinocchio 观测器，验证近似误差可忽略。
- **充分性**：仿真实验包含 OOD 条件（60 N 力、4 kg 负载），真机实验覆盖多重复，结果统计稳定。但**对比基线单一**（仅本体感知），未与基于学习力估计的方法（如 Zhi et al., 2025）或域随机化方法（如 Radosavovic et al., 2024）直接比较；**未在多种机器人型号上验证通用性**；**未系统评估轻步奖励对手部扰动或能耗等其他性能的影响**。

## 六、论文的主要结论与发现
- 提出的全身扰动观测器在仿真和真机上均能准确估计注入的关节扰动（接近真实值），真机中受摩擦等未知因素影响误差稍大。
- 将估计扰动作为策略输入（ADAPT）显著提升了鲁棒性：在训练内和分布外扰动下，速度跟踪误差、侧向漂移和偏航漂移均低于仅本体感知基线。
- ADAPT 策略展现出**涌现的力响应行为**：在不平衡负载下主动倾斜躯干补偿力矩，在推力测试中挺直姿态抵抗扰动。
- 利用扰动估计进行奖励塑形成功诱导出更轻快的步态（脚尖踮地而非重踏），并在真机上得到验证。
- 通过显式物理感知而非隐式学习，ADAPT 实现了对未见扰动的良好泛化。

## 七、优点
- **物理驱动，无需传感器**：仅利用现有本体感知和控制指令，即可获得显式扰动估计，不依赖额外力/力矩硬件。
- **通用性强**：方法独立于具体任务，可通过同一观测器支持多种扰动类型（推力、负载、冲击等），并自然泛化到 OOD 场景。
- **即插即用**：扰动估计可融入现有 RL 策略（作为观测或奖励），无需大幅修改策略架构，易于迁移到其他机器人。
- **支持奖励塑形**：利用同一估计信号设计任务相关奖励（如轻步），扩展了框架灵活性。
- **与状态估计结合**：首次将 FAST-LIO 用于 RL 人形策略的根线速度输入，提升了真机部署的准确性。
- **实验充分**：仿真覆盖多变量组合，真机重复验证，消融实验帮助分析设计选择。

## 八、不足与局限
- **观测器响应延迟**：低通滤波（1 Hz）和有限增益导致对快速变化扰动（如冲击、瞬时推力）收敛慢，可能使策略对快速扰动响应保守。文中承认这一点并提出未来分离快慢变分量。
- **对比基线不足**：仅与无扰动感知的基线对比，未与现有基于学习力估计的方法（如 Zhi et al., 2025）或域随机化方法（如 H-Infinity 控制）进行直接竞争性比较，削弱说服力。
- **单一机器人平台**：所有实验在宇树 G1 上完成，未在不同自由度或动力学的其他机器人（如波士顿动力 Atlas、优必选 Walker）上验证，限制了结论的通用性。
- **轻步奖励依赖性**：轻步行为仅基于下肢扰动残差，可能忽略上肢或全身协调的其他影响（如能耗、稳定裕度）；未评估对跟踪精度的潜在负面效应。
- **传感器依赖**：需要激光雷达（FAST-LIO）获得准确根线速度，在无 LiDAR 场景适用性受限；观测器依赖精确的动力学模型（文中使用 MuJoCo 近似），真实模型偏差可能降低估计精度。
- **训练代价**：两阶段课程训练需要精细的课程设计和较高的迭代次数，且对 GPU 并行环境要求高（4096 环境），可能对资源有限的团队不友好。

（完）
