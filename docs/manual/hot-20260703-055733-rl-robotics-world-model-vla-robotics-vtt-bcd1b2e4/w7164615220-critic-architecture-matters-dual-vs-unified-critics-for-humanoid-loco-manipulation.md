---
title: "Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation"
title_zh: 批评者架构至关重要：用于人形机器人全身运动操控的双重批评者与统一批评者
authors: Mehmet Turan Yardımcı
date: 2026-06-10
pdf: "https://arxiv.org/pdf/2606.11891"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: "人形机器人多目标强化学习需协调运动与操作，其中critic架构是关键设计选择。本文在Unitree G1上对比统一与双critic，通过13级顺序课程训练。双critic策略在到达速度（6.5 vs 22.6步）、吞吐量（14.3 vs 7.0次/千步）和验证率（65.2% vs 53.8%）上显著优于统一critic，且额外反博弈奖励无进一步收益。结果表明critic架构比奖励工程影响更大，对模仿学习策略的RL微调具有指导意义。"
source: openalex
selection_source: hot_paper_scout
motivation: 多目标人形机器人策略中critic架构（统一或分离）未被充分研究，是影响协调性能的潜在首要因素。
method: 在Isaac Lab中，对Unitree G1（23自由度）训练loco-manipulation策略，通过13级课程对比双critic与统一critic。
result: "双critic到达快3.5倍（6.5步vs22.6步），吞吐量高2倍（14.3 vs 7.0次/千步），验证率达65.2% vs 53.8%。"
conclusion: critic架构是比奖励工程更关键的设计选择，统一critic可能抑制操作学习，对RL微调策略有直接启示。
---

## 摘要
人形机器人的多目标强化学习必须在单一策略内协调运动与操控。一个自然的设计选择是使用单一（统一）批评者来估计所有目标的组合价值，还是使用具有不相交奖励信号的独立（双重）批评者。我们在NVIDIA Isaac Lab中，基于Unitree G1人形机器人（23个主动自由度）进行了受控比较，通过一个从静态抓取到携带可变方向目标行走的13级顺序课程训练全身运动操控策略。在标准化评估中，与统一批评者策略相比，双重批评者策略到达目标快3.5倍（6.5步对比22.6步模拟步数），吞吐量提高2倍（每1000步有效到达次数14.3对比7.0），并实现更高的有效到达率（65.2%对比53.8%）。值得注意的是，额外的反博弈奖励机制在仅改变架构的基础上并未带来进一步改进（60.9%对比65.2%）。这些结果对基于模仿学习的策略进行RL微调的新兴范式具有直接启示：当用RL优化预训练的操控策略时，统一批评者有可能通过竞争性的运动梯度抑制已学行为。这些发现表明，在多目标人形机器人强化学习中，批评者架构是一个首要且常被忽视的设计选择，其对到达效率的影响大于奖励工程。

## Abstract
Multi-objective reinforcement learning for humanoid robots must coordinate locomotion and manipulation within a single policy. A natural design choice is whether to use a single (unified) critic that estimates the combined value of all objectives, or separate (dual) critics with disjoint reward signals. We present a controlled comparison on the Unitree G1 humanoid (23 active DoF) in NVIDIA Isaac Lab, training loco-manipulation policies through a sequential curriculum spanning 13 levels from stationary reaching to walking with variable-orientation targets. In standardized evaluation, dual-critic policies reach targets 3.5$\times$ faster (6.5 vs. 22.6 simulation steps), achieve 2$\times$ higher throughput (14.3 vs. 7.0 validated reaches per 1,000 steps), and attain higher validated reach rates (65.2% vs. 53.8%) compared to the unified-critic policy. Notably, additional anti-gaming reward mechanisms provide no further improvement beyond the architectural change alone (60.9% vs. 65.2%). These results have direct implications for the emerging paradigm of RL fine-tuning of imitation-learned policies: when refining a pre-trained manipulation policy with RL, a unified critic risks suppressing the learned behavior through competing locomotion gradients. These findings demonstrate that critic architecture is a primary - and often overlooked - design choice in multi-objective humanoid RL, with greater impact than reward engineering on reaching efficiency.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 人形机器人需要同时协调行走（locomotion）和抓取/操控（manipulation），即全身运动操控（loco-manipulation），这是一个典型的多目标强化学习问题。
- 在多目标RL中，一个关键但常被忽视的设计选择是**critic架构**：是使用一个统一的critic来估计所有目标的组合价值，还是使用多个独立的critic（每个目标有自己的价值函数）？
- 现有文献大多直接采用某一种架构而不进行对比。本文旨在系统比较统一critic与双critic架构对学习效率和最终性能的影响。
- 此外，该问题与“模仿学习+RL微调”的混合范式密切相关：若用统一critic微调预训练的操控策略，运动目标的梯度可能抑制已学到的操控行为，而双critic可自然隔离梯度。

## 二、论文提出的方法论
- **平台与环境**：在NVIDIA Isaac Lab中训练Unitree G1人形机器人（23个主动自由度：12个腿关节、5个手臂关节（右臂：肩部pitch/roll/yaw、肘部pitch/roll），手腕和手指关节固定）。
- **策略结构**：
  - 统一critic架构：两个独立的actor（π_loco和π_arm），但一个统一的critic接收109维拼接观测，估计运动+操控奖励的组合价值。
  - 双critic架构：完全独立的两个分支。运动分支（actor π_loco + critic V_loco）观测57维信息（基座速度、投影重力、腿关节状态等），输出12维腿动作；手臂分支（actor π_arm + critic V_arm）观测52~55维信息（基座运动、腿上下文、臂关节状态、末端效应器/目标位置等），输出5维手臂残差动作。两个critic接收不相交的奖励信号（运动分支：速度跟踪+平衡；手臂分支：到达距离+位移）。
- **训练算法**：PPO，学习率3e-4（余弦退火），γ=0.99，λ=0.95，clip ratio=0.2，4096个并行环境。
- **顺序课程设计**：共13个等级（0~12），分四个阶段：
  - 0~4级：站立+抓取（目标位置阈值从0.12m降至0.06m，无方向要求）
  - 5~6级：行走+抓取（速度0~0.3m/s，位置阈值0.06→0.05m）
  - 7~8级：固定末端方向（手掌向下）
  - 9~12级：可变方向锥（张开角度20°~80°，速度0~0.6m/s，位置阈值0.05→0.04m）
  - 课程升级条件：持续有效到达率超过阈值。
- **反博弈奖励机制（仅用于S7变体）**：包括绝对工作空间采样、三条件有效到达验证（位置、位移、时间）、运动中心奖励、基于有效到达率的课程推进、博弈检测启发式。该变体使用双critic架构，冻结运动分支，重新初始化手臂策略。

## 三、实验设计
- **评估设置**：标准化benchmark，所有策略在相同条件下评估（绝对目标采样、最小目标距离0.12m、位置阈值0.06m、位移阈值0.10m、超时150步、单环境、确定性动作）。评估分为站立模式和行走模式，各运行3000步。
- **对比方法**（三个策略）：
  - **S6u（统一critic）**：统一critic（109维），52维手臂观测，12维手臂动作，课程等级10/12。
  - **S6s（双critic）**：双actor-critic，52维手臂观测，5维手臂动作，课程等级12/12。
  - **S7（双critic+反博弈）**：双critic加反博弈奖励机制，冻结运动策略，新初始化手臂策略，课程等级7/7。
- **评估指标**：有效到达率、位置仅到达率、平均到达时间、每千步有效到达次数、超时率、平均位移、手臂动作幅度等。
- **数据集/场景**：在仿真环境中随机采样目标位置，覆盖站立和行走两种模式，目标方向从无到变锥。

## 四、资源与算力
- 实验平台：NVIDIA Isaac Lab，4096个并行环境。
- GPU：单个RTX 5070 Ti（12GB VRAM），每秒约17,000个模拟步。
- 训练时长：文中未明确给出具体小时数，仅说明训练过程中课程达到不同等级（S6u到10级，S6s到12级，S7到7级）。可推断训练时间在数小时内。
- 未提及使用的CPU、内存等资源。

## 五、实验数量与充分性
- 共三个策略对比（S6u、S6s、S7），每个策略在站立和行走两种模式下各评估一次（共6次评估？实际表II给出站立和行走两行结果，但未说明多次重复）。
- 实验**不够充分**：
  - 仅采用单一种子（single-seed training），缺乏统计显著性分析。
  - 未做消融实验分离动作维度与critic架构的混淆（S6u使用12维手臂动作，S6s使用5维，作者也承认这一混淆）。
  - 仅比较了统一与双critic两种架构，未探索更多critic数量（如三个）。
  - 评估仅基于仿真，未进行真实机器人验证。
- 尽管如此，对比方法在相同评估条件下进行，且验证了检查点加载（位精确权重匹配），确保了比较的客观性。

## 六、论文的主要结论与发现
1. **Critic架构决定到达效率**：双critic策略相比统一critic，到达速度快3.5倍（6.5步 vs 22.6步），吞吐量高2倍（14.3 vs 7.0次/千步），有效到达率提高11个百分点（65.2% vs 53.8%）。
2. **反博弈奖励机制无额外收益**：加入反博弈机制的双critic变体（S7）性能反而略低于纯双critic（60.9% vs 65.2%），差异可能源于S7训练步数更少（课程等级7 vs 12）。
3. **训练指标无法反映效率差异**：统一critic的课程等级、累计到达次数、奖励值看似与双critic相当，但实际效率差距很大，只有通过标准化评估（时间到到达、吞吐量）才能揭示。
4. **对模仿学习+RL微调的启示**：统一critic可能通过竞争性梯度抑制预训练的操控行为（手臂动作幅度仅为1.22 vs 2.54），而双critic可自然保护已学技能。

## 七、优点
- **聚焦于一个被忽视的设计维度**：critic架构通常不是人形机器人RL研究的焦点，本文系统地揭示了其重要性。
- **标准化的评估方法论**：使用统一benchmark（相同采样、阈值、超时、确定性动作），使得不同架构可直接比较。
- **课程学习设计合理**：从静止到行走、从无方向到变方向，逐步增加难度，有助于学习稳定策略。
- **发现反博弈奖励的无效性**：提示在架构问题解决后，奖励工程的影响力有限，这一发现具有实用指导价值。
- **计算效率高**：单GPU（RTX 5070 Ti）即可完成训练，门槛较低。

## 八、不足与局限
- **仿真环境局限**：未进行sim-to-real迁移，结果仅适用于Isaac Lab仿真，真实机器人上的行为可能不同。
- **单种子训练**：缺乏多次重复实验，统计可靠性存疑。结果可能受随机种子影响。
- **混淆因素**：统一critic策略（S6u）使用12维手臂动作，双critic策略（S6s）使用5维，动作维度的差异未被隔离，无法完全归因于critic架构。
- **手臂自由度有限**：仅控制右臂5个关节，手腕和手指固定，未实现完整的灵巧操作。
- **未探索更多变体**：例如三重critic（双腿+双臂）、共享部分观测的critic等。
- **课程等级不一致**：S6u等级10，S6s等级12，S7等级7，训练步数不同，可能影响比较公平性（尤其对于S7）。
- **未与现有最强方法比较**：没有和HOVER、ULC等工作对比，缺乏整体性能基线。
- **单一机器人平台**：仅测试了Unitree G1，结论的泛化性待验证。

（完）
