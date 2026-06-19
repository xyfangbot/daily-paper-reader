---
title: "A New Path: Scaling Vision-and-Language Navigation with Synthetic Instructions and Imitation Learning"
title_zh: 新路径：利用合成指令与模仿学习扩展视觉语言导航
authors: "Aishwarya Kamath, Peter Anderson, Su Wang, Jing Yu Koh, Alexander Ku, Austin Waters, Yinfei Yang, Jason Baldridge, Zarana Parekh"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/020-2023_kamath_scaling_synthetic_instructions-93e654be-e86ebf138c0c.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Synthetic Instructions", "query:Imitation Learning", "query:Data Augmentation", "query:Transformer"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉-语言导航任务因人工指令稀缺和环境多样性不足，智能体在复杂语言理解上表现不佳。本文利用500+室内环境的密集全景采样构建导航轨迹，通过Marky合成多语言指令，并借助GAN生成新视角图像，构建了420万条指令-轨迹对。采用模仿学习训练简单Transformer智能体，在RxR数据集上NDTW在seen环境从71.1提升至79.1，unseen环境从64.6提升至66.8，超越所有现有强化学习智能体。这项工作表明，大规模高质量合成指令与模仿学习是提升指令跟随智能体的有效新路径。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 869, \"height\": 491, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1422, \"height\": 841, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 568, \"height\": 380, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1134, \"height\": 595, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1732, \"height\": 1358, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1732, \"height\": 1359, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1732, \"height\": 1839, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1733, \"height\": 1355, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1733, \"height\": 1834, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1808, \"height\": 350, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1805, \"height\": 458, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1810, \"height\": 532, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1810, \"height\": 597, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1805, \"height\": 502, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-020-e86ebf138c0c-a-new-path-scaling-vision-and-language-navigation-with-synthetic-instructions-and-imitation-learning/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1810, \"height\": 725, \"label\": \"Table\"}]"
motivation: 人工指令数据稀缺且训练环境多样性不足，限制了VLN模型的语言理解和空间推理能力。
method: 从500+室内环境生成导航轨迹，利用Marky合成多语言指令，结合GAN合成新视角图像，构建4.2M指令-轨迹对，并用模仿学习训练Transformer智能体。
result: 在RxR测试集上，NDTW在seen环境中从71.1提升至79.1，unseen环境中从64.6提升至66.8。
conclusion: 大规模高质量合成指令与模仿学习为改进指令跟随智能体提供了有效新路径。
---

## 摘要
近期在视觉语言导航（VLN）领域的研究训练强化学习体在逼真环境中执行自然语言导航指令，朝着能够遵循人类指令的机器人迈进一步。然而，由于人类指令数据稀缺且训练环境多样性有限，这些体在复杂语言基础与空间语言理解方面仍面临困难。基于网络大规模文本和图像-文本数据集的预训练已被广泛探索，但改进有限。我们研究了利用合成指令的大规模增强方法。我们选取500+个以密集采样360°全景图捕获的室内环境，通过这些全景图构建导航轨迹，并使用高质量多语言导航指令生成器Marky为每条轨迹生成视觉基础指令。我们还利用图像到图像的GAN从新视角合成图像观测。由此产生的包含420万对指令-轨迹的数据集比现有的人工标注数据集大两个数量级，且包含更多样的环境和视角。为了高效利用这一规模的数据，我们使用模仿学习训练一个简单的Transformer体。在具有挑战性的RxR数据集上，我们的方法超越了所有现有的强化学习体，在已见环境中将NDTW从71.1提升至79.1，在未见测试环境中从64.6提升至66.8。我们的工作为改进指令遵循体指出了一条新路径，强调在接近人类质量的合成指令上进行大规模训练。

## Abstract
Recent studies in Vision-and-Language Navigation (VLN) train RL agents to execute natural-language navigation instructions in photorealistic environments, as a step towards robots that can follow human instructions. However, given the scarcity of human instruction data and limited diversity in the training environments, these agents still struggle with complex language grounding and spatial language understanding. Pretraining on large text and image-text datasets from the web has been extensively explored but the improvements are limited. We investigate large-scale augmentation with synthetic instructions. We take 500+ indoor environments captured in densely-sampled 360° panoramas, construct navigation trajectories through these panoramas, and generate a visually-grounded instruction for each trajectory using Marky, a high-quality multilingual navigation instruction generator. We also synthesize image observations from novel viewpoints using an image-to-image GAN. The resulting dataset of 4.2M instruction-trajectory pairs is two orders of magnitude larger than existing human-annotated datasets, and contains a wider variety of environments and viewpoints. To efficiently leverage data at this scale, we train a simple transformer agent with imitation learning. On the challenging RxR dataset, our approach outperforms all existing RL agents, improving the state-of-the-art NDTW from 71.1 to 79.1 in seen environments, and from 64.6 to 66.8 in unseen test environments. Our work points to a new path to improving instruction-following agents, emphasizing large-scale training on near-human quality synthetic instructions.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 视觉语言导航（VLN）旨在训练智能体在逼真3D环境中跟随自然语言指令进行导航，是迈向指令遵循机器人的关键步骤。
- 现有瓶颈：
  - **人工指令数据稀缺**：如RxR仅12.6万条、R2R仅2.2万条，标注成本高，语言多样性和环境覆盖有限。
  - **传统预训练提升有限**：使用大规模静态图像-文本数据（如Conceptual Captions）或纯文本数据（如BERT）预训练，因缺乏空间接地和动作导向语言（如“左转”“爬上楼梯”“避开前方房间”），对VLN帮助不大。
  - **强化学习（RL）收敛慢、交互成本高**：多数现有体（如HAMT、EnvEdit）依赖RL，在线交互限制了训练吞吐量。
- 核心假设：**高质量、大规模的合成指令数据，结合模仿学习（IL），可有效弥补人工数据不足，提升空间语言理解能力和导航性能**。

## 二、论文提出的方法论
- **核心思想**：以“更多数据+更简单训练范式”替代“小数据+复杂RL”，利用大规模合成指令进行模仿学习，释放Transformer架构的高吞吐训练潜力。
- **主要技术细节**：
  1. **合成指令生成**：
     - 使用**Marky**（基于mT5的指令生成器，训练自RxR，支持英语/印地语/泰卢固语）为每条轨迹生成接近人类质量的指令。
     - 从**Gibson**（572个室内场景）中自动构建导航图：利用RedNet模型在Matterport3D上训练的导航方向分类器（F1=0.70），结合Habitat Simulator障碍距离、欧氏距离等条件，生成节点-边图，并添加最小生成树保证连通性。
     - 轨迹采样：随机采样3个全景节点，用TSP求解器求最短路径，丢弃>40m或>16步的路径，每环境最多3000条。
     - 结果：**Marky-Gibson数据集**包含320万条指令-轨迹对（平均7.1步、19.3m），加上原Marky-Matterport的100万条，共420万条。
  2. **图像观测增强**：
     - 使用**SE3DS**（图像到图像GAN）合成新视角全景图，对每个Matterport环境生成200种变体，训练时随机采样，50%概率将全景图空间扰动至多1.5m并重渲染。
  3. **智能体架构（MARVAL）**：
     - 基于**mT5**（T5多语言变体）的Transformer编码器，输入包括：指令文本W、历史观测o₁:ₜ₋₁与动作a₁:ₜ₋₁、当前观测oₜ、候选动作集Aₜ。
     - 观测特征：使用MURAL-large（EfficientNet-B7训练于1.8B多语言图像-文本对和6B翻译对）提取640维特征，结合绝对方向嵌入和相对方向嵌入。
     - 历史压缩：对每个历史全景的36个视角特征，用独立Transformer平均池化压缩为单向量。
     - 预训练联合4个任务：掩码语言建模（MLM，15%掩码）、进度预测（20分类）、约束动作预测（从候选Aₜ中分类）、无约束动作预测（从37个离散方向+STOP中分类）。
     - 使用AdaFactor优化器，批大小128，学习率指数衰减（从0.1开始），dropout=0.1。
  4. **训练策略**：
     - **预训练**（420万合成指令+SE3DS）：从头初始化Transformer权重，不依赖任何图像-文本预训练。
     - **微调**（行为克隆BC）：在目标数据集（RxR或R2R）上训练，仅更新WordPiece嵌入，其余权重冻结，dropout=0.2，学习率常数0.001。
     - **DAGGER**（在线模仿学习）：单次迭代，在验证集上让当前策略产生轨迹，由专家（图中最短路径或回溯到真实轨迹最近节点）给出纠正动作，增强训练数据。

## 三、实验设计
- **数据集**：
  - **RxR**（Room-across-Room）：12.6万条人类指令（英/印地/泰卢固语），平均15米轨迹，含非最短路径。
  - **R2R**（Room-to-Room）：1.4万条英语指令，平均10米，严格最短路径。
  - 合成数据：Speaker-Matterport（17.8万条，LSTM生成）、Marky-Matterport（100万条）、Marky-Gibson（320万条）。
- **评估标准**：导航误差（NE↓）、成功率（SR↑）、SPL↑、NDTW↑、SDTW↑。
- **对比方法**：LSTM基线、PREVALENT、RecBERT、EnvDrop+、AirBERT、HAMT、REM、EnvEdit（均为RL体或具有RL组件的体），以及人类表现。
- **主要实验**：
  - 消融研究（Table 2）：逐步添加R2R、RxR、Speaker-MP、Marky-MP、Marky-Gibson、SE3DS、模型大小（base→large），共9组对比。
  - 微调结果（Table 3、Table 4）：在RxR和R2R上对比BC、DAGGER、预探索（Pre-Explore）与所有基线。
  - 语言分解（Table 6）：按英语（en-IN/en-US）、泰卢固语（te-IN）、印地语（hi-IN）分别报告。
  - 错误分析（Figure 4）：统计第一步错误出现的步数分布。
- **公平性**：所有基线使用官方或作者提供的报告结果；EnvEdit结果为三模型集成。

## 四、资源与算力
- **文中未明确说明GPU型号和数量**，仅提到：
  - 预训练使用**mT5-base**（约220M参数）和**mT5-large**（约770M参数）。
  - 批大小128，预训练迭代步数：基础设置最多5.14M步，对应**超过7亿步经验**（含微调）。
  - 使用**AdaFactor**优化器，无额外分布式训练细节。
- 未提及训练总时长、功耗、硬件配置，但鉴于数据规模（420万轨迹×每轨迹平均7步），可推测需大量GPU（如TPU v3或V100集群）运行数天至数周。

## 五、实验数量与充分性
- **实验数量**：较为充分。
  - 预训练消融：9组（Table 2）。
  - 微调结果：RxR上4组（Pretrained, BC, DAGGER, Pre-Explore），R2R上4组。
  - 语言分解：4种语言×2个数据划分。
  - 错误分析：1组分布图。
  - 附录中还提供Val-Seen结果（Table 5）。
- **充分性**：
  - 系统性地验证了各组件（合成指令来源、新环境、新视角、模型容量）的贡献。
  - 与多个SOTA方法对比，指标全面。
  - 在RxR上全面领先，在R2R上非最优但有合理解释（域差异）。
- **客观性**：报告了单次最好结果，但未注明是否多次运行取平均；EnvEdit结果来自三模型集成，对比条件略不对等（但表示公平引用）。

## 六、论文的主要结论与发现
1. **大规模合成指令可显著提升VLN性能**：比传统Speaker模型（LSTM）效果高得多（+27% SR on RxR vs +2%）。
2. **模仿学习（IL）在小数据场景下不如RL，但在大数据量下可超越RL**：MARVAL在RxR Test上NDTW 66.8，优于所有RL基线（EnvEdit 64.6）。
3. **Gibson环境增加多样性是关键**：加入320万Marky-Gibson指令后，RxR Val-Unseen SR提升11%。
4. **新视角合成（SE3DS）有效但部分被环境多样性覆盖**：无Gibson时提升6% SR，有Gibson时仅提升2%。
5. **模型越大效果越好**：mT5-large比mT5-base在RxR Val-Unseen上SR提升2%。
6. **域对齐至关重要**：Marky训练自RxR，因此MARVAL在RxR上SOTA，但在R2R上因指令长度/文化差异而弱于一些经R2R优化的方法（如EnvEdit）。
7. **智能体主要错误发生在后期而非初期**：Figure 4显示MARVAL比人类早期犯错更少，但后期恢复能力不足导致最终成功率仍低（64.8% vs 人类94.5%）。

## 七、优点
1. **数据扩展性极强**：将合成数据从30万条扩展到420万条，环境从61个扩展到500+，是现有工作的两个数量级提升。
2. **方法简洁高效**：仅使用模仿学习（BC+DAGGER）而非复杂RL，训练吞吐量高，易于扩展到更大模型和更多数据。
3. **通用架构**：基于标准mT5 Transformer，可受益于未来更大的预训练多任务模型（如PaLI）。
4. **开源贡献**：发布了Gibson导航图和Marky-Gibson数据集，促进后续研究。
5. **详尽的消融实验**：明确拆解了各组件贡献，为未来数据增强策略提供指导。
6. **语言多模态支持**：合成指令覆盖三种语言，且在每种语言上均有提升。

## 八、不足与局限
1. **合成指令域依赖性强**：Marky基于RxR训练，导致在R2R上提升有限（非SOTA），且无法直接用于其他领域（如户外导航）。
2. **未见环境泛化仍有较大差距**：在RxR Test上NDTW 66.8，远低于人类79.5；且相比已见环境（79.1）下降了12个点，说明过拟合依然存在。
3. **未使用视觉-语言预训练**：虽声称是优点，但与当前许多工作（如CLIP、ViT预训练）相比，可能遗漏了大规模视觉先验，限制上限。
4. **计算资源消耗大**：预训练超过7亿步经验，尽管仅IL，但数据量巨大，实际部署成本高，未提供资源效率对比。
5. **DAGGER仅单次迭代**：虽声称“大部分增益已捕获”，但未探索多轮DAGGER或与其他在线RL结合的可能性，可能错过进一步优化。
6. **对场景结构化信息利用不足**：未利用语义地图、房间类型等高层信息，完全依赖端到端学习，可解释性弱。
7. **性能报告未统计多次运行方差**：可能影响结果的可靠性（尤其当训练噪声大时）。

（完）
