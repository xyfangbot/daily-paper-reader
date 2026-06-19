---
title: "VLN BERT: A Recurrent Vision-and-Language BERT for Navigation"
title_zh: VLN BERT：一种用于导航的循环视觉-语言BERT模型
authors: "Yicong Hong, Qi Wu, Yuankai Qi, Cristian Rodriguez-Opazo, Stephen Gould"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/032-2021_hong_vln_bert-935798c7-73d68d5d66e9.pdf
tags: ["query:手动上传", "paper:PDF", "query:VLN", "query:BERT", "query:Recurrent Navigation", "query:Vision-and-Language", "query:Transformer"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航任务中，现有视觉语言BERT模型因局部可观测马尔可夫过程的时序依赖性而受限。本文提出递归BERT模型，通过引入循环函数维护跨模态状态信息，实现历史感知的注意力与决策。在R2R和REVERIE数据集上取得最优结果，且可泛化至其他Transformer架构，支持预训练并能同时处理导航与指代表达任务。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 861, \"height\": 326, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1800, \"height\": 1010, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 874, \"height\": 515, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 872, \"height\": 796, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1766, \"height\": 369, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1672, \"height\": 2261, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1808, \"height\": 1981, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1814, \"height\": 1653, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1631, \"height\": 700, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1806, \"height\": 393, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1806, \"height\": 423, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 871, \"height\": 196, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 869, \"height\": 170, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 871, \"height\": 279, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-032-73d68d5d66e9-vln-bert-a-recurrent-vision-and-language-bert-for-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 868, \"height\": 199, \"label\": \"Table\"}]"
motivation: 解决现有视觉语言BERT难以适应VLN中部分可观测马尔可夫决策过程的问题。
method: 在BERT中嵌入循环函数，维持跨模态状态信息以实现历史依赖的注意力与决策。
result: 在R2R和REVERIE基准上取得最先进结果。
conclusion: 该方法可替代复杂编解码器，支持预训练与多任务泛化，适用于导航与指代表达。
---

## 摘要
众多视觉-语言任务从视觉与语言（V&L）BERT的应用中显著受益。然而，其在视觉-语言导航（VLN）任务中的应用仍然有限。原因之一是难以将BERT架构适应于VLN中存在的部分可观测马尔可夫决策过程，这需要依赖历史的注意力与决策。本文提出了一种用于VLN的时间感知循环BERT模型。具体地，我们为BERT模型配备了一个循环函数，用于维护智能体的跨模态状态信息。通过在R2R和REVERIE上的广泛实验，我们证明了该模型可以替代更复杂的编码器-解码器模型，达到最先进的结果。此外，我们的方法可推广到其他基于Transformer的架构，支持预训练，并能同时解决导航与指代表达任务。

## Abstract
Accuracy of many visiolinguistic tasks has benefited significantly from the application of vision-and-language (V&L) BERT. However, its application for the task of vision-and-language navigation (VLN) remains limited. One reason for this is the difficulty adapting the BERT architecture to the partially observable Markov decision process present in VLN, requiring history-dependent attention and decision making. In this paper we propose a recurrent BERT model that is time-aware for use in VLN. Specifically, we equip the BERT model with a recurrent function that maintains cross-modal state information for the agent. Through extensive experiments on R2R and REVERIE we demonstrate that our model can replace more complex encoder-decoder models to achieve state-of-the-art results. Moreover, our approach can be generalised to other transformer-based architectures, supports pre-training, and is capable of solving navigation and referring expression tasks simultaneously.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：视觉-语言导航（VLN）任务被建模为**部分可观测马尔可夫决策过程（POMDP）**，智能体需要根据历史观测和当前指令进行决策。现有的视觉-语言BERT（V&L BERT）模型虽然在其他视觉-语言任务上表现出色，但难以直接应用于VLN，因为它们缺乏对时间依赖和部分可观测状态的建模能力。
- **研究背景**：以往工作要么仅将预训练BERT用作语言编码器（如PRESS、PREVALENT），要么用于衡量指令-路径兼容性（如VLN-BERT），而非将BERT本身作为导航网络。同时，VLN中长序列的自注意力计算会消耗大量GPU内存。
- **本文目标**：通过在V&L BERT中引入循环机制，使其能够处理时序依赖输入，从而将预训练跨模态知识直接用于导航学习，替代复杂的编码器-解码器模型，并支持多任务学习（导航与远程指代表达）。

## 二、论文提出的方法论
- **核心思想**：提出**VLN³BERT**，一种递归视觉-语言BERT。在BERT中嵌入**循环函数**，使模型能够维护跨模态状态信息。状态表示作为输入序列的前导token，在每一步通过与语言token和视觉token进行自注意力来更新，并以自回归方式传递到下一步。
- **语言处理**：初始化时，将`[CLS]`、指令词和`[SEP]`输入BERT，`[CLS]`的输出作为初始状态`s₀`。导航阶段，语言token仅作为Key和Value，不再作为Query更新，以节省计算资源。
- **视觉处理**：每一步输入当前视觉观察（场景网格特征和可选的物体区域特征），投影到token空间后与状态和语言token拼接。
- **状态表示与精炼**：
  1. 状态token作为输入序列的首位，通过自注意力更新内容。
  2. **状态精炼**：计算最终层中状态对语言和视觉token的平均注意力权重，对原始特征加权求和，并通过元素级乘积进行跨模态匹配，将匹配结果与状态输出拼接后经线性变换得到精炼状态。
  3. 同时，将所选动作的方向特征也馈入状态，记录历史决策。
- **决策制定**：直接使用最终层状态对各视觉token的平均注意力权重作为动作概率（包括停止动作）；在REVERIE中，物体选择概率也类似计算。
- **训练目标**：结合强化学习（A2C）和模仿学习（IL）的混合损失。RL使用进度奖励、归一化动态时间扭曲奖励和停止惩罚奖励。IL采用教师强制下的交叉熵损失。
- **模型适配**：可适配OSCAR（单流BERT）和PREVALENT（LXMERT-like双流架构）。在PREVALENT中，去除了语言分支的交叉模态编码器，将状态与视觉token进行自注意力。

## 三、实验设计
- **数据集**：使用两个主流VLN基准数据集：
  - **R2R**：室内导航，低层级指令，61个训练场景，11个验证场景，18个测试场景。
  - **REVERIE**：远程指代表达任务，高层级指令，需先导航至目标可视点再选择物体，共4,140个目标物体。
- **评估指标**：
  - R2R：轨迹长度（TL）、导航误差（NE）、成功率（SR）、成功加权路径长度（SPL）。
  - REVERIE：SR、OSR（语义成功率）、SPL、远程接地成功率（RGS）、RGSPL。
- **对比方法**：包括随机基线、Seq2Seq-SF、Speaker-Follower、SMNA、RCM+SIL、PRESS、FAST-Short、EnvDrop、AuxRN、PREVALENT、RelGraph等。还比较了消融实验中的不同组件配置。
- **实验类型**：
  1. **主实验结果**：在R2R和REVERIE的验证可见、验证不可见、测试不可见三个划分上进行单轮（greedy）性能对比。
  2. **消融实验**：分析V&L BERT替换/添加网络组件的影响；比较不同语言自注意力策略（Emb-Attn、Init-Attn、Re-Attn vs Ours）；训练中使用或不使用路径保真奖励；PREVALENT-based模型有无状态精炼。
  3. **学习曲线对比**：比较无初始化、初始化OSCAR、初始化PREVALENT三种设置下的损失和SPL变化。
  4. **注意力可视化**：展示状态-语言注意力随导航进度从指令开头移至结尾，以及状态-视觉注意力对动作选择的影响。

## 四、资源与算力
- **硬件**：所有实验在**单张NVIDIA 2080Ti GPU（11GB显存）**上完成。
- **训练配置**：
  - R2R：batch size为16（RL和IL各半），训练300,000次迭代。
  - REVERIE：batch size为8，训练200,000次迭代。
  - 优化器：AdamW，学习率固定为1e-5。
- **训练时长**：
  - 从OSCAR初始化：约7天完成600,000次迭代（最好结果在约3.5天取得）。
  - 从PREVALENT初始化：约4.5天完成600,000次迭代（最好结果在约1天取得）。
  - 训练时间包含每2,000次迭代在验证集上评估的开销。
- **注意**：论文明确指出其方法无需大规模预训练（OSCAR和PREVALENT权重已是预训练好的），旨在利用已有预训练知识进行导航学习，相比从头训练更高效。

## 五、实验数量与充分性
- **实验数量**：包含主实验两个数据集共6个划分的对比、多组消融实验（组件消融、自注意力策略、奖励、状态精炼）、学习曲线对比、注意力可视化。此外还有附录中的梯度累积实验和REVERIE上的额外消融。
- **充分性**：
  - **对比充分**：与近20种方法进行了比较，覆盖了当时的SoTA方法。
  - **消融覆盖全面**：系统性地验证了V&L BERT替换不同组件、状态精炼、自注意力策略、奖励设计等对性能的影响。
  - **公平性**：所有对比模型在相同数据增强（PREVALENT生成数据）和训练策略下训练，消融实验控制变量。
  - **客观性**：支持多指标对比，包括SR、SPL等；可视化分析辅助理解模型行为。
- **潜在不足**：仅验证了两个数据集（R2R和REVERIE），未在连续环境（如VLN-CE）、对话导航（CVDN）等设置上评估，泛化性验证有限。

## 六、论文的主要结论与发现
1. **递归BERT在VLN中有效**：在V&L BERT中引入循环机制使其能够处理部分可观测的时序依赖，直接作为导航网络可替代复杂编码器-解码器模型。
2. **性能提升显著**：在R2R测试不可见划分上，初始化PREVALENT的方法达到**63% SR**（+8%相对提升），**57% SPL**（+5%）；在REVERIE上导航SR达24.62%，RGS达12.65%，均超越之前最好方法。
3. **预训练知识至关重要**：从预训练OSCAR初始化相比随机初始化带来大幅性能提升；从专门针对VLN预训练的PREVALENT初始化进一步加速收敛并提升性能。
4. **多任务学习潜力**：模型可同时处理导航和远程指代表达任务，在REVERIE上通过目标检测特征实现物体接地，无需独立模块。
5. **注意力可视化验证**：状态注意力随导航进度从指令开头移至结尾，说明模型能够跟踪子指令完成情况；视觉注意力可准确指示所选方向。
6. **计算效率**：通过仅在初始化时自注意力语言token，避免导航阶段对长序列重复计算，使得单GPU即可训练，且性能不降反升。

## 七、优点
- **创新性**：首次将循环机制引入V&L BERT，利用BERT自身架构实现时序依赖推理，无需外部记忆或循环网络。
- **通用性**：可适配多种V&L BERT架构（单流如OSCAR，双流如PREVALENT），具有泛化潜力。
- **高效性**：通过控制语言token仅作为Key/Value，大幅减少计算和内存消耗，支持在单GPU上训练长轨迹。
- **简洁性**：直接使用注意力权重作为动作概率，避免额外复杂解码器；通过状态精炼和跨模态匹配增强状态表达。
- **多任务能力**：同时支持导航和指代表达，无需分别设计模型。
- **实验设计严谨**：多组消融、多指标评估、注意力可视化，提供深入洞察。

## 八、不足与局限
- **数据集验证有限**：仅在R2R（室内）和REVERIE（室内远程指代）上验证，未涉及街道导航（Touchdown）、连续环境（VLN-CE）、对话导航（CVDN）等场景，泛化性结论需谨慎。
- **单GPU训练限制**：尽管方法高效，但梯度累积实验显示更大batch size可能进一步提升性能，受限于11GB显存未充分探索。
- **预训练依赖**：模型性能高度依赖初始的预训练权重（OSCAR/PREVALENT），若缺乏合适的预训练模型，方法效果会大幅下降（消融中随机初始化性能明显劣化）。
- **状态精炼设计针对性强**：跨模态匹配和动作编码设计针对VLN任务，可能不易直接迁移至其他序列决策任务（如对话、动作预测）。
- **未在更长的多步骤任务上测试**：如RxR（Room-Across-Room）具有更长的指令和路径，论文未报告在该类数据集上的结果。
- **训练时间成本**：尽管相比大规模预训练更高效，但单模型训练仍需数天（7天/4.5天），对于快速迭代可能仍显不足。
- **缺乏对失败案例的深入分析**：未讨论模型在哪些场景下容易出错（如复杂岔路、模糊指令等），也未分析OSR与SR的差距。

（完）
