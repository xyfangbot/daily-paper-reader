---
title: Planning-aligned Token Compression for Long-Context Autonomous Driving
title_zh: 规划对齐的长上下文自动驾驶令牌压缩
authors: "Zhixuan Liang, Yuxiao Chen, Yurong You, Péter Karkus, Wenhao Ding, Boyi Li, Alexander Popov, Yan Wang (15435), Maximilian Igl, Yiming Li, Danfei Xu, Nikolai Smolyanskiy, Boris Ivanovic, Ping Luo, Marco Pavone"
date: 2026-06-05
pdf: "https://arxiv.org/pdf/2606.07464"
tags: ["query:热点论文筛选", "query:综合方向", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=lead-affiliation; institutions=Nvidia (United Kingdom), University of Hong Kong; query=generalist robot policy"
tldr: "自动驾驶中的单体视觉-动作模型在处理长时序上下文时产生超预算token序列。现有规则式压缩方法（如时间衰减）与规划脱节，可能丢失决策关键信息。本文提出COMPACT-VA，基于条件VQ-VAE的规划对齐工作记忆框架，将压缩条件化于历史轨迹与学习到的规划意图（后验从未来轨迹蒸馏，先验从压缩观测预测），实现端到端优化。在动态场景下，该方法在可比token预算下成功率达68.3%（提升>6%），并实现3.3倍加速与2.7倍内存压缩，同时保持通用驾驶性能。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有token压缩采用与规划脱节的规则式启发（如时间衰减），易丢失决策关键信息，亟需规划对齐的上下文压缩方法。
method: 提出COMPACT-VA，基于条件VQ-VAE的规划对齐工作记忆：后验编码器从未来轨迹蒸馏规划意图，先验编码器从压缩观测预测该意图，压缩记忆与预测潜变量连接后输入策略进行端到端优化。
result: "在动态场景中，可比token预算下成功率提升>6%（达68.3%），且具有3.3倍速度提升与2.7倍内存压缩，消融实验验证了规划对齐耦合的有效性。"
conclusion: 规划对齐的token压缩能保留决策关键信息，以显著加速和内存缩减实现高效长上下文自动驾驶，无需修改主干架构。
---

## 摘要
单体视觉-动作模型代表了自动驾驶领域的一种新兴范式。然而，当编码用于复杂交互的扩展时间上下文时，这种架构产生的令牌序列会迅速超出实时计算预算。虽然线性变换器和外部记忆等方法试图让上下文变得轻量，但令牌压缩与架构最为兼容，因为它无需修改主干网络。然而，现有压缩采用基于规则的启发式方法（如时间衰减），与规划解耦，存在丢失决策关键信息的风险。我们提出COMPACT-VA，一种基于条件VQ-VAE的规划对齐工作记忆框架，将扩展上下文压缩为有界表征。压缩同时依赖于历史轨迹和一种学习的规划意图，其中后验编码器在训练期间从未来轨迹中提取该意图，而先验编码器则学习从压缩观测中预测它。压缩记忆与预测的潜变量拼接后馈送给策略进行端到端优化，从而保留决策关键信息进行规划。我们在高信号动态场景中进行评估，这些场景中历史上下文对行为正确性（如停车、让行或通行）最为关键，并据此设计了行为指标。在可比的令牌预算下，我们在成功率上实现了超过6%的提升（68.3%），且各项指标均有一致改善。消融实验验证了规划对齐耦合的有效性。闭环评估证实，与未压缩处理相比，COMPACT-VA以3.3倍加速和2.7倍内存减少保持了通用驾驶性能。

## Abstract
Monolithic vision-action models represent an emerging paradigm in autonomous driving. However, this architecture produces token sequences that quickly exceed real-time computational budgets when encoding extended temporal context for complex interactions. While approaches like linear transformers and external memory try to make the context lightweight, token compression is most compatible with the architecture as it requires no backbone modifications. Yet existing compression adopts rule-based heuristics like temporal decay, decoupled from planning, risking loss of decision-critical information. We propose COMPACT-VA, a planning-aligned working memory framework built on conditional VQ-VAE, compressing extended context into bounded representations. Compression is conditioned on both historical trajectory and a learned planning intent that the posterior encoder distills from future trajectories during training, while the prior encoder learns to predict it from compressed observations. The compressed memory, concatenated with the predicted latent, feeds the policy for end-to-end optimization, planning with retained decision-critical information. We evaluate on high-signal dynamic scenarios where historical context is most critical for behavior correctness (e.g., stop, yield, or proceed), and accordingly design behavioral metrics. Under comparable token budgets, we achieve $>$6% improvement (68.3%) on success rates with consistent gains across metrics. Ablations validate planning-aligned coupling effectiveness. Closed-loop evaluation confirms that COMPACT-VA maintained general driving performance with 3.3* speedup and 2.7* memory reduction over uncompressed processing.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 研究背景：自动驾驶中的单体视觉-动作（Vision-Action, VA）或视觉-语言-动作（VLA）策略通过统一Transformer骨干网络直接映射传感器输入到车辆轨迹，避免了传统模块化流水线（感知-预测-规划）的显式状态表示。然而，当需要编码更长的历史上下文（例如10秒）以处理复杂交互时，视觉令牌序列会急剧增长（如5秒40帧图像产生6400个令牌），导致实时计算代价过高（注意力复杂度O(N²)）。
- 核心问题：现有长上下文处理方法（线性注意力、外部记忆模块）要么修改骨干架构，要么与规划目标脱节。尤其是令牌压缩方法目前依赖基于规则的启发式（如时间衰减——保留最近帧、丢弃较远帧），这种策略与规划目标解耦，可能丢失决策关键的历史信息（例如在四向停车路口需要追溯3秒前哪辆车先到达以确定通行权）。
- 研究动机：探索一种规划对齐的令牌压缩方法，使压缩过程能根据下游规划需求自适应地保留决策关键信息，同时保持与原有架构兼容，且不增加大规模计算开销。
- 整体含义：提出COMPACT-VA框架，将压缩与轨迹预测通过条件变分自编码器（cVAE）耦合，实现端到端的学习型工作记忆，在保持约1400令牌预算下提升决策正确率，同时获得3.3倍加速和2.7倍内存缩减。

## 二、论文提出的方法论
- 核心思想：基于条件VQ-VAE的规划对齐工作记忆框架。设计两个编码器：后验编码器从未来真实轨迹中蒸馏驾驶意图（training only），先验编码器从压缩后的历史观测中预测该意图。通过KL散度迫使压缩观测保留足够信息以准确预测意图，从而隐式地学习保留决策关键信息。压缩记忆与预测的潜在技能嵌入拼接后馈入统一策略骨干进行端到端优化。
- 关键技术细节：
  1. **层次化FIFO记忆缓冲**：将5秒（20帧）历史观测组织成三层，每层应用不同压缩比。第一层（最近4帧）不压缩（160令牌/帧），第二层（中间5帧）压缩为10令牌/帧，第三层（最远11帧）压缩为2令牌/帧。总令牌数从6400降至1424（4.5倍压缩）。每层通过Q-Former模块（可学习查询令牌与观测令牌拼接后自注意力）实现压缩，并根据压缩比缩放RoPE位置编码。
  2. **条件VAE+VQ**：后验编码器（训练用）将64维未来轨迹先转化为操控序列（加速度、曲率），经MLP压缩为5个聚合令牌（1全局+4局部），通过小型Transformer输出高斯分布参数并采样潜变量zq。先验编码器（训练和推理都用）从Q-Former输出的压缩观测中通过注意力池化和MLP产生潜变量zp。两者均向量量化到20维离散码本，使用直通估计器梯度传播，并加入承诺损失。
  3. **策略输入构成**：将量化的离散技能嵌入z_skill（先验编码器输出）通过线性层重投影后作为特殊令牌，与压缩记忆、历史轨迹令牌及位置/相机嵌入拼接，按时间顺序重新排序后输入统一的Transformer骨干（基于Alpamayo）。骨干自回归预测未来轨迹令牌（FSQ令牌化）。
  4. **端到端训练损失**：L = L_traj + λKL * KL(q||p) + λcommit * L_commit。其中L_traj是轨迹令牌的交叉熵；KL项迫使先验匹配后验；承诺损失鼓励潜变量接近码本。训练时策略以前置编码器采样的潜变量（而非后验）为条件，保证训练推理一致。
  5. **推理流程**：Q-Former压缩观测，先验编码器预测zp，量化VQ获得技能嵌入，拼接后输入策略自回归生成轨迹。

## 三、实验设计
- 数据集和场景：使用NVIDIA Physical AI自动驾驶数据集（1727+小时驾驶数据，25国25+城市）。重点测试三类“高信号动态场景”（记忆关键型）：(a) 四向停车路口（按到达顺序决定通行权）；(b) 带动态遮挡的停止/让行牌（需要保留先前观察到的参与者状态）；(c) 无保护左转（需要根据对向车辆几秒前的减速趋势决定是否让行）。从数据集中筛选子集：轨迹经历减速至<1m/s、停车≥0.5s、再加速，约占总数据16%。验证集2万片段（20秒，10Hz，关键决策点在50帧），其余用于训练。
- 评估指标：行为指标（超越传统位移误差minADE）：停车成功率（Stop SR）、通行成功率（Go SR，主要指标，直接反映记忆有效保留）、滚停率、停车位置误差、停车时长误差。同时做闭环评估（Alpasim仿真器，910个多样场景）。
- 对比方法：标准Alpamayo（1秒8帧1280令牌）、稀疏长历史（5秒8帧1280令牌）、密集长历史（5秒40帧6400令牌，无压缩）、无规划对齐的压缩（层次压缩但无cVAE模块）、COMPACT-VA离散版（FSQ令牌化）、COMPACT-VA连续版（连续潜变量）。所有方法在相同数据上端到端训练，训练专业子集。

## 四、资源与算力
- 论文未明确给出使用的GPU型号、数量、训练时长等具体算力信息。仅在效率实验（Tab III）中提到在NVIDIA A100上测量推理时间和内存。说明COMPACT-VA在A100上推理平均377ms（中位数374ms），峰值显存3.95GB；对比未经压缩的长上下文（5s40帧）平均1253ms，显存10.51GB。训练算力细节未披露。

## 五、实验数量与充分性
- 实验数量：主要表I（7种方法对比，包括两种COMPACT-VA变体）、表II（闭环评估，8个指标）、表III（效率，3种配置）、表IV（架构消融，4种变体）、表V（压缩率消融，7种配置）、表VI（历史长度消融，5种长度）。此外还有代码利用率分析（20个技能中激活15-17个）。共约6+组主要实验，每组包含多次随机种子。
- 充分性：实验覆盖了开放环和闭环评估、行为指标、效率指标、多层级消融（无压缩→朴素压缩→历史条件压缩→规划对齐V1→规划对齐V2）。对比基线合理，包括稀疏采样、密集无压缩、无规划对齐的压缩，能有效验证各组件贡献。统计误差（±标准差）在多数指标中给出。存在一定局限（如闭环评估未覆盖停车路口场景，因模拟器缺少足够重建）。整体实验设计较充分客观。

## 六、论文的主要结论与发现
- 在可比令牌预算（~1400令牌）下，COMPACT-VA在主要指标Go成功率上达到68.3%，比标准Alpamayo（63.8%）提升4.5个百分点（相对6%+），比无规划对齐压缩（65.6%）提升2.7个百分点。滚停率降低22%（9.0%→7.0%），停车成功率提升（89.2% vs 86.8%），停车时长误差降低。
- 密集长历史无压缩方案（6400令牌）性能最差（Go SR 61.9%），说明暴力增加令牌反而有害；稀疏采样（8帧）也低于标准，说明丢失关键中间帧。层次化压缩本身已带来提升（65.6%），但加入规划对齐后进一步提升。
- 消融证实：历史条件、未来潜变量注入、编码器耦合均贡献显著。最佳配置：8帧最近（160令牌/帧）、10帧中间（10令牌/帧）、22帧最远（2令牌/帧），5秒40帧共1424令牌。
- 闭环评估：在通用驾驶910场景中，COMPACT-VA（5s 40帧压缩）与基线（2s 18帧）在安全相关指标（碰撞、偏离道路等）上性能相当，但推理加速1.32倍，显存降低33%。对比同长上下文无压缩版，加速3.3倍，显存降低2.7倍。
- 说明规划对齐压缩能在保留决策关键信息的同时实现高效长上下文，且不牺牲通用驾驶能力。

## 七、优点
1. **任务驱动压缩**：首次将令牌压缩与驾驶规划目标通过cVAE显式耦合，使压缩器学会保留决策相关信息，无需人工规则。
2. **层次化结构合理**：结合时间衰减启发式（近密远疏）与可学习Q-Former，既保持效率又保留灵活性。
3. **行为指标创新**：针对记忆关键场景设计停车/通行成功率、滚停率等指标，比传统位移误差更能反映实际驾驶质量。
4. **兼容性极佳**：无需修改骨干Transformer，可作为即插即用模块集成到现有VA/VLA策略中。
5. **多场景验证**：开放环和闭环双评估，覆盖记忆关键场景和通用场景，消融实验全面。
6. **效率优势明显**：在保持甚至提升性能的同时，大幅降低推理时间和显存，适用于实时部署。

## 八、不足与局限
1. **闭环场景覆盖不足**：闭环评估仅在通用驾驶场景进行，缺乏对停车路口等记忆关键场景的直接闭环验证（受限于模拟器重建可用性）。
2. **训练数据分布局限性**：高信号场景仅占数据集16%，模型在该子集上微调后，可能对其他场景泛化性有待进一步验证（尽管闭环通用场景结果尚可）。
3. **历史长度获益有限**：消融表明更长历史（如5s 80帧）未能进一步显著提升，暗示受限于基座模型的预训练分布或有效建模容量——最佳历史长度可能需重新预训练而非微调。
4. **对超参数敏感**：压缩率分配（表V）影响较大，最优配置需仔细调参，缺乏自适应分配机制。
5. **计算资源细节缺失**：未报告训练算力需求，无法评估训练成本。
6. **对比基准局限**：只对比了同一体系下Alpamayo的变体，未与外部先进的长上下文方法（如StreamingLLM、Mamba、Compressive Transformer）直接对比，论证力度可进一步加强。

（完）
