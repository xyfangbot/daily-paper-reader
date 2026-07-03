---
title: Planning-aligned Token Compression for Long-Context Autonomous Driving
title_zh: 面向长上下文自动驾驶的规划对齐令牌压缩
authors: "Zhixuan Liang, Yuxiao Chen, Yurong You, Péter Karkus, Wenhao Ding, Boyi Li, Alexander Popov, Yan Wang (15435), Maximilian Igl, Yiming Li, Danfei Xu, Nikolai Smolyanskiy, Boris Ivanovic, Ping Luo, Marco Pavone"
date: 2026-06-05
pdf: "https://arxiv.org/pdf/2606.07464"
tags: ["query:热点论文筛选", "query:综合方向", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=lead-affiliation; institutions=Nvidia (United Kingdom), University of Hong Kong; query=generalist robot policy"
tldr: "针对单块视觉-动作模型处理长上下文时token超实时预算的问题，现有基于规则的压缩与规划解耦易丢失关键信息。提出COMPACT-VA，采用条件VQ-VAE将历史上下文压缩为有界表示，并通过学习规划意图对齐压缩与决策。在高信号动态场景下，以可比token预算实现成功率提升超6%（达68.3%），并保持3.3倍加速与2.7倍内存缩减。该规划对齐的压缩范式在确保行为正确性的同时显著提升效率。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有token压缩方法采用规则启发式（如时间衰减），与规划解耦，导致决策关键信息丢失，影响长上下文驾驶行为正确性。
method: 提出COMPACT-VA，基于条件VQ-VAE的规划对齐工作记忆框架，利用历史轨迹和未来轨迹提炼的规划意图作为压缩条件，端到端优化策略。
result: "在可比token预算下，成功率提升超6%（达68.3%），各项行为指标一致提升；闭环评估实现3.3倍速度提升和2.7倍内存减少。"
conclusion: 规划对齐的token压缩在保留决策关键信息的同时大幅提升效率，验证了耦合压缩与规划的可行性。
---

## 摘要
单体视觉-动作模型代表了自动驾驶领域的一种新兴范式。然而，当为复杂交互编码扩展的时间上下文时，这种架构产生的令牌序列会迅速超出实时计算预算。虽然线性变换器和外部记忆等方法试图使上下文轻量化，但令牌压缩与架构的兼容性最佳，因为它不需要修改骨干网络。然而，现有的压缩采用基于规则的启发式方法，如时间衰减，与规划解耦，可能导致决策关键信息的丢失。我们提出COMPACT-VA，一种基于条件VQ-VAE的规划对齐工作记忆框架，将扩展上下文压缩为有界表征。压缩同时基于历史轨迹和一种学习的规划意图——后验编码器在训练期间从未来轨迹中提炼出该意图，而先验编码器则学习从压缩的观测中预测它。压缩的记忆与预测的潜变量拼接，馈送给策略进行端到端优化，从而在保留决策关键信息的情况下进行规划。我们在历史上下文对行为正确性最为关键的高信号动态场景（例如，停车、让行或前进）上进行评估，并相应设计了行为指标。在相当的令牌预算下，我们在成功率上实现了超过6%的提升（68.3%），且各指标持续增益。消融实验验证了规划对齐耦合的有效性。闭环评估证实，与未压缩处理相比，COMPACT-VA以3.3倍加速和2.7倍内存缩减保持了通用驾驶性能。

## Abstract
Monolithic vision-action models represent an emerging paradigm in autonomous driving. However, this architecture produces token sequences that quickly exceed real-time computational budgets when encoding extended temporal context for complex interactions. While approaches like linear transformers and external memory try to make the context lightweight, token compression is most compatible with the architecture as it requires no backbone modifications. Yet existing compression adopts rule-based heuristics like temporal decay, decoupled from planning, risking loss of decision-critical information. We propose COMPACT-VA, a planning-aligned working memory framework built on conditional VQ-VAE, compressing extended context into bounded representations. Compression is conditioned on both historical trajectory and a learned planning intent that the posterior encoder distills from future trajectories during training, while the prior encoder learns to predict it from compressed observations. The compressed memory, concatenated with the predicted latent, feeds the policy for end-to-end optimization, planning with retained decision-critical information. We evaluate on high-signal dynamic scenarios where historical context is most critical for behavior correctness (e.g., stop, yield, or proceed), and accordingly design behavioral metrics. Under comparable token budgets, we achieve $>$6% improvement (68.3%) on success rates with consistent gains across metrics. Ablations validate planning-aligned coupling effectiveness. Closed-loop evaluation confirms that COMPACT-VA maintained general driving performance with 3.3* speedup and 2.7* memory reduction over uncompressed processing.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：单体视觉-动作（VA）模型是自动驾驶的新范式，但处理长历史上下文（例如5-10秒的观测）时，令牌序列长度激增，超出实时计算预算。现有解决方案如线性Transformer或外部记忆模块改变骨架架构，而令牌压缩虽兼容性最好，但采用基于规则的启发式（如时间衰减）与规划解耦，可能丢弃对决策至关重要的历史信息。
- **整体含义**：提出一种**规划对齐的令牌压缩框架**，使压缩过程明确耦合驾驶规划目标，学习保留决策关键信息而非盲目丢弃，从而在有限令牌预算下实现更优的行为正确性，同时提升计算效率。

## 二、论文提出的方法论
- **核心思想**：基于条件变分自编码器（cVAE）和向量量化（VQ）构建规划对齐工作记忆。通过将历史观测压缩为有界表示，并学习一个反映“驾驶意图”的离散潜变量，该潜变量在训练时由未来轨迹蒸馏（后验编码器），在推理时仅由压缩观测预测（先验编码器）。策略以压缩记忆与预测的意图潜变量为输入，端到端优化。
- **关键技术细节**：
  1. **骨架**：采用统一VA策略（Alpamayo变体），视觉编码器、因果Transformer骨干、轨迹解码器。
  2. **层次化压缩**：构建K层FIFO记忆库。近期帧保持高令牌密度（无压缩），中层适度压缩，远层强压缩。每层使用Q-Former模块，通过可学习的查询令牌与原始观测、时间/相机嵌入进行自注意力，输出压缩令牌。总令牌数从原始6400降为1424（4.5倍压缩）。使用旋转位置编码并按压缩比缩放频率。
  3. **规划对齐变分压缩**：
     - **后验编码器**（仅训练）：输入未来轨迹→MLP压缩为令牌→小Transformer输出高斯分布参数，采样得到潜变量zq。
     - **先验编码器**（训练和推理）：输入压缩观测→注意力池化→MLP输出高斯分布，采样得到zp。
     - **向量量化**：zq和zp映射到共享离散码本，通过直通估计器保持梯度流，加入承诺损失。
     - **策略输入**：将量化后的意图潜变量z_skill作为特殊令牌，与压缩记忆、历史轨迹令牌拼接，送入Transformer解码器。
  4. **端到端训练损失**：L = L_traj + λ_KL · KL散度 + λ_commit · L_commit。KL散度驱动先验分布匹配后验，迫使压缩保留能预测未来意图的信息。
- **算法流程**：训练时，模型压缩观测→先验采样→量化→与压缩记忆拼接→策略预测轨迹；同时后验从未来轨迹提取意图，通过KL散度约束先验。推理时，仅运行先验通路。

## 三、实验设计
- **数据集与场景**：
  - 基于NVIDIA Alpamayo物理AI数据集（自动驾驶）。
  - 专门聚焦**高信号动态场景**：四向停车、动态遮挡、无保护左转。这些场景中，历史上下文（5-10秒）直接决定离散决策正确性（停车、让行或前进）。
  - 从数据集中筛选16%的样本——轨迹包含减速至静止并再次加速（表明成功完成决策）。保留20,000个20秒长的验证clip（每clip 200帧，10Hz；决策点在第50帧）。
- **Benchmark与对比方法**：
  - 标准Alpamayo（1s/8帧/1280令牌）
  - 稀疏长历史（5s/8帧/1280令牌）
  - 密集长历史（5s/40帧/6400令牌，无压缩）
  - 无规划对齐的压缩（5s/40帧/1424令牌）
  - COMPACT-VA离散版和连续版（5s/40帧/1424令牌）
- **行为指标**（而非传统minADE）：停车成功率、前进成功率、滑行率、停车位置误差、停车时长误差。
- **闭环评估**：在Alpasim模拟器（基于神经重建）上对910个多样化场景（通用驾驶）评估，对比基线（2s/18帧）。测量平均速度、碰撞率、违规等。

## 四、资源与算力
- 论文**未明确说明**使用的GPU型号、数量、训练时长等具体算力信息。仅提到推理时间测试在NVIDIA A100上，但未提供训练资源细节。

## 五、实验数量与充分性
- **实验数量**：
  - 开环主实验：表I，对比5种方法，每种报告均值±标准差（多次运行）。
  - 闭环评估：表II。
  - 消融实验：表IV（架构组件）、表V（不同压缩率）、表VI（历史长度）。
  - 额外分析：VQ码本利用率、定性示例（图4）。
- **充分性与公平性**：
  - 对比方法设置一致（相同历史长度、相同推理预算）。
  - 行为指标专为决策正确性设计，比传统minADE更相关。
  - 消融实验逐步验证各组件贡献，逻辑清晰。
  - 闭环评估在通用场景验证，避免过拟合到特定记忆场景。
  - **不足**：仅在一个数据集（Alpamayo）上评估；码本大小（K=20）和层次结构未进行系统超参搜索；未与基于线性Transformer或外部记忆的最新方法（如Mamba、MemoryVLA）比较。

## 六、论文的主要结论与发现
- 在可比令牌预算下，COMPACT-VA的**前进成功率**达68.3%（基线最佳62-64%），提升超6%；**滑行率**降低22%；停车时长误差减小。
- 规划对齐压缩（COMPACT-VA）相比无规划对齐压缩，性能提升2.7%—证明耦合规划目标的必要性。
- 闭环评估中，保持与基线相当的通用性能，同时实现**3.3倍推理加速**和**2.7倍内存缩减**（对比无压缩5s历史）。
- VQ码本利用率达80%（15-17/20个技能激活），表明模型学习到有意义的离散驾驶意图。
- 较长的历史（5s）普遍优于短历史（1s），但帧数过多可能退化性能（64.6%→61.9%），说明压缩和结构化记忆至关重要。

## 七、优点
1. **规划对齐压缩的新颖性**：首次将令牌压缩与驾驶规划目标通过cVAE框架显式耦合，避免规则启发式的盲目性。
2. **行为指标创新**：针对决策正确性（停车/前进成功率等）而非传统轨迹精度，更贴合安全关键场景。
3. **层次化压缩设计**：近期细粒度、远期粗粒度，结合学习查询，在压缩率和信息保留间取得平衡。
4. **端到端轻量性**：不需要修改骨干网络，兼容现有统一VA架构；推理时仅增加一次前向传播，计算开销小。
5. **实验验证全面**：含开环主实验、闭环通用性能、多组消融、码本利用率分析，结果有统计意义。
6. **兼具效率提升**：在改善决策的同时显著加速和降低内存，实际部署价值高。

## 八、不足与局限
1. **数据集单一**：仅使用Alpamayo数据集，未在Waymo、nuScenes等公开基准上验证，泛化性存疑。
2. **场景覆盖有限**：重点测试停车/让行交叉口，未涵盖高速、变道、合并等需长期依赖的场景，也未包含极端噪声或遮挡。
3. **缺乏与替代压缩方法的对比**：未比较ToMe、StreamingLLM、Mamba等流行高效架构或记忆模块（如Transformer-XL、Titans），相对竞争力证据不足。
4. **超参未充分优化**：码本大小（K=20）、层次数（K=3）、层分配等固定值，未进行系统搜索。
5. **资源与训练细节缺失**：未报告GPU型号、数量、训练时长、总计算量，可复现性受影响。
6. **潜在偏差**：仅筛选16%含明确停车-加速模式的样本，模型可能偏向该类场景，对无明确二元决策的场景适应性未知。
7. **闭环模拟局限性**：Alpasim模拟器基于神经重建，可能无法完美再现复杂交互，闭环结果的真实推广需谨慎。

（完）
