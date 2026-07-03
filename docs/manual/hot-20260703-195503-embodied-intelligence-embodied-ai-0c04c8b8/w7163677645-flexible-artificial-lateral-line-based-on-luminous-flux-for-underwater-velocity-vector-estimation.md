---
title: Flexible artificial lateral line based on luminous flux for underwater velocity vector estimation
title_zh: 基于光通量的柔性人工侧线用于水下速度矢量估计
authors: "Xintao Wang, Zhengwei Li, Zhuoliang Zhang, Junfeng Fan, Yaming Ou, Xiangyu Sun, Min Tan, Long Cheng, Chao Zhou"
date: 2026-06-04
pdf: "https://doi.org/10.1093/nsr/nwag337"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:beijing academy of artificial intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=beijing academy of artificial intelligence; relation_source=lead-affiliation; institutions=Shandong Institute of Automation, Beijing Academy of Artificial Intelligence, Institute of Automation; query=robot"
tldr: 鱼类侧线系统能感知水流场变化。本文基于光通量原理设计柔性人工侧线传感器，采用双层倒扣杯形摇杆将流速变化转为光通量变化。提出CLANN深度神经网络算法解决柔性材料建模难题，实现流速矢量校准与多传感器融合。集成到水下机器人，与IMU融合估计速度矢量，精度达0.048 m/s和16.49°，轨迹误差0.284 m。
source: openalex
selection_source: hot_paper_scout
motivation: 模仿鱼类侧线系统，实现水下流速矢量的高精度感知，克服传统传感器刚性强、易受干扰的局限。
method: 设计基于光通量的双层摇杆柔性传感器，结合CLANN深度神经网络进行流速矢量校准与多传感器数据融合。
result: 速度矢量估计平均绝对误差0.048 m/s和16.49°，线性度0.896，机器人轨迹估计误差0.284 m。
conclusion: 该柔性人工侧线传感器与IMU融合，可有效估计水下机器人速度矢量并估算运动轨迹。
---

## 摘要
摘要：鱼类游动时，其身体周围会形成特定的“流场”。侧线系统能够通过水流对毛细胞的刺激，实时反馈流场变化。为此，本文基于光通量原理开发了一种用于测量流速矢量的柔性人工侧线（ALL）传感器单元。该传感器采用双层倒杯式摇杆设计，水流冲击摇杆压缩柔性硅胶弹簧，将流速变化转化为多个方向光敏单元接收到的光通量变化，从而实现局部流速矢量感知。针对柔性材料大变形、非线性力学及耦合特性带来的传统建模难题，提出了一种基于深度神经网络的流速感知算法CLANN。该算法不仅便于流速矢量的标定，还能实现多传感器数据融合，从而更准确地预测流速。最后，将所提出的ALL传感器单元集成到水下机器人平台上。在姿态扰动条件下，传感器与惯性测量单元融合，实现了机器人速度矢量的多传感器融合估计。结果表明，测得的速度矢量在大小上的平均绝对误差为0.048 m/s，方向为16.49°，线性系数（$R^2$）为0.896。此外，机器人可在不同运动状态下估计自身轨迹，误差为0.284米。

## Abstract
ABSTRACT When fish swim, a specific ‘water flow field’ forms around their bodies. The lateral line system can provide real-time feedback on flow field variations through the stimulation of hair cells by water currents. Therefore, this paper developed a flexible artificial lateral line (ALL) sensor unit based on the principle of luminous flux that measures flow velocity vector. The sensor employs a dual-layer inverted cup-shaped rocker design. Water flow impacts the rocker, compressing the flexible silicone spring and converting flow velocity changes into variations in luminous flux received by photosensitive units in multiple directions, thereby achieving local flow velocity vector sensing. To address traditional modeling challenges posed by large deformations, nonlinear mechanics, and coupling characteristics in flexible materials, a deep neural network-based flow velocity perception algorithm named CLANN is proposed. This algorithm not only facilitates calibration of flow velocity vectors but also enables multi-sensor data fusion for more accurate flow velocity prediction. Finally, the proposed ALL sensor unit was integrated onto an underwater robotic platform. Under attitude disturbance conditions, the sensor was fused with an inertial measurement unit to achieve multi-sensor fusion estimation of the robot’s velocity vector. Results indicate that the measured velocity vector exhibits a mean absolute error of 0.048 m/s in magnitude and 16.49° in direction, with a linearity coefficient ($R^2$) of 0.896. Furthermore, the robot can estimate its own trajectory under different motion states with an error of 0.284 m.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 鱼类侧线系统能够感知水下流场变化，为游动提供实时反馈，这启发了人工侧线（ALL）传感器的研究。
- 现有水下流速传感器多基于刚性材料，体积大、易受干扰，且难以实现流速矢量的高精度、柔性化感知。
- 本文旨在模仿鱼类侧线，利用光通量原理设计一种柔性人工侧线传感器单元，实现对水下速度矢量（大小和方向）的精准估计，并集成到水下机器人上，与惯性测量单元（IMU）融合，克服传统传感器的局限。

## 二、论文提出的方法论
- **核心思想**：将水流对柔性结构的冲击转化为光通量变化，利用深度学习网路处理柔性材料带来的非线性、大变形和耦合建模难题，实现多传感器融合估计。
- **关键技术细节**：
  - 设计双层倒扣杯形摇杆（双层倒扣杯式摇杆）作为敏感结构，水流冲击摇杆压缩柔性硅胶弹簧，摇杆位移改变多个方向上的光通量，由光敏单元接收。
  - 流速矢量通过多个光敏单元的差异信号解算。
  - 提出CLANN（基于深度神经网络的流速感知算法），用于流速矢量的标定和多传感器数据融合，解决传统力学模型难以描述柔性材料大变形和非线性行为的问题。
  - 将ALL传感器与水下机器人的IMU数据融合，利用CLANN估计机器人的速度矢量，并通过积分估算运动轨迹。
- **算法流程**（文字描述）：多路光信号输入 → 经CLANN网络提取特征并映射到流速矢量 → 与IMU加速度、角速度数据融合 → 输出速度大小、方向及轨迹。

## 三、实验设计
- **数据集/场景**：未明确提及公开数据集；实验场景为水下机器人平台，在姿态扰动条件下进行测试（可能为实验室水池或受控水槽）。
- **Benchmark**：未提及其他对比方法，仅展示了所提出方法的结果（平均绝对误差0.048 m/s和16.49°，线性度0.896，轨迹误差0.284 m）。
- **对比方法**：文献未说明与现有ALL传感器（如基于压电、电容、热线的方案）进行定量比较，仅自我评估。
- **实验场景多样性**：提及“不同运动状态下估计自身轨迹”，推测包含直线、转向等不同运动模式，但细节未披露。

## 四、资源与算力
- **文中未明确说明**使用的GPU型号、数量、训练时长等信息。
- 仅提到CLANN为深度神经网络，但无法推断其规模和计算资源消耗。

## 五、实验数量与充分性
- **实验数量**：未列出具体实验次数（如重复次数、不同流速条件组合数等），仅给出最终统计指标。
- **充分性**：实验覆盖了姿态扰动、不同运动状态，但缺乏对传感器在不同水深、温度、湍流强度、多方向来流等复杂场景下的验证。未进行消融实验（如有/无IMU融合对比），也未与其他人工侧线方法对比，充分性一般。
- **客观与公平**：实验设计基于研究者自建平台，未使用标准化benchmark，可能存在过拟合风险；但指标数值（0.048 m/s, 16.49°）在绝对误差上具有一定参考价值。

## 六、论文的主要结论与发现
- 基于光通量的柔性人工侧线传感器单元可有效感知水下流速矢量。
- CLANN算法能够解决柔性材料建模难题，实现多传感器融合，提升预测精度。
- 在姿态扰动下，与IMU融合后估计的速度矢量平均绝对误差为0.048 m/s（大小）和16.49°（方向），线性相关系数R²=0.896。
- 机器人可在不同运动状态下估计自身轨迹，轨迹误差仅0.284米，证实了该方案用于水下机器人运动估计的潜力。

## 七、优点
- **创新性**：首次将光通量原理引入柔性人工侧线设计，结构简单、无电磁干扰、易于集成。
- **解决难点**：针对柔性材料大变形、非线性力学特性，采用数据驱动的深度学习网络（CLANN）替代传统解析模型，降低了建模难度。
- **多传感器融合**：结合IMU可补偿姿态扰动对流速测量的影响，提高速度矢量估计的鲁棒性。
- **性能指标**：在实际水下机器人平台验证中，获得较低的轨迹误差（0.284 m），表明实用性较强。

## 八、不足与局限
- **实验不充分**：未与已有多种人工侧线方法（如基于压电、热线式等）进行对比，难以评估相对优势。
- **缺失关键细节**：未说明CLANN的网络结构（层数、参数量）、训练数据获取方式（是否仅靠标定数据）、是否针对不同流速范围分别训练等。
- **应用限制**：未讨论传感器在海水腐蚀、高水压、浑浊水质（影响光通路）等真实海洋环境下的可靠性；仅测试了单一集成机器人平台，缺乏多场景泛化验证。
- **偏差风险**：性能指标可能仅在特定实验室条件下成立，未来需在更复杂流场（如涡流、紊流）中检验。

（完）
