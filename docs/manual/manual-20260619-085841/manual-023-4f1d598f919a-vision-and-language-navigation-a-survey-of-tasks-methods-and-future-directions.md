---
title: "Vision-and-Language Navigation: A Survey of Tasks, Methods, and Future Directions"
title_zh: 视觉与语言导航：任务、方法与未来方向综述
authors: "Jing Gu, Eliana Stefani, Qi Wu, Jesse Thomason, Xin Eric Wang"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/023-2022_gu_vln_survey-c0bf7e01-4f1d598f919a.pdf
tags: ["query:手动上传", "paper:PDF", "query:VLN", "query:Vision-and-Language Navigation", "query:survey", "query:embodied agents", "query:instruction following"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 构建能通过自然语言与人类交流、感知环境并执行真实任务的智能体是AI长期目标。视觉与语言导航（VLN）作为基础跨学科课题，受到自然语言处理、计算机视觉、机器人等领域关注。本文系统综述了VLN的任务、评价指标与方法，通过结构化分析当前进展与挑战，指出了现有VLN的局限性及未来研究方向。该综述为VLN研究社区提供了全面参考。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-023-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 736, \"height\": 528, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-023-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 794, \"height\": 706, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-023-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1653, \"height\": 919, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-023-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1638, \"height\": 1481, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-023-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1025, \"height\": 458, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-023-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1637, \"height\": 931, \"label\": \"Table\"}]"
motivation: 推动构建能够自然语言交互、环境感知与执行任务的智能代理，VLN作为关键跨学科课题缺乏系统综述，需总结现状与挑战。
method: 回顾当代VLN研究，涵盖任务定义、评价指标、方法体系等，通过结构化分析梳理进展与局限性。
result: 揭示了当前VLN在导航鲁棒性、语言理解与视觉感知整合等方面的局限，并指出了跨任务泛化、多模态融合等未来方向。
conclusion: 本文为VLN社区提供了全景式参考，有助于促进该领域的系统性发展与创新。
---

## 摘要
人工智能研究的一个长期目标是构建能够用自然语言与人类交流、感知环境并执行现实世界任务的智能体。视觉与语言导航（VLN）是实现这一目标的基础性和跨学科研究课题，并受到自然语言处理、计算机视觉、机器人学和机器学习领域的日益关注。本文回顾了新兴的VLN领域的当代研究，涵盖了任务、评估指标、方法等。通过对当前进展和挑战的结构化分析，我们指出了当前VLN的局限性以及未来工作的机遇。本文为VLN研究社区提供了全面的参考。

## Abstract
A long-term goal of AI research is to build intelligent agents that can communicate with humans in natural language, perceive the environment, and perform real-world tasks. Vision-and-Language Navigation (VLN) is a fundamental and interdisciplinary research topic towards this goal, and receives increasing attention from natural language processing, computer vision, robotics, and machine learning communities. In this paper, we review contemporary studies in the emerging field of VLN, covering tasks, evaluation metrics, methods, etc. Through structured analysis of current progress and challenges, we highlight the limitations of current VLN and opportunities for future work. This paper serves as a thorough reference for the VLN research community.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：构建能够理解自然语言、感知环境并自主完成任务的智能体是人工智能的长期目标，而视觉与语言导航（VLN）是实现该目标的基础且跨学科的研究课题。VLN在自然语言处理、计算机视觉、机器人学和机器学习等领域日益受到关注。
- **整体含义**：本文是一篇全面的VLN综述，系统梳理了现有任务定义、基准数据集、评估指标、核心方法以及存在的挑战，旨在为VLN研究社区提供结构化参考，并指出未来发展方向。

## 二、论文提出的方法论
- **论文本身是综述，并未提出新方法，而是对现有方法进行结构化分类和梳理**：
  1. **表示学习（Representation Learning）**：
     - 预训练：利用预训练的视觉（ResNet、ViT）或语言模型（BERT、GPT）进行单模态初始化；多模态预训练（ViLBERT、VLN-BERT、PREVALENT）学习联合表示。
     - 语义理解：区分高低层视觉特征、指令内不同令牌（物体、方向）的作用；利用注意力机制进行跨模态软对齐。
     - 图表示：构建指令与环境的语义关系图（GNN编码），用于路径预测或行动概率分布。
     - 记忆增强模型：使用LSTM/Transformer记录导航历史（如HAMT分层编码），或构建独立记忆模块存储相关信息。
     - 辅助任务：添加额外损失（如动作解释、未来预测、视觉-指令对齐）以增强理解，无需额外标签。
  2. **动作策略学习（Action Strategy Learning）**：
     - 强化学习（RL）：将VLN建模为马尔可夫决策过程，设计细粒度奖励（指令忠实度、地标对齐、CLS/nDTW等指标作为奖励信号）。
     - 导航中的探索：学生强制、探索-利用权衡（何时回溯、如何深度探索），使用世界模型（Pathdreamer）合成未来视角。
     - 导航规划：预测航点、下一状态与奖励、生成未来观测或融入邻域视图；基于指令预测里程碑、分解子任务。
     - 求助机制：利用动作概率或独立模型判断何时请求帮助；基于规则或神经网络的对话系统（如DialFRED使用语言模型作为Oracle）。
  3. **数据驱动学习（Data-centric Learning）**：
     - 数据增强：训练“说话者”模块生成轨迹-指令对，用对齐评分器或对抗鉴别器筛选；环境增强（随机遮罩、场景拆分重组、风格转移）增加多样性。
     - 课程学习：按指令长度或路径复杂程度逐步增加难度。
     - 多任务学习：跨VLN相关任务（如对话导航、QA）共享知识。
     - 指令解释：编码多条指令、将长指令拆分为子指令、通过解释明确目标物体类别。
  4. **先验探索（Prior Exploration）**：
     - 允许代理在测试环境中进行无监督探索（如自监督模仿学习、环境适应），构建环境地图或拓扑图以提升在未见环境中的泛化能力。

## 三、实验设计
- **论文是综述，不包含作者自己的实验。** 但它对现有VLN任务的基准数据集、评估指标和代表性方法进行了全面汇总：
  - **数据集**：按照“通信复杂度”（初始指令、Oracle引导、人类对话）和“任务目标”（细粒度导航、粗粒度导航、导航+物体交互）两个维度分类。主要数据集包括：
    - 细粒度导航：R2R（Matterport3D）、Room-for-Room、RxR、VLNCE（连续环境）、TOUCHDOWN（户外街景）、LANI（无人机）等。
    - 粗粒度导航：RoomNav、EmbodiedQA、REVERIE、SOON。
    - 导航+物体交互：IQA、ALFRED、CHAI等。
    - Oracle引导：Just Ask、VNLA、HANNA、CEREALBAR。
    - 对话：CVDN、RobotSlang、Talk the Walk、TEACh、DialFRED。
  - **评估指标**：
    - 目标导向指标：成功率（SR）、路径长度（PL）、SPL（成功率加权路径长度）、SED、Oracle成功率和导航误差等。
    - 路径保真度指标：nDTW、SDTW、CLS等。
  - **基准方法对比**：整理R2R测试未见过环境上的排行榜（表4），列出了从Seq-to-Seq (2018)到HAMT、Airbert (2021)等20余种方法的TL、NE、OSR、SR、SPL等结果，包括单次运行、先验探索和束搜索设置。
  - **模拟器**：Matterport3D、Habitat、AI2-THOR、Gibson、House3D、Google Street View等。

## 四、资源与算力
- **文中未明确说明综述所涉及的各个方法使用的具体算力资源（GPU型号、数量、训练时长等）。** 仅简单提及一些方法可训练数亿参数模型（如PREVALENT、VLN-BERT），但无量化细节。因此，无法总结具体算力开销。综述研究本身不需要大量计算资源。

## 五、实验数量与充分性
- **本文不包含原始实验**，但作为综述，其覆盖面较为充分：
  - 覆盖了超过25个VLN数据集、10余种模拟器、20多种评估指标、四大类方法（包括多个子类别）。
  - 对每个方法子类都列举了代表性论文（超过100篇参考文献），并提供了R2R排行榜的完整对比（表4）。
  - 横向比较了不同方法的性能（SR、SPL等）在相同任务上的差异，但未进行严格公平性分析（如不同设置下无法直接对比）。
  - 综述对VLN领域的历史发展、现有挑战和未来方向进行了全面梳理，实验信息足够支撑其分析框架。但受限于综述性质，无法深入验证各方法的可复现性或进行统一复现。

## 六、论文的主要结论与发现
- VLN是一个跨学科且快速发展的领域，任务定义从简单的细粒度导航延伸到复杂的人机对话、物体交互和连续环境操作。
- 当前方法面临的核心挑战包括：多模态信息对齐与理解、数据稀缺、泛化到未见环境的能力不足、模拟与现实的差距。
- 分类学框架（通信复杂度×任务目标）和四类方法（表示学习、动作策略、数据驱动、先验探索）有效总结了现有工作。
- 未来方向包括：协同多代理VLN、模拟到现实的迁移、隐私与伦理问题、跨文化/多语言环境、物体交互（最后1英里问题）。
- 当前最佳方法（如HAMT、Airbert、3DSR）在R2R测试未见环境的SR达到63~66%，但距离人类水平（SR 86%）仍有差距。

## 七、优点
1. **结构清晰**：提出的二维分类轴（通信复杂度×任务目标）系统性地组织了各种VLN任务，易于理解当前研究的全貌。
2. **覆盖面广**：详细梳理了任务定义、数据集、评估指标、方法类别和模拟器，提供了完整的引用和排行榜数据，是VLN领域的权威参考。
3. **方法分类新颖合理**：将众多方法归纳为表示学习、动作策略、数据驱动、先验探索四大类，每个子类都给出具体例子，便于读者追踪技术沿革。
4. **前瞻性讨论**：明确指出未来方向，包括协同导航、sim-to-real迁移、隐私、多文化VLN等，为后续研究提供了指导。
5. **资源开源**：提供了GitHub仓库（awesome-vision-language-navigation）持续跟踪最新进展。

## 八、不足与局限
1. **实验部分缺失原创贡献**：作为综述，未提出新方法或进行统一实验对比，因此无法验证不同方法在相同条件下的公平比较。
2. **覆盖深度有限**：对于每个具体方法，仅给出高层次描述，缺乏算法细节（如网络结构、损失函数、超参数设置），不足以支持复现。
3. **数据集汇总不完整**：未列出所有数据集的规模（如路径数量、指令数量），表格信息（表1、表2）相对简略。
4. **忽视计算资源讨论**：未探讨不同方法在计算效率、训练时间、模型大小等方面的差异，而这对实际部署很重要。
5. **评估指标分析不深入**：虽然列出了多种指标，但未讨论各指标的优缺点、相关性或局限性（如SPL对路径长度的敏感性问题）。
6. **领域发展迅速，内容可能滞后**：截至2022年3月，之后涌现的新方法（如基于大语言模型的VLN）未被包含。
7. **缺少开源代码与复现性保证**：综述本身不提供代码，对其引用的研究成果的可重复性无法保证。

（完）
