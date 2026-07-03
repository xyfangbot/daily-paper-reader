---
title: Planning-aligned Token Compression for Long-Context Autonomous Driving
title_zh: 面向规划一致的长上下文自动驾驶令牌压缩
authors: "Zhixuan Liang, Yuxiao Chen, Yurong You, Péter Karkus, Wenhao Ding, Boyi Li, Alexander Popov, Yan Wang (15435), Maximilian Igl, Yiming Li, Danfei Xu, Nikolai Smolyanskiy, Boris Ivanovic, Ping Luo, Marco Pavone"
date: 2026-06-05
pdf: "https://arxiv.org/pdf/2606.07464"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=lead-affiliation; institutions=Nvidia (United Kingdom), University of Hong Kong; query=generalist robot policy"
tldr: "长上下文自动驾驶中，视觉-动作模型产生过长token序列，导致实时计算不足。现有规则基压缩与规划脱节，丢失关键信息。本文提出COMPACT-VA，通过条件VQ-VAE将规划意图与历史轨迹结合指导压缩，保留决策所需信息。在动态场景测试中，成功率提升超6%至68.3%，同时实现3.3倍加速和2.7倍内存减少，验证了规划对齐压缩的有效性。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有令牌压缩采用与规划脱节的规则启发式，易丢失决策关键信息，需设计规划对齐的压缩方法。
method: 基于条件VQ-VAE的规划对齐工作记忆框架，以历史轨迹和学习到的规划意图为条件，将长上下文压缩为紧致表示。
result: "在行为关键动态场景中，成功率提升6%以上（68.3%），速度提升3.3倍，内存减少2.7倍，指标全面增益。"
conclusion: 规划对齐的令牌压缩有效保留决策关键信息，显著提升长上下文自动驾驶的计算效率与性能。
---

## 摘要
单一视觉-行动模型代表了自动驾驶领域的一种新兴范式。然而，当为复杂交互编码扩展的时间上下文时，这种架构产生的令牌序列会迅速超出实时计算预算。虽然线性变换器和外部记忆等方法试图使上下文轻量化，但令牌压缩与架构兼容性最高，因为它无需修改主干网络。然而，现有压缩采用基于规则的启发式方法（如时间衰减），与规划脱节，可能导致决策关键信息的丢失。我们提出COMPACT-VA，一种基于条件VQ-VAE的面向规划的工作记忆框架，将扩展的上下文压缩为有界表示。压缩同时以历史轨迹和学习到的规划意图为条件，后验编码器在训练期间从未来轨迹中提炼出该意图，而先验编码器则学习从压缩观测中预测它。压缩记忆与预测的潜在表示拼接后，用于策略的端到端优化，从而在规划中保留决策关键信息。我们在高信号动态场景（此时历史上下文对行为正确性最为关键，例如停车、让行或前行）下进行评估，并相应设计了行为指标。在可比令牌预算下，我们在成功率上实现了超过6%的提升（68.3%），各项指标持续增长。消融实验验证了面向规划耦合的有效性。闭环评估证实，与未压缩处理相比，COMPACT-VA以3.3倍加速和2.7倍内存缩减保持了通用驾驶性能。

## Abstract
Monolithic vision-action models represent an emerging paradigm in autonomous driving. However, this architecture produces token sequences that quickly exceed real-time computational budgets when encoding extended temporal context for complex interactions. While approaches like linear transformers and external memory try to make the context lightweight, token compression is most compatible with the architecture as it requires no backbone modifications. Yet existing compression adopts rule-based heuristics like temporal decay, decoupled from planning, risking loss of decision-critical information. We propose COMPACT-VA, a planning-aligned working memory framework built on conditional VQ-VAE, compressing extended context into bounded representations. Compression is conditioned on both historical trajectory and a learned planning intent that the posterior encoder distills from future trajectories during training, while the prior encoder learns to predict it from compressed observations. The compressed memory, concatenated with the predicted latent, feeds the policy for end-to-end optimization, planning with retained decision-critical information. We evaluate on high-signal dynamic scenarios where historical context is most critical for behavior correctness (e.g., stop, yield, or proceed), and accordingly design behavioral metrics. Under comparable token budgets, we achieve $>$6% improvement (68.3%) on success rates with consistent gains across metrics. Ablations validate planning-aligned coupling effectiveness. Closed-loop evaluation confirms that COMPACT-VA maintained general driving performance with 3.3* speedup and 2.7* memory reduction over uncompressed processing.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：在长上下文自动驾驶中，单一视觉-动作（VA）或视觉-语言-动作（VLA）模型将全部历史直接编码为观察令牌序列，导致令牌数量急剧增长，超出实时计算预算（注意力O(N²)成本不可控）。现有令牌压缩方法（如基于时间衰减的规则启发式）简单丢弃远距离帧，与规划目标脱节，容易丢失决策关键信息（如交叉路口车辆到达顺序）。
- **整体含义**：需要在令牌预算约束下，通过学习方式保留对规划（如停车、让行、前行）至关重要的历史信息，同时保持与原始VA架构的兼容性。本文提出**规划对齐的压缩**，将压缩质量与轨迹预测性能直接耦合，实现端到端学习任务相关的记忆保留。

## 二、论文提出的方法论
- **核心思想**：基于条件VQ-VAE构建**工作记忆机制**。通过一个正则化变分目标，迫使压缩模块保留足以正确预测驾驶意图的历史信息；将驾驶意图表示为离散潜在变量，作为特殊令牌输入策略。
- **关键技术细节**：
  - **分层FIFO缓冲**：将历史帧组织为K个压缩层，最近层保留完整令牌分辨率（无压缩），中间层适度压缩，远层激进压缩。采用Q-former（可学习查询令牌）从各层观察中聚合特征，基于自注意力生成压缩令牌。
  - **规划对齐变分压缩**：
    - **后验编码器（Q-net）**：仅在训练时使用，从未来轨迹提炼驾驶意图潜在分布（高斯），采样后经VQ量化得到离散技能嵌入。
    - **先验编码器（P-net）**：训练和推理时使用，从压缩观察中预测该潜在分布，通过KL散度约束匹配后验。
    - **向量量化（VQ）**：将潜在映射到共享码本（大小K=20），使用直通估计器传递梯度。
  - **策略输入构成**：离散技能嵌入作为特殊令牌，与压缩记忆、历史轨迹令牌、位置编码拼接，输入统一Transformer主干（Alpamayo架构），自回归预测未来轨迹令牌。
  - **端到端优化损失**：L = L_traj + λ_KL · D_KL(q_ϕ||p_θ) + λ_commit · L_commit。训练时策略条件来自先验采样，保证训练-推理一致。
- **算法流程**：训练时，多视角历史图像→视觉编码器→原始观察令牌→Q-former压缩（条件含历史轨迹）→先验编码器预测潜在→后验编码器从未来轨迹提取真实潜在→KL散度约束→VQ离散化→拼接后输入策略→预测轨迹→交叉熵损失。推理时仅走先验路径，不依赖未来。

## 三、实验设计
- **数据集与场景**：使用**Alpamayo物理AI数据集**（NVIDIA提供，含1727+小时多模态驾驶数据，覆盖25个国家2500+城市）。专门筛选**高信号动态场景**（记忆依赖严重）：四向停车交叉口、动态遮挡停车/让行、无保护转弯。这些场景中正确行为取决于离散决策（停或走）而非轨迹平滑度。
- **Benchmark与评价指标**：
  - **行为指标**：停止成功率（Stop SR）、前进成功率（Go SR，主要指标）、滚行通过率（Roll-through Rate，越低越好）、停止位置误差、停止时长误差。拒绝采用传统minADE（与决策正确性不匹配）。
  - **开放环路评估**：在记忆依赖子集上，从数据集中提取20000个20秒样本（10Hz，关键决策点在第50帧），训练专用模型。
  - **闭环评估**：在Alpasim模拟器上使用910个通用驾驶场景，验证一般驾驶能力（碰撞、偏离道路、计划偏差等）。
- **对比方法**：
  - 标准Alpamayo（1秒/8帧，1280令牌）
  - 稀疏长历史（5秒/8帧，1280令牌）
  - 密集长历史（5秒/40帧，6400令牌，无压缩）
  - 无规划对齐压缩（5秒/40帧，1424令牌，但无cVAE耦合）
  - COMPACT-VA离散版/连续版（5秒/40帧，1424令牌）
- **实现细节**：T=20步（5秒，4Hz），Ncam=2，Nimg=160令牌/图。分层压缩：层1（4帧，1×）、层2（5帧，16×）、层3（11帧，80×），总Ncompressed=1424（4.5×缩减）。潜在维度dz=32，码本大小K=20，停止速度阈值0.5m/s。

## 四、资源与算力
- 文中未明确说明训练所用的GPU型号、数量及训练时长。
- 仅在推理效率评估中提到：在NVIDIA A100 GPU上测量推理时间和峰值GPU内存，该部分用于计算加速比和内存缩减。因此，训练算力细节缺失。

## 五、实验数量与充分性
- **实验数量**：充分且系统。
  - 主要结果（表I）对6种方法进行对比，在每个指标上报告均值和标准差（多次运行）。
  - 闭环评估（表II）比较两种设置下9个指标。
  - 消融实验四组：架构组件（表IV，5种变体）、压缩率（表V，7种配置）、历史长度（表VI，4种长度）、技能利用率分析（稳定码本利用率15-17/20）。
  - 效率对比（表III）给出时间/内存统计。
- **充分性与公平性**：
  - 所有方法在同一数据集、相同训练流程下比较，令牌预算尽量对齐（1424 vs 1280），公平性好。
  - 行为指标专门设计，避免minADE的偏差，评价更客观。
  - 闭环验证确保通用驾驶能力未退化。
- **不足**：仅在一个数据集（Alpamayo）上测试，缺乏跨数据集或真实世界的验证；记忆依赖场景仅占数据集16%，可能无法完全代表所有长上下文需求。

## 六、论文的主要结论与发现
- 规划对齐的令牌压缩（COMPACT-VA）在可比令牌预算下，将前进成功率从62.0%提升至68.3%（+6.3%绝对提升），滚行通过率降低22%。
- 相比无规划对齐的压缩（65.6%），COMPACT-VA再提升+2.7%，验证变分耦合有效性。
- 闭环节相比短上下文基线（2秒）维持同等安全性，同时实现3.3倍推理加速和2.7倍内存缩减（对比未压缩5秒处理）。
- 技能码本利用率达80%（15-17/20），无模式坍缩，表明学到有意义的驾驶意图离散表征。
- 分层压缩结构最佳配置：最近层保留全分辨率，中间层适度压缩，远层激进压缩；分配更多令牌给近帧优于过度扩展远历史。

## 七、优点
- **方法创新**：首次将变分自编码器（cVAE）与令牌压缩耦合，实现规划目标驱动的保留机制，避免手工规则。
- **场景与指标设计**：识别三类记忆依赖高信号场景，设计行为指标直接评估决策正确性，克服传统轨迹指标不足，评价更贴近真实安全需求。
- **端到端集成**：压缩模块、意图预测、策略主干联合训练，训练-推理一致，无需额外阶段。
- **效率突出**：在提升决策质量的同时大幅降低计算开销，推理时间377ms（＜500ms实时要求），内存仅3.95GB，适合部署。
- **消融全面**：逐组件（压缩、历史条件、规划耦合）、压缩率、历史长度均做消融，结论可信。

## 八、不足与局限
- **通用场景增益有限**：在闭环通用驾驶场景中，COMPACT-VA性能与短上下文基线持平，提升主要见于特定记忆依赖场景，泛化性有限。
- **历史长度受限**：消融表明最佳历史长度为5秒/40帧；更长时间（5秒/80帧）提升微弱，部分受基础模型预训练分布限制，可能无法充分发挥长上下文优势。
- **训练算力未公开**：未提供训练所需的GPU型号、数量及时长，不利于复现与成本评估。
- **数据集单一**：仅使用Alpamayo数据集，缺乏在nuScenes、Waymo等公开数据集或真实道路上的交叉验证。
- **场景覆盖不全**：记忆依赖场景仅占数据集16%，且不包括极端遮挡、多竞争者等更复杂情况（文中作为未来工作提及）。
- **架构耦合紧密**：方法紧密依赖Alpamayo主干，迁移至其他VA/VLA架构可能需要适配。

（完）
