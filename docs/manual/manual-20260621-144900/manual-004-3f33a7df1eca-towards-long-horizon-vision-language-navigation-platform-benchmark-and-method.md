---
title: "Towards Long-Horizon Vision-Language Navigation: Platform, Benchmark and Method"
title_zh: 面向长程视觉语言导航：平台、基准与方法
authors: "Xinshuai Song, Weixing Chen, Yang Liu, Weikai Chen, Guanbin Li, Liang Lin"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2412.09082v3"
arxiv_id: 2412.09082v3
arxiv_url: "https://arxiv.org/abs/2412.09082v3"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/004-2024_song_lh_vln-7780b44d-3f33a7df1eca.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2412.09082v3", "query:Long-Horizon Vision-Language Navigation", "query:LH-VLN", "query:NavGen", "query:LHPR-VLN", "query:Multi-Granularity Dynamic Memory"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有视觉语言导航方法局限于单阶段任务，难以处理长时域多子场景。本文提出长时域视觉语言导航（LH-VLN）任务，开发自动数据生成平台NavGen，构建含3260个任务、平均150步的LHPR-VLN基准。提出多粒度动态记忆模块MGDM，融合短时模糊与长时检索提升动态环境适应性。新指标ISR/CSR/CGT实现细粒度评估，为长时域导航奠定基础框架。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1548, \"height\": 641, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1539, \"height\": 478, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 688, \"height\": 425, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1622, \"height\": 540, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1659, \"height\": 382, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1789, \"height\": 723, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1687, \"height\": 900, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1666, \"height\": 501, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1309, \"height\": 317, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1756, \"height\": 287, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 822, \"height\": 201, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 866, \"height\": 202, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 845, \"height\": 769, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1491, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1804, \"height\": 447, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-004-3f33a7df1eca-towards-long-horizon-vision-language-navigation-platform-benchmark-and-method/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1844, \"height\": 378, \"label\": \"Table\"}]"
motivation: 现有VLN方法仅适用于单阶段导航，无法应对长时域多子任务场景，亟需长期规划与决策一致性能力。
method: 提出NavGen自动数据生成平台与LHPR-VLN基准，设计多粒度动态记忆MGDM模块，结合短时模糊与长时检索。
result: 构建含3260任务、平均150步的LHPR-VLN基准；提出ISR/CSR/CGT指标；MGDM模块提升动态环境导航灵活性。
conclusion: 平台、基准、指标和模型共同构成LH-VLN基础框架，推动长时域导航研究发展。
---

## 摘要
现有的视觉语言导航方法主要关注单阶段导航，限制了其在复杂动态环境中多阶段和长程任务中的有效性。为应对这些局限，我们提出一种新的视觉语言导航任务——长程视觉语言导航（LH-VLN），强调跨连续子任务的长期规划与决策一致性。此外，为支持LH-VLN，我们开发了自动化数据生成平台NavGen，通过双向多粒度生成方法构建具有复杂任务结构的数据集并提升数据效用。为精确评估复杂任务，我们构建了LH-VLN中的长程规划与推理基准（LHPR-VLN），包含3,260个任务，平均步骤150步，是首个专为长程视觉语言导航任务设计的数据集。进一步，我们提出独立成功率（ISR）、条件成功率（CSR）和基于真实标签的CSR权重（CGT）指标，提供任务完成的细粒度评估。为提升模型在复杂任务中的适应性，我们提出新颖的多粒度动态记忆（MGDM）模块，融合短期记忆模糊与长期记忆检索，实现在动态环境中的灵活导航。我们的平台、基准和方法为LH-VLN提供了稳健的数据生成流水线、全面的模型评估数据集、合理的指标以及新颖的VLN模型，为推进LH-VLN奠定基础框架。

## Abstract
Existing Vision-Language Navigation (VLN) methods primarily focus on single-stage navigation, limiting their effectiveness in multi-stage and long-horizon tasks within complex and dynamic environments. To address these limitations, we propose a novel VLN task, named Long-Horizon Vision-Language Navigation (LH-VLN), which emphasizes long-term planning and decision consistency across consecutive subtasks. Furthermore, to support LH-VLN, we develop an automated data generation platform NavGen, which constructs datasets with complex task structures and improves data utility through a bidirectional, multi-granularity generation approach. To accurately evaluate complex tasks, we construct the Long-Horizon Planning and Reasoning in VLN (LHPR-VLN) benchmark consisting of 3,260 tasks with an average of 150 task steps, serving as the first dataset specifically designed for the long-horizon vision-language navigation task. Furthermore, we propose Independent Success Rate (ISR), Conditional Success Rate (CSR), and CSR weight by Ground Truth (CGT) metrics, to provide fine-grained assessments of task completion. To improve model adaptability in complex tasks, we propose a novel Multi-Granularity Dynamic Memory (MGDM) module that integrates short-term memory blurring with long-term memory retrieval to enable flexible navigation in dynamic environments. Our platform, benchmark and method supply LH-VLN with a robust data generation pipeline, comprehensive model evaluation dataset, reasonable metrics, and a novel VLN model, establishing a foundational framework for advancing LH-VLN.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有视觉语言导航（VLN）方法主要聚焦于单阶段、短时导航任务，任务目标单一、动作序列有限，难以应对真实世界中复杂的、多阶段的长程任务。
- 长程导航要求智能体具备长期规划、持续决策、动态重规划以及跨时段推理的能力，这在自主助手或服务机器人等应用中至关重要。
- 当前缺乏专门针对长程多阶段VLN的任务定义、自动化数据生成平台、高质量基准数据集以及具备自适应记忆能力的模型。
- 本文首次提出长程视觉语言导航（Long-Horizon VLN, LH-VLN）任务，并从**平台（NavGen）**、**基准（LHPR-VLN）** 和**方法（MGDM）** 三方面提供系统解决方案，旨在推动VLN在复杂真实场景中的实用性。

## 二、论文提出的方法论
- **NavGen数据生成平台**：
  - **前向生成**：基于GPT-4和场景资产（HM3D）、机器人配置（Spot/Stretch），通过提示生成多阶段任务指令，并在Habitat3模拟器中由专家模型（navmesh + greedy pathfinder）生成轨迹。
  - **后向生成**：利用轨迹分割算法将复杂任务轨迹分解为连续动作段，结合RAM图像标注模型和GPT-4生成逐步导航指令，实现双向多粒度生成，提高数据多样性和效用。
- **LHPR-VLN基准**：
  - 首个针对LH-VLN的数据集，包含3,260个任务，平均150步，涵盖2~4个子任务，场景来自216个HM3D室内场景。
  - 任务格式：“找到某处某物，将其带到某处某物，然后...”，要求智能体依次完成多个单阶段导航子任务，每个子任务需在目标物体1米内且视角60°内。
- **新评价指标**：
  - **独立成功率（ISR）**：每个子任务的独立成功率。
  - **条件成功率（CSR）**：考虑子任务间依赖的整体任务成功率。
  - **基于真实路径长度的CSR权重（CGT）**：根据真实路径长度加权，更精细评估任务完成情况。
  - 此外保留传统指标（SR、OSR、SPL、NE）以及基于NE的**目标接近率（TAR）**。
- **多粒度动态记忆模型（MGDM）**：
  - **基础模型**：使用预训练视觉编码器（EVA-CLIP ViT）提取多视角图像特征，通过Transformer融合，结合方向嵌入和历史嵌入输入大语言模型（Vicuna 7B）。
  - **CoT反馈模块**：在子任务开始和导航中定期使用GPT-4根据当前观测、历史记忆和任务指令生成思维链，提升任务理解和行动规划。
  - **自适应记忆整合与更新（AMIU）**：
    - **短期记忆**：存储历史观测编码，当记忆长度达到上限时，基于置信度向量的熵最小化进行模糊和遗忘（池化操作），保留关键信息。
    - **长期记忆**：从数据集中检索与当前目标最匹配的观测-动作对（余弦相似度），加权当前决策向量。
    - 最终通过交叉熵损失（模型决策 vs 专家决策）进行训练。

## 三、实验设计
- **模拟器**：Habitat3（连续3D场景），另有部分实验在Isaac Sim（高质量渲染和物理交互）。
- **传感器与动作**：智能体在每个步骤获取前、左（+60°）、右（-60°）三个方向的RGB观测；动作包括前进（+0.25m）、左转（+30°）、右转（-30°）和停止。
- **场景资产**：主要使用HM3D（216个场景语义标注），额外使用HSSD（211个场景）测试数据生成泛化性。
- **机器人配置**：Stretch（轮式+机械臂）和Spot（四足机器人），分别占任务约50%。
- **训练设置**：交替使用模仿学习和轨迹监督学习；LLM为Vicuna 7B v0，视觉编码器为EVA-CLIP ViT（冻结）；优化器Adam，学习率3e-5。
- **对比方法**：
  - Random（随机动作）
  - GLM-4v prompt（零样本）
  - NaviLLM（预训练和微调版本）
  - GPT-4 + NaviLLM（GPT-4分解任务，NaviLLM执行各子任务）
  - InstructNav（零样本，使用额外深度图/顶视图等）
  - 多种MGDM变体（不同LLM/训练策略）
- **实验分组**：
  - **主要实验**：在LH-VLN任务（2~3子任务和3~4子任务）上测试所有模型，报告SR、NE、ISR、CSR、CGT。
  - **逐步导航任务实验**：在单阶段逐步任务上测试部分模型（表3）。
  - **消融实验**：去除自适应记忆、去除长期记忆、去除CoT反馈，分析各组件贡献。
  - **机器人配置对比**：分别测试Spot和Stretch任务性能。
  - **不同LLM/训练策略**：Llama 3 8B vs Vicuna，两阶段训练 vs 交替训练。
  - **数据生成验证**：在Habitat和Isaac Sim中展示NavGen生成的任务和轨迹。

## 四、资源与算力
- 论文中**未明确说明具体使用的GPU型号、数量、训练时长等算力信息**。
- 只提及训练中使用Vicuna 7B v0 LLM和EVA-CLIP ViT视觉编码器，微调时使用Adam优化器，学习率3e-5；替代试验中冻结了Llama 3前五层以适应GPU内存限制。
- 总体而言，算力细节缺失，不利于复现评估。

## 五、实验数量与充分性
- **实验数量**：较为丰富，包括：
  - 核心对比实验（2~3子任务和3~4子任务，共2种难度，8+模型）
  - 逐步导航任务实验（表3）
  - 消融实验（4种设置）
  - 机器人配置对比（Spot vs Stretch）
  - 不同LLM/训练策略对比（表8）
  - 数据生成展示（图8）
- **充分性**：
  - 对比基线多样，覆盖零样本、预训练、微调、任务分解等多种范式。
  - 消融实验设计合理，验证了记忆和CoT模块的重要性。
  - 但是：
    - 所有模型在LH-VLN主任务上的成功率几乎为0（SR=0），仅少数完成部分子任务，表明任务难度极高，但实验未在更简单变体或简化设置下验证，可能限制结论的普适性。
    - 逐步导航实验中MGDM的SR也为0，但OSR较高，暗示模型无法正确执行“停止”动作，但论文未深入分析原因。
    - 缺少与最新端到端VLN模型（如VLN-BERT、HAMT等）的对比，仅对比了NaviLLM和相关变体。
    - 不同机器人配置下的对比有一定价值，但Spot和Stretch训练数据分布均衡，且差异解释存在推测（如Spot的更低视角有利），需要更严格的统计检验。

## 六、论文的主要结论与发现
- 现有VLN模型在LH-VLN任务上表现极差（SR为0），无法理解和完成多阶段复杂任务，凸显LH-VLN的挑战性。
- 将复杂任务分解为单阶段子任务（GPT-4+NaviLLM）可以提升ISR，但整体SR和CGT仍然很低，且对长难子任务表现不如专门设计的MGDM。
- 记忆模块（短期模糊+长期检索）和思维链反馈对长程导航至关重要，消融后性能显著下降。
- 多子任务（3~4子任务）的任务上，各模型的ISR、CSR、CGT反而优于2~3子任务，可能是因为更多子任务使智能体积累更多记忆并提高后续子任务成功率，或者因为子任务间区域关联性更强、平均子任务步数更短。
- MGDM凭借自适应记忆和CoT，在NE指标上显著低于其他模型，且CSR/CGT略优，表现出更好的潜在能力。

## 七、优点
- **任务定义新颖**：首次正式定义长程多阶段VLN任务，填补领域空白。
- **数据平台自动化**：NavGen实现双向多粒度生成，减少人工标注，提升数据规模和多样性。
- **基准全面**：LHPR-VLN包含3,260个任务、216场景、多种子任务数量，平均150步，远超以往VLN数据集。
- **新评价指标合理**：ISR/CSR/CGT从独立子任务、条件依赖、路径难度加权三个角度提供细粒度评估，更适用于复杂任务。
- **记忆模块设计创新**：MGDM融合短期动态模糊（池化+熵最小化）与长期检索加权，有效处理长序列记忆累积和关键信息保留。
- **实验对比充分**：涵盖多种基线，消融实验验证各模块贡献，并考虑不同机器人配置和LLM变体。
- **开源贡献**：提供代码、平台和基准，促进可复现研究。

## 八、不足与局限
- **主任务成功率过低**：所有模型SR近乎为0，说明LH-VLN当前版本任务难度极高，可能超出模型能力范围，缺乏对模型能力梯度的有效区分（除了NE等连续指标）。未来或需设计中等难度子集。
- **缺乏实际物理环境验证**：仅在模拟器（Habitat、Isaac Sim）中实验，未迁移到真实机器人平台，真实场景中的泛化性未知。
- **算力资源未报告**：无法评估训练成本，不利于其他研究者复现和比较。
- **模型在“停止”动作上表现差**：逐步任务中OSR高但SR=0，表明模型难以判断何时完成子任务，但论文未详细分析或提出解决方案。
- **对比基线不够广泛**：缺少与更多主流VLN模型（如VLN-BERT、Seq2Seq、CMA等）的对比，仅以NaviLLM为主，可能低估其他方法的潜力。
- **数据生成依赖GPT-4和外部标注模型**：可能引入语言偏见或场景标注错误，且生成质量未经过充分人工验证。
- **消融实验仅用NE等少数指标**：在ISR、CSR上均为0，导致消融效果主要反映在NE上，但对成功执行能力的提升证据较弱。
- **任务难度不平衡**：分析表明2~3子任务的任务平均子任务步数更长（68 vs 53 vs 51），导致模型表现更差，可能混淆了子任务数量与难度的关系。

（完）
