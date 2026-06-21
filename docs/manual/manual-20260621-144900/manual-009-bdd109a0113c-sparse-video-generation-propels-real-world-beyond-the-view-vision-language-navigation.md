---
title: Sparse Video Generation Propels Real-World Beyond-the-View Vision-Language Navigation
title_zh: 稀疏视频生成推动真实世界超视域视觉语言导航
authors: Beyond-the-View Vision-Language Navigation
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2602.05827v1"
arxiv_id: 2602.05827v1
arxiv_url: "https://arxiv.org/abs/2602.05827v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/009-2026_zhang_sparsevideonav-2b565e3d-bdd109a0113c.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2602.05827v1", "query:Sparse Video Generation", "query:Beyond-the-View Navigation", "query:Vision-Language Navigation", "query:Video Generation Models", "query:Real-World Navigation"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航通常需要详细指令，但现实世界应支持简单高层意图的自主导航，即Beyond-the-View Navigation (BVN)任务。本文首次引入视频生成模型，利用其长程监督优势提出SparseVideoNav，通过生成稀疏未来帧实现20秒视野的亚秒级轨迹推理。真实零样本实验中，SparseVideoNav在BVN任务上成功率比SOTA LLM基线提升2.5倍，速度提升27倍，并首次在夜间场景实现导航。该工作为现实世界高层意图导航提供了高效可行的方案。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1774, \"height\": 933, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1660, \"height\": 945, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 858, \"height\": 1002, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1671, \"height\": 1016, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 893, \"height\": 682, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1469, \"height\": 914, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 862, \"height\": 880, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 877, \"height\": 321, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 876, \"height\": 395, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1302, \"height\": 348, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1868, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1864, \"height\": 1232, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1848, \"height\": 1395, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1756, \"height\": 576, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 940, \"height\": 278, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 799, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-009-bdd109a0113c-sparse-video-generation-propels-real-world-beyond-the-view-vision-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1305, \"height\": 324, \"label\": \"Table\"}]"
motivation: 现有LLM导航方法依赖短视监督，延长视野会训练不稳定，而视频生成模型天然适合长程对齐。
method: 提出SparseVideoNav，首次引入视频生成模型，通过生成稀疏未来帧实现20秒视野的亚秒级轨迹推理。
result: 真实零样本BVN任务中成功率比SOTA LLM基线高2.5倍，速度提升27倍，并首次实现夜间导航。
conclusion: 视频生成模型的长程监督特性可有效解决Beyond-the-View导航挑战，为现实世界自主导航开辟新途径。
---

## 摘要
为什么视觉语言导航必须绑定详细而冗长的语言指令？虽然这些细节便于决策，但它们在根本上与真实世界导航的目标相矛盾。理想情况下，智能体应具备自主导航能力，仅由简单的高级意图指导，在未知环境中探索。实现这一愿景带来了一个艰巨的挑战：超视域导航（BVN），即智能体必须在没有密集、逐步指导的情况下定位远处的不可见目标。现有的基于大语言模型（LLM）的方法虽然擅长遵循密集指令，但由于依赖于短视监督，往往表现出短视行为。然而，简单地扩展监督视野会破坏LLM训练的稳定性。在这项工作中，我们识别出视频生成模型天然受益于长视野监督以对齐语言指令，使其特别适用于BVN任务。基于这一洞察，我们首次提出将视频生成模型引入该领域。然而，生成跨越数十秒的视频所带来的高延迟使得现实部署不切实际。为弥补这一差距，我们提出了SparseVideoNav，通过在生成稀疏的未来轨迹（覆盖20秒视野）指导下实现亚秒级轨迹推理。与未经优化的版本相比，这实现了27倍的速度提升。广泛的实际零样本实验表明，在BVN任务上，SparseVideoNav的成功率是现有最先进LLM基线的2.5倍，并且标志着在具有挑战性的夜间场景中首次实现了这种能力。

## Abstract
Why must vision-language navigation be bound to detailed and verbose language instructions? While such details ease decision-making, they fundamentally contradict the goal for navigation in the real-world. Ideally, agents should possess the autonomy to navigate in unknown environments guided solely by simple and high-level intents. Realizing this ambition introduces a formidable challenge: Beyond-the-View Navigation (BVN), where agents must locate distant, unseen targets without dense and step-by-step guidance. Existing large language model (LLM)-based methods, though adept at following dense instructions, often suffer from short-sighted behaviors due to their reliance on short-horizon supervision. Simply extending the supervision horizon, however, destabilizes LLM training. In this work, we identify that video generation models inherently benefit from long-horizon supervision to align with language instructions, rendering them uniquely suitable for BVN tasks. Capitalizing on this insight, we propose introducing the video generation model into this field for the first time. Yet, the prohibitive latency for generating videos spanning tens of seconds makes real-world deployment impractical. To bridge this gap, we propose SparseVideoNav, achieving sub-second trajectory inference guided by a generated sparse future spanning a 20-second horizon. This yields a remarkable 27× speed-up compared to the unoptimized counterpart. Extensive real-world zero-shot experiments demonstrate that SparseVideoNav achieves 2.5× the success rate of state-of-the-art LLM baselines on BVN tasks and marks the first realization of such capability in challenging night scenes.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有视觉语言导航（VLN）依赖密集、逐步的语言指令，与真实世界中智能体需要基于简单高层意图自主导航的需求相矛盾。
- 本文聚焦于 **Beyond-the-View Navigation (BVN)** 任务：智能体必须在没有详细中间指导的情况下，自主定位远处不可见的目标。
- 基于大语言模型（LLM）的现有方法因使用短视监督（通常 4-8 步）而表现出短视行为，如意外转向、在死胡同中停滞等。简单延长监督视野会破坏 LLM 训练稳定性。
- 作者识别出视频生成模型（VGM）天然具备与语言指令对齐的长视野监督能力，因此首次将 VGM 引入导航领域，以解决 BVN 挑战。

## 二、论文提出的方法论
- **核心思想**：利用视频生成模型的长视野生成能力为导航提供未来规划，并通过 **稀疏视频生成** 降低计算开销，实现兼顾预测视野与实时性的实用系统。
- **关键技术**：
  - **稀疏化策略**：放弃连续帧预测，改为固定间隔（间隔=3）生成稀疏未来帧，覆盖 \( T+1 \) 到 \( T+20 \) 共 20 秒视野（4 FPS），同时首两个 chunk 保持连续以保证动作精度。
  - **四阶段训练管道**：
    1. **T2V → I2V 适配**：将文本-视频模型 Wan2.1-1.3B 微调为图像-视频模型，使用 flow matching 损失 \( \mathcal{L} = \mathbb{E}||u(x_t, l, c_T, t;\theta) - v_t||^2 \)。
    2. **历史注入**：通过 Q-Former 和 Video-Former 压缩历史观测，在 Wan 的 transformer 块中添加交叉注意力层注入历史信息，损失函数增加条件 \( h_T \)。
    3. **扩散蒸馏**：采用 PCM 方法将蒸馏步骤从 50 步减少到 4 步，加速约 10 倍。
    4. **动作学习**：冻结蒸馏后的 I2V 模型，使用条件 DiT 生成 8 步连续动作，损失函数为 DDIM 去噪重建误差，并用 Depth Anything 3 对生成帧重新标注动作标签以消除不一致。
- **网络架构**：基于 Wan2.1 T2V-1.3B 主干，历史压缩模块含 Q-Former（4层、512维）和 Video-Former（6层、512维），动作头包含 8 层 Video-Former 和 12 层 Diffusion Transformer。

## 三、实验设计
- **数据集**：自建 **140 小时真实世界导航数据集**，包含约 13,000 条轨迹（平均 140 帧，4 FPS），覆盖室内（Room、Lab Building）、室外（Yard、Park）和夜间（Square、Mountain）共 6 个场景。使用 DA3 估计相机姿态提取连续动作标签，人工标注语言指令。
- **基准方法**：对比三个 SOTA LLM 基线——Uni-NaVid、StreamVLN、InternVLA-N1。
- **评估协议**：每个场景设计 4 个任务（2 个指令跟随导航 IFN + 2 个超视域导航 BVN），每个模型每任务测试 10 次，共计 240 次试验。成功判定标准：智能体在目标 1.5 米内停止。所有实验在相同时间窗口内进行以控制环境变量。
- **硬件平台**：Unitree Go2 机器人狗，顶部安装 DJI Osmo Action 4 摄像头（高度约 1m），远程工作站配备 RTX 4090 GPU。

## 四、资源与算力
- **训练算力**：使用 **32 块 NVIDIA H200 GPU**，完整四阶段训练共约 **64 小时**。Stage 1 和 Stage 2 各需约 32 小时（从 T2V 逐步适配 vs 直接训练节省 2× 时间）。
- **推理延迟**：SparseVideoNav 实现 **亚秒级轨迹推理**（约 0.79 秒），比未优化 50 步版本快 10 倍，比连续生成版本快 1.7 倍，比原始未蒸馏版本快 27 倍。

## 五、实验数量与充分性
- **实验数量**：主实验共 240 次试验（4 方法 × 6 场景 × 4 任务 × 10 次）。消融实验包括：数据规模（8h/50h/140h）、稀疏间隔（连续 2/连续 10/稀疏）、蒸馏（4 步 vs 50 步 vs 无蒸馏）、历史压缩方式（有/无 Q-Former & Video-Former）、Stage 1 预训练有效性。另外讨论了动态行人避障和相机高度敏感性。
- **充分性与客观性**：实验设计较为充分，覆盖多种场景和任务类型，采用统一的成功判定标准（距离 ≤1.5m），并在相同环境条件下比较。零样本评估避免了过拟合，但场景数量仅 6 个，对极端环境的泛化性验证有限。消融实验对比关键组件，论证了稀疏设计的优越性。不过，夜间场景仅 2 个，样本量较小。

## 六、论文的主要结论与发现
- SparseVideoNav **在 BVN 任务上成功率比 SOTA LLM 基线高 2.5 倍**（25% vs 10%），在 IFN 任务上也显著领先（50% vs 35%）。
- 首次在 **夜间场景** 实现 BVN 导航（成功率 17.5%），而所有 LLM 基线完全失败。
- 稀疏生成设计带来 **1.7 倍推理加速** 和 **1.4 倍训练加速**，同时性能仅轻微下降（相对于 50 步连续版本）。
- 扩散蒸馏将推理步骤从 50 减至 4，加速约 **10 倍**，且视觉保真度相近。
- 模型展现出 **动态避障** 和 **相机高度鲁棒性**（从 1m 到 50cm 仍有效）的涌现能力。
- 数据规模从 8h 扩大到 140h 时 FVD 持续降低，表明良好的可扩展性。

## 七、优点
- **方法创新**：首次将视频生成模型引入视觉语言导航领域，并开创性地提出 **稀疏视频生成** 范式，突破传统连续生成的限制。
- **系统设计**：四阶段训练管道逐步适配，兼顾了生成质量、长视野推理和实时性；蒸馏与稀疏化共同实现实际部署可行的推理速度。
- **数据贡献**：构建了目前最大的真实世界 VLN 数据集（140 小时），并计划开源。
- **实验验证**：在真实机器人上进行了广泛的零样本评估，覆盖白天、夜间、室内外多种复杂地形，结果可靠且具有说服力。
- **涌现能力**：模型在未显式训练的情况下显示出动态避障、高度鲁棒性等，表明 VGM 底层的强泛化能力。

## 八、不足与局限
- **数据规模不足**：140 小时数据集相比网络规模（如 YouTube 视频、仿真数据）仍较小，限制了进一步性能提升；高度挑战场景下可能出现模式崩溃。
- **推理延迟**：虽经大幅优化，但 0.79 秒仍慢于 LLM 方法（如 StreamVLN 可能更快），需探索更高效的蒸馏或量化技术。
- **动作标注依赖**：使用 Depth Anything 3 估计动作，在动态行人前被过滤掉，导致未直接训练避障能力；虽然模型涌现了避障行为，但可靠性未充分验证。
- **评估场景有限**：仅在 6 个场景进行零样本测试，多样化程度不够（如未包含雨雪、强光照等极端条件）。夜间场景仅 2 个，样本量较小。
- **对比基线选择**：对比的 LLM 基线均为 2025-2026 年方法，但未与某些端到端强化学习方法或基于地图的方法比较，可能有遗漏。
- **可重复性**：模型依赖 Wan2.1 预训练权重和自定义数据集，未提及是否提供完整训练代码与数据，可能影响复现。

（完）
