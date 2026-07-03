---
title: "Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation"
title_zh: 评论家架构的重要性：双评论家与统一评论家在人形机器人行走-操作中的对比
authors: Mehmet Turan Yardımcı
date: 2026-06-10
pdf: "https://doi.org/10.48550/arxiv.2606.11891"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning for humanoid robot control and locomotion"
tldr: "人形机器人多目标强化学习需协调移动与操作，评论家架构是常被忽视的设计选择。本文在Unitree G1上通过13级课程训练对比统一与分离评论家，发现分离评论家策略达到目标速度提升3.5倍、吞吐量2倍、成功率65.2% vs 53.8%。额外奖励机制无进一步改进。结果表明评论家架构比奖励工程影响更大，对RL微调模仿学习策略具有直接启示。"
source: openalex
selection_source: hot_paper_scout
motivation: 多目标人形机器人RL中，评论家架构是常被忽视的关键设计选择，对协调移动与操作性能影响显著。
method: 在NVIDIA Isaac Lab中，对Unitree G1（23自由度）训练移动操作策略，通过13级课程比较统一评论家与分离评论家架构。
result: "分离评论家策略达到目标更快（6.5 vs 22.6步），成功率更高（65.2% vs 53.8%），额外反博弈奖励无改进。"
conclusion: 评论家架构比奖励工程对达到效率影响更大，对RL微调预训练操作策略有直接启示。
---

## 摘要
多目标强化学习需要在一个策略中协调行走和操作。自然的设计选择是使用单个（统一）评论家来估计所有目标的组合值，还是使用分离的（双）评论家并带有不重叠的奖励信号。我们在NVIDIA Isaac Lab中的Unitree G1人形机器人（23个主动自由度）上进行了受控比较，通过一个从静态到达变化方向目标的13级顺序课程训练了行走-操作策略。在标准化评估中，双评论家策略比统一评论家策略到达目标快3.5倍（6.5步 vs 22.6步），吞吐量高2倍（每1000步有效到达14.3次 vs 7.0次），并达到更高的有效到达率（65.2% vs 53.8%）。值得注意的是，额外的反博弈奖励机制在仅改变架构的基础上没有提供进一步改进（60.9% vs 65.2%）。这些结果对模仿学习策略的RL微调的新兴范式有直接影响：当使用RL微调预训练的操作策略时，统一评论家可能通过竞争的行走梯度抑制学习到的行为。这些发现表明，评论家架构是多目标人形机器人RL中一个主要的且经常被忽视的设计选择，对到达效率的影响比奖励工程更大。

## Abstract
Multi-objective reinforcement learning for humanoid robots must coordinate locomotion and manipulation within a single policy. A natural design choice is whether to use a single (unified) critic that estimates the combined value of all objectives, or separate (dual) critics with disjoint reward signals. We present a controlled comparison on the Unitree G1 humanoid (23 active DoF) in NVIDIA Isaac Lab, training loco-manipulation policies through a sequential curriculum spanning 13 levels from stationary reaching to walking with variable-orientation targets. In standardized evaluation, dual-critic policies reach targets 3.5$\times$ faster (6.5 vs. 22.6 simulation steps), achieve 2$\times$ higher throughput (14.3 vs. 7.0 validated reaches per 1,000 steps), and attain higher validated reach rates (65.2% vs. 53.8%) compared to the unified-critic policy. Notably, additional anti-gaming reward mechanisms provide no further improvement beyond the architectural change alone (60.9% vs. 65.2%). These results have direct implications for the emerging paradigm of RL fine-tuning of imitation-learned policies: when refining a pre-trained manipulation policy with RL, a unified critic risks suppressing the learned behavior through competing locomotion gradients. These findings demonstrate that critic architecture is a primary - and often overlooked - design choice in multi-objective humanoid RL, with greater impact than reward engineering on reaching efficiency.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 研究动机：人形机器人多目标强化学习需要在一个策略中协调行走（locomotion）和操作（manipulation），但奖励信号和值函数估计的设计选择常被忽视。核心问题是：应该使用单个统一评论家（unified critic）来估计所有目标的组合值，还是使用分离的双评论家（dual critics）为每个目标分配独立的奖励信号？
- 背景：现有模仿学习策略通过RL微调时，统一评论家可能因竞争的行走梯度抑制已学到的操作行为，导致性能下降。论文强调评论家架构本身是一个首要但经常被忽略的设计选择，其对任务效率的影响可能超过奖励工程。

## 二、论文提出的方法论
- 核心思想：在PPO框架下，对比两种评论家架构——统一评论家（单网络输出所有目标的联合值）和双评论家（两个独立网络分别估计行走和操作的值函数，但共享一个策略网络）。
- 关键技术细节：
  - 使用Unitree G1人形机器人（23个主动自由度）在NVIDIA Isaac Lab中训练。
  - 采用13级顺序课程（curriculum）训练行走-操作策略：从静止到达（stationary reaching）逐步过渡到行走中追逐可变朝向目标。
  - 奖励信号：双评论家中，行走和操作使用不重叠的奖励；统一评论家则将所有奖励加权求和。
- 额外实验：针对统一评论家引入了“反博弈奖励机制”（anti-gaming reward），试图抑制策略对单一目标的过度优化，以评估奖励工程能否弥补架构缺陷。

## 三、实验设计
- 评估场景：在模拟环境中，Unitree G1机器人执行到达任务，目标位置和朝向随机变化，机器人需在行走中完成操作。
- Benchmark：未使用外部公开数据集，而是自建标准化评估流程——在固定时间窗口内统计有效到达次数、到达速度、到达率。
- 对比方法：
  - 双评论家策略（Dual-critic）
  - 统一评论家策略（Unified-critic）
  - 统一评论家+反博弈奖励（Unified + anti-gaming）
- 评估指标：到达目标所需模拟步数（steps）、每1000步有效到达次数（throughput）、验证到达率（validated reach rate）。

## 四、资源与算力
- 论文中未明确说明使用的GPU型号、数量及训练时长。仅提到训练在NVIDIA Isaac Lab仿真环境中进行，未提供具体硬件配置和训练时间。

## 五、实验数量与充分性
- 实验组数：主要进行了三组对比实验（双评论家、统一评论家、统一+反博弈），每组在13级课程下训练，并在标准化评估中报告了关键指标。
- 充分性：实验设计较为清晰，控制变量（仅评论家架构不同），且包含了奖励工程的消融。但存在以下限制：
  - 仅测试了单一机器人平台（Unitree G1）和单一任务（到达）。
  - 未评估其他多目标RL架构（如分开策略网络、共享评论家等）。
  - 未在真实机器人上验证。
- 客观公平性：评估步骤和指标标准化，但可能因随机种子和超参数调优引入偏差。论文未报告多次运行的平均值和方差，削弱了统计显著性。

## 六、论文的主要结论与发现
- 双评论家策略在到达速度上比统一评论家快3.5倍（6.5步 vs 22.6步），吞吐量高2倍（14.3 vs 7.0次/千步），验证到达率更高（65.2% vs 53.8%）。
- 额外反博弈奖励机制并未带来进一步改善（60.9% vs 65.2%），说明架构变化本身比奖励工程对效率的提升更关键。
- 对RL微调模仿学习策略的启示：使用统一评论家微调预训练操作策略时，行走梯度可能干扰已学行为，导致性能退化；双评论家通过分离梯度更新可以避免该问题。
- 结论：评论家架构是多目标人形机器人RL中首要且被忽视的设计选择，其影响大于奖励工程。

## 七、优点
- 实验聚焦于一个特定但重要的设计变量（评论家架构），控制严谨。
- 提出了13级课程训练，逐步增加任务难度，有助于稳定学习。
- 包含了反博弈奖励的消融实验，有力证明了架构的支配性。
- 结果对实际应用（如人形机器人操作任务的RL微调）有直接指导意义。
- 论文简洁（仅4页），但信息密度高，结论清晰。

## 八、不足与局限
- 仅基于仿真实验，未在真实机器人上验证，泛化性存疑（Sim-to-Real gap）。
- 仅评估了单一任务（到达）和单一机器人（Unitree G1），结论是否适用于其他机器人（如双足、轮式）或其他操作任务（如抓取、推动）未知。
- 未报告多次实验的统计量（均值、方差），无法判断结果的稳定性。
- 未提供详细超参数、网络结构、训练时长和计算资源，可复现性受限。
- 未讨论双评论家可能带来的计算开销或训练不稳定问题。
- 缺乏与其他多目标RL方法（如基于回报加权、分层强化学习）的对比。

（完）
