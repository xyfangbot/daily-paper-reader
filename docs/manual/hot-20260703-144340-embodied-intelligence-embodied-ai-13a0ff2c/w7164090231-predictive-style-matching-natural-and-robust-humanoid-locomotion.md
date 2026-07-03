---
title: "Predictive Style Matching: Natural and Robust Humanoid Locomotion"
title_zh: 预测式风格匹配：自然且稳健的类人机器人行走
authors: "Simeon Nedelchev, Ekaterina Chaikovskaia, Egor Davydenko, Eduard Zaliaev, Roman Gorbachev"
date: 2026-06-05
pdf: "https://arxiv.org/pdf/2606.07083"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=humanoid robot policy"
tldr: 强化学习控制人形机器人时，任务奖励导致运动僵硬不对称，而模仿学习虽提升自然度却因依赖时间索引参考信号而对抗干扰敏感。提出Predictive Style Matching，通过离线预测器根据下半身状态和速度命令生成状态条件的上半身关节与步态目标来塑造奖励。在Unitree G1上，PSM相比纯任务RL降低约10倍上半身风格误差，且保持相同摔倒恢复率；相比模仿学习，鲁棒性提高约5倍。该方法在不增加部署成本的前提下实现了自然且抗干扰的双足运动。
source: openalex
selection_source: hot_paper_scout
motivation: 现有方法在运动自然度与抗干扰鲁棒性之间难以兼得：任务RL动作僵硬，模仿学习易因参考信号冲突而失衡。
method: 提出Predictive Style Matching，训练时离线预测器根据下半身状态历史与速度命令输出状态条件的上半身姿态及步态目标，用于奖励计算；部署时无需该预测器。
result: 在Unitree G1上，PSM比任务RL降低约10倍上半身风格误差，且摔后恢复率持平；模仿学习风格误差最低，但摔倒率高出约5倍。
conclusion: PSM在不增加部署成本的前提下，实现了自然且鲁棒的人形机器人运动控制，化解了风格与鲁棒性的矛盾。
---

## 摘要
强化学习已成为类人机器人行走控制的主流方法：策略能够可靠地从仿真迁移到硬件，并优雅地从干扰中恢复。然而，运动质量仍显不足：仅基于任务奖励的策略往往收敛至僵硬、不对称的步态，而运动模仿方法虽改善了外观，却因参考信号可能与恢复平衡所需的瞬时姿态相悖，从而对外部干扰更加敏感。我们提出预测式风格匹配（Predictive Style Matching），该方法通过离线预测器将机器人下半身状态历史与速度指令映射为可解释的上半身关节目标与步态目标，进而在训练期间塑造奖励。由于目标是基于状态而非时间索引，且预测器仅在训练时使用，部署后的控制器继承了纯任务奖励强化学习基线的基本感知接口与推理成本。在Unitree G1上的仿真与硬件实验中，预测式风格匹配相比纯任务奖励强化学习将上半身风格误差降低约一个数量级，同时保持其跌倒恢复率；而运动模仿基线虽取得了最低的风格误差，但跌倒恢复失败频率高出约五倍。

## Abstract
Reinforcement learning has become the prevailing approach to humanoid locomotion control: policies transfer reliably from simulation to hardware and recover gracefully from disturbances. Motion quality, however, still lags behind: task-only rewards often converge to stiff, asymmetric gaits, while motion imitation methods improve appearance but become more sensitive to external disturbances because reference signals can oppose the transient poses needed to regain balance. We propose Predictive Style Matching, in which an offline predictor maps the robot's lower-body state history and velocity commands to interpretable upper-body joint and gait targets that shape the rewards during training. Because the targets are state-conditioned rather than time-indexed and the predictor is used only at training time, the deployed controller inherits the proprioceptive interface and inference cost of a task-only RL baseline. On the Unitree G1, in both simulation and hardware, PSM reduces upper-body style error by roughly an order of magnitude over task-only RL while preserving its fall-recovery rate, whereas the motion-imitation baseline attains the lowest style error but fails to recover from disturbances about five times as often.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 强化学习已成为双足人形机器人行走控制的主流方法，策略能够从仿真可靠迁移到硬件，并有效从干扰中恢复。
- 但现有方法在运动自然度与抗干扰鲁棒性之间存在难以兼顾的矛盾：
  - **纯任务奖励RL**：仅优化速度跟踪、平衡等任务指标，缺乏对人体协调（如手臂摆动、骨盆运动）的显式约束，导致策略收敛至僵硬、不对称的步态，外观不自然。
  - **运动模仿方法**（如DeepMimic、ZEST等）：通过匹配时间索引的参考姿态（来自动捕数据或视频）来提升外观自然度，但参考信号可能违背恢复平衡所需的瞬时姿态，导致对外部扰动更加敏感，跌倒恢复率下降。
- 核心问题：如何在RL训练中注入人类运动协调性，同时不增加部署时的参考生成器，且不迫使策略追求与恢复相悖的风格目标。

## 二、论文提出的方法论
- **核心思想**：Predictive Style Matching（预测式风格匹配，PSM），一个两阶段流水线：
  - **阶段1（离线预测器训练）**：训练一个网络 \( f_\phi \)，输入机器人下半身状态历史（髋/膝关节角度、足部位置、根速度）和速度指令，输出可解释的上半身关节角度（17个）和步态描述符（步长、步宽、足倾角、根高、占空比等）。
  - **阶段2（RL训练阶段）**：在PPO训练中，冻结预测器 \( f_\phi \)，将其输出作为匹配奖励（match rewards）添加到标准运动任务奖励中。部署时只保留策略网络 \( \pi_\theta \)，预测器不参与推理，因此部署接口与纯任务RL相同（仅有本体感受输入）。
- **关键技术细节**：
  - 预测器使用GRU编码历史序列，MLP回归未来 \( T_p \) 步的目标。
  - 训练损失包括均方误差项和一个左右对称性正则项 \( L_{\text{sym}} \)。
  - 输入包含历史窗口 \( T_h = 25 \) 步（50 Hz控制频率），未来窗口 \( T_p = 10 \) 步。
  - 匹配奖励使用指数核函数，对每个关节和描述符分别计算，然后加权求和。
  - 策略训练采用课程学习：先纯任务训练，待平衡行为建立后才逐步增加风格匹配权重。
- 与两类替代方案对比：
  - **Clip-tracking**：使用时间索引的参考姿态，目标独立于机器人恢复状态。
  - **AMP**：使用判别器提供全状态标量风格分数，不可分解至具体关节和步态描述符。

## 三、实验设计
- **平台**：Unitree G1双足人形机器人（仿真环境使用MuJoCo，通过MJLAB框架训练）。
- **数据集**：基于BoneSeed动捕数据中的步行子集（约10%的可用片段），重新目标化至Unitree G1。
- **对比方法**：
  - **Vanilla RL**：仅使用纯任务奖励（\( r_t = r_t^{\text{loco}} \)）。
  - **Tracking**（代表clip-tracking方法）：使用BeyondMimic实现，在奖励中加入时间索引姿态匹配，每个参考轨迹训练一个策略。
  - **PSM**：使用预测器输出的风格匹配奖励。
- **训练设置**：三个方法共享相同的MDP、观测空间、PPO超参数、域随机化、课程学习计划和干扰调度，仅风格信号不同。
- **评估指标**：
  - **自然度**：使用动态时间规整（DTW）计算上半身关节序列与参考剪辑的差异。
  - **鲁棒性**：在相同指令轨迹下施加脉冲推力/速度冲击，测量跌倒率、速度跟踪误差、任务恢复时间 \( T_{\text{vel}} \)。
  - 仿真中进行大规模批量测试，硬件上执行代表性命令子集。

## 四、资源与算力
- 论文明确提到：
  - 预测器训练在一张RTX 4090上进行约60分钟，经过45000次Adam更新。
  - PSM的RL训练阶段，查询预测器使每轮迭代增加约10%时间（同样在RTX 4090上）。
  - 未说明RL训练总时长、使用的GPU数量（推测单卡）、整体实验总计算量。

## 五、实验数量与充分性
- **自然度实验**：在仿真中批量测试多种速度指令轨迹（包括来自数据集的质心速度和自定义脚本化模式）。DTW结果取平均值和标准差。
- **鲁棒性实验**：重复相同指令轨迹，施加预先设定的脉冲推力和速度冲击，报告跌倒率和恢复时间。涵盖不同推力和方向（图6）。
- **硬件实验**：执行代表性的命令子集，展示协调的手臂摆动和步态（图1和补充视频）。
- **消融分析**：论文提到仅使用上半身匹配权重已能通过运动耦合改善步态节奏，但最终同时匹配上半身和步态描述符更稳定。
- **公平性**：三个方法在相同训练环境、相同PPO预算、相同课程和干扰下比较，保证差异仅源于风格信号。
- 充分性评价：实验设计较为全面，覆盖了自然度、鲁棒性（仿真+硬件）、不同扰动类型，但缺少与AMP和通用跟踪器（如ZEST）的直接对比。

## 六、论文的主要结论与发现
- PSM在仿真中将上半身DTW误差相对Vanilla RL降低约8倍（0.31 vs. 2.41），步态DTW降低约4倍（0.21 vs. 0.81），同时保持与Vanilla RL相当的跌倒率（4.1% vs. 4.4%）和恢复时间（约0.9秒）。
- Tracking方法取得了最低的DTW（自然度最佳），但跌倒率高达21.5%（约为PSM和Vanilla RL的5倍），恢复时间更长（1.80秒），尤其在侧向推力下表现最差。
- 速度跟踪误差三个方法相近，说明执行了相同的运动任务。
- 硬件上PSM展示了协调的上半身运动和良好的推力鲁棒性。
- 核心结论：通过使用状态条件（而非时间索引）的风格目标，PSM实现了自然度与鲁棒性的良好平衡，且不增加部署成本。

## 七、优点
- **创新性地解耦风格与鲁棒性**：将风格信号作为训练时的状态条件先验，而非部署时必须跟踪的参考轨迹，从根本上避免了干扰恢复过程中的冲突。
- **部署简洁**：部署时只需策略网络，运行成本与纯任务RL相同，无额外推理负担。
- **可解释的风格目标**：预测器输出具体关节角度和步态标量，而非抽象隐变量或标量分数，便于调试和分析。
- **方法通用性**：原则上可迁移至其他双足平台（仅需重新训练预测器并调整匹配关节子集）。
- **实验设计严谨**：在相同MDP、训练超参、域随机化条件下对比三种方法，使差异可归因于风格信号。

## 八、不足与局限
- **预测器质量瓶颈**：PSM能达到的自然度上限受限于离线预测器的准确性，而预测器仅在下半身状态和命令上训练，可能无法完全泛化到所有运动模式。
- **未解决仿真与真实数据之间的腿部位移偏差**：预测器输入的下半身状态来自仿真，与动捕数据存在差距，论文未显式处理这一对齐问题。
- **仅使用第一帧预测**：尽管预测器输出未来 \( T_p \) 步，但RL中只使用最接近的一帧（\( k=0 \)），未充分利用多步信息。
- **缺失与AMP及通用跟踪器的直接对比**：论文仅在controlled setup中对比了单剪辑跟踪，未与AMP [12]或ZEST [10]等更先进的方法在相同数据上比较。
- **实验仅针对平坦地面行走**：未考虑地形变化、上下坡等更具挑战的场景，预测器也可能需要地形信息。
- **算力消耗未完整报告**：RL训练总GPU小时数、多卡并行情况未说明，可复现性受一定影响。

（完）
