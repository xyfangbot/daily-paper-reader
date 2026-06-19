---
title: "Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments"
title_zh: 视觉与语言导航：在真实环境中解读基于视觉的导航指令
authors: "Peter Anderson, Qi Wu, Damien Teney, Jake Bruce, Mark Johnson, Niko S¨underhauf, Ian Reid, Stephen Gould, Anton van den Hengel"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/017-2018_anderson_r2r_vln-8842e6ee-7578598cb99e.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Matterport3D Simulator", "query:Room-to-Room (R2R) dataset", "query:Natural Language Navigation", "query:Visual Grounding"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉与语言导航（VLN）任务要求机器人根据自然语言指令在真实环境中导航，这类似于视觉问答。现有方法将问题视为视觉化的序列到序列翻译。为推进研究，我们构建了基于真实图像的Matterport3D模拟器，并发布了首个真实建筑中视觉化自然语言导航基准数据集R2R，支持强化学习等方法的评估。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 865, \"height\": 586, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1324, \"height\": 690, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 841, \"height\": 514, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 426, \"height\": 246, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 429, \"height\": 247, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 427, \"height\": 248, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 434, \"height\": 248, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 860, \"height\": 301, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 744, \"height\": 741, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1782, \"height\": 430, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 829, \"height\": 472, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1805, \"height\": 2279, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1547, \"height\": 1113, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 879, \"height\": 676, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-017-7578598cb99e-vision-and-language-navigation-interpreting-visually-grounded-navigation-instructions-in-real-environments/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1794, \"height\": 1807, \"label\": \"Table\"}]"
motivation: 机器人基于视觉理解自然语言导航指令仍是难题，现有视觉语言方法进步显著但缺乏真实环境中的基准数据集。
method: 构建Matterport3D模拟器，基于真实室内图像提供沉浸式环境；创建Room-to-Room (R2R)数据集，包含导航指令与路径对应。
result: R2R数据集作为首个真实建筑内视觉化导航基准，已支持多种序列到序列模型的训练与评估。
conclusion: 该模拟器和数据集降低了VLN研究门槛，有望推动具身智能体在真实场景中的语言理解与导航能力。
---

## 摘要
自从《杰森一家》动画系列想象由一群殷勤的机器人助手带来的悠闲生活之前，能够执行自然语言指令的机器人一直是一个梦想。这是一个仍然顽固地遥不可及的梦想。然而，视觉和语言方法的最新进展在密切相关的领域取得了令人难以置信的进展。这意义重大，因为机器人根据所见之物解读自然语言导航指令的过程，与视觉问答类似，都属于视觉序列到序列的翻译问题，许多相同的方法同样适用。为了促进并鼓励将视觉和语言方法应用于解读基于视觉的导航指令问题，我们提出了Matterport3D模拟器——一个基于真实图像的大规模强化学习环境[11]。利用这一模拟器（未来可支持一系列具身视觉和语言任务），我们提供了首个在真实建筑中进行基于视觉的自然语言导航的基准数据集——Room-to-Room (R2R)数据集。

## Abstract
A robot that can carry out a natural-language instruction has been a dream since before the Jetsons cartoon series imagined a life of leisure mediated by a fleet of attentive robot helpers. It is a dream that remains stubbornly distant. However, recent advances in vision and language methods have made incredible progress in closely related areas. This is significant because a robot interpreting a natural-language navigation instruction on the basis of what it sees is carrying out a vision and language process that is similar to Visual Question Answering. Both tasks can be interpreted as visually grounded sequence-to-sequence translation problems, and many of the same methods are applicable. To enable and encourage the application of vision and language methods to the problem of interpreting visually-grounded navigation instructions, we present the Matterport3D Simulator – a large-scale reinforcement learning environment based on real imagery [11]. Using this simulator, which can in future support a range of embodied vision and language tasks, we provide the first benchmark dataset for visually-grounded natural language navigation in real buildings – the Room-to-Room (R2R) dataset.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：机器人在真实、未预先测绘的室内环境中，如何根据自然语言导航指令，结合视觉观察自主导航到目标位置。这一挑战被称为**视觉与语言导航（VLN）**。
- **研究动机**：虽然自然语言控制机器人的研究已有数十年，但大部分工作要么简化视觉感知（如使用标签替代真实图像），要么在渲染的虚拟环境中进行。这使得模型难以泛化到真实世界的开放集场景。与此同时，视觉问答（VQA）等视觉-语言任务取得了显著进展，但它们不具备移动或控制相机的交互能力。
- **整体含义**：本文首次将序列到序列的视觉-语言方法应用于真实建筑中的导航任务，通过提供大规模、视觉丰富的模拟环境与基准数据集，推动具身智能体在真实场景中的语言理解和导航能力。

## 二、论文提出的方法论
- **核心思想**：将VLN建模为视觉化的序列到序列翻译问题。利用真实世界全景图像构建交互式模拟器，收集人类编写的导航指令，训练基于注意力机制的LSTM序列到序列模型。
- **关键技术细节**：
  1. **Matterport3D Simulator**：基于Matterport3D数据集（90个建筑场景，10,800个全景视点），构建导航图（每个节点对应一个视点，边表示可达路径）。提供离散动作空间：左转、右转、上、下、前进、停止，动作确定且状态相关（只能移动到视野内的可到达视点）。
  2. **R2R数据集**：从导航图中采样7,189条路径（长度5-10m，经过4-6条边），每条路径收集3条众包导航指令（共21,567条，平均词长29词）。指令覆盖多样抽象水平，词汇量约3.1k。
  3. **序列到序列模型**：
     - **编码器**：LSTM逐词读入反向排序的指令词嵌入，输出隐状态序列。
     - **解码器**：在每个时间步，输入当前图像ResNet-152特征和上一动作嵌入，结合LSTM隐状态，通过注意力机制加权指令编码，预测下一动作分布（6个动作）。
     - **训练**：采用两种策略——老师强制（使用真实动作）和学生强制（采样模型预测动作，相当于在线DAGGER）。
     - **实现**：PyTorch，LSTM隐层512，词嵌入256，动作嵌入32，dropout 0.5，Adam优化器，batch size 100，固定迭代次数，测试时贪婪解码。

## 三、实验设计
- **数据集与场景**：使用自建的R2R数据集，基于Matterport3D模拟器。数据划分：61个场景用于训练（14,025条指令），11个场景作为val unseen（2,349条），18个场景作为test（4,173条），另有val seen子集（1,020条，来自训练场景但不同指令）。
- **评价指标**：导航误差（最终位置与目标的最短路径距离）、成功率（误差<3m）、Oracle成功率（若在轨迹中最近点停止则认为成功）。
- **对比方法**：
  - **学习无关基线**：RANDOM（随机转向后前进5步）、SHORTEST（始终走最短路径）。
  - **人类表现**：在测试集1/3的指令上收集人类导航轨迹（AMT），成功率达86.4%。
  - **序列到序列模型**：老师强制（Teacher-forcing）和学生强制（Student-forcing）。
- **实验设置**：所有模型均在同一模拟器上评估，测试集结果通过提交轨迹到服务器获得（未公开目标位置）。

## 四、资源与算力
- **未明确说明**：论文提供了训练细节（PyTorch、Adam、batch size 100、LSTM隐层512），但**未提及使用的GPU型号、数量及训练时长**。文中仅提到“预缓存所有CNN特征”以加速训练，并说明“训练固定迭代次数”，但具体迭代步数未给出。

## 五、实验数量与充分性
- **实验数量**：主要报告了四个实验场景（val seen, val unseen, test）上的结果，对比了RANDOM、Teacher-forcing、Student-forcing和人类。此外，展示了训练过程中的验证损失、导航误差和成功率曲线（Figure 7），以及val seen上成功率的可视化（Figure 8）。
- **充分性评价**：
  - **积极之处**：包含了人类基准，验证了任务的可行性与难度；区分了seen/unseen环境，揭示了泛化挑战；使用Oracle成功率分离了“识别目标”与“停止决策”问题。
  - **不足**：缺乏消融实验（如注意力机制的必要性、图像特征提取方式、动作嵌入大小等）；仅测试了一种模型架构（seq2seq），未尝试强化学习或更复杂的视觉注意力；未在合成环境上对比以验证真实图像的优势。

## 六、论文的主要结论与发现
1. **VLN任务具有挑战性**：人类在测试集上成功率为86.4%，而最优序列到序列模型（student-forcing）仅20.4%。
2. **泛化到未见环境难度显著**：在已见验证集上student-forcing成功率为38.6%，但在未见环境降至21.8%，说明模型严重过拟合到训练环境的视觉特征。
3. **Student-forcing优于Teacher-forcing**：通过采样模型动作训练可探索更多状态，提升了在已见和未见环境中的表现（val seen: 38.6% vs 27.1%; val unseen: 21.8% vs 19.6%）。
4. **现有的视觉-语言方法可直接应用**，但需针对泛化问题进行改进。
5. **众包真实重建场景是高度可扩展的资源**，未来可收集更多建筑数据。

## 七、优点
- **首次构建真实场景下的VLN基准**：使用真实照片而非渲染图像，保留了视觉多样性和开放集特性，更贴近实际机器人应用。
- **模拟器设计兼顾交互性与重复性**：离散动作空间基于导航图，确保不可穿越障碍，同时支持自由相机旋转；提供Python/RL平台接口（OpenAI Gym, ParlAI）。
- **数据集质量高**：指令长度长、词汇丰富，由众包者通过3D交互界面编写，包含多种抽象水平。
- **评估协议清晰**：定义导航误差、成功率及Oracle成功率，并设立测试服务器保证公平比较。
- **开源贡献**：模拟器、数据集和基线模型均已公开，促进社区后续研究。

## 八、不足与局限
- **实验覆盖不足**：仅测试了一种模型（seq2seq LSTM），未探索强化学习、视觉注意力、预训练语言模型等更先进方法；缺乏消融实验分析各组件贡献。
- **资源与算力信息缺失**：未报告训练所需的GPU型号、数量、耗时，不利于复现和比较效率。
- **环境偏差**：Matterport3D数据集中建筑多为整洁、豪华的家庭或办公场所，且几乎无人和动物，可能与真实机器人应用场景存在差异；视点选择偏向“视野良好”的位置，并非机器人可能所处的典型位置。
- **离散动作空间的局限性**：虽然便于训练，但实际机器人需要连续控制，从离散策略到连续控制的迁移尚未验证。
- **泛化挑战未充分解决**：论文指出了泛化难题，但未提出有效解决方案，仅作为事实陈述。
- **指令收集中的潜在偏差**：众包工人可能受“智能机器人”的常见误解影响，导致指令抽象程度不一，模型需适应多种心理模型。

（完）
