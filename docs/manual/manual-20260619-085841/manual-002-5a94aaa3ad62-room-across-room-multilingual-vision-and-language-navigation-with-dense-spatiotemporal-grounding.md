---
title: "Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding"
title_zh: 跨房间：密集时空接地下的多语言视觉与语言导航
authors: "Alexander Ku, Peter Anderson, Roma Patel, Eugene Ie, Jason Baldridge"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/002-2020_ku_rxr-cfa95f03-5a94aaa3ad62.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:multilingual", "query:spatiotemporal grounding", "query:dataset", "query:embodied agents"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有视觉语言导航数据集存在路径偏差和单语言限制。本文提出多语言（英语、印地语、泰卢固语）大规模数据集Room-Across-Room，指令中每个词与创建者/验证者的虚拟姿态时间对齐，提供密集时空标注。基线实验验证了单语、多语及多任务学习设置的效果。模型通过聚焦人类示范中关注的图像区域实现更好导航。该数据集显著拓展了具身语言代理在仿真照片环境中的研究边界。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 783, \"height\": 480, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 798, \"height\": 400, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 794, \"height\": 396, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 396, \"height\": 210, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 403, \"height\": 209, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 404, \"height\": 211, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 400, \"height\": 209, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 402, \"height\": 207, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 398, \"height\": 205, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 399, \"height\": 210, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 399, \"height\": 206, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 404, \"height\": 205, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 394, \"height\": 206, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 402, \"height\": 209, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 810, \"height\": 423, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1651, \"height\": 1722, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 543, \"height\": 277, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 541, \"height\": 276, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 541, \"height\": 279, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 539, \"height\": 279, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 540, \"height\": 280, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 542, \"height\": 279, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 540, \"height\": 280, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 541, \"height\": 277, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 542, \"height\": 279, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 539, \"height\": 278, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 542, \"height\": 279, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 539, \"height\": 277, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 540, \"height\": 280, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 541, \"height\": 278, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-031.webp\", \"caption\": \"\", \"page\": 0, \"index\": 31, \"width\": 542, \"height\": 281, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-032.webp\", \"caption\": \"\", \"page\": 0, \"index\": 32, \"width\": 539, \"height\": 277, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-033.webp\", \"caption\": \"\", \"page\": 0, \"index\": 33, \"width\": 540, \"height\": 275, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-034.webp\", \"caption\": \"\", \"page\": 0, \"index\": 34, \"width\": 544, \"height\": 277, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-035.webp\", \"caption\": \"\", \"page\": 0, \"index\": 35, \"width\": 541, \"height\": 278, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-036.webp\", \"caption\": \"\", \"page\": 0, \"index\": 36, \"width\": 541, \"height\": 279, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-037.webp\", \"caption\": \"\", \"page\": 0, \"index\": 37, \"width\": 540, \"height\": 280, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-038.webp\", \"caption\": \"\", \"page\": 0, \"index\": 38, \"width\": 540, \"height\": 280, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-039.webp\", \"caption\": \"\", \"page\": 0, \"index\": 39, \"width\": 539, \"height\": 280, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-040.webp\", \"caption\": \"\", \"page\": 0, \"index\": 40, \"width\": 541, \"height\": 278, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-041.webp\", \"caption\": \"\", \"page\": 0, \"index\": 41, \"width\": 541, \"height\": 280, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-042.webp\", \"caption\": \"\", \"page\": 0, \"index\": 42, \"width\": 540, \"height\": 279, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-043.webp\", \"caption\": \"\", \"page\": 0, \"index\": 43, \"width\": 539, \"height\": 274, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-044.webp\", \"caption\": \"\", \"page\": 0, \"index\": 44, \"width\": 538, \"height\": 277, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-045.webp\", \"caption\": \"\", \"page\": 0, \"index\": 45, \"width\": 541, \"height\": 277, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-046.webp\", \"caption\": \"\", \"page\": 0, \"index\": 46, \"width\": 540, \"height\": 277, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/fig-047.webp\", \"caption\": \"\", \"page\": 0, \"index\": 47, \"width\": 540, \"height\": 277, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 805, \"height\": 311, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 807, \"height\": 469, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1654, \"height\": 533, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 822, \"height\": 512, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1656, \"height\": 419, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1656, \"height\": 259, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1656, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-002-5a94aaa3ad62-room-across-room-multilingual-vision-and-language-navigation-with-dense-spatiotemporal-grounding/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1654, \"height\": 459, \"label\": \"Table\"}]"
motivation: 现有VLN数据集存在路径偏差且仅含单语言，缺乏细粒度语言与视觉对齐。
method: 构建多语言RxR数据集，每个词与指令创建者/验证者的虚拟姿态时间对齐，并设计从同步姿态轨迹学习的模型。
result: 在单语和多语设置上建立基线，多任务学习提升性能，模型通过聚焦人类关注区域实现更好导航。
conclusion: RxR以其规模、多语言和密集时空标注极大拓展了具身语言代理的研究前沿。
---

## 摘要
我们介绍了Room-Across-Room (RxR)，一个新的视觉与语言导航(VLN)数据集。RxR是多语言的（英语、印地语和泰卢固语），并且比其他VLN数据集更大（更多路径和指令）。它通过解决路径中的已知偏差并引发更多对可见实体的提及，强调了语言在VLN中的作用。此外，指令中的每个单词都与指令创建者和验证者的虚拟姿态进行了时间对齐。我们为单语言和多语言设置以及包含Room-to-Room注释的多任务学习建立了基线分数。我们还提供了一种模型的结果，该模型通过仅关注人类演示中注视的全景部分，从同步的轨迹中学习。RxR的规模、范围和细节极大地拓展了在模拟、逼真环境中具身语言体研究的前沿。

## Abstract
We introduce Room-Across-Room (RxR), a new Vision-and-Language Navigation (VLN) dataset. RxR is multilingual (English, Hindi, and Telugu) and larger (more paths and instructions) than other VLN datasets. It emphasizes the role of language in VLN by addressing known biases in paths and eliciting more references to visible entities. Furthermore, each word in an instruction is time-aligned to the virtual poses of instruction creators and validators. We establish baseline scores for monolingual and multilingual settings and multitask learning when including Room-to-Room annotations. We also provide results for a model that learns from synchronized pose traces by focusing only on portions of the panorama attended to in human demonstrations. The size, scope and detail of RxR dramatically expands the frontier for research on embodied language agents in simulated, photo-realistic environments.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有视觉与语言导航（VLN）数据集存在两大关键局限：一是路径设计存在明显偏差（如路径过短、多为起点到终点最短路径），导致智能体可“作弊”而非真正理解语言；二是数据集均为单语言（英语），限制了研究的泛化性。此外，缺乏细粒度的语言与视觉之间的时空对齐标注。
- **整体含义**：为解决上述问题，本文提出了**Room-Across-Room（RxR）** 数据集——一个多语言（英语、印地语、泰卢固语）、规模更大、路径更长更多样，且每条指令的每个词都与标注者的虚拟姿态序列（位置与视角）精确时间对齐的新VLN基准。该数据集旨在推动具身语言体在复杂真实场景中真正基于语言理解进行导航，而非利用统计捷径。
- **背景**：已有R2R、Touchdown、CVDN、REVERIE等数据集均存在上述局限。RxR通过两阶段路径采样（房间级+全景级）生成非最短路径，并通过贪婪覆盖策略保证全景点的均匀覆盖，从而减少偏置。多语言指令由母语者从头撰写而非翻译，保留了语言在空间和时间编码上的独特性。

## 二、论文提出的方法论
- **核心思想**：构建一个包含密集时空接地（每个词-姿态对齐）的、多语言的、路径多样性高的VLN数据集，并设计能利用人类演示姿态轨迹进行监督训练的模型。
- **关键技术细节**：
  - **两级路径采样**：
    - 高层：在房间图上采样无重复房间的简单路径（最多5个房间，2个楼层）；低层：在由房间序列诱导的全景子图上计算最短路径作为最终全景路径。
    - 满足四个设计原则：路径长度高方差、可间接接近目标、路径自然（无循环/频繁转向）、全景点覆盖均匀。
    - 贪心选择：从所有候选路径中迭代选取使覆盖贡献最大且偏好非最短路径的路径。
  - **数据收集与标注**：
    - **Guide任务**：标注者沉浸于Matterport3D模拟器中，探索给定路径并口头描述，系统记录其6自由度虚拟姿态序列（含时间戳）；标注者随后转录音频，并通过ASR与人工转录对姿态序列进行时间对齐。
    - **Follower任务**：另一标注者听从Guide录音尝试跟随路径，同样记录姿态序列，作为指令质量的验证和额外的训练信号。
    - 每个路径被不同语言圈标注三次；若Follower失败则重新标注。
  - **模型架构**：
    - 基于Reinforced Cross-Modal Matching (RCM) 的变体。
    - 指令编码器：用1D卷积+残差网络代替双向LSTM，以更好处理长指令；使用预训练多语言BERT词嵌入。
    - 视觉特征：预训练的EfficientNet-B4 CNN（在Conceptual Captions上图像-文本双编码器训练）。
    - 解码器：LSTM，每一步通过点积注意力整合全景特征和指令特征，并通过相似度排序选择下一个动作。
  - **接地监督**：
    - 将Guide/Follower姿态轨迹转换为每一步的文本掩码 **b_t**（哪些词已被提及/听到）和视觉掩码 **m_t**（哪些像素已被观察）。
    - 在训练中，当智能体位于正确路径上时，对注意力权重施加交叉熵损失，迫使对掩码为0的无关特征注意力归零，从而模拟人类关注范围。
  - **训练**：使用VALAN分布式强化学习框架，混合行为克隆（50%）和策略梯度（50%），奖励为每一步NDTW增量加最终导航误差线性函数。Adam优化器，100K迭代，batch size 32，学习率1e-4。

## 三、实验设计
- **使用数据集**：
  - **RxR**：含16.5K路径（11,089训练，1,232验证-已见环境，1,517验证-未见环境，2,684测试），每个路径有英、印地、泰卢固三种语言的指令（英语分美式和印式），共126K指令。
  - **R2R** (Room-to-Room)：用于对比和多任务学习。
- **基准与对比方法**：
  - 简单基线：随机行走、随机转向后直走、给定第一步后直走（表4）。
  - 单语模型：仅用英语/印地/泰卢固训练（表5实验1-3）。
  - 多语模型：同时用三种语言训练（表5实验4）。
  - 跨翻译增强：用机器翻译将每种指令翻译成另外两种语言（表5实验5）。
  - 接地监督：对视觉注意力施加掩码损失（表5实验6）。
  - 多任务学习：联合训练RxR和R2R（表6实验8）。
  - 迁移学习：RxR→R2R 或 R2R→RxR（表6实验7与4）。
  - 单模态消融：仅语言、仅视觉（表7实验9-10）。
- **评估指标**：Navigation Error (NE, 低越好), Success Rate (SR, 高越好), Success weighted by normalized inverse Path Length (SPL), Normalized Dynamic Time Warping (NDTW), Success weighted by NDTW (SDTW)。重点使用NDTW/SDTW以更准确衡量路径遵循度。
- **数据集划分**：与R2R/Matterport3D使用相同环境划分，确保公平可比。

## 四、资源与算力
- **明确说明**：论文未明确报告所使用的GPU型号、数量及具体训练时长。仅提到使用**VALAN分布式强化学习框架**，训练配置为100K迭代，batch size 32。训练基于Google Research内部基础设施。
- **需要指出**：由于缺乏具体算力细节，读者难以评估训练成本或复现难度。模型规模（多语言BERT + EfficientNet-B4 + LSTM）相对适中，但强调“分布式”暗示使用了多GPU/TPU。

## 五、实验数量与充分性
- **实验组数**：共约12组主要实验（表5中6组，表6中3组，表7中3组，加上表4简单基线3组，表8最终测试），覆盖单语、多语、多任务、迁移、接地监督、单模态消融等维度。
- **充分性评价**：
  - **较充分**：系统比较了单语vs多语、Guide vs Follower路径、有无接地监督、语言/视觉单模态等核心因素；并设计了多任务和迁移学习实验。
  - **有欠缺**：
    - 接地监督实验（实验6）效果不显著（NDTW稍好但成功率下降），作者仅称“初步探索”，未进行超参数调优或更精细的注意力损失设计。
    - 未与当时最先进的VLN模型（如基于Transformer的Prevalent/R2R_CM2等）对比，基线仅使用RCM变体，可能低估了RxR的挑战性。
    - 未设计交叉语言迁移实验（如用英语训练、印地语测试等），限制了多语言价值的展示。
    - 消融实验仅各做一组，未报告多次重复的均值/方差，统计可靠性未知。
- **客观公平**：数据划分与R2R一致；简单基线在两种数据集上公平对比；人类表现作为上界提供。但模型超参数未专门为每种语言/设置独立调整，可能导致部分结果偏低。

## 六、论文的主要结论与发现
1. **RxR比R2R更具挑战性**：路径更长（平均8步，14.9m vs 5步，9.4m）、非最短路径比例高（44.5%），且简单直走策略效果差（表4）。
2. **单语模型优于多语模型**：联合三种语言训练反而导致性能下降（表5实验4 vs 3），作者认为与多语言机器翻译中的“负迁移”现象一致。
3. **Follower路径有帮助**：同时使用Guide和Follower路径训练优于单独使用任一类（表5实验3 vs 1和2）。
4. **多任务学习有效**：联合R2R和RxR训练在两者上都取得最佳性能（表6实验8），但直接迁移学习因领域差异（路径长度、语言风格）效果不佳。
5. **接地监督效果混合**：视觉注意力监督（Multi*）仅带来NDTW微弱提升，成功率指标略降；文本注意力监督未改善。
6. **人类远优于模型**：人类Follower成功率高达93.9%（NDTW ~79%），而最优模型SR仅约25-30%，NDTW约42-45%，表明巨大提升空间。
7. **单模态消融证实双模态必要**：仅语言模型优于仅视觉模型，但均远不及多模态。

## 七、优点
- **数据集规模与质量**：含126K指令、9.8M词，是R2R的约5-6倍；多语言为英文、印地语、泰卢固语三条线，由母语者原创，保留语言真实特性。
- **密集时空接地**：每个词对齐到姿态序列，比R2R/REVERIE等仅有句子-路径对齐细粒度得多，为细粒度视觉定位、注意力监督等提供基础。
- **路径设计科学**：通过房间级+全景级两级采样有效消除最短路径偏差，路径自然且覆盖均匀，迫使模型真正依赖语言。
- **Follower演示**：既验证了指令质量，又提供了额外的姿态轨迹作为训练信号，模拟了人类解读指令的过程。
- **开源与工具**：数据集、实验代码、标注工具计划公开，便于复现与扩展。

## 八、不足与局限
- **实验验证的局限性**：
  - 接地监督实验效果微弱，且未充分探索如何有效利用姿态掩码（如更复杂的注意力损失或预训练策略）。
  - 未评测当前最先进的VLN方法（如VLN-BERT、HAMT等）在RxR上的表现，基线方法较陈旧（RCM变体），可能低估了RxR的难度。
  - 多语实验仅展示了性能下降，未分析跨语言迁移潜力（如利用多语言预训练模型）。
- **数据集局限**：
  - 仅基于Matterport3D的90个室内环境，场景多样性和真实世界分布有限。
  - 音频文件因隐私审查未公开，限制了听觉-视觉联合研究。
  - 三种语言虽具代表性，但远未覆盖世界语言多样性。
  - 路径生成过程限制了房间个数和楼层数（最多5个房间、2层），存在上限。
- **算力与透明度**：未提供GPU型号、数量及训练时长，不利于资源评估和公平对比。
- **模型局限**：所用CNN/LSTM架构在长序列上可能不如Transformer高效，且未使用预训练的VLN专用模型（如EnvDrop、PREVALENT）。
- **伦理考量**：标注者来自美国/印度，但未详细说明工资水平、工作条件及数据隐私保护（附录仅简要提及）。

（完）
