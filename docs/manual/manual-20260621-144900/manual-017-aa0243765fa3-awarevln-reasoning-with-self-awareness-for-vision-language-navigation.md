---
title: "AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation"
title_zh: "AwareVLN: 具有自我意识的视觉语言导航推理"
authors: "Wenxuan Guo, Xiuwei Xu, Yichen Liu, Xiangyu Li, Hang Yin, Huangxing Chen, Wenzhao Zheng, Jianjiang Feng, Jie Zhou, Jiwen Lu"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2605.22816v1"
arxiv_id: 2605.22816v1
arxiv_url: "https://arxiv.org/abs/2605.22816v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/017-2026_guo_awarevln-f1410476-aa0243765fa3.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2605.22816v1", "query:Vision-and-Language Navigation", "query:Self-aware Reasoning", "query:Vision-Language Models", "query:Embodied AI", "query:Navigation"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航中现有方法缺乏对自身状态与任务进度的显式理解。AwareVLN通过结构推理模块实现空间与任务导向的自我感知，并设计自动数据引擎按进度划分训练样本。在Habitat模拟器上显著超越先前方法。其贡献在于以端到端方式引入可解释的自我推理。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1799, \"height\": 685, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1718, \"height\": 810, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1738, \"height\": 722, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 594, \"height\": 294, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1805, \"height\": 675, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1684, \"height\": 207, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 596, \"height\": 292, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 837, \"height\": 150, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 853, \"height\": 483, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1749, \"height\": 296, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1747, \"height\": 265, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1746, \"height\": 306, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1633, \"height\": 273, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1630, \"height\": 310, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1606, \"height\": 280, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1727, \"height\": 983, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 878, \"height\": 236, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 791, \"height\": 255, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 809, \"height\": 223, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-017-aa0243765fa3-awarevln-reasoning-with-self-awareness-for-vision-language-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 883, \"height\": 456, \"label\": \"Table\"}]"
motivation: 现有VLN方法缺乏对智能体自身状态与任务进度的显式可解释理解。
method: 提出AwareVLN，包含结构推理模块实现自我感知，以及自动数据引擎按进度划分训练。
result: 在Habitat模拟器多个数据集上显著超越先前最先进方法。
conclusion: AwareVLN以端到端数据驱动方式赋予模型自我感知推理能力，提升了导航性能。
---

## 摘要
视觉语言导航要求智能体根据语言指令在视觉环境中自主移动。尽管最先进的方法利用视觉语言模型的推理能力进行端到端的动作预测，但它们往往缺乏对智能体、指令和场景之间关系的显式且可解释的理解。相反，显式构建场景地图进行启发式规划直观上很有吸引力，但依赖于额外的3D传感器，并阻碍了大规模视觉语言预训练。为弥合这一差距，我们提出AwareVLN，一种新颖框架，为导航模型配备自我意识推理机制，使其能够以完全端到端和数据驱动的方式理解智能体状态和任务进展。我们的方法有两个关键创新：（1）结构推理模块，培养空间和任务导向的自我意识；（2）自动数据引擎，包含进度划分以实现有效训练。在Habitat模拟器中多个数据集上的大量实验表明，我们的AwareVLN显著优于先前最先进的视觉语言导航方法。

## Abstract
Vision-and-Language Navigation (VLN) requires an agent to ground language instructions to its own movement within a visual environment. While state-of-the-art methods leverage the reasoning capabilities of Vision-Language Models (VLMs) for end-to-end action prediction, they often lack an explicit and explainable understanding of the relationships between the agent, the instruction, and the scene. Conversely, explicitly building a scene map for heuristic planning is intuitively appealing but relies on additional 3D sensors and hinders large-scale vision-language pre-training. To bridge this gap, we propose AwareVLN, a novel framework that equips the navigation model with a self-aware reasoning mechanism, enabling it to understand the agent's state and task progress in a fully end-to-end and data-driven manner. Our approach features two key innovations: (1) a structural reasoning module that fosters spatial and task-oriented self-awareness, and (2) an automatic data engine with progress division for effective training. Extensive experiments on various datasets in Habitat simulator show our AwareVLN significantly outperforms previous state-of-the-art vision-language navigation methods.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究背景**：视觉语言导航要求智能体根据自然语言指令在未知环境中自主移动。现有方法分为两类：一类依赖显式拓扑图和3D传感器（如SLAM），另一类采用端到端视觉语言模型直接预测动作。
- **核心问题**：当前VLM-based方法虽然利用了大模型推理能力，但只关注端到端动作预测，缺乏对智能体自身状态、任务进度和指令-环境关系的显式、可解释的理解，导致在复杂长程导航中难以进行子任务规划和错误纠正。
- **研究动机**：如何让导航模型具备自我意识（self-awareness）——即能够自动判断位置、识别偏差、评估进度、规划下一步，并以端到端数据驱动的方式实现，同时保持计算效率和可解释性。
- **解决思路**：提出AwareVLN，引入稀疏、结构化的自我推理机制，仅在关键导航节点触发深度分析，并设计自动数据引擎生成高质量推理训练数据。

## 二、论文提出的方法论
- **核心思想**：统一视觉语言模型同时执行动作预测和自我反思推理，通过特殊令牌控制“推理模式”与“动作模式”的切换，实现稀疏推理。
- **关键技术细节**：
  1. **统一推理-动作框架**：模型πθ基于指令I、观测序列Ot和上一次推理结果R及相对步数编码，输出一个logit d和文本yt。若d[REASON] > d[ACT]则输出[REASON]进入推理模式，否则输出[ACT]生成动作命令并解析为低层动作执行。
  2. **结构化推理格式**：推理输出包含三个因果成分：①场景描述（当前视觉上下文）；②进度评估（已完成指令部分、是否偏差）；③下一步计划。
  3. **稀疏触发时机**：仅在三种关键节点触发推理：子任务完成（如房间切换）、路径偏差识别与纠正、停止错误检测与重规划。
  4. **自动数据引擎**：利用Habitat模拟器中场景语义标注和真值路径自动标注关键节点。采用两种收集策略：①完美跟随真值轨迹；②DAgger式采样（用早期模型导航并纠正返回），采集包含错误-纠正的真实轨迹。将多模态上下文（节点类型、观测、房间切换、进度百分比、纠正视频）输入Qwen-VL-Max生成结构化推理文本，按多轮对话流程逐步生成全局理解、子任务节点、偏差节点、停止节点推理。
- **训练流程**：预训练阶段使用常规导航数据和VQA数据；微调阶段使用自动引擎生成的推理增强轨迹和额外人类视频，训练在4×NVIDIA H20上完成，推理在单张RTX 4090上约1 FPS。

## 三、实验设计
- **数据集与Benchmark**：①R2R-CE（Val-Unseen含1,839个episode）；②RxR-CE（Val-Unseen含11,006个episode，三语言长轨迹）；③真实世界：自制18条指令在Corridor/Home/Office三类环境简单+复杂任务。
- **评价指标**：导航误差（NE）、成功率（SR）、SPL（成功率加权路径长度）、nDTW等。
- **对比方法**：涵盖三大类：①使用深度+全景+里程计的显式建图方法（如CMA、GridMM、ETPNav等）；②纯RGB端到端方法（如NaVid、NaVILA、StreamVLN）；③使用VLM推理的方法（如Nav-R1等）。共对比约20个方法。

## 四、资源与算力
- 论文明确说明训练使用4块NVIDIA H20 GPU，推理使用单张NVIDIA RTX 4090 GPU，推理速度约1 FPS。未报告具体训练时长（小时/天数）和参数量。

## 五、实验数量与充分性
- **实验组数**：①主表对比实验（Tab.1）覆盖R2R和RxR两个数据集，含20+方法；②真实世界定量评估（Tab.2）含3环境×2复杂度×每环境3条指令（共18条）；③消融实验（Tab.3）分析三种关键节点各自贡献；④架构消融（Tab.4）比较有无特殊令牌、稠密vs稀疏推理；⑤跨数据集泛化实验（Tab.5）RxR上未见场景测试；⑥四种仿真rollout可视化+真实环境部署展示。
- **充分性与公平性**：实验比较全面，涵盖了仿真和真实环境，消融逐项归因。对比方法按观测类型分组标注，公平性较好。真实环境评测指令较少（18条），样本量有限但具参考价值。

## 六、论文的主要结论与发现
- 在R2R-CE Val-Unseen上，SR达65.4%、SPL 55.1%，超越所有纯RGB输入方法，且优于多数使用深度/全景的建图方法。
- 在RxR-CE Val-Unseen上，SR 67.6%、SPL 56.1%，大幅领先先前方法。
- 真实世界评测三个环境中SR显著高于NaVid和NaVILA，证明有效泛化。
- 消融表明：子任务完成节点贡献最大，路径偏差和停止错误节点均不可或缺；稀疏推理优于稠密推理，特殊令牌结构优于无令牌直接输出。
- 可解释性：模型在仿真和真实环境中生成了结构化推理轨迹，成功展示自我纠错和进度认知。

## 七、优点
- **方法创新**：首次在端到端VLN中引入稀疏结构化自我意识推理，避免计算浪费，提升可解释性。
- **数据生成自动化**：无需人工标注，利用模拟器语义和真值自动标注关键节点，再利用通用VLM生成高质量推理数据，可扩展性强。
- **统一框架**：单模型同时完成推理和动作，避免两阶段级联带来误差累积。
- **性能领先**：在多项指标上显著超越SOTA，尤其纯RGB场景下表现突出，部署友好。
- **跨域验证**：同时包含仿真和真实环境定量+定性评估，验证了泛化能力。

## 八、不足与局限
- **3D感知精度不足**：论文自述在真实部署时偶尔发生碰撞门框或停止位置偏差，说明基于单目RGB的3D理解有限。
- **推理速度限制**：约1 FPS，难以支持实时高频控制，可能需边缘端优化。
- **真实世界评测规模较小**：仅18条指令，任务复杂度和环境多样性有限，统计显著性存疑。
- **未披露完整训练成本**：GPU数量和型号已知，但缺少训练周期和能耗等细节。
- **对模拟场景语义标注依赖**：自动数据引擎依赖Habitat提供的房间级语义和真值路径，在无此类标注的开放环境中不可直接应用。
- **对比实验未包含所有最新方法**：尤其某些使用更强VLM基座的方法（如GPT-4V等）未纳入比较。

（完）
