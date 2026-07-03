---
title: "CycleRL: Sim-to-Real Deep Reinforcement Learning for Robust Autonomous Bicycle Control"
title_zh: CycleRL：面向鲁棒自主自行车控制的仿真到现实深度强化学习
authors: "Gelu Liu, Teng Wang, Z Z Wu, J I A H U I Wu, Songyuan Li, Xiangwei Zhu"
date: 2026-06-16
pdf: "https://arxiv.org/pdf/2603.15013"
tags: ["query:热点论文筛选", "query:topic", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; institutions=Sun Yat-sen University; query=classic mobile robot trajectory optimization methods"
tldr: "针对欠驱动自行车在真实环境中模型失配与适应性不足的问题，提出CycleRL框架，在高保真NVIDIA Isaac Sim中利用PPO优化感知-动作映射，并设计复合奖励函数同时控制平衡、速度和转向；通过系统域随机化弥合仿真到现实的鸿沟。仿真中平衡成功率99.90%，航向误差1.15°，速度误差0.18 m/s，且成功部署到硬件，验证了DRL相比传统方法的卓越适应性。"
source: openalex
selection_source: hot_paper_scout
motivation: 传统控制策略难以应对欠驱动自行车系统的非线性动态、模型偏差和真实环境不确定性，亟需鲁棒且自适应的解决方案。
method: 在NVIDIA Isaac Sim中建立CycleRL框架，使用PPO优化直接感知-动作策略，结合复合奖励函数与域随机化实现平衡、速度跟踪和转向控制。
result: "仿真实现99.90%平衡成功率、1.15°航向误差和0.18 m/s速度误差，并成功转移到真实硬件。"
conclusion: CycleRL证明深度强化学习是实现欠驱动自行车鲁棒控制的有效范式，显著优于传统控制方法。
---

## 摘要
自主自行车为城市出行和最后一公里物流提供了一种有前景的敏捷解决方案。然而，传统控制策略往往难以应对欠驱动非线性动力学，对模型失配敏感，且对现实世界不确定性的适应性有限。为此，我们开发了CycleRL，一个面向鲁棒自主自行车控制的全面仿真到现实框架。我们的方法在高保真NVIDIA Isaac Sim环境中建立了直接的感知到动作映射，利用近端策略优化（PPO）来优化控制策略。该框架具有一个为同时保持平衡、速度跟踪和转向控制而量身定制的复合奖励函数。关键在于，采用系统化的域随机化来减少对精确系统建模的依赖，弥合仿真与现实之间的差距，并促进直接迁移。在仿真中，CycleRL实现了有前景的性能，包括99.90%的平衡成功率、1.15°的航向跟踪误差和0.18 m/s的速度跟踪误差。这些定量结果，加上成功的硬件部署，验证了DRL作为自主自行车控制的有效范式，相比传统方法具有更优越的适应性。视频演示可在https://cpnt-lab.github.io/CycleRL/观看。

## Abstract
Autonomous bicycles offer a promising agile solution for urban mobility and last-mile logistics. However, conventional control strategies often struggle with underactuated nonlinear dynamics, suffering from sensitivity to model mismatches and limited adaptability to real-world uncertainties. To address this, we develop CycleRL, a comprehensive sim-to-real framework for robust autonomous bicycle control. Our approach establishes a direct perception-to-action mapping within the high-fidelity NVIDIA Isaac Sim environment, leveraging Proximal Policy Optimization (PPO) to optimize the control policy. The framework features a composite reward function tailored for concurrent balance maintenance, velocity tracking, and steering control. Crucially, systematic domain randomization is employed to reduce the reliance on precise system modeling, bridge the simulation-to-reality gap and facilitate direct transfer. In simulation, CycleRL achieves promising performance, including a 99.90% balance success rate, a heading tracking error of 1.15°, and a velocity tracking error of 0.18 m/s. These quantitative results, coupled with successful hardware deployment, validate DRL as an effective paradigm for autonomous bicycle control, offering superior adaptability over traditional methods. Video demonstrations are available at https://cpnt-lab.github.io/CycleRL/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **问题**：自主自行车是欠驱动、非线性、非完整约束系统，传统控制方法（PID、LQR、MPC、模糊逻辑等）高度依赖精确动力学模型，对参数失配和真实环境不确定性（如路面变化、传感器噪声）敏感，鲁棒性和适应性差。
- **需求**：需要一种不依赖精确模型、能从仿真高效迁移到真实场景、且能同时维持平衡、速度跟踪和转向控制的鲁棒控制器。
- **贡献**：提出CycleRL框架，首次将深度强化学习（DRL）与系统化的域随机化相结合，实现欠驱动自行车的稳健实物控制，仿真达到99.90%平衡成功率，并成功部署于真实自行车平台。

## 二、论文提出的方法论
- **核心思想**：在高保真仿真器（NVIDIA Isaac Sim）中训练一个从感知观测（IMU、编码器）直接到执行器动作（转向、驱动）的随机策略，采用PPO算法优化，避免显式动力学建模。
- **关键技术细节**：
  1. **马尔可夫决策过程（MDP）建模**：状态空间为瞬时观测（IMU+编码器），动作空间为连续（转向角、电机速度），奖励函数为复合式，折扣因子γ用于长期回报。
  2. **复合奖励函数**（公式3）：
     - 生存奖励（\(r_{surv}=1\)）：鼓励持续运行。
     - 速度跟踪奖励（\(r_{vel}=\exp(-0.25|v_{actual}-v_{cmd}|)\)）。
     - 航向跟踪奖励（\(r_{head}=\exp(-0.1|\psi_{actual}-\psi_{desired}|)\)）。
     - 动作幅度惩罚（\(r_{act}=-\|a_t\|^2\)）：抑制过大动作。
     - 动作变化率惩罚（\(r_{rate}=-\|a_t - a_{t-1}\|^2\)）：保证平滑。
     - 权重：\(\lambda_{surv}=1.0,\ \lambda_{vel}=3.0,\ \lambda_{head}=5.0,\ \lambda_{act}=1.0,\ \lambda_{rate}=2.0\)。
  3. **域随机化策略**（表I）：
     - **动力学随机化**：总质量[15,45]kg、质心高度[0.5,0.8]m、摩擦系数[0.5,1.2]、执行器增益[0.9,1.1]、观测噪声（幅值1%-20%）。
     - **初始状态随机化**：初始速度[1.0,2.5]m/s、初始倾斜角[-10°,10°]、伺服/轮毂电机初始位置随机。
     - **任务/指令随机化**：目标速度[1.0,5.0]m/s、目标航向[-10°,10°]，每3-5秒重新采样。
  4. **训练算法**：PPO（公式9），使用GAE计算优势，裁剪比率限制在[1-ε,1+ε]。
- **公式流程**：输入观测 → MLP策略网络输出动作 → 环境反馈复合奖励 → PPO更新策略。训练在Isaac Sim中以16384并行环境并行执行。

## 三、实验设计
- **仿真环境**：NVIDIA Isaac Sim（GPU加速物理引擎），包含高级接触、执行器动力学、可变摩擦和IMU噪声。
- **基准方法**：PID（双环结构，Ziegler-Nichols调参）、LQR（线性化模型，实时求解Riccati方程）、MLCL（改进线性控制律）。所有基线在仿真中以相同条件（目标速度2.0 m/s）调参，采用零样本迁移到硬件。
- **评估指标**（表II）：
  - 平衡：Balance Success Rate (BSR)、Balance Recovery Time (BRT)、Max Balance Duration (MBD)、Critical Angle Tolerance (CAT)。
  - 控制：Heading Tracking Error (HTE)、Velocity Tracking Error (VTE)、System Response Latency (SRL)。
  - 鲁棒性：Maximum Noise Tolerance (MNT)、Minimum Sustaining Speed (MSS)。
- **主要仿真实验**：10000个随机episode（保留初始状态和指令随机化，无动力学随机化），结果如表III。
- **鲁棒性实验**（表V）：速度区间（1-3 m/s vs 3-5 m/s）、传感器退化（无噪声、最大噪声20%、丢包10%）、地形（平坦、粗糙路面、砾石、斜坡、阶梯）。
- **消融实验**（表IV和表VI）：奖励函数各分量剔除；域随机化各组件（无随机、仅动力学、仅初始状态、仅命令、仅地形、完整）。
- **敏感性分析**（图6）：对5个奖励权重分别缩放0.1×至5.0×，观察BSR、HTE、VTE变化。
- **硬件验证**：自定义自行车（表VII），含Jetson Orin NX、IMU、伺服电机、轮毂电机；采用零样本直接部署策略；与仿真性能对比（转移比）；额外测试视觉车道线跟踪和不同地形/负载/扰动。

## 四、资源与算力
- **GPU**：单块NVIDIA RTX 4090。
- **并行环境数**：16384个并行仿真环境。
- **仿真速度**：超过700,000步/秒。
- **训练轮次**：约1000个epoch后稳定收敛（约7亿仿真步）。文中未明确给出总训练时长（如小时数），但提及每次训练在单卡上完成。

## 五、实验数量与充分性
- **实验规模**：仿真评估使用10,000个独立episode（BSR等指标）；训练曲线使用10个随机种子；消融实验均重复多次；硬件实验涵盖多种条件（至少十种以上场景，包括不同路面、速度、负载、扰动）。
- **充分性与公正性**：
  - 基线方法在仿真中使用典型调参，并采用零样本迁移到硬件（与CycleRL相同条件），结果基线硬件失败，证明了CycleRL的优势。
  - 消融实验覆盖了所有关键组件（奖励项、随机化策略），验证了各部分贡献。
  - 敏感性分析展示了权重选取的合理性，但未进行全域超参搜索。
  - 硬件实验缺少与基线在真实世界的定量对比（因为基线无法启动），但通过转移比和视频证据说明了性能。
  - 整体实验设计较为系统、结果客观，但未测试不同自行车几何参数变体或极端天气条件。

## 六、论文的主要结论与发现
- CycleRL在仿真中达到**99.90%平衡成功率**，显著优于PID（76.50%）、LQR（93.24%）和MLCL（96.43%）。
- 航向跟踪误差仅**1.15°**，速度误差**0.18 m/s**，恢复时间最短（1.05 s），临界倾斜角最大（27.79°）。
- 域随机化对实物迁移至关重要：无随机化的策略在仿真中BSR接近100%，但HTE恶化（5.16° vs 1.15°），VTE也显著升高。
- 成功零样本迁移到真实硬件，BSR达95%，最大持续平衡超1800秒，最低稳定速度1.33 m/s，并验证了多场景鲁棒性（斜坡、砾石、负载变化、视觉导航）。
- 证明DRL是欠驱动自行车控制的有效范式，尤其适合对模型不确定性鲁棒性要求高的实物应用。

## 七、优点
- **端到端框架**：直接从感知映射到动作，无需显式动力学建模或繁琐的系统辨识，简化了控制管线。
- **精心设计的复合奖励函数**：平衡了稳定、跟踪和效率，通过权重调节避免“站住不动”的次优策略。
- **全面且系统的域随机化**：覆盖动力学、初始状态、指令和地形，显著提升了零样本泛化能力，消融实验证实其必要性。
- **广泛的实物验证**：在真实自行车平台上测试了多种地形、速度、负载、传感器噪声、横向扰动，甚至集成车道视觉实现自主导航，验证了实用性。
- **可复现性**：使用开源仿真器（Isaac Sim）和常见硬件组件，公开了视频和代码信息。

## 八、不足与局限
- **高速性能下降**：在3-5 m/s速度区间BSR降至86.21%，主要因高速转弯时的侧向加速度与执行器延迟耦合，以及仿真器物理精度限制。
- **域随机化引入保守性**：相比“无随机化”策略，完整随机化策略在理想仿真条件下BSR略低（99.90% vs 99.99%），体现了性能-鲁棒性权衡，但在实际部署中是可接受的。
- **奖励函数工程设计依赖**：虽然敏感性分析验证了权重，但奖励形状和权重选择仍需手工调参，未采用自动化方法（如贝叶斯优化）。
- **硬件实验定量对比不足**：由于基线零样本迁移失败，无法直接与PID/LQR在真实平台上进行公平的定量比较，仅以转移比和定性结果说明优势。
- **物理平台特定性**：策略仅在一种自行车几何参数上训练和验证，未测试不同轴距、质量分布或轮径变化；零样本迁移到滑板车仅有视频证据，缺乏定量指标。
- **控制器频率与通信延迟**：固定50 Hz控制率，未考虑更高频率或硬件延迟对策略性能的详细影响。
- **环境泛化性**：仿真中未涵盖雨雪、强风等复杂气候，真实实验也未在雨天或极端路面进行。

（完）
