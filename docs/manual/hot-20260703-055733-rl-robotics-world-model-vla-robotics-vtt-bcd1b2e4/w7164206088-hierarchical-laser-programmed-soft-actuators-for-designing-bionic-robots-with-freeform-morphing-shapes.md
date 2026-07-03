---
title: Hierarchical laser-programmed soft actuators for designing bionic robots with freeform morphing shapes
title_zh: 层级激光编程软体驱动器用于设计具有自由形态变形的仿生机器人
authors: "Y.S.H. Guo, Mingguang Han, Weixiong Yang, Meihong He, Haibin Duan, Xilun Ding, Sida Luo"
date: 2026-06-10
pdf: "https://www.science.org/doi/pdf/10.1126/sciadv.aeb1989?download=true"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:physical intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=1; institution_filter=company; company_relation_match=physical intelligence; relation_source=abstract; institutions=Beihang University; query=reinforcement learning for robot navigation"
tldr: 传统刺激响应策略在制造简单性与运动复杂性间存在权衡。本文提出空间差异化激光编程技术，通过跨尺度控制激光能量和扫描方向，同时调控材料异质性与结构层次，编码出四种基本运动单元。任意组合这些单元，设计了章鱼触手、尺蠖/海豹爬行器等仿生机器人，实现抓取、导航、避障等多任务运动。该框架将数字设计与物理智能融合，为软机器人创造复杂可编程形态提供新途径。
source: openalex
selection_source: hot_paper_scout
motivation: 克服传统刺激响应策略中制造简单性与运动复杂性之间的权衡，实现可配置的三维复杂运动。
method: 通过跨尺度控制激光能量和扫描方向，同时调控材料异质性与结构异向性，编码四种运动单元。
result: 任意组合运动单元，设计出章鱼触手、尺蠖及海豹爬行器等仿生机器人，完成抓取、导航和避障任务。
conclusion: 该框架将数字设计与物理智能融合，为软机器人创造复杂可编程形态开辟新途径。
---

## 摘要
受生物启发的形态变形结构对于具有空前适应性的下一代软体机器人至关重要，这要求驱动器能够实现复杂且可配置的三维运动。通过克服传统刺激响应策略在制造简易性与运动复杂性之间的权衡，我们引入了一种空间差异化的激光编程技术，用于数字化制造具有自由形态变形能力的激光诱导石墨烯基软体驱动器（LIG-SA）。通过跨尺度控制激光能量和划线方向，可以同时调控材料异质性和结构层次，引入解耦的电热分布和刚度各向异性，从而为LIG-SA编码四种典型运动单元：直线弯曲、定向卷曲、刚性支撑和柔性连接。通过将多模态变形单元任意组合成具体设备，该方法进一步实现了仿生机器人的自由形式设计，包括章鱼状触手和尺蠖/海豹状爬行器，用于共形抓取、路径导航和避障等多任务运动。该框架将数字设计与物理智能相结合，为软体机器人创造复杂且可编程的形态开辟了前所未有的途径。

## Abstract
Bio-inspired shape-morphing structures, essential for next-generation soft robotics with unprecedented adaptability, demand actuators capable of complex and configurable three-dimensional motions. By overcoming traditional stimulus-responsive strategies facing the trade-off between manufacturing simplicity and kinematic sophistication, here, we introduce a spatially differentiated laser-programming technology for digital manufacturing laser-induced graphene-based soft actuators (LIG-SAs) with freeform morphing capabilities. Via cross-scale control of lasing energy and scribing direction, material heterogeneity and structural hierarchy can be tuned simultaneously for introducing decoupled electrothermal distribution and stiffness anisotropy, thus encoding LIG-SAs with four typical motion units: straight bending, directional curling, rigid supporting, and soft connecting. By arbitrarily grouping multimodal morphing units into concretized devices, this approach further empowers freeform design of bionic robots including octopus-like tentacles and inchworm/seal-like crawlers toward multitask locomotion of conformal grasping, path navigation, and obstacle avoidance. This framework bridges digital design with physical intelligence, unlocking previously unidentified avenues of soft robots for creating sophisticated and programmable morphologies.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 传统刺激响应软体驱动器（如基于水凝胶、形状记忆聚合物等）虽然能实现基础变形（弯曲、收缩），但多局限于均匀形变，难以实现复杂、可配置的三维运动。
- 现有局部编程方法（如3D打印、光刻、激光刻蚀）虽然在提升变形复杂度上取得进展，但普遍存在制造精度与材料多样性之间的权衡，且集成多种驱动模式往往需要复杂、多步骤的异质组装过程，影响了制造效率、可扩展性和编程自由度。
- 本研究旨在开发一种**单步、数字化的激光编程技术**，在不牺牲制造简易性的前提下，实现软体驱动器的**自由形态变形**能力，并直接用于组装具有复杂生物形态的仿生机器人。

## 二、论文提出的方法论
- **核心思想**：通过**空间差异化的激光编程**，对激光诱导石墨烯（LIG）层进行跨尺度（局部→组件→器件）控制，同时调控材料异质性与结构层次，从而解耦电热分布和刚度各向异性，编码出四种基本运动单元。
- **关键技术细节**：
  - **材料结构**：三层结构（Kapton底层 + LIG中间层 + PDMS顶层），通过电热驱动产生差热膨胀实现形变。
  - **两种局部编程策略**：
    - **差异激光能量（DLE）**：通过改变离焦量（DL）控制碳化程度与电阻，实现局部温度与弯曲曲率的独立调控，产生“指关节”式运动。
    - **定向激光划线（DLS）**：通过改变划线角度（−90°至90°），引入各向异性刚度与卷曲方向，实现定向卷曲或刚性支撑。
  - **四种运动单元**：直线弯曲（0°聚焦）、定向卷曲（45°聚焦）、刚性支撑（90°聚焦）、柔性连接（0°离焦）。
  - **设计流程**：通过有限元仿真（ABAQUS）预测形变，然后任意组合局部单元，设计出**单关节、多关节、十字形、闭环、可展开**等复杂结构。
- **公式/算法**：文中未提供显式数学公式，但给出了电阻-曲率、卷曲角度-电流之间的定量关系（如线性拟合、电阻比与曲率比线性相关）。

## 三、实验设计
- **实验场景与数据集**：
  - 使用PI纸、Kapton、PDMS等材料自制驱动器，未使用公开数据集。
  - 测试场景包括：不同激光参数（离焦量、功率、划线角度）下的材料电阻、微观形貌（SEM、拉曼、XRD）、弯曲曲率、卷曲角度、刚度。
  - 仿生机器人场景：章鱼触手三种模式（前向卷曲收集、远端屈曲钩取、螺旋缠绕提取）、四种十字抓手（抓取球/矩形/锥体/组合目标）、尺蠖爬行器（双向直线）、海豹爬行器（转向+蠕动），以及迷宫导航、跨缝隙、融冰、电路修复等多任务避障。
- **Benchmark**：未设立统一的定量对比基准，但与文献中类似热驱动器进行了性能比较（如爬行速度、转弯角度，见补充材料表S1/S2）。
- **对比方法**：未直接对比其他驱动技术（如形状记忆聚合物、液晶弹性体等），主要展示了本方法自身的参数调控能力和多功能性。

## 四、资源与算力
- 文中未明确说明 GPU 型号、数量或训练时长。
- 有限元仿真使用 ABAQUS 2022 进行电-热-力耦合计算，但未提及计算平台细节（如 CPU/GPU、内存、耗时）。
- 实验制造与测试主要依赖激光加工系统（CO₂激光器）、直流电源、红外热像仪等常规设备。

## 五、实验数量与充分性
- 实验数量较多且系统：
  - 材料表征：不同DL、功率下电阻（图3C）、SEM/Raman（附图S6-S10）。
  - 单循环与循环耐久性（100次循环，图3D）。
  - 多参数定量关系：电流-温度-曲率（图3E-F）、电阻比-曲率比（图3G）、卷曲角度-电流（图4A-B）、刚度-角度（图4C）。
  - 多关节设计：单/双/多关节、十字形、闭环、可展开结构（图4G-K）。
  - 仿生机器人演示：8种以上不同构型，涵盖抓取、爬行、转向、避障。
- 实验覆盖了从局部单元到器件系统的多层级验证，**充分性较高**。
- 不足：实验主要在实验室环境（室温、水平地面）进行，缺乏与同类先进方法的直接对比基准（如爬行速度、负载能力、能量效率的横向比较表）。

## 六、论文的主要结论与发现
- 空间差异化激光编程技术能够**一步制造**具有自由形态变形能力的LIG-SA，突破了传统方法在制造简单性与运动复杂性之间的权衡。
- 通过引入DLE和DLS，可独立控制局部区域的电热与力学属性，编码四种基本运动单元，并通过任意组合实现复杂三维形变。
- 基于该技术成功设计了多种仿生机器人：章鱼触手可实现悬垂收集、缝隙探测、螺旋缠绕；十字抓手能共形抓取不同形状物体；尺蠖/海豹爬行器能在迷宫导航、跨缝隙、融冰、电路修复等任务中自主移动。
- 框架将数字设计与物理智能融合，为创造复杂可编程软体机器人开辟了新途径。

## 七、优点
- **数字化与单步制造**：无需多步异质组装，通过计算机控制激光参数即可在单一基底上编程多种驱动模式，制造效率高、可定制性强。
- **自由组合与可扩展性**：四种基本运动单元可任意组合，支持从简单弯曲到复杂3D形态的过渡，适用于不同尺寸和几何形状。
- **跨尺度控制**：从局部材料属性到组件级形变到器件级功能，实现了多层级的协同设计。
- **多功能一体化**：同一器件可兼具抓取、爬行、转向、加热、导电等多重功能，无需额外集成。
- **丰富的仿生验证**：涵盖了多种生物启发形态（章鱼、尺蠖、海豹），并展示了实际场景中的多任务能力。

## 八、不足与局限
- **缺少系统化定量比较**：未提供与其他代表性软体驱动器（如形状记忆聚合物、液晶弹性体、磁驱动等）在关键性能指标（如响应速度、负载能力、能量效率、寿命）上的严格对比。
- **环境适应性有限**：实验主要在室温、水平、干燥条件下进行，缺乏对潮湿、高温、粗糙表面等真实复杂环境的测试。
- **疲劳与可靠性数据不足**：虽然进行了100次循环测试，但缺乏长期（数千次以上）疲劳测试和材料老化分析。
- **驱动方式单一**：仅依赖电热驱动，存在响应速度慢、能耗高的固有局限（加热/冷却周期制约），且文中主动冷却策略仅初步提及。
- **制造与控制的精度限制**：激光划线的最小特征尺寸受限于光斑直径（~100 μm），更精细的局部调控可能受限。
- **可拓展性与成本**：大面积批量制造的一致性与成本未讨论，且依赖PI纸等特定材料，普适性有待验证。

（完）
