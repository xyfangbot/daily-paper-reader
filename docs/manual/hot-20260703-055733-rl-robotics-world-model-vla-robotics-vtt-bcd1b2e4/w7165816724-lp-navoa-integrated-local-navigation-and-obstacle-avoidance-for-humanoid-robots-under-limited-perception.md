---
title: "LP-NavOA: Integrated Local Navigation and Obstacle Avoidance for Humanoid Robots under Limited Perception"
title_zh: "LP-NavOA: 有限感知下仿人机器人的集成局部导航与避障"
authors: "Yi Luo, J T, Yuyao Min, Jinzhe Li, Kaihong Huang, P P Li"
date: 2026-06-22
pdf: "https://arxiv.org/pdf/2606.23249"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: "人形机器人在杂乱环境中的局部导航需同时解决避障、稀疏目标恢复和稳定运动，但短距离部分可观测感知增加了难度。本文提出LP-NavOA框架：先训练基于射线投影的PPO运动骨干（含速度命令和安全过滤器），冻结后利用A*和waypoint教师蒸馏出递归局部规划器，部署时仅改写航向命令。在MuJoCo测试中，按时到达率从38-40%提升至85-97%，碰撞大幅减少。该方法无需全局地图或外部规划器，并在Unitree G1上验证了硬件可执行性。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有分解式规划控制存在延迟，纯反应式控制器在障碍遮挡后易丢失目标，需一种集成方案同时解决避障、目标恢复与稳定运动。
method: "训练PPO运动骨干并冻结，用A*和waypoint教师生成rollouts蒸馏递归局部规划器，部署时仅覆盖航向命令，保留全身策略。"
result: "MuJoCo实验中蒸馏规划器将按时到达率从38-40%提升至85-97%，碰撞减少；消融验证动态路径塑造与命令接口关键性，骨干速度达3.0m/s。"
conclusion: LP-NavOA在有限感知下实现高效局部导航与避障，无需全局地图，硬件部署可行。
---

## 摘要
仿人机器人在杂乱环境中的局部导航必须同时解决避障、稀疏目标恢复以及短距离部分可观测传感下的稳定全身运动问题。显式的规划器-控制器分解会引入延迟，且可能无法匹配仿人机器人敏捷的指令跟踪极限，而纯粹的反应式控制器则可能在障碍物遮挡后丢失目标。我们提出了LP-NavOA，一个针对仿人机器人的有限感知导航与避障框架。首先，基于射线投射条件的感知-行动近端策略优化（PPO）运动骨干网络通过以机器人为中心的圆形航向速度指令和共享指令侧安全滤波器进行训练。在冻结该骨干网络后，A*算法和路径点教师生成轨迹，用于蒸馏一个递归局部规划器，该规划器在部署时仅覆盖航向指令，而保持全身策略不变。在运行时，LP-NavOA使用本体感知、短距离局部距离传感以及机体坐标系下的目标方向，无需全局地图、路径点流或外部规划器。在MuJoCo的开放墙壁和室内布局中，蒸馏后的规划器实现了障碍物绕行和避障后的目标恢复，将教师校准的准时到达率从38-40%提高到85-97%，并相比纯骨干网络控制器减少了接触密集的推进过程。消融实验表明，动态路径塑造、教师主动数据收集以及圆形指令接口对于导航效率以及训练3.0米/秒的骨干网络至关重要。Unitree G1的部署分析证明了其无需连续摇杆操纵的硬件可执行性。

## Abstract
Humanoid local navigation in cluttered environments must jointly resolve obstacle avoidance, sparse-goal recovery, and stable whole-body locomotion under short-range and partially observable sensing. Explicit planner-control decompositions introduce latency and can mismatch agile humanoid command-tracking limits, while purely reactive controllers may lose the goal after obstacle occlusion. We present LP-NavOA, a limited-perception navigation and obstacle-avoidance framework for humanoid robots. A raycast-conditioned perception-action proximal policy optimization (PPO) locomotion backbone is first trained with a robot-centered circular heading-speed command and a shared command-side safety filter. With this backbone frozen, A-star and waypoint teachers generate rollouts for distilling a recurrent local planner that overwrites only the heading command at deployment, leaving the whole-body policy intact. At runtime, LP-NavOA uses proprioception, short-range local range sensing, and a body-frame goal direction, requiring no global map, waypoint stream, or external planner. In MuJoCo open-wall and indoor layouts, the distilled planner produces obstacle bypassing and post-avoidance goal recovery, raising teacher-calibrated on-time arrival from 38--40\% to 85--97\% and reducing brush/contact-heavy progress relative to a backbone-only controller. Ablations show that dynamic route shaping, teacher-active data collection, and the circular command interface are important for navigation efficiency and for training the 3.0\,m/s backbone. A Unitree G1 deployment analysis demonstrates hardware executability without continuous joystick steering.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 仿人机器人在杂乱环境中进行局部导航时，需要同时解决三个耦合问题：避障、稀疏目标恢复（绕过障碍后重新朝向目标）以及基于短距离部分可观测传感的稳定全身运动。
- 现有方法存在两难：显式的规划器-控制分解（如A* + 动态窗口）会引入延迟，且抽象规划与敏捷仿人机器人的指令跟踪极限不匹配；纯反应式控制器虽然低延迟，但在障碍物遮挡后容易丢失目标，无法实现可靠的避障后恢复。
- 本文旨在提出一种在有限感知条件下（仅依赖本体感知、短距离射线扫描和目标方向）的集成局部导航与避障框架，无需全局地图、路径点流或外部规划器，同时保持仿人机器人的稳定运动。

## 二、论文提出的方法论
- **核心思想**：采用“训练时借助教师、部署时无教师”的两阶段分离策略。第一阶段训练一个基于近端策略优化（PPO）的感知-动作运动骨干网络，学习如何接收航向速度指令并生成全身关节动作；第二阶段冻结骨干网络，利用A*和路径点（waypoint）教师生成轨迹数据，蒸馏出一个递归局部规划器，该规划器在部署时仅改写航向指令，不干预全身策略。
- **关键技术细节**：
  - **第一阶段**：PPO骨架输入包括本体感知（IMU、关节位置/速度、上次动作等）、三个8×8射线栅格（前/左/右，4米范围）以及指令向量 [航向误差Δψ, 目标速度v*]。采用圆形目标命令生成：目标航向围绕当前机器人偏航均匀采样，转换为相对航向误差Δψ，使稀疏目标跟踪退化为航向-速度跟踪。共享指令侧安全滤波器：根据前端射线停止时间限制速度，并对阻塞侧航向施加阻尼。
  - **第二阶段**：冻结PPO骨架后，A*或路径点教师生成轨迹，收集观测-标签对（观测包括目标方向、射线栅格、记忆状态等；标签为教师给出的航向指令）。递归局部规划器使用GRU单元和MLP，输出一个范围限制的航向修正dΔψ。**动态路径塑造（Dynamic Route Shaping）**：教师标签在路径点航向和目标航向之间动态混合，混合系数α基于前端和侧向清空度（raycast）计算，使得靠近障碍时α≈0（使用路径点绕行），清空后α≈1（恢复向目标）。该混合控制同时用于标签和注入到骨干网络的数据收集，从而影响状态分布。
  - **推理时**：仅需本感、短距离射线、机体坐标系目标方向（4维：偏移和朝向角）、GRU记忆，输出航向命令，与共享安全滤波器配合送入冻结骨干网络，产生全身动作。
- **公式或算法流程**（文字说明）：
  1. 初始化PPO骨干网络参数θ，使用圆形目标命令和奖励训练，直到收敛。
  2. 冻结θ，用教师（A*或waypoint）在模拟器中展开轨迹，同时使用动态路径塑造生成目标航向序列，收集观测olp和标签y（航向误差）。
  3. 训练GRU+MLP组成的局部规划器f_φ，最小化行为克隆损失。
  4. 部署时，f_φ读取实时观测，计算航向修正，经安全滤波器后输入冻结的PPO骨架。

## 三、实验设计
- **使用场景**：MuJoCo仿真中的两个障碍族——开放直墙（open straight-wall）和室内障碍布局（indoor obstacle layout，含房间边界、中央墙和盒子障碍）。机器人模型为Unitree G1人形机器人。
- **Benchmark**：没有公开数据集，而是自建仿真场景。评价指标包括：
  - **准时到达率（T-rel. on-time）**：以教师（T1）展开中成功到达的98%有效距离为阈值，计算首次有用到达的比例（非超时完成）。
  - **时间开销Δt**：实际到达时间超出名义最佳路径时间的秒数。
  - **接触/碰撞指标**：任意擦碰（any brush，属于安全包线内但接触）、接触擦碰（contact brush，身体/脚接触障碍）、硬碰撞（hard collision）。
- **对比方法**：
  - **R1（骨干网络仅目标方向）**：直接朝当前关键目标发送航向指令，作为基线。
  - **OURS (DR)**：使用冻结骨干网络和学习到的局部规划器，状态基于航位推算（dead-reckoning）。
  - **OURS (Odom)**：使用里程计辅助的相对目标计算，去掉速度输出头。
  - **T1 (Teacher, PP)**：教师辅助（规划器存在），作为校准参考（非对比方法）。
- **消融实验**（在开放墙任务上）：
  - 分别取消动态路径塑造（仅路径点、仅关键目标）、去掉教师标签注入到骨干网络（no teacher forcing）、去掉安全滤波器。
  - 对比DR和Odom两种状态模式。

## 四、资源与算力
- 论文明确提及训练硬件：Intel Core i9-14900K CPU 和 NVIDIA GeForce RTX 4090D GPU。
- 训练配置：PPO骨干训练使用8192个并行环境，1600次迭代（per seed），三个训练种子。导航评估使用256个并行环境，每个种子500个回合。
- 未明确说明训练总时长，但指出基于mjlab框架进行GPU加速。

## 五、实验数量与充分性
- **实验数量**：主导航实验在两个场景（开放墙和室内布局）上各进行3个种子的500回合评估，共计约3000回合。消融实验在开放墙任务上，对多个变量（目标控制方式、状态模式、安全滤波器）进行对比，每个条件同样覆盖3个种子。
- **充分性**：统计指标包含均值±标准差，消除随机性。对比了速度骨干训练的命令形式（圆形vs固定序列），验证了命令接口的必要性。消融实验全面分析了动态路径塑造、教师强制、安全过滤器等关键组件的影响。实验设计较为客观，控制变量（共享骨干、安全滤波器、传感器等）。
- **公平性**：所有方法共享相同的感知输入、安全过滤器、回合限制，仅导航策略不同，对比公平。

## 六、论文的主要结论与发现
- 所提出的两阶段训练+蒸馏规划器（LP-NavOA）在开放墙和室内布局中，将准时到达率从骨干网络基线的38-40%提升至85-97%，同时时间开销从+14秒降低至约+5.5~7.5秒，擦碰/接触率大幅下降。
- 圆形航向速度命令（而非固定世界坐标航点）对于训练高速（3.0 m/s）运动骨干至关重要，后者难以跟踪固定航点。
- 动态路径塑造是核心：仅使用路径点标签会导致模板重演（在无教师时无法泛化），仅使用目标标签则学不会绕行。动态混合既提供绕行监督又在清空后切换为目标恢复，是最有效的。
- 教师标签必须同时注入到骨干网络的数据收集（teacher forcing）中，否则状态分布与测试时不一致，性能下降。
- 安全滤波器在仿真中略微降低效率，但保留作为部署的最后防线；学习到的规划器本身已能处理大部分避障。
- 在Unitree G1真实机器人上验证了部署可行性：紧凑的推理接口能生成绕行与恢复指令，无需持续摇杆控制。

## 七、优点
- **设计优雅**：将复杂的导航决策与稳定的全身运动解耦，通过蒸馏将教师知识压缩为轻量递归规划器，部署时仅需极少的输入。
- **带宽高效**：规划器仅改写航向命令，保留冻结的全身运动策略，避免了重新训练整个网络。
- **泛化性好**：动态路径塑造使得学生模型学会基于当前感知（而非记忆的路径点）进行绕行决策，提高了对未见障碍布局的适应能力。
- **实验严谨**：多种消融、多种子、多指标（非仅到达率），区分了首到达与超时到达，并跟踪接触/碰撞细节，更贴近实际导航质量。
- **硬件验证**：在真实Unitree G1上做了可行性测试，表明方法可从仿真迁移到真实机器人（虽未做大规模真实实验）。

## 八、不足与局限
- **感知局限**：仅依赖短距离（4m）射线扫描，对更远或动态障碍物、遮挡严重的环境可能失效。未考虑视觉信息（如RGB-D），感知通量有限。
- **场景范围窄**：正式评估仅限于两种静态布局（开放墙和室内固定障碍），未涉及复杂动态障碍、非结构化地形（如楼梯、斜坡）、多人场景等。
- **真实实验不充分**：仅有Unitree G1的单一壁障布局演示，缺少在多种真实环境下的系统量化对比（与仿真结果无法直接对标），也未测试不同命令速度、不同障碍形状下的鲁棒性。
- **未讨论计算开销与实时性**：对于GRU网络在嵌入式硬件上的推理延迟、功耗等未提及。
- **依赖仿真泛化**：训练完全在MuJoCo仿真中完成，真实环境的传感器噪声、动力学误差、延迟等可能造成性能下降，文中未进行零样本迁移测试（除一段部署演示外）。
- **目标假设较强**：假设目标方向（机体坐标系下）始终已知，现实中可能需要全局定位或视觉识别支持，这超出了本文范围。

（完）
