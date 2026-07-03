---
title: Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm
title_zh: 基于物理的Unitree G1人形机器人手臂电力消耗模型识别
authors: "Nestor N. Deniz, Sebastian Vega, Simon Parsons, Fernando Auat Cheein"
date: 2026-06-14
pdf: "https://arxiv.org/pdf/2606.15915"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=title; query=reinforcement learning for humanoid robot control and locomotion"
tldr: 电池供电人形机器人需精确预测电力消耗以支持能量感知规划与热管理。本文针对Unitree G1七自由度左臂，提出一种基于物理的线性参数功耗模型，融合执行器损耗项、重力补偿基线扭矩校正及多关节耦合交互项。利用897条实验轨迹识别参数，模型R²达0.933，RMSE仅1.07W；在46条新速度轨迹上验证R²=0.965，泛化能力优异。参数分析揭示各关节主导损耗机制（粘性摩擦、铜损或库仑摩擦），为节能运动控制提供依据。
source: openalex
selection_source: hot_paper_scout
motivation: 准确预测电力消耗对于人形机器人的节能运动规划、电池管理和热监测至关重要。
method: 提出了基于物理的线性参数功耗模型，结合执行器损耗、重力补偿校正和成对交互项，利用Unitree G1实验数据识别参数。
result: 在897条轨迹上R²=0.933、RMSE=1.07W，在46条未见速度轨迹上R²=0.965，泛化性强。
conclusion: 模型准确预测功耗且泛化性好，参数分析揭示关节损耗由粘性摩擦、铜损或库仑摩擦分别主导。
---

## 摘要
精确预测电力消耗对于电池供电的人形机器人的能量感知运动规划、电池管理和热监控至关重要。本文提出了一种基于物理的线性参数模型，用于Unitree G1人形机器人七自由度左臂的电力消耗。该公式将执行器损耗项与捕捉重力补偿负载变化的基准扭矩校正相结合，能够准确预测负净功率轨迹。引入成对交互项以模拟多关节同时运动时的功率耦合。模型参数通过在实际Unitree G1上收集的实验数据识别，以机载功率测量作为回归目标。在覆盖单关节和协调手臂运动、多种速度水平的897条轨迹中，识别模型的R²=0.933，RMSE为1.07 W。在以前未见速度下执行的46条轨迹上的验证得到R²=0.965，表明在识别数据集之外具有良好的泛化能力。对识别参数的分析揭示了手臂各关节不同的电力消耗特性：粘性摩擦主导大多数关节（肩部俯仰和所有三个腕关节），铜损主导肩部偏航和肘关节，而肩部滚动则独特地由库仑摩擦主导。

## Abstract
Accurate prediction of electrical power consumption is essential for energy-aware motion planning, battery management, and thermal monitoring in battery-powered humanoid robots. This letter presents a physics-based, linear-in-parameters model for the electrical power consumption of the seven-degree-of-freedom left arm of the Unitree~G1 humanoid robot. The proposed formulation combines actuator loss terms with a baseline-torque correction that captures changes in gravity-compensation load and enables accurate prediction of negative net power trajectories. Pairwise interaction terms are introduced to model power coupling during simultaneous multi-joint motion. Model parameters are identified from experimental data collected on a physical Unitree~G1 using onboard power measurements as the regression target. Across 897 trajectories covering single-joint and coordinated arm motions at multiple speed levels, the identified model achieves $R^2 = 0.933$ with an RMSE of 1.07 (W). Validation on 46 trajectories executed at previously unseen speeds yields $R^2 = 0.965$, demonstrating strong generalisation beyond the identification dataset. Analysis of the identified parameters reveals distinct power-consumption characteristics across the arm, with viscous friction dominating most joints (shoulder pitch and all three wrist joints), copper losses dominating shoulder yaw and the elbow, and shoulder roll uniquely dominated by Coulomb friction.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：电池供电的人形机器人（如Unitree G1）在执行物流、制造、农业等任务时，受限于有限电池容量，需要准确预测电力消耗以支持能量感知运动规划、电池管理、任务时长估计和热保护。在操作密集型任务中，上肢的功耗占机器人总功率预算的很大比例。
- **背景**：现有机器人能耗建模方法分为纯数据驱动（高精度但泛化能力有限）和详细电-机械物理模型（需详细的执行器参数，商用平台常不可得）。线性参数物理模型提供了一种折中，兼具物理可解释性和计算高效的参数辨识。
- **核心问题**：尚无针对现代人形机器人手臂的基于物理的线性-参数电力消耗模型，且现有模型很少考虑不同手臂姿态下重力补偿功率的变化以及多关节同时运动时的耦合效应。
- **整体含义**：填补人形机器人手臂电力消耗模型空白，为节能运动规划提供可解释且泛化性强的功耗预测工具。

## 二、论文提出的方法论
- **核心思想**：建立每个关节的净功率模型，公式由四项组成：机械功率项（τᵢq̇ᵢ乘以效率倒数aᵢ）、铜损项（bᵢ∆τᵢ²，其中∆τ²为相对于静态基线的平方扭矩偏差）、库仑摩擦项（cᵢ|q̇ᵢ|）、粘性摩擦项（dᵢq̇ᵢ²）。对于多关节同时运动，增加成对速度乘积交互项（eᵢⱼ|q̇ᵢ||q̇ⱼ|）。最终模型对所有关节求和，总共49个非负参数（每关节4个+21个交互系数）。
- **关键技术细节**：
  - **基线铜损校正**：定义静态基线功率为关节在静止姿态（q=0）时的功率，减去后得到净功率P_net,i = aᵢτᵢq̇ᵢ + bᵢ(τᵢ² - τ̄₀²) + cᵢ|q̇ᵢ| + dᵢq̇ᵢ²，其中τ̄₀²为静态窗口的平均平方扭矩。该校正允许模型预测负净功率（当手臂移向重力负载更低的构型时）。
  - **成对交互项**：eᵢⱼ|q̇ᵢ||q̇ⱼ| (i<j) 建模多轴同时运动时的功率耦合，来源于共享直流母线的传动系统相互作用。
  - **参数估计**：将模型写作线性形式P_net = φᵀθ。由于机载功率传感器采样率仅1 Hz，而运动数据为100 Hz，直接逐样本拟合导致病态（条件数极大，R²<0.04）。因此采用**轨迹级聚合**：每条轨迹内将所有样本的回归器和目标取平均，得到一个独立观测。最终使用带非负约束的二次规划（凸QP，IPOPT求解）估计θ。
- **算法流程**：采集数据→计算每条轨迹平均回归向量和平均净功率→异常值过滤（两阶段：IMU稳定性过滤+3σ残差迭代过滤）→约束最小二乘求解。

## 三、实验设计
- **平台与传感器**：实际Unitree G1人形机器人站立状态，左臂、Dex3-1手爪安装。使用主板上臂电源轨传感器（MBS，1 Hz采样，基线约120 W）作为回归目标。关节状态（位置、速度、估计扭矩）通过ROS2以100 Hz发布。
- **数据集**：单次录制会话共1017条轨迹。包括：
  - 7个关节的单关节扫描（肩部俯仰/滚转/偏航、肘、腕滚转/俯仰/偏航）
  - 所有两关节组合（含腕关节）
  - 三、四及更多关节组合；每个运动轨迹使用三次时间缩放，最大速度5个等级：0.5, 1.0, 1.5, 2.0, 2.5 rad/s。
  - 轨迹含前/后空闲段（2 s）以估计静态基线和平均扭矩。
- **过滤后**：IMU稳定性剔除104条（躯干因平衡补偿晃动），3σ残差剔除16条，最终保留M=897条轨迹用于识别。
- **验证集**：单独采集46条轨迹，使用完全相同的路径但最大速度为四个中间层级（0.75, 1.25, 1.75, 2.25 rad/s），这些速度在训练集中从未出现。
- **基准与对比**：未对比其他模型，而是通过自身拟合优度和验证集泛化证明模型有效性。主要评估指标：R²、RMSE、MAE。

## 四、资源与算力
- **计算资源**：文中未明确说明使用的GPU型号、数量或训练时长。参数辨识为凸二次规划（线性约束），在普通CPU上即可快速求解（作者使用CasADi+IPOPT）。无大规模深度学习训练。
- **数据采集**：物理机器人单次会话，未提及耗时。

## 五、实验数量与充分性
- **实验数量**：
  - 识别数据集：897条轨迹（过滤后），每条轨迹平均约1016个样本，覆盖单关节、2-3-4+关节组合及5个速度等级。
  - 验证集：46条轨迹，覆盖所有单关节扫掠、腕部2/3关节组合，4个未见速度。
- **充分性评估**：
  - **正面**：数据覆盖了从单关节到多关节、多种速度的广泛运动，由滤波确保了数据质量，验证集使用了训练中未出现的速度，测试泛化能力。
  - **不足**：所有实验仅在**左臂带有Dex3-1手爪**、机器人站立不动（右臂静止）条件下进行，未测试不同手爪、不同基座运动或多臂协同；仅与自身数据对比，未与其他功耗模型（如纯数据驱动、详细电机械模型）作横向比较。缺少消融实验评估各组件（如交互项、基线校正）的贡献。验证集仅46条，相对较小。
  - **公平性**：参数辨识过程有明确约束和滤波，结果客观。但缺乏与已有流行模型的基准对比，因此难以判断绝对优势。

## 六、论文的主要结论与发现
- **模型精度**：
  - 识别集（897条）：R²=0.933，RMSE=1.07 W，MAE=0.86 W。残差接近高斯分布（偏度0.15，峰度2.97）。
  - 验证集（46条，未见速度）：R²=0.965，RMSE=3.58 W（相对全量程121.7 W约为2.9%），MAE=2.33 W，轻微欠预测（偏差-0.72 W）。R²高于训练集，表明模型未过拟合且泛化良好。
- **各关节主导损耗机制**（表I）：
  - **粘性摩擦主导**：肩部俯仰、所有三个腕关节（腕偏航系数最大d₆=1.7848 W·s²/rad²）。
  - **铜损主导**：肩部偏航（b₂=0.2799）、肘关节（b₃=0.3942）。
  - **库仑摩擦主导**：肩部滚动（c₁=1.2767）。
  - 腕俯仰（c₅=0.3464, b₅=0.3768, d₅=1.2004）是唯一三个机制贡献较均衡的关节。
- **功率项贡献**（验证集分析）：铜损42.4%、粘性摩擦38.2%、机械功率10.1%、库仑摩擦4.7%、交互项4.5%，证明铜损和粘性摩擦占主导，交互项虽小但不可忽略。
- **交互系数**（表II）：最大值的成对组合集中在运动链中相邻或经常协同运动的关节（如肩部滚动-肘、肩部俯仰-肘、肩部偏航-腕偏航等）。
- **效率参数aᵢ均为1**：说明齿轮等损耗已被b、c、d吸收。

## 七、优点
- **物理可解释性**：模型公式直接源于电机物理（铜损、摩擦），参数有明确物理意义，便于分析关节差异。
- **简洁高效**：线性参数形式，凸二次规划快速求解，无需深度网络训练，易部署。
- **创新基线校正**：通过静态平方扭矩偏差Δτ²校正，正确预测负净功率（低负载姿态），这是现有模型常忽略的。
- **成对交互项**：首次在人形机器人手臂功耗模型中显式建模多关节功率耦合，提升多轴运动预测精度。
- **轨迹级聚合策略**：解决了低采样率传感器（1 Hz）与高动态数据不匹配导致的数值病态，是实用技巧。
- **严格异常过滤**：两阶段（IMU稳定性+3σ残差）提高数据质量和模型鲁棒性。
- **泛化验证**：在未见速度上R²高，且针对轨迹级聚合带来的独立性问题，验证可信。

## 八、不足与局限
- **实验覆盖有限**：
  - 仅测试Unitree G1左臂，带有特定Dex3-1手爪，结论可能不泛化到其他机器人或不同手爪。
  - 所有实验机器人站立不动，右臂静止；未考虑行走、双臂协调或动态全身运动对臂功率的影响。
  - 仅使用**机器人等级关节扭矩估计**（未使用地面真值力矩传感器），本身存在误差。
  - 速度变化仅5个等级，验证速度虽未见但仍在训练速范围边界内；更极端速度（如>2.5 rad/s）或非均匀运动未测试。
- **模型限制**：
  - 忽略温度对绕组电阻的影响（漂移），长时间任务下b参数会变化。
  - 忽略制动不对称：谐波驱动在加减速时效率不同，模型使用单一aᵢ。
  - 当两条轨迹速度剖面完全相同时，交互项与粘性项共线，单独参数不可辨识（仅组合效应可靠）。
- **缺乏基准对比**：未与其他典型模型（如神经网络, 详细电机械模型) 比较，难以验证“物理线性模型”是否优于现有方法。
- **验证集规模小**：仅46条，可能不足以全面测试泛化；单次离群值（17.2 W）对RMSE影响大。
- **计算资源未说明**：虽然参数辨识简单，但未提及数据采集耗时、机器人设置等，复现门槛信息不完整。

（完）
