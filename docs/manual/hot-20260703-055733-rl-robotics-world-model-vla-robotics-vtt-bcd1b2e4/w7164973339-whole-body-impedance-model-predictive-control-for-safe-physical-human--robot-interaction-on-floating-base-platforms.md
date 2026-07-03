---
title: Whole-Body Impedance Model Predictive Control for Safe Physical Human--Robot Interaction on Floating-Base Platforms
title_zh: 浮动基座平台上安全物理人机交互的全身阻抗模型预测控制
authors: Yongyan Cao
date: 2026-06-12
pdf: "https://arxiv.org/pdf/2606.14617"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 针对浮动基座机器人在持续人机交互力下稳态误差累积问题，提出三层阻抗MPC架构：质心MPC规划接触力，WBC层通过零空间投影保证平衡，剩余零空间由经卡尔曼增强的滚动时域QP预测并抑制人扰。接触一致反馈线性化将末端动态简化为常矩阵双积分器，支持≥1kHz实时优化；协方差膨胀确保接触模式切换时干扰估计连续。理论证明无限时域极限可恢复自适应阻抗律，在17-DOF双足与Unitree G1仿真中实现零稳态误差。
source: openalex
selection_source: hot_paper_scout
motivation: 现有浮动基座WBC在持续人机交互力下存在稳态误差，且固定增益阻抗缺乏干扰预测能力。
method: 三层架构：质心MPC规划接触力，WBC优先分解平衡，剩余零空间由带卡尔曼预测的滚动时域QP处理人扰；通过接触一致反馈线性化实现常状态矩阵，允许离线QP预计算。
result: 在17-DOF双足和Unitree G1人形机器人仿真中，该方法实现≥1kHz实时优化，对恒定有界pHRI负载达到零稳态误差。
conclusion: 提出一种可同时保证平衡与柔顺交互的三层阻抗MPC框架，理论证明其可恢复自适应阻抗律，仿真验证有效性。
---

## 摘要
浮动基座机器人必须在刚性接触约束下保持平衡，同时安全地与人类交互。现有的全身控制（WBC）框架将整个关节空间分配给运动，或依赖于固定增益的阻抗反馈，在持续的物理人机交互（pHRI）力作用下会积累稳态误差。本文通过一个三层架构将作者原有的固定基座双层阻抗模型预测控制（Impedance MPC）扩展到浮动基座平台：一个质心MPC在500毫秒范围内规划接触力；一个优先级驱动的WBC层通过接触一致的零空间投影将平衡问题分解为关节力矩；剩余的零空间由一个滚动时域二次规划（QP）控制，该QP使用卡尔曼增强状态预测并抑制pHRI干扰。接触一致的反馈线性化将手臂末端执行器模型简化为一个在每个接触模式下具有恒定状态矩阵的双积分器，从而支持QP代价的离线预计算和≥1 kHz的运行频率。协方差膨胀协议在接触模式切换时保持干扰估计，确保在有界恒定pHRI负载下稳态误差为零。阻抗等价定理表明，无限时域极限恢复了一个经典的任务空间阻抗定律，其有效质量、阻尼和刚度随姿态和接触构型自适应调整。在17自由度双足机器人和Unitree G1人形机器人上的仿真验证了该设计。

## Abstract
Floating-base robots must balance under rigid contact constraints while interacting safely with humans. Existing whole-body control~(WBC) frameworks allocate the full joint space to locomotion or rely on fixed-gain impedance feedback that accumulates steady-state error under sustained physical human--robot interaction~(pHRI) forces. This paper extends the authors' fixed-base two-layer Impedance MPC to floating-base platforms through a three-level architecture: a centroidal MPC plans contact forces over a 500\,ms horizon; a priority-driven WBC layer resolves balance into joint torques through contact-consistent null-space projection; and the residual null space is governed by a receding-horizon quadratic program~(QP) that predicts and rejects pHRI disturbances using a Kalman-augmented state. A contact-consistent feedback linearization reduces the arm end-effector plant to a double integrator with a \emph{constant} state matrix within each contact mode, enabling offline precomputation of the QP cost and ${\geq}1$\,kHz operation. A covariance-inflation protocol preserves the disturbance estimate across contact-mode switches, guaranteeing zero steady-state error under bounded constant pHRI loads, and an Impedance Equivalence Theorem shows the infinite-horizon limit recovers a classical task-space impedance law whose effective mass, damping, and stiffness adapt to posture and contact configuration. Simulations on a 17-DOF biped and the Unitree G1 humanoid validate the design.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：浮动基座机器人（如双足/四足人形机器人）在执行任务时必须同时满足与地面保持刚性接触的平衡约束，并在物理人机交互（pHRI）中安全地与人互动。现有全身控制（WBC）框架存在两大局限：一是将全部关节空间分配给运动或姿态维持，无法主动调节外臂交互；二是采用固定增益的阻抗反馈，在持续的人机交互力作用下会产生不可忽略的稳态误差（例如经典PD控制下误差与刚度倒数成正比）。
- **背景**：已有质心MPC（如MIT Cheetah 3）和分层WBC（如ANYmal）主要面向纯运动，缺乏对持续扰动的预测和零稳态误差的保证；而固定基座阻抗MPC无法处理浮动基座的未驱动基座和接触约束耦合。
- **研究意义**：填补浮动基座平台上兼具平衡保持、接触约束满足和零稳态误差柔顺交互的技术空白。

## 二、论文提出的方法论
- **核心思想**：提出三层阻抗MPC架构，在保证平衡和不违反接触约束的前提下，利用模型预测和卡尔曼扰动估计实现末端执行器对持续人机交互力的零稳态误差跟踪。
- **技术细节**：
  1. **Level 1 – 质心MPC**（40–100 Hz）：基于单刚体动力学（SRBD）模型在500 ms时域内规划质心轨迹和地面反作用力。
  2. **Level 2 – 全身控制WBC**（500 Hz）：采用Sentis–Khatib 优先级零空间投影（SK05定律），将Level 1的接触力分解为关节力矩，保证平衡和接触维护；手臂末端任务槽保持开放。
  3. **Level 3 – 阻抗MPC（≥1 kHz）**：残留的零空间用于手臂末端。关键技术包括：
     - **接触一致反馈线性化**：利用接触一致质量逆 $\bar{M}^{-1}$ 进行前馈补偿，将末端动力学简化为双积分器，状态转移矩阵 $A_d$ 在固定接触模式下为常数，允许离线预计算QP代价矩阵和Cholesky分解。
     - **滚动时域QP**：在每个接触模式下，输入矩阵 $B_d^{(m)}$ 被预先索引和存储，QP问题为严格凸，OSQP求解<0.1 ms（$N=20$）。
     - **卡尔曼扰动增强**：状态扩增引入干扰估计 $\hat{d}$，同时估计pHRI力、未建模腿部动量变化和SRBD近似误差。积分结构确保对有界常值扰动零稳态误差。
     - **接触模式切换协议**：协方差膨胀（$\alpha = 3-5$）保留扰动估计，不重置，加速重新收敛；切换后加载对应的 $B_d^{(m)}$。
  4. **阻抗等价定理**：在无约束无限时域极限下，所提MPC退化为经典任务空间阻抗律 $ \Lambda_{arm} \ddot{e} + \Lambda_{arm} D_d \dot{e} + \Lambda_{arm} K_d e = F_h$，有效质量、阻尼、刚度通过 $\Lambda_{arm}(q)$ 自适应于手臂姿态和接触构型。
  5. **完整关节力矩**：$\tau = \tau_{contact} + \bar{N}_1^\top \tau_{balance} + \bar{N}_{12}^\top \left[ \tau_{ff,arm} + J_{arm}^\top F_{mpc} + \tau_{null} \right]$，层次化零空间投影保证各层不互相干扰。

## 三、实验设计
- **仿真平台**：MuJoCo 3.2，积分步长2 kHz。
- **实验场景与机器人模型**：
  - **双足模型**（自行设计）：17-DOF（6未驱动基座+11驱动关节），46 kg。场景A：固定双支撑，8 N阶跃pHRI力持续4.5 s。场景B：固定双支撑，持续8 N pHRI力 + 1 Hz 6 N冲击（0.1 s）。
  - **Unitree G1官方模型**（MuJoCo Menagerie）：29-DOF，33.3 kg，位置控制（$K_p=500$），通过位置-力矩近似注入阻抗力。场景C：固定站立，同8 N阶跃。
- **对比方法**（7种）：
  - D1：SK05 PD（$K_P=800$ N/m, $K_D=40$ Ns/m）
  - D2：SK05 PI（额外积分项，$K_I=150$ N/(m·s)）
  - D3：固定基座阻抗MPC（使用 $M^{-1}$ 而非 $\bar{M}^{-1}$）
  - D4：WBC + PD（正确零空间，无预测）
  - D5：提出方法（WBC + 阻抗MPC，无卡尔曼）
  - D6：提出方法（WBC + 阻抗MPC + 卡尔曼，无协方差膨胀 $\alpha=1$）
  - D7：完整提出方法（WBC + 阻抗MPC + 卡尔曼 + 协方差膨胀 $\alpha=4$）
- **评价指标**：RMS误差、稳态误差、接触切换时峰值误差。

## 四、资源与算力
- **文中未明确说明使用的GPU型号、数量或训练时长**。所有实验基于MuJoCo物理仿真，控制器运行在CPU（OSQP求解QP <0.1 ms），未涉及大规模训练；Level 1/2/3 全为在线优化或解析计算，无离线训练过程。
- 控制器更新频率：Level 1 100 Hz，Level 2 500 Hz，Level 3 ≥1 kHz。仿真时间步2 kHz。

## 五、实验数量与充分性
- **实验数量**：共3个主要场景（A、B、C），每个场景对比7种控制器（D1–D7），合计21组对比数据输出（表III、IV、V）。此外包含理论证明和消融分析（有无卡尔曼、有无协方差膨胀、是否使用 $\bar{M}^{-1}$）。
- **充分性与客观性**：
  - 场景A验证固定接触下零稳态误差性质，理论预测与实验吻合（D1稳态10.16 mm vs 理论10.0 mm）。
  - 场景B验证接触切换时的暂态性能，峰值误差对比清晰，协方差膨胀效果明显（D6 vs D7峰值4.32→4.15 mm）。
  - 场景C在真实商业人形机器人模型（Unitree G1）上验证，确认框架泛化性，但性能下降（位置控制带宽限制）被合理讨论。
- **不足**：缺少动态行走或跑步场景、缺失真实硬件实验。消融实验较为全面，但仅用一个扰动幅值（8 N）可能不足。结论基于仿真，需谨慎推广。

## 六、论文的主要结论与发现
- 提出的三层全身阻抗MPC架构在仿真中实现了：
  - 在固定接触模式下，对恒定有界pHRI力实现**零稳态误差**（D7稳态0.037 mm vs D1 10.16 mm，提升273倍）。
  - 接触模式切换时，采用协方差膨胀可将峰值误差从4.32 mm降至4.15 mm，验证了暂态界公式。
  - 使用接触一致质量逆 $\bar{M}^{-1}$ 是必要的：使用 $M^{-1}$ 的固定基座MPC（D3）误差反而更大（11.9 mm vs 0.037 mm）。
  - 无限时域极限下恢复经典阻抗律，且有效阻抗参数随构型自适应调整。
  - 在Unitree G1上获得2.5倍于PD控制的稳态误差改善（9.57 mm→3.90 mm），但受限于位置控制带宽。

## 七、优点
- **方法创新**：首次将两层阻抗MPC从固定基座扩展到浮动基座，引入接触一致反馈线性化维持常状态转移矩阵，实现≥1 kHz实时优化。
- **理论严谨**：提供阻抗等价定理、零稳态误差证明（基于PBH可镇定性和卡尔曼积分结构）、接触切换暂态界。
- **架构实用性**：分层零空间投影保证上层平衡不受下层干扰；离线预计算QP代价，在线仅为矩阵-向量乘法，适合实际部署。
- **对比充分**：与多种基线（PD、PI、固定基座MPC、无卡尔曼变体）对比，消融实验覆盖关键设计选择（$\bar{M}^{-1}$、卡尔曼、协方差膨胀）。
- **验证平台多样**：自行设计双足和商业Unitree G1，增强适用性。

## 八、不足与局限
- **缺乏真实硬件验证**：所有实验在MuJoCo仿真中进行，实际机器人（尤其Unitree G1位置控制带宽低至5 Hz）可能无法复现1 kHz MPC的全部性能，文中已承认位置执行器会衰减校正。
- **实验覆盖有限**：仅测试固定站姿（双支撑）和单一幅值（8 N）的扰动，未考虑动态行走、奔跑、单支撑或多支撑变化、大幅交互力（可能触发饱和）等更复杂情况。
- **假设条件限制**：假设刚性接触、恒定接触模式内状态转移矩阵常数、SRBD近似误差由卡尔曼吸收但未建模高动态影响。未考虑接触滑移、柔性地面或非刚性交互。
- **对比基线可能不公**：所提方法使用了卡尔曼状态估计和MPC，而基线如D1仅为PD，未进行公平tuning（如提高$K_P$可能降低稳态误差但牺牲稳定性）。
- **Scalability分析缺失**：虽然QP很快，但未讨论对于更高DOF机器人（如全身>30 DOF）的实时性是否保持，以及接触模式数量增多时预计算库大小。
- **计算资源依赖**：依赖于离线预计算每个接触模式的QP代价，对于非常复杂或动态变化的接触模式（如非周期触点）可能不适用。

（完）
