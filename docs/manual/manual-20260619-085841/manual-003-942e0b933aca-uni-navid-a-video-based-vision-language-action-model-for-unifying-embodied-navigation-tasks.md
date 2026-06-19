---
title: "Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks"
title_zh: Uni-NaVid：一种基于视频的视觉-语言-动作模型，用于统一具身导航任务
authors: "Jiazhao Zhang, Kunyu Wang, Shaoan Wang, Minghan Li, Haoran Liu, Songlin Wei, Zhongyuan Wang, Zhizheng Zhang, He Wang"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/003-2024_zhang_uni_navid-b2b5edc3-942e0b933aca.pdf
tags: ["query:手动上传", "paper:PDF", "query:Embodied Navigation", "query:Vision-Language-Action Model", "query:Multi-task Navigation", "query:Online Token Merging", "query:Video-based VLA"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有具身导航方法多针对单一任务，难以自然融合多种导航能力。对此提出Uni-NaVid，一种端到端的视频VLA模型，统一指令跟随、目标搜索等任务，直接输出低级动作。采用在线token合并策略压缩视觉信息，推理速度达5Hz。在3.6M数据上训练，多个基准上取得SOTA，验证了统一框架的有效性。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1868, \"height\": 798, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1887, \"height\": 880, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 910, \"height\": 614, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 913, \"height\": 502, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 918, \"height\": 804, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1874, \"height\": 635, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 924, \"height\": 677, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 922, \"height\": 395, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 910, \"height\": 274, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 648, \"height\": 508, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 912, \"height\": 254, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 924, \"height\": 338, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1693, \"height\": 458, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1684, \"height\": 389, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1681, \"height\": 444, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1679, \"height\": 436, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 82, \"height\": 70, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1797, \"height\": 448, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 81, \"height\": 70, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1774, \"height\": 434, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 80, \"height\": 72, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 82, \"height\": 69, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 1712, \"height\": 452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 1735, \"height\": 461, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 1787, \"height\": 417, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 1744, \"height\": 429, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 1783, \"height\": 436, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 1766, \"height\": 433, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 1700, \"height\": 219, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 1696, \"height\": 216, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-031.webp\", \"caption\": \"\", \"page\": 0, \"index\": 31, \"width\": 1698, \"height\": 214, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-032.webp\", \"caption\": \"\", \"page\": 0, \"index\": 32, \"width\": 1693, \"height\": 219, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/fig-033.webp\", \"caption\": \"\", \"page\": 0, \"index\": 33, \"width\": 1731, \"height\": 325, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 845, \"height\": 238, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 874, \"height\": 655, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 876, \"height\": 396, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 895, \"height\": 371, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 881, \"height\": 409, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 715, \"height\": 300, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 858, \"height\": 339, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 921, \"height\": 295, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 916, \"height\": 495, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 902, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 568, \"height\": 140, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 876, \"height\": 401, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 625, \"height\": 664, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 877, \"height\": 300, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-003-942e0b933aca-uni-navid-a-video-based-vision-language-action-model-for-unifying-embodied-navigation-tasks/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 863, \"height\": 241, \"label\": \"Table\"}]"
motivation: 现有导航模型任务专用，缺乏统一框架，无法利用任务间协同提升性能。
method: 提出视频VLA模型，端到端输入自然语言和RGB视频，输出动作；创新在线token合并策略加速推理。
result: 推理速度5Hz，在多个导航基准上取得SOTA性能。
conclusion: Uni-NaVid统一多种导航任务，通过任务协同提升性能，且仅需单目RGB输入。
---

## 摘要
具身导航是智能机器人的一项基本能力，要求机器人遵循人类指令并在物理环境中自主移动。尽管取得了显著进展，但大多数现有导航方法都针对特定的导航任务，如指令跟随、物体搜索、问题回答、人员跟踪等。然而，对高级具身导航日益增长的需求提出了一个挑战：设计一个能够自然融合多种导航任务并从这些任务间的协同效应中获益的实用导航智能体。为此，我们提出了Uni-NaVid，一种基于视频的视觉-语言-动作（VLA）模型，以统一不同范式的导航任务，并通过促进不同导航子任务之间的协同来提升导航性能。该VLA模型可以直接以自然语言指令和RGB视频流作为输入，并以端到端的方式输出低级机器人动作。为了高效处理大量的RGB视频流，我们提出了一种在线令牌合并策略，该策略在空间和时间上合并相似的视觉信息，从而将推理速度提升至5 Hz。为了训练Uni-NaVid，我们收集了来自不同导航任务的360万条导航数据样本。在多种导航基准上的广泛实验表明，Uni-NaVid仅使用以自我为中心的RGB视频作为输入，便能在统一框架内实现最先进的性能。

## Abstract
Embodied Navigation is a fundamental capability for intelligent robots, requiring robots to follow human commands and move autonomously within physical environments. Despite significant advancements, most existing navigation approaches are tailored to specific navigation tasks, such as instruction following, searching objects, answering questions, tracking people, and more. However, the increasing demands on advanced embodied navigation pose the challenge of designing a practical navigation agent that can incorporate multiple navigation tasks naturally and benefits from the synergy between these tasks. To this end, we present Uni-NaVid, a video-based vision-language-action (VLA) model to unify different paradigms of navigation tasks and improve navigation performance by encouraging the synergy among different navigation sub-tasks. This VLA model can directly take natural language instructions and RGB video streams as inputs and output low-level robotic actions in an end-to-end manner. To efficiently process extensive RGB video streams, we propose an online token merge strategy that spatially and temporally consolidates similar visual information which improves the inference speed to 5 Hz. For training Uni-NaVid, we collect 3.6 million navigation data samples across different navigation tasks. Extensive experiments on diverse navigation benchmarks demonstrate that Uni-NaVid achieves state-of-the-art performance within a unified framework by using only ego-centric RGB video as inputs.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有具身导航方法大多针对单一任务（如视觉语言导航、物体目标导航、具身问答、人员跟随）设计，依赖专用模块和任务特定数据集，缺乏统一框架，无法利用任务间的协同效应来提升整体性能，也难以直接部署于多用途的真实场景。
- **研究动机**：要设计一个实用的通用导航智能体，需要自然地融合多种导航任务，并从中获益。当前基于LLM的方法（如InstructNav、NaviLLM）依赖离散化和预定义图结构，牺牲了输出灵活性并增加了部署难度。而基于视频的VLA模型可以端到端处理RGB视频和语言指令，直接输出低级动作，但面临视频流处理效率低下的挑战。
- **整体含义**：Uni-NaVid提出一种基于视频的VLA模型，通过在线令牌合并策略实现高效推理，并在多任务海量数据（3.6M导航样本 + 2.3M VQA样本）上训练，统一了四种主流导航任务，展示了在仿真和真实环境中的通用导航能力。

## 二、论文提出的方法论
- **核心思想**：构建一个端到端的视频VLA模型，输入自然语言指令和在线捕获的自我中心RGB视频流，输出离散的低级动作（前向、左转、右转、停止）。通过多任务联合训练和高效的在线视觉令牌合并机制，实现通用导航与实时推理。
- **关键技术细节**：
  - **视觉编码**：使用EVA-CLIP将每帧图像编码为256个视觉令牌。
  - **在线视觉令牌合并（Online Visual Token Merging）**：
    - 基于Atkinson-Shiffrin记忆模型，将令牌分为三类：
      - 当前帧令牌（`X_curr`）：用α_curr=2的网格池化压缩为64个令牌。
      - 短期记忆令牌（`X_short`）：最近B=64帧，用α_short=8压缩为4个令牌/帧。
      - 长期记忆令牌（`X_long`）：更早的帧，用α_long=16压缩为1个令牌/帧。
    - 在线更新：新帧到来时，仅对边界帧进行网格池化（如将当前帧压缩后移入短期记忆），并通过余弦相似度融合长期令牌（阈值τ=0.95）。这使历史令牌数量缓慢增长，推理时间稳定在约0.2秒（5Hz）。
  - **动作规划**：合并后的令牌通过两层MLP投影到LLM（Vicuna-7B）的输入空间，与指令令牌拼接，加上导航任务指示符`<NAV>`，然后LLM一次性预测未来4个动作令牌。
- **算法流程**（文字说明）：
  1. 接收当前帧，用EVA-CLIP编码获取256个令牌。
  2. 对当前帧令牌进行2×2网格池化得到64个当前令牌。
  3. 将上一帧的当前令牌（64个）进行8/2=4倍网格池化得到4个令牌，加入短期记忆缓存。
  4. 当短期记忆超过B步时，将最旧的短期令牌进行16/8=2倍网格池化得到1个令牌，尝试与长期记忆末尾令牌合并（若余弦相似度>0.95则加权平均，否则追加为新令牌）。
  5. 最后将所有令牌（长+短+当前）投影后与指令令牌拼接，送入LLM输出4个动作令牌。

## 三、实验设计
- **数据集与场景**：
  - **视觉语言导航（VLN）**：VLN-CE R2R（2.4M样本）、RxR（含在2.4M中），基于HM3D场景。
  - **物体目标导航（ObjectNav）**：HM3D ObjectNav（483k样本），以及零样本评估HM3D-OVON开放词汇基准。
  - **具身问答（EQA）**：MP3D-EQA（240k视频-动作+10k视频-答案样本），以及OpenEQA基准。
  - **人员跟随（Human Following）**：基于Habitat 3.0自建的语言描述人员跟随基准（544k样本），包含8种不同着装的人形角色。
  - **视频理解辅助**：Panda-70M、LLaMA-VID等2.3M开放世界VQA和视频字幕数据。
- **Benchmark**：
  - VLN: R2R Val-Unseen, RxR Val-Unseen (无重叠场景)。
  - ObjectNav: HM3D ObjectNav Val, HM3D-OVON。
  - EQA: MP3D-EQA Val, OpenEQA。
  - Human Following: 自建HM3D基准及跨环境HSSD、MP3D基准。
  - 视频VQA: ScanQA, MSVD-QA, MSRVTT-QA, ActivityNet-QA。
- **对比方法**：
  - VLN: NaVid, HPN+DN, CMA, Sim2Sim, GridMM, HAMT, ETPNav, InstructNav, LAW等。
  - ObjectNav: DD-PPO, Habitat-Web, PIRLNav, OVRL, VLFM, DAgRL等。
  - EQA: NaviLLM, EQA(habitat-lab), GPT-4V等。
  - Human Following: PoliFormer, IBVS（两种检测设置）。
  - 视频VQA: LLaMA-VID, Video-LLaVA, ST-LLM等。

## 四、资源与算力
- 文中明确说明：使用**40块NVIDIA H800 GPU**，训练约**35小时**，总计**1400 GPU小时**。
- 训练分为两阶段：第一阶段预训练投影器（VQA数据），第二阶段联合微调投影器和LLM（导航数据+VQA数据），仅训练1个epoch。

## 五、实验数量与充分性
- **实验数量**：
  - 主实验中，在4个导航任务共8个基准上进行了性能对比（表II~IX），每个基准均与多种基线对比。
  - 消融实验（表X）：包含<Nav>令牌、VQA数据、不同记忆层级（Curr./Short./Long）共7组。
  - 额外消融（表XV）：当前令牌数、τ阈值。
  - 真实世界实验：25个简单指令+25个复杂指令指令跟随（表XI）。
  - 跨数据集实验：移除RxR训练数据后的RxR评估（表XII）；跨环境人员跟随（表XIV）；OpenEQA评估（表XIII）。
  - 效率分析（图12）：与NaVid、LLaMA-VID对比时间和令牌数。
- **充分性与公平性**：
  - 控制变量一致：所有方法均使用相同观测（RGB）和动作空间（连续环境），评测采用各基准默认指标。
  - 多基线对比涵盖传统方法、基于LLM的方法、端到端VLA方法，设置合理。
  - 消融实验覆盖核心设计，验证了各组件贡献。
  - 跨数据集/跨环境实验验证了泛化能力。
  - 真实世界零样本测试增加了实用性验证。

## 六、论文的主要结论与发现
- **性能优越**：Uni-NaVid在VLN R2R上SR=47.0%（+25.7%优于NaVid），RxR上SR=48.7%（+25.1%）；ObjectNav HM3D上SR=73.7%（+4.7%）；EQA上ACC=47.3%（+10.3%优于NaviLLM连续环境）；人员跟随上SR=61.2%（+21.0%优于PoliFormer）。
- **多任务协同**：多任务联合训练相比单任务训练在VLN、ObjectNav、EQA上均有显著提升，人员跟随提升较小（因对该任务历史依赖较少）。
- **数据规模效应**：随训练数据从1M增至5.9M，性能持续提升（增益递减）。
- **在线令牌合并有效**：移除记忆（仅当前帧）导致VLN SR暴跌80.3%；仅当前+短期记忆性能下降但仍优于无记忆；完整记忆策略最佳。
- **真实世界泛化**：零样本部署在多种真实室内环境中成功完成长距离导航、开放词汇物体搜索、人员跟随和复合指令任务。

## 七、优点
- **端到端统一框架**：首次将四种核心导航任务统一到一个VLA模型中，仅需单目RGB视频和自然语言指令，无需姿态、深度或地图等额外传感器。
- **高效的在线令牌合并**：设计基于记忆的令牌分组和在线聚合机制，使推理时间稳定在0.2秒（5Hz），支持非阻塞式实时导航，优于NaVid（~1-2秒）和LLaMA-VID。
- **大规模高质量训练数据**：自建3.6M导航数据（含首个语言描述的人员跟随基准），并整合2.3M开放世界VQA数据，提升了场景理解和泛化能力。
- **前瞻预测**：同时预测未来4步动作，支持异步执行，提高系统鲁棒性。
- **实验全面且扎实**：覆盖仿真和真实环境，跨数据集/跨环境验证，消融实验深入，对比基线强且公平。
- **代码与数据开源**（论文声称将开源），促进社区研究。

## 八、不足与局限
- **任务覆盖有限**：仅包含四个导航任务，其他重要任务（如目标驱动导航、社交导航、多楼层导航）未被纳入，数据可进一步扩充。
- **机器人尺寸假设**：训练数据基于标准尺寸机器人（高度0.88-1.25m，半径0.1-0.6m），未考虑不同尺寸机器人的适应，需要额外处理（如ExAug工作）。
- **动作空间受限**：仅输出离散的低级动作（前向25cm、旋转30°），无法生成连续平滑轨迹，限制了在复杂动态环境中的灵活性。
- **依赖远程服务器**：真实部署需远程服务器（NVIDIA A100）执行模型推理（~0.2s）+网络通信（~0.3s），总延迟约0.5s，且需要稳定WiFi连接，离线/轻量部署不可行。
- **仿真数据多样性瓶颈**：训练数据来自有限合成场景（HM3D/MP3D共861个场景），仿真与真实之间存在“Sim-to-Real”差距，尽管VQA数据有所缓解，但仍可能过拟合特定渲染风格。
- **人员跟随性能受限**：遇到严重遮挡时（如其他家具或人）性能下降，表明需要更多高质量动态场景数据。
- **消融实验细节不足**：部分超参数（如α、B）的消融仅在补充材料中给出单一阈值，缺乏系统扫描。

（完）
