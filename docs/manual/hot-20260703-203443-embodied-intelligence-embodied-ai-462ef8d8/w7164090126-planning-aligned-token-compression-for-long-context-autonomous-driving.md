---
title: Planning-aligned Token Compression for Long-Context Autonomous Driving
title_zh: 针对长上下文自动驾驶的规划对齐令牌压缩
authors: "Zhixuan Liang, Yuxiao Chen, Yurong You, Péter Karkus, Wenhao Ding, Boyi Li, Alexander Popov, Yan Wang (15435), Maximilian Igl, Yiming Li, Danfei Xu, Nikolai Smolyanskiy, Boris Ivanovic, Ping Luo, Marco Pavone"
date: 2026-06-05
pdf: "https://arxiv.org/pdf/2606.07464"
tags: ["query:热点论文筛选", "query:综合方向", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=lead-affiliation; institutions=Nvidia (United Kingdom), University of Hong Kong; query=generalist robot policy"
tldr: "长上下文的单块视觉-动作模型在自动驾驶中产生大量token，超出实时计算预算。现有压缩方法采用基于时间衰减的规则，与规划解耦，易丢失决策关键信息。提出COMPACT-VA，利用条件VQ-VAE实现规划对齐的工作记忆压缩，以历史轨迹和规划意图为条件，后验编码器从未来轨迹中蒸馏意图，先验编码器从压缩观测预测。在动态场景中，成功率提升超6%（达68.3%），速度提升3.3倍，内存减少2.7倍，实现了高效且保留关键信息的上下文压缩。"
source: openalex
selection_source: hot_paper_scout
motivation: 长上下文自动驾驶模型的token序列超出实时预算，现有压缩与规划解耦，导致决策关键信息丢失。
method: 提出COMPACT-VA，基于条件VQ-VAE，以历史轨迹和规划意图为条件压缩，后验编码器从未来轨迹蒸馏意图，先验编码器预测，与策略端到端优化。
result: "动态场景成功率68.3%（提升>6%），速度3.3倍，内存2.7倍，所有指标一致提升。"
conclusion: 规划对齐的压缩能有效保留决策关键信息，实现高效长上下文自动驾驶。
---

## 摘要
单块视觉-动作模型代表了自动驾驶中的一种新兴范式。然而，这种架构在编码用于复杂交互的扩展时间上下文时，产生的令牌序列会迅速超过实时计算预算。虽然线性变换器和外部记忆等方法试图使上下文轻量化，但令牌压缩与架构最为兼容，因为它不需要修改骨干网络。然而，现有的压缩采用基于规则的启发式方法，如时间衰减，与规划解耦，存在丢失决策关键信息的风险。我们提出COMPACT-VA，一个基于条件VQ-VAE的规划对齐工作记忆框架，将扩展上下文压缩为有界表示。压缩条件基于历史轨迹和学习到的规划意图，其中后验编码器在训练期间从未来轨迹中提取规划意图，而先验编码器学习从压缩观测中预测它。压缩记忆与预测的潜变量连接，输入策略进行端到端优化，规划保留了决策关键信息。我们在高信号动态场景中评估，其中历史上下文对行为正确性（例如停车、让行或前行）最为关键，并相应地设计了行为指标。在可比的令牌预算下，我们在成功率上实现了超过6%的提升（68.3%），且各指标一致增益。消融实验验证了规划对齐耦合的有效性。闭环评估证实，COMPACT-VA保持了通用驾驶性能，与未压缩处理相比，加速3.3倍，内存减少2.7倍。

## Abstract
Monolithic vision-action models represent an emerging paradigm in autonomous driving. However, this architecture produces token sequences that quickly exceed real-time computational budgets when encoding extended temporal context for complex interactions. While approaches like linear transformers and external memory try to make the context lightweight, token compression is most compatible with the architecture as it requires no backbone modifications. Yet existing compression adopts rule-based heuristics like temporal decay, decoupled from planning, risking loss of decision-critical information. We propose COMPACT-VA, a planning-aligned working memory framework built on conditional VQ-VAE, compressing extended context into bounded representations. Compression is conditioned on both historical trajectory and a learned planning intent that the posterior encoder distills from future trajectories during training, while the prior encoder learns to predict it from compressed observations. The compressed memory, concatenated with the predicted latent, feeds the policy for end-to-end optimization, planning with retained decision-critical information. We evaluate on high-signal dynamic scenarios where historical context is most critical for behavior correctness (e.g., stop, yield, or proceed), and accordingly design behavioral metrics. Under comparable token budgets, we achieve $>$6% improvement (68.3%) on success rates with consistent gains across metrics. Ablations validate planning-aligned coupling effectiveness. Closed-loop evaluation confirms that COMPACT-VA maintained general driving performance with 3.3* speedup and 2.7* memory reduction over uncompressed processing.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：单块视觉-动作（VA）或视觉-语言-动作（VLA）策略在自动驾驶中直接处理多模态输入并生成轨迹，但当需要编码扩展的时间上下文（例如5-10秒的历史）时，生成的令牌序列会迅速超出实时计算预算。
- **现有方法的不足**：线性变换器和外部记忆等方法虽能减轻上下文负担，但令牌压缩与架构最为兼容（无需修改骨干）。然而，现有压缩采用基于规则的启发式方法（如时间衰减——保留近期帧、丢弃远期帧），这些规则与规划目标解耦，容易被忽略决策关键的历史信息（例如右转规则中的到达顺序）。
- **研究动机**：解决长上下文场景下，压缩过程必须能够自适应地保留对下游规划至关重要的信息，而非依赖静态规则。

## 二、论文提出的方法论

- **核心思想**：提出 COMPACT-VA（COMpression via Planning-Aligned Context Tokens）框架，一种规划对齐的工作记忆机制，通过条件变分自编码器（cVAE）与向量量化（VQ）相耦合，将扩展上下文压缩为有界表示，并端到端优化以保留决策相关信息。
- **关键技术细节**：
  - **分层FIFO记忆缓冲**：将5秒（20帧）历史分为三层（最近4帧无压缩、中间5帧中等压缩、远期11帧强压缩），总令牌从6400降至1424（4.5×压缩），使用Q-former模块进行可学习压缩。
  - **条件VAE框架**：
    - **后验编码器**（训练专用）：从未来轨迹（控制序列离散化）蒸馏出驱动意图潜变量 \(z_q\)，经VQ映射到离散码本。
    - **先验编码器**（训练+推理）：仅从压缩观测中预测潜变量 \(z_p\)，并使用VQ得到 \(z_{skill}\)。
    - **KL散度**促使先验分布匹配后验分布，从而迫使压缩保留足以预测未来意图的信息。
  - **端到端优化**：总损失由轨迹交叉熵、KL散度和提交损失组成，策略骨干在输入中拼接压缩记忆、历史轨迹令牌和预测的 \(z_{skill}\) 令牌进行自回归轨迹预测。

## 三、实验设计

- **数据集与场景**：
  - 使用Alpamayo物理AI数据集（NVIDIA提供）。
  - 特别筛选“高信号动态场景”：四向停止路口（需记忆到达顺序）、停止/让行加动态遮挡（需追踪消失的车辆）、无保护转弯（需评估对向车辆减速趋势）。占数据集约16%。
  - 验证集：20000个20秒片段，每个片段包含一个关键决策点。
- **基准与行为指标**：
  - 主要行为指标：Go Success Rate（Go SR，前行成功率，最依赖记忆）、Stop SR、Roll-Through率（未完全停止）、Stop Position Error、Stop Duration Error。
  - 对比基线：Standard Alpamayo（1s 8帧）、Sparse Obs w/ Long Hist（5s 8帧）、Dense Obs w/ Long Hist（5s 40帧无压缩）、Compression w/o plan-align（分层压缩但无规划对齐），以及COMPACT-VA离散/连续变体。
  - 闭环评估：在Alpasim模拟器上测试910个多样性场景，对比安全指标（碰撞、偏离等）。
- **实验公平性**：所有方法在相同数据集和令牌预算（约1424 vs 1280令牌）下训练，保证可比性。

## 四、资源与算力

- **文中未明确说明**训练使用的GPU型号、数量或总训练时长。仅在效率评估中提到推理时间和内存测量在NVIDIA A100上完成（单次推理平均377ms，峰值内存3.95GB）。推断训练可能在A100集群上完成，但具体资源未公开。

## 五、实验数量与充分性

- **实验组数较多**：包含主要对比（表I：7种设置）、闭环评估（表II：10+指标）、架构消融（表IV：4个变体）、压缩率消融（表V：7种配置）、历史长度消融（表VI：4种长度），以及代码本利用率分析（4个种子）和训练动态观察。
- **充分性与客观性**：
  - 实验设计较为全面，从开放式决策指标到闭环通用性能均有覆盖。
  - 控制变量（令牌数、历史长度、压缩结构）严格，统计均值和标准差，随机种子重复实验。
  - 但仅聚焦于三类停止控制场景（占数据集16%），在通用驾驶场景上改进较小（闭环结果与基线持平），可能低估了记忆依赖更复杂场景的挑战。

## 六、论文的主要结论与发现

- **性能提升**：在可比令牌预算下，COMPACT-VA的Go SR达到68.3%，比标准Alpamayo（63.8%）提升4.5个百分点，比无规划对齐压缩（65.6%）提升2.7个百分点。Roll-Through率降低22%（从9.0%降至7.0%），Stop SR和Stop Duration Error也有改善。
- **效率优势**：相比未压缩的5s 40帧处理，推理加速3.3倍、内存减少2.7倍；相比1s基线，也实现1.32倍加速和33%内存降低。
- **规划对齐有效**：消融实验表明，条件VAE耦合（添加意图潜变量令牌）是性能提升的关键因素，先验-后验一致训练成功迫使压缩保留决策相关信息。
- **代码本利用**：离散码本（K=20）稳定激活15-17个技能，覆盖率80%，未发生模式崩塌。

## 七、优点

- **方法创新性**：首次将规划对齐的思想引入令牌压缩，通过条件VQ-VAE显式地将压缩质量与轨迹预测的变分目标耦合，使模型自动学习保留哪些历史信息，避免了手工规则。
- **针对性评估设计**：聚焦于高信号动态场景，并设计了行为指标（如Go SR、Roll-Through率），比传统的位移指标（如minADE）更直接反映决策正确性，契合实际安全需求。
- **消融实验全面**：对架构组件、压缩率、历史长度均进行了系统对比，验证了每个设计的贡献。
- **闭环验证**：不仅在开放式指标上改进，还在模拟器中验证了通用驾驶性能的维持，增强了方法实用性。

## 八、不足与局限

- **场景覆盖局限**：实验仅聚焦三类停止控制场景（占数据集16%），且开放式验证集中只有一个决策点。对更复杂的长尾场景（如多车交互、严重遮挡）尚未充分验证。
- **通用场景改进不大**：闭环评估中，COMPACT-VA在通用驾驶指标上与1s基线持平，增益主要体现在特定记忆场景，模型泛化能力有待提升。
- **历史长度上限未明确**：消融显示5s 40帧最佳，但80帧（5s更多帧）性能接近甚至略差，暗示模型可能受预训练分布限制，无法有效利用更长或更密集的历史。
- **计算资源未公开**：文中缺乏训练成本（GPU数量、训练时间）的具体数据，限制了复现和工程效率评估。
- **固定码本大小**：K=20的码本虽然利用率高，但可能无法表征更细粒度的驾驶意图变体，对连续决策空间表达能力有限。

（完）
