---
title: "ADAPT: Analytical Disturbance-Aware Policy Training for Humanoid Locomotion"
title_zh: ADAPT：面向仿人机器人运动的解析式扰动感知策略训练
authors: "Bofan Lyu, Jindou Jia, Kuangji Zuo, Yanshuo Lu, Shijia Han, Gen Li, Boyu Ma, Jingliang Li, Geng Li, Jie Yang"
date: 2026-06-15
pdf: "https://doi.org/10.48550/arxiv.2606.16542"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=humanoid robot policy"
tldr: 人形机器人部署在人类环境中需处理外力干扰，现有方法在准确性、可迁移性或鲁棒性上存在局限。提出的ADAPT框架以分析性全身扰动观测器为核心，无需力传感器即可在线估计外力/力矩，直接输入策略。在Unitree G1机器人上实验表明，ADAPT在多种扰动场景下实现准确扰动预测，鲁棒性和速度跟踪均优于仅本体感受的基线，并能有效处理分布外扰动。该工作赋予机器人物理感知的外力意识，通过惩罚下肢扰动鼓励更轻量步态，显著提升泛化能力。
source: openalex
selection_source: hot_paper_scout
motivation: 现有基于学习的人形机器人步行策略在应对外力干扰时，受限于随机化、任务特定力目标或数据依赖的估计方式，在准确性、任务迁移性或分布外鲁棒性上各有缺陷。
method: 提出ADAPT框架，其核心是一个分析性全身扰动观测器，利用可访问的机器人动力学在线估计残余力/力矩，无需额外力传感器，并将估计结果直接馈入策略网络。
result: 在Unitree G1人形机器人上，ADAPT在躯干扰动、站立推挤、不对称手持负载等场景下准确预测扰动，鲁棒性和速度跟踪均优于仅本体感受基线，对分布外扰动同样有效。
conclusion: ADAPT通过物理扰动脉冲感知使策略具备跨场景泛化能力，并能通过惩罚推断的下肢扰动来鼓励更轻的步态，提升人形机器人步行鲁棒性。
---

## 摘要
部署在以人为本环境中的仿人机器人必须处理力交互任务，其中外部接触会引入意外扰动，破坏运动精度与稳定性。现有基于学习的方法依赖于广泛的领域随机化、特定任务的力目标，或基于运动历史的学习型力估计器，但每种方法都在精度、任务迁移性或分布外鲁棒性上有所妥协。我们提出解析式扰动感知策略训练（ADAPT），该框架为仿人机器人策略配备了一个基于物理原理的扰动观测器。ADAPT的核心是一个解析式全身扰动观测器，它利用可获取的机器人动力学在线估计残余力/力矩，无需力/力矩传感器。估计的扰动直接输入策略，使仿人机器人获得对外部力/力矩的显式、源于物理的感知，能够泛化到各种未见场景。在Unitree G1仿人机器人上的实验表明，与仅基于本体感知的基线相比，ADAPT在躯干扰动、站立推力和非对称手持载荷下实现了精确的扰动预测和更强的鲁棒性，即使在分布外扰动下也能改善速度跟踪。此外，ADAPT能够对下肢关节的推断扰动施加惩罚，以鼓励更轻快的运动。

## Abstract
Humanoids deployed in human-centered environments must handle force-interactive tasks, where external contacts introduce unexpected disturbances that disrupt locomotion accuracy and stability. Existing learning-based approaches rely on broad domain randomization, task-specific force objectives, or learning-based force estimators from motion history, each of which compromises accuracy, task transferability, or out-of-distribution (OOD) robustness. We present Analytical Disturbance-Aware Policy Training (ADAPT), a framework that equips humanoid policies with a physically grounded disturbance observer. The core of ADAPT is an analytical whole-body disturbance observer that estimates residual force/torque online with the accessible robot dynamics, without requiring force/torque sensors. Fed directly into the policy, the estimated disturbances give the humanoid an explicit, physics-derived sense of external force/torque that can generalize across diverse unseen scenes. Experiments on a Unitree G1 humanoid show that ADAPT achieves accurate disturbance prediction and stronger robustness than a proprioception-only baseline under torso perturbations, standing pushes, and asymmetric hand payloads, with improved velocity tracking even on OOD disturbances. Moreover, ADAPT enables penalizing inferred disturbances at lower-body joints to encourage lighter locomotion.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 仿人机器人在人类中心环境中执行力交互任务时，外部接触会引入意外扰动，破坏运动精度与稳定性。
- 现有基于学习的方法存在局限性：
  - 广泛领域随机化方法精度不足。
  - 任务特定力目标方法缺乏任务迁移性。
  - 基于运动历史的学习型力估计器在分布外（OOD）场景下鲁棒性差。
- 核心目标：为仿人机器人策略提供一种基于物理原理、无需额外力传感器的扰动感知能力，以提升在未见场景下的泛化鲁棒性。

## 二、论文提出的方法论
- **核心思想**：提出分析式扰动感知策略训练（ADAPT）框架，核心是一个解析式全身扰动观测器。
- **关键技术细节**：
  - 利用可获取的机器人动力学模型，在线估计残余力/力矩，无需力/力矩传感器。
  - 将估计的扰动直接作为策略网络的输入，使机器人获得对外部力/力矩的显式、物理感知。
  - 在训练中，可以对下肢关节的推断扰动施加惩罚，鼓励更轻快的运动（即更高效的步态）。
- **算法流程（文字描述）**：
  1. 基于机器人动力学模型构建扰动观测器，利用当前关节状态和命令计算期望力矩，与实际力矩之差即为残余力/力矩（扰动估计）。
  2. 将扰动估计值与本体感觉（如关节位置、速度、IMU等）一起输入策略网络。
  3. 策略网络输出关节位置/扭矩指令。
  4. 训练时额外加入对下肢扰动估计值的惩罚项，以鼓励策略抵抗干扰并优化步态。

## 三、实验设计
- **实验场景与任务**：
  - 使用Unitree G1仿人机器人进行实验。
  - 测试场景包括：躯干扰动、站立推挤、非对称手持载荷（如单手提重物）。
  - 还包含分布外（OOD）扰动场景。
- **基准方法（Baseline）**：仅使用本体感知（proprioception-only）的策略，即不加入扰动估计信号。
- **对比方法**：未明确提及与其他方法（如域随机化、学习型力估计器）的直接对比，主要与本体感受基线对比。
- **评测指标**：扰动预测准确性、鲁棒性（抗扰动能力）、速度跟踪误差。

## 四、资源与算力
- 论文中**未明确说明**训练所使用的GPU型号、数量、训练时长等资源细节。
- 仅提及在Unitree G1平台上进行实验，未描述仿真环境或实机训练的具体算力配置。

## 五、实验数量与充分性
- 实验覆盖三种主要扰动场景（躯干、站立推挤、手持载荷）以及OOD场景。
- 进行了消融分析（如是否加入扰动估计、是否使用下肢惩罚项），但具体消融实验数量未详述。
- **充分性评估**：实验设计较为合理，涵盖了常见外力干扰类型和分布外情况，但缺少与更多现有方法（如域随机化、基于学习的估计器）的定量对比，对比基线单一，说服力有限。
- 实验在单一机器人平台（Unitree G1）上进行，缺乏跨平台验证，客观性需进一步补充。

## 六、论文的主要结论与发现
- ADAPT框架能够实现准确的扰动预测，在躯干扰动、站立推挤和非对称手持载荷下，鲁棒性和速度跟踪均优于仅本体感受的基线。
- 即使在分布外扰动下，ADAPT仍能改善速度跟踪。
- 通过惩罚下肢关节的推断扰动，可以鼓励机器人采取更轻快、高效的运动模式。
- 结论：解析式扰动观测器能够赋予仿人机器人跨场景泛化的外力感知能力，显著提升步行鲁棒性。

## 七、优点
- **物理可解释性**：基于动力学模型的解析式观测器，无需数据驱动的学习估计器，避免了分布外失效问题。
- **无需额外传感器**：仅利用已有关节编码器和力矩传感器信息（或仿真中的真实状态），降低硬件成本。
- **泛化能力强**：显式的物理扰动估计可直接迁移到未见场景，提升OOD鲁棒性。
- **训练信号利用**：通过惩罚下肢扰动间接优化步态，具有实用价值。
- 实验在真实机器人平台上进行，结果具有实际参考意义。

## 八、不足与局限
- **对比方法单一**：仅与本体感受基线对比，未与域随机化、基于学习的力估计器等方法进行系统比较，难以明确ADAPT的相对优势幅度。
- **实验覆盖面有限**：仅在Unitree G1单一平台上测试，未在其他仿人机器人（如Atlas、Cassie等）上验证，泛化性存疑。
- **资源细节缺失**：未报告训练算力消耗，不利于复现和成本评估。
- **扰动类型**：仅测试了躯干、推挤、手持载荷等基本类型，未涉及复杂地面接触、斜坡、楼梯等更复杂的扰动场景。
- **假设依赖**：解析式观测器依赖于准确的机器人动力学模型，模型误差可能影响扰动估计精度，文中未讨论模型失配情况下的鲁棒性。

（完）
