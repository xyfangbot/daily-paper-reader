---
title: "RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning"
title_zh: RoboNaldo：通过运动引导的课程强化学习实现精准、稳定且有力的仿人足球射门
authors: "Yichao Zhong, Yidan Lu, Ye Lu, Tianyang Tang, Haoguang Mai, Yixuan Pan, Tianyu Li, L Lin-Lin Chen, Yi-Xiang Wang, Zhongyu Li, Peng Lu, Hongyang Li"
date: 2026-06-09
pdf: "https://arxiv.org/pdf/2606.11092"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=humanoid robot policy"
tldr: "人形机器人足球射门需兼顾全身稳定性、高冲量交互与准确性，但现有方法存在局限：运动跟踪RL难以适应不同球位，任务奖励RL难以从零探索。本文提出RoboNaldo三阶段运动引导课程RL框架，从单个参考先验逐步优化至射门性能。模拟中自由球误差降低48.6%，射门速度达2.96倍；实际场景中Unitree G1在3米处自由球和移动球平均误差分别为0.73m和0.86m，球速13.10m/s，达到职业球员59-71%水平。该工作为高冲量全身交互任务提供了稳定且精准的解决方案。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有方法无法同时保证人形机器人射门的稳定性和对不同球位的适应性，亟需一种能逐步探索并优化高冲量全身交互的框架。
method: 三阶段课程RL：从单一人体踢球参考学习全身先验，适应自由球随机位置，再通过运动指令与踢球接口扩展到移动球射门。
result: "模拟中自由球误差降低48.6%，射门速度提升2.96倍；实际3米自由球误差0.73m，移动球0.86m，球速13.10m/s。"
conclusion: RoboNaldo实现了高精度、高速度的人形机器人射门，为高冲量全身交互任务提供了有效范式。
---

## 摘要
精英级别的仿人足球射门需要全身稳定性、高冲量的全身交互以及对目标的精准度。运动跟踪驱动的强化学习提供了全身运动协调的稳定性，但固定的参考使得它难以适应不同的球位和击球时机；相比之下，任务奖励驱动的强化学习则难以从头探索并发现有效的射门动作。因此，我们提出了RoboNaldo，一种用于高冲量仿人交互的三阶段运动引导课程强化学习框架。它以单次人类踢球参考作为支架，并逐步将优化目标转向射门性能。该课程首先学习稳定的全身踢球先验，然后使踢球动作适应自由球设定（球静止在随机位置），最后通过运动指令和踢球触发接口扩展到运动中的射门。在训练过程中，一个高层启发式规划器控制该接口，而在推理时，替代的高层控制器可以驱动相同的底层策略。在仿真中，RoboNaldo的自由球射门误差比先前基线方法低48.6%，射门速度是它们的2.96倍。在现实世界中，搭载机载感知的Unitree G1上，RoboNaldo在自由球和运动球情况下，从3米外射门的平均目标误差分别为0.73米和0.86米。触球后球速达到13.10米/秒，相当于已报道的职业球员运动战射门速度的59-71%。项目页面：https://opendrivelab.com/RoboNaldo。

## Abstract
Elite humanoid soccer shooting requires whole-body stability, high-impulse whole-body interactions, and accuracy to targets. Motion tracking-driven reinforcement learning (RL) provides stability in whole-body movement coordination, but a fixed reference makes it hard to adapt to varied ball positions and strike timings; in contrast, task reward-driven RL struggles to explore and discover valid kicks from scratch. We therefore introduce RoboNaldo, a three-stage motion-guided curriculum RL framework for high-impulse humanoid interaction. A single human-kick reference is used as a scaffold and progressively shifts optimization towards shooting performance. The curriculum first learns a stable whole-body kicking prior, then adapts the kick to free-kick settings where the ball is stationary at random positions, and finally extends it to moving-ball shooting through a locomotion-command and kick-trigger interface. A high-level heuristic planner controls this interface during training, while alternative high-level controllers can drive the same low-level policy at inference. In simulation, RoboNaldo demonstrates free-kick shot error 48.6% lower and shoot velocity 2.96x than prior work baselines. In real world on a Unitree G1 with onboard perception, RoboNaldo attains 0.73 m and 0.86 m average target shooting error from 3 m away in free-kick and moving-ball cases, accordingly. And the post-contact ball velocity reaches 13.10 m/s, which is 59-71% of reported professional open-play shot speed. Project page: https://opendrivelab.com/RoboNaldo.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 精英级仿人足球射门要求同时具备全身稳定性、高冲量全身交互（短时强力撞击）以及对目标的精准度。
- 现有方法存在根本性矛盾：运动跟踪驱动的强化学习（RL）能保证全身运动协调的稳定性，但固定参考运动无法适应球位变化和击球时机；任务奖励驱动的RL可以从零探索，但在高维仿人控制空间中因稀疏奖励面临信用分配难题，难以自主发现有效射门。
- 当前仿人足球系统（如STOFT、Reactive、Striker、HumanX、PAiD）在射门精度、力量、移动球射门、机载感知和室外部署等方面存在明显局限：多数系统未同时报告点级精度和球速，只有极少工作考虑移动球射门且未评估精度和力量。
- 因此本文提出RoboNaldo，旨在通过一个三阶段运动引导课程RL框架，使仿人机器人能够稳定、精准、强力地完成自由球和移动球射门任务。

## 二、论文提出的方法论
- 核心思想：按每个学习信号能可靠提供的能力阶段性组织训练。一个单次人类踢球参考作为支架，逐步将优化重心转向射门性能。
- 三阶段课程设计：
  - **第一阶段：运动跟踪** – 模仿从人类视频重定向的侧脚踢参考运动，不使用球或任务奖励，建立稳定全身踢球先验。
  - **第二阶段：射门适应** – 引入球、目标和射门奖励，在球位随机采样下使策略适应接触点、击球方向和力度，同时保留运动跟踪先验（权重降低）。学会自由球射门。
  - **第三阶段：任务泛化** – 引入高层运动指令和踢球触发接口，将每回合分为接近、踢球、踢后稳定三个模式，解决移动球射门所需的时空调度。训练时由启发式规划器控制该接口，推理时可替换为其他高层控制器（如人类指令或协同训练的高层神经策略）。
- 奖励设计：
  - 运动跟踪奖励：14个身体部分的指数核跟踪，加重脚速权重。
  - 正则化奖励：罚动作率、平滑性、脚滑、空中时间、关节速度和力矩、关节限位等。
  - 射门任务奖励：包含脚/质心接近、球速、接触方向、**即时交互奖励**（覆盖接近、撞击、射后结果的全生命周期）和**稠密射门奖励**（弹道外推测后球到球门线交叉点位置，给予预测误差奖励，解决信用分配延迟）。
- 观察空间：547维，包括运动参考、锚参考、本体感知（5步历史）、外感知（5步球和目标在机器人坐标系的位置）。第三阶段锚参考被替换为高层运动指令。
- 策略网络：3层MLP（512→256→128），ELU激活，Actor+Critic架构，PPO优化。
- 域随机化：摩擦力、质心偏移、关节偏移、随机推力等，提升Sim-to-Real迁移鲁棒性。

## 三、实验设计
- **仿真实验**：
  - 平台：Isaac Lab（基于PhysX），4096并行环境（NVIDIA RTX 4090训练）。
  - 评估：16384个保留配置。
  - 任务：自由球（静止球在1m×1m前方方形区域采样，目标在5m外8m×2m球门平面）；移动球（球以0-5m/s速度从2m×2m前方区域射向机器人）。
  - 对比方法：PPO、AMP、PAiD（最新基线）、纯运动跟踪（Stage 1）、Stage 2零样本迁移、RoboNaldo Stage 2/3。
  - 消融实验：课程结构消融（Stage 0→2、Stage 1→3、Stage 2→3无规划器）、机制消融（无自适应采样、无稳定阶段）、交互奖励消融（替换为HDMI风格）。
  - 指标：存活率、射门误差（最小球-目标距离）、0.5m/1.0m成功率、峰值球速、接触率。
- **真实世界实验**：
  - 硬件：Unitree G1（29自由度，35kg），头部Livox MID-360 LiDAR + 胸部RealSense D435（红外+深度）。
  - 感知：LiDAR近距拟合反光球，红外相机远距离增强，AprilTag定位目标板。全机载状态估计，无动作捕捉。
  - 场景：室内地板和室外草坪足球场。
  - 任务：自由球（3米远，左/中/右目标）、移动球（人类传球）。
  - 指标：同上，但分为总尝试次数和有效尝试次数（成功发射球）。
- **实验结果**：
  - 仿真：RoboNaldo Stage 2自由球误差0.899m，成功率65.5%（<1m），球速14.79m/s，误差比PAiD低48.6%，速度是PAiD的2.96倍；Stage 3移动球误差1.131m，成功率63.3%，球速13.88m/s。
  - 真实：自由球（136次尝试，124次有效）平均误差0.73m，球速7.42m/s，1.0m成功率80.6%；移动球（27次尝试，20次有效）平均误差0.86m，球速7.10m/s，1.0m成功率70%。峰值球速13.10m/s，达到职业女球员71%、男球员59%。

## 四、资源与算力
- 仿真训练使用1块NVIDIA RTX 4090 GPU（4096个并行环境），训练到阶段收敛约需数十万次迭代（每阶段最多10^5次迭代），具体训练时长未明确报告。
- 推理时策略在Unitree G1机载运行（ONNX格式，50Hz控制频率），无需外部算力。
- 文中未说明具体训练耗时（小时数）、是否多卡分布式训练等细节。

## 五、实验数量与充分性
- 仿真实验：主比较包含5种方法（PPO/AMP/PAiD/运动跟踪/Stage2/Stage3），覆盖自由球和移动球两个场景；消融实验包含6组（课程结构×3、机制×2、奖励×1），每种条件报告3个随机种子均值±标准差。总共约上百个独立实验配置。
- 真实实验：自由球136次尝试（左58/中50/右28），移动球27次尝试，分别报告有效次数和全部结果。统计量足够，但移动球样本相对较小（27次）。
- 实验设计较全面：仿真验证了课程结构、机制和奖励的必要性；真实实验覆盖了多目标位置、不同球速、室外环境，并展示了失败分布（如右利脚偏差、移动球接触率下降）。
- 公平性：基线方法（PPO/AMP/PAiD）在类似环境中训练和评估，但PAiD使用不同感知拓扑（文中指出其目标仅为球门区域而非点级精度）。消融实验从对应阶段检查点热启动，避免从头训练的差异。
- 充分性：实验覆盖了主要断言（稳定性、精度、力量、泛化性）的验证，但仍有扩展空间：如更多基线的复现、对感知误差的定量分析、更长射程（5米）、更复杂场景（防守、拦截等）。

## 六、论文的主要结论与发现
- 运动引导的课程RL是解决高冲量仿人交互（如足球射门）的有效范式：第一阶段提供稳定先验，第二阶段学习精确接触和瞄准，第三阶段实现时空调度。
- RoboNaldo在仿真和真实世界都实现了**同时**精准、强力、稳定的射门，自由球和移动球均适用，并具备室外泛化能力。
- 与最新基线PAiD相比，自由球误差降低48.6%，球速提升2.96倍；真实球速13.10m/s接近职业球员水平。
- 消融实验证实了每个阶段、自适应采样、稳定阶段和即时交互奖励的不可或缺性。
- 策略可被不同高层控制器（启发式规划器或未来学习的策略）驱动的模块化接口设计是重要贡献。

## 七、优点
- **任务分解清晰**：三阶段课程合理分离了稳定性、适应性和计时性，使每个阶段目标明确、信号有效。
- **奖励设计精巧**：即时交互奖励避免了短时接触下奖励坍塌；稠密射门奖励通过弹道外推提前提供瞄准信号，解决信用分配延迟。
- **Sim-to-Real迁移成功**：域随机化+高效感知栈使得在真实草地、不同光照和人类传球干扰下仍能表现良好。
- **模块化高频接口**：高层指令（运动+踢触发）与低层策略解耦，便于未来集成更高水平的决策规划。
- **全面评估**：同时报告点级精度、球速、接触率、存活率，对实际部署有重要参考价值；对比了最新系统并明确列出能力矩阵（表1）。
- **开源项目**：提供项目页面和代码（推测），便于复现和进一步研究。

## 八、不足与局限
- **仅限单种参考运动**：当前只使用一个侧脚踢参考，无法应对需要多种技能（如脚背抽射、吊射、头球）的丰富场景。
- **高层触发器手动设计**：阶段转换和踢球触发由启发式规则控制，其阈值需要手动调节，可能影响泛化性；未训练端到端的高层决策策略。
- **感知模块特化**：依赖反光球和AprilTag，无法直接适用自然足球或者非标记环境；视觉对移动高速球的跟踪鲁棒性有限（文中提到YOLO快速运动模糊失效）。
- **真实实验样本量有限**：移动球仅27次尝试，统计显著性不够强；自由球虽然136次，但分解到左右中目标后每项约30-60次，仍可增加。
- **未评估长距离射门或带防守的场景**：仿真距离5m、真实3m，面对更远目标或对手干扰时性能未知。
- **仿真与现实的球速差距**：仿真中球速可达14.79m/s，真实世界平均7.42m/s（峰值13.10m/s），说明域随机化或物理参数校准仍有gap。
- **未提供详尽的算力和时间消耗报告**：如训练收敛所需小时数、GPU利用率等，对复现者不够友好。
- **对失败的定性分析不足**：虽然提到了移动球接触率下降归因于Sim-to-Real的计时gap和人类传球不一致，但缺乏定量分解（如感知误差、抖动、平衡损失等占比）。

（完）
