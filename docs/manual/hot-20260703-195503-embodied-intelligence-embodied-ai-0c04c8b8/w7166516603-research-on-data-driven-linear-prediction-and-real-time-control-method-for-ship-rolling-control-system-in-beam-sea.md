---
title: Research on Data-Driven Linear Prediction and Real-Time Control Method for Ship Rolling Control System in Beam Sea
title_zh: 横浪中船舶横摇控制系统的数据驱动线性预测与实时控制方法研究
authors: "Tongtong Qie, Jianyong Zheng, Jianzheng Zhang, Hongyu Wei, Haolin Yang, Kun Wei"
date: 2026-06-26
pdf: "https://www.mdpi.com/2673-1924/7/4/53/pdf?version=1782483402"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:beijing academy of artificial intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=beijing academy of artificial intelligence; relation_source=lead-affiliation; institutions=Beijing Academy of Artificial Intelligence, Intelligent Health (United Kingdom); query=robot"
tldr: "船舶在波浪中的运动预测对安全航行至关重要，但现有局部线性预测模型在实际海洋环境中的鲁棒性和实时性不足。本文提出基于Koopman算子的全局线性预测器(GLP)，将船舶非线性横摇动力学转化为全局线性表示，实现实时预测与控制。在规则和不规则波浪环境下的仿真实验中，GLP模型的预测精度比经典方法高约14%，且在所有波浪条件下横摇减小效率超过91%。该工作为船舶横摇控制提供了一种高精度、强鲁棒的数据驱动实时控制方法。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有船舶运动预测模型基于局部线性假设，在真实海洋波浪环境中鲁棒性和实时性不足，需更有效的全局线性方法。
method: 提出基于Koopman算子的全局线性预测器(GLP)，将船舶非线性横摇动力学全局线性化，用于实时预测与控制。
result: "在规则与不规则波浪实验中，预测精度比经典方法高约14%，横摇减小效率超过91%。"
conclusion: 所提GLP方法有效提升了船舶横摇预测与控制性能，显著降低横摇幅度，适用于真实海洋环境。
---

## 摘要
预测船舶在波浪中的运动趋势对于安全航行和作业至关重要。现有预测模型大多基于局部线性动力学假设，在理想海洋环境中能取得良好效果。然而，船舶通常在包含规则波或不规则波的真实海洋环境中航行，这使得船舶运动估计模型的鲁棒性和实时性尤为重要。为解决这一局限性，本文提出了一种基于Koopman算子的全局线性预测器（GLP），该预测器能有效表征船舶的非线性横摇动力学。此外，利用该GLP模型实时预测并控制船舶的横摇运动。所提方法在规则波和不规则波环境中均得到验证。仿真实验结果表明，在船舶横摇动力学方面，所提方法的精度比其它经典方法高出约14%。并且在所有波浪条件下，其横摇减幅效率超过91%，显著降低了船舶横摇的幅度。

## Abstract
Predicting a ship’s motion trend in waves is crucial for safe navigation and operation. Existing prediction models are mostly based on the assumption of local linear dynamics, which can achieve great performance in idealized ocean environments. However, ships typically sail in real marine environments with regular or irregular waves, which makes the robustness and real-time performance of ship motion estimation models particularly important. To address this limitation, this paper proposes a global linear predictor (GLP) based on the Koopman operator, which can effectively represent the nonlinear rolling dynamics of ships. Furthermore, the GLP model is used to predict and control the rolling motion of a ship in real time. The proposed method is validated in both regular and irregular wave environments. The simulation experiment results show that the accuracy of the proposed method is about 14% higher than that of other classical methods on ships’ rolling dynamics. And it achieves a more than 91% rolling reduction efficiency in all wave conditions, significantly decreasing the amplitude of a ship’s rolling.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 船舶在波浪中的横摇运动是导致失稳和倾覆的主要因素，精确预测横摇趋势对安全航行极为重要。
- 现有预测模型多基于局部线性假设（如泰勒展开），在理想规则波环境下表现良好，但在真实海洋环境（不规则波、大振幅、噪声干扰）中鲁棒性和实时性不足。
- 直接使用非线性控制方法（如滑模控制、非线性MPC）计算量大，难以满足实时控制需求；线性控制方法（如H∞、角速率反馈）虽实时性好，但在非线性显著时预测精度下降。
- 本文旨在构建一种数据驱动的全局线性预测器（GLP），既能保留非线性动力学特性，又具备线性预测的计算效率，并集成到模型预测控制（MPC）框架中，实现船舶横摇的实时高效控制。

## 二、论文提出的方法论
- **核心思想**：利用Koopman算子理论，将非线性船舶横摇动力学提升到高维空间，在该空间中系统演化近似为线性。通过数据驱动的方式（扩展动态模式分解，EDMD）从系统输入输出数据中学习得到有限维线性预测模型。
- **关键技术细节**：
  - 船舶-陀螺减摇系统建模：1自由度非线性横摇动力学（含高阶阻尼和恢复项），以及陀螺减摇器动力学（含电机模型）。
  - 定义提升状态 `z = [x; h(x)]`，其中 `x` 为原始状态（横摇角、角速度、进动角、进动角速度、电机电流），`h(x)` 为非线性提升函数（本文测试了高斯、多项式、三角函数、混合四种）。
  - 通过EDMD最小化预测误差，求解状态转移矩阵 `A_T`、控制矩阵 `B_T` 和状态恢复矩阵 `C_T`，获得全局线性预测器：`z_{k+1}=A_T z_k + B_T u_k`，`x̂_k = C_T z_k`。
  - 基于该线性预测器设计线性MPC（称为GMPC），滚动优化二次型代价函数，实时求解凸二次规划问题获得控制量 `u_k`（陀螺电机电压）。
  - 稳定性分析：利用Lyapunov函数证明闭环系统渐近稳定。
- **算法流程**（文字说明）：
  1. 离线阶段：在不同初始状态和控制激励下，通过仿真生成数据集，并使用EDMD辨识 `A_T, B_T, C_T`。
  2. 在线阶段：每个控制周期测量当前状态，通过提升函数得到 `z_0`；求解MPC优化问题（QP）获得最优控制序列；将第一个控制量作用于系统；重复。

## 三、实验设计
- **仿真场景**：
  - 基于一艘实船（JH-7500）和真实陀螺减摇器参数，参数来源于实验室测量。
  - 规则波工况：Case 1（幅值4°，周期10s）。
  - 不规则波工况：Case 2~6，采用ITTC双参数波谱，显著波高Hs从0.25m到3.10m，谱峰周期Tp从4.75s到11.88s，对应北大西洋典型海况I~V级。
  - 波激励力矩计算：规则波用简单公式，不规则波通过RAO和波谱叠加，并加入随机初相。
  - 测量噪声：在预测阶段和反馈状态中加入高斯噪声。
- **Benchmark与对比方法**：
  - 预测精度对比：GLP vs 局部线性预测器（LLP，基于泰勒展开的线性化）。
  - 控制性能对比：GMPC（本文） vs LMPC（基于局部线性预测的MPC） vs NMPC（基于非线性模型的MPC，使用CasADi求解）。
  - 控制指标：横摇角标准差、控制效率η（η=(σ_uncontrolled-σ_controlled)/σ_uncontrolled×100%）、每步计算耗时（ms）。
- **参数设置**：
  - 采样时间0.01s，仿真时长60s（6000步），预测时域3步。
  - GMPC提升维度N=100，提升函数最终选用高斯函数。
  - 权重矩阵：Q=diag(10,0,0,0,3)，R=0.05，P同Q（对GMPC仅前5维有效，其余0）。

## 四、资源与算力
- 论文中未明确提及使用的GPU型号、数量或训练时长。
- 控制求解工具：MATLAB 2024a 开源的二次规划工具（用于LMPC和GMPC），NMPC使用CasADi工具包。
- 运行时算力分析：从实验结果看，GMPC单步计算耗时约0.4~0.5ms，远小于采样间隔10ms，说明在普通CPU上即可满足实时性要求；NMPC单步耗时约20ms，超出采样间隔，表明需要更高算力或无法实时运行。
- 结论：本文未专门统计训练算力，但强调在线推理所需的计算资源极低。

## 五、实验数量与充分性
- **预测精度实验**：
  - 五种提升函数（高斯、多项式、三角函数、混合） × 四种提升维度（10,30,50,100） → 共20组参数组合，每组重复100次取平均RMSE。
  - 最终选择高斯 + N=100，并与LLP对比全状态预测误差（5个状态变量，如图5所示）。
- **控制性能实验**：
  - 六种海况（Case 1~6） × 三种控制器（LMPC, NMPC, GMPC） × 10次重复（随机波浪切片和初始状态） → 共180次仿真运行。
  - 另外单独展示了不同海况下的RAO对比（图8）和详细数值结果（表6）。
- **充分性评价**：
  - 实验覆盖了规则波和5种不规则波（从轻浪到大浪），噪声引入增强了实际场景模拟。
  - 对比了经典线性方法和非线性方法，且考察了计算时间这一关键实际指标。
  - 所有数值结果均报告平均值，并给出了统计稳定性。
  - 不足：未包括硬件在环实验或实船实验，仅仿真验证；未考虑六自由度耦合的影响。

## 六、论文的主要结论与发现
- 所提出的GLP预测精度比LLP（局部线性）高出约14%（平均RMSE从18.66%降至3.10%，在N=100高斯核下）。
- GMPC在所有六种波浪条件下均保持超过91%的横摇减幅效率（最高91.75%，最低89.85%），而LMPC效率约为84-90%，NMPC仅为64-75%。
- GMPC每步计算时间不到0.5ms，与LMPC相当，远低于NMPC（~20ms），具备实时控制潜力。
- 随着海况恶化，LMPC和NMPC控制效率下降，而GMPC几乎保持不变，展示出强鲁棒性。
- 验证了Koopman算子提升变换能有效线性化非线性船舶横摇动力学，并成功与线性MPC结合。

## 七、优点
- **方法创新**：首次将Koopman算子全局线性化方法应用于船舶横摇预测与控制，突破了局部线性假设的局限。
- **数据驱动**：无需精确解析水动力系数，仅需系统输入输出数据即可建立模型，降低了对物理建模的依赖。
- **实时性好**：在线计算仅需求解小型二次规划，耗时小于0.5ms，满足实际嵌入式控制器需求。
- **鲁棒性强**：在不同波浪强度及含噪声条件下均保持高控制效率（>90%），优于LMPC和NMPC。
- **实验充分**：覆盖6种海况，包含规则波和不规则波，进行了预测和控制多维度对比，并引入噪声测试鲁棒性，结果统计可靠。

## 八、不足与局限
- **离线辨识依赖性**：Koopman预测器基于仿真生成的训练数据，其质量（覆盖范围、噪声水平）直接影响预测精度，若训练数据与实际工况差异大，可能性能下降。
- **仅考虑1自由度横摇**：忽略了纵摇、首摇等自由度耦合对横摇的影响，而真实船舶运动是六自由度耦合的，简化可能带来偏差。
- **仅仿真验证**：所有实验均为数值仿真，未进行实船试验或硬件在环测试，实际海洋环境中的不确定性和硬件限制未考虑。
- **提升函数选择缺乏理论指导**：文中通过实验对比选择了高斯核，但未给出为何高斯最优的机理分析，且混合核并未超越单一核，说明提升函数设计仍依赖经验。
- **无自适应机制**：预测器固定不变，无法在线适应船舶参数变化或环境漂移，未来工作可考虑在线Koopman学习。

（完）
