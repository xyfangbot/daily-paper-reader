---
title: "StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling"
title_zh: StreamVLN：通过慢快上下文建模的流式视觉与语言导航
authors: "Meng Wei, Chenyang Wan, Xiqian Yu, Tai Wang, Yuqiang Yang, Xiaohan Mao, Chenming Zhu, Wenzhe Cai, Hanqing Wang, Yilun Chen, Xihui Liu, Jiangmiao Pang"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2507.05240v1"
arxiv_id: 2507.05240v1
arxiv_url: "https://arxiv.org/abs/2507.05240v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/002-2025_wei_streamvln-69d7f63e-0c409e36467d.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2507.05240v1", "query:Visual-and-Language Navigation", "query:Visual-Language-Action Model", "query:Streaming", "query:SlowFast Context Modeling", "query:Video-LLM"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 在现实视觉语言导航任务中，智能体需处理连续视频流并基于语言指令低延迟生成动作。StreamVLN提出快慢双通道上下文建模：快速通道通过滑动窗口实时维护对话历史，支持快速响应；慢速通道利用3D感知token剪枝压缩长期视觉记忆，降低存储与计算开销。通过高效KV缓存复用，模型支持长视频流且上下文大小有界。在VLN-CE基准上，StreamVLN取得最先进性能，并保持稳定低延迟，兼顾鲁棒性与实际部署效率。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1306, \"height\": 856, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 508, \"height\": 522, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1432, \"height\": 482, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1423, \"height\": 941, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 580, \"height\": 439, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1241, \"height\": 2315, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1425, \"height\": 1859, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1355, \"height\": 320, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1349, \"height\": 385, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1355, \"height\": 399, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1346, \"height\": 365, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1347, \"height\": 318, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1345, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1345, \"height\": 318, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1350, \"height\": 467, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1440, \"height\": 1030, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1139, \"height\": 568, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1328, \"height\": 406, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1299, \"height\": 237, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 804, \"height\": 413, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1407, \"height\": 242, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-002-0c409e36467d-streamvln-streaming-vision-and-language-navigation-via-slowfast-context-modeling/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1461, \"height\": 207, \"label\": \"Table\"}]"
motivation: 现实VLN面临连续视觉流理解、长期上下文建模与低延迟推理的冲突，现有方法难以兼顾。
method: 提出快慢双通道机制：快速通道滑动窗口维护对话历史；慢速通道3D感知token剪枝压缩长期视觉记忆。
result: 在VLN-CE基准上达到SOTA性能，并保持稳定低延迟，推理高效，鲁棒性强。
conclusion: StreamVLN通过快慢上下文建模有效平衡了长期记忆与实时响应，为实际部署提供了高效鲁棒方案。
---

## 摘要
真实环境中的视觉与语言导航（VLN）要求智能体处理连续的视觉流，并基于语言指令以低延迟生成动作。尽管基于视频的大语言模型（Video-LLM）推动了近期进展，但当前基于Video-LLM的VLN方法往往在细粒度视觉理解、长期上下文建模和计算效率之间面临权衡。我们提出了StreamVLN，一种流式VLN框架，采用混合慢快上下文建模策略，支持对交错视觉、语言和动作输入的多模态推理。快速流式对话上下文通过活跃对话的滑动窗口促进响应动作生成，而慢速更新记忆上下文则利用3D感知令牌剪枝策略压缩历史视觉状态。通过这种慢快设计，StreamVLN通过高效的KV缓存复用实现连贯的多轮对话，支持具有有限上下文大小和推理成本的长视频流。在VLN-CE基准上的实验展示了具有稳定低延迟的最先进性能，确保了实际部署中的鲁棒性和效率。项目页面：https://streamvln.github.io/。

## Abstract
Vision-and-Language Navigation (VLN) in real-world settings requires agents to process continuous visual streams and generate actions with low latency grounded in language instructions. While Video-based Large Language Models (Video-LLMs) have driven recent progress, current VLN methods based on Video-LLM often face trade-offs among fine-grained visual understanding, long-term context modeling and computational efficiency. We introduce StreamVLN, a streaming VLN framework that employs a hybrid slow-fast context modeling strategy to support multi-modal reasoning over interleaved vision, language and action inputs. The fast-streaming dialogue context facilitates responsive action generation through a sliding-window of active dialogues, while the slow-updating memory context compresses historical visual states using a 3D-aware token pruning strategy. With this slow-fast design, StreamVLN achieves coherent multi-turn dialogue through efficient KV cache reuse, supporting long video streams with bounded context size and inference cost. Experiments on VLN-CE benchmarks demonstrate state-of-the-art performance with stable low latency, ensuring robustness and efficiency in real-world deployment. The project page is: https://streamvln.github.io/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 真实环境中的视觉与语言导航（VLN）要求智能体处理连续视频流，并基于语言指令低延迟地生成动作。
- 现有基于Video-LLM的VLN方法难以同时兼顾三点：细粒度视觉理解、长期上下文建模、计算效率。
- 当前方法要么通过固定帧采样牺牲时间分辨率，要么通过池化/令牌合并压缩视觉信息导致细节丢失，且普遍需要在每个动作步骤刷新LLM对话上下文，造成大量冗余计算。
- 因此，迫切需要一种能支持连续交互、低延迟、有界上下文的流式导航框架。

## 二、论文提出的方法论
- **核心思想**：提出快慢双通道上下文建模（SlowFast Context Modeling）的流式VLN框架StreamVLN。
  - **快速流式对话上下文（Fast-Streaming）**：通过固定大小的滑动窗口缓存最近N轮对话的KV状态，实现高响应性的动作解码。
  - **慢速更新记忆上下文（Slow-Updating Memory）**：对历史窗口的视觉令牌进行3D感知剪枝，压缩为紧凑的记忆令牌，用于长期时序推理，同时支持KV缓存高效复用。
- **关键技术细节**：
  - 基于LLaVA-Video 7B（Qwen2-7B）扩展为交错视觉-语言-动作模型。
  - 滑动窗口机制：保留固定数量（如8轮）的最近对话，超出后卸载旧窗口KV，丢弃非观察令牌（如提示词、动作），只保留经剪枝的记忆令牌。
  - 基于体素的空间剪枝算法（Algorithm 1）：利用深度信息将2D图像块反投影到共享3D空间，离散化为统一体素；同一体素内只保留最近观察的令牌，生成剪枝掩码M，平均减少约20%输入令牌。
  - 多源数据联合训练：包括导航专用数据（MP3D、HM3D场景的模仿学习采样+DAgger纠正演示）和通用多模态数据（VideoQA、MMC4交错图文），保留预训练模型推理能力。
  - 动作表示使用稀有符号（↑←→ STOP）以减少过拟合，每动作仅1个令牌，兼顾表达与效率。

## 三、实验设计
- **主要基准**：
  - VLN-CE：R2R-CE（5.6K英文轨迹）和RxR-CE（126K多语言指令，路径更长更多样），在Habitat模拟器上评估，关注验证未知拆分。
  - 额外基准：ScanQA（3D问答，评估空间场景理解）、HM3D-ObjectNav（零样本目标导航）。
  - 真实世界实验：基于Unitree Go2机器人+Intel RealSense D455，远程RTX 4090推理。
- **对比方法**：
  - 传统方法：HPN+DN、CMA、VLNBERT、Sim2Sim、GridMM、ETPNav、ScaleVLN等（常依赖全景或航点先验）。
  - 基于Video-LLM的RGB-only方法：NaVid、MapNav、NaVILA、UniNaVid。
  - 在VLN-CE上覆盖了20+种方法；在ScanQA上对比了ScanRefer、3D-LLM、LEO、ChatScene等；在ObjectNav上对比了GoW、ESC、PixelNav、VoroNav等。
- **消融实验**：
  - 数据成分消融（有无DAgger、是否加入VideoQA/MMC4/ScaleVLN数据）。
  - 记忆上下文大小（2×196、4×196、8×196、全部）与滑动窗口大小（8、4、2）。
  - KV缓存复用策略对延迟的影响（全轮复用、滑动窗口、单轮）。
  - 体素剪枝有无的对比。
  - 动作类型设计（4令牌符号 vs 4令牌文本 vs 23令牌自然语言）。

## 四、资源与算力
- 模型基于LLaVA-Video 7B（Qwen2-7B为语言模型）。
- 训练分两阶段，每阶段一个epoch：第一阶段使用450K oracle轨迹，第二阶段使用DAgger数据与多模态数据混合。
- 每步处理128个视频片段，峰值学习率2e-5（语言模型）、5e-6（视觉编码器）。
- **总训练算力**：约**1500 A100 GPU小时**（文中明确提及）。

## 五、实验数量与充分性
- **实验数量充足**：在2个主要VLN-CE基准（R2R、RxR）的Val-Unseen上报告了10+指标（NE、OS、SR、SPL、nDTW），对比了20+方法；额外在ScanQA、HM3D-ObjectNav上进行验证；并呈现真实世界定性结果。
- **消融实验覆盖全面**：数据成分（6种组合）、内存窗口大小（4种）、滑动窗口大小（3种）、KV缓存策略（3种）、体素剪枝（有无）、动作类型（3种）等，共约6组以上消融。
- **充分性与公平性**：
  - 对比方法包括有无额外训练数据的设置，StreamVLN在两个设置下均报告结果（“†”表示使用额外数据）。
  - 与NaVILA、UniNaVid等直接可比（均为RGB-only end-to-end Video-LLM方法）。
  - 在ScanQA上使用相同帧数（16帧）对比，公平。
  - 消融实验控制变量（总VL数据量相同），结论稳健。
- **局限性**：未在离散设置（如R2R离散版）上验证，且真实世界实验仅为定性，缺乏定量成功率统计。

## 六、论文的主要结论与发现
- StreamVLN在VLN-CE R2R Val-Unseen上达到**56.9% SR / 51.9% SPL**（RGB-only），在RxR上达到**52.9% SR / 46.0% SPL**，均达到SOTA。
- 慢快混合设计使得KV缓存高效复用：滑动窗口机制在保持低延迟的同时避免上下文无限增长；体素剪枝在不牺牲甚至提升性能（+1~1.2% SR）的前提下压缩约20%令牌。
- 多源数据联合训练提升显著：DAgger数据带来+5.5 SR，MMC4交错图文进一步+2.0 SR，ScaleVLN/RxR数据也有效。
- 记忆上下文大小存在最优值（8×196），过大或过长反而不佳；滑动窗口尺寸8平衡性能与训练效率。
- 模型在ScanQA上超越NaviLLM、NaVILA等，展示强空间推理能力；零样本ObjectNav表现接近专家方法，体现跨任务泛化能力。

## 七、优点
1. **方法创新性强**：提出“慢快双通道”上下文建模，兼顾实时响应与长期记忆，形式简洁有效。
2. **工程实用性好**：通过KV缓存复用和体素剪枝实现低延迟（0.27s/4动作）和有界内存，适合实际机器人部署。
3. **实验充分且公平**：在多个基准、多种对比、多类消融上验证，对公平性有明确处理（如区分有无额外数据）。
4. **数据效率高**：仅使用ScaleVLN子集（150K轨迹）即超越使用3M轨迹的HMAT，展示更强泛化能力。
5. **通用性强**：在VQA、ObjectNav等任务上表现良好，说明方法不依赖导航特定设计。

## 八、不足与局限
1. **低层动作稳健性不足**：直接生成原始动作对视角变化和遮挡不够鲁棒，真实环境控制可能不优。
2. **长时导航局限**：当前慢快设计对超长导航（如>100步）仍面临推理一致性挑战，记忆压缩可能丢失关键细节。
3. **异步部署复杂性**：动作历史作为对话上下文的一部分，在异步推理时需要同步，增加了系统复杂度。
4. **真实实验为定性**：仅展示了几个场景的定性成功案例，缺乏在真实环境下的定量成功率、失败分析；环境多样性有限（仅4个场景）。
5. **未报告离散VLN结果**：实验局限于连续环境，缺乏与离散设置方法的直接比较。
6. **仅对比RGB-only方法**：未与使用深度/全景/航点预测的强方法（如ETPNav）进行公平对比（虽在部分指标上接近或超越，但输入模态不同，需谨慎解读）。

（完）
