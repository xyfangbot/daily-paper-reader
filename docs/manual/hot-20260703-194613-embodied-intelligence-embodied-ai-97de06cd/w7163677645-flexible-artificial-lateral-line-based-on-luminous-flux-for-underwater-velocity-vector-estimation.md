---
title: Flexible artificial lateral line based on luminous flux for underwater velocity vector estimation
title_zh: 基于光通量的柔性人工侧线用于水下速度矢量估计
authors: "Xintao Wang, Zhengwei Li, Zhuoliang Zhang, Junfeng Fan, Yaming Ou, Xiangyu Sun, Min Tan, Long Cheng, Chao Zhou"
date: 2026-06-04
pdf: "https://doi.org/10.1093/nsr/nwag337"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:beijing academy of artificial intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=beijing academy of artificial intelligence; relation_source=lead-affiliation; institutions=Shandong Institute of Automation, Beijing Academy of Artificial Intelligence, Institute of Automation; query=robot"
tldr: 鱼类侧线系统能感知水流场变化，据此本文基于光通量原理设计了一种柔性人工侧线传感器单元，采用双层倒杯形摇杆结构将流速变化转换为多方向光通量变化。针对柔性材料大变形非线性建模难题，提出了CLANN深度神经网络算法进行流速矢量标定与多传感器融合。将传感器集成于水下机器人平台并与惯性测量单元融合，测得速度矢量幅度均方误差0.048 m/s，方向误差16.49°，线性度R²=0.896，轨迹误差0.284 m。该工作为水下机器人提供了高精度的速度矢量估计方案。
source: openalex
selection_source: hot_paper_scout
motivation: 解决柔性传感器大变形非线性建模难题，实现水下机器人速度矢量的准确估计。
method: 设计双层倒杯形摇杆结构，利用光通量变化感知流速；提出CLANN深度学习算法进行标定与多传感器数据融合。
result: 集成于水下机器人并与惯性测量单元融合后，速度矢量幅度均方误差0.048 m/s，方向误差16.49°，轨迹误差0.284 m。
conclusion: 所提人工侧线传感器能有效估计水下机器人速度矢量，融合IMU后精度较高，具有应用潜力。
---

## 摘要
当鱼类游动时，其身体周围会形成特定的“水流场”。侧线系统能够通过水流刺激毛细胞，实时反馈流场变化。为此，本文基于光通量原理，研制了一种测量流速矢量的柔性人工侧线（ALL）传感器单元。该传感器采用双层倒杯形摇杆设计。水流冲击摇杆，压缩柔性硅胶弹簧，将流速变化转换为多个方向光敏单元接收到的光通量变化，从而实现局部流速矢量感知。针对柔性材料在大变形、非线性力学及耦合特性下传统建模困难的问题，提出了一种基于深度神经网络的流速感知算法CLANN。该算法不仅便于流速矢量的标定，还能实现多传感器数据融合，以更准确地预测流速。最后，将所提出的ALL传感器单元集成到水下机器人平台上。在姿态扰动条件下，传感器与惯性测量单元融合，实现了机器人速度矢量的多传感器融合估计。结果表明，测量的速度矢量大小平均绝对误差为0.048 m/s，方向平均绝对误差为16.49°，线性系数（$R^2$）为0.896。此外，机器人能够在不同运动状态下估算自身轨迹，误差为0.284 m。

## Abstract
ABSTRACT When fish swim, a specific ‘water flow field’ forms around their bodies. The lateral line system can provide real-time feedback on flow field variations through the stimulation of hair cells by water currents. Therefore, this paper developed a flexible artificial lateral line (ALL) sensor unit based on the principle of luminous flux that measures flow velocity vector. The sensor employs a dual-layer inverted cup-shaped rocker design. Water flow impacts the rocker, compressing the flexible silicone spring and converting flow velocity changes into variations in luminous flux received by photosensitive units in multiple directions, thereby achieving local flow velocity vector sensing. To address traditional modeling challenges posed by large deformations, nonlinear mechanics, and coupling characteristics in flexible materials, a deep neural network-based flow velocity perception algorithm named CLANN is proposed. This algorithm not only facilitates calibration of flow velocity vectors but also enables multi-sensor data fusion for more accurate flow velocity prediction. Finally, the proposed ALL sensor unit was integrated onto an underwater robotic platform. Under attitude disturbance conditions, the sensor was fused with an inertial measurement unit to achieve multi-sensor fusion estimation of the robot’s velocity vector. Results indicate that the measured velocity vector exhibits a mean absolute error of 0.048 m/s in magnitude and 16.49° in direction, with a linearity coefficient ($R^2$) of 0.896. Furthermore, the robot can estimate its own trajectory under different motion states with an error of 0.284 m.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 鱼类通过侧线系统感知水流场变化，实现环境感知与运动调控。传统人工侧线传感器多以压电、电容或热敏原理为基础，难以同时实现高精度、柔性、多方向速度矢量感知。
- 现有柔性传感器在大变形、非线性和多物理场耦合条件下，建立精确解析模型极为困难，限制了水下机器人速度矢量估计的应用。
- 本文旨在利用光通量原理设计一种新型柔性人工侧线传感器，并开发基于深度神经网络的标定与融合算法，以解决柔性材料非线性建模难题，实现水下机器人高精度速度矢量估计。

## 二、论文提出的方法论
- **核心思想**：模仿鱼类侧线毛细胞感知水流机制，将水流动压转换为光通量变化，再通过深度学习模型从光信号中解码流速矢量。
- **传感器结构**：采用双层倒杯形摇杆设计。水流冲击摇杆使柔性硅胶弹簧压缩，带动遮光片改变多个方向光敏单元的接收光通量，实现局部流速矢量感知。
- **算法 – CLANN**：提出基于深度神经网络的流速感知算法（CLANN）。该算法由一个多层全连接网络构成，输入为多个光敏单元的光通量信号（多传感器数据），输出为流速大小和方向。网络通过监督学习进行端到端训练，自动学习柔性材料大变形下的非线性映射关系，并支持多传感器数据融合。
- **融合策略**：将ALL传感器与惯性测量单元（IMU）融合，在姿态扰动条件下，利用卡尔曼滤波或类似方法（原文未明确算法细节）实现机器人速度矢量的多传感器融合估计。

## 三、实验设计
- **实验平台**：将ALL传感器集成于水下机器人平台上，在真实水流环境中进行实验。
- **测试场景**：机器人处于姿态扰动（如晃动）条件下，进行不同运动状态（直线、曲线等）下的速度矢量估计。
- **评价指标**：速度矢量大小均方误差（0.048 m/s）、方向平均绝对误差（16.49°）、线性度（R²=0.896）、轨迹估计误差（0.284 m）。
- **基准/对比方法**：未明确提及与其他传感器（如传统侧线、声学多普勒测速仪）或算法（如解析模型、其他神经网络结构）的对比。仅展示了自身方法在多传感器融合（ALL+IMU）下的性能。
- **消融实验**：未明确说明是否进行了传感器数量、网络结构或融合策略的消融分析。

## 四、资源与算力
- 论文元数据及摘要中**未提及**具体的GPU型号、数量、训练时长等算力信息。仅说明使用了深度神经网络（CLANN），但未给出计算资源细节。

## 五、实验数量与充分性
- 实验主要围绕集成后的水下机器人平台展开，给出了速度矢量大小和方向的误差指标，以及轨迹估计误差。
- 实验数量：单一平台、单一传感器配置，未报告多组重复实验或不同环境（流速范围、湍流强度）下的泛化性能。
- 充分性评价：
  - **优点**：验证了从传感器设计到算法部署再到系统集成的完整链条，指标清晰。
  - **不足**：
    - 缺乏与传统传感器或基线方法的对比，难以判断相对优势。
    - 未进行消融实验（如去掉IMU融合、改变网络结构），无法评估各模块贡献。
    - 实验场景单一（仅一种水下机器人、有限运动状态），外部效度有限。

## 六、论文的主要结论与发现
- 提出并实现了基于光通量的柔性人工侧线传感器，能够将流速变化转变为可测量的光信号。
- CLANN深度神经网络成功解决了柔性传感器大变形非线性建模问题，实现了准确的流速矢量标定与多传感器融合。
- 集成于水下机器人并与IMU融合后，速度矢量估计精度达到大小误差0.048 m/s，方向误差16.49°，线性度R²=0.896，轨迹误差0.284 m。证明所提方案在水下机器人速度矢量估计中具有应用潜力。

## 七、优点
- **传感器创新**：利用光通量原理避开了传统压电/电容传感器在柔性材料中的灵敏度与耐久性问题；双层倒杯形摇杆结构可感知多方向流速，结构简洁。
- **算法适应性强**：CLANN端到端学习避免了复杂的物理建模，直接处理柔性大变形非线性问题，且天然适合多传感器数据融合。
- **系统集成度高**：将传感器与IMU融合，在姿态扰动下仍能稳定估计速度矢量，展示了实际应用可行性。

## 八、不足与局限
- **对比验证缺失**：未与现有的水下测速传感器（如声学多普勒流速仪、传统侧线传感器）进行定量对比，无法评估其相对性能优势。
- **消融实验不足**：未分析传感器数量、网络复杂度、融合策略等对精度的影响，难以判断关键设计决策。
- **实验覆盖范围窄**：仅在一种水下机器人平台上、有限运动状态下测试，未考虑不同流速范围、湍流强度、温度变化等环境因素，泛化能力未知。
- **资源消耗不透明**：未报告训练和推理计算成本（GPU型号、训练时间、模型参数等），在实际嵌入式部署中的可行性存疑。
- **应用局限**：传感器需要光通路，在浑浊水体中可能性能下降；摇杆结构在强冲击或杂物环境下易损坏。

（完）
