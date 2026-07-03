---
title: Planning-aligned Token Compression for Long-Context Autonomous Driving
title_zh: 面向长上下文自动驾驶的规划对齐令牌压缩
authors: "Zhixuan Liang, Yuxiao Chen, Yurong You, Péter Karkus, Wenhao Ding, Boyi Li, Alexander Popov, Yan Wang (15435), Maximilian Igl, Yiming Li, Danfei Xu, Nikolai Smolyanskiy, Boris Ivanovic, Ping Luo, Marco Pavone"
date: 2026-06-05
pdf: "https://arxiv.org/pdf/2606.07464"
tags: ["query:热点论文筛选", "query:综合方向", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=lead-affiliation; institutions=Nvidia (United Kingdom), University of Hong Kong; query=generalist robot policy"
tldr: "自动驾驶视觉-动作模型处理长时序上下文时计算成本过高，导致token序列超实时预算。现有令牌压缩采用与规划解耦的规则启发式，容易丢失决策关键信息。本文提出COMPACT-VA，一种基于条件VQ-VAE的规划对齐工作记忆框架，通过历史轨迹和可学习的规划意图条件压缩上下文，压缩记忆与预测潜变量直接用于策略优化。在停车、让行等关键动态场景中，相同token预算下成功率提升超过6%（达68.3%），并实现3.3倍速度提升和2.7倍内存节省，验证了规划对齐压缩的有效性与效率。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有token压缩方法采用与规划解耦的规则启发式（如时间衰减），可能丢失决策关键信息，影响行为正确性。
method: 提出COMPACT-VA，基于条件VQ-VAE的规划对齐工作记忆，利用历史轨迹和学习到的规划意图压缩长上下文，压缩记忆与预测潜变量用于端到端策略优化。
result: "在关键动态场景中，相同token预算下成功率提升>6%（68.3%），各行为指标一致提升；闭环比测速3.3倍、内存减少2.7倍。"
conclusion: 规划对齐的token压缩能有效保留决策关键信息，在不牺牲驾驶性能前提下大幅提升效率。
---

## 摘要
单体视觉-动作模型代表了自动驾驶领域的一种新兴范式。然而，这种架构在编码用于复杂交互的扩展时间上下文时，产生的令牌序列会迅速超出实时计算预算。尽管线性变换器和外部记忆等方法试图使上下文轻量化，但令牌压缩与架构最为兼容，因为它不需要修改主干网络。然而，现有的压缩采用基于规则的启发式方法（如时间衰减），与规划脱节，存在丢失决策关键信息的风险。我们提出COMPACT-VA，一种基于条件VQ-VAE的规划对齐工作记忆框架，将扩展上下文压缩为有界表示。压缩同时依赖于历史轨迹和一个学习到的规划意图，在训练期间，后验编码器从未来轨迹中提炼该意图，而先验编码器则学会从压缩观测中预测它。压缩记忆与预测的潜在变量拼接，输入策略进行端到端优化，从而在保留决策关键信息的情况下进行规划。我们在高信号动态场景（其中历史上下文对行为正确性最为关键，例如停车、让行或前行）上进行评估，并相应地设计了行为指标。在可比的令牌预算下，我们在成功率上实现了超过6%的提升（68.3%），且各项指标均持续提升。消融实验验证了规划对齐耦合的有效性。闭环评估证实，与未压缩处理相比，COMPACT-VA在保持一般驾驶性能的同时实现了3.3倍加速和2.7倍内存减少。

## Abstract
Monolithic vision-action models represent an emerging paradigm in autonomous driving. However, this architecture produces token sequences that quickly exceed real-time computational budgets when encoding extended temporal context for complex interactions. While approaches like linear transformers and external memory try to make the context lightweight, token compression is most compatible with the architecture as it requires no backbone modifications. Yet existing compression adopts rule-based heuristics like temporal decay, decoupled from planning, risking loss of decision-critical information. We propose COMPACT-VA, a planning-aligned working memory framework built on conditional VQ-VAE, compressing extended context into bounded representations. Compression is conditioned on both historical trajectory and a learned planning intent that the posterior encoder distills from future trajectories during training, while the prior encoder learns to predict it from compressed observations. The compressed memory, concatenated with the predicted latent, feeds the policy for end-to-end optimization, planning with retained decision-critical information. We evaluate on high-signal dynamic scenarios where historical context is most critical for behavior correctness (e.g., stop, yield, or proceed), and accordingly design behavioral metrics. Under comparable token budgets, we achieve $>$6% improvement (68.3%) on success rates with consistent gains across metrics. Ablations validate planning-aligned coupling effectiveness. Closed-loop evaluation confirms that COMPACT-VA maintained general driving performance with 3.3* speedup and 2.7* memory reduction over uncompressed processing.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 研究动机：面向统一架构的视觉-动作（VA/VLA）自动驾驶模型在处理长时序上下文时，token序列长度过快增长，超出实时计算预算。现有token压缩方法（如时间衰减规则）与规划目标解耦，仅保留近期帧而忽略远期决策关键信息，导致行为错误（如在路口错误判断路权）。
- 整体含义：提出一种**规划对齐（planning-aligned）** 的token压缩机制，通过将压缩过程与驾驶意图预测显式耦合，自动学习保留对下游规划至关重要的历史信息，从而在有限token预算下提升长上下文驾驶决策的正确性与计算效率。

## 二、论文提出的方法论
- 核心思想：基于条件VQ-VAE（conditional vector-quantized variational autoencoder）构建**规划对齐工作记忆框架（COMPACT-VA）**。压缩模块（Q-former）不仅依赖历史观测，还依赖一个可学习的驾驶意图潜变量（driving intent latent）；该意图在训练时由后验编码器从未来轨迹蒸馏得到，在推理时由先验编码器从压缩观测中预测；压缩后的记忆与预测潜变量作为特殊token输入策略主干，端到端优化。
- 关键技术细节：
  - **分层FIFO缓冲**：将历史观测按时间分为多层（近、中、远），分别施加不同压缩比（如1×、16×、80×），在保留近期高分辨率的同时压缩远处帧。
  - **Q-former压缩**：在每一层使用可学习查询token与观测token、时间编码、相机编码进行自注意力，选择性地聚合视觉特征。
  - **条件VAE**：后验编码器（仅训练）从未来轨迹输出高斯分布参数；先验编码器从压缩观测预测潜变量；两者经向量量化（VQ）映射到共享技能码本（codebook size=20, latent dim=32）。量化后的离散潜变量（skill embedding）经线性层后作为特殊token与压缩记忆拼接。
  - **训练损失**：轨迹预测的交叉熵损失 + KL散度（鼓励先验匹配后验）+ commitment loss。推理时仅使用先验路径。
- 算法流程：多视角历史图像→视觉token→Q-former压缩（同时输入历史轨迹和可学习查询）→先验编码器预测潜变量→VQ量化→skill token→与压缩记忆、历史轨迹token拼接→统一transformer主干→自回归生成未来轨迹token。

## 三、实验设计
- **数据集与场景**：使用NVIDIA Alpamayo物理AI数据集，从中筛选出**高信号动态场景**（四路停车、动态遮挡、无保护转弯）约16%作为开环评估子集；提取20,000个20秒长片段（关键决策点在第50帧）用于验证。闭环评估使用Alpasim模拟器中的910个多样化场景（来自Physical AI AV NuRec数据集）。
- **基准方法**：
  - Standard Alpamayo（1s 8帧，1280 tokens）
  - Sparse Obs w/ Long Hist（5s 8帧，1280 tokens）
  - Dense Obs w/ Long Hist（5s 40帧，6400 tokens，无压缩）
  - Compression w/o plan-align（5s 40帧，1424 tokens，分层压缩但无规划对齐）
  - COMPACT-VA (Discrete / Continuous) —— 使用离散FSQ或连续潜变量编码
- **评估指标**：针对行为正确性设计，包括**Go成功率**（主要）、Stop成功率、Roll-through率、停止位置误差、停止持续时间误差。
- **效率指标**：推理时间（A100 GPU）、峰值GPU内存。

## 四、资源与算力
- 文中仅提到推理测试在NVIDIA A100 GPU上进行，但**未明确说明训练所使用的GPU型号、数量及训练时长**。闭环模拟器运行在A100上。因此无法获知完整的计算资源开销。

## 五、实验数量与充分性
- **实验数量**：主要开环结果（表I）比较了5种方法+2种变体；消融研究包括：
  - 架构消融（表IV）：无压缩、朴素压缩、无规划对齐压缩、两个版本的规划对齐压缩（共5种配置）
  - 压缩率消融（表V）：8种不同层分配组合
  - 历史长度消融（表VI）：5种帧数（20/40/60/80 imgs）
  - 闭环评估（表II）：2个方法对比
  - 技能码本利用率分析：4个随机种子，50K步
- **充分性**：实验设计较系统，覆盖了方法核心组件（压缩、历史条件、规划对齐）的影响，且在不同token预算、不同历史长度下进行了对比。但闭环场景局限于910个一般驾驶场景，未能在高信号停车场景中闭环验证；baseline选择合理但未包含近期其他高效架构（如Mamba）。整体充分但可进一步提升场景多样性。

## 六、论文的主要结论与发现
- 在可比token预算下，COMPACT-VA的Go成功率（68.3%）超过标准Alpamayo（63.8%）及无规划对齐压缩（65.6%），且Roll-through率降低22%（7.0% vs 9.0%）。
- 分层有损压缩（1424 tokens）优于无压缩的全帧（6400 tokens），表明纯粹增加token密度反而因注意力过载而损害时空推理。
- 规划对齐的VAE机制是性能增益的关键：加入历史轨迹条件提升2.1% Go SR，再加入未来意图潜变量再提升2.7%。
- 闭合环测表明在一般驾驶场景中性能持平，同时实现3.3倍推理加速和2.7倍内存减少。

## 七、优点
- **方法创新**：将条件VQ-VAE引入VA驾驶模型的token压缩，使压缩过程本身成为端到端规划的一部分，自动学习保留决策关键历史。
- **评估指标设计**：针对高信号场景提出行为正确性指标（Go/Stop成功率等），优于传统位移误差指标，更贴合实际安全需求。
- **实验体系完整**：开环+闭环、多种消融、效率对比，证明了方法在决策质量和计算效率上的双重优势。
- **可扩展性**：压缩框架与统一VA架构兼容，无需修改骨干网络，易于集成到现有系统。

## 八、不足与局限
- **闭环场景限制**：闭环评估仅在一般驾驶场景（910个）上进行，缺乏高信号停车控制交叉口的闭环验证（作者指出模拟器重建不足），导致无法评估方法在真实行为决策闭环中的表现。
- **基线范围有限**：未对比子其他高效架构（如Mamba、Transformer-XL等），也未与近期基于记忆的方法（如MemoryVLA）比较。
- **训练资源未报告**：未明确披露训练所需的GPU型号、数量和时长，影响可复现性和算力评估。
- **泛化依赖**：方法在一般驾驶场景提升较小（作者承认），且依赖预训练模型的分布（历史长度受限于预训练数据），可能在高复杂性场景下表现未知。
- **潜在偏差**：开环数据筛选标准（制动减速→停车→再出发）可能引入特定驾驶风格的偏差，且场景仅覆盖三种类型（四路停车、动态遮挡、无保护转弯），未覆盖其他记忆关键场景（如变道、合并等）。

（完）
