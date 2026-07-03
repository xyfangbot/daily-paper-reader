---
title: Hierarchical laser-programmed soft actuators for designing bionic robots with freeform morphing shapes
title_zh: 分层激光编程软体致动器用于设计具有自由形态变形能力的仿生机器人
authors: "Y.S.H. Guo, Mingguang Han, Weixiong Yang, Meihong He, Haibin Duan, Xilun Ding, Sida Luo"
date: 2026-06-10
pdf: "https://www.science.org/doi/pdf/10.1126/sciadv.aeb1989?download=true"
tags: ["query:热点论文筛选", "query:VLA方向", "query:具身智能公司相关", "paper:OpenAlex", "company:physical intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=1; institution_filter=company; company_relation_match=physical intelligence; relation_source=abstract; institutions=Beihang University; query=multimodal robot manipulation policy"
tldr: 仿生形状变形结构对软体机器人至关重要，但传统刺激响应策略在制造简单性与运动复杂性间存在权衡。本文提出空间差异化激光编程技术，通过跨尺度控制激光能量与扫描方向，同时调节材料异质性和结构层次，解码电热分布与刚度各向异性，从而编码四种典型运动单元。通过任意分组多模态变形单元，设计了章鱼触手及尺蠖/海豹爬行机器人，实现共形抓取、路径导航与避障等多任务运动。该框架连接数字设计与物理智能，为可编程形态软机器人开辟新路径。
source: openalex
selection_source: hot_paper_scout
motivation: 克服传统刺激响应策略在制造简单性与运动复杂性之间的权衡，需要能实现复杂可配置三维运动的驱动器。
method: 提出空间差异化激光编程技术，通过跨尺度控制激光能量与扫描方向，同时调节材料异质性和结构层次，编码四种典型运动单元。
result: 通过分组多模态变形单元，设计出章鱼触手和尺蠖/海豹爬行机器人，实现共形抓取、路径导航和避障等多任务运动。
conclusion: 该框架连接数字设计与物理智能，为可编程形态软机器人开辟新途径。
---

## 摘要
受生物启发的形态变形结构对于下一代具有前所未有适应性的软体机器人至关重要，需要能够实现复杂且可配置的三维运动的致动器。通过克服传统刺激响应策略在制造简易性与运动学复杂性之间的权衡，我们引入了一种空间差异化的激光编程技术，用于数字化制造具有自由形态变形能力的激光诱导石墨烯基软体致动器（LIG-SAs）。通过跨尺度控制激光能量和划线方向，可以同时调节材料异质性和结构层级，从而引入解耦的电热分布和刚度各向异性，为LIG-SAs编码四种典型运动单元：直线弯曲、定向卷曲、刚性支撑和软连接。通过将多模态变形单元任意组合成具体装置，该方法进一步实现了仿生机器人的自由形态设计，包括章鱼状触手和尺蠖/海豹状爬行器，用于共形抓取、路径导航和避障等多任务运动。该框架将数字设计与物理智能相连接，为创建复杂且可编程形态的软体机器人开辟了前所未有的途径。

## Abstract
Bio-inspired shape-morphing structures, essential for next-generation soft robotics with unprecedented adaptability, demand actuators capable of complex and configurable three-dimensional motions. By overcoming traditional stimulus-responsive strategies facing the trade-off between manufacturing simplicity and kinematic sophistication, here, we introduce a spatially differentiated laser-programming technology for digital manufacturing laser-induced graphene-based soft actuators (LIG-SAs) with freeform morphing capabilities. Via cross-scale control of lasing energy and scribing direction, material heterogeneity and structural hierarchy can be tuned simultaneously for introducing decoupled electrothermal distribution and stiffness anisotropy, thus encoding LIG-SAs with four typical motion units: straight bending, directional curling, rigid supporting, and soft connecting. By arbitrarily grouping multimodal morphing units into concretized devices, this approach further empowers freeform design of bionic robots including octopus-like tentacles and inchworm/seal-like crawlers toward multitask locomotion of conformal grasping, path navigation, and obstacle avoidance. This framework bridges digital design with physical intelligence, unlocking previously unidentified avenues of soft robots for creating sophisticated and programmable morphologies.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 传统刺激响应策略的软体致动器在制造简易性与运动学复杂性之间存在根本性权衡：简单制造方法通常仅能产生单一或简单变形模式，难以实现复杂的可配置三维运动。
- 受生物启发的形态变形结构是下一代软体机器人实现高度适应性的关键，但现有技术缺乏同时兼顾制造简便与运动多样性的能力。
- 本文旨在引入一种空间差异化的激光编程技术，通过跨尺度控制激光能量和扫描方向，同步调节材料异质性与结构层次，从而在激光诱导石墨烯基软体致动器（LIG-SA）中编码多种基本运动单元，并实现自由形态变形的仿生机器人。

## 二、论文提出的方法论
- 核心思想：通过空间差异化的激光编程，将材料异质性和结构层级的控制相结合，解耦电热分布与刚度各向异性，从而为LIG-SA编码四种典型运动单元：
  - 直线弯曲（straight bending）
  - 定向卷曲（directional curling）
  - 刚性支撑（rigid supporting）
  - 软连接（soft connecting）
- 关键技术细节：
  - 跨尺度控制激光能量（影响材料石墨化程度与电热特性）和划线方向（影响结构各向异性与刚度分布）。
  - 通过激光参数的局部变化，在同一LIG-SA基材上实现不同区域的差异化响应，形成可编程的变形域。
- 算法/流程（用文字说明）：
  - 步骤1：设计目标变形形态，分解为四种基本运动单元的组合。
  - 步骤2：利用空间差异化激光编程，在LIG-SA的特定区域分别设置激光能量和扫描方向，编码对应的运动单元。
  - 步骤3：通过电热激励（如通电加热）激活各区域的不同变形模式，实现整体组合运动。
  - 步骤4：将多模态变形单元任意分组并集成到具体装置中，构成仿生机器人。

## 三、实验设计
- 使用的数据集/场景：本文未明确提及公开数据集，而是基于物理实验构建了多种仿生机器人场景：
  - 章鱼状触手（用于共形抓取）
  - 尺蠖状爬行器（用于路径导航）
  - 海豹状爬行器（用于避障）
- Benchmark：文中未提及与现有方法或系统的标准基准对比，主要展示自身方法的可行性及多种运动能力。
- 对比方法：未明确与其他同类方法（如传统热响应、光响应致动器）进行定量对比，更多是定性演示。

## 四、资源与算力
- 文末未明确说明使用的GPU型号、数量或训练时长。
- 鉴于本文主要涉及激光加工工艺和物理实验，未涉及大规模深度学习训练，因此算力消耗较低，但具体硬件资源未提及。

## 五、实验数量与充分性
- 实验数量：论文介绍了几类变形单元的原理验证，以及章鱼触手、尺蠖、海豹三种仿生机器人的功能演示。未提供详细的重复实验次数或统计误差分析。
- 充分性分析：实验覆盖了从基本运动单元到多种仿生机器人的功能展示，证明了方法的可行性；但缺乏系统性的定量性能评估（如弯曲角度精度、响应速度、寿命、负载能力等）以及与其他技术的对照实验，因此充分性有限。
- 客观性与公平性：实验设计偏向概念验证，未设置基线对照或多折交叉验证，可能存在选择偏差。

## 六、论文的主要结论与发现
- 空间差异化激光编程技术成功实现了LIG-SA中四种典型运动单元的编码，且这些单元可任意组合，产生自由形态的三维变形。
- 基于该技术制造的仿生机器人（章鱼触手、尺蠖、海豹）能够在复杂任务中实现共形抓取、路径导航和避障等多模式运动。
- 该框架连接数字设计与物理智能，为可编程形态软体机器人开辟了新途径，克服了制造简易与运动复杂性间的权衡。

## 七、优点
- 创新性强：首次将空间差异化激光编程用于同时控制材料异质性和结构层级，实现多模态运动单元的片上编码。
- 制造简单：基于激光直写技术，无需复杂多层或异质材料堆叠，减少了工艺复杂度。
- 组合灵活：四种基本单元可任意分组并集成，赋予软体机器人高度可配置的变形能力。
- 仿生应用多样：成功演示了触手抓取、爬行机器人等代表性应用，展示了实际潜力。

## 八、不足与局限
- 实验覆盖不足：缺乏与其他软体致动器技术的定量对比（如响应时间、功耗、载荷等），难以评估其性能优势。
- 缺乏统计验证：展示的变形与运动多为定性演示，未报告重复性误差或控制精度。
- 应用限制：激光编程对材料（LIG）有特定要求，目前可能局限于碳基复合材料；且当前演示的机器人运动速度、尺度及负载能力可能有限。
- 可扩展性未验证：从基本单元组合到复杂机器人尚需稳定的对接与驱动控制策略，论文未深入讨论多单元协同控制的鲁棒性。
- 资源与算力信息缺失，不利于可复现性评估。

（完）
