---
title: Design and motion control of a planar mobile robotic platform
title_zh: 平面移动机器人平台的设计与运动控制
authors: "Mingyang Huang, 陈康法"
date: 2026-06-30
pdf: "https://doi.org/10.1177/09544070261462614"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:beijing academy of artificial intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=beijing academy of artificial intelligence; relation_source=lead-affiliation; institutions=Beijing Academy of Artificial Intelligence, Ministry of Education, University of Science and Technology Beijing; query=robot"
tldr: 平面移动机器人平台存在运动精度与稳定性瓶颈，尤其是轮式滑动和速度波动引起的位姿漂移。针对四轮差速底盘，提出集成控制方案：以轮式里程计为主定位源，扩展卡尔曼滤波融合多源传感器抑制漂移；规划层采用准均匀B样条生成曲率连续平滑轨迹，满足避障约束；执行层使用梯形速度曲线限制加速度，实时跟踪控制器输出轮速指令。实验室环境路径跟踪均方根误差为4.97毫米，实现毫米级精度。进一步分析了大工作区域和复杂环境下的可扩展性。该框架为服务机器人和自动导引车提供稳定定位、平滑跟踪与可靠航位推算基础。
source: openalex
selection_source: hot_paper_scout
motivation: 解决平面移动机器人平台运动精度和稳定性瓶颈，抑制轮滑和速度波动导致的位姿漂移。
method: 提出四轮差速底盘集成控制方案：EKF多源融合定位、准均匀B样条轨迹规划、梯形速度曲线与实时跟踪控制器。
result: 实验室环境路径跟踪均方根误差4.97毫米，验证了毫米级精度与系统可扩展性。
conclusion: 该框架实现稳定定位、平滑跟踪与避障，为服务机器人和AGV提供可靠运动控制基础。
---

## 摘要
本文针对平面移动机器人平台的运动精度与稳定性瓶颈，提出了一种四轮差速驱动底盘的一体化控制方案。以轮式里程计作为主要定位源，并利用扩展卡尔曼滤波器融合多源传感器测量值，抑制由车轮打滑和速度波动引起的位姿漂移。在规划层面，引入准均匀B样条轨迹生成光滑、曲率连续的参考路径，同时满足避障约束。在执行层面，采用梯形速度曲线施加加速度限制，使底盘能够平稳启动、加速和减速。实时跟踪控制器将规划轨迹转化为轮速指令，在受限实验室环境中实现了毫米级（均方根误差4.97 mm）路径跟踪精度。此外，分析了系统在更大作业区域和高度复杂环境中的可扩展性。实验表明，所提框架在室内环境中实现了稳定的定位、平滑的跟踪以及实用的避障能力，为可扩展的服务机器人和自动导引车提供了可靠的运动控制与航位推算基础。

## Abstract
This paper addresses the motion-accuracy and stability bottlenecks of planar mobile robot platforms and presents an integrated control scheme for a four-wheel differential-drive chassis. Wheel odometry is used as the primary localization source, while an EKF fuses multi-source sensor measurements to suppress pose drift caused by wheel slip and speed fluctuations. At the planning level, quasi-uniform B-spline trajectories are introduced to generate smooth, curvature-continuous reference paths that also satisfy obstacle-avoidance constraints. At the execution level, a trapezoidal velocity profile imposes acceleration limits so that the chassis can start, accelerate, and decelerate smoothly. A real-time tracking controller then converts the planned trajectory into wheel-speed commands, achieving millimeter-level (RMSE of 4.97 mm) path-tracking accuracy in a constrained laboratory environment. Furthermore, an analysis of the system’s scalability in larger operational areas and highly complex environments is presented. Experiments show that the proposed framework delivers stable localization, smooth tracking, and practical obstacle-avoidance capability in indoor environments, providing a reliable motion-control and dead-reckoning basis for scalable service robots and AGVs.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 平面移动机器人平台（如服务机器人、自动导引车AGV）在实际运行中面临运动精度与稳定性瓶颈，主要问题包括：车轮打滑和速度波动引起的位姿漂移，导致路径跟踪误差累积，影响航位推算可靠性。
- 现有方案往往在定位、轨迹规划、运动控制三个层面独立设计，缺乏集成化、系统性的控制框架，难以同时满足高精度、平滑性和避障需求。
- 本文旨在提出一套针对四轮差速驱动底盘的一体化控制方案，实现毫米级路径跟踪精度，并为可扩展的室内移动机器人提供稳定的运动控制基础。

## 二、论文提出的方法论
- **核心思想**：以轮式里程计为主定位源，通过扩展卡尔曼滤波器（EKF）融合多源传感器测量值（如惯性测量单元、激光雷达等），抑制漂移；规划层生成曲率连续的光滑轨迹；执行层施加加速度限制并实时跟踪。
- **关键技术细节**：
  1. **定位与状态估计**：轮式里程计提供高频但易漂移的位姿估计，EKF融合其他传感器（如IMU、激光雷达）的观测，在线修正由于打滑和速度波动引起的误差。
  2. **轨迹规划**：采用准均匀B样条（quasi-uniform B-spline）生成参考路径，保证曲率连续，同时满足避障约束（障碍物表示为空间禁止区域）。
  3. **速度规划**：梯形速度曲线（trapezoidal velocity profile）对加速度和减速度施加限制，实现底盘平稳启动、加速和减速，避免急动。
  4. **实时跟踪控制**：设计跟踪控制器，将规划的参考轨迹转换为左右轮速指令，通过差速驱动实现路径跟踪。
- **算法流程说明**：传感器数据输入→EKF状态估计→全局路径规划（B样条）→局部速度规划（梯形曲线）→跟踪控制器→轮速指令输出→电机执行。

## 三、实验设计
- **实验场景**：受限的室内实验室环境，未详细说明具体尺寸或障碍物布置；后续分析扩展到更大工作区域和复杂环境。
- **数据集**：未使用公开数据集，实验基于自建场景（可能是特定室内布局）进行。
- **基准对比**：文中未提及与其他方法的定量对比，仅报告了本框架的路径跟踪误差。
- **评价指标**：路径跟踪均方根误差（RMSE），结果为4.97 mm（毫米级）。

## 四、资源与算力
- 论文未明确说明使用的GPU型号、数量、训练时长等计算资源信息。推测整个系统主要依赖嵌入式控制器（如微控制器或工控机）进行实时控制，未涉及深度学习训练，因此未提及算力需求。

## 五、实验数量与充分性
- **实验组数**：仅提及一组实验结果（实验室环境路径跟踪RMSE 4.97 mm），未报告多场景重复实验或不同参数下的对比实验。
- **充分性与客观性**：实验覆盖较为单一，缺乏在复杂环境（如多变光照、大面积打滑地面、动态障碍物）下的验证；没有与现有方法（如纯跟踪算法、模型预测控制等）的横向比较；未进行消融实验（如去除EKF或去除B样条规划）来量化各模块贡献。因此实验充分性不足，结论的外部有效性有限。

## 六、论文的主要结论与发现
- 所提出的集成控制框架在室内实验室环境中实现了毫米级路径跟踪精度（RMSE 4.97 mm），验证了稳定定位、平滑跟踪和避障能力。
- 系统具有良好的可扩展性，可以适应更大工作区域和更复杂环境（定性分析，未提供定量数据）。
- 该框架为服务机器人和自动导引车提供了可靠的运动控制和航位推算基础。

## 七、优点
- 方法集成度高：将EKF多源融合定位、B样条平滑轨迹规划、梯形速度控制和实时跟踪控制器有机结合，形成端到端控制流程。
- 实用性突出：针对轮式滑移和速度波动等工程常见问题提出了具体解决方案，结果达到毫米级精度，对实际应用有参考价值。
- 轨迹平滑性：采用准均匀B样条保证轨迹曲率连续，有利于底盘平稳运行和跟踪性能。
- 可扩展性分析：在讨论部分考虑了更大区域和复杂环境，体现了系统设计的通用性。

## 八、不足与局限
- 实验验证不充分：仅报告一组实验室环境结果，缺乏多场景（如不同地面摩擦、障碍物密度、运行速度）的统计实验，难以证明方法的鲁棒性。
- 缺乏基准对比：未与现有成熟方法（如PID+纯跟踪、模型预测控制等）进行定量比较，无法判断本方案的相对优劣。
- 未进行消融实验：没有分离验证EKF、B样条、梯形速度曲线三个核心模块的独立贡献，无法明确性能提升来源。
- 资源消耗与实时性分析缺失：未给出控制器计算频率、延迟等关键实时性指标，在资源受限嵌入式平台上部署可行性未知。
- 公开复现性差：未提供代码或详细参数，数据集也未公开，其他研究者难以复现结果。

（完）
