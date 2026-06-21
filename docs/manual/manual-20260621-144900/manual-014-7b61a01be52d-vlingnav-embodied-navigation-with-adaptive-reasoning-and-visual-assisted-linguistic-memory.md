---
title: "VLingNav: Embodied Navigation with Adaptive Reasoning and Visual-Assisted Linguistic Memory"
title_zh: VLingNav：具有自适应推理和视觉辅助语言记忆的具身导航
authors: "Shaoan Wang, Yuanfei Luo, Xingyu Chen, Aocheng Luo, Dongyue Li, Chang Liu, Sheng Chen, Yangang Zhang, Junzhi Yu"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2601.08665v1"
arxiv_id: 2601.08665v1
arxiv_url: "https://arxiv.org/abs/2601.08665v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/014-2026_wang_vlingnav-44ae9540-7b61a01be52d.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2601.08665v1", "query:Embodied Navigation", "query:Vision-Language-Action Models", "query:Adaptive Chain-of-Thought", "query:Visual-Assisted Linguistic Memory", "query:Reinforcement Learning"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有VLA模型在具身导航中依赖被动映射，缺乏显式推理和持久记忆，难以处理复杂长程任务。VLingNav提出自适应思维链(AdaCoT)动态触发推理，并构建视觉辅助语言记忆模块(VLingMem)实现跨模态语义记忆。在Nav-AdaCoT-2.9M数据集训练并结合在线专家引导强化学习，在多个导航基准上达到SOTA，零样本迁移至真实机器人，展现强跨域和跨任务泛化能力。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1706, \"height\": 817, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1666, \"height\": 706, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1197, \"height\": 605, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1706, \"height\": 807, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1198, \"height\": 666, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1696, \"height\": 1095, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 677, \"height\": 791, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 702, \"height\": 803, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1617, \"height\": 1428, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 630, \"height\": 449, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1042, \"height\": 455, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1028, \"height\": 717, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1675, \"height\": 516, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1719, \"height\": 1081, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 999, \"height\": 812, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1003, \"height\": 807, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1097, \"height\": 614, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 782, \"height\": 496, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1504, \"height\": 376, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1346, \"height\": 338, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-014-7b61a01be52d-vlingnav-embodied-navigation-with-adaptive-reasoning-and-visual-assisted-linguistic-memory/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1314, \"height\": 240, \"label\": \"Table\"}]"
motivation: 现有VLA模型在复杂长程导航任务中缺乏显式推理能力和持久记忆，难以处理空间依赖和动态环境。
method: 提出VLingNav模型，包含自适应思维链(AdaCoT)和视觉辅助语言记忆(VLingMem)模块，并构建Nav-AdaCoT-2.9M数据集，结合在线专家引导强化学习训练。
result: 在多个具身导航基准上取得SOTA结果，零样本迁移至真实机器人，完成未见任务。
conclusion: 提出具身导航VLA模型，通过自适应推理和跨模态记忆实现强泛化能力，有效解决了长程导航中的推理和记忆问题。
---

## 摘要
视觉-语言-动作（VLA）模型通过统一感知与规划，同时继承大型视觉-语言模型（VLM）的强大泛化能力，在具身导航中展现出巨大潜力。然而，现有大多数VLA模型依赖于从观察到动作的反应式映射，缺乏复杂长程导航任务所需的显式推理能力和持久记忆。为解决这些问题，我们提出VLingNav——一种基于语言驱动认知的具身导航VLA模型。首先，受人类认知双过程理论启发，我们引入自适应思维链（AdaCoT）机制，仅在必要时动态触发显式推理，使智能体能够在快速直觉执行与缓慢深思熟虑规划之间流畅切换。其次，为处理长程空间依赖关系，我们开发了视觉辅助语言记忆模块（VLingMem），构建持久跨模态语义记忆，使智能体能回忆过往观察以避免重复探索，并推断动态环境中的运动趋势。训练方面，我们构建了Nav-AdaCoT-2.9M——迄今为止最大的带推理标注的具身导航数据集，其中包含自适应CoT标注，诱导出能调整思考时机与内容的推理范式。此外，我们融入在线专家引导的强化学习阶段，使模型超越纯模仿学习，获得更鲁棒的自我探索导航行为。大量实验表明，VLingNav在广泛的具身导航基准测试中达到最先进性能。值得注意的是，VLingNav以零样本方式迁移到真实机器人平台，成功执行实际导航任务（包括先前未见且未经训练的任务），展现出强大的跨领域与跨任务泛化能力。

## Abstract
Vision-Language-Action (VLA) models have shown promising potential in embodied navigation by unifying perception and planning while inheriting the strong generalization abilities of large Vision-Language Models (VLMs). However, most existing VLA models rely on reactive mappings directly from observations to actions, lacking the explicit reasoning capabilities and persistent memory required for complex, long-horizon navigation tasks. To address these challenges, we propose VLingNav, a VLA model for embodied navigation grounded in linguistic-driven cognition. First, inspired by the dual-process theory of human cognition, we introduce an adaptive chain-of-thought (AdaCoT) mechanism, which dynamically triggers explicit reasoning only when necessary, enabling the agent to fluidly switch between fast, intuitive execution and slow, deliberate planning. Second, to handle long-horizon spatial dependencies, we develop a visual-assisted linguistic memory module (VLingMem) that constructs a persistent, cross-modal semantic memory, enabling the agent to recall past observations to prevent repetitive exploration and infer movement trends for dynamic environments. For training, we construct Nav-AdaCoT-2.9M, the largest embodied navigation dataset with reasoning annotations to date, enriched with adaptive CoT annotations that induce a reasoning paradigm capable of adjusting both when to think and what to think about. Moreover, we incorporate an online expert-guided reinforcement learning stage, enabling the model to surpass pure imitation learning and to acquire more robust, self-explored navigation behaviors. Extensive experiments demonstrate that VLingNav achieves state-of-the-art performance across a wide range of embodied navigation benchmarks. Notably, VLingNav transfers to real-world robotic platforms in a zero-shot manner, successfully executing practical navigation tasks, including previously unseen and untrained tasks, and demonstrating strong cross-domain and cross-task generalization.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有VLA（视觉-语言-动作）模型在复杂、长程导航任务中严重依赖从观看到动作的被动反应式映射，缺乏显式推理能力和持久记忆，难以处理空间依赖和动态环境变化。
- 大多数模型在固定推理预算下运行，无法根据任务复杂度灵活调整计算量；同时缺乏语义记忆，导致重复探索、循环行为等问题。
- 受人类认知双过程理论（快思考与慢思考）启发，论文旨在构建一种具备自适应推理和跨模态持久记忆的语言驱动VLA模型，提升导航系统的鲁棒性、可解释性与泛化能力。
- 核心挑战：如何使智能体能够“何时该思考”、“思考什么”，以及如何构建长期一致的语义记忆以支撑长程决策。

## 二、论文提出的方法论
- **整体框架**：VLingNav基于LLaVA-Video-7B视觉语言模型，集成MLP-based动作模型，输入为多模态指令与视频流，输出为连续轨迹（包含位置与方向）。
- **观察编码**：
  - 采用动态FPS采样策略，根据时间间隔对历史帧进行差异化采样（近期高帧率，远期低帧率），并配以网格池化降采样，控制计算成本。
  - 引入时间感知指示器（RoPE编码），使模型感知帧间时间间隔。
- **自适应CoT（AdaCoT）**：
  - 模型首先生成一个CoT指示器令牌（`<think_on>`或`<think_off>`），决定是否需要进行显式推理。
  - 当输出`<think_on>`时，生成两部分内容：1）推理内容（`<think>…</think>`），包含空间感知、任务分解、历史访问判断等；2）环境摘要（`<summary>…</summary>`），作为后续输入的语义记忆。
- **视觉辅助语言记忆（VLingMem）**：
  - 将历史CoT摘要与关键视觉特征以语言形式存储，构建持久跨模态记忆。在每次输入时，该记忆作为额外令牌注入模型上下文，帮助避免重复探索并推断运动趋势。
- **动作模型**：基于VLM最后令牌隐藏状态，通过MLP头预测连续轨迹（多元高斯分布，支持概率采样用于探索）。
- **训练流程**：
  1. **预训练（Stage 1）**：在大规模开放世界自适应CoT视频数据上单轮训练，赋予模型基础自适应视觉推理能力。
  2. **监督微调（SFT，Stage 2）**：在Nav-AdaCoT-2.9M数据集（含2.9M导航步骤、472K CoT标注）与开放世界视频数据（1.6M样本）上联合训练，损失包括轨迹MSE损失和文本交叉熵损失。
  3. **在线专家引导强化学习（Stage 3）**：使用PPO-style目标函数，结合**混合数据收集策略**（自身策略采样+专家纠偏轨迹），通过REINFORCE++计算优势，提升策略鲁棒性并超越模仿学习。
- **数据集构建**：Nav-AdaCoT-2.9M是目前最大带推理标注的导航数据集，整合ObjNav、EVT、ImageNav三大任务，并通过Qwen2.5-VL-72B自动化标注CoT，经两阶段筛选（规则检查+质量验证）确保质量。

## 三、实验设计
- **模拟基准**：
  - **Object Goal Navigation**：HM3Dv1 ObjNav、HM3Dv2 ObjNav、MP3D ObjNav、HM3D-OVON（开放词汇）
  - **Embodied Visual Tracking**：EVT-Bench（单目标跟踪、干扰跟踪）
  - **Image Goal Navigation**：HM3D Instance ImageNav
- **对比方法**：包括模块化方法（VLFM、SG-Nav、GOAT等）、端到端小模型（OVRL、PirlNav、FiLM-Nav等）、VLA模型（Uni-NaVid、NavFoM、TrackVLA、Nav-R1等），共三大类十余种方法。
- **真实世界实验**：基于Unitree Go2四足机器人+RealSense D457相机，在家庭、办公室、户外场景中测试ObjNav、EVT、ImageNav以及跨任务组合（如图像目标跟踪）。
- **评估指标**：Success Rate (SR)、SPL、Tracking Rate (TR)、Collision Rate (CR)。

## 四、资源与算力
- 训练在128块NVIDIA A100 GPU上进行。
- 三阶段训练时长未明确给出单次时长，但提供了步数信息：预训练1个epoch，SFT阶段20K步，在线RL 10轮迭代（每轮收集128集数据）。
- 推理时，使用单块NVIDIA RTX 4090 GPU，在500帧视频流下延迟<300ms，有效推理约2.5 FPS（含通信开销）。

## 五、实验数量与充分性
- 覆盖三个主要导航任务（ObjNav、EVT、ImageNav）共7个模拟基准，每个基准包含多个子集或难度设置。
- 进行了大量消融实验：
  - CoT策略（无CoT、密集CoT、固定间隔、自适应CoT）
  - 记忆模态（无记忆、纯视觉、纯语言、VLingMem）
  - 开放世界视频协同训练（有/无）
  - SFT训练步数影响
  - 在线RL不同收集策略（混合/专家/单纯）
  - 多任务协同（单任务 vs 多任务）
- 真实世界实验在三个场景类型（家庭、办公室、户外）中，每类设置多个目标（ObjNav每目标10次，EVT每场景10次，ImageNav每目标10次），兼顾随机性控制。
- 实验设计较为充分且公平：共享模型权重无任务微调，对比范围广泛，消融控制了变量。

## 六、论文的主要结论与发现
- VLingNav在所有模拟基准上达到SOTA，尤其在长程导航（MP3D ObjNav：SR提高26.4%）和干扰跟踪（EVT干扰跟踪SR提高1.7%，TR提高6.8%）上增益显著。
- 自适应CoT能以极低激活率（平均2.1%）带来大幅性能提升，优于固定间隔或密集推理。
- VLingMem（视觉+语言混合记忆）显著优于纯视觉或纯语言记忆，有效避免重复探索。
- 在线专家引导RL优于纯SFT和纯在线RL（混合收集策略最佳），说明专家纠偏+自我探索协同有效。
- 多任务联合训练带来跨任务和跨域涌现能力（例如语言指令跟踪可零样本迁移到图像目标跟踪；对人类跟踪可迁移到非人类物体跟踪）。
- 零样本真实世界部署成功，体现强sim-to-real泛化。

## 七、优点
- **创新的自适应推理机制**：基于双过程理论，动态决定何时进行显式CoT，在效率与性能间取得优秀平衡，推理激活率极低却大幅提升任务成功率。
- **语言驱动的持久记忆**：VLingMem将视觉信息转化为简洁语言摘要，与AdaCoT协同，有效解决长程导航中的记忆缺失和重复探索问题。
- **大规模高质量推理数据集**：Nav-AdaCoT-2.9M是当前最大导航推理数据集，覆盖多任务，通过自动化标注+严格筛选保证质量。
- **专家引导的在线RL框架**：混合收集策略（自身策略+专家纠偏）结合PPO范式，突破模仿学习局限，提升策略鲁棒性。
- **强大的泛化能力**：单模型跨任务、跨领域（如跟踪非人类目标、图像目标跟踪）零样本迁移，真实部署效果显著。
- **实验全面且可重复**：公开项目页面，提供详细超参数和训练细节。

## 八、不足与局限
- **感知局限**：仅依赖单目RGB摄像头的第一视角观察，视野有限（HFOV 90°），在大面积环境中可能遗漏关键信息。未来可集成多视角输入。
- **单系统架构限制频率**：采用单一VLM架构（无分离的快速反应系统），预测频率受限（约2.5 FPS），在高度动态环境中难以快速响应避障。计划升级为双系统架构（快慢系统）。
- **无灵活运动模型**：当前仅使用MPC-based waypoint控制器控制轨迹跟踪，缺乏更灵活的locomotion控制器（如直接输出电机速度），限制运动速度和可达区域。
- **训练资源需求高**：128块A100 GPU的门槛较高，可能限制其在资源受限场景的复现。
- **真实实验场景多样性有限**：真实世界仅在一个机器人平台、有限场景（办公室/家庭/户外各3个目标）进行，未在更复杂、开放场景（如密集人群、极端光照、不同地形）充分验证。
- **数据集偏差**：CoT标注依赖Qwen2.5-VL-72B，可能引入VLM自身偏见；导航数据主要来自模拟器（HM3D、MP3D等），虽然做了sim-to-real迁移但仍存在差距。

（完）
