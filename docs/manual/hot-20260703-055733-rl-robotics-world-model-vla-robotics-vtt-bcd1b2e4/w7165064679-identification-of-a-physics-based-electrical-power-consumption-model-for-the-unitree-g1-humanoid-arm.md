---
title: Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm
title_zh: 基于物理学的Unitree G1人形机器人手臂电力消耗模型识别
authors: "Nestor N. Deniz, Sebastian Vega, Simon Parsons, Fernando Auat Cheein"
date: 2026-06-14
pdf: "https://arxiv.org/pdf/2606.15915"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=title; query=reinforcement learning for humanoid robot control and locomotion"
tldr: 针对电池驱动人形机器人能耗预测需求，提出Unitree G1左臂物理基线性参数功耗模型。模型融合执行器损耗、基线扭矩校正（捕获重力补偿变化）及多关节耦合成对交互项，利用机载测量数据辨识参数。在897条单关节与协调运动轨迹上R²达0.933，RMSE为1.07W；46条未知速度轨迹验证泛化R²=0.965。参数分析揭示各关节主导损耗：粘性摩擦主导肩俯仰和三个腕关节，铜损主导肩偏航与肘关节，库仑摩擦主导肩滚转。
source: openalex
selection_source: hot_paper_scout
motivation: 人形机器人能效管理需精确功耗预测，现有模型难以处理多关节耦合及负净功率轨迹。
method: 建立含执行器损耗、基线扭矩校正及成对交互项的线性参数模型，以机载功率测量为回归目标辨识参数。
result: 897条轨迹训练R²=0.933、RMSE=1.07W；46条新速度轨迹验证R²=0.965，强泛化。
conclusion: 模型准确预测功耗且具可解释性，揭示关节损耗类型，支撑能量感知运动规划。
---

## 摘要
准确预测电力消耗对于电池供电的人形机器人的能量感知运动规划、电池管理和热监测至关重要。本文提出了一种基于物理学的线性参数模型，用于Unitree G1人形机器人七自由度左臂的电力消耗。所提出的公式将执行器损耗项与基线扭矩校正相结合，捕捉重力补偿负载的变化，并能够准确预测负净功率轨迹。引入成对交互项来模拟多关节同时运动期间的功率耦合。模型参数通过物理Unitree G1上采集的实验数据进行识别，使用机载功率测量作为回归目标。在涵盖单关节和协调手臂运动、多个速度水平的897条轨迹中，识别后的模型实现了R² = 0.933，RMSE为1.07瓦特。在先前未见速度下执行的46条轨迹上进行验证，得到R² = 0.965，显示出超越识别数据集的强大泛化能力。对识别参数的分析揭示了手臂各关节不同的功耗特性：粘性摩擦主导大多数关节（肩部俯仰和所有三个腕关节），铜损主导肩部偏航和肘关节，而肩部滚动则独特地由库仑摩擦主导。

## Abstract
Accurate prediction of electrical power consumption is essential for energy-aware motion planning, battery management, and thermal monitoring in battery-powered humanoid robots. This letter presents a physics-based, linear-in-parameters model for the electrical power consumption of the seven-degree-of-freedom left arm of the Unitree~G1 humanoid robot. The proposed formulation combines actuator loss terms with a baseline-torque correction that captures changes in gravity-compensation load and enables accurate prediction of negative net power trajectories. Pairwise interaction terms are introduced to model power coupling during simultaneous multi-joint motion. Model parameters are identified from experimental data collected on a physical Unitree~G1 using onboard power measurements as the regression target. Across 897 trajectories covering single-joint and coordinated arm motions at multiple speed levels, the identified model achieves $R^2 = 0.933$ with an RMSE of 1.07 (W). Validation on 46 trajectories executed at previously unseen speeds yields $R^2 = 0.965$, demonstrating strong generalisation beyond the identification dataset. Analysis of the identified parameters reveals distinct power-consumption characteristics across the arm, with viscous friction dominating most joints (shoulder pitch and all three wrist joints), copper losses dominating shoulder yaw and the elbow, and shoulder roll uniquely dominated by Coulomb friction.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 人形机器人广泛应用于物流、制造、农业等领域，受限于有限机载电池容量，精确预测电力消耗对能量感知运动规划、任务持续时间估计、电池管理和执行器热保护至关重要。
- 现有方法存在不足：纯数据驱动模型需大量训练数据且外推能力有限；传统物理模型依赖详细执行器参数，商业平台常不公开。
- 目前尚无针对现代人形机器人手臂、以机载功率测量为回归目标的物理基电力消耗模型，现有公式也未考虑姿态变化引起的重力补偿功率变化及多关节同时运动的耦合效应。

## 二、论文提出的方法论
- **模型结构**：建立基于物理的线性参数模型，每个关节的净功率包含四项：
  - 机械功率项：$a_i \tau_i \dot{q}_i$（逆齿轮效率）
  - 铜损项：$b_i \Delta \tau_i^2$（基线扭矩校正：静态预空闲期间均方扭矩与当前扭矩平方之差）
  - 库仑摩擦项：$c_i |\dot{q}_i|$
  - 粘性摩擦项：$d_i \dot{q}_i^2$
- **多关节耦合**：引入成对交互项 $e_{ij} |\dot{q}_i||\dot{q}_j|$ 模拟同时多关节运动时的功率耦合。
- **参数辨识**：
  - 采用轨迹级聚合：将每个轨迹内的样本平均为一行，消除低速采样（1 Hz）带来的数值病态（条件数 $7.8\times10^{11}$）。
  - 约束最小二乘：通过凸二次规划（IPOPT求解器）求解，约束所有参数非负且 $a_i \geq 1$。
- **离群过滤**：
  - 第一阶段：检测IMU角速度标准差，删除因腿部稳定器补偿导致的功率泄漏轨迹（104条）。
  - 第二阶段：迭代3σ残差剔除（16条），使残差峰度从77降至2.97（近似高斯）。

## 三、实验设计
- **硬件平台**：Unitree G1人形机器人左臂（7自由度），搭载Dex3-1灵巧手；主板上传感器（MBS）监测上肢功率轨，采样约1 Hz。
- **轨迹设置**：
  - 训练集：1017条轨迹（含单关节、两关节、三关节及以上组合），5个速度水平（$\dot{q}_{\max} \in \{0.5,1.0,1.5,2.0,2.5\}$ rad/s），最终保留897条（经离群过滤）。
  - 验证集：46条轨迹，4个未见速度（0.75,1.25,1.75,2.25 rad/s），使用相同路径点。
- **评价指标**：R²、RMSE、MAE；基准为无交互项模型、未聚合模型等（但论文未系统对比其他方法，仅对比了不同配置）。
- **对比基准**：缺乏与其他数据驱动或物理模型的直接对比，但通过消融展示了轨迹聚合和离群过滤的必要性。

## 四、资源与算力
- **文中未明确说明**使用的GPU型号、数量或训练时长。参数辨识通过凸二次规划求解，计算量较小，可能在普通CPU上完成。深度强化学习训练部分仅在结论中提到，未详述算力需求。

## 五、实验数量与充分性
- **实验数量**：训练897条轨迹（包含单关节至多关节组合、5种速度），验证46条轨迹（4种未见速度）。
- **充分性分析**：
  - 轨迹类型覆盖广泛（单关节、两两组合、多关节），但未包含所有可能的多关节组合（如四关节以上联合运动较少）。
  - 离群过滤合理（IMU稳定性+统计残差），保留数据量足够。
  - 验证集速度与训练集无重叠，但轨迹路径相同，泛化测试仅针对速度外推，未测试不同负载或不同初始姿态。
  - 未与其他模型（如纯数据驱动、简化物理模型）进行公平比较，缺乏基准对比。
- **总体评价**：实验设计较为严谨，但对比性和泛化范围有限。

## 六、论文的主要结论与发现
- 最终7关节模型在训练集上达到R²=0.933，RMSE=1.07 W；验证集上R²=0.965，MAE=2.33 W，证明模型有效且泛化良好。
- 参数分析揭示各关节主导损耗机制：
  - 粘性摩擦主导：肩部俯仰、三个腕关节。
  - 铜损主导：肩部偏航、肘关节。
  - 库仑摩擦主导：肩部滚动（唯一）。
- 铜损（42.4%）和粘性摩擦（38.2%）占总预测功率80%以上，耦合项贡献约4.5%，验证了引入交互项的必要性。
- 模型可用于深度强化学习框架中的能量奖励项，支持能量高效运动规划。

## 七、优点
- **物理可解释性**：模型参数对应明确物理意义（齿轮效率、摩擦系数、电阻），便于分析各关节能量损耗来源。
- **创新机制**：基线扭矩校正准确处理负净功率轨迹；成对交互项捕捉多关节功率耦合，提升预测精度。
- **实用性强**：仅需机载低速功率传感器（1 Hz）和常规关节状态即可辨识，无需额外硬件。
- **验证充分**：训练集与验证集速度不重叠，证明模型能外推至新速度水平；离群过滤策略显著提升模型稳健性。

## 八、不足与局限
- **温度依赖性未建模**：电机绕组电阻随温度变化，长期运行可能使 $b_i$ 漂移。
- **制动不对称忽略**：谐波减速器不可逆，减速时齿轮效率不同，当前用单一 $a_i$ 建模不准确。
- **特征共线性**：当两关节速度曲线相同，$|\dot{q}_i||\dot{q}_j|$ 与 $\dot{q}_i^2$ 完全共线，导致 $d_i$、$e_{ij}$ 不可分离辨识。
- **手部惯性干扰**：Dex3-1手部附加惯性可能使腕关节粘性摩擦系数虚高，未进行裸机对比实验分离影响。
- **验证范围有限**：仅测试速度外推，未测试不同负载、不同初始姿态、不同运动模式（如动态抓取）下的泛化性。
- **缺乏基准对比**：未与数据驱动模型（如神经网络）或其他物理简化模型比较，无法证明方法在精度-可解释性权衡中的优势。
- **采样率限制**：MBS传感器仅1 Hz，虽用轨迹聚合可缓解，但可能丢失高频瞬态功率细节。

（完）
