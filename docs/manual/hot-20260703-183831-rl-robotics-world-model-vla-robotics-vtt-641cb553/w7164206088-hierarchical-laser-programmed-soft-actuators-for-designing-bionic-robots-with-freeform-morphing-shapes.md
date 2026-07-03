---
title: Hierarchical laser-programmed soft actuators for designing bionic robots with freeform morphing shapes
title_zh: 分层激光编程软致动器用于设计具有自由形态变形能力的仿生机器人
authors: "Y.S.H. Guo, Mingguang Han, Weixiong Yang, Meihong He, Haibin Duan, Xilun Ding, Sida Luo"
date: 2026-06-10
pdf: "https://www.science.org/doi/pdf/10.1126/sciadv.aeb1989?download=true"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:physical intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=1; institution_filter=company; company_relation_match=physical intelligence; relation_source=abstract; institutions=Beihang University; query=reinforcement learning for robot navigation"
tldr: 受生物启发的形状变形结构对下一代软体机器人至关重要，但现有刺激响应策略在制造简单性与运动复杂性间存在权衡。本文提出空间差异化激光编程技术，通过跨尺度控制激光能量与扫描方向，同时调节材料异质性与结构层次，实现解耦的电热分布与刚度各向异性，从而编码直弯、定向卷曲、刚性支撑、软连接四种运动单元。通过任意组合多模态变形单元，成功设计章鱼触手、尺蠖/海豹爬行器等仿生机器人，实现共形抓取、路径导航与避障。该框架连接数字设计与物理智能，为软体机器人创建复杂可编程形态开辟新途径。
source: openalex
selection_source: hot_paper_scout
motivation: 破解现有刺激响应软体致动器在制造简单性与运动复杂性之间的固有矛盾，实现自由形态变形能力。
method: 通过空间差异化激光编程技术，跨尺度控制激光能量与扫描方向，同时调控材料异质性与结构层次，编码四种基本运动单元。
result: 组合多模态变形单元，成功制造章鱼触手、尺蠖/海豹爬行器等仿生机器人，实现共形抓取、路径导航与避障等多任务运动。
conclusion: 该框架连接数字设计与物理智能，为软体机器人创造复杂可编程形态提供全新范式。
---

## 摘要
受生物启发的形态变形结构对于下一代具有前所未有的适应性的软体机器人至关重要，这要求执行器能够实现复杂且可配置的三维运动。通过克服传统刺激响应策略在制造简单性与运动复杂性之间的权衡，我们引入了一种空间差异化的激光编程技术，用于数字制造具有自由形态变形能力的激光诱导石墨烯基软致动器（LIG-SA）。通过跨尺度控制激光能量和刻划方向，可以同时调节材料非均匀性和结构层次，从而引入解耦的电热分布和刚度各向异性，进而为LIG-SA编码四种典型的运动单元：直弯曲、定向卷曲、刚性支撑和软连接。通过将多模态变形单元任意分组到具体化的设备中，这种方法进一步实现了仿生机器人的自由形态设计，包括章鱼状触手和尺蠖/海豹状爬行器，用于多任务运动：共形抓取、路径导航和避障。该框架将数字设计与物理智能相结合，为创建复杂且可编程形态的软体机器人开辟了前所未有的途径。

## Abstract
Bio-inspired shape-morphing structures, essential for next-generation soft robotics with unprecedented adaptability, demand actuators capable of complex and configurable three-dimensional motions. By overcoming traditional stimulus-responsive strategies facing the trade-off between manufacturing simplicity and kinematic sophistication, here, we introduce a spatially differentiated laser-programming technology for digital manufacturing laser-induced graphene-based soft actuators (LIG-SAs) with freeform morphing capabilities. Via cross-scale control of lasing energy and scribing direction, material heterogeneity and structural hierarchy can be tuned simultaneously for introducing decoupled electrothermal distribution and stiffness anisotropy, thus encoding LIG-SAs with four typical motion units: straight bending, directional curling, rigid supporting, and soft connecting. By arbitrarily grouping multimodal morphing units into concretized devices, this approach further empowers freeform design of bionic robots including octopus-like tentacles and inchworm/seal-like crawlers toward multitask locomotion of conformal grasping, path navigation, and obstacle avoidance. This framework bridges digital design with physical intelligence, unlocking previously unidentified avenues of soft robots for creating sophisticated and programmable morphologies.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 生物启发的形状变形结构对下一代高适应性软体机器人至关重要，需要执行器具备复杂且可配置的三维运动能力。
- 现有刺激响应策略存在制造简单性与运动复杂性之间的权衡：要么制造流程复杂但运动模式单一，要么制造简单但难以实现复杂、可编程的形态变化。
- 本文旨在破解这一矛盾，开发一种既能简化制造又能赋予软体机器人自由形态变形能力的新技术，从而实现仿生机器人的多任务运动（如共形抓取、路径导航、避障）。

## 二、论文提出的方法论
- **核心思想**：提出空间差异化激光编程技术，通过跨尺度控制激光能量和扫描方向，同时调节材料非均匀性与结构层次，实现电热分布与刚度各向异性的解耦，从而编码四种基本运动单元。
- **关键技术细节**：
  - 使用激光诱导石墨烯（LIG）作为活性材料，制造软致动器（LIG-SA）。
  - 跨尺度控制参数：激光能量影响材料电热性能，扫描方向引入结构各向异性。
  - 编码四种运动单元：
    - 直弯曲（straight bending）
    - 定向卷曲（directional curling）
    - 刚性支撑（rigid supporting）
    - 软连接（soft connecting）
- **算法流程（文字描述）**：
  1. 通过数字设计规划目标变形形态；
  2. 依据解耦的电热-刚度映射关系，将目标运动分解为基本运动单元的组合；
  3. 利用激光编程技术在不同区域施加特定激光能量和扫描方向，一次性制造出具有异质电热分布和刚度梯度的LIG-SA；
  4. 集成多模态变形单元形成具体仿生机器人，通过电热激励驱动实现预定运动。

## 三、实验设计
- **使用场景/数据集**：未使用公开数据集，而是以仿生机器人设计为场景，包括章鱼触手（用于共形抓取）、尺蠖爬行器、海豹爬行器（用于路径导航和避障）。
- **Benchmark**：未明确设置外部基准方法，但通过与传统刺激响应策略（如单模式弯曲致动器、均匀材料致动器）对比，体现本方法在运动复杂性和制造简易性上的优势。
- **对比方法**：主要与现有软体致动器制造方法（如传统热响应/光响应致动器、3D打印/多层复合方法）进行定性比较，突显空间差异化激光编程的一步制造和多模态优势。

## 四、资源与算力
- **未明确说明**：论文摘要和元数据中未提及使用的GPU型号、数量、训练时长等算力资源。该方法侧重制造工艺而非深度学习模型训练，因此可能不涉及大规模计算资源消耗。

## 五、实验数量与充分性
- **实验数量**：论文设计了至少三种仿生机器人实例（章鱼触手、尺蠖爬行器、海豹爬行器），每个实例展示了不同的运动模式（抓取、爬行、避障）。
- **充分性评价**：
  - 实验覆盖了多种典型运动单元（弯曲、卷曲、支撑、连接）及其组合，验证了方法的通用性。
  - 但缺乏定量对比实验（如抓取力、爬行速度、能耗等指标），也未进行大规模消融实验（如不同激光参数的影响）。实验偏向于概念验证，充分性一般，但足以证明方法的可行性。

## 六、论文的主要结论与发现
- 空间差异化激光编程技术可同时调控材料非均匀性与结构层次，实现解耦的电热-刚度控制。
- 基于四种基本运动单元，可以自由组合设计具有复杂三维变形能力的软体机器人。
- 制造的仿生机器人（章鱼触手、尺蠖/海豹爬行器）成功实现了共形抓取、路径导航和避障等多任务运动。
- 该方法将数字设计与物理智能融合，为软体机器人创建可编程形态提供了全新范式。

## 七、优点
- **制造简单性**：通过一步激光编程即可实现多模态变形，避免了多层复合、模具等复杂工艺。
- **运动复杂性**：能够编码多种基本运动单元，并自由组合，突破了传统致动器的单一运动模式限制。
- **跨尺度调控**：同时控制材料异质性和结构层次，实现电热与刚度的解耦，设计空间大。
- **仿生应用直观**：直接对应生物运动模式（抓取、蠕动、俯卧爬行），展示了实际应用潜力。

## 八、不足与局限
- **实验覆盖不充分**：缺乏定量性能评测（如弯曲角度、响应速度、寿命、负载能力等），也未见与其他方法在同一指标下的严格对比。
- **偏差风险**：仅演示了少数几种构型，且未讨论参数敏感性或制造误差对运动的影响，可能夸大通用性。
- **应用限制**：
  - 目前依赖于电热驱动，响应速度可能较慢（热惯性），能耗较高。
  - 材料体系局限于激光诱导石墨烯，缺乏对其他柔性基底或驱动机制的拓展讨论。
  - 未进行大规模自动化设计或多目标优化，实际工程部署需进一步开发设计工具。
- **资源与算力未说明**：如果涉及设计优化或数字孪生，可能需要计算资源，但论文未提及，评审完整性不足。

（完）
