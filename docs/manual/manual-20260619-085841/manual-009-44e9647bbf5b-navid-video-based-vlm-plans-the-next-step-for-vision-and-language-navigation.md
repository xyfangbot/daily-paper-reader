---
title: "NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation"
title_zh: NaVid：基于视频的VLM为视觉语言导航规划下一步行动
authors: "Jiazhao Zhang, Kunyu Wang, Rongtao Xu, Gengze Zhou, Yicong Hong, Xiaomeng Fang, Qi Wu, Zhizheng Zhang, He Wang"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/009-2024_zhang_navid-c09da9f3-44e9647bbf5b.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Video-based VLM", "query:Embodied AI", "query:Sim-to-Real Transfer", "query:Generalization"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航长期面临跨分布场景和仿真到真实环境的泛化挑战。本文提出NaVid，仅需单目相机视频流即可输出下一步动作，无需地图、里程计或深度输入。模型采用五十一万导航样本和七十六万网页数据训练，在仿真和真实世界均达到最优性能，展现出卓越的跨数据集和仿真到真实迁移能力。该工作展示了视觉语言模型在导航中的巨大潜力，为简化导航设置和推动研究提供了全新范式。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 884, \"height\": 587, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1749, \"height\": 1024, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 862, \"height\": 256, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 892, \"height\": 301, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 874, \"height\": 427, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 903, \"height\": 479, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 902, \"height\": 513, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1807, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1705, \"height\": 476, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 916, \"height\": 645, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 914, \"height\": 578, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 559, \"height\": 421, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 922, \"height\": 245, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 921, \"height\": 195, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1736, \"height\": 203, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1722, \"height\": 197, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1729, \"height\": 196, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1742, \"height\": 198, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1738, \"height\": 203, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1743, \"height\": 200, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1707, \"height\": 472, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 1705, \"height\": 469, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 1711, \"height\": 465, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 1743, \"height\": 471, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 85, \"height\": 76, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 1758, \"height\": 469, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 1762, \"height\": 466, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 1772, \"height\": 469, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 1797, \"height\": 477, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 1663, \"height\": 455, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-031.webp\", \"caption\": \"\", \"page\": 0, \"index\": 31, \"width\": 1667, \"height\": 457, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-032.webp\", \"caption\": \"\", \"page\": 0, \"index\": 32, \"width\": 1654, \"height\": 450, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-033.webp\", \"caption\": \"\", \"page\": 0, \"index\": 33, \"width\": 1680, \"height\": 450, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-034.webp\", \"caption\": \"\", \"page\": 0, \"index\": 34, \"width\": 1652, \"height\": 452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-035.webp\", \"caption\": \"\", \"page\": 0, \"index\": 35, \"width\": 1647, \"height\": 452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-036.webp\", \"caption\": \"\", \"page\": 0, \"index\": 36, \"width\": 1649, \"height\": 454, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/fig-037.webp\", \"caption\": \"\", \"page\": 0, \"index\": 37, \"width\": 1653, \"height\": 456, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 888, \"height\": 586, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 894, \"height\": 370, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 778, \"height\": 329, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 857, \"height\": 232, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 684, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1557, \"height\": 261, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 893, \"height\": 299, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 819, \"height\": 196, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-009-44e9647bbf5b-navid-video-based-vlm-plans-the-next-step-for-vision-and-language-navigation/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 535, \"height\": 232, \"label\": \"Table\"}]"
motivation: 旨在解决视觉语言导航在跨分布场景和从仿真到真实环境迁移中的泛化困难。
method: 提出NaVid，利用单目RGB视频流输入，直接预测下一步动作，无需地图、里程计或深度信息。
result: 在多个仿真和真实环境导航任务中达到最优性能，跨数据集和Sim2Real迁移表现优于现有方法。
conclusion: 展示了视频基大语言模型在无地图简化导航设置中的可行性及其从仿真到真实世界的卓越迁移能力，为导航研究开辟新范式。
---

## 摘要
视觉语言导航（VLN）是具身AI的一个关键研究问题，旨在使智能体能够在遵循语言指令的情况下在未知环境中导航。在这一领域，泛化是一个长期挑战，无论是对于分布外场景还是从仿真到真实环境。本文提出了一种基于视频的大型视觉语言模型（VLM）NaVid，以缩小这种泛化差距。NaVid首次展示了VLM在无需地图、里程计或深度输入的情况下实现最先进导航水平的能力。遵循人类指令，NaVid仅需来自机器人搭载的单目RGB摄像头的实时视频流，即可输出下一步行动。我们的公式模拟了人类导航的方式，自然消除了里程计噪声以及地图或深度输入带来的Sim2Real差距。此外，我们的基于视频的方法能够有效编码机器人的历史观测结果，作为决策和指令遵循的时空上下文。我们使用从连续环境中收集的51万条导航样本（包括动作规划和指令推理样本）以及76.3万条大规模网络数据训练NaVid。大量实验表明，NaVid在仿真环境和现实世界中均达到了最先进的性能，展示了卓越的跨数据集和Sim2Real迁移能力。因此，我们相信所提出的VLM方法不仅为导航智能体，也为该研究领域规划了下一步行动。

## Abstract
Vision-and-language navigation (VLN) stands as a key research problem of Embodied AI, aiming at enabling agents to navigate in unseen environments following linguistic instructions. In this field, generalization is a long-standing challenge, either to out-of-distribution scenes or from Sim to Real. In this paper, we propose NaVid, a video-based large vision language model (VLM), to mitigate such a generalization gap. NaVid makes the first endeavor to showcase the capability of VLMs to achieve state-of-the-art level navigation performance without any maps, odometers, or depth inputs. Following human instruction, NaVid only requires an on-the-fly video stream from a monocular RGB camera equipped on the robot to output the next-step action. Our formulation mimics how humans navigate and naturally gets rid of the problems introduced by odometer noises, and the Sim2Real gaps from map or depth inputs. Moreover, our video-based approach can effectively encode the historical observations of robots as spatio-temporal contexts for decision making and instruction following. We train NaVid with 510k navigation samples collected from continuous environments, including action-planning and instruction-reasoning samples, along with 763k large-scale web data. Extensive experiments show that NaVid achieves state-of-the-art performance in simulation environments and the real world, demonstrating superior cross-dataset and Sim2Real transfer. We thus believe our proposed VLM approach plans the next step for not only the navigation agents but also this research field.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 视觉语言导航（VLN）要求智能体在从未见过的环境中根据自然语言指令导航，其长期面临两大泛化挑战：跨分布场景的泛化（cross‑dataset）和从仿真到真实环境的迁移（Sim‑to‑Real）。
- 现有方法大多依赖深度图、里程计或预构建地图，这些输入在真实世界中易受传感器噪声、领域差异影响，导致 Sim‑to‑Real 性能大幅下降。
- 本文首次探索利用视频基大型视觉语言模型（VLM）直接解决 VLN 的泛化问题，提出 NaVid——仅需单目 RGB 视频流即可预测下一步低层动作，无需额外传感器或地图，模仿人类导航的简约范式。
- 该工作旨在证明 VLM 的通用知识可以迁移至 VLN 任务，并显著缩小离散仿真与连续真实世界的差距，为无地图、纯视觉的导航系统开辟新范式。

## 二、论文提出的方法论
- **核心思想**：将 VLN 转化为基于视频的 Vision‑Language‑Action（VLA）问题，通过预训练的 VLM 直接输出可执行的行动（含动作类型和量化参数），无需中间表示（如地图或深度）。
- **架构**（基于 LLaMA‑VID 改进）：
  - 视觉编码器：EVA‑CLIP，将每帧 RGB 图像转换为 256 个 patch 特征。
  - 指令查询令牌（Instruction‑queried token）：通过 Q‑Former 在视觉特征与语言指令之间进行跨模态交互，生成 1 个与指令相关的令牌，聚焦任务相关区域。
  - 指令无关令牌（Instruction‑agnostic token）：对每帧特征图进行网格池化（grid pooling）并投影，保留细粒度几何信息。历史帧使用 4 个令牌，当前帧使用 64 个令牌，兼顾效率与信息量。
  - 大语言模型：Vicuna‑7B，接收拼接后的观察令牌、语言指令令牌及特殊分隔符（<HIS>, <OBS>, <NAV>），输出语言形式的下一步动作（如 “move forward 75 cm”）。
  - 动作解码：使用正则表达式解析输出，提取动作类型（FORWARD/TURN‑LEFT/TURN‑RIGHT/STOP）及对应的距离或角度参数。
- **训练策略**：
  - 混合数据：320k oracle 轨迹 + 180k 非 oracle 轨迹（通过 Dagger 算法收集）+ 10k 指令推理样本（反向生成轨迹描述）+ 763k 大规模网络视频‑文本数据（用于防止遗忘通用知识）。
  - 联合训练 VLN 动作预测与两个辅助任务：指令推理（根据轨迹生成指令）和视频问答（来自 LLaMA‑VID 数据）。
  - 所有预训练组件（EVA‑CLIP、Q‑Former、BERT、Vicuna‑7B）加载默认权重，仅优化 LLM 和文本编码器部分，训练 1 个 epoch。
- **核心创新**：视频式历史编码代替文本或地图描述，保留丰富的时空上下文；特殊令牌机制清晰区分历史/当前观测；RGB‑only 输入消除了里程计噪声和深度域差距。

## 三、实验设计
- **仿真环境**：
  - 数据集：VLN‑CE 的 R2R（10,819 训练，1,839 val‑unseen 测试）和 RxR（1,517 val‑unseen 用于跨数据集评估）。
  - 测度：成功路（SR）、或aclesuccess（OS）、SPL（成功率加权路径长度）、导航误差（NE）和轨迹长度（TL）。
  - 对比方法：Seq2Seq、CMA（RGB/Depth）、WS‑MGMap、LAW、CM2、GridMM、HAMT、ETPNav 等低层动作预测方法，以及 GPT‑4V、LLaVA、LLaMA‑VID 等基础模型改造版（LLaVA‑Nav、LLaMA‑VID‑Nav）。
- **真实世界**：
  - 平台：TurtleBot4 + Azure Kinect DK（仅用 RGB）+ RPLIDAR（仅用于基线里程计）。
  - 场景：四个不同的室内环境（Meeting Room、Office、Lab、Lounge），每场景 25 条简单指令 + 25 条复杂指令，共 200 条。
  - 对比基线：Seq2Seq、CMA、WS‑MGMap（这些方法需深度/里程计）。
- **消融实验**：
  - 训练策略：无 co‑training、无指令推理样本、无 dagger 样本。
  - 架构：移除特殊令牌、改用文本/地图历史表示、不同视觉令牌数量（1/4/16）、直接输出 waypoint 坐标。
  - 数据规模：逐步增加导航数据量时的性能变化。
  - 对比不同历史表示（文本、地图+文本、ego‑view+文本 vs 视频）。
  - 对比 LM‑Nav 及其变体（使用不同基础模型）。
  - 零样本目标导航（Object Goal）测试（HM3D 数据集）。

## 四、资源与算力
- 训练集群：24 块 NVIDIA A100 GPU，总训练时间约 28 小时（折合 672 GPU 小时）。
- 模型推理：在 A100 上每步动作约需 1.2–1.5 秒（未量化）；若使用量化和加速技术可降低延迟。

## 五、实验数量与充分性
- **实验数量**：论文包含 9 张表格（Table I–IX）和 8 张图（Fig 3–8），涵盖仿真 R2R 主实验、RxR 跨数据集实验、真实世界四大场景、大模型对比、历史表示对比、LM‑Nav 对比、消融（训练策略、架构、token 数、数据规模）以及附加的目标导航实验。
- **充分性**：
  - 主实验：在标准 benchmark（VLN‑CE R2R/RxR）上与其他方法进行了全面比较，覆盖多种输入模态（RGB‑only 与 RGB+Depth+Odo）的方法，确保公平。
  - 消融完整：针对训练数据（co‑turning、dagger）、网络结构（特殊token、token数量、输出方式）进行了逐一验证。
  - 真实世界：跨越 4 个场景、200 条指令，并提供了可视化轨迹，验证了 Sim‑to‑Real 迁移能力。
  - 额外实验：零样本 object navigation 与其他基线（ESC、GoW 等）对比，显示 RGB‑only 方法的竞争力。
- **客观性**：对比方法均来自公开文献，超参数及设定说明清晰；对于 GPT‑4V 等闭源模型，通过精心 prompt 使输出可执行；消融实验方案设计合理，能有效归因各组件贡献。

## 六、论文的主要结论与发现
- NaVid 在 VLN‑CE R2R val‑unseen 上以 RGB‑only 输入达到 SPL 35.9%，与需要深度/里程计的最优方法（WS‑MGMap，SPL 34.3%）相当甚至更优，远超 RGB‑only 基线（SPL <5%）。
- 跨数据集（R2R→RxR）零样本测试中，NaVid 的 SR 和 SPL 分别达到 23.8% 和 21.2%，大幅领先所有基线（包括零样本的 A2Nav：SR 16.8%、SPL 6.3%）。
- 真实世界 200 条指令中，NaVid 在简单任务上平均成功率达 85%，复杂任务达 47%，而 WS‑MGMap 仅 52%/24%，证明了 Sim‑to‑Real 显著优势。
- 视频式历史编码优于文本或地图式表示（SPL 从 35.9% 降至 20.8%/8.97%），说明保持时空连续性对于 VLN 至关重要。
- 视觉令牌数量在 4 时达到效率与性能的最佳平衡（SR 37.4%，推理 1.22s）；更多令牌（16）性能提升有限（SR 38.0%）但推理时间翻倍。
- 大型基础模型（GPT‑4V、LLaVA 等）未经导航数据微调时，无法稳定输出有效动作（SR ≤5%），说明任务特定数据的重要性。

## 七、优点
- **输入极简**：仅需单目 RGB 视频，无需任何额外传感器（深度、里程计、地图），大幅降低部署门槛，规避了传感器校准和 Sim‑to‑Real 域差。
- **视频建模创新**：利用指令查询令牌与指令无关令牌组合，兼顾任务关注与全局信息保留；对历史帧和当前帧采用不同粒度令牌，在上下文长度与信息密度间取得平衡。
- **泛化能力卓越**：跨数据集（R2R→RxR）和 Sim‑to‑Real 迁移性能显著优于现有方法，证明了大模型导航的潜力。
- **数据高效策略**：通过 Dagger 收集非 oracle 轨迹、加入指令推理辅助任务，有效利用有限仿真数据，提升模型鲁棒性。
- **实验设计全面**：覆盖仿真标准 benchmark、真实世界多场景、消融、大模型对比、历史表示对比等，验证充分，结论可信。

## 八、不足与局限
- **计算延迟**：每步推理需 1.2–1.5 秒（A100），对于实时导航（尤其是复杂环境）仍显缓慢，论文虽提到量化加速，但未给出实际改进效果。
- **长指令与长上下文**：在超过 90 步的长轨迹上，性能有下降（虽然文中图表显示稳定，但平均 SR 仍随步数增加而波动），且训练数据中长轨迹比例低；缺乏高质量长视频标注数据。
- **实验场景局限性**：真实世界仅测试了 4 个室内场景（会议室、办公室、实验室、休息室），且指令由人工设计（非自然采集），场景多样性和指令难度可能不足以代表全部真实挑战。
- **对比公平性潜在偏差**：部分基线（如 WS‑MGMap）在真实世界测试中可能未针对机器人平台进行最优调参；此外，NaVid 的输入仅 RGB，而基线使用 RGB+Depth+Odo，方法本身不对等，但“公平”体现在任务条件相同（导航成功率）而非输入条件相同。
- **可解释性不足**：VLMs 输出的动作依据无法直观追溯，当决策错误时难以分析原因（例如是否因视觉歧义或语言理解错误）。
- **依赖预训练模型**：模型性能很大程度上受限于 EVA‑CLIP 和 Vicuna 的预训练知识，对于极端分布外环境（如工厂、户外）可能泛化不足。

（完）
