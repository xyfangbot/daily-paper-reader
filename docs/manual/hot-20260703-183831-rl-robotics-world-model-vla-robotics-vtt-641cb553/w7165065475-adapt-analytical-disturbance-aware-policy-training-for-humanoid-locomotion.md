---
title: "ADAPT: Analytical Disturbance-Aware Policy Training for Humanoid Locomotion"
title_zh: ADAPT：基于解析的扰动感知仿人机器人运动策略训练
authors: "Bofan Lyu, Jindou Jia, Kuangji Zuo, Yanshuo Lu, Shijia Han, Gen Li, B Y Ma, Jingliang Li, Geng Li, Jie Yang"
date: 2026-06-15
pdf: "https://arxiv.org/pdf/2606.16542"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 人形机器人执行力交互任务时，外部接触常破坏运动稳定性和精度，现有方法在精度、任务迁移性或分布外鲁棒性上存在缺陷。ADAPT框架引入分析型全身扰动观测器，利用机器人动力学在线估计残余力/力矩，无需力传感器，将物理感知的扰动估计直接输入策略。在Unitree G1上实验表明，该方法在躯干扰动、站立推、不对称载荷等场景下实现准确预测和更强鲁棒性，速度跟踪优于本体感知基线，且有效应对分布外扰动。ADAPT赋予机器人物理推导的外力理解，提升泛化能力，并可通过惩罚下肢扰动实现更轻快的运动。
source: openalex
selection_source: hot_paper_scout
motivation: 现有学习方法依赖域随机化或任务特定力目标，在精度、迁移性或分布外鲁棒性上存在不足。
method: 提出ADAPT框架，核心是分析型全身扰动观测器，从动力学在线估计残余力/力矩，无需力传感器，输入策略。
result: 在Unitree G1上，ADAPT在多种扰动下预测准确，鲁棒性优于本体感知基线，速度跟踪更佳，且处理分布外扰动有效。
conclusion: ADAPT使人形机器人获得物理感知的外力理解，提升泛化性和运动轻快性。
---

## 摘要
部署在以人为本环境中的仿人机器人必须处理力交互任务，其中外部接触会引入意外扰动，破坏运动精度和稳定性。现有基于学习的方法依赖于广泛的域随机化、特定任务的力目标，或基于运动历史的学习型力估计器，这些方法各自在精度、任务可迁移性或分布外（OOD）鲁棒性上有所妥协。我们提出基于解析的扰动感知策略训练（ADAPT），这是一个为仿人机器人策略配备物理基础扰动观测器的框架。ADAPT的核心是一个解析全身扰动观测器，它利用可获取的机器人动力学在线估计残余力/力矩，无需力/力矩传感器。将估计的扰动直接输入策略，使仿人机器人获得明确的、源自物理的外力/力矩感知，该感知能泛化到各种未见场景。在宇树G1仿人机器人上的实验表明，ADAPT在躯干扰动、站立推压和非对称手部负载下实现了比仅基于本体感觉的基线更准确的扰动预测和更强的鲁棒性，即使在分布外扰动下速度跟踪也得到改善。此外，ADAPT能够对下肢关节的推断扰动进行惩罚，以鼓励更轻盈的运动。

## Abstract
Humanoids deployed in human-centered environments must handle force-interactive tasks, where external contacts introduce unexpected disturbances that disrupt locomotion accuracy and stability. Existing learning-based approaches rely on broad domain randomization, task-specific force objectives, or learning-based force estimators from motion history, each of which compromises accuracy, task transferability, or out-of-distribution (OOD) robustness. We present Analytical Disturbance-Aware Policy Training (ADAPT), a framework that equips humanoid policies with a physically grounded disturbance observer. The core of ADAPT is an analytical whole-body disturbance observer that estimates residual force/torque online with the accessible robot dynamics, without requiring force/torque sensors. Fed directly into the policy, the estimated disturbances give the humanoid an explicit, physics-derived sense of external force/torque that can generalize across diverse unseen scenes. Experiments on a Unitree G1 humanoid show that ADAPT achieves accurate disturbance prediction and stronger robustness than a proprioception-only baseline under torso perturbations, standing pushes, and asymmetric hand payloads, with improved velocity tracking even on OOD disturbances. Moreover, ADAPT enables penalizing inferred disturbances at lower-body joints to encourage lighter locomotion.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 人形机器人在人机共融环境中需执行力交互任务（如搬运、推车、开门等），外部接触会引入意外扰动，破坏运动精度和稳定性。
- 现有基于学习的方法存在缺陷：广泛域随机化牺牲跟踪精度；任务特定力目标缺乏迁移性；基于运动历史的学习型力估计器对分布外扰动泛化差。
- 核心动机：能否利用机器人自身的物理知识（而非数据驱动）提供一种物理基础的扰动感知，提升策略的鲁棒性与泛化能力，且不依赖额外力传感器。

## 二、论文提出的方法论
- **核心思想**：将解析全身扰动观测器与强化学习策略相结合，观测器利用可获取的机器人动力学在线估计残余力/力矩，作为明确、物理驱动的观测输入给策略。
- **关键技术细节**：
  - **扰动观测器设计**：基于广义动量（p = M(q)v）推导，避免直接计算加速度。通过引入辅助状态z，得到无加速度项的一阶观测器：
    - ˙z = -Ko(β + τm + ˆτe)，ˆτe = z + Kop
    - 其中β = C^T v - g，τm为电机广义力。实际使用MuJoCo模型高效计算名义动力学（M, qbias），近似β≈-qbias，引入的˙M v误差在实践中可忽略。
    - 观测器增益Ko为正定对角，设定ko=3.0，运行于50Hz。输出经二阶巴特沃斯低通滤波（截止频率1Hz）后得到¯τe。
  - **扰动感知策略**：
    - 采用PPO算法，非对称Actor-Critic结构（三层MLP，512-256-128，ELU激活）。
    - Actor观测包括5步历史：基座线速度/角速度、投影重力、关节位置/速度、速度指令、归一化扰动估计ρ（线性/角/关节残余分别除以mg、mgl_ref、τ_max），以及上一步动作。
    - 两阶段训练课程：阶段1无扰动学习基本行走；阶段2引入外部力扰动（躯干&末端）递增训练。
  - **扰动归一化**：采用统一尺度归一化（除以质量、参考长度、关节力矩上限），而非标准归一化，以适应两阶段量级差异。
  - **奖励塑形**：额外定义轻步奖励，基于腿部关节扰动残差包络的高尾均值与峰值，惩罚高冲击落地，鼓励轻盈步态。
  - **实用考虑**：部署时使用FAST-LIO（LiDAR-惯性里程计）提供精确根线速度，通过雅可比转换到根坐标系。

## 三、实验设计
- **平台**：宇树G1人形机器人（19个主动自由度），模拟环境基于mjlab（MuJoCo），训练4096个并行环境。
- **场景与评估指标**：
  - **扰动观测器性能评估**：固定向前行走（0.8 m/s），在左肩、左肘、右肩、腰部关节注入已知扰动转矩，评估观测器跟踪精度（模拟和实物）。
  - **控制性能评估**：
    - 躯干拉力测试（模拟）：施加矢状面躯干力（0~60N，训练最大40N），不同速度指令（0.5/0.8/1.1 m/s）；方向性测试（8个水平方向，40N和60N）。指标：速度跟踪误差、横向漂移、偏航漂移。
    - 站立拉动测试（实物）：零速度指令下操作者手动推拉躯干和肩膀，观察姿态抵抗能力。
    - 非对称手部负载测试：模拟中右手施加向下恒力（10/20/40N），实物挂载1/2/4 kg（4kg为OOD）。评估横向漂移。
  - **轻步奖励塑形**：前向行走（0.8 m/s），比较腿部扰动包络（模拟和实物），观察步态变化。
- **对比基线**：与ADAPT架构相同但不接收显式扰动观测的策略（proprioception-only baseline）。
- **消融实验**：统一尺度归一化 vs 标准归一化（附录E）。

## 四、资源与算力
- **训练硬件**：一块NVIDIA RTX 5090 GPU。
- **并行环境**：4096个并行仿真环境（mjlab）。
- **训练迭代**：阶段1训练15,000次迭代，阶段2从阶段1检查点继续训练20,000次迭代。
- **模拟频率**：物理步长0.005s，控制降采样4倍，策略更新50Hz。
- **部署硬件**：外部笔记本（NVIDIA RTX 5070 Ti Laptop GPU），通过有线以太网连接机器人；机器载计算机运行FAST-LIO（100Hz）。

## 五、实验数量与充分性
- **扰动观测器**：模拟和实物各一次关节注入测试，定性展示跟踪精度，量化误差未全面报告。
- **控制性能**：
  - 躯干拉力测试：多种速度×力大小×方向组合，每个条件10个随机种子（共约4×8×10=320次模拟运行）。实物仅展示定性结果。
  - 非对称负载：模拟中3种力×3种速度×10种子（约90次），实物中3种负载×2种速度×3次重复（18次）。报告了横向漂移曲线，统计充分。
  - 轻步预测：模拟20个随机种子，实物7次重复。
- **消融实验**（附录E）：展示统一归一化优于标准归一化，但未报告统计显著性。
- **总体评价**：实验覆盖了主要扰动类型（推力、拉力、持续负载），并进行了OOD测试。消融实验较简单，缺乏对观察器增益、滤波截止频率等超参数的敏感性分析。实物实验以定性演示为主，定量指标较少，但有重复性。整体公平，基线设置合理。

## 六、论文的主要结论与发现
- **扰动观测器**：在模拟和实物中均能准确跟踪注入的关节扰动，通道间隔离良好；实物误差稍大，主要来自未建模摩擦和电机模型误差。
- **控制性能**：
  - ADAPT在躯干拉力（训练内和OOD）下速度跟踪误差、横向漂移和偏航漂移均显著低于基线。
  - 在非对称手部负载下，ADAPT主动倾斜躯干补偿力矩，横向漂移远小于基线，OOD负载（4kg）仍保持稳定。
  - 站立拉动测试中，ADAPT表现出更强的姿态抵抗能力。
- **轻步奖励**：ADAPT训练的策略产生较低的腿部扰动包络，形成“踮脚”步态，减少了冲击，优于基线的“跺脚”步态。

## 七、优点
- **方法亮点**：
  - 物理驱动 vs 数据驱动：解析扰动观测器基于机器人动力学，无需从运动历史学习，泛化能力强，可处理OOD扰动。
  - 无额外传感器成本：仅利用本体感知和电机命令，不依赖力/力矩传感器。
  - 与强化学习策略无缝集成：直接作为观测输入，并可用于奖励塑形，实现任务特定行为（如轻步）。
  - 两阶段课程训练实用，有效逐步增强策略鲁棒性。
  - 使用FAST-LIO提供精确根速度，提升实际部署性能。
- **实验亮点**：
  - 覆盖多种扰动类型（快速冲击、持续力、非对称负载），并包含OOD测试。
  - 实物验证了关键可迁移性（负载补偿、姿态抵抗）。
  - 奖励塑形展示了扰动信号的多用途性。

## 八、不足与局限
- **观测器收敛延迟**：对快速变化扰动（如冲击、触地）响应有延迟，可能使策略偏保守。论文提出未来可分离快变分量或设计专用观测器。
- **近似误差**：使用MuJoCo偏置力近似β引入˙M v误差，虽然实验影响可忽略，但理论上可能在高速运动或高惯性变化时累积。
- **实验覆盖不足**：
  - 未在其他机器人平台（如更高自由度或更小尺寸）验证泛化性。
  - 缺乏与学习型力估计方法（如Zhi et al. 2025）的直接对比，仅对比本体感知基线。
  - 轻步奖励仅测试基本前向行走，未评估在复杂地形或扰动下的效果。
- **计算与实时性**：观测器+FAST-LIO+策略需在外部笔记本50Hz运行，对计算资源有一定要求；未评估在机载低算力平台的可部署性。
- **偏差风险**：实物实验主要由同一团队操作，可能缺乏第三方独立验证；部分实物定性结果（如站立拉动）存在主观判断。
- **局限陈述**：论文第6节已列出局限性，包括观测器收敛延迟和未探索的其他结合方向。

（完）
