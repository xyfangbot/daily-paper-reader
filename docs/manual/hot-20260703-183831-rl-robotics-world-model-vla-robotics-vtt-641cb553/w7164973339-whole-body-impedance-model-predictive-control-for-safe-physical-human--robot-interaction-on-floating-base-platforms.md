---
title: Whole-Body Impedance Model Predictive Control for Safe Physical Human--Robot Interaction on Floating-Base Platforms
title_zh: 全身阻抗模型预测控制在浮动基座平台上的安全物理人机交互
authors: Yongyan Cao
date: 2026-06-12
pdf: "https://arxiv.org/pdf/2606.14617"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 浮动基座机器人在与人物理交互时需同时维持平衡和柔顺，现有全身体制控制存在稳态误差或计算效率低的问题。本文提出三层阻抗模型预测控制架构：质心MPC规划接触力，优先级WBC保证平衡，滚动时域QP利用卡尔曼估计预测并抑制外力扰动。通过接触一致反馈线性化实现QP成本离线预计算，运行频率达1kHz以上，并证明无限时域下恢复经典阻抗控制。在双足和人形机器人仿真中验证了零稳态误差的柔顺交互性能。
source: openalex
selection_source: hot_paper_scout
motivation: 现有全身体制控制框架在持续人机物理交互力下积累稳态误差，且固定增益阻抗反馈无法适应动态接触条件。
method: 提出质心MPC、优先级WBC和基于卡尔曼增强状态的滚动时域QP三层架构，通过接触一致反馈线性化将末端执行器简化为双积分器。
result: 在17-DOF双足和Unitree G1人形机器人仿真中实现零稳态误差位置跟踪，QP运行频率≥1kHz。
conclusion: 该方法通过离线预计算和协方差膨胀协议，保证实时性同时实现浮动基座安全交互，无限时域下等价于自适应阻抗控制。
---

## 摘要
浮动基座机器人必须在刚性接触约束下保持平衡，同时与人类安全交互。现有的全身控制（WBC）框架将整个关节空间分配给运动，或依赖固定增益阻抗反馈，在持续物理人机交互（pHRI）力作用下会累积稳态误差。本文通过三层架构将作者的固定基座双层阻抗MPC扩展到浮动基座平台：一个质心MPC在500毫秒时域内规划接触力；一个优先级驱动的WBC层通过接触一致性零空间投影将平衡解算为关节扭矩；残差零空间由递推时域二次规划（QP）控制，该QP使用卡尔曼增广状态预测并抑制pHRI干扰。一种接触一致性反馈线性化将手臂末端执行器模型简化为在每个接触模式下具有恒定状态矩阵的双积分器，从而实现QP代价的离线预计算和≥1 kHz的运行频率。一种协方差膨胀协议在接触模式切换时保持干扰估计，确保在有界恒定pHRI负载下零稳态误差，并且阻抗等价定理表明无限时域极限恢复了经典任务空间阻抗定律，其有效质量、阻尼和刚度自适应于姿态和接触配置。在17自由度双足机器人和Unitree G1人形机器人上的仿真验证了该设计。

## Abstract
Floating-base robots must balance under rigid contact constraints while interacting safely with humans. Existing whole-body control~(WBC) frameworks allocate the full joint space to locomotion or rely on fixed-gain impedance feedback that accumulates steady-state error under sustained physical human--robot interaction~(pHRI) forces. This paper extends the authors' fixed-base two-layer Impedance MPC to floating-base platforms through a three-level architecture: a centroidal MPC plans contact forces over a 500\,ms horizon; a priority-driven WBC layer resolves balance into joint torques through contact-consistent null-space projection; and the residual null space is governed by a receding-horizon quadratic program~(QP) that predicts and rejects pHRI disturbances using a Kalman-augmented state. A contact-consistent feedback linearization reduces the arm end-effector plant to a double integrator with a \emph{constant} state matrix within each contact mode, enabling offline precomputation of the QP cost and ${\geq}1$\,kHz operation. A covariance-inflation protocol preserves the disturbance estimate across contact-mode switches, guaranteeing zero steady-state error under bounded constant pHRI loads, and an Impedance Equivalence Theorem shows the infinite-horizon limit recovers a classical task-space impedance law whose effective mass, damping, and stiffness adapt to posture and contact configuration. Simulations on a 17-DOF biped and the Unitree G1 humanoid validate the design.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：浮动基座机器人（如双足、四足、人形机器人）在执行任务时，必须同时维持与地面的刚性接触约束（平衡）和与人类的柔顺物理交互（pHRI）。现有全身控制（WBC）框架存在两类缺陷：一是将全部控制权分配给运动，将外部交互视为干扰并强力抑制；二是采用固定增益阻抗反馈，在持续外力下产生不可消除的稳态误差。因此缺乏一种既能保证平衡、又能实现零稳态误差的柔顺交互控制方法。
- **研究背景**：经典阻抗控制假设基座固定；质心MPC主要负责运动，未考虑手臂交互；固定基座阻抗MPC无法处理浮动基座的欠驱动特性。本文目标是填补这一技术空白，将作者此前提出的固定基座双层阻抗MPC扩展到浮动基座平台，并保证实时性（≥1 kHz）和零稳态误差。

## 二、论文提出的方法论
- **核心思想**：提出三层架构（Level 1–3），将手臂的柔顺交互控制作为残差零空间中的预测性阻抗MPC，与上层平衡/接触任务解耦。关键创新是接触一致性反馈线性化，将手臂末端执行器模型在每个接触模式下简化为线性双积分器，使得QP成本矩阵可离线预计算，支撑1 kHz以上更新率。
- **关键技术细节**：
  1. **Level 1 – 质心MPC**（40–100 Hz）：基于单刚体动力学（SRBD）模型，在500 ms时域内规划质心轨迹和地面反力（GRF）。
  2. **Level 2 – 优先级WBC层**（500 Hz）：采用Sentis-Khatib接触一致性零空间投影，将Level 1规划的GRF解算为关节扭矩，优先满足接触保持与平衡任务，将手臂任务槽预留为开放。
  3. **Level 3 – 阻抗MPC**（≥1 kHz）：在残差零空间中运行滚动时域QP。
     - 通过接触一致性反馈线性化，将手臂末端执行器误差动力学简化为线性双积分器：\(\ddot{e} = -\Lambda_{\text{arm}}^{-1} F_{\text{mpc}} + d(t)\)，其中状态转移矩阵 \(A_d\) 在固定接触模式下恒定。
     - 输入矩阵 \(B_d^{(m)}\) 随接触模式索引（双足、三足等）预计算，形成库。
     - 采用卡尔曼滤波增广状态（误差+扰动），扰动状态包括pHRI力、未建模腿动量变化、SRBD近似误差。增广矩阵为9×9，保证稳定性和零稳态误差。
     - QP的代价矩阵\(H^{(m)}\)及其Cholesky因子可离线计算，在线更新仅为矩阵-向量乘，QP求解时间<0.1 ms（N=20）。
  4. **接触切换处理**：协方差膨胀协议（α=3~5），保留扰动估计，允许卡尔曼快速重新收敛，避免重置。
  5. **阻抗等价定理**：证明无约束无限时域极限下，该方法恢复经典任务空间阻抗控制，且有效质量、阻尼、刚度通过\(\Lambda_{\text{arm}}(q)\)自动适应姿态和接触配置，无需在线优化。
- **完整扭矩公式**：\(\tau = \tau_{\text{contact}} + \bar{N}_1^{\top} \tau_{\text{balance}} + \bar{N}_{12}^{\top} [\tau_{\text{ff,arm}} + J_{\text{arm}}^{\top} F_{\text{mpc}} + \tau_{\text{null}}]\)，层次化零空间保护保证手臂MPC不破坏上层平衡。

## 三、实验设计
- **仿真平台**：MuJoCo 3.2物理引擎，采样率2 kHz。
- **场景与机器人**：
  - **场景A**：17自由度双足机器人（3自由度右臂，2×4自由度腿，6自由度浮动基座，总质量46 kg），固定双足支撑，施加8 N阶跃pHRI力（x方向），持续4.5 s。
  - **场景B**：同机器人，固定双足支撑，施加持续8 N pHRI + 1 Hz周期冲击（6 N，0.1 s）。
  - **场景C**：Unitree G1官方MJCF模型（29自由度，33.3 kg），固定支撑，8 N阶跃pHRI力。
- **Benchmark & 对比方法**：共7种控制器（D1–D7）：
  - D1：SK05 PD（KP=800 N/m，KD=40 Ns/m）
  - D2：SK05 PI（外加KI=150 N/(m·s)）
  - D3：固定基座阻抗MPC（使用自由空间质量逆\(M^{-1}\)，而非接触一致性\(\bar{M}^{-1}\)）
  - D4：WBC层次+PD（正确零空间，无预测）
  - D5：提出架构但不含卡尔曼滤波
  - D6：提出架构+卡尔曼但无协方差膨胀（α=1）
  - D7：提出架构完整版（含卡尔曼+协方差膨胀 α=4）
- **评价指标**：RMS误差（全过程）、稳态误差（末尾平均值）、峰值误差（接触切换时）。
- **参数**：Level 1: 100 Hz, N=10；Level 2和Level 3: 1 kHz, N=20；摩擦力锥半角μ=0.6；代价权重Q=diag(6e4 I₃, 60 I₃)，R=0.01 I₃；卡尔曼噪声Q_w, R_v设定。

## 四、资源与算力
- **文中未明确说明使用的GPU型号、数量、训练时长**。所有实验均基于MuJoCo物理仿真进行，控制算法在CPU上实时运行（QP求解<0.1 ms）。未提及大规模并行训练或深度学习训练，因此无相关GPU算力消耗。文中仅注明仿真整合率2 kHz，控制频率1 kHz，QP求解器OSQP。

## 五、实验数量与充分性
- **实验数量**：论文设置了三个场景（A固定支撑阶跃扰动、B固定支撑+周期冲击、C真实人形模型），每个场景对比7种控制器（D1–D7），覆盖消融（无卡尔曼、无膨胀、使用错误质量逆）和基线（PD、PI、WBC+PD、固定基座MPC）。总计3×7=21组实验结果（每个场景给出RMS和稳态误差/峰值等指标）。此外还提供了时序图（Fig. 1–3）和表格（Table III–V）。
- **充分性与公平性**：
  - 消融设计合理：逐步去掉或替换关键组件（卡尔曼、协方差膨胀、接触一致性质量逆），有效验证各部分贡献。
  - 基线选择具有代表性：PD（标准阻抗）、PI（积分控制抗零差）、固定基座MPC（忽略浮动基座耦合）、WBC+PD（当前主流层次控制）。
  - 所有控制器共用同一仿真设置、同一扰动输入、同一机器人模型，确保公平。
  - **局限性**：仅包含仿真实验，无真实硬件验证；仅测试了固定支撑和简单周期冲击，未测试动态步行中的连续接触切换；未对更多扰动类型（如变方向、非线性摩擦）进行测试。

## 六、论文的主要结论与发现
1. **零稳态误差**：完整方法（D7）在固定支撑下对8 N持续pHRI力实现0.037 mm稳态误差，相比标准PD的10.2 mm提升约273倍，验证了定理2。
2. **接触一致性必要性**：使用自由空间质量逆（D3）的固定基座MPC在相同扰动下产生11.9 mm误差，证实接触一致性反馈线性化是关键。
3. **预测与卡尔曼缺一不可**：不包含卡尔曼（D5）时稳态误差8.5 mm，仅减少16%；加上卡尔曼（D6）降至0.037 mm；协方差膨胀（α=4）在接触冲击场景降低了峰值（4.15 vs 4.32 mm）。
4. **真实模型迁移**：在Unitree G1官方模型上（位置执行器，带宽5 Hz），完整方法稳态误差3.90 mm，是PD的2.5倍提升，证明了方法在实际硬件参数下的潜力。
5. **计算效率**：离线预计算QP代价后，在线求解<0.1 ms（N=20），支持≥1 kHz更新率。
6. **阻抗等价**：无限时域下恢复经典阻抗控制并具有姿态/接触自适应特性，设计参数（Kd, Dd）语义清晰。

## 七、优点
- **理论完备性**：从动力学推导到稳定性证明（定理1-2）、阻抗等价定理、接触切换瞬态界，逻辑链条完整。
- **计算高效**：通过离线预计算和恒定状态转移矩阵，实现1 kHz实时控制，适合实际嵌入式系统。
- **层次解耦清晰**：利用接触一致性零空间投影，保证手臂MPC不干扰平衡任务，简化系统设计与调参。
- **实验设计严谨**：包含充分消融、基线对比、不同机器人模型验证，结果量化且具有统计意义（RMS、稳态误差、峰值）。
- **可迁移性**：明确适用于任何接触-一致浮动基座机器人（双足、四足、人形），且代码/协议可直接对接Unitree等商用硬件的低层SDK。

## 八、不足与局限
- **仿真局限性**：所有实验均在MuJoCo仿真中进行，未在真实机器人上验证。真实硬件存在力传感器噪声、执行器延迟、柔性关节等未建模因素，性能可能下降。
- **实验场景有限**：仅测试了固定双足支撑下的静态/准静态接触变化，未包含动态行走中的连续接触切换（如踏步、越障）、非刚性接触（摩擦系数变化）、多人交互等情况。
- **扰动类型单一**：仅测试了恒定方向和周期的外力，未覆盖变方向、随机脉冲、非均匀分布扰动。
- **未考虑感知延迟**：假设外部扰动力可直接观测或通过卡尔曼准确估计，未探讨视觉/触觉反馈延迟对系统的影响。
- **位置执行器限制**：在Unitree G1上使用位置模式近似扭矩，导致带宽低，稳态误差从0.037 mm升至3.9 mm，说明方法对执行器性能敏感。
- **无通用开源实现**：论文未公开代码或仿真配置，可复现性受限。

（完）
