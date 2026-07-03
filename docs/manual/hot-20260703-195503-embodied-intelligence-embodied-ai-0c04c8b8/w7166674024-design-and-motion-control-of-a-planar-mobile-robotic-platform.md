---
title: Design and motion control of a planar mobile robotic platform
title_zh: 平面移动机器人平台的设计与运动控制
authors: "Mingyang Huang, 陈康法"
date: 2026-06-30
pdf: "https://doi.org/10.1177/09544070261462614"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:beijing academy of artificial intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=beijing academy of artificial intelligence; relation_source=lead-affiliation; institutions=Beijing Academy of Artificial Intelligence, Ministry of Education, University of Science and Technology Beijing; query=robot"
tldr: 针对平面移动机器人平台运动精度与稳定性瓶颈，提出四轮差速底盘集成控制方案。采用轮式里程计为主定位源，扩展卡尔曼滤波融合多传感器抑制滑移漂移。规划层引入准均匀B样条生成曲率连续且避障的平滑轨迹，执行层梯形速度剖面限制加速度。实时跟踪控制器将轨迹转化为轮速指令，实验室环境下实现毫米级路径跟踪精度（RMSE 4.97 mm），并分析系统在大范围复杂环境中的可扩展性。
source: openalex
selection_source: hot_paper_scout
motivation: 克服轮式平台因滑移与速度波动导致的位姿漂移，提升低速运动控制精度与稳定性。
method: 融合EKF多源定位、准均匀B样条避障轨迹规划及梯形速度剖面约束，设计实时跟踪控制器输出轮速指令。
result: 室内受限环境下路径跟踪RMSE达4.97 mm，实现稳定定位与平滑跟踪。
conclusion: 该框架为服务机器人与AGV在可扩展场景中提供了可靠的航位推算与运动控制基础。
---

## 摘要
本文针对平面移动机器人平台的运动精度与稳定性瓶颈，提出了一种四轮差速底盘集成控制方案。以轮式里程计为主要定位源，同时利用扩展卡尔曼滤波器融合多源传感器测量数据，抑制由车轮打滑和速度波动引起的位姿漂移。在规划层，引入准均匀B样条轨迹生成平滑且曲率连续的参考路径，同时满足避障约束。在执行层，采用梯形速度曲线施加加速度限制，使底盘能够平稳启动、加速和减速。实时跟踪控制器将规划轨迹转化为轮速指令，在受限实验环境下实现了毫米级（均方根误差4.97 mm）路径跟踪精度。此外，还分析了系统在更大工作区域和高度复杂环境中的可扩展性。实验表明，所提框架可在室内环境下实现稳定的定位、平滑跟踪和实用的避障能力，为可扩展的服务机器人和自动导引车提供了可靠的运动控制与航迹推算基础。

## Abstract
This paper addresses the motion-accuracy and stability bottlenecks of planar mobile robot platforms and presents an integrated control scheme for a four-wheel differential-drive chassis. Wheel odometry is used as the primary localization source, while an EKF fuses multi-source sensor measurements to suppress pose drift caused by wheel slip and speed fluctuations. At the planning level, quasi-uniform B-spline trajectories are introduced to generate smooth, curvature-continuous reference paths that also satisfy obstacle-avoidance constraints. At the execution level, a trapezoidal velocity profile imposes acceleration limits so that the chassis can start, accelerate, and decelerate smoothly. A real-time tracking controller then converts the planned trajectory into wheel-speed commands, achieving millimeter-level (RMSE of 4.97 mm) path-tracking accuracy in a constrained laboratory environment. Furthermore, an analysis of the system’s scalability in larger operational areas and highly complex environments is presented. Experiments show that the proposed framework delivers stable localization, smooth tracking, and practical obstacle-avoidance capability in indoor environments, providing a reliable motion-control and dead-reckoning basis for scalable service robots and AGVs.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：平面移动机器人平台（特别是四轮差速底盘）在运动过程中因车轮打滑和速度波动导致位姿漂移，限制了运动精度与稳定性。
- **研究动机**：克服轮式平台的航位推算误差，提升低速运动控制的毫米级跟踪精度与抗干扰能力。
- **整体含义**：为服务机器人和自动导引车（AGV）提供一套兼具定位、轨迹规划与实时跟踪的集成控制方案，在受限室内环境中实现稳定运动，并探讨向更大、更复杂场景的可扩展性。

## 二、论文提出的方法论
- **核心思想**：以轮式里程计为主定位源，扩展卡尔曼滤波（EKF）融合多源传感器（如IMU、编码器等）抑制滑移引起的漂移；规划层使用准均匀B样条生成曲率连续且避障的参考轨迹；执行层采用梯形速度曲线限制加速度；实时跟踪控制器将轨迹转化为轮速指令，实现闭环控制。
- **关键技术细节**：
  - **定位**：EKF将里程计预测与传感器观测融合，修正位置与航向角。
  - **轨迹规划**：准均匀B样条保证路径连续性与局部可控性，同时满足避障约束（如障碍物膨胀）。
  - **速度规划**：梯形速度剖面实现平滑启停，避免加速度突变。
  - **跟踪控制**：基于当前位姿误差，计算期望轮速并输出给电机驱动器。
- **算法流程**（文字说明）：
  1. 初始化：设置底盘参数、传感器标定。
  2. 定位：EKF接收编码器（里程计）和IMU数据，输出最优位姿估计。
  3. 规划：根据目标点与障碍物信息，生成准均匀B样条路径，并附上梯形速度曲线。
  4. 跟踪：实时比较规划位姿与估计位姿，计算前向速度和转向角，转换为左右轮速。
  5. 执行：发送轮速指令，并循环更新。

## 三、实验设计
- **实验场景**：在室内受限实验室环境（地面平整、无障碍物或有可避障的简单障碍）中进行路径跟踪实验。
- **数据集 / 基准**：未使用公开数据集，自建实验室环境；未明确说明 benchmark 或对比方法。
- **对比方法**：论文未提及与其他方法（如纯里程计、PID、MPC等）进行定量对比，仅展示了所提框架自身的跟踪误差。

## 四、资源与算力
- **文中未明确说明**使用的GPU型号、数量、训练时长等算力信息。仅提到实时跟踪控制器，推测为嵌入式系统（如STM32或工控机），但未给出具体硬件参数。

## 五、实验数量与充分性
- **实验数量**：论文仅报告了单次（或一组）具体实验的结果——路径跟踪均方根误差（RMSE）为4.97 mm。未提及多组重复实验、不同场景（如不同速度、不同曲率路径、不同地面材质）的对比，也未进行消融实验（如是否使用EKF、是否使用B样条规划）。
- **充分性评价**：实验不够充分，缺乏统计显著性分析和泛化性验证。仅在一个理想化实验室条件下测试，无法全面评估系统在真实复杂环境中的性能。结论的客观性和公平性有待更多实验支撑。

## 六、论文的主要结论与发现
- 所提出的基于EKF融合定位、准均匀B样条轨迹规划与梯形速度约束的集成控制框架，在室内实验室环境下实现了毫米级（RMSE 4.97 mm）路径跟踪精度。
- 系统能够保持稳定的定位、平滑的跟踪和实用的避障能力。
- 分析认为该框架可通过增加传感器（如激光雷达、视觉）和优化规划算法，向更大工作区域和更复杂环境扩展，为服务机器人和AGV提供可靠的运动控制与航迹推算基础。

## 七、优点
- **方法集成性好**：将定位、规划、速度平滑和跟踪控制有机结合，形成一个完整闭环。
- **注重工程实用性**：采用梯形速度剖面限制加速度，避免底盘冲击，适合实际应用。
- **精度突出**：在受限环境下达到毫米级跟踪误差，满足精密作业要求。
- **可扩展性分析**：讨论了向大场景、高复杂度环境的扩展方向，有前瞻性。

## 八、不足与局限
- **实验设计单薄**：仅报告一组室内实验，缺乏与现有方法（如纯位姿PID、模型预测控制等）的定量对比，也缺少在不同条件下的消融研究。
- **未评估鲁棒性**：未在滑移较严重（如光滑地面、快速加减速）的场景下测试，且未量化EKF抑制漂移的实际效果。
- **硬件与算力信息缺失**：无法评估方法的实时性、资源消耗等工程限制。
- **应用限制**：主要针对低速、小范围室内环境，在高速、大规模、动态障碍物场景下的性能未知。
- **传感器依赖**：轮式里程计在严重打滑时可能失效，论文未讨论异常退化情况下的应对策略。

（完）
