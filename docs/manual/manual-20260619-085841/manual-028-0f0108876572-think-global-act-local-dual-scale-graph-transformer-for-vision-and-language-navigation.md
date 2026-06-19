---
title: "Think Global, Act Local: Dual-scale Graph Transformer for Vision-and-Language Navigation"
title_zh: 全局思考，局部行动：面向视觉与语言导航的双尺度图变换器
authors: "Shizhe Chen, Pierre-Louis Guhur, Makarand Tapaswi, Cordelia Schmid, Ivan Laptev"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/028-2022_chen_duet-37c88db6-0f0108876572.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Graph Transformer", "query:Topological Map", "query:Dual-scale Encoding", "query:Global Action Planning"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航任务中，智能体需跟随语言指令在未知环境导航。提出双尺度图变换器DUET，在线构建拓扑地图，通过图变换器动态融合局部细尺度观测编码和全局粗尺度地图编码，实现长期动作规划与细粒度语言理解。在REVERIE、SOON基准上显著超越现有方法，在R2R上提升成功率。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1798, \"height\": 521, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 871, \"height\": 722, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 866, \"height\": 300, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1792, \"height\": 699, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 868, \"height\": 755, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 853, \"height\": 939, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 859, \"height\": 911, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1608, \"height\": 1190, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 895, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 865, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 867, \"height\": 338, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 860, \"height\": 278, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 898, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1819, \"height\": 541, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 892, \"height\": 694, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1552, \"height\": 320, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-028-0f0108876572-think-global-act-local-dual-scale-graph-transformer-for-vision-and-language-navigation/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 791, \"height\": 324, \"label\": \"Table\"}]"
motivation: 现有方法在全局动作空间推理与细粒度语言定位之间存在复杂度平衡难题，需同时实现高效探索与精细跨模态理解。
method: 提出DUET，在线构建拓扑地图，利用双尺度图变换器动态组合局部细尺度编码和全局粗尺度编码。
result: 在REVERIE和SOON上显著超越SOTA，在R2R上提升成功率。
conclusion: 双尺度图变换器有效平衡全局探索与局部细粒度理解，为视觉语言导航提供新范式。
---

## 摘要
遵循语言指令在未知环境中导航对于自主具身智能体来说是一个具有挑战性的问题。智能体不仅需要将语言在视觉场景中进行接地，还需要探索环境以到达目标。在这项工作中，我们提出了一种双尺度图变换器（DUET），用于联合长期行动规划和细粒度跨模态理解。我们动态构建拓扑地图，以实现在全局行动空间中的高效探索。为了平衡大行动空间推理的复杂性与细粒度语言接地，我们通过图变换器动态地将局部观测的细尺度编码与全局地图上的粗尺度编码相结合。所提出的方法DUET在面向目标的视觉与语言导航（VLN）基准REVERIE和SOON上显著优于最先进的方法。它还在细粒度VLN基准R2R上提高了成功率。

## Abstract
Following language instructions to navigate in unseen environments is a challenging problem for autonomous embodied agents. The agent not only needs to ground languages in visual scenes, but also should explore the environment to reach its target. In this work, we propose a dual-scale graph transformer (DUET) for joint long-term action planning and fine-grained cross-modal understanding. We build a topological map on-the-fly to enable efficient exploration in global action space. To balance the complexity of large action space reasoning and fine-grained language grounding, we dynamically combine a fine-scale encoding over local observations and a coarse-scale encoding on a global map via graph transformers. The proposed approach, DUET, significantly outperforms state-of-the-art methods on goal-oriented vision-and-language navigation (VLN) benchmarks REVERIE and SOON. It also improves the success rate on the fine-grained VLN benchmark R2R.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- **研究问题**：视觉与语言导航（VLN）要求智能体根据自然语言指令在未知环境中导航至目标。现有方法面临两大短板：
  - 大部分方法（如LSTM、HAMT）只允许局部动作（移动到相邻位置），无法高效执行长期回溯或远距离规划，导致探索效率低、计算开销大。
  - 少数基于拓扑地图的方法（如GBE、SSM）虽支持全局动作，但依赖循环网络进行状态跟踪，且节点仅用粗尺度视觉特征，缺乏细粒度物体和场景的描述能力，难以精确匹配指令中的细节（如“桌子上的植物”）。
- **核心挑战**：如何在保持全局高效探索（大动作空间）的同时，实现细粒度跨模态语言-视觉对齐，且不带来过高的复杂度。
- **整体意义**：提出双尺度图变换器（DUET），通过在线构建拓扑地图并结合粗-细双尺度编码与动态融合，首次在VLN中同时实现长期动作规划和细粒度语言接地，显著提升面向目标（goal-oriented）和细粒度（fine-grained）导航任务性能。

## 二、论文提出的方法论

- **核心思想**：在线构建拓扑地图，并采用双尺度编码（粗尺度：全局地图节点特征；细尺度：当前节点的全景图像+物体特征），通过图变换器进行跨模态融合，动态结合两个尺度的动作预测，以平衡探索与定位。
- **关键技术细节**：
  1. **拓扑地图构建**：每步添加新节点和可导航节点，维护已访问节点、未访问节点和当前节点三类。当前节点使用全景特征（图像+物体）并经自注意力编码；可导航节点从对应视角特征累积平均得到。
  2. **粗尺度跨模态编码器**：
     - 节点嵌入：视觉特征 + 位置编码（方向、距离）+ 导航步编码（最近访问时间）。
     - 图感知自注意力（GASA）：在标准自注意力中加入图邻接距离矩阵学习到的偏置项 \( \mathbf{M} = \mathbf{E}\mathbf{W}_e + \mathbf{b}_e \)，使附近节点获得更高注意力，编码环境布局。
     - 跨注意力层与文本特征交互，输出全局节点表示，预测所有可导航节点（含停止）的分数。
  3. **细尺度跨模态编码器**：
     - 输入：当前节点的全景图像特征、物体特征、指令文本，附加位置嵌入（房间绝对位置、邻居相对方向）。
     - 通过标准跨模态Transformer进行细粒度对齐，输出局部动作分数（停止 + 当前邻居）。
  4. **动态融合**：
     - 将局部分数映射到全局动作空间（对非当前邻居的节点统一赋予回溯分数）。
     - 通过拼接粗尺度的停止节点表示 \( \hat{v}_0 \) 和细尺度的停止表示 \( \hat{r}_0 \)，用Sigmoid生成融合权重 \( \sigma_t \)，最终分数 \( s_i = \sigma_t s_i^{c} + (1-\sigma_t) s_i^{f'} \)。
  5. **训练方法**：
     - 预训练：行为克隆（SAP, OG）+ 辅助任务（MLM, MRC）。
     - 策略微调：结合专家演示（行为克隆）和伪交互演示（PID），即使用当前策略采样轨迹，再用全局最优专家（根据环境图选择最短路径）提供监督标签，平衡分布偏移。损失函数 \( L = \lambda L_{SAP} + L_{PID} + L_{OG} \)，λ取0.2。
  6. **推理**：每步更新地图，预测全局动作，使用Floyd算法规划最短路径执行；超步时强制停止并选取停止概率最大的节点。

## 三、实验设计

- **数据集与场景**：
  - **REVERIE**：目标导向VLN，高层指令（平均21词），需在最后定位物体（给定物体框）。训练/验证/测试房屋数：60/10/16，路径长度4-7步。
  - **SOON**：目标导向，指令更长（47词），物体定位需预测中心点坐标（使用自动检测器）。训练/验证/测试房屋数：34/5/14，路径平均9.5步。
  - **R2R**：细粒度逐步指令（32词），无物体定位，平均6步。
- **对比方法**：
  - REVERIE：Seq2Seq, RCM, SMNA, FAST-MATTN, SIA, RecBERT, Airbert, HAMT等。
  - SOON：GBE。
  - R2R：多组方法，包括序列记忆（HAMT）、地图方法（EGP, GBE, SSM）等。
- **评估指标**：
  - 导航：TL（路径长度）、NE（最终位置误差）、OSR（Oracle成功率）、SR（成功率）、SPL（路径长度加权成功率）。
  - 物体定位：RGS（远程定位成功率）、RGSPL（路径长度加权RGS）。

## 四、资源与算力

- **REVERIE预训练**：2张Nvidia Tesla P100 GPU，batch size 32，训练100k iterations。
- **REVERIE微调**：1张Tesla P100，batch size 8，训练20k iterations，按验证集SPL选择最优epoch。
- **SOON预训练**：batch size 32，40k iterations（单卡？未明确具体GPU数；微调用1张P100，batch 2，40k iterations）。
- **R2R预训练**：batch size 64，200k iterations（未明确GPU数量；微调用batch 8，20k iterations，1张P100）。
- **文中未明确总训练时长或FLOPs**，但给出了迭代数和GPU型号。

## 五、实验数量与充分性

- **消融实验**：在REVERIE验证未见过（val unseen）上进行了多组消融：
  - 单尺度 vs 双尺度融合（表1）：比较粗尺度、细尺度、平均融合、动态融合。
  - 图感知自注意力GASA（表2）：有/无GASA。
  - 训练损失（表3）：SAP、+OG、+Aux（MLM+MRC）、+RL、+PID。
  - 数据增强（表4）：是否使用合成指令。
  - 融合权重平衡因子λ（附录表9）。
  - 回溯比率分析、融合权重阶段分析、错误分析（房间类型、物体定位准确率）。
- **对比实验**：在REVERIE（表6）、SOON（表5）、R2R（表7）上与SOTA全面对比，涵盖三个数据集的所有标准split（val seen, val unseen, test unseen）。
- **定性可视化**：提供多组轨迹图（图5-8），展示与HAMT的对比。
- **充分性评价**：消融覆盖了主要组件（双尺度、GASA、训练策略、数据增强），对比方法全面，且在多个数据集上均有效。但未做更多的超参数搜索（如Transformer层数、注意力头数）的消融，也未在连续环境（如 Matterport3D 连续导航）上测试。

## 六、论文的主要结论与发现

- DUET在REVERIE上大幅超越SOTA：在val unseen上SR提升14.03%，SPL提升3.53%，RGSPL提升5.75%；在test unseen上SR提升22.11%，SPL提升9.39%，RGSPL提升8.98%。
- 在SOON上也显著优于此前唯一方法GBE：test unseen上SR提升20.54%，SPL提升12.19%。
- 在R2R上SR提升4%，但SPL相近（因地图方法回溯造成路径更长）。
- 动态融合优于平均融合和单尺度；GASA对SPL提升明显；伪交互演示（PID）优于强化学习（RL）。
- 双尺度设计有效平衡了全局探索（粗尺度）和细粒度物体定位（细尺度），尤其是在需要远程回溯的场景中。

## 七、优点

- **创新性**：首次将拓扑地图与图变换器结合，并提出动态双尺度融合机制，解决了长期规划与细粒度接地的矛盾。
- **图感知自注意力**：在Transformer中显式编码图拓扑结构，优于单纯视觉相似度注意力。
- **训练策略**：预训练+行为克隆+伪交互演示（PID），避免强化学习的稀疏奖励问题，同时缓解分布偏移。
- **通用性**：方法在目标导向（REVERIE, SOON）和细粒度（R2R）两类VLN任务上均有效，且不依赖物体框（SOON上使用自动检测器）。
- **实验充分**：在多个标准benchmark、多组消融、大规模对比下均展示显著优势；代码/模型开源。

## 八、不足与局限

- **环境限制**：方法仅在离散环境（预先定义的导航图）上验证，未测试连续环境下的泛化能力。
- **细粒度失败分析**：在REVERIE val unseen上仍有29.82%的错误源于停错房间类型，23.20%停对房间但位置偏移；物体定位准确率仅68.43%——细粒度理解仍有提升空间。
- **对语言变化不够鲁棒**：定性例（图8）显示同一轨迹下不同指令导致不同结果，模型可能无法稳定处理指令变体。
- **SOON性能仍较低**：SR仅33.44%（test unseen），受限于训练数据少、指令复杂、自动检测器噪声。
- **未消融架构细节**：未研究不同层数、注意力头数等超参数影响；未对比其他图编码方式（如GCN、GAT）。
- **算力消耗**：多阶段训练（预训练+微调）需大量迭代，但未提供完整训练时间或资源成本对比。

（完）
