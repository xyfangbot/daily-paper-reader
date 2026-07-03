---
title: "Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation"
title_zh: 评论家架构的重要性：双评论家与统一评论家在人形机器人移动操控中的应用
authors: Mehmet Turan Yardımcı
date: 2026-06-10
pdf: "https://doi.org/10.48550/arxiv.2606.11891"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning for humanoid robot control and locomotion"
tldr: "人形机器人多目标强化学习需协调移动与操作，批评家架构是关键设计选择。本文在Unitree G1（23自由度）上通过13级顺序课程训练，对比统一批评家与双批评家。双批评家策略在触及速度（6.5 vs 22.6步）、吞吐量（14.3 vs 7.0次/千步）和验证成功率（65.2% vs 53.8%）上显著更优，额外反博弈奖励机制无进一步提升。结果表明批评家架构的影响力超越奖励工程，对模仿学习策略的RL微调具有重要启示。"
source: openalex
selection_source: hot_paper_scout
motivation: 探索人形机器人多目标强化学习中批评家架构对协调移动与操作性能的影响。
method: 在Unitree G1上使用13级顺序课程训练操作-移动策略，对比统一批评家与双批评家架构。
result: "双批评家策略达到目标快3.5倍，吞吐量高2倍，验证触及率65.2%显著高于统一批评家的53.8%。"
conclusion: 批评家架构是比奖励工程更关键的设计选择，对RL微调模仿策略有直接指导意义。
---

## 摘要
多目标强化学习在人形机器人中必须在一个策略内协调移动和操控。一个自然的设计选择是使用单个（统一）评论家来估计所有目标的组合价值，还是使用具有不相交奖励信号的单独（双）评论家。我们在NVIDIA Isaac Lab中对Unitree G1人形机器人（23个主动自由度）进行了受控比较，通过一个从静态到达至具有可变方向目标的行走的13个级别的顺序课程训练移动操控策略。在标准化评估中，与统一评论家策略相比，双评论家策略达到目标的速度快3.5倍（6.5 vs. 22.6仿真步），吞吐量高2倍（每1000步有效到达数14.3 vs. 7.0），并且有效到达率更高（65.2% vs. 53.8%）。值得注意的是，除了架构改变之外，额外的反博弈奖励机制并未带来进一步改进（60.9% vs. 65.2%）。这些结果对基于模仿学习策略的RL微调的新兴范式有直接影响：当使用RL微调预训练的操控策略时，统一评论家可能通过竞争性的移动梯度抑制已学习的行为。这些发现表明，评论家架构是多目标人形机器人RL中一个主要且常被忽视的设计选择，对达到效率的影响大于奖励工程。

## Abstract
Multi-objective reinforcement learning for humanoid robots must coordinate locomotion and manipulation within a single policy. A natural design choice is whether to use a single (unified) critic that estimates the combined value of all objectives, or separate (dual) critics with disjoint reward signals. We present a controlled comparison on the Unitree G1 humanoid (23 active DoF) in NVIDIA Isaac Lab, training loco-manipulation policies through a sequential curriculum spanning 13 levels from stationary reaching to walking with variable-orientation targets. In standardized evaluation, dual-critic policies reach targets 3.5$\times$ faster (6.5 vs. 22.6 simulation steps), achieve 2$\times$ higher throughput (14.3 vs. 7.0 validated reaches per 1,000 steps), and attain higher validated reach rates (65.2% vs. 53.8%) compared to the unified-critic policy. Notably, additional anti-gaming reward mechanisms provide no further improvement beyond the architectural change alone (60.9% vs. 65.2%). These results have direct implications for the emerging paradigm of RL fine-tuning of imitation-learned policies: when refining a pre-trained manipulation policy with RL, a unified critic risks suppressing the learned behavior through competing locomotion gradients. These findings demonstrate that critic architecture is a primary - and often overlooked - design choice in multi-objective humanoid RL, with greater impact than reward engineering on reaching efficiency.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 人形机器人多目标强化学习必须在一个策略内协调移动（locomotion）和操控（manipulation）两个目标。
- 关键设计选择：采用单个统一评论家（unified critic）估计所有目标的组合价值，还是采用分离的双评论家（dual critics）分别处理不同奖励信号。
- 现有研究往往聚焦于奖励工程（reward engineering），但评论家架构本身的影响常被忽视。作者认为评论家架构是影响多目标人形机器人RL性能的首要且常被忽略的设计选择。

## 二、论文提出的方法论
- 在NVIDIA Isaac Lab仿真环境中，使用Unitree G1人形机器人（23个主动自由度）进行受控对比实验。
- 训练策略：采用顺序课程（sequential curriculum），包含从静态到达（stationary reaching）到带可变方向目标行走的13个难度级别。
- 对比两组架构：
  - **统一评论家（unified critic）**：单个评论家网络估计所有目标的组合价值。
  - **双评论家（dual critics）**：两个分离的评论家，分别处理移动和操控的不相交奖励信号。
- 额外对比：在双评论家基础上增加反博弈奖励机制（anti-gaming reward mechanisms），验证是否进一步改善性能。
- 评估指标：达到目标所需仿真步数、每千步有效到达次数（吞吐量）、有效到达率。

## 三、实验设计
- 仿真平台：NVIDIA Isaac Lab。
- 机器人平台：Unitree G1人形机器人，23个主动自由度。
- 训练任务：移动-操控联合策略，通过13级顺序课程（从静态伸手到带方向目标行走）逐步训练。
- 对比方法：
  - 统一评论家策略。
  - 双评论家策略。
  - 双评论家策略 + 额外反博弈奖励机制。
- 评估基准：标准化评估，测量到达速度、吞吐量和到达率。
- 未提及使用外部标准benchmark数据集，而是自建课程任务。

## 四、资源与算力
- 论文未明确说明使用的GPU型号、数量、训练时长等算力资源信息。
- 仅提及在NVIDIA Isaac Lab仿真环境中进行实验，未提供具体硬件配置或训练耗时。

## 五、实验数量与充分性
- 主要对比了三组实验：统一评论家、双评论家、双评论家+反博弈奖励机制。
- 每组实验在13级课程上训练，并在标准化评估中报告关键指标。
- 实验设计为受控对比，控制除评论家架构外的其他因素（如课程、奖励、网络结构等）一致。
- 实验数量相对有限（仅三组条件），但采用了多级课程和多个独立指标，评估较为全面。
- 公平性：强调了“受控比较”，并指出额外反博弈奖励机制仅在双评论家基础上测试，未在统一评论家上测试该机制，可能存在不对称比较。
- 总体而言，实验设计清晰，但覆盖范围较窄（仅基于Unitree G1单一机器人、单一仿真环境、单一任务族）。

## 六、论文的主要结论与发现
- 双评论家策略相比统一评论家策略具有显著优势：
  - 达到目标速度快3.5倍（6.5 vs. 22.6仿真步）。
  - 吞吐量高2倍（每千步有效到达14.3 vs. 7.0）。
  - 有效到达率更高（65.2% vs. 53.8%）。
- 额外反博弈奖励机制并未在双评论家基础上提供进一步改进（60.9% vs. 65.2%），表明架构改变本身的效果更强。
- 评论家架构是比奖励工程更关键的设计选择。
- 对模仿学习策略的RL微调有直接启示：在微调预训练操控策略时，统一评论家可能通过竞争性的移动梯度抑制已学行为，而双评论家可避免此问题。

## 七、优点
- 关注了一个常被忽视的架构选择问题，揭示了评论家架构对多目标RL性能的决定性影响。
- 实验设计简洁直接，仅通过改变评论家数量即可获得显著性能提升，方法论易于复现。
- 使用真实机器人模型（Unitree G1）和成熟的仿真平台（NVIDIA Isaac Lab），具有现实参考价值。
- 通过13级顺序课程训练，提高了策略的泛化能力。
- 额外设计了反博弈奖励机制的消融实验，验证了架构改变本身的有效性。

## 八、不足与局限
- 算力资源未公开，难以评估实验的可复现性和资源需求。
- 仅使用单一机器人模型（Unitree G1）和单一仿真环境，结论的泛化性有限，需在更多人形机器人和真实物理环境上验证。
- 实验组数较少，仅有三种条件对比，缺少对评论家网络结构（如层数、宽度）或其他超参数的消融研究。
- 未涉及多目标奖励权重对架构选择的影响，也未探究双评论家架构下的奖励设计细节。
- 反博弈奖励机制仅在双评论家基础上测试，未在统一评论家基础上测试其效果，可能遗漏潜在交叉效应。
- 论文尚未正式发表（arXiv预印本，标注为ICRA 2026 Workshop论文），需经同行评审验证。

（完）
