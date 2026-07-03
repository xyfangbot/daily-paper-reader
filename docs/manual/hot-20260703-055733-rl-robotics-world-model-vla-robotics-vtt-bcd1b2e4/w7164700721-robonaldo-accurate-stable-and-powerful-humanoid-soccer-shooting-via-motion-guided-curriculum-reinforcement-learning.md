---
title: "RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning"
title_zh: "RoboNaldo: 通过运动引导的课程强化学习实现精确、稳定且强力的人形机器人足球射门"
authors: "Yichao Zhong, Yidan Lu, Ye Lu, Tianyang Tang, Haoguang Mai, Yixuan Pan, Tianyu Li, L Lin-Lin Chen, Yi-Xiang Wang, Zhongyu Li, Peng Lu, Hongyang Li"
date: 2026-06-09
pdf: "https://arxiv.org/pdf/2606.11092"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: "人形机器人足球射门需兼顾全身稳定、高冲击力交互和精度。现有运动跟踪强化学习难以适应球位变化，任务奖励驱动方法探索效率低。本文提出三阶段运动引导课程强化学习框架RoboNaldo：以单个人类踢球动作为脚手架，先学习稳定全身踢球先验，再适应随机位置静止球自由踢，最后通过运动指令与踢球触发接口扩展至移动球射门。仿真中自由踢误差降低48.6%且速度提升2.96倍；真实Unitree G1上，3米距离自由踢平均误差0.73m、移动球0.86m，触球后球速达13.10m/s（职业球员的59%-71%）。该框架首次实现从单参考到高精度、高速度人形机器人射门的端到端学习，且低层策略可集成不同高层控制器。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有运动跟踪强化学习因固定参考难以适应不同球位和踢球时机，任务奖励驱动方法则难以从零探索有效高冲击踢球动作。
method: 提出三阶段课程强化学习：先学习稳定全身踢球先验，再适应随机位置静止球自由踢，最后通过运动指令与踢球触发接口扩展至移动球射门，训练时由高层启发式规划器控制接口。
result: "仿真中自由踢误差降低48.6%，射门速度提升2.96倍；真实Unitree G1上，3米距离自由踢平均误差0.73m，移动球0.86m，球速13.10m/s。"
conclusion: RoboNaldo实现了准确、稳定、有力的人形机器人足球射门，低层策略可灵活集成不同高层控制器，显著优于此前基线。
---

## 摘要
精英级人形机器人足球射门需要全身稳定性、高冲量全身交互以及目标精度。运动追踪驱动的强化学习（RL）提供了全身运动协调的稳定性，但固定的参考轨迹使其难以适应不同的球位和击球时机；相比之下，任务奖励驱动的RL难以从零开始探索并发现有效的踢球动作。因此，我们提出RoboNaldo，一种三阶段运动引导的课程强化学习框架，用于高冲量人形机器人交互。以单一人踢球参考作为支架，并逐步将优化目标转向射门表现。该课程首先学习稳定的全身踢球先验知识，然后使踢球适应球静止于随机位置的开球场景，最后通过运动指令与踢球触发接口扩展到移动球射门。训练过程中，高层启发式规划器控制该接口，而在推理时，替代的高层控制器可驱动相同的低层策略。在仿真中，RoboNaldo在开球射门误差上比先前工作基线降低48.6%，射门速度提升2.96倍。在真实环境中，搭载机载感知的宇树G1机器人上，RoboNaldo在开球和移动球场景下从3米距离射门的平均目标误差分别为0.73米和0.86米。接触后球速达到13.10米/秒，是文献报道的职业比赛运动战射门速度的59-71%。项目页面：https://opendrivelab.com/RoboNaldo。

## Abstract
Elite humanoid soccer shooting requires whole-body stability, high-impulse whole-body interactions, and accuracy to targets. Motion tracking-driven reinforcement learning (RL) provides stability in whole-body movement coordination, but a fixed reference makes it hard to adapt to varied ball positions and strike timings; in contrast, task reward-driven RL struggles to explore and discover valid kicks from scratch. We therefore introduce RoboNaldo, a three-stage motion-guided curriculum RL framework for high-impulse humanoid interaction. A single human-kick reference is used as a scaffold and progressively shifts optimization towards shooting performance. The curriculum first learns a stable whole-body kicking prior, then adapts the kick to free-kick settings where the ball is stationary at random positions, and finally extends it to moving-ball shooting through a locomotion-command and kick-trigger interface. A high-level heuristic planner controls this interface during training, while alternative high-level controllers can drive the same low-level policy at inference. In simulation, RoboNaldo demonstrates free-kick shot error 48.6% lower and shoot velocity 2.96x than prior work baselines. In real world on a Unitree G1 with onboard perception, RoboNaldo attains 0.73 m and 0.86 m average target shooting error from 3 m away in free-kick and moving-ball cases, accordingly. And the post-contact ball velocity reaches 13.10 m/s, which is 59-71% of reported professional open-play shot speed. Project page: https://opendrivelab.com/RoboNaldo.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 人形机器人足球射门是一项高度综合的任务，要求同时具备**全身稳定性**、**高冲量交互**（极短的足-球接触时间，约3-5个控制步长）和**精确的目标命中**。
- 现有方法存在根本性矛盾：
  - **运动跟踪强化学习**（如DeepMimic、AMP）虽能提供稳定的全身协调，但固定参考轨迹无法适应变化的球位和击球时机。
  - **任务奖励驱动强化学习**（如PPO）虽能指定球的目标方向，但需要从零探索平衡、摆腿、接触、瞄准等耦合技能，且稀疏奖励导致信用分配困难。
- 已有的人形足球系统（如HumanX、PAiD）在精度、速度、移动球射门、室外部署等方面存在不足：多数仅评估方向余弦（忽略点级精度），未同时报告动能和移动球能力。
- 因此，论文旨在提出一个能**同时实现稳定性、精度、力量和泛化性**的人形射门学习框架。

## 二、论文提出的方法论
- **核心思想**：采用**三阶段运动引导课程强化学习**，将学习信号按各自能可靠提供的能力分阶段使用。
  - **Stage 1（运动跟踪）**：使用单一人踢球参考（通过GVHMR和GMR从人类视频重定向），学习稳定的全身踢球先验。**无球、无任务奖励**，只模仿运动。
  - **Stage 2（射门适应）**：引入球、目标和射门奖励，球在名义接触位置周围随机生成。策略必须调整接触点、击球方向和速度以适应不同球位。学习**自由踢（静止球）射门**。
  - **Stage 3（任务泛化）**：引入**运动指令/踢球触发接口**，将移动球射门分解为接近控制 + 接触时机决策。训练时，启发式规划器控制接口；推理时可替换为其他高层控制器。包含接近、踢球、踢后稳定三个阶段。
- **关键技术细节**：
  - **观察空间**（547维）：运动参考、锚参考（Stage3替换为运动命令）、本体感知历史（5步）、外部感知（球和目标位置、5步历史）。
  - **奖励设计**：
    - 运动跟踪奖励：14个身体部位的指数核跟踪。
    - 正则化奖励：动作率、平滑性、足滑、悬空、关节限位等。
    - 射门任务奖励：包含**即时交互奖励**（R_interact = (R_contact + R_goal) * (R_vel + R_force)/4），覆盖接近、冲击、球速和目标结果；**密集化射门奖励**：通过外推弹道，在每次后接触步提供预测目标误差的密集信号。
  - **阶段切换**：任务奖励饱和、动作噪声收敛、行为出现后自动进入下一阶段。
  - **域随机化**：摩擦力、重心偏移、关节位置偏移、执行器延迟、随机推力等，实现sim-to-real迁移。

## 三、实验设计
- **实验场景**：
  - **仿真环境**：Isaac Lab，4096并行环境，物理步长5ms，控制频率50Hz。球为刚体球（半径0.115m，质量0.41kg）。目标平面为8m×2m，距机器人5m。
  - **真实环境**：宇树G1机器人（29自由度，35kg），室内地板和室外草地足球场。机载感知：头戴Livox MID-360 LiDAR + 胸部RealSense D435（红外/灰度进行球检测）。球为尺寸5足球，目标为AprilTag板。
- **对比方法**：
  - **仿真基线**：PPO（稀疏奖励）、AMP（对抗性运动先验）、PAiD（渐进感知-行动框架）、Stage 1运动跟踪、Stage 2零样本迁移到移动球、RoboNaldo Stage 2/3。
  - **消融实验**：去除Stage 1（Stage 0→2）、去除Stage 2（Stage 1→3）、去除Stage 3规划器、去除自适应采样、去除稳定阶段、替换为HDMI风格交互奖励。
- **评估指标**：生存率、射门误差（最小球-目标距离）、0.5m/1.0m成功率、峰值球速、接触率。

## 四、资源与算力
- 仿真训练：使用**1块NVIDIA RTX 4090 GPU**，4096并行环境，每阶段最多100k迭代，每1k检查点。
- 训练细节：PPO优化，异步RL（RSL-RL），每个更新使用5个学习周期、4个mini-batch，24环境步每rollout，折扣γ=0.99，GAE λ=0.95。
- 真实推理：ONNX策略在机器人上以**50Hz**运行，无外部位姿估计，完全机载。

## 五、实验数量与充分性
- **仿真实验**：主对比实验包括自由踢和移动球两个场景，每个方法报告均值和标准差，共7个对比方法+7个消融变体。消融覆盖课程结构、采样机制、稳定阶段、交互奖励等关键设计。
- **真实实验**：
  - 自由踢：136次总尝试，124次有效射门（91.2%接触率），按左/中/右目标分组。
  - 移动球：27次总尝试，20次有效射门。
- **充分性评价**：实验数量充足，覆盖仿真大规模统计和真实有限样本。消融实验设计系统，验证每个组件的必要性。随机种子多次运行报告标准差，结果可复现。但真实实验未进行多次重复（如多次运行求平均），且移动球样本较少（27次），结论需谨慎。未在多个机器人或不同环境上复现。

## 六、论文的主要结论与发现
- **仿真结论**：
  - Stage 2自由踢：0.899m平均误差，65.5% 1.0m成功率，14.79m/s球速。相比PAiD，误差降低48.6%，速度提升2.96倍。
  - Stage 3移动球：1.131m平均误差，63.3% 1.0m成功率，13.875m/s球速。
- **真实结论**：
  - 自由踢：0.73m平均误差，80.6% 1.0m成功率，球速7.42m/s，接触率91.2%，生存率100%。
  - 移动球：0.86m平均误差，70.0% 1.0m成功率，球速7.10m/s，接触率74.1%，生存率88.9%。
  - 峰值球速13.10m/s，达到职业女足和男足运动战射门速度的59-71%。
- **关键发现**：三阶段课程有效分离了稳定性、精确瞄准和移动球时间对齐难题；即时交互奖励优于HDMI稀疏奖励；自适应采样和稳定阶段对移动球鲁棒性至关重要。

## 七、优点
- **方法创新**：首次提出运动引导课程强化学习框架，将单一人踢参考逐步转化为适应不同球位和时机的精确射门策略。
- **性能领先**：同时在仿真和真实中实现高精度（<1m误差）、高速度（>13m/s）和高泛化（自由踢+移动球），显著优于此前基线。
- **模块化设计**：低层策略可被不同高层控制器（规则规划器、人类指令、共训练神经策略）驱动，无需重新训练。
- **端到端真实部署**：使用机载感知（LiDAR+摄像头），完全脱离动作捕捉和外位置估计，在室外草地成功演示。
- **奖励工程精细**：密集化射门奖励和即时交互奖励解决了脉冲碰撞任务的信用分配问题。

## 八、不足与局限
- **单一参考动作**：目前依赖单一人踢参考，无法应对需要多技能（如过顶球、凌空抽射）的复杂场景。
- **手工高层触发器**：阶段转换和踢球触发由启发式规则控制，缺乏鲁棒自适应性。移动球场景的sim-to-real差距主要源于时机判断不准确。
- **感知模块定制**：球检测依赖反光足球的强反射特征，对自然足球（无反射涂层）失效，限制了应用范围。
- **真实实验样本量有限**：移动球仅27次尝试，统计可靠性不足；未进行机器人间或多环境复现。
- **评估指标未覆盖所有维度**：未报告射门角度、球旋转、不同地表条件（如湿草地）下的表现。
- **未明确训练总时长**：论文未给出各阶段实际训练时间，仅给出迭代次数，不利于复现估算。
- **代码与数据未公开**：虽提供项目页面，但未明确是否开源代码和数据集。

（完）
