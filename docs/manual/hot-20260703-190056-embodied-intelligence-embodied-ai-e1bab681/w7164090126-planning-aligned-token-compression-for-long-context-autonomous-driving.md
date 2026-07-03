---
title: Planning-aligned Token Compression for Long-Context Autonomous Driving
title_zh: 面向规划的长上下文自动驾驶令牌压缩
authors: "Zhixuan Liang, Yuxiao Chen, Yurong You, Péter Karkus, Wenhao Ding, Boyi Li, Alexander Popov, Yan Wang (15435), Maximilian Igl, Yiming Li, Danfei Xu, Nikolai Smolyanskiy, Boris Ivanovic, Ping Luo, Marco Pavone"
date: 2026-06-05
pdf: "https://arxiv.org/pdf/2606.07464"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=lead-affiliation; institutions=Nvidia (United Kingdom), University of Hong Kong; query=generalist robot policy"
tldr: "长上下文自动驾驶中的单体视觉-动作模型因token序列过长难以实时处理。现有基于规则的压缩（如时间衰减）与规划解耦，可能丢失关键信息。本文提出COMPACT-VA，一种基于条件VQ-VAE的规划对齐工作记忆框架，利用历史轨迹与学习到的规划意图（后验蒸馏自未来轨迹，先验从压缩观测预测）进行压缩。相同token预算下，成功率提升6%达68.3%，其他指标一致提升，速度提升3.3倍，内存减少2.7倍。该方法不修改主干，通过规划对齐保留决策信息，实现高效长上下文自动驾驶。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有基于规则的token压缩方法（如时间衰减）与规划解耦，在长上下文自动驾驶中易丢失决策关键信息，影响行为正确性。
method: 提出COMPACT-VA，基于条件VQ-VAE，利用历史轨迹和学习到的规划意图（后验从未来轨迹蒸馏，先验从压缩观测预测）进行规划对齐的上下文压缩。
result: "相同token预算下，成功率提升超过6%（达68.3%），其他指标一致提升；闭环评估中速度提升3.3倍，内存减少2.7倍。"
conclusion: COMPACT-VA通过规划对齐的token压缩，在保留决策关键信息的同时显著提升长上下文自动驾驶效率与性能，无需修改主干架构。
---

## 摘要
单体视觉-动作模型代表了自动驾驶中的一种新兴范式。然而，当为复杂交互编码扩展的时间上下文时，这种架构产生的令牌序列会迅速超出实时计算预算。虽然线性变换器和外部存储器等方法试图使上下文轻量化，但令牌压缩与架构兼容性最佳，因为它不需要修改主干网络。然而现有的压缩采用基于规则的启发式方法（如时间衰减），与规划解耦，存在丢失决策关键信息的风险。我们提出COMPACT-VA，一种基于条件VQ-VAE的面向规划的工作记忆框架，将扩展上下文压缩为有界表示。压缩同时依赖于历史轨迹和一种学习到的规划意图，其中后验编码器在训练期间从未来轨迹中提取该意图，而先验编码器学习从压缩观测中预测该意图。压缩记忆与预测的潜变量拼接后，输入策略进行端到端优化，从而利用保留的决策关键信息进行规划。我们在历史上下文对行为正确性（如停车、让行或前行）最关键的强信号动态场景中进行评估，并据此设计了行为指标。在相当的令牌预算下，我们的成功率提高了>6%（达到68.3%），且所有指标均一致提升。消融实验验证了面向规划的耦合有效性。闭环评估证实，与未压缩处理相比，COMPACT-VA在保持一般驾驶性能的同时实现了3.3倍加速和2.7倍内存缩减。

## Abstract
Monolithic vision-action models represent an emerging paradigm in autonomous driving. However, this architecture produces token sequences that quickly exceed real-time computational budgets when encoding extended temporal context for complex interactions. While approaches like linear transformers and external memory try to make the context lightweight, token compression is most compatible with the architecture as it requires no backbone modifications. Yet existing compression adopts rule-based heuristics like temporal decay, decoupled from planning, risking loss of decision-critical information. We propose COMPACT-VA, a planning-aligned working memory framework built on conditional VQ-VAE, compressing extended context into bounded representations. Compression is conditioned on both historical trajectory and a learned planning intent that the posterior encoder distills from future trajectories during training, while the prior encoder learns to predict it from compressed observations. The compressed memory, concatenated with the predicted latent, feeds the policy for end-to-end optimization, planning with retained decision-critical information. We evaluate on high-signal dynamic scenarios where historical context is most critical for behavior correctness (e.g., stop, yield, or proceed), and accordingly design behavioral metrics. Under comparable token budgets, we achieve $>$6% improvement (68.3%) on success rates with consistent gains across metrics. Ablations validate planning-aligned coupling effectiveness. Closed-loop evaluation confirms that COMPACT-VA maintained general driving performance with 3.3* speedup and 2.7* memory reduction over uncompressed processing.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 单体视觉‑动作（VA）或视觉‑语言‑动作（VLA）模型是自动驾驶的新范式，能够通过统一的 Transformer 主干直接将多模态输入映射为车辆轨迹。
- 然而，这类模型需要处理扩展的时间上下文（例如数秒的历史观测），导致 token 序列长度快速增长，超出实时计算预算。
- 现有方法中，线性 Transformer、外部记忆等虽试图减轻计算负担，但 token 压缩因无需修改主干而最具实用性。但当前压缩方法普遍采用基于规则的启发式策略（如“时间衰减”——保留最近帧、丢弃较早帧），这些策略与规划目标解耦，可能丢失决策关键的历史信息（例如在四向停牌路口判断谁先到达、是否需要让行）。
- 因此，核心问题是如何在有限的 token 预算下，保留对规划决策至关重要的历史上下文，实现高效且正确的长上下文自动驾驶。

## 二、论文提出的方法论
- **核心思想**：提出 COMPACT‑VA，一种面向规划对齐的工作记忆框架，基于条件 VQ‑VAE（conditional VQ‑VAE）。压缩过程同时利用历史轨迹和学习到的“驾驶意图”（driving intent）潜变量，使压缩结果直接服务于下游规划任务，从而保留决策关键信息。
- **关键技术细节**：
  1. **分层 FIFO 记忆缓存**：将历史观测组织为 K 个压缩层（如近期层保留全分辨率、中间层适度压缩、远层强压缩），通过可学习的 Q‑former 模块对每帧的观测 token 进行聚合压缩，输出压缩 token 序列。
  2. **规划对齐变分压缩**：引入条件 VAE，包含两个编码器：
     - 后验编码器（Q‑net，训练时使用）：从未来轨迹中提取驾驶意图潜变量 z_q，遵循高斯分布。
     - 先验编码器（P‑net，训练和推理时使用）：仅从压缩观测中预测潜变量 z_p，并在训练时通过 KL 散度学习匹配后验分布。
     - 两者通过向量量化（VQ）映射到共享离散码本，得到技能嵌入 z_skill。
  3. **策略输入**：将 z_skill 作为特殊 token，与压缩记忆、历史轨迹 token 以及时间/摄像头嵌入拼接后输入统一 Transformer 主干，端到端自动回归预测未来轨迹 token。
  4. **联合优化**：总损失为轨迹交叉熵损失 + λ_KL · KL 散度 + λ_commit · 承诺损失，确保压缩模块保留足以准确预测驾驶意图的信息。

## 三、实验设计
- **数据集与场景**：基于 Alpamayo 物理 AI 数据集，重点从其中提取三类“强信号动态场景”：
  - 四向停牌路口（需基于到达顺序判断通行权）
  - 动态遮挡下的停牌/让行（需记忆曾被观测但后被遮挡的车辆）
  - 无保护转弯（需评估对向车辆的减速/让行意图）
- **Benchmark**：从数据集中筛选约 16% 的片段（包含减速至静止再加速的明确行为），构建 20,000 个验证片段（每个 20 秒，10Hz，关键决策点在 50 帧）及对应的训练集。
- **对比方法**：
  1. Standard Alpamayo（1s 上下文，1280 tokens）
  2. Sparse Obs w/ Long Hist（5s 稀疏采样，1280 tokens）
  3. Dense Obs w/ Long Hist（5s 密采样，6400 tokens，无压缩）
  4. Compression w/o plan-align（5s 密采样 + 层次压缩，1424 tokens，但不含规划对齐模块）
  5. COMPACT‑VA（离散版和连续版，5s 密采样 + 规划对齐压缩，1424 tokens）
- **评估指标**：行为指标（Go SR、Stop SR、Roll‑through Rate、Stop Position Error、Stop Duration Error）以及传统效率指标（推理时间、峰值 GPU 内存）。
- **闭环评估**：在 Alpasim 模拟器上对 910 个通用驾驶场景评估，对比 2s 18 imgs 基准模型与 COMPACT‑VA（5s 40 imgs + 压缩）。

## 四、资源与算力
- 论文未明确说明使用的 GPU 型号、数量及训练时长。
- 推断：模型基于 Alpamayo 框架，训练可能在 NVIDIA 内部集群（如 A100）上进行，但具体算力细节在本文中缺失。

## 五、实验数量与充分性
- 实验较为充分：
  - 在验证集上报告了主要指标及标准差（3 次随机种子）。
  - 进行了多组消融实验：
    - 架构消融（无压缩、朴素压缩、无规划对齐、两种规划对齐变体）
    - 分层压缩比率消融（不同层配置）
    - 历史长度消融（5s 20/40/60/80 帧）
    - 技能使用率分析（VQ 码本利用率）。
  - 闭环实验对比了关键安全指标与效率指标。
- 评价：实验设计客观、公平，覆盖了决策关键场景和通用场景，控制 token 预算相当，并报告了标准差以体现稳定性。但仅使用单一数据集（Alpamayo），未在其它公开数据集（如 nuScenes、Waymo）上验证，泛化性受限。

## 六、论文的主要结论与发现
- COMPACT‑VA 在相同的 token 预算下，Go SR 达到 68.3%，比最佳基线（压缩无规划对齐，65.6%）提高 2.7 个百分点，比标准 Alpamayo（63.8%）提高 4.5 个百分点。
- Roll‑through 率降低 22%（7.0% vs 9.0%），Stop SR、Stop Position Error、Stop Duration Error 均有改善。
- 效率：在闭环通用场景中，COMPACT‑VA 保持与短上下文基准相当的驾驶性能（碰撞、偏离等），同时实现 3.3 倍加速和 2.7 倍内存缩减（相比未压缩 5s 40imgs）。
- 消融验证每个组件（层次压缩、历史轨迹条件、规划对齐潜变量）均贡献提升。
- VQ 码本利用率达 80%（激活 15–17/20 个技能），表明学习到多样化的驾驶意图。

## 七、优点
- **方法创新**：首次将规划对齐引入 token 压缩，通过条件 VQ‑VAE 隐式让模型“自动”学到哪些历史信息对决策重要，无需人工规则。
- **兼容性强**：不修改主干架构，可直接用于现有 VA/VLA 模型。
- **行为指标设计合理**：针对决策关键场景设计了 Stop SR、Go SR、Roll‑through 等指标，比传统 minADE 更反映实际安全性。
- **效率与性能双赢**：在降低计算开销的同时提升决策正确性。
- **消融实验系统**：从各个角度验证了方法各组件的作用，结果清晰。

## 八、不足与局限
- **数据集单一**：仅使用 Alpamayo 数据集（NVIDIA 内部），未在 nuScenes、Waymo 等公开基准上评估，泛化性存疑。
- **场景覆盖有限**：三类强信号场景虽重要但远非全部，对更复杂交互（如多车博弈、环岛、行人密集区）未验证。
- **闭环评估场景不足**：闭环仅在通用驾驶场景（910个）中测试，缺乏足够数量的停牌路口重建场景，因此未能在闭环中直接验证强信号场景下的行为收益。
- **计算资源信息缺失**：未报告训练所需 GPU 数量/时长，不利于复现和公平比较。
- **性能增益在某些场景下较小**：在通用驾驶场景中，与短上下文基准性能持平，未显著提升（可能因为这类场景对长上下文需求不高）。
- **历史长度上限**：当历史超过 5s 时（如 5s 80 帧），性能并未持续提升，可能与模型预训练分布有关，未来需探索更长上下文机制。

（完）
