---
title: Hierarchical laser-programmed soft actuators for designing bionic robots with freeform morphing shapes
title_zh: 层级激光编程软体致动器用于设计具有自由形态变形能力的仿生机器人
authors: "Y.S.H. Guo, Mingguang Han, Weixiong Yang, Meihong He, Haibin Duan, Xilun Ding, Sida Luo"
date: 2026-06-10
pdf: "https://www.science.org/doi/pdf/10.1126/sciadv.aeb1989?download=true"
tags: ["query:热点论文筛选", "query:VLA方向", "query:具身智能公司相关", "paper:OpenAlex", "company:physical intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=1; institution_filter=company; company_relation_match=physical intelligence; relation_source=abstract; institutions=Beihang University; query=multimodal robot manipulation policy"
tldr: 传统刺激响应策略在制造简易与运动复杂性间存在权衡。为此提出空间差异化激光编程技术，通过跨尺度控制激光能量和扫描方向，同时调节材料异质性与结构层次，制造出具有自由形态变形能力的激光诱导石墨烯软体驱动器(LIG-SA)。该驱动器编码直弯、定向卷曲、刚性支撑、柔性连接四种运动单元，组合后实现章鱼触手、尺蠖/海豹爬行器等仿生机器人的多任务运动（抓取、导航、避障）。该方法桥接数字设计与物理智能，为可编程形状变形的软体机器人开辟新途径。
source: openalex
selection_source: hot_paper_scout
motivation: 突破传统刺激响应策略在制造简易性与运动复杂性间的权衡，实现可配置三维运动。
method: 通过空间差异化激光编程技术，跨尺度调节激光能量和扫描方向，同时控制材料异质性与结构层次，编码四种运动单元。
result: 制造出LIG-SA并组合成仿生机器人（章鱼触手、尺蠖/海豹爬行器），实现抓取、导航、避障等多任务运动。
conclusion: 该框架桥接数字设计与物理智能，为软体机器人自由形态可编程形状变形提供新途径。
---

## 摘要
受生物启发的形态变形结构对于下一代具有前所未有适应性的软体机器人至关重要，这类结构需要能够实现复杂且可配置的三维运动的致动器。通过克服传统刺激响应策略在制造简易性与运动学复杂性之间的权衡，本文引入了一种空间差异化激光编程技术，用于数字化制造具有自由形态变形能力的激光诱导石墨烯基软体致动器（LIG-SAs）。通过对激光能量和刻写方向的跨尺度控制，可以同时调节材料异质性和结构层次性，从而引入解耦的电热分布和刚度各向异性，为LIG-SAs编码四种典型的运动单元：直线弯曲、定向卷曲、刚性支撑和柔性连接。通过将多模态变形单元任意组合成具体装置，该方法进一步实现了仿生机器人的自由形态设计，包括章鱼状触手和尺蠖/海豹状爬行器，用于共形抓取、路径导航和避障等多任务运动。该框架将数字设计与物理智能相结合，为创造复杂且可编程形态的软体机器人开辟了前所未有的途径。

## Abstract
Bio-inspired shape-morphing structures, essential for next-generation soft robotics with unprecedented adaptability, demand actuators capable of complex and configurable three-dimensional motions. By overcoming traditional stimulus-responsive strategies facing the trade-off between manufacturing simplicity and kinematic sophistication, here, we introduce a spatially differentiated laser-programming technology for digital manufacturing laser-induced graphene-based soft actuators (LIG-SAs) with freeform morphing capabilities. Via cross-scale control of lasing energy and scribing direction, material heterogeneity and structural hierarchy can be tuned simultaneously for introducing decoupled electrothermal distribution and stiffness anisotropy, thus encoding LIG-SAs with four typical motion units: straight bending, directional curling, rigid supporting, and soft connecting. By arbitrarily grouping multimodal morphing units into concretized devices, this approach further empowers freeform design of bionic robots including octopus-like tentacles and inchworm/seal-like crawlers toward multitask locomotion of conformal grasping, path navigation, and obstacle avoidance. This framework bridges digital design with physical intelligence, unlocking previously unidentified avenues of soft robots for creating sophisticated and programmable morphologies.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 研究动机：受生物启发的形态变形结构是下一代软体机器人的关键，但传统刺激响应策略面临制造简易性与运动复杂性之间的权衡，难以同时实现低成本制造和可配置的三维复杂运动。
- 背景：现有软体致动器通常只能实现单一或简单的变形模式，缺乏在单一器件中集成多种运动单元的自由形态变形能力，限制了仿生机器人的功能多样性和适应性。
- 整体意义：该工作旨在突破这一权衡，通过数字化制造方法赋予软体致动器可编程的自由形态变形能力，为高适应性软体机器人提供新的设计范式。

## 二、论文提出的方法论
- 核心思想：提出空间差异化激光编程技术，通过跨尺度控制激光能量和扫描方向，同时调节材料异质性和结构层次，在激光诱导石墨烯（LIG）基底上编码多种运动单元，实现可配置的三维运动。
- 关键技术细节：
  - 利用激光诱导石墨烯（LIG）作为电热驱动材料，通过调节激光参数（能量、刻写方向）实现空间差异化的电热分布和刚度各向异性。
  - 编码四种典型的运动单元：直线弯曲、定向卷曲、刚性支撑、柔性连接。
  - 通过将多模态变形单元任意组合成具体装置，实现仿生机器人的自由形态设计。
- 算法流程（文字说明）：
  - 1. 设计目标运动模式，分解为所需运动单元集合。
  - 2. 通过计算机辅助设计（CAD）规划各单元的激光加工参数（能量、方向、路径）。
  - 3. 执行空间差异化激光扫描，形成具有异质性和层次结构的LIG薄膜。
  - 4. 施加电热刺激，驱动编码好的运动单元协同变形，实现预定三维形态变化。

## 三、实验设计
- 使用的数据集/场景：论文未明确说明使用标准数据集；实验场景包括仿生机器人功能演示：章鱼状触手（共形抓取）、尺蠖/海豹状爬行器（路径导航和避障）。
- Benchmark：未提供与现有方法的定量基准对比（如变形角度、响应速度、负载能力等指标对比）。
- 对比方法：未明确列出对比方法，属于方法类型的验证性展示，而非性能竞赛式对比。

## 四、资源与算力
- 文中未明确说明使用的算力资源（如GPU型号、数量、训练时长等）。
- 由于该方法主要为材料加工和物理实验，不涉及大规模神经网络训练，算力需求可能较低，但论文对此未作说明。

## 五、实验数量与充分性
- 实验数量：论文展示了三种仿生机器人（章鱼触手、尺蠖爬行器、海豹爬行器）的多种运动任务（共形抓取、路径导航、避障），但未报告统计性重复实验或大量样本测试。
- 充分性：实验覆盖了不同运动模式（弯曲、卷曲、支撑、连接）的组合，证明了自由形态设计可行性。但缺乏定量性能评估（如变形精度、响应速度、耐久性等），也未进行系统性消融实验验证各运动单元的必要性。
- 客观性/公平性：演示性实验较直观，但缺乏与现有软体致动器标准化测试的对比，公平性有提升空间。

## 六、论文的主要结论与发现
- 成功开发了空间差异化激光编程技术，实现了激光诱导石墨烯软体致动器（LIG-SA）的自由形态变形能力。
- 编码的四种运动单元可任意组合，构建出具有多任务运动能力的仿生机器人（章鱼触手、尺蠖/海豹爬行器）。
- 该框架将数字设计与物理智能桥接，为复杂可编程形态的软体机器人开辟了新途径。
- 证明该方法克服了传统策略在制造简易性与运动复杂性之间的权衡。

## 七、优点
- 创新性：首次通过单一激光编程同时调控材料异质性和结构层次，实现了多运动单元集成，突破了传统软体致动器的变形模式限制。
- 制造简易性：数字化激光加工工艺简便、可重复、易扩展，适合快速原型制造。
- 功能多样性：单一致动器可编码多种运动单元，组合后实现复杂三维变形，支持多种仿生机器人形态。
- 物理智能与数字设计融合：实现了从设计到制造的端到端可编程性，具有实际应用潜力。

## 八、不足与局限
- 缺乏定量性能评估：未提供变形角度、响应速度、负载能力、寿命等关键指标的定量数据，也未与现有方法进行统一基准对比，结论说服力有限。
- 实验覆盖不足：仅展示概念演示，未进行系统消融实验或统计显著性分析，难以判断各运动单元的独立贡献和鲁棒性。
- 应用限制：当前演示限于特定LIG材料和简单机器人形态，实际应用中材料疲劳、环境适应性（温度、湿度等）等问题未探讨。
- 算力与数据未明：若未来需要结合机器学习预测变形，现有文本未提供任何相关数据或模型，限制了方法的可复现性。

（完）
