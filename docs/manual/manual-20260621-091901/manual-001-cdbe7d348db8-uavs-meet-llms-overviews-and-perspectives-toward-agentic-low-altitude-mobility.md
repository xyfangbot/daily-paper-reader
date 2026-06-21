---
title: "UAVs Meet LLMs: Overviews and Perspectives Toward Agentic Low-Altitude Mobility"
title_zh: 无人机遇见大语言模型：迈向自主低空移动的综述与展望
authors: "Yonglin Tian, Fei Lin, Yiduo Li, Tengchao Zhang, Qiyao Zhang, Xuan Fu, Jun Huang, Xingyuan Dai, Yutong Wang, Chunwei Tian, Bai Li, Yisheng Lv, Levente Kovacs, Fei-Yue Wang"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2501.02341v2"
arxiv_id: 2501.02341v2
arxiv_url: "https://arxiv.org/abs/2501.02341v2"
manual_pdf_url: assets/manual-pdfs/manual-20260621-091901/001-001-uav_vln-cdbe7d348db8.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2501.02341v2", "query:Unmanned aerial vehicles", "query:large language models", "query:foundation intelligence", "query:low altitude mobility systems"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 当前无人机操作依赖人工控制，仅在简单场景中具备有限自主性，难以适应复杂环境。本文探索将大型语言模型（LLM）与无人机集成，以提升其智能和适应性。系统梳理了无人机系统组件、LLM技术现状以及多模态数据资源，分类分析了关键任务和应用场景。最后提出了从自主感知、记忆、推理到工具使用的智能无人机发展路线图，为实现自主低空移动性提供了参考。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1748, \"height\": 1353, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 916, \"height\": 657, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 916, \"height\": 592, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1455, \"height\": 1452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1670, \"height\": 1013, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1872, \"height\": 690, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1883, \"height\": 511, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1766, \"height\": 1965, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1865, \"height\": 805, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1810, \"height\": 1007, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1805, \"height\": 661, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1808, \"height\": 573, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1808, \"height\": 1075, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1807, \"height\": 884, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1808, \"height\": 1128, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-091901-manual-001-cdbe7d348db8-uavs-meet-llms-overviews-and-perspectives-toward-agentic-low-altitude-mobility/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1789, \"height\": 1767, \"label\": \"Table\"}]"
motivation: 解决无人机在复杂环境中缺乏智能和适应性、依赖人工控制的问题，借助LLM的强大推理与泛化能力推进自主化。
method: 概述UAV系统组成与LLM技术，梳理多模态数据资源，分类分析UAV与LLM融合的关键任务和应用场景，并设计实现智能无人机的路线图。
result: 构建了涵盖多模态数据、关键任务和应用场景的UAV-LLM集成框架，提出了实现自主感知、记忆、推理与工具使用的路线图。
conclusion: 通过集成LLM，无人机可逐步实现智能体能力，为低空自主移动提供可行路径。
---

## 摘要
低空移动性，以无人机为例，已在交通、物流和农业等多个领域带来了变革性进展。凭借灵活的视角和快速的机动性，无人机扩展了传统系统的感知和行动能力，引起了学术界和工业界的广泛关注。然而，当前的无人机操作主要依赖人工控制，仅在简单场景中具备有限的自主性，缺乏应对更复杂环境和任务所需的智能和适应性。大语言模型的出现展现了卓越的问题解决和泛化能力，为推进无人机智能提供了一条有前景的途径。本文探讨了大语言模型与无人机的融合，首先概述了无人机系统的基本组件和功能，随后介绍了最先进的大语言模型技术。接着，系统性地强调了无人机可用的多模态数据资源，这些资源为训练和评估提供了关键支持。此外，对无人机与大语言模型融合的关键任务和应用场景进行了分类和分析。最后，提出了面向自主无人机的参考路线图，使无人机能够通过自主感知、记忆、推理和工具利用实现代理式智能。

## Abstract
Low-altitude mobility, exemplified by unmanned aerial vehicles (UAVs), has introduced transformative advancements across various domains, like transportation, logistics, and agriculture. Leveraging flexible perspectives and rapid maneuverability, UAVs extend traditional systems’ perception and action capabilities, garnering widespread attention from academia and industry. However, current UAV operations primarily depend on human control, with only limited autonomy in simple scenarios, and lack the intelligence and adaptability needed for more complex environments and tasks. The emergence of large language models (LLMs) demonstrates remarkable problem-solving and generalization capabilities, offering a promising pathway for advancing UAV intelligence. This paper explores the integration of LLMs and UAVs, beginning with an overview of UAV systems’ fundamental components and functionalities, followed by an overview of the state-of-the-art LLM technology. Subsequently, it systematically highlights the multimodal data resources available for UAVs, which provide critical support for training and evaluation. Furthermore, key tasks and application scenarios where UAVs and LLMs converge are categorized and analyzed. Finally, a reference roadmap towards agentic UAVs is proposed to enable UAVs to achieve agentic intelligence through autonomous perception, memory, reasoning, and tool utilization.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 当前无人机（UAV）操作高度依赖人工控制，仅在简单场景下具备有限自主性，在复杂动态环境中缺乏智能和适应性。
- 大语言模型（LLM）展现出强大的问题解决和泛化能力，为提升无人机自主性提供了新途径。
- 论文旨在系统性综述LLM与UAV融合的现状，并勾勒出朝着自主智能体（Agentic UAV）发展的路线图，推动低空移动系统的智能化转型。

## 二、论文提出的方法论
- **核心思想**：构建一套系统性的集成框架，将LLM、视觉基础模型（VFM）和视觉语言模型（VLM）嵌入UAV的传统功能模块中，以增强感知、推理、规划和交互能力。
- **关键技术细节**：
  - 全面梳理UAV系统的七大功能模块（感知、导航、规划、控制、通信、交互、载荷）及多种构型（固定翼、多旋翼、混合翼等）。
  - 详细总结LLM、VLM、VFM的代表性模型及其核心能力（零样本学习、链式推理、多模态对齐）。
  - 分类整理了面向UAV的公开数据集（环境感知、事件识别、目标跟踪、导航定位等8大类）和仿真平台（AirSim、CARLA、Isaac Sim等）。
  - 提出了名为 **Agentic UAV** 的通用架构，包含五大模块：
    - **数据模块**：将UAV多模态数据转换为适合LLM/VLM微调的格式；
    - **知识模块**：通过检索增强生成（RAG）注入领域知识（空域规则、场景库等）；
    - **工具模块**：集成通用工具（如Grounding DINO、SAM）和专用工具（如PX4飞控）；
    - **FM模块**：选择并优化LLM/VLM（通过提示工程、LoRA微调、RLHF等）；
    - **代理模块**：包括管理者代理和UAV个体代理工作流，实现感知→规划→控制的自主循环与多机协作。
- 未提出新的数学公式或算法流程，而是以概念架构和分类综述为主。

## 三、实验设计
- **本文为综述论文，未自行设计实验**。但系统整理了现有研究中的实验设置，包括：
  - **数据集**：在表格3-9中列出了超过60个公开UAV数据集，覆盖交通、遥感、农业、军事、野生动物等领域（如VisDrone、DOTA、UAV-Human、FloodNet等）。
  - **仿真平台**：介绍了AirSim、CARLA、NVIDIA Isaac Sim、AerialVLN Simulator、Embodied City等。
  - **基准方法对比**：表格10汇总了近50篇文献中的方法，按任务（视觉感知、VLN、规划、飞行控制、基础设施）列出所用基座模型（如GPT-4、LLaVA、Grounding DINO）和类型（VLM、VFM、LLM组合）。
- 论文未提供统一的benchmark数值比较，而是通过文献调研展示各类方法的适用场景。

## 四、资源与算力
- 文中未提及作者团队自己的算力消耗（因为是无实验的综述）。
- 仅在介绍LLM时提及模型规模（如GPT-3有175B参数），但未涉及训练或推理所需的具体GPU型号、数量、时长。

## 五、实验数量与充分性
- 作为综述，无直接实验。但从文献覆盖度看：
  - 引用了超过400篇参考文献，覆盖2014至2025年；
  - 数据集表格包含60+个数据集，并附有年份、类型、规模描述；
  - 方法表格（表10）系统对比了不同任务下的代表性工作，每个子任务至少列举3-10种方法。
- **充分性评价**：实验/数据覆盖性较高，分类清晰，但缺乏定量对比（如表格中无性能数字）；对于Agentic UAV框架本身，论文未提供任何仿真或真实环境验证，属于概念性提案。

## 六、论文的主要结论与发现
- LLM/VLM的集成能显著增强UAV的感知、推理、规划和人类交互能力，在视觉-语言导航、目标搜索、编队控制等任务中表现出潜力。
- 提出了“Agentic UAV”参考框架，强调未来无人机应具备自主感知、记忆、推理和工具利用的智能体能力。
- 当前主要挑战有三：
  1. **计算成本**：大模型参数量大，实时推理在资源受限的UAV平台上困难；
  2. **安全性**：模型幻觉可能带来不安全行为；
  3. **基础设施不足**：缺乏可靠的通信、供能网络支撑大规模部署。
- 未来方向包括：模型量化与边缘计算、空地海多域协同无人系统。

## 七、优点
- **系统性全面**：从系统、模型、数据三方面进行完整梳理，首次整合了UAV与多种基础模型的融合现状。
- **分类清晰**：将任务划分为视觉感知、VLN、规划、控制、基础设施五大类，便于研究者快速定位。
- **数据资源丰富**：整理了大量公开数据集和仿真平台，并附有官方链接，实用性强。
- **前瞻性框架**：提出的Agentic UAV架构具备模块化、可扩展性，为后续研究提供了明确路线图。
- **问题分析透彻**：对传统AI方法的局限性（泛化差、多任务弱、人机交互难）和LLM的优势（自然语言理解、零样本、多模态）分析到位。

## 八、不足与局限
- **缺乏实证验证**：Agentic UAV框架仅为概念设计，未在仿真或真实环境中实现或评估，可行性存疑。
- **定量对比缺失**：综述中未提供任何统一指标下的性能数值对比，读者难以直接比较不同方法的优劣。
- **计算资源讨论肤浅**：仅提及大模型计算成本高，但未量化在典型UAV硬件（如Jetson系列）上的推理时延、能耗等实际约束。
- **数据偏差风险**：所汇总数据集中多数为特定场景采集（如城市、交通），对极端环境（如极地、沙漠、夜间）覆盖不够；部分数据集更新滞后。
- **多机协作机制细节不足**：虽然提到Manager Agent和个体工作流，但未深入讨论通信延迟、动态拓扑、鲁棒性等实际应用中的关键问题。
- **缺乏与现有强基线对比**：未与传统方法（如基于强化学习的规划）进行系统对比，难以凸显LLM集成带来的具体提升幅度。

（完）
