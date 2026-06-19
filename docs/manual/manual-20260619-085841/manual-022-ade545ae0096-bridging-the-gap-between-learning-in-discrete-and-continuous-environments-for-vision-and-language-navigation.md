---
title: Bridging the Gap Between Learning in Discrete and Continuous Environments for Vision-and-Language Navigation
title_zh: 弥合离散与连续环境中视觉与语言导航学习的差距
authors: "Yicong Hong, Zun Wang, Qi Wu, Stephen Gould"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/022-2022_hong_bridge_discrete_continuous_vln-33900ffc-ade545ae0096.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Discrete-to-Continuous Transfer", "query:Candidate Waypoints Predictor", "query:High-Level Actions", "query:Continuous Environments"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "视觉与语言导航中离散与连续环境存在域差距，离散智能体依赖连接图先验知识，无法直接用于连续环境。本文提出航点预测器，通过优化Matterport3D连接图使之适应Habitat-Matterport3D，并在精炼图上训练，为连续环境生成候选航点，使高层动作智能体如Cross-Modal Matching Agent和VLN-BERT得以迁移；训练时增强航点以多样化视野和路径，提升泛化。在R2R-CE和RxR-CE测试集上，SPL绝对差距分别降低11.76%和18.24%，使用简单模仿学习即达新SOTA；主要贡献在于弥合离散连续鸿沟，推动VLN现实应用。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1808, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 868, \"height\": 348, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 869, \"height\": 331, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1800, \"height\": 541, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 861, \"height\": 448, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 872, \"height\": 414, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 867, \"height\": 746, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1618, \"height\": 2142, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1593, \"height\": 2159, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1532, \"height\": 2086, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1528, \"height\": 2057, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 871, \"height\": 189, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 873, \"height\": 303, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 867, \"height\": 193, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1807, \"height\": 461, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1808, \"height\": 294, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 827, \"height\": 194, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 869, \"height\": 216, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 896, \"height\": 670, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 890, \"height\": 672, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-022-ade545ae0096-bridging-the-gap-between-learning-in-discrete-and-continuous-environments-for-vision-and-language-navigation/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 868, \"height\": 160, \"label\": \"Table\"}]"
motivation: 离散与连续VLN的域差距导致智能体无法跨环境泛化，而连续导航更贴近现实但训练困难。
method: 通过预测器生成候选航点，优化Matterport3D连接图并精炼，使基于高层动作的智能体可迁移至连续环境训练。
result: "在R2R-CE和RxR-CE测试集上，SPL绝对差距分别降低11.76%和18.24%，使用简单模仿学习即达新SOTA，大幅超越先前方法。"
conclusion: 提出弥合离散与连续VLN差距的方法，显著提升连续环境导航性能，推动VLN现实应用。
---

## 摘要
现有大多数视觉与语言导航（VLN）研究集中于离散或连续环境，训练的智能体无法跨两者泛化。尽管在连续空间中学习导航更接近现实世界，但训练此类智能体比训练离散空间中的智能体困难得多。然而，由于领域差距，离散VLN的最新进展难以迁移到连续VLN。两种设置的根本区别在于，离散导航假设对环境连通图有先验知识，从而智能体可以通过将导航方向图像作为锚点，将低层控制的导航问题有效转化为高层动作的节点跳跃。为弥合离散到连续的差距，我们提出一种预测器，在导航过程中生成一组候选路径点，从而使设计为高层动作的智能体能够迁移到连续环境并在此训练。我们精炼Matterport3D的连通图以适配连续的Habitat-Matterport3D，并利用精炼后的图训练路径点预测器，使其在每个时间步生成可达路径点。此外，我们证明在训练期间可以增强预测路径点，以多样化视野和路径，从而提升智能体的泛化能力。通过大量实验，我们展示了使用预测路径点在连续环境中导航的智能体性能显著优于使用低层动作的智能体，将Cross-Modal Matching Agent的绝对离散到连续差距减小了11.76%的SPL（按路径长度加权的成功率），VLN-BERT减小了18.24%的SPL。我们的智能体仅通过简单的模仿学习目标训练，就大幅超越了之前的方法，在R2R-CE和RxR-CE数据集的测试环境中取得了新的最优结果。

## Abstract
Most existing works in vision-and-language navigation (VLN) focus on either discrete or continuous environments, training agents that cannot generalize across the two. Although learning to navigate in continuous spaces is closer to the real-world, training such an agent is significantly more difficult than training an agent in discrete spaces. However, recent advances in discrete VLN are challenging to translate to continuous VLN due to the domain gap. The fundamental difference between the two setups is that discrete navigation assumes prior knowledge of the connectivity graph of the environment, so that the agent can effectively transfer the problem of navigation with low-level controls to jumping from node to node with high-level actions by grounding to an image of a navigable direction. To bridge the discrete-to-continuous gap, we propose a predictor to generate a set of candidate waypoints during navigation, so that agents designed with high-level actions can be transferred to and trained in continuous environments. We refine the connectivity graph of Matterport3D to fit the continuous Habitat-Matterport3D, and train the waypoints predictor with the refined graphs to produce accessible waypoints at each time step. Moreover, we demonstrate that the predicted waypoints can be augmented during training to diversify the views and paths, and therefore enhance agent's generalization ability. Through extensive experiments we show that agents navigating in continuous environments with predicted waypoints perform significantly better than agents using low-level actions, which reduces the absolute discrete-to-continuous gap by 11.76% Success Weighted by Path Length (SPL) for the Cross-Modal Matching Agent and 18.24% SPL for the VLN-BERT. Our agents, trained with a simple imitation learning objective, outperform previous methods by a large margin, achieving new state-of-the-art results on the testing environments of the R2R-CE and the RxR-CE datasets.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- 视觉与语言导航（VLN）任务要求智能体根据自然语言指令在未知环境中执行动作序列。目前存在两种主流的实验场景：**离散环境**（基于预先定义的连通图，智能体可进行全景视角的高层动作，如节点间跳跃）和**连续环境**（智能体需执行低层控制，如“前进0.25米”、“左转15度”）。
- 离散环境中的智能体训练更高效，大量先进方法（如基于预训练视觉‑语言Transformer、场景记忆、数据增强等）均在此类环境下取得突破，但这些方法无法直接迁移到连续环境中。连续环境更接近真实世界，但训练难度显著更高。两类场景之间存在巨大的**域差距**，导致约20%的成功率差距。
- 核心问题：**如何弥合离散与连续环境中VLN的域差距，使原本基于高层动作的智能体能够有效适应连续环境？**
- 本文认为根本差异在于离散导航依赖连通图提供的**可导航先验**，连续环境缺少此信息。因此，核心思路是**在连续环境中实时预测候选路径点**，从而重建类似离散导航的高层动作空间。

## 二、论文提出的方法论

- **核心思想**：提出一个**候选路径点预测器**，在连续环境中每个时间步从RGB‑D全景观测中推断出智能体周围可达的路径点，作为高层动作的候选位置。智能体选择其中一个路径点后，再将高层动作分解为低层控制逐步执行。这样离散环境的导航方法可直接应用到连续环境中。
- **关键技术细节**：
  1. **路径点预测器网络结构**：
     - 输入：12张RGB和12张深度图像（每30°一张，共360°全景），分别用两个ResNet‑50编码（一个ImageNet预训练，一个DDPPO预训练）。
     - Transformer模块：两层、每层12个自注意力头，建模相邻视角间的空间关系。
     - 分类器：MLP将Transformer输出映射为**120个角度×12个距离**的热力图（角度步长3°，距离0.25m~3.00m，步长0.25m）。
     - 通过非极大值抑制（NMS）从热力图中提取最多**5个**候选路径点。
  2. **训练数据构建**：
     - 将原始Matterport3D（MP3D）的连通图投影到Habitat‑MP3D连续空间，并手工修正无效节点/边（移除穿过障碍物的边、合并过近节点、添加新节点以保证连通性），得到精炼图$G^∗$。
     - 在每个节点处，将其3米半径内的邻域离散化为120×12网格，将真实路径点转化为高斯分布热力图，作为训练标签。
  3. **迁移与训练**：
     - 将两个代表性的离散VLN智能体（CMA和VLN-BERT）迁移到连续环境，每个时间步使用预测路径点进行**视角选择**（选择具有最高匹配概率的路径点）。
     - 训练时引入**路径点增强**：从选中视角对应的热力图斑块中随机采样新路径点，使智能体接触到不同的观测和步长，提升泛化能力。
  4. **训练损失**：预测器训练采用MSE损失；导航智能体采用交叉熵模仿学习损失，结合调度采样（schedule sampling）逐渐从教师强制过渡到学生采样。

## 三、实验设计

- **数据集与场景**：
  - **R2R‑CE**：基于R2R数据集在Habitat‑MP3D连续环境中生成的版本。
  - **RxR‑CE**：多语言（英语、印地语、泰卢固语）连续VLN数据集。
  - 均使用Habitat模拟器，验证集分为Seen（可见环境）和Unseen（未见环境），测试集为保留环境。
- **基准与对比方法**：
  - 对比了低层动作基线（原始VLN‑CE）、使用真实连通图的高层动作、固定步长视角选择等消融实验。
  - 与已有SOTA方法比较：VLN‑CE [33]、LAW [45]、SASRA [29]、Waypoint Models [32]。
- **主要评估指标**：SR（成功率）、SPL（按路径长度加权成功率）、nDTW（归一化动态时间扭曲）、SDTW（加权的nDTW）、NE（导航误差）、TL（轨迹长度）。

## 四、资源与算力

- 论文明确说明了硬件与训练规模：
  - **硬件**：单块NVIDIA RTX 3090 GPU。
  - 路径点预测器：学习率$10^{-6}$，batch size 64，使用AdamW优化器。
  - 导航智能体训练：
    - R2R‑CE：CMA和VLN‑BERT各训练50个epoch，batch size 16，**每模型约3.5天**。
    - RxR‑CE：CMA训练约3天/语言，VLN‑BERT约3天/语言（batch size分别为16和8，共25个epoch）。

## 五、实验数量与充分性

- 实验组别丰富，覆盖以下维度：
  1. **消融实验**：表1和表2量化了“视角选择”和“路径点传送”两个机制各自的价值；表3对比了不同路径点预测器（基线、U‑Net、本文Transformer）的性能。
  2. **核心对比**：表4在过滤后的数据集上对比了使用真实图、冻结预测器、增强预测器以及低层动作的CMA和VLN‑BERT，共10组配置。
  3. **SOTA对比**：表5（R2R‑CE）和表6（RxR‑CE）对比了与过去5种方法的性能，覆盖Seen、Unseen、Test三个子集。
  4. **附加分析**：附录中对比了MP3D图与Habitat‑MP3D图的性能差异、滑动/非滑动的影响等。
- 实验充分性评价：
  - 消融实验系统性地隔离了各个组件的影响，验证了路径点预测器和增强机制的有效性。
  - 对比的方法均为近年的代表性工作，公平性由标准数据集和官方评估服务器保证。
  - 但仅用MSE损失训练预测器，且仅训练**61个环境**（共90个场景，保留18个用于测试），训练数据覆盖可能不足。
- 总体而言，实验设计客观、公平，结论可靠。

## 六、论文的主要结论与发现

1. **高层动作（视角选择+路径点传送）是离散环境优势的关键**。消融实验表明，仅提供可导航方向即可大幅缩小性能差距。
2. **提出的路径点预测器可有效替代真实连通图**。在CMA上，使用冻结预测器在Val‑Unseen上达到与真实图几乎相同的SPL（33.90% vs 33.89%）；在VLN‑BERT上差距从18.69%缩小到2%以内。
3. **路径点增强进一步提升泛化能力**，使智能体在未见环境中的SPL甚至超过使用真实图的结果。
4. **与现有SOTA方法比较**：
   - R2R‑CE Test：CMA SPL 33%（比Waypoint Models 30%高3%），VLN‑BERT SPL 36%（比前者高6%）。
   - RxR‑CE Test：nDTW分别达到37.39%和37.30%，SR约24%，大幅超越VLN‑CE基线。
5. **简单模仿学习即可获得优异表现**，无需复杂强化学习或多GPU大规模训练。

## 七、优点

1. **创新性**：巧妙地利用路径点预测器将离散环境的高层动作范式无缝迁移到连续环境，思路简洁有效。
2. **通用性**：方法不依赖特定导航网络，在CMA（LSTM序列模型）和VLN‑BERT（Transformer预训练模型）上都有效，表明其通用性。
3. **效率**：仅使用单GPU和简单交叉熵损失，训练成本远低于已有的Waypoint Models（需要64个GPU和DDPPO策略），但性能更优。
4. **消融完整**：系统量化了视角选择和传送各自的贡献，以及路径点增强的效果，论证充分。
5. **可复现性好**：公开了代码和训练好的模型，详细说明了图构造、数据过滤等细节。

## 八、不足与局限

1. **路径点预测器的训练数据有限**：仅使用61个环境的9566个节点训练，对于罕见空间结构（如楼梯）预测效果差（见附录图11），可能导致导航失败。
2. **固定预测数量**：强行限制最多5个候选路径点，在某些宽敞空间可能不足（例如大厅中可能有6个以上可导航方向）。
3. **预测器无在线调整机制**：智能体完全信任预测的路径点，一旦预测失败（如楼梯处无路点），无法自救。在RxR‑CE中问题更严重，易导致死锁。
4. **评价覆盖不够全面**：主要报告SPL/nDTW等宏观指标，未详细分析失败案例的分布（如障碍物碰撞、路径不可达的比例）。附录仅给出少量可视化。
5. **域外泛化未验证**：仅在Habitat‑MP3D场景内测试，未验证在Gibson、AI2‑THOR等其他连续环境中的性能。
6. **依赖弱监督**：训练预测器需要精炼的连通图（手工修正过），获取成本较高；未来可探索无图或弱监督方法。
7. **缺少利用智能体状态信息**：预测器仅基于当前观测，不考虑导航进度、指令中的地标等信息，可能生成次优路径点。

（完）
