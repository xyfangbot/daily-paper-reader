---
title: "Design, analysis, and experimental research on installation robot for hanging column"
title_zh: 悬挂柱安装机器人设计、分析与实验研究
authors: "Xiaoqiang Wang, Xijing Zhu, Xiang Li, Jingyu Yang"
date: 2026-06-09
pdf: "https://www.nature.com/articles/s41598-026-54684-w_reference.pdf"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:huawei"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=huawei; relation_source=lead-affiliation; institutions=Shanxi University, Haier Group (China), China State Shipbuilding (China); query=robot"
tldr: 针对隧道内吊挂柱安装劳动强度大、安全风险高、效率低的问题，提出基于机器人的机械化自动化方案。设计集成操作装备，采用改进D-H法建立运动学模型，提出代数法与遗传算法混合求解逆运动学，并基于七次多项式插值规划时间最优轨迹以抑制冲击。实验表明机器人工作空间覆盖操作范围，方位精度优于10⁻⁶，位置精度优于10×10⁻³，关节运动平滑。该方案验证了可行性，为设备设计与优化提供理论基础。
source: openalex
selection_source: hot_paper_scout
motivation: 解决隧道吊挂柱安装中人工操作劳动强度大、安全风险高、效率低的问题。
method: 设计集成操作装备，基于改进D-H法建模，混合代数法与遗传算法求解逆运动学，采用七次多项式插值规划时间最优轨迹。
result: 工作空间完全覆盖需求，方位精度优于10⁻⁶，位置精度优于10×10⁻³，关节运动平滑无冲击。
conclusion: 设备能高效完成安装任务，验证方案可行性，为设备设计与后续改进提供理论依据。
---

## 摘要
摘要  为解决隧道内悬挂柱安装过程中劳动强度大、安全风险高、作业效率低的问题，提出了一种基于机器人的机械化与自动化解决方案。首先，设计了集成化作业设备，用于完成吊装、夹持、举升和安装。其次，通过改进的D-H参数法建立机器人连杆坐标系，获得正运动学模型并仿真工作空间。为提高逆运动学求解精度，提出了一种代数方法与遗传算法相结合的混合方法，并基于最短路径选取最优逆解。此外，为避免冲击与振动并实现最优效率，提出了基于七次多项式插值的时间最优轨迹。最后，进行了实验验证。结果表明，机器人的工作空间完全覆盖所需作业范围。所提方法精度较高，姿态精度优于10⁻⁶，位置精度优于10×10⁻³。关节运动平稳且无冲击。实验证实了设备高效完成安装任务的能力，验证了所提方案的可行性。研究成果为设备设计提供了理论基础，并为后续改进提供了重要参考。

## Abstract
Abstract To address the challenges of labor-intensive operations, high safety risks, and low operational efficiency in the installation of hanging columns within tunnels, we propose a robotics-based mechanized and automated solution. First, integrated operational equipment is designed to perform hoisting, gripping, lifting, and installation. Next, the robot linkage coordinate system is established via the modified D–H parameter method to obtain a forward kinematic model and simulate the workspace. To improve the accuracy of solving the inverse kinematic solution, a hybrid approach combining algebraic methods and genetic algorithms is proposed, and the optimal inverse solution is selected on the basis of the shortest path. Furthermore, to avoid impact and vibration while achieving optimal efficiency, a time-optimal trajectory based on seventh-degree polynomial interpolation is presented. Finally, experiments validation was conducted. The results show that the robot’s workspace fully covers the required operational range. The proposed method achieves high accuracy, with orientation accuracy better than 10 −6 and position accuracy better than 10 × 10 −3 . The motion of the joint is smooth and shock-free. The experiments confirm the equipment’s capability to efficiently complete installation tasks, verifying the feasibility of the proposed solution. The research results provide a theoretical foundation for equipment design and offer important references for subsequent improvements.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究背景**：高速铁路隧道中悬挂柱（HC）是接触网系统的关键部件，长约4米、重约180公斤，需安装在隧道顶部约9米高处，间距3米（每公里超过300个）。传统人工安装依赖脚手架和梯车，工人需手动将HC举升至隧道顶部并爬高固定，劳动强度大、安全风险高、效率低（约1小时完成一个）。
- **核心问题**：当前缺乏机械化和自动化手段来解决隧道有限空间内的HC安装难题，亟需一种能替代人工作业、提升效率与安全性的机器人方案。
- **研究目标**：设计并验证一套集成化作业设备，以机器人为主体实现HC的抓取、举升、运输和安装全过程自动化，消除人工干预，提供理论依据和实验支持。

## 二、论文提出的方法论
- **整体方案**：设计集成操作装备，包括底盘车、起重机、安装机器人、高空作业平台、动力系统等。安装机器人本身由旋转基座、小俯仰臂、大俯仰臂、三级伸缩臂、角度调整机构、末端摆动机构、末端微调机构、末端执行器和视觉系统组成。末端执行器包含铰链夹紧机构、对准调整机构和螺栓拧紧组件。
- **正运动学建模**：采用改进D-H参数法建立连杆坐标系，推导相邻连杆变换矩阵，最终得到末端执行器相对于基座的齐次变换矩阵。在MATLAB Robotics Toolbox中建立仿真模型验证解析模型的正确性。
- **工作空间分析**：使用蒙特卡罗方法随机采样300,000组关节变量，绘制可达工作空间点云，并与需求工作范围对比。结果显示初始工作空间超出需求，通过迭代优化将棱柱关节J4行程从(2900,8100)优化为(2900,7600)，减少行程6.17%仍满足要求。
- **逆运动学求解（AGA混合方法）**：
  - 先进行代数分析，直接从运动学方程解析部分变量（如θ₁、θ₆和θ₂+θ₃+θ₅的和），将未知变量从6个减至4个，缩小搜索空间。
  - 采用遗传算法框架：初始种群大小N=20000，个体在各自范围内随机初始化。适应度函数结合姿态误差和位置误差（权重β=0.3）。使用轮盘赌选择、单点交叉（交叉率0.9）和变异（变异率0.03）。
  - 运行200次迭代，输出最优关节变量。多次运行取最短路径解。
- **轨迹规划**：针对从抓取位姿到安装位姿的运输阶段，提出时间最优轨迹规划方法。
  - 采用七次多项式插值，边界条件约束位置、速度、加速度和跃度均为零（初末状态）。
  - 算法通过逐步增加运动时间t，检查最大速度和最大加速度是否达到物理极限，收敛时输出最小可行时间。
  - 对比五阶多项式插值：七阶多项式能确保跃度连续且初末为零，有效抑制冲击和振动。

## 三、实验设计
- **实验场景**：在专用室内设施中搭建模拟隧道环境。使用金属板加工两条平行槽道模拟隧道顶部的安装槽，固定在8米高度处。
- **实验内容**：
  1. **末端执行器和机械臂单部件测试**：称重（总重222.5kg，满足≤250kg要求），运动测试（液压站驱动下执行抓取和夹紧动作）。
  2. **整机安装机器人功能测试**：验证抓取HC并运输至安装位置的能力。
  3. **操作效率测试**：记录完整工作流程各步骤耗时，与人工安装对比。
  4. **稳定性和精度测试**：以目标安装位置为原点建立笛卡尔坐标系，测量HC末端执行器在三个方向（Rx、Ry、Rz）的角度偏差。进行4组独立测试（每组多次测量），统计最小值、最大值、极差、均值、中位数、标准差，并计算95%置信区间与工程公差（|Rx|≤0.15°，|Ry|≤0.15°，|Rz|≤0.15°）进行比较。
- **基准/对比方法**：
  - 逆运动学：对比传统遗传算法（GA）与所提AGA混合方法。
  - 轨迹规划：对比五阶多项式插值与七阶多项式插值。
  - 效率：对比人工安装（约1小时）。

## 四、资源与算力
- 论文未明确提及使用的GPU型号、数量或训练时长。所有仿真和计算均基于MATLAB实现（使用Robotics Toolbox和自定义遗传算法代码），算力需求较低，未涉及深度学习训练。

## 五、实验数量与充分性
- **实验数量**：
  - 逆运动学仿真：AGA运行4次获得4组解，GA运行4次获得4组解。
  - 轨迹规划仿真：分别对五阶和七阶多项式进行单一轨迹计算。
  - 物理实验：对末端执行器和机械臂各进行运动功能测试；效率测试一次完整流程；精度测试进行了4组独立试验（G1-G4），每组记录多次测量数据。
- **充分性评估**：
  - 逆运动学对比充分，显示了AGA的显著精度提升。
  - 轨迹规划对比合理，解释了为何选择七阶多项式。
  - 物理实验方面：效率测试仅一次，代表性有限但可估算；精度测试4组虽能体现一定离散性，但样本量偏小，且缺乏重复性验证（如多次重复同一配置）。此外，仅测试了单个目标安装点，未覆盖不同位置、不同HC重量等工况。实验整体设计基本客观，但充分性有待加强。

## 六、论文的主要结论与发现
1. **设计可行**：集成操作装备成功实现抓取、举升和安装的机械化与自动化，替代传统人工方法。
2. **工作空间满足需求**：仿真显示机器人工作空间完全覆盖操作范围，优化后J4行程减少6.17%仍满足要求。
3. **逆运动学精度高**：AGA方法求解精度显著优于传统GA，姿态误差小于10⁻⁶，位置误差小于10×10⁻³，满足工程要求。
4. **轨迹平滑无冲击**：七次多项式插值使速度、加速度、跃度连续且初末为零，有效抑制振动，同时达到时间最优。
5. **效率提升**：自动化流程约22分50秒，相较于人工安装（约1小时）效率提升约1.7倍。
6. **精度达标**：4组实验中G2在三方向均满足|R|≤0.15°公差，且均值更接近零。Rz方向精度和稳定性明显优于Rx和Ry，后者是未来优化的关键方向。

## 七、优点
- **问题洞察准确**：紧扣隧道内HC安装的实际痛点，方案针对性强。
- **方法系统完整**：从机构设计、运动学建模、逆解算法优化到轨迹规划、实验验证形成完整闭环。
- **技术创新**：AGA混合方法结合代数解析与智能优化，显著提升逆解精度；七次多项式轨迹规划在时间最优与冲击抑制间取得平衡。
- **理论结合实践**：仿真分析指导设计优化（如J4行程缩减），物理实验验证可行性，结论可靠。
- **表述清晰规范**：对D-H参数、变换矩阵、算法流程、实验数据的记录和分析详实。

## 八、不足与局限
- **实验样本量小**：精度测试仅4组，每组测量次数未说明，统计稳定性可能不足；效率测试仅一次。
- **工况覆盖有限**：仅测试了单个目标安装位置，未验证不同HC重量、不同隧道曲率、不同初始位姿下的表现。
- **缺乏动态性能测试**：未测量实际运动中的振动、加速度、关节扭矩等，仅依赖仿真轨迹分析。
- **缺少对比基线**：效率提升对比仅给出人工时长估计（约1小时），未提供实际人工测试数据或文献参考。
- **工程应用限制**：论文未讨论环境条件（如粉尘、温度）、长期可靠性、维护性等实际部署问题。
- **资源算力未提及**：未说明仿真和算法运行的硬件环境，影响复现性。
- **视觉系统细节缺失**：论文提及视觉系统用于定位，但未给出视觉算法、精度或与机器人协同的控制策略。

（完）
