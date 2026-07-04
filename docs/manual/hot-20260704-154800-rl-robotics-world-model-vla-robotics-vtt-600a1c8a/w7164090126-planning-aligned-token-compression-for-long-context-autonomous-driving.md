---
title: Planning-aligned Token Compression for Long-Context Autonomous Driving
title_zh: 面向长上下文自动驾驶的规划对齐令牌压缩
authors: "Zhixuan Liang, Yuxiao Chen, Yurong You, Péter Karkus, Wenhao Ding, Boyi Li, Alexander Popov, Yan Wang (15435), Maximilian Igl, Yiming Li, Danfei Xu, Nikolai Smolyanskiy, Boris Ivanovic, Ping Luo, Marco Pavone"
date: 2026-06-05
pdf: "https://arxiv.org/pdf/2606.07464"
tags: ["query:热点论文筛选", "query:VLA-robotics", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=lead-affiliation; institutions=Nvidia (United Kingdom), University of Hong Kong; query=robot foundation model generalist manipulation policy"
tldr: "针对长上下文自动驾驶中视觉-行动模型的token序列超出实时计算预算的问题，现有规则启发式压缩（如时间衰减）与规划解耦，易丢失决策关键信息。本文提出COMPACT-VA，一种基于条件VQ-VAE的规划对齐工作记忆框架，通过历史轨迹和学习到的规划意图条件压缩，先验编码器从压缩观测预测意图，后验编码器从未来轨迹蒸馏，将压缩记忆与预测潜在连接输入策略端到端优化。在相同token预算下，成功率提升>6%（68.3%），闭环评估速度提升3.3倍，内存减少2.7倍，消融实验验证规划对齐耦合的有效性。该工作实现了保留决策关键信息的高效长上下文压缩，显著提升驾驶行为正确性。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有token压缩采用规则启发式（如时间衰减）且与规划解耦，导致决策关键信息丢失，需设计规划对齐的压缩方法。
method: 提出COMPACT-VA，基于条件VQ-VAE，压缩条件结合历史轨迹与学习到的规划意图（后验从未来蒸馏、先验从压缩观测预测），实现端到端优化。
result: "相同token预算下，成功率提升>6%（68.3%），闭环评估速度提升3.3倍、内存减少2.7倍，消融验证规划对齐有效性。"
conclusion: 规划对齐的token压缩显著保留决策关键信息，在长上下文自动驾驶中同时提升性能与效率，具有实用价值。
---

## 摘要
单体视觉-动作模型代表了自动驾驶领域的新兴范式。然而，当编码用于复杂交互的扩展时间上下文时，这种架构产生的词元序列会迅速超出实时计算预算。尽管线性Transformer和外部记忆等方法试图减轻上下文负担，但词元压缩与架构最为兼容，因为它不需要修改主干网络。然而，现有的压缩方法采用基于规则的启发式策略（如时间衰减），与规划过程解耦，有可能丢失决策关键信息。我们提出COMPACT-VA，一种基于条件VQ-VAE构建的规划对齐工作记忆框架，将扩展上下文压缩为有界表示。压缩不仅以历史轨迹为条件，还以学习到的规划意图为条件——后验编码器在训练期间从未来轨迹中提炼该意图，而先验编码器则学习从压缩观测中预测该意图。压缩后的记忆与预测潜变量拼接后馈入策略，实现端到端优化，从而在保留决策关键信息的同时进行规划。我们在历史上下文对行为正确性最为关键的高信号动态场景（如停车、让行或通行）上进行评估，并相应设计了行为指标。在可比词元预算下，我们的成功率提升了超过6%（达到68.3%），且各项指标均有稳定提升。消融实验验证了规划对齐耦合的有效性。闭环评估证实，与未压缩处理相比，COMPACT-VA在保持一般驾驶性能的同时实现了3.3倍加速和2.7倍内存减少。

## Abstract
Monolithic vision-action models represent an emerging paradigm in autonomous driving. However, this architecture produces token sequences that quickly exceed real-time computational budgets when encoding extended temporal context for complex interactions. While approaches like linear transformers and external memory try to make the context lightweight, token compression is most compatible with the architecture as it requires no backbone modifications. Yet existing compression adopts rule-based heuristics like temporal decay, decoupled from planning, risking loss of decision-critical information. We propose COMPACT-VA, a planning-aligned working memory framework built on conditional VQ-VAE, compressing extended context into bounded representations. Compression is conditioned on both historical trajectory and a learned planning intent that the posterior encoder distills from future trajectories during training, while the prior encoder learns to predict it from compressed observations. The compressed memory, concatenated with the predicted latent, feeds the policy for end-to-end optimization, planning with retained decision-critical information. We evaluate on high-signal dynamic scenarios where historical context is most critical for behavior correctness (e.g., stop, yield, or proceed), and accordingly design behavioral metrics. Under comparable token budgets, we achieve $>$6% improvement (68.3%) on success rates with consistent gains across metrics. Ablations validate planning-aligned coupling effectiveness. Closed-loop evaluation confirms that COMPACT-VA maintained general driving performance with 3.3* speedup and 2.7* memory reduction over uncompressed processing.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：单体视觉-动作模型（Vision-Action, VA）在处理长上下文时，token 序列长度急剧增长，超出实时计算预算。现有 token 压缩方法（如时间衰减）采用与规划解耦的规则启发式策略，容易丢失决策关键的历史信息。
- **研究动机**：在自动驾驶中，正确行为（如停车、让行、通行）往往依赖于 5-10 秒内的历史上下文，而规则压缩无法区分关键信息与冗余信息，导致行为错误（如错误判定先行权）。
- **背景**：VLA 政策缺乏显式记忆机制或依赖与规划无关的压缩，急需一种规划对齐的压缩方法，在 token 预算内保留决策相关历史。

## 二、论文提出的方法论
- **核心思想**：提出 COMPACT-VA，一种基于条件 VQ-VAE 的规划对齐工作记忆框架，将长上下文压缩成有界表示，并通过联合优化使压缩与规划目标耦合。
- **关键技术细节**：
  - **分层 FIFO 记忆缓存**：采用三层压缩（近期无压缩、中期适度压缩、远期强力压缩），通过 Q-former 模块进行学习式查询聚合。
  - **条件变分自编码器**：后验编码器 qϕ（训练时从未来轨迹提取驾驶意图），先验编码器 pθ（从压缩观测预测意图），两者共享 VQ 码书（K=20），通过 KL 散度约束。
  - **端到端训练**：策略以先验编码器输出的离散潜变量为条件，联合优化轨迹交叉熵损失、KL 散度和码书承诺损失。
  - **推理时**：仅用先验通路，压缩观测后预测意图，经 VQ 量化后作为特殊 token 输入策略 Transformer 进行自回归轨迹生成。

## 三、实验设计
- **数据集与场景**：在 Alpamayo 物理 AI 数据集上进行评估，重点选取三类高信号动态场景（四向停车、动态遮挡、无保护转弯），这些场景的行为正确性依赖于历史上下文。
- **Benchmark**：对比方法包括标准 Alpamayo（1s 上下文）、稀疏采样长历史（5s）、密集完整历史（5s 无压缩）、无规划对齐压缩，以及 COMPACT-VA 的离散/连续潜变量版本。
- **评价指标**：除传统轨迹指标，还设计了行为指标：停止成功率、通行成功率、滚停率、停止位置误差、停止时长误差。
- **实验设置**：20k 验证片段，5s 历史（40帧@4Hz，2相机），压缩后 1424 token（4.5倍压缩）。闭环评估使用 Alpasim 模拟器在 910 个多样化场景上验证通用驾驶性能。

## 四、资源与算力
- 论文未明确说明训练所用的 GPU 型号、数量及训练时长。仅在推理效率测试中提及使用 NVIDIA A100 GPU，测量推理时间和内存（平均 20 次运行）。
- 数据规模和模型体量：Alpamayo 数据集包含 1727+ 小时驾驶数据，训练子集约占总数据 16%（行为关键场景）。模型骨干基于 Alpamayo，未说明具体参数量。

## 五、实验数量与充分性
- **实验组数**：包含主要对比实验（表 I，7 种方法）、闭环评估（表 II，与基线对比）、消融实验（表 IV-VI）：架构消融、压缩率消融、历史长度消融、码书利用率分析。
- **充分性**：实验覆盖了开环和闭环评价，指标全面（行为+效率），消融实验逐一验证每个组件的贡献（如有无历史轨迹、有无规划对齐潜变量）。但缺少在更多类型场景（如复杂遮挡、多车交互）的验证，且仅基于单一数据集。

## 六、论文的主要结论与发现
- 在相同 token 预算下，COMPACT-VA 相比标准基线提升通行成功率 4.5%（63.8%→68.3%），滚停率降低 22%（9.0%→7.0%），停止成功率和位置误差均有改善。
- 与无规划对齐压缩相比，COMPACT-VA 通行成功率提升 2.7%（65.6%→68.3%），验证了规划对齐耦合的有效性。
- 闭环评估显示，COMPACT-VA 在保持通用驾驶性能的同时，推理速度提升 3.3 倍、峰值内存减少 2.7 倍（相比未压缩长上下文）。
- 码书利用率达到 80%（15-17/20 技能），证明成功学到多样化驾驶意图。

## 七、优点
- **方法创新性**：首次将条件 VQ-VAE 应用于自动驾驶 token 压缩，使压缩与规划目标对齐，自动发现决策相关历史信息。
- **实验设计严谨**：针对高信号场景设计专门行为指标，避免传统轨迹指标对决策正确性不敏感的缺陷；消融实验完整，验证每个组件贡献。
- **效率与性能双赢**：在 token 预算内同时提升决策正确性和推理效率，实用性强。
- **开放性与可复现**：基于开源的 Alpamayo 骨干和 Alpasim 模拟器，代码和数据可获取。

## 八、不足与局限
- **场景局限性**：主要验证三类停车控制场景，对于其他需要长上下文（如高速公路合流、复杂交叉口）未充分覆盖。
- **训练数据依赖**：仅使用 Alpamayo 单一数据集，可能引入域偏移；训练子集筛选标准可能忽略部分重要决策场景。
- **闭环比照不足**：闭环评估仅包含通用驾驶场景，缺少对停车控制场景的闭环复现（文中指出目前 Alpasim 缺少足够停车交叉口重建）。
- **计算资源未报告**：未提供训练所需的 GPU 型号、数量和时间，影响可复现性和规模判断。
- **消融分析限制**：历史长度消融显示 5s 40 帧最佳，但可能受预训练分布影响，最优长度未充分探索。

（完）
