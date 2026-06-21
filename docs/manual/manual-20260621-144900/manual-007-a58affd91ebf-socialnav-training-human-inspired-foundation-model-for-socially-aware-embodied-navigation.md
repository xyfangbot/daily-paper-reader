---
title: "SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation"
title_zh: "SocialNav: 训练仿人基础模型实现社交感知具身导航"
authors: "Ziyi Chen, Yingnan Guo, Zedong Chu, Minghua Luo, Yanfen Shen, Mingchao Sun, Junjun Hu, Shichao Xie, Kuan Yang, Pei Shi, Zhining Gu, Lu Liu, Honglin Han, Xiaolong Wu, Mu Xu, Yu Zhang, Ning Guo"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2511.21135v2"
arxiv_id: 2511.21135v2
arxiv_url: "https://arxiv.org/abs/2511.21135v2"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/007-2025_chen_socialnav-5fcf49d8-a58affd91ebf.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2511.21135v2", "query:Socially-Aware Navigation", "query:Foundation Model", "query:Reinforcement Learning", "query:Social Norms", "query:Embodied AI"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "社交感知导航是具身智能的重要挑战。本文提出SocialNav，一种层次化“大脑-行动”基础模型，通过构建包含700万样本的SocNav数据集（认知激活数据与专家轨迹金字塔），先以模仿学习注入导航技能与社会规范，再经提出的SAFE-GRPO流式强化学习进一步优化。实验表明，SocialNav在成功率上提升38%，社交合规率提升46%，为社交感知导航提供了有效范例。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 865, \"height\": 526, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1804, \"height\": 745, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1802, \"height\": 793, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1795, \"height\": 995, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 859, \"height\": 474, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1802, \"height\": 706, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1791, \"height\": 597, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1702, \"height\": 1689, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1507, \"height\": 364, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1307, \"height\": 426, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 867, \"height\": 321, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1798, \"height\": 389, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 804, \"height\": 532, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 865, \"height\": 232, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 662, \"height\": 500, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1532, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-007-a58affd91ebf-socialnav-training-human-inspired-foundation-model-for-socially-aware-embodied-navigation/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1510, \"height\": 427, \"label\": \"Table\"}]"
motivation: 现有导航模型缺乏对社交规范的理解，导致在人类环境中行为不自然或不安全。
method: 构建SocNav数据集（700万样本，含认知激活与专家轨迹），采用层次化架构，先模仿学习后SAFE-GRPO强化学习。
result: "成功率比SOTA高38%，社交合规率比SOTA高46%。"
conclusion: SocialNav表明结合大规模社交数据与多阶段训练可显著提升社交感知导航性能。
---

## 摘要
遵守社会规范的具身导航仍然是一个开放的研究挑战。我们的SocialNav是一个具有分层“大脑-动作”架构的社交感知导航基础模型，能够理解高层次社会规范并生成低层次、符合社交规范的轨迹。为了实现这种双重能力，我们构建了SocNav数据集，这是一个包含700万样本的大规模数据集，包括：(1) 认知激活数据集，提供社会推理信号，如思维链解释和社交可穿越性预测；(2) 专家轨迹金字塔，聚合来自互联网视频、模拟环境和真实世界机器人的多样化导航演示。我们提出了一个多阶段训练流程，逐步注入和优化导航智能：首先通过模仿学习向模型注入通用导航技能和社会规范理解，然后通过精心设计的社交感知流量探索GRPO（SAFE-GRPO）来优化这些技能，这是第一个基于流的具身导航强化学习框架，明确奖励符合社交规范的行为。与最先进的方法相比，SocialNav的成功率提高了38%，社交合规率提高了46%，在导航性能和社交合规性方面均表现出强劲的提升。

## Abstract
Embodied navigation that adheres to social norms remains an open research challenge. Our SocialNav is a foundational model for socially-aware navigation with a hierarchical "brain-action" architecture, capable of understanding high-level social norms and generating low-level, socially compliant trajectories. To enable such dual capabilities, we construct the SocNav Dataset, a large-scale collection of 7 million samples, comprising (1) a Cognitive Activation Dataset providing social reasoning signals such as chain-of-thought explanations and social traversability prediction, and (2) an Expert Trajectories Pyramid aggregating diverse navigation demonstrations from internet videos, simulated environments, and real-world robots. A multi-stage training pipeline is proposed to gradually inject and refine navigation intelligence: we first inject general navigation skills and social norms understanding into the model via imitation learning, and then refine such skills through a deliberately designed Socially-Aware Flow Exploration GRPO (SAFE-GRPO), the first flow-based reinforcement learning framework for embodied navigation that explicitly rewards socially compliant behaviors. SocialNav achieves +38% success rate and +46% social compliance rate compared to the state-of-the-art method, demonstrating strong gains in both navigation performance and social compliance.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有具身导航模型（如GNM、ViNT、NoMaD）主要关注最短路径规划和碰撞避免，忽视了人类环境中普遍的社会规范（例如：不应横穿马路、不应穿越草坪或机动车道）。
- 缺乏社会意识的导航会导致机器人在真实场景中出现不安全、不自然的社交违规行为（如“闯红灯”、穿越私家草地），阻碍其在实际生活中的部署（如导盲机器人）。
- 本文的研究动机是解决“如何让机器人同时理解高层次的社会规范并生成低层次的符合规范的运动轨迹”这一开放挑战，从而使导航既高效又社会友好。

## 二、论文提出的方法论
- **核心思想**：构建一个分层次的“大脑-行动”基础模型（SocialNav），将高层次的社会语义理解与低层次的轨迹生成相解耦。
- **模型架构**：
  - **大脑模块（Brain Module）**：基于视觉-语言模型（VLM，采用Qwen2.5-VL-3B），负责从图像和历史位姿中推理出三类可解释输出：社交可穿越区域（多边形）、导航思维链（CoT）和通用视觉问答（VQA）。
  - **行动专家（Action Expert）**：基于条件流匹配（Conditional Flow Matching）的扩散Transformer（12层，12头，隐藏维1536），以大脑模块的最后一层隐藏特征为条件，生成未来5步的轨迹点。
- **多阶段训练流程**：
  1. **预训练（Stage 1）**：使用大规模专家轨迹金字塔（ETP，包含互联网视频、模拟场景数据）和认知激活数据集（CAD，包含社交可穿越性标注、CoT、VQA），进行端到端的模仿学习，激活VLM的导航能力并训练流模型预测底层级航点。
  2. **微调（Stage 2）**：冻结VLM，仅使用高质量真实机器人轨迹（Dreal）对行动专家进行微调，缩小仿真到现实的差距。
  3. **强化学习对齐（Stage 3）**：提出**SAFE-GRPO**（Socially-Aware Flow Exploration GRPO），是第一个用于具身导航的基于流的强化学习框架。它将确定性ODE变为随机SDE（dxt = vflow dt + σt dw），在保留VLM语义条件下进行受控探索，并通过手工设计的奖励函数（包括社会合规奖励Rsocial、专家相似Rexpert、平滑Rsmooth、效率Reff）对符合社会规范的行为进行显式鼓励。

## 三、实验设计
- **使用的数据集/场景**：
  - 训练：自建SocNav数据集（700万样本），包含专家轨迹金字塔ETP（2M互联网视频伪轨迹 + 1.7M模拟场景轨迹 + 340K真实机器人轨迹）和认知激活数据集CAD（1.2M社交可穿越性标注 + 825K导航CoT + 1M通用VQA）。
  - 基准测试：自建SocNav Benchmark，基于Isaac Sim物理引擎和3DGS照片级渲染，包含9个新捕获的大型社交场景（3个公园、3条街道、2个办公室、1个校园，总面积73K m²），每个场景采样10对起点-终点（20m和100m距离），共180个测试用例。
- **对比方法**：GNM、ViNT、NoMaD、CityWalker——均为开源的点目标导航方法，部分基线重新训练为点目标任务。
- **评估设置**：三种评估环境：
  - 开环评估（CityWalker Benchmark）：指标为最大平均方向误差（MAOE）。
  - 闭环评估（SocNav Benchmark）：指标包括成功率（SR）、路径完成率（RC）、SPL，以及社会合规指标距离合规率（DCR）和时间合规率（TCR）。
  - 真实世界部署：在Unitree Go2机器人上，跨3个环境（街道过街、办公园区、购物商场），每个环境20次试验，共60次试验。
- **消融实验**：系统性地添加数据成分（Dvideo、Dsim、Dcog）和训练阶段（IL vs. RL），分析各组件贡献；还消融了RL奖励函数中的Rsocial。

## 四、资源与算力
- **训练算力**：
  - 预训练阶段：96块H20 GPU，batch size=192，学习率5×10⁻⁵，训练3个epoch。
  - 微调阶段：32块H20 GPU，batch size=256，学习率1×10⁻⁵。
  - SAFE-GRPO阶段：16块H20 GPU，rollout batch size=128，学习率5×10⁻⁷。
- **推理硬件**：真实世界部署时使用云端NVIDIA A10 GPU，控制频率>5Hz。
- **未明确说明**：总训练时间、单阶段耗时等细节未在文中明确给出。

## 五、实验数量与充分性
- **实验数量**：在三大评估维度下共设计超过10组实验，包括：
  - 开环6个场景对比（表1）；
  - 闭环9个场景、5项指标对比（表2）；
  - 真实世界3个环境各20次试验（表3）；
  - 消融实验6组（表4），覆盖数据成分和训练阶段的逐步增加；
  - 额外奖励消融1组（表8）；开环基线再训练对比（表9）。
- **充分性与公平性**：
  - 开环和闭环均采用多个独立场景、统一机器人和物理设置，确保比较基准一致。
  - 基线方法均重新训练为点目标导航，避免架构不匹配。
  - 消融实验细致，涵盖了数据量、认知数据、强化学习各环节的影响，能够清晰量化每个模块的贡献。
  - 真实世界实验虽仅60次试验，但涵盖了不同复杂度场景且多次验证，结果具有统计显著性。
  - 总体实验设计客观、系统、公平，足以支撑主要结论。

## 六、论文的主要结论与发现
- SocialNav在各项指标上显著超越所有基线：
  - 开环MAOE降低至10.2，比CityWalker低约33%。
  - 闭环SR达到86.1%（比CityWalker +38.3%），RC 91.2%，SPL 77.4%。
  - 社会合规指标DCR 82.5%、TCR 82.9%，比CityWalker（约36%）提升超过一倍，即社交合规率提升46%。
  - 真实世界平均SR 85%（最佳基线CityWalker 62.5%）。
- 关键发现：
  - 大规模互联网视频（Dvideo）和模拟恢复轨迹（Dsim）显著增强导航鲁棒性；认知激活数据（Dcog）对社交合规至关重要且是强化学习成功的前提。
  - SAFE-GRPO在没有Dcog时反而损害社交合规（DCR下降），表明高层语义认知是RL有效对齐社会规范的必要条件。
  - 强化学习后SPL略有下降（79.4→77.4），反映社会合规与几何最短路径之间存在固有权衡，模型更倾向于人类偏好的安全路径。

## 七、优点
1. **方法创新**：首次将条件流匹配与VLM结合用于社交导航，提出层次化推理-生成解耦架构，既保证了可解释性又实现了高精度轨迹生成。
2. **数据集规模与多样性**：SocNav数据集达700万样本，覆盖真实、模拟、互联网三种来源，并包含认知激活任务（CoT、可穿越性、VQA），为社交导航提供了前所未有的训练资源。
3. **强化学习框架新颖**：SAFE-GRPO是首个基于流的RL方法用于导航，通过在流积分中引入SDE提供受控探索，同时保持VLM语义固定，有效平衡探索与利用。
4. **评估全面**：开环、闭环、真实世界三层次评估，引入专门的社会合规指标（DCR/TCR），消融实验系统深入，结论扎实。
5. **实际部署可行**：在低成本GPU（A10）上实现>5Hz实时控制，具备实用潜力。

## 八、不足与局限
1. **奖励设计依赖手工规则**：Rsocial等奖励基于手工标注的占据图和距离变换，难以泛化到未见过的或更复杂的（如文化差异）社交规范。
2. **认知数据生成依赖封闭集VLM**：CoT数据由Qwen2.5-VL-72B生成，可能存在偏见或遗漏，影响认知激活数据的质量。
3. **强化学习场景单一**：SAFE-GRPO仅在Dsim中的SocCity场景训练，未覆盖互联网视频或真实数据，可能导致RL阶段对仿真环境的过拟合。
4. **真实世界实验规模有限**：仅3个环境、60次试验，且使用单一机器人（Unitree Go2），未测试不同形态或更多样化的动态场景（如人群中、繁忙路口）。
5. **未见对失败案例的分析**：论文未详细讨论SR未达到100%的部分失败原因，例如碰撞、社交违规的具体类型，限制了方法的深度理解。
6. **计算资源需求高**：预训练需要96块H20 GPU，对多数实验室团队来说门槛较高，但论文未提供蒸馏或小模型方案。

（完）
