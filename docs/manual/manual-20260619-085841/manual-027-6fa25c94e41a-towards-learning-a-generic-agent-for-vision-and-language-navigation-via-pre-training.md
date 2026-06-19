---
title: Towards Learning a Generic Agent for Vision-and-Language Navigation via Pre-training
title_zh: 通过预训练学习用于视觉-语言导航的通用代理
authors: "Weituo Hao, Chunyuan Li, Xiujun Li, Lawrence Carin, Jianfeng Gao"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/027-2020_hao_prevalent-82653881-6fa25c94e41a.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Pre-training", "query:Multimodal Learning", "query:Transformer", "query:Self-supervised Learning"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "视觉语言导航任务要求智能体跟随自然语言指令在环境中导航，但多模态输入变化大且训练数据有限。本文提出首个针对VLN的预训练与微调范式，通过自监督学习在大量图像-文本-动作三元组上预训练PREVALENT模型，学习通用表示。在Room-to-Room基准上，路径加权成功率从47%提升至51%；在视觉对话导航和Help, Anna!任务上也达到新最优。该预训练表示可轻松迁移至其他VLN任务，显著提升泛化能力。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 700, \"height\": 464, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 740, \"height\": 625, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1420, \"height\": 581, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 820, \"height\": 820, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 925, \"height\": 388, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1664, \"height\": 729, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1217, \"height\": 318, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1324, \"height\": 460, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1583, \"height\": 297, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1540, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 772, \"height\": 226, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1282, \"height\": 302, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 878, \"height\": 258, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-027-6fa25c94e41a-towards-learning-a-generic-agent-for-vision-and-language-navigation-via-pre-training/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 884, \"height\": 326, \"label\": \"Table\"}]"
motivation: 现有VLN方法在新任务上训练数据有限，模型泛化能力不足，亟需预训练来学习通用的多模态表示。
method: 提出PREVALENT，采用自监督预训练范式，在图像-文本-动作三元组上学习通用表示，可即插即用地嵌入现有VLN框架。
result: "在Room-to-Room上路径加权成功率提升4个百分点至51%，在视觉对话导航和Help, Anna!任务上均刷新最优。"
conclusion: 预训练范式能有效学习通用多模态表示，显著提升VLN的学习效率和泛化能力，且易于迁移至其他任务。
---

## 摘要
按照自然语言指令在视觉环境中导航是一项具有挑战性的任务，因为智能体的多模态输入高度可变，并且新任务的训练数据通常有限。我们提出了首个用于视觉-语言导航（VLN）任务的预训练和微调范式。通过以自监督学习方式在大量图像-文本-动作三元组上进行训练，预训练模型提供了视觉环境和语言指令的通用表示。它可以轻松地作为现有VLN框架的即插即用模块，从而形成所提出的代理PREVALENT。它在新任务中学习更有效，并在未见过的环境中泛化更好。该性能在三个VLN任务上得到验证。在Room-to-Room基准测试中，我们的模型在按路径长度加权的成功率上将最先进水平从47%提升到51%。此外，学习到的表示可迁移到其他VLN任务。在最近的两个任务——视觉与对话导航以及Help, Anna!中，所提出的PREVALENT相较于现有方法取得了显著改进，达到了新的最先进水平。

## Abstract
Learning to navigate in a visual environment following natural-language instructions is a challenging task, because the multimodal inputs to the agent are highly variable, and the training data on a new task is often limited. We present the first pre-training and fine-tuning paradigm for vision-and-language navigation (VLN) tasks. By training on a large amount of image-text-action triplets in a self-supervised learning manner, the pre-trained model provides generic representations of visual environments and language instructions. It can be easily used as a drop-in for existing VLN frameworks, leading to the proposed agent PREVALENT. It learns more effectively in new tasks and generalizes better in a previously unseen environment. The performance is validated on three VLN tasks. On the Room-to-Room benchmark, our model improves the state-of-the-art from 47% to 51% on success rate weighted by path length. Further, the learned representation is transferable to other VLN tasks. On two recent tasks, vision-and-dialog navigation and Help, Anna!, the proposed PREVALENT leads to significant improvement over existing methods, achieving a new state of the art.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 视觉-语言导航（VLN）要求智能体跟随自然语言指令在照片级室内环境中导航，但多模态输入高度可变，训练数据通常有限。
- 现有方法大多采用序列到序列架构，从零开始独立学习每条指令，缺乏对视觉-语言领域公共知识的利用。
- 指令与轨迹的对齐不完美，单靠指令本身存在歧义，而视觉状态与语言描述共享许多常见形式和关系，因此有必要预先学习一份联合的“常识”表示用于迁移学习。
- 本文提出第一个针对VLN的预训练与微调范式PREVALENT，旨在通过自监督预训练获得通用视觉-语言表示，从而提升新任务上的学习效率和未见环境的泛化能力。

## 二、论文提出的方法论
- **核心思想**：构建一个基于Transformer的编码器，在大量图像-文本-动作三元组上以自监督方式预训练，然后在下游VLN任务上微调。预训练编码器可以即插即用地嵌入现有VLN框架。
- **输入嵌入**：
  - 视觉嵌入：全景视图（36张图像）的ResNet特征（2048维）与方向特征（128维）拼接后通过全连接层和层归一化得到768维向量。
  - 文本嵌入：标准Transformer的token嵌入加位置嵌入，再经层归一化。
- **编码器架构**：多层Transformer，包含两个单模态编码器（分别处理视觉和语言）和一个跨模态编码器。视觉编码器1层，文本编码器9层，跨模态编码器3层。跨模态编码器中查询来自另一模态，键值来自本模态，实现双向注意。
- **预训练目标**：
  1. **图像关注的掩码语言建模（MLM）**：以15%概率随机遮蔽指令中的词，模型需根据上下文词和所有图像特征预测被遮蔽的词。
  2. **动作预测（AP）**：基于[CLS]标记的融合表示，预测当前时间步应执行的动作，使用交叉熵损失。
  总损失为 L = L_MLM + L_AP。
- **预训练数据集**：来自R2R训练集的104K个三元组（已有人工指令）加上由Speaker模型生成的6,482K个三元组（对最短路径轨迹合成指令），总计6,582K个图像-文本-动作三元组，98.4%来自合成数据。

## 三、实验设计
- **三个下游任务**：
  1. **R2R（Room-to-Room）**：给定完整指令从起点导航至目标，评估泛化到未见环境的能力。指标：轨迹长度（TL）、导航误差（NE）、成功率（SR）、路径加权成功率（SPL）。
  2. **CVDN（Cooperative Vision-and-Dialogue Navigation）**：基于多轮对话历史进行导航，指令间接模糊。指标：目标进展（GP）。比较方法：RANDOM、SEQ2SEQ。
  3. **HANNA（Help, Anna!）**：交互式任务，智能体可请求助手给出子任务指令和参考图像。指标：SR、SPL、NE、请求次数（#R）。比较方法：RANDOM WALK、FORWARD 10、NO ASSISTANCE、ANNA等。
- **R2R SoTA对比**：包含RANDOM、SEQ2SEQ、RPA、SPEAKER-FOLLOWER、SMNA、RCM+SIL、REGRETFUL、FAST、ENVDROP、PRESS等9种方法，在验证集已见/未见和测试集未见上比较。
- **消融实验**：
  - 预训练目标消融（L_MLM+L_AP vs 仅L_MLM vs BERT预训练/微调）：在CVDN和HANNA上进行。
  - 特征提取vs微调模式比较：在R2R上，特征提取（固定预训练参数）加上两阶段微调（先特征提取再微调跨注意力层）。
  - 学习曲线分析：PREVALENT vs EnvDrop（R2R）和Seq2Seq（CVDN），观察已见/未见环境性能差距。
- **训练细节**：R2R微调使用同EnvDrop的学习计划；CVDN同原论文；HANNA同原论文。均采用AdamW优化器，给出了具体的batch size和学习率。

## 四、资源与算力
- 预训练：8块NVIDIA V100 GPU，每GPU batch size 96，学习率5×10⁻⁵，AdamW优化器，训练20个epoch。
- 微调：NVIDIA 1080Ti GPU。R2R微调batch size 20（增强监听器）和10（跨注意力层），CVDN batch size 15，HANNA batch size 32。
- 文中未明确说明预训练和微调的总时长（小时数），但提供了迭代步数和epoch数。

## 五、实验数量与充分性
- **实验组数充分**：涵盖3个独立数据集/任务，每个任务均有与多个SoTA的对比（R2R对比9种方法，CVDN和HANNA各对比多种基线）。
- **消融实验覆盖关键因素**：
  - 预训练目标（L_MLM+L_AP vs 仅L_MLM vs BERT）在CVDN和HANNA上均有结果。
  - 特征提取vs微调在R2R上比较。
  - 预训练数据规模影响（合成数据占比）在附录中讨论。
  - 学习曲线定性分析泛化速度。
- **公平性**：与PRESS等模型保持一致的设置（如多指令使用），并在同一评估平台上对比公开排行榜结果。但未进行统计显著性检验。
- **客观性**：所有结果均来自公开排行榜或复现，指标定义清晰。实验设计合理，消融有力证明了各组件贡献。

## 六、论文的主要结论与发现
- 预训练+微调范式在VLN中有效：PREVALENT在R2R测试未见环境上SR达54%（SPL 51%），较之前最好方法提升4个百分点；在CVDN上目标进展远超Seq2Seq；在HANNA未见环境上SR达52.91%，超过ANNA的47.45%。
- 预训练表示可迁移至不同任务（R2R→CVDN、HANNA），且跨任务改进显著。
- 图像关注的MLM（利用视觉上下文）优于纯文本BERT预训练；加入动作预测目标进一步提升性能。
- 预训练缩小了已见/未见环境性能差距，有效缓解过拟合，使模型快速适应新环境。
- 使用合成数据（Speaker模型生成）扩充预训练数据集是可行的，且能提升预训练效果。

## 七、优点
- **方法创新性**：首次将VLN问题纳入预训练-微调范式，提出针对导航任务的视觉-语言-动作联合预训练目标，填补了该领域空白。
- **即插即用**：预训练编码器设计为通用模块，可轻松替换现有VLN框架中的编码部分，兼容性好。
- **全面评估**：在三个难度/模态各异的任务上验证，包含域内和域外迁移，实验覆盖全面。
- **消融深入**：通过对比MLM、AP、BERT基线等，清晰展示了各组件价值；还比较了特征提取与微调策略。
- **实用价值**：相对已有方法在泛化性能上提升显著，且通过学习曲线证明收敛更快，对实际部署有利。
- **开源**：发布代码和预训练模型，可复现性强。

## 八、不足与局限
- **预训练数据依赖合成质量**：98.4%的三元组由Speaker模型生成，合成指令可能存在噪声或不自然，可能影响预训练表示质量。
- **计算资源需求高**：需要8块V100 GPU进行预训练，对研究团队算力门槛较高。
- **任务覆盖范围有限**：仅在Matterport3D模拟器上的三个任务验证，未在Touchdown、REVERIE等数据集或真实机器人上测试，域外泛化范围有限。
- **未消融预训练数据集规模**：虽然用了合成数据扩充，但未设计实验对比不同数据量下的预训练效果，难以判断最小所需数据量。
- **动作预测目标简化**：仅基于当前状态预测下一步动作，忽略了历史依赖性，可能不适用于需要长程规划的复杂场景。
- **未进行统计显著性检验**：实验结果为单次训练或排行榜最佳，缺少多次运行的标准差或显著性分析。
- **跨任务迁移机制分析不足**：虽然观察到性能提升，但对为什么预训练表示能跨任务泛化缺乏深层分析（如特征可视化、注意力分析）。

（完）
