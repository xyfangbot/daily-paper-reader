---
title: Hierarchical laser-programmed soft actuators for designing bionic robots with freeform morphing shapes
title_zh: 层级激光编程软体致动器用于设计自由形态变形的仿生机器人
authors: "Y.S.H. Guo, Mingguang Han, Weixiong Yang, Meihong He, Haibin Duan, Xilun Ding, Sida Luo"
date: 2026-06-10
pdf: "https://www.science.org/doi/pdf/10.1126/sciadv.aeb1989?download=true"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:physical intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=1; institution_filter=company; company_relation_match=physical intelligence; relation_source=abstract; institutions=Beihang University; query=robot foundation model"
tldr: 传统刺激响应软执行器在制造简单性与运动复杂性间存在权衡，难以实现复杂3D变形。本文提出空间差异化激光编程技术，通过跨尺度控制激光能量和划线方向，同时调节材料异质性与结构层次，编码直弯曲、定向卷曲、刚性支撑和柔性连接四种运动单元，制造出激光诱导石墨烯软执行器（LIG-SAs）。基于此，自由组合多模态变形单元构建了章鱼触手、尺蠖/海豹爬行器等仿生机器人，实现共形抓取、路径导航和避障等任务。该框架桥接数字设计与物理智能，为软体机器人复杂可编程形态设计开辟新途径。
source: openalex
selection_source: hot_paper_scout
motivation: 克服传统刺激响应策略在制造简单性-运动复杂性之间的权衡，实现软执行器的复杂可配置3D运动。
method: 空间差异化激光编程技术，通过跨尺度调控激光能量与划线方向，同步调节材料异质性和结构层次，赋予四种典型运动单元。
result: LIG-SAs具备自由形态变形能力，组建的多模态仿生机器人（章鱼触手、尺蠖/海豹爬行器）完成共形抓取、路径导航与避障。
conclusion: 该框架实现了数字设计与物理智能的融合，为软体机器人构建复杂可编程形态提供了新范式。
---

## 摘要
受生物启发的形态变形结构是下一代具有前所未有适应性的软体机器人的关键，它需要能够实现复杂且可配置的三维运动的致动器。通过克服传统刺激响应策略在制造简便性与运动复杂性之间的权衡，本文引入了一种空间差异化的激光编程技术，用于数字制造具有自由形态变形能力的激光诱导石墨烯基软体致动器（LIG-SA）。通过跨尺度控制激光能量和划刻方向，可以同时调节材料异质性和结构层次，从而引入解耦的电热分布和刚度各向异性，进而为LIG-SA编码四种典型的运动单元：直弯、定向卷曲、刚性支撑和柔性连接。通过将多模态变形单元任意组合成具体设备，该方法进一步实现了仿生机器人（包括章鱼状触手和尺蠖/海豹状爬行器）的自由形态设计，以完成共形抓取、路径导航和避障等多任务运动。该框架将数字设计与物理智能相结合，为软体机器人创造复杂且可编程形态开辟了前所未有的途径。

## Abstract
Bio-inspired shape-morphing structures, essential for next-generation soft robotics with unprecedented adaptability, demand actuators capable of complex and configurable three-dimensional motions. By overcoming traditional stimulus-responsive strategies facing the trade-off between manufacturing simplicity and kinematic sophistication, here, we introduce a spatially differentiated laser-programming technology for digital manufacturing laser-induced graphene-based soft actuators (LIG-SAs) with freeform morphing capabilities. Via cross-scale control of lasing energy and scribing direction, material heterogeneity and structural hierarchy can be tuned simultaneously for introducing decoupled electrothermal distribution and stiffness anisotropy, thus encoding LIG-SAs with four typical motion units: straight bending, directional curling, rigid supporting, and soft connecting. By arbitrarily grouping multimodal morphing units into concretized devices, this approach further empowers freeform design of bionic robots including octopus-like tentacles and inchworm/seal-like crawlers toward multitask locomotion of conformal grasping, path navigation, and obstacle avoidance. This framework bridges digital design with physical intelligence, unlocking previously unidentified avenues of soft robots for creating sophisticated and programmable morphologies.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 传统刺激响应软执行器（如水凝胶、形状记忆聚合物、液晶弹性体、纳米复合材料）能实现基本变形（膨胀、收缩、均匀弯曲），但面对需要高级运动协调和形态重构的任务时存在明显约束。
- 现有局部编程方法（如3D打印、激光雕刻、层压、喷墨打印等）在制造精度、材料多样性、多模态集成方面存在根本性权衡：光刻精度高但材料选择严格；直接墨水写入能多材料集成但分辨率和界面可靠性下降。
- 多模态执行器（如弯曲、卷曲兼具）常需复杂多步制造流程，牺牲制造效率和灵活性，阻碍形状变形的可编程自由度。
- 激光诱导石墨烯（LIG）技术虽在传感器、加热器、发电机等领域展现优势，但现有LIG软执行器在结构集成与变形复杂性之间始终存在权衡，只能实现简单均匀弯曲或有限的非均匀变形。
- 本文旨在通过空间差异化激光编程技术，实现单步制造具有自由形态变形能力的LIG-SA，桥接数字设计与物理智能，为软体机器人开辟复杂可编程形态的新途径。

## 二、论文提出的方法论
- **核心思想**：通过跨尺度（局部尺度 - 组件尺度 - 器件尺度）控制激光能量和划线方向，同步调节材料异质性与结构层次，引入解耦的电热分布和刚度各向异性，从而编码四种基本运动单元（直弯曲、定向卷曲、刚性支撑、柔性连接），再通过任意组合这些单元实现自由形态变形。
- **关键技术细节**：
  - 采用三层结构：底层Kapton胶带（密封）、中间LIG层（焦耳加热兼机械约束层）、顶层PDMS（热活性层）。通过直流电源供电，利用差异热膨胀效应驱动变形。
  - **策略一：差异化激光能量（DLE）**：通过控制激光聚焦/散焦状态，调节局部石墨化程度和电阻（8~261Ω/sq）。高电阻区域在相同电流下温度更高，弯曲曲率更大，形成“关节”状运动；低电阻区域几乎不弯曲。可编程关节的位置、长度和数量。
  - **策略二：定向激光划线（DLS）**：通过改变激光扫描方向（-90°至90°），形成微条纹图案（交替软硬区域），产生机械各向异性（弯曲模量33.4~103.4 MPa）和电学各向异性（电阻76.3~118.2 Ω/sq）。划线角度决定卷曲方向与卷曲圈数（0~1.1圈）和偏差距离（0~38 mm）。90°划线时刚度最大，几乎不变形，用作刚性支撑；0°划线时柔韧性最大，实现直弯曲。
  - **组合策略**：将DLE和DLS结合，可对每个局部区域独立编程（三种基本类型：规则弯曲、定向卷曲、固定），实现多关节、多形态的复杂变形。
- **算法/流程**：计算机控制CO₂激光器根据设计路径扫描PI纸（90μm厚），形成LIG图案；然后涂覆导电银浆、连接铜线；旋涂PDMS并固化；最后切割成型。整个过程约2小时，可实现批量制造。

## 三、实验设计
- **数据集/场景**：未使用标准公开数据集。实验基于自建PI纸作为基底，通过激光参数调节实现不同电阻、不同划线角度的LIG-SA样本。应用场景涵盖章鱼触手式抓取机器人（单触手或多触手）、尺蠖爬行机器人（CR-I）、海豹爬行机器人（CR-V、CR-Y）在迷宫、管道、冰墙等环境中的任务。
- **Benchmark**：论文未明确定义标准benchmark。对比了不同激光参数（能量、散焦量、划线角度）、不同电流水平（10~80 mA）下的变形性能（曲率、卷曲数、偏差距离）。此外，将与现有热驱动双向爬行机器人和多足转向机器人进行了定量性能对比（见表S1、表S2、图S34、S36）。
- **对比方法**：论文主要对比了均匀处理LIG-SA与采用DLE/DLS策略的多区域LIG-SA，以及不同组合方式下的变形效果。没有与同类激光编程技术的其他工作（如纯机械刻蚀、喷墨打印等）直接进行定量基准比较。定性对比展示了其独特优势（一步制造、自由形态）。

## 四、资源与算力
- 论文未明确提供GPU型号、数量、训练时长等算力信息。
- 使用了商用CO₂激光系统（Universal Laser Systems DLS 2.3）、直流电源（三通道）、红外热像仪、动态力学分析系统、扫描电镜、拉曼光谱仪等常规实验设备。
- 有限元仿真采用ABAQUS 2022版本，在线性弹性假设下进行电-热-力耦合计算，未提及具体计算资源。

## 五、实验数量与充分性
- **实验数量**：非常丰富。包括：
  - 不同电阻（8~261 Ω/sq）与不同散焦量/激光功率的系统测试（图3C）。
  - 100次循环耐久性测试（图3D）。
  - 电流-曲率线性关系（10~80 mA，图3E）。
  - 电阻-曲率关系（不同电流下，图3F）。
  - 两区域电阻比与曲率比线性关系（图3G）。
  - 多参数可编程关节设计（图3H~K）：不同电阻水平、长度、位置、数量。
  - DLS实验：不同划线角度下的卷曲圈数、偏差距离、电阻、弯曲模量（图4A~C）。
  - 多类型结构演示：单关节、双关节、十字形、闭环、展开结构（图4G~K）。
  - 多种仿生机器人实验：章鱼单触手三种模式、四触手四种抓取类型、尺蠖双向爬行、海豹转向/爬行、迷宫导航、越障、融冰、电路修复等（约14个视频补充材料）。
- **充分性与客观性**：
  - 实验覆盖了从材料表征、运动定量分析到机器人级演示的完整链条，设计较为充分。
  - 提供了大量定量数据（曲率、温度、电阻、力、速度、角度等），且多数数据具有统计或线性拟合。
  - 但缺乏严格的统计显著性检验（如重复次数仅部分说明）。对性能的基准对比（表S1、S2）虽已列出，但比较范围有限（仅与少数热驱动爬行机器人比较），对比方法的参数和实验条件描述不够详细。
  - 消融实验（如移除一种策略）未见明确设计，但通过逐一改变参数可间接体现各因素贡献。
  - **总体评价**：实验设计较充分，客观性较好，但基准对比不够全面，可进一步加强。

## 六、论文的主要结论与发现
- 空间差异化激光编程技术能够单步制造具有自由形态变形能力的LIG-SA，同时实现制造简便性和运动复杂性的统一。
- 通过跨尺度控制激光能量（DLE）和划线方向（DLS），可以同步调节局部电热特性（电阻）和力学特性（弯曲模量），实现四种独立运动模式（直弯曲、定向卷曲、刚性支撑、柔性连接）。
- 区域化设计可精确控制曲率分布（电阻比与曲率比线性相关）、卷曲圈数和偏差距离（由划线角度和电阻共同决定）。
- 基于该技术，成功构建了多种仿生软体机器人：章鱼触手（三种抓取模式）、多触手抓取机器人（四种配置，对应不同形状目标）、尺蠖式双向爬行机器人（CR-I，速度36.5 mm/min）、海豹式转向/爬行机器人（CR-V可360°旋转，CR-Y可实现直线+转向+迷宫避障+融冰+电路修复等复合任务）。
- 该框架桥接数字设计与物理智能，打开了软体机器人复杂、可编程形态设计的新途径。

## 七、优点
- **创新性方法论**：将激光能量和划线方向两个参数跨尺度协同控制，同时实现材料异质性和结构层次调节，打破了传统方法在制造简便性和变形复杂性之间的权衡。
- **单步、可扩展制造**：整个制造过程仅需一步激光写入+涂敷封装，无需多步异质集成，2小时内可完成，支持批量生产。
- **高设计自由度**：任意组合四种基本运动单元，可实现从简单弯曲到多关节、变方向、甚至闭环/展开结构的复杂3D变形。
- **定量可控性**：建立了电阻-曲率、划线角度-卷曲圈数/偏差距离等明确的量化关系，有限元仿真可预测变形，支撑精确编程。
- **多功能集成**：机器人不仅具有变形能力，还利用LIG的导电性和焦耳热效应实现电热冰融和电路修复功能，展现多功能一体化。
- **仿生应用丰富**：演示了多种生物启发下的抓取、爬行、导航任务，包括复杂环境（狭缝、管道、冰墙）中的作业，验证了实用潜力。

## 八、不足与局限
- **基准对比有限**：尽管附录中有少量比较，但整体缺乏与现有软体致动器（如其他LIG工作、形状记忆聚合物、液晶弹性体等）在相同任务下的系统性定量性能比较（如速度、负载、寿命、能耗等），难以全面评估其领先程度。
- **实验统计强度不足**：部分定量结果（如曲率、卷曲数）仅展示单次或少量重复，未给出误差棒或统计显著性水平（如p值）。循环测试虽进行了100次，但仅在一组参数下完成，代表性有限。
- **应用场景限制**：演示的机器人均为实验室环境下的简单任务（抓取泡沫、爬行平板、融冰等），未涉及真实复杂工业或自然场景（如崎岖地形、水下、高温/低温、电磁干扰等）。抓取物体的尺寸和重量相对较小。
- **长期可靠性未深入探讨**：材料疲劳、环境老化（湿度、氧气）、多次变形后的电性能漂移等长期性能数据不足。尽管提及电阻漂移很小，但只限于短期弯曲和温度测试。
- **驱动方式受限**：仅采用电热驱动（焦耳热），响应速度受限于热传导/散热，无法快速恢复，主动冷却辅助才能提升。缺乏与其他驱动方式（光、磁、湿度等）的兼容性比较。
- **制造精度与规模问题**：尽管LIG可实现微米级加工，但PDMS旋涂和手工组装可能引入误差。批量一致性、大面积制造时的均匀性未详细讨论。
- **仿生机器人自主性低**：大多数机器人需要外部手动操作电源开关或改变输入电流，缺乏闭环自主感知与决策能力（除CR-Y的部分路径规划外）。与集成传感器、强化学习等先进控制方法尚有差距。

（完）
