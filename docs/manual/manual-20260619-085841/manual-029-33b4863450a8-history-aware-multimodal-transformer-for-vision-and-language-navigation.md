---
title: History Aware Multimodal Transformer for Vision-and-Language Navigation
title_zh: 历史感知多模态Transformer用于视觉与语言导航
authors: "Shizhe Chen, Pierre-Louis Guhur, Cordelia Schmid, Ivan Laptev"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/029-2021_chen_hamt-5152c860-33b4863450a8.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Multimodal Transformer", "query:Hierarchical Vision Transformer", "query:Long-horizon History", "query:End-to-end Training"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航(VLN)要求智能体根据指令在真实场景中导航，现有方法依赖循环状态记忆历史，但难以处理长距离依赖。本文提出History Aware Multimodal Transformer (HAMT)，通过层次视觉Transformer (ViT) 编码历史全景观测：先对单帧ViT编码，再建模全景内空间关系，最后建模历史中全景间时间关系。HAMT联合文本、历史和当前观测预测下一步动作，经代理任务预训练和强化学习微调。在R2R、RxR、R2R-Last、REVERIE、CVDN、R4R等多项VLN基准上达到新SOTA，尤其显著提升了长轨迹任务的性能。该工作证明了长历史建模对多模态导航决策的重要性。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1434, \"height\": 627, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1452, \"height\": 510, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 507, \"height\": 345, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 724, \"height\": 489, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 575, \"height\": 397, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1442, \"height\": 996, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1436, \"height\": 1030, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1434, \"height\": 740, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1435, \"height\": 911, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1431, \"height\": 983, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1438, \"height\": 866, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1418, \"height\": 242, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 884, \"height\": 303, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 736, \"height\": 299, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 675, \"height\": 264, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 681, \"height\": 286, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1453, \"height\": 475, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 779, \"height\": 374, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1456, \"height\": 268, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 808, \"height\": 266, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 695, \"height\": 273, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1261, \"height\": 438, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1438, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 611, \"height\": 250, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 914, \"height\": 336, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1465, \"height\": 441, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 597, \"height\": 337, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 587, \"height\": 247, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1390, \"height\": 277, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-029-33b4863450a8-history-aware-multimodal-transformer-for-vision-and-language-navigation/table-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 601, \"height\": 335, \"label\": \"Table\"}]"
motivation: 现有VLN方法使用循环状态记忆历史，难以有效建模长距离依赖和复杂空间-时间关系。
method: 提出HAMT，采用层次ViT编码历史全景观测，联合文本、历史和当前观测进行多模态决策，并设计代理任务和强化学习训练。
result: 在R2R、RxR、REVERIE、CVDN和R4R等VLN任务上取得新SOTA，尤其长轨迹导航性能提升显著。
conclusion: 长历史建模是提升VLN性能的关键，HAMT为多模态导航提供了一种高效、可扩展的框架。
---

## 摘要
视觉与语言导航（VLN）旨在构建能够遵循指令并在真实场景中导航的自主视觉智能体。为了记忆先前访问过的位置和采取的动作，大多数VLN方法使用循环状态来实现记忆。相反，我们引入了历史感知多模态Transformer（HAMT），将长时程历史纳入多模态决策中。HAMT通过分层视觉Transformer（ViT）高效编码所有过去的全景观测，该ViT首先使用ViT对单个图像进行编码，然后对全景观测中图像之间的空间关系进行建模，最后考虑历史中全景图之间的时间关系。随后，它联合组合文本、历史和当前观测来预测下一步动作。我们首先使用多个代理任务（包括单步动作预测和空间关系预测）端到端训练HAMT，然后使用强化学习进一步改进导航策略。HAMT在广泛的VLN任务上达到了新的最先进水平，包括细粒度指令导航（R2R、RxR）、高级指令导航（R2R-Last、REVERIE）、对话导航（CVDN）以及长时程VLN（R4R、R2R-Back）。我们证明了HAMT对于较长轨迹的导航任务特别有效。

## Abstract
Vision-and-language navigation (VLN) aims to build autonomous visual agents that follow instructions and navigate in real scenes. To remember previously visited locations and actions taken, most approaches to VLN implement memory using recurrent states. Instead, we introduce a History Aware Multimodal Transformer (HAMT) to incorporate a long-horizon history into multimodal decision making. HAMT efficiently encodes all the past panoramic observations via a hierarchical vision transformer (ViT), which first encodes individual images with ViT, then models spatial relation between images in a panoramic observation and finally takes into account temporal relation between panoramas in the history. It, then, jointly combines text, history and current observation to predict the next action. We first train HAMT end-to-end using several proxy tasks including single step action prediction and spatial relation prediction, and then use reinforcement learning to further improve the navigation policy. HAMT achieves new state of the art on a broad range of VLN tasks, including VLN with fine-grained instructions (R2R, RxR), high-level instructions (R2R-Last, REVERIE), dialogs (CVDN) as well as long-horizon VLN (R4R, R2R-Back). We demonstrate HAMT to be particularly effective for navigation tasks with longer trajectories.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 视觉与语言导航（VLN）要求智能体理解自然语言指令、感知视觉世界并执行导航动作到达目标位置。
- 现有方法主要依赖循环神经网络（RNN）将历史观测与动作压缩为固定大小的状态向量，这种紧凑表示容易丢失长距离依赖信息，例如“把勺子递给我”需要记住起点位置，但早期记忆在循环状态中容易衰减。
- 部分工作尝试构建外部地图记忆或仅编码朝向视角，但依然无法兼顾计算效率与历史信息完整性。本文旨在通过显式编码完整历史序列（而非循环状态）来解决长时程VLN中的记忆与决策问题。

## 二、论文提出的方法论
- **核心思想**：提出 History Aware Multimodal Transformer（HAMT），将全部历史全景观测显式编码为序列，联合文本指令、历史与当前观测进行多模态决策。
- **关键技术细节**：
  - **文本编码**：使用 9 层 BERT 风格的 Transformer 对指令词序列编码，叠加词嵌入、位置嵌入与类型嵌入。
  - **观测编码**：每帧全景图包含 36 个视图，对每个视图的视觉特征（ViT-B/16 提取）与角度特征（heading/elevation 正余弦）进行层归一化后求和，并添加导航类型嵌入（非导航/导航/停止）。
  - **层次历史编码**：先对单帧全景图内 36 个视图进行 ViT 编码（共享参数），再用 2 层全景 Transformer 学习空间关系，得到每个全景的池化表示；然后与朝向视角特征残差连接，加上步数嵌入和类型嵌入，构成时间序列，通过另一个 Transformer 建模全景间的时间关系。计算复杂度从 Flatten 方法的 O(t²K²) 降至 O(tK² + t²)。
  - **跨模态编码**：采用双流架构，文本流和视觉流（历史+观测）各自进行内部自注意力后再执行交叉注意力，共 4 层跨模态 Transformer，输出文本、历史、观测的更新表示。
  - **代理任务训练（五任务）**：
    - MLM：随机遮盖15%指令词，预测原词。
    - MRM：随机遮盖15%观测帧，预测其 ImageNet 类别概率分布（KL 散度损失）。
    - ITM：判断指令与轨迹是否匹配，使用噪声对比估计损失。
    - SAP/SAR：基于当前观测和历史，分类预测导航视角或回归预测朝向角度（模仿学习）。
    - SPREL：自监督预测全景内两个视图的相对空间位置（角度回归）。
  - **两阶段训练策略**：
    - 阶段一：固定 ViT（ImageNet 预训练），训练其他随机初始化模块（200k 迭代）。
    - 阶段二：解冻 ViT，端到端训练全部模块（20k 迭代），ViT 学习率更高以避免梯度消失。
  - **微调阶段**：结合强化学习（A3C）和模仿学习（IL），IL 使用 SAP 损失，RL 基于减少距离与路径对齐奖励，加权系数 λ=0.2。

## 三、实验设计
- **数据集与基准**：覆盖7个VLN任务/数据集：
  - 细粒度指令：R2R（7189条轨迹，90个房屋）、RxR（多语言大规模）。
  - 高级指令：R2R-Last（仅用R2R指令最后一句）、REVERIE（远程物体定位）。
  - 对话导航：CVDN（多轮问答导航）。
  - 长时程VLN：R4R（拼接两个R2R轨迹）、R2R-Back（返回起点）。
- **对比方法**：包括 Seq2Seq、Speaker-Follower、EnvDrop、PRESS、PREVALENT、RelGraph、RecBERT、PTA、RCM 等，部分方法基于 LSTM 或 Transformer。
- **评价指标**：TL、NE、SR、SPL，以及长轨迹专用的 CLS、nDTW、SDTW；CVDN 使用 Goal Progress (GP)。
- **消融实验**：
  - 历史编码方式比较（循环 vs 仅时间 vs 层次）。
  - 代理任务有效性（有无 SAP/R、SPREL）。
  - 视觉特征（ResNet152 vs ViT）及端到端训练。
  - 微调目标（仅IL、仅RL、IL+RL）。
  - 长轨迹任务（R4R、R2R-Back）中历史编码的影响。
  - 不同预测 token 的选择。
- **实验设置**：单次运行（单次推理），报告多次运行结果（均值±标准差或最佳值），保证公平性。

## 四、资源与算力
- **代理任务预训练（阶段一）**：4 块 NVIDIA Tesla P100 GPU，200k 迭代，约 1 天。
- **端到端训练（阶段二）**：20 块 NVIDIA V100 GPU，20k 迭代，约 20 小时。
- **微调阶段**：单 GPU，100k 迭代，学习率 1e-5，batch size 8。
- **备注**：训练使用 R2R 训练集及其增强数据（来自 PREVALENT）；其他数据集未使用增强数据。

## 五、实验数量与充分性
- **实验数量**：在7个不同的VLN任务/数据集上进行了完整对比；包含至少10个以上消融实验组（历史编码、代理任务、视觉表示、微调策略等）；还提供了指令长度分析、计算时间对比、可视化案例。
- **充分性与客观性**：
  - 与多项基线方法在同一标准下对比（相同训练/推理设置），结果报告均值与标准差。
  - 消融实验独立验证各组件贡献，结论一致（层次历史更优、代理任务提升、端到端有益）。
  - 在长轨迹任务上差距尤其显著，验证了方法核心假设。
  - 实验设计全面且公平，但REVERIE的物体接地部分性能逊于SOTA，作者给出了客观解释（ViT特性非目标检测最优）。

## 六、论文的主要结论与发现
- 层次历史编码在性能与计算效率上均优于循环状态和仅时间历史编码。
- 代理任务预训练（尤其是 SAP/R 和 SPREL）显著提升导航精度和泛化能力，在未见环境上 SR 提高 16.7%、SPL 提高 18.0%。
- 端到端优化视觉表示（ViT）对VLN有益（SPL 提升 2.1%），是首次在该任务中验证。
- RL+IL 混合微调优于单独使用任一目标，因为 RL 改善探索，IL 稳定训练。
- HAMT 在 R2R、RxR、R4R、R2R-Back、CVDN、REVERIE、R2R-Last 上均达到 SOTA，在长轨迹任务上提升最显著（如 R4R 的 nDTW 提升 9.5%）。
- 历史信息对于环境理解和指令跟踪至关重要，尤其在需要长期记忆的返回起点任务中提升巨大（R2R-Back SR 提升 39%）。

## 七、优点
- **架构创新**：首次提出完全基于 Transformer 的端到端 VLN 模型，有效编码长时程历史（层次化设计）并联合多模态。
- **训练策略合理**：两阶段训练（先固定 ViT 避免灾难性遗忘，再端到端微调）结合多样化代理任务，学习稳定且泛化强。
- **计算效率权衡**：层次历史编码在保留全景信息的同时降低复杂度，推理时间仅比 RecBERT 慢 10%~50%。
- **实验覆盖广**：涵盖多种 VLN 场景（细粒度、高级、对话、长轨迹），验证了方法的通用性。
- **可复现性**：论文公开了代码、模型和数据增强细节。

## 八、不足与局限
- **计算资源需求较高**：预训练和端到端训练需要多 GPU 集群（20 块 V100），单 GPU 成本较高，可能限制资源有限的研究组。
- **REVERIE 物体接地性能欠佳**：在物体定位（RGS/RGSPL）上不如 SOTA，因为 ViT 特征未针对目标检测优化，且未使用大规模物体检测预训练。
- **泛化到连续动作空间**：目前基于拓扑图离散动作空间，未探索连续动作（如遥控导航），论文仅作为未来工作提及。
- **对专家轨迹依赖**：代理任务和 IL 训练依赖专家演示，在缺乏高质量轨迹的数据集上可能受限。
- **失败案例分析**：可视化显示 HAMT 在异常场景（如特殊材质地面）或罕见物体识别上仍可能出错，表明视觉语义理解仍有不足。
- **训练策略敏感**：论文指出单阶段端到端训练效果差，说明训练顺序和超参数需要精细调节，泛化性有待检验。

（完）
