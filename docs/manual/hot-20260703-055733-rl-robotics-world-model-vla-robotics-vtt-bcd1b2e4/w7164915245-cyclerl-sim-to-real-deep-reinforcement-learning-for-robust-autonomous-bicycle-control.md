---
title: "CycleRL: Sim-to-Real Deep Reinforcement Learning for Robust Autonomous Bicycle Control"
title_zh: CycleRL：面向鲁棒自主自行车控制的仿真到现实深度强化学习
authors: "Gelu Liu, Teng Wang, Z Z Wu, J I A H U I Wu, Songyuan Li, Xiangwei Zhu"
date: 2026-06-16
pdf: "https://arxiv.org/pdf/2603.15013"
tags: ["query:热点论文筛选", "query:topic", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; institutions=Sun Yat-sen University; query=classic mobile robot trajectory optimization methods"
tldr: "传统控制器难以应对自平衡自行车的欠驱动非线性动力学，对模型误差敏感且适应真实环境不确定性有限。为此提出CycleRL框架，在高保真NVIDIA Isaac Sim环境中使用PPO优化从感知到动作的映射，设计复合奖励函数同时平衡、速度跟踪和转向控制，并通过系统域随机化弥合sim-to-real差距。模拟中平衡成功率99.90%，航向跟踪误差1.15°，速度跟踪误差0.18 m/s，且硬件部署成功。工作验证了深度强化学习在自平衡自行车控制中的有效性，展现了优于传统方法的适应性。"
source: openalex
selection_source: hot_paper_scout
motivation: 传统控制方法在欠驱动非线性自行车系统中易受模型失配影响，难以适应真实世界的动态不确定性。
method: 基于NVIDIA Isaac Sim高保真环境，采用PPO优化复合奖励函数（平衡、速度、转向），结合系统域随机化实现从仿真到真实世界的直接策略迁移。
result: "模拟中平衡成功率99.90%，航向跟踪误差1.15°，速度误差0.18 m/s；硬件部署验证了实际控制效果。"
conclusion: CycleRL表明深度强化学习可有效解决自平衡自行车控制难题，其适应性显著优于传统方法。
---

## 摘要
自主自行车为城市交通与最后一公里物流提供了一种有前景的敏捷方案。然而，传统控制策略往往难以应对欠驱动非线性动力学，对模型失配敏感，且难以适应现实世界的不确定性。为此，我们开发了CycleRL——一个面向鲁棒自主自行车控制的端到端仿真到现实综合框架。该方法在逼真的NVIDIA Isaac Sim环境中建立了从感知到行动的直连映射，利用近端策略优化（PPO）优化控制策略。该框架包含一个针对同时保持平衡、速度跟踪与转向控制而设计的复合奖励函数。关键在于，我们采用系统性域随机化来降低对精确系统建模的依赖，弥合仿真与现实之间的差距，促进策略直接迁移。在仿真中，CycleRL展现了卓越性能，包括99.90%的平衡成功率、1.15°的航向跟踪误差以及0.18米/秒的速度跟踪误差。这些定量结果，加之成功的硬件部署，验证了深度强化学习作为自主自行车控制的有效范式，相比传统方法具有更优的适应性。视频演示请见https://cpnt-lab.github.io/CycleRL/。

## Abstract
Autonomous bicycles offer a promising agile solution for urban mobility and last-mile logistics. However, conventional control strategies often struggle with underactuated nonlinear dynamics, suffering from sensitivity to model mismatches and limited adaptability to real-world uncertainties. To address this, we develop CycleRL, a comprehensive sim-to-real framework for robust autonomous bicycle control. Our approach establishes a direct perception-to-action mapping within the high-fidelity NVIDIA Isaac Sim environment, leveraging Proximal Policy Optimization (PPO) to optimize the control policy. The framework features a composite reward function tailored for concurrent balance maintenance, velocity tracking, and steering control. Crucially, systematic domain randomization is employed to reduce the reliance on precise system modeling, bridge the simulation-to-reality gap and facilitate direct transfer. In simulation, CycleRL achieves promising performance, including a 99.90% balance success rate, a heading tracking error of 1.15°, and a velocity tracking error of 0.18 m/s. These quantitative results, coupled with successful hardware deployment, validate DRL as an effective paradigm for autonomous bicycle control, offering superior adaptability over traditional methods. Video demonstrations are available at https://cpnt-lab.github.io/CycleRL/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：传统控制方法（如PID、LQR、MPC）面对自主自行车这种欠驱动非线性系统时，对模型误差高度敏感，鲁棒性差，难以适应真实世界的不确定性；而基于模型的方法需要精确的系统辨识，计算负担大。
- **整体含义**：论文提出CycleRL框架，利用模型无关的深度强化学习（DRL）在仿真中直接学习从感知到动作的映射，并通过域随机化实现到真实自行车的零样本迁移，验证了DRL作为自主自行车控制的有效范式。

## 二、论文提出的方法论
- **核心思想**：在NVIDIA Isaac Sim高保真物理仿真环境中，使用PPO算法训练一个神经网络策略，输入为IMU和编码器观测（姿态、速度、航向等），输出为转向伺服和轮毂电机控制指令，直接完成平衡、速度跟踪与转向控制。
- **关键技术细节**：
  1. **马尔可夫决策过程（MDP）建模**：状态空间为连续观测向量，动作空间为连续控制量；由于控制频率高（50 Hz），假设部分可观测性问题不显著，直接使用当前观测作为状态。
  2. **复合奖励函数设计**：总奖励为五项加权和——生存奖励（常量正奖励）、速度跟踪奖励（指数函数，系数α=0.25）、航向跟踪奖励（指数函数，系数β=0.1）、动作幅度惩罚（L2范数）、动作变化率惩罚（相邻动作差的L2范数）。权重分别设为1.0、3.0、5.0、1.0、2.0。终止条件：超时（64秒）或滚转角超过45°。
  3. **域随机化策略**：包括动力学随机化（质量、质心高度、摩擦系数、执行器增益、观测噪声）、初始状态随机化（速度、滚转角、伺服/轮毂电机初始状态）、任务指令随机化（目标速度、目标航向随机变化）。
  4. **训练算法**：PPO，使用GAE估计优势，标准剪裁目标函数。

## 三、实验设计
- **数据与场景**：全部在NVIDIA Isaac Sim中训练和评估，模拟多种物理参数、传感器噪声、地面类型（平坦、粗糙、碎石、斜坡、台阶）。真实部署在自制自行车平台上（NVIDIA Jetson Orin NX，IMU、伺服电机、轮毂电机等）。
- **对比基准**：PID控制器、LQR控制器、改进线性控制律（MLCL）。所有基线在仿真中调参，零样本迁移到真实平台。
- **评估指标**：平衡成功率（BSR）、平衡恢复时间（BRT）、最大平衡持续时间（MBD）、临界角度容限（CAT）、航向跟踪误差（HTE）、速度跟踪误差（VTE）、系统响应延迟（SRL）、最大噪声容忍度（MNT）、最低维持速度（MSS）。
- **实验类型**：
  1. **仿真性能对比**：10,000个episode，与PID、LQR、MLCL对比。
  2. **收敛性分析**：10个随机种子的训练曲线。
  3. **鲁棒性验证**：改变速度区间、传感器噪声/丢失、地形类型（共8种条件），各10,000次试验。
  4. **消融实验**：奖励函数各组件去掉后的性能变化（表IV）；域随机化各组分去掉后的影响（表VI）；奖励权重局部灵敏度分析（图6）。
  5. **仿真 vs. 真实对比**：在真实平台上测试上述指标，计算转移比率。

## 四、资源与算力
- **显式说明**：论文明确指出训练基础设施使用NVIDIA Isaac Sim，在单块NVIDIA RTX 4090上实现超过700,000步/秒的仿真速度，环境并行数量为16,384个。训练约1000个epoch（约7亿步）后收敛。文中未提及多GPU或总训练时长具体数值，但算力消耗较大。

## 五、实验数量与充分性
- **实验数量**较多：仿真性能对比10,000个episode；鲁棒性验证共覆盖8种条件各10,000次；消融实验涵盖5种奖励组件、5种域随机化策略、5种权重缩放比例（25个点）；收敛性采用10种随机种子。真实部署进行了多场景测试（不同路面、载荷、轮胎异常等）。
- **充分性**：实验设计较为全面，涵盖了理想条件、噪声、地形变化、消融分析、灵敏度分析、仿真-真实对比。基准对比采用了经典PID、LQR以及较新的MLCL，比较公平。但真实世界基线因无法稳定而缺失，论文对此给出了合理解释。
- **潜在偏差**：仿真中物理引擎PhysX对高速动力学模拟的缺陷被指出，可能影响高速场景的评估质量。所有实验在单一种族车辆平台上进行，泛化性验证仅通过零样本迁移到滑板车做了一次定性展示。

## 六、论文的主要结论与发现
- CycleRL在仿真中达到99.90%的平衡成功率，显著优于PID（76.50%）、LQR（93.24%）、MLCL（96.43%）。
- 航向跟踪误差1.15°，速度误差0.18 m/s，响应延迟1.06秒。
- 通过域随机化，策略成功迁移到真实自行车，平衡成功率95%，最大平衡持续时间超过30分钟，最低维持速度1.33 m/s（仿真1.05 m/s）。
- 消融实验验证了复合奖励函数中各组件、域随机化各层的重要性；局部灵敏度分析表明名义权重设置较平衡。
- 结论：模型无关DRL结合域随机化可有效解决欠驱动自行车控制难题，具有优于传统方法的适应性和鲁棒性。

## 七、优点
- **方法创新**：构建了完整的sim-to-real自行车控制流水线，复合奖励函数设计合理（显式区分性能奖励与控制惩罚）。
- **域随机化策略系统化**：涵盖动力学、初始状态、任务指令三层随机化，针对自行车特性定制（如质心高度、摩擦系数、噪声幅度等）。
- **验证充分**：仿真实验量大，鲁棒性测试覆盖多种真实干扰（噪声、丢失、路面类型），消融实验全面，包括奖励权重灵敏度分析。
- **硬件部署成功**：在定制自行车平台上零样本迁移，并展示了人机协同和视觉导航两种高级功能，迁移比率在多数指标上接近1.0。
- **计算效率**：单块RTX 4090即可实现高效训练（70万步/秒），表明方法对硬件要求不高。

## 八、不足与局限
- **高速场景性能下降明显**：3-5 m/s时BSR降至86.21%，论文归因于高速转向的二次放大效应和PhysX仿真缺陷，但未提出具体改进。
- **真实世界基线缺失**：PID/LQR等基线在真实平台上未能稳定运行，因此缺少直接的真实对比量化数据，仅通过仿真对比间接说明。
- **部分指标转移比率较低**：航向跟踪误差的转移比率仅为0.56，临界角度容限为0.72，说明对IMU噪声和未建模动态的鲁棒性仍有提升空间。
- **域随机化的超参数依赖**：虽避免了手工建模，但奖励权重、随机化范围等仍需人工选择，存在启发式成分。
- **泛化性验证有限**：仅通过一次滑板车零样本迁移作展示，未在更多车型、载荷、极端天气下系统测试。
- **环境依赖**：训练依赖于NVIDIA Isaac Sim，迁移到其他仿真器可能需重新调整。

（完）
