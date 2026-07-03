---
title: "Design, analysis, and experimental research on installation robot for hanging column"
title_zh: 挂柱安装机器人的设计、分析与实验研究
authors: "Xiaoqiang Wang, Xijing Zhu, Xiang Li, Jingyu Yang"
date: 2026-06-09
pdf: "https://www.nature.com/articles/s41598-026-54684-w_reference.pdf"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:huawei"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=huawei; relation_source=lead-affiliation; institutions=Shanxi University, Haier Group (China), China State Shipbuilding (China); query=robot"
tldr: 针对隧道内悬柱安装劳动强度大、安全风险高、效率低的问题，本文设计了集成起吊、抓取、升降与安装功能的机器人。采用改进D-H法建立运动学模型并仿真工作空间，通过代数法与遗传算法混合求解逆运动学，并规划七次多项式时间最优轨迹。实验表明，工作空间覆盖需求，定向精度优于10⁻⁶，位置精度优于10×10⁻³，关节运动平稳无冲击，高效完成任务。研究成果为隧道悬柱安装机器人的装备设计与优化提供了理论基础和工程参考。
source: openalex
selection_source: hot_paper_scout
motivation: 解决隧道内悬柱安装中人工操作强度大、安全风险高、效率低的难题，实现机械化与自动化。
method: 设计集成起吊、抓取、升降、安装的机器人；利用改进D-H法建模；代数法与遗传算法混合求解逆运动学；规划七次多项式时间最优轨迹。
result: 机器人工作空间覆盖所需范围；定向精度优于10⁻⁶，位置精度优于10×10⁻³；关节运动平滑无冲击，高效完成安装任务。
conclusion: 验证了机器人方案的可行性与有效性，为隧道悬柱安装装备设计提供了理论依据和工程参考。
---

## 摘要
摘要 针对隧道内挂柱安装过程中劳动强度大、安全风险高、作业效率低的问题，提出了一种基于机器人的机械化与自动化解决方案。首先，设计了集成的作业设备，用于完成吊装、夹持、升降和安装。然后，通过修正D-H参数法建立机器人连杆坐标系，获得正运动学模型并模拟工作空间。为了提高逆运动学求解的精度，提出了一种代数方法与遗传算法相结合的混合方法，并根据最短路径选择最优逆解。此外，为避免冲击和振动并实现最佳效率，提出了基于七次多项式插值的时间最优轨迹。最后，进行了实验验证。结果表明，机器人的工作空间完全覆盖所需的作业范围。所提出方法具有高精度，定向精度优于10^-6，位置精度优于10×10^-3。关节运动平滑且无冲击。实验证实了设备能够高效完成安装任务，验证了所提出方案的可行性。研究结果为设备设计提供了理论基础，并为后续改进提供了重要参考。

## Abstract
Abstract To address the challenges of labor-intensive operations, high safety risks, and low operational efficiency in the installation of hanging columns within tunnels, we propose a robotics-based mechanized and automated solution. First, integrated operational equipment is designed to perform hoisting, gripping, lifting, and installation. Next, the robot linkage coordinate system is established via the modified D–H parameter method to obtain a forward kinematic model and simulate the workspace. To improve the accuracy of solving the inverse kinematic solution, a hybrid approach combining algebraic methods and genetic algorithms is proposed, and the optimal inverse solution is selected on the basis of the shortest path. Furthermore, to avoid impact and vibration while achieving optimal efficiency, a time-optimal trajectory based on seventh-degree polynomial interpolation is presented. Finally, experiments validation was conducted. The results show that the robot’s workspace fully covers the required operational range. The proposed method achieves high accuracy, with orientation accuracy better than 10 −6 and position accuracy better than 10 × 10 −3 . The motion of the joint is smooth and shock-free. The experiments confirm the equipment’s capability to efficiently complete installation tasks, verifying the feasibility of the proposed solution. The research results provide a theoretical foundation for equipment design and offer important references for subsequent improvements.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 高速铁路隧道内悬挂柱（HC）是接触网的关键部件，长约4 m、重约180 kg，需安装于隧道顶部约9 m高处，每3 m一个，每公里需安装超过300个。
- 传统安装依赖脚手架和梯车，工人需手动攀高固定，存在劳动强度大、安全风险高、效率低（约需1小时）等问题，难以满足现代高铁建设需求。
- 本文研究动机：利用机器人技术实现机械化与自动化安装，以提升效率、保障安全、减轻人力负担。

## 二、论文提出的方法论
- **核心思想**：设计一套集成吊装、抓取、提升、安装功能的作业设备，以安装机器人为主体，辅以底盘车、起重机、空中作业平台、动力系统等，实现全流程自动化。
- **技术细节**：
  - **机械结构**：安装机器人包含回转底座、小俯仰臂、大俯仰臂、三级伸缩臂、角度调节机构、末端摆动机构、末端微调机构、末端执行器（含铰链夹爪、对准调节机构、紧固组件）及视觉系统。
  - **运动学建模**：采用修正D‑H参数法建立连杆坐标系，推导正运动学齐次变换矩阵；利用蒙特卡洛法仿真工作空间，验证覆盖作业范围。
  - **逆运动学求解**：提出代数法与遗传算法混合（AGA）方法。先通过代数法化简耦合变量，再用GA在缩减的搜索空间中优化，以最短路径原则选择最优解，提升精度。
  - **轨迹规划**：引入七次多项式插值，在关节空间内规划时间最优轨迹，约束速度、加速度、加加速度（jerk）连续且起止为零，避免冲击振动，同时最小化运动时间。
  - **算法流程**：给定目标位姿矩阵 → 代数分析简化未知数 → 初始化种群 → 适应度函数计算（加权位姿误差） → 轮盘赌选择、单点交叉、变异 → 迭代至收敛。

## 三、实验设计
- **实验场景与数据集**：在室内专用场地搭建模拟隧道环境，用金属板加工两条平行沟槽模拟隧道顶部安装槽，固定于8 m高度。
- **基准与对比方法**：
  - 逆运动学：与标准遗传算法（GA）对比，AGA在方向精度（优于10⁻⁶ vs 10⁻²）和位置精度（优于10×10⁻³）上显著提升。
  - 轨迹规划：对比五次多项式插值和七次多项式插值，七次多项式能实现jerk起止为零，更有效抑制振动，尽管运动时间略长，但综合性能更优。
- **实验内容**：
  - 末端执行器重量验证（要求≤250 kg，实测222.5 kg）及夹持、旋转动作测试。
  - 机械臂关节范围测试。
  - 整机抓取、提升、安装流程测试。
  - 效率测试：记录完整流程时间，约22分50秒，比人工（约1小时）提升约1.7倍。
  - 稳定性与精度测试：在目标安装位置建立坐标系，测量HC姿态偏差角Rx、Ry、Rz，进行4组独立重复试验（每组多次测量），统计均值、标准差、95%置信区间与工程容差范围[−0.15°，0.15°]的比较。

## 四、资源与算力
- 论文中未提及所使用的GPU型号、数量、训练时长等算力资源。仿真与算法运行主要基于MATLAB软件（Robotics Toolbox、遗传算法工具箱），未使用大规模深度学习或专用加速硬件。

## 五、实验数量与充分性
- **实验组数**：包含末端执行器重量与动作测试、机械臂范围测试、整机流程测试、效率测试（1次完整流程计时）、稳定性精度测试（4组独立重复试验，每组多次测量）。共约10余项子实验。
- **充分性评价**：实验覆盖了核心功能验证、精度量化、效率对比和稳定性评估，设计较为全面。但部分实验未报告重复次数细节（如效率测试仅给出单次时间），稳定性测试仅4组，样本量偏小，结论的统计可靠性有限。总体而言，实验设计基本满足工程验证需求，但在统计严谨性上可进一步强化。

## 六、论文的主要结论与发现
- 所设计的一体化作业设备能够有效完成抓取、提升、安装任务，解决传统方法劳动强度大、风险高、效率低的问题，为隧道内HC安装提供可靠机械方案。
- 基于MD‑H参数的正运动学模型准确可靠，工作空间仿真完全覆盖作业范围，且可通过优化伸缩臂行程减少6.17%的行程。
- AGA混合方法显著提升逆解精度，方向误差<10⁻⁶、位置误差<10×10⁻³，满足工程需求。
- 七次多项式时间最优轨迹规划实现速度、加速度、jerk连续且起止为零，有效抑制冲击振动，同时保证运动效率。
- 实验证明机器人操作方案可行，设备可在约23分钟内完成安装，精度测试中G2组（Rx=0.0521°, Ry=-0.0211°, Rz=0.0079°）均满足容差，综合性能最优；Rz方向精度与稳定性优于Rx、Ry方向。

## 七、优点
- **方法创新**：代数法与遗传算法混合求解逆运动学，有效缩小搜索空间、提升精度；七次多项式轨迹同时满足运动平滑与时间最优。
- **工程应用性强**：从需求分析、结构设计、理论建模到实验验证形成完整闭环，所提方案可直接指导装备制造。
- **实验设计较全面**：涵盖功能验证、精度量化、稳定性分析、效率对比，实验结果支撑主要结论。
- **优化细节**：通过工作空间分析优化伸缩臂行程，降低机械复杂度。

## 八、不足与局限
- **实验样本量有限**：稳定性精度测试仅4组独立试验，每组的测量次数未明确，统计结论的置信度有待提高。
- **效率测试缺乏重复性验证**：仅报告单次流程时间，未给出多次测试均值或方差，难以评估操作一致性。
- **未说明视觉系统具体性能**：视觉引导精度未量化，对整体定位精度的影响未分析。
- **缺乏真实隧道环境验证**：实验在室内模拟环境中进行，未考虑实际隧道内的粉尘、照明、温差等干扰因素。
- **未与其他逆解算法（如几何法、迭代法）进行系统对比**：仅与标准GA对比，对比基准不够丰富。
- **算力资源未提及**：无法评估算法在高频率实时控制场景下的计算可行性。

（完）
