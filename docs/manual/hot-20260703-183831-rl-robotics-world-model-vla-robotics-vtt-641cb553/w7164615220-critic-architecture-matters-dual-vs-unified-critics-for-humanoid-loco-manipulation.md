---
title: "Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation"
title_zh: 评论家架构的重要性：用于人形机器人移动操作的双评论家与统一评论家
authors: Mehmet Turan Yardımcı
date: 2026-06-10
pdf: "https://arxiv.org/pdf/2606.11891"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 人形机器人多目标强化学习需协调运动与操作，评论家架构设计常被忽视。本文在Unitree G1上对比统一与分离评论家，通过13级课程训练策略。双评论家策略在到达速度、吞吐量和成功率上显著优于统一评论家。结果表明评论家架构是核心设计选择，其影响超过奖励工程。
source: openalex
selection_source: hot_paper_scout
motivation: 探究不同评论家架构对多目标人形机器人强化学习策略效果的影响。
method: 在Unitree G1人形机器人上通过13级顺序课程训练，比较统一评论家和分离评论家两种架构。
result: "双评论家策略到达速度提升3.5倍，吞吐量提高2倍，成功率达65.2%对53.8%。"
conclusion: 评论家架构是比奖励工程更关键的优化杠杆，直接影响多目标协调效率。
---

## 摘要
针对人形机器人的多目标强化学习必须在单一策略中协调移动和操作。一个自然的设计选择是使用单个（统一）评论家来估计所有目标的组合价值，还是使用具有不相交奖励信号的独立（双）评论家。我们在NVIDIA Isaac Lab中的Unitree G1人形机器人（23个主动自由度）上进行了受控比较，通过一个从静止抓取到具有可变方向目标的行走的13级顺序课程训练移动操作策略。在标准化评估中，与统一评论家策略相比，双评论家策略达到目标的速度快3.5倍（6.5步对比22.6步），吞吐量高2倍（每1000步有效抓取14.3次对比7.0次），并且有效抓取率更高（65.2%对比53.8%）。值得注意的是，额外的反博弈奖励机制在仅改变架构的基础上并未带来进一步提升（60.9%对比65.2%）。这些结果对新兴的基于模仿学习的策略的强化学习微调范式有直接影响：当使用强化学习微调预训练的操作策略时，统一评论家可能通过竞争性的移动梯度抑制已学到的行为。这些发现表明，评论家架构是多目标人形机器人强化学习中一个主要且常被忽视的设计选择，其对抓取效率的影响大于奖励工程。

## Abstract
Multi-objective reinforcement learning for humanoid robots must coordinate locomotion and manipulation within a single policy. A natural design choice is whether to use a single (unified) critic that estimates the combined value of all objectives, or separate (dual) critics with disjoint reward signals. We present a controlled comparison on the Unitree G1 humanoid (23 active DoF) in NVIDIA Isaac Lab, training loco-manipulation policies through a sequential curriculum spanning 13 levels from stationary reaching to walking with variable-orientation targets. In standardized evaluation, dual-critic policies reach targets 3.5$\times$ faster (6.5 vs. 22.6 simulation steps), achieve 2$\times$ higher throughput (14.3 vs. 7.0 validated reaches per 1,000 steps), and attain higher validated reach rates (65.2% vs. 53.8%) compared to the unified-critic policy. Notably, additional anti-gaming reward mechanisms provide no further improvement beyond the architectural change alone (60.9% vs. 65.2%). These results have direct implications for the emerging paradigm of RL fine-tuning of imitation-learned policies: when refining a pre-trained manipulation policy with RL, a unified critic risks suppressing the learned behavior through competing locomotion gradients. These findings demonstrate that critic architecture is a primary - and often overlooked - design choice in multi-objective humanoid RL, with greater impact than reward engineering on reaching efficiency.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 人形机器人需要同时协调运动（行走）和操作（抓取），即locomotion-manipulation（移动操作），这是一个基础但具有挑战性的多目标强化学习问题。
- 现有文献中，大多数工作直接采用单一策略或单一价值函数（统一评论家，unified critic）来估计所有目标的组合价值，而未讨论评论家架构（critic architecture）这一设计选择对策略性能的影响。
- 作者指出，评论家架构的选择直接影响多目标间的梯度协调机制：统一评论家可能因目标之间的竞争（如移动奖励主导早期训练）而抑制操作行为；而双评论家（dual critic）通过独立的奖励信号和价值函数，可以隔离不同目标的梯度信号，从而避免干扰。
- 该问题对于“模仿学习+RL微调”的混合范式尤为重要：当用RL微调从人类演示学到的操作策略时，统一评论家可能通过竞争性的移动梯度覆盖或抑制已学到的操作行为，导致灾难性遗忘。

## 二、论文提出的方法论
- **核心思想**：将人形机器人的移动操作任务分解为两个独立的强化学习分支——移动分支和手臂分支，每个分支拥有独立的演员（actor）和评论家（critic），且两个评论家接收不相交的奖励信号。
- **关键技术细节**：
  - **统一评论家（基线）**：使用单一评论家接收拼接后的109维观测（57维移动观察+52维手臂观察），估计移动奖励和操作奖励的组合价值。
  - **双评论家（提出的架构）**：移动分支（演员 + 评论家）输入57维状态，输出12个腿部关节目标；手臂分支（演员 + 评论家）输入52维（或55维，在加入反博弈特征时）状态，输出5个手臂关节残差动作。两个评论家分别基于各自分支的奖励信号（移动分支：速度跟踪和平衡；手臂分支：抓取距离和位移）进行学习。
  - **课程学习（Curriculum）**：设计13个难度级别（0~12），分为四个阶段：静止抓取（级别0-4）、行走+抓取（5-6）、固定末端执行器方向（7-8）、可变方向锥形区域（9-12，锥角从20°至80°）。课程升级条件为持续有效抓取率超过阈值。
  - **反博弈机制（anti-gaming）**：为了对比，设计了一个变体（S7），包含五种惩罚：绝对工作空间采样、三条件有效抓取验证（位置、位移、时间限制）、朝向目标的运动奖励、使用有效抓取率进行课程升级、游戏检测启发式。该变体采用双评论家架构，但冻结移动分支，从头初始化手臂策略。
- **算法流程**：使用PPO（Proximal Policy Optimization）进行训练，学习率3×10⁻⁴（余弦退火），γ=0.99，λ=0.95，裁剪比例0.2。

## 三、实验设计
- **仿真平台与机器人**：NVIDIA Isaac Lab仿真环境，Unitree G1人形机器人（23个主动自由度），12个腿部关节，5个手臂关节（右臂：肩部俯仰/横滚/偏航，肘部俯仰/横滚），手腕和手指关节固定。
- **并行环境**：4096个并行环境。
- **对比方法**：三种策略：
  - S6u（统一评论家）：统一109维评论家，52维手臂观测，12维手臂动作，课程级别10/12。
  - S6s（双评论家）：双演员-双评论家，52维手臂观测，5维手臂残差动作，课程级别12/12。
  - S7（双评论家+反博弈）：双评论家，但冻结移动分支，从头初始化手臂策略，加入五种反博弈机制，课程级别7/7。
- **评估指标**：对每个策略在3,000个仿真步骤中进行站立模式和行走模式下的标准化评估。指标包括：有效抓取率、仅按位置抓取率、平均到达时间（步骤数）、每1000步有效抓取次数、超时率、平均位移、手臂动作幅度。
- **评估设置**：绝对目标采样，最小目标距离0.12m，位置阈值0.06m，位移阈值0.10m，超时150步，确定性动作，单一环境。

## 四、资源与算力
- **GPU硬件**：NVIDIA RTX 5070 Ti（12GB VRAM）。
- **训练速度**：约17,000步/秒（在4096个并行环境下）。
- **训练时长**：原文未明确给出总训练时间（小时数），只提及训练过程按课程等级推进。评估阶段每个策略运行3,000步，但未给出完整训练的总步数或时间。
- **其他**：所有实验使用单GPU完成，未提及使用多GPU或多节点。

## 五、实验数量与充分性
- **实验数量**：主要进行了三个策略的对比（S6u、S6s、S7），每个策略在站立和行走两种模式下各评估一次（共3×2=6次基准测试）。此外，训练过程中包含了课程等级的推进、训练奖励的监控，但并未针对多种随机种子或重复实验进行报告。
- **充分性讨论**：
  - **优点**：实验设计直接对比了评论家架构这一变量，同时加入了反博弈机制的消融，结果清晰展示了架构差异带来的效率提升。
  - **不足**：仅进行了一次评估（单种子），缺乏统计显著性检验和多种子重复实验，因此无法排除随机性影响。此外，训练过程中的指标（奖励、课程等级、训练抓取次数）未能反映策略效率差异，评估仅基于3,000步的短期测试，可能不足以完全代表长期行为。
  - **公平性**：S6u和S6s在手臂动作维度上不同（12维vs 5维），作者承认这是一个混杂因素，但认为5维是12维的子集，评论家架构变化是最可能的原因。S7使用了冻结的移动分支和从头初始化的手臂策略，训练迭代次数较少（课程等级7 vs 12），因此与S6s的对比可能存在不公平。

## 六、论文的主要结论与发现
1. **评论家架构决定抓取效率**：双评论家策略相比于统一评论家，抓取速度快3.5倍（6.5步 vs 22.6步），吞吐量提高2倍（每1000步14.3次 vs 7.0次），有效抓取率提升11个百分点（65.2% vs 53.8%）。
2. **反博弈奖励机制无额外收益**：在双评论家基础上加入五种反博弈机制（S7）并未提升性能，反而略低于无反博弈的S6s（60.9% vs 65.2%），差异可能源于S7训练迭代较少。
3. **训练指标掩盖效率差异**：统一评论家策略的课程级别、训练奖励、抓取总次数等常规指标与双评论家策略相近，无法反映3.5倍的速度和2倍的吞吐量差异。因此需要标准化的时间-到达和吞吐量评估指标。
4. **对模仿学习+RL微调的启示**：双评论家架构通过梯度隔离可以保护预训练的操作行为不被移动梯度覆盖，这对防止IL+RL混合范式中灾难性遗忘至关重要。

## 七、优点
- **问题新颖且实用**：首次系统性地比较了人形机器人多目标RL中评论家架构的影响，指出这是常被忽视的关键设计选择。
- **实验设计简洁有力**：直接控制评论家架构变量（统一 vs 双），并加入反博弈机制的消融，清晰地证明了架构优于奖励工程。
- **课程学习设计**：13级课程由简到难，涵盖了从静止到移动、从固定方向到可变方向的完整任务谱系，提高了策略的泛化性和训练的稳定性。
- **对混合IL+RL范式的启示**：双评论家架构的梯度隔离机制为解决IL+RL微调中的灾难性遗忘提供了潜在解决方案，具有较高的应用价值。
- **评估方法创新**：提出了标准化基准测试（包括时间-到达、吞吐量等指标），揭示了训练指标无法反映的效率差异。

## 八、不足与局限
- **仅仿真实验**：所有实验在NVIDIA Isaac Lab仿真中进行，未进行真实机器人上的sim-to-real迁移验证，结果在真实场景下的鲁棒性未知。
- **单种子训练和评估**：未进行多次随机种子重复实验，无法评估结果的统计显著性和稳定性，存在因偶然性导致结论偏差的风险。
- **混杂变量**：统一评论家策略使用12维手臂动作空间，而双评论家策略使用5维残差动作，动作维度差异可能对性能有影响，无法完全归因于评论家架构。作者虽指出5维是12维的子集，但未做消融实验隔离该变量。
- **策略变体间训练不均衡**：S7使用了不同的课程等级（7/7）和冻结移动分支，与S6s（12/12, 完整训练）的训练条件不同，直接对比可能不公平。
- **评估时间短**：每个策略仅评估3,000步，可能不足以覆盖所有目标位置和场景变化，长期稳定性和泛化性未充分测试。
- **手臂控制自由度有限**：仅控制5个手臂关节（右臂），固定了手腕和手部，未扩展到29自由度双臂操作，结论的泛化性受限。
- **未系统分析奖励工程**：虽然对比了反博弈机制，但未深入分析不同奖励权重、奖励函数设计对双评论家性能的影响，反博弈机制的设置可能不够优化。
- **缺乏计算资源详细报告**：未提供训练总时间、总步数、GPU利用效率等信息，难以评估方法在实际部署中的计算成本。

（完）
