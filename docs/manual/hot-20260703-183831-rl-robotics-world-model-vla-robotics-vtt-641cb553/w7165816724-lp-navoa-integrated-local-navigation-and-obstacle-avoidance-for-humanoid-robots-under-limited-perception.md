---
title: "LP-NavOA: Integrated Local Navigation and Obstacle Avoidance for Humanoid Robots under Limited Perception"
title_zh: LP-NavOA：有限感知下仿人机器人的集成局部导航与避障
authors: "Yi Luo, J T, Yuyao Min, Jinzhe Li, Kaihong Huang, P P Li"
date: 2026-06-22
pdf: "https://arxiv.org/pdf/2606.23249"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: "仿人机器人在杂乱环境中局部导航需要同时处理避障、稀疏目标恢复和稳定运动，但现有方法在部分可观测短距离感知下存在延迟或丢失目标。LP-NavOA通过射线投射感知-动作PPO训练运动骨干并冻结，再利用A*教师蒸馏出循环局部规划器，运行时仅调整航向命令，无需全局地图。在MuJoCo中，准时到达率从38-40%提升至85-97%，接触减少。该框架实现硬件可执行，无需持续摇杆操控。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有方法在部分可观测短距离感知下，要么因延迟导致避障与目标追踪不匹配，要么反应式控制器在障碍物遮挡后丢失目标。
method: "首先训练基于射线投射的PPO运动骨干，使用圆形命令和安全滤波器；冻结后，利用A*教师生成轨迹蒸馏循环局部规划器，部署时仅覆盖航向命令。"
result: "在MuJoCo中，蒸馏规划器将准时到达率从38-40%提升至85-97%，减少碰撞；消融验证了动态路由和教师数据采集的重要性。"
conclusion: LP-NavOA实现了无需全局地图和外部规划器的仿人机器人导航，在有限感知下兼顾避障与目标恢复，且可在硬件上执行。
---

## 摘要
在杂乱环境中，仿人机器人的局部导航必须同时解决避障、稀疏目标恢复以及短距离、部分可观测传感条件下的稳定全身运动。显式的规划器-控制器分解会引入延迟，并可能与仿人机器人敏捷的运动指令跟踪极限不匹配，而纯反应式控制器在障碍物遮挡后可能丢失目标。我们提出了LP-NavOA，一个面向仿人机器人的有限感知导航与避障框架。首先，以射线投射条件化的感知-动作近端策略优化（PPO）运动骨干网络为基础，结合以机器人为中心的圆形航向-速度指令和共享的指令侧安全滤波器进行训练。冻结该骨干网络后，利用A*和路径点教师生成轨迹，通过蒸馏得到一个循环局部规划器，该规划器在部署时仅覆盖航向指令，而保持全身策略不变。运行时，LP-NavOA利用本体感知、短距离局部测距以及机体坐标系下的目标方向，无需全局地图、路径点流或外部规划器。在MuJoCo开放式墙壁和室内布局中，蒸馏后的规划器实现了障碍物绕行和避障后的目标恢复，将教师校准的准时到达率从38–40%提升至85–97%，并减少了相对于仅骨干网络控制器的碰撞/接触密集进度。消融实验表明，动态路径塑造、教师主动数据采集以及圆形指令接口对于导航效率以及训练3.0米/秒的骨干网络至关重要。宇树G1部署分析展示了无需持续摇杆操控的硬件可执行性。

## Abstract
Humanoid local navigation in cluttered environments must jointly resolve obstacle avoidance, sparse-goal recovery, and stable whole-body locomotion under short-range and partially observable sensing. Explicit planner-control decompositions introduce latency and can mismatch agile humanoid command-tracking limits, while purely reactive controllers may lose the goal after obstacle occlusion. We present LP-NavOA, a limited-perception navigation and obstacle-avoidance framework for humanoid robots. A raycast-conditioned perception-action proximal policy optimization (PPO) locomotion backbone is first trained with a robot-centered circular heading-speed command and a shared command-side safety filter. With this backbone frozen, A-star and waypoint teachers generate rollouts for distilling a recurrent local planner that overwrites only the heading command at deployment, leaving the whole-body policy intact. At runtime, LP-NavOA uses proprioception, short-range local range sensing, and a body-frame goal direction, requiring no global map, waypoint stream, or external planner. In MuJoCo open-wall and indoor layouts, the distilled planner produces obstacle bypassing and post-avoidance goal recovery, raising teacher-calibrated on-time arrival from 38--40\% to 85--97\% and reducing brush/contact-heavy progress relative to a backbone-only controller. Ablations show that dynamic route shaping, teacher-active data collection, and the circular command interface are important for navigation efficiency and for training the 3.0\,m/s backbone. A Unitree G1 deployment analysis demonstrates hardware executability without continuous joystick steering.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究背景**：仿人机器人在人类尺度空间中运动时，局部导航与全身运动紧密耦合。在部分可观测、短距离感知条件下（如仅靠短距激光测距），机器人必须同时处理避障、稀疏目标恢复和稳定行走，而现有方法存在显式规划器-控制器分解带来的延迟，或纯反应式控制器在障碍物遮挡后丢失目标的问题。
- **核心问题**：如何在无全局地图、无外部规划器、仅依赖本体感知和局部测距的情况下，实现仿人机器人在杂乱环境中的避障与目标恢复，并保证运动稳定性。
- **整体含义**：提出一种有限感知下的集成导航与避障框架（LP-NavOA），通过将规划器教师仅用于训练，部署时复用冻结的运动骨干网络与轻量级循环局部规划器，实现无需持续摇杆操控的自主导航。

## 二、论文提出的方法论
- **整体思路**：采用教师-学生蒸馏范式，分两阶段训练。
    - **第一阶段**：训练基于射线投射感知-动作的PPO运动骨干网络，使用以机器人为中心的圆形航向-速度指令（`[∆ψ_t, v*_t]`）和共享指令侧安全滤波器，学习如何执行指令实现稳定行走。
    - **第二阶段**：冻结骨干网络后，利用A*或路径点教师生成轨迹数据，通过行为克隆训练一个循环局部规划器（GRU），该规划器在部署时仅覆盖航向指令，保留全身策略不变。
- **关键技术细节**：
    - 运动骨干输入：本体感知（IMU、关节位置/速度、先前动作）+ 三个方向（前、左、右）的8×8射线投射栅格 + 指令向量；输出归一化关节动作。
    - 指令侧安全滤波器：根据前向距离停止时间限制前向速度，并阻尼危险偏航指令，在所有推理条件下共享。
    - 循环局部规划器输入：本体感知（航向编码、联合速度或里程计）、三个射线投射栅格经过共享CNN编码后的32维特征、机体坐标系下的目标偏移和单位方向；输出：偏航修正量（与可能的前向速度预测）。
    - 教师标签生成（动态路径塑造）：混合关键目标航向和路径点航向，通过基于射线投射的闸门α_t动态切换：当近距离障碍物存在时偏向路径点，当清空时恢复关键目标。避免了纯路径点依赖（可能退化为路线记忆）和纯关键目标（无法学习绕行）的问题。
- **公式与算法流程**：
    - 第一阶段：θ* = argmax E[Σγ^t r_ll(t)]，获得骨干参数；第二阶段：φ* = argmin E[ℓ(f_φ, y_t)]，通过掩码行为克隆损失学习规划器参数。
    - 部署推理：规划器产生`∆ψ_t`，经安全滤波器后送入冻结骨干，输出关节目标。

## 三、实验设计
- **仿真环境与场景**：
    - 使用MuJoCo模拟器，仿真宇树G1仿人机器人。
    - **开放式墙壁布局（open straight-wall）**：机器人接近单面墙壁，需绕行并恢复目标。
    - **室内布局（indoor obstacle layout）**：包含房间边界、中央墙壁和箱体障碍物。
- **评价指标**：
    - **T-rel. on-time到达率**：以教师校准的有效距离预算（约23-31秒）衡量准时到达比例，避免超时绕圈通过。
    - **平均超时∆t**：实际使用时间减去标称最佳路径时间。
    - **任何碰撞（Any brush）**：持续安全包络刹车和身体/足部接触；**接触碰撞（Contact brush）**：低于硬碰撞终止的接触；**硬碰撞（Hard coll.）**：触发终止的碰撞。
- **对比方法**：
    - **R1 (Backbone-only)**：直接发送朝向当前关键目标的航向指令，无学习规划器。
    - **OURS (DR)**：冻结骨干 + 学习规划器，使用航位推算（dead-reckoning）状态。
    - **OURS (Odom)**：使用里程计状态（移除速度预测头）。
    - **T1 (Teacher, PP)**：教师存在（规划器参与）作为校准参考（不参与对比）。
- **消融实验**：
    - 命令格式消融：圆形移动目标 vs 固定世界坐标系目标序列，验证圆形命令对训练高速骨干的重要性。
    - 路径塑造消融：动态路线塑造 vs 纯路径点 vs 纯关键目标 vs 无教师强制（rollout时不注入教师标签） vs 无安全滤波器。
    - 在开放式墙壁任务上，对航位推算和里程计两种模式分别进行了对比。

## 四、资源与算力
- **训练硬件**：论文明确提到训练使用Intel Core i9-14900K CPU和NVIDIA GeForce RTX 4090D GPU。
- **并行环境数量**：
    - 命令格式消融：8192并行环境，1600次PPO迭代。
    - 导航评估：256并行环境，500 episodes/种子。
- **训练时间**：论文未明确给出具体训练时长（如小时数），仅说明迭代次数。未提供梯度更新步数或总样本数量细节。

## 五、实验数量与充分性
- **实验组数**：
    - 命令格式消融：对比2种条件 × 3种子。
    - 导航质量评估：3种子 × 500 episodes/种子，在开放式墙壁和室内两种布局上测试，报告均值±标准差。
    - 路径塑造消融：在开放式墙壁任务上，6种变体（DR模式：全动态、纯路径点、纯关键目标、无教师强制、无安全过滤器；Odom模式对应5种，共约11组），每组3种子。
    - 部署分析：单次真实机器人测试（多种墙壁布局），作为可行性验证。
- **充分性评价**：
    - **优点**：多个种子统计、合理的评价指标（计时、接触率）、消融设计系统全面，覆盖了主要设计选择；对比方法合理（骨干基线、教师校准）。
    - **不足**：实验完全基于MuJoCo仿真，缺乏真实环境定量对比（如不同光照、材质的地面）；仅一款机器人（Unitree G1），泛化性未验证；运动速度被限制在0.5-1.2 m/s（导航任务），真实场景动态障碍物未考虑；室内布局仅包含静态箱体，复杂度有限。

## 六、论文的主要结论与发现
- **核心结论**：LP-NavOA通过教师蒸馏的循环局部规划器显著提升了有限感知下仿人机器人的导航质量。
    - 在开放式墙壁和室内布局中，准时到达率从38-40%（纯骨干）提升至85-97%。
    - 平均超时从+14秒降低至+5.5~+7.5秒，Brush接触大幅减少（任何碰撞从~70%降至~10-24%）。
- **关键发现**：
    - **圆形航向-速度命令**对于训练高速运动骨干（3.0 m/s）至关重要，固定世界坐标命令只能达到1.44 m/s跟踪能力。
    - **动态路径塑造**相比纯路径点或纯关键目标标签，能更好地让规划器学会根据障碍物几何信息进行绕行与目标恢复，并降低PP（教师）-NoPP（规划器）转移差距。
    - 教师标签在数据采集时注入真实骨干rollout（教师强制）是必要的，否则性能下降（任何brush从23%升至54%）。
    - 安全滤波器在仿真中可被替代，但为真实部署提供最后防线。

## 七、优点
- **方法设计亮点**：
    - **分离训练与推理接口**：利用教师（A*、路径点）仅在训练阶段提供引导，部署时无需任何外部规划器或全局地图，仅需低级传感器和循环记忆，降低了硬件部署复杂度。
    - **动态路径塑造机制**：根据实时空间几何自动切换目标（关键目标 vs. 绕行路径点），避免了纯行为克隆的路线记忆问题，提高了泛化性。
    - **指令侧安全滤波器共享**：在所有推理条件下统一使用，确保公平对比，并提供了额外的安全层。
- **实验设计亮点**：
    - **时间敏感评价指标**：使用T-rel. on-time而不是传统的超时完成率，更能反映实际导航效率，避免绕圈通过。
    - **大量消融实验**：系统验证了命令格式、路径塑造、教师强制、安全滤波器等设计元素的有效性，结论可靠。
    - **种子统计报告均值±标准差**，实验可重复性强。

## 八、不足与局限
- **实验覆盖局限**：
    - **完全基于仿真**：所有导航结果来自MuJoCo，未在真实室内环境（如办公室、走廊）进行定量评估真实世界光照、摩擦、传感器噪声下的性能。
    - **仅使用静态障碍物**：未考虑动态障碍物（如行人），限制了应用场景。
    - **单一机器人平台**：仅验证了宇树G1，对尺寸、动力学不同的仿人机器人（如HRP、Atlas）未测试。
- **偏差风险**：
    - **教师依赖**：蒸馏过程中教师为A*与路径点，其本身可能无法覆盖所有复杂障碍布局（如迷宫、未知位置障碍），导致学生遇到未见过的配置时失败。
    - **安全滤波器的保守性**：在仿真中禁用滤波器后表现更好（更少brush），说明滤波器可能过度保守，在实际应用中可能牺牲速度与效率。
- **应用限制**：
    - **感知范围限制**：仅使用4米短距测距，对于高速运动（3.0 m/s）可用制动距离不足，论文也确认了命令速度被限制在0.5-1.2 m/s进行导航。
    - **无视觉输入**：仅依靠射线投射，无法区分物体类型、悬崖或透明障碍物，不适合复杂日常环境。
    - **未解决全局定位**：航位推算/里程计存在漂移，长时间大范围导航性能可能下降（论文未评估长距离场景）。

（完）
