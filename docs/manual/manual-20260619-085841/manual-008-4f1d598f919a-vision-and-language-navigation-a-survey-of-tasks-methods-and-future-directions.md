---
title: "Vision-and-Language Navigation: A Survey of Tasks, Methods, and Future Directions"
title_zh: 视觉与语言导航：任务、方法及未来方向综述
authors: "Jing Gu, Eliana Stefani, Qi Wu, Jesse Thomason, Xin Eric Wang"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/008-vln_survey2-fb619814-4f1d598f919a.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:VLN", "query:Survey", "query:Tasks", "query:Methods"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 人工智能的长期目标是构建能通过自然语言与人类交流、感知环境并执行现实任务的智能体。视觉与语言导航（VLN）作为实现这一目标的基础跨学科方向，正受到自然语言处理、计算机视觉、机器人学等领域的广泛关注。本文系统综述了VLN领域的研究进展，涵盖任务定义、评估指标与方法体系。通过结构化分析当前进展与挑战，揭示了现有方法的局限性，并指出了未来研究方向。该综述为VLN研究社区提供了全面的参考，有助于推动跨学科合作与后续研究。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-008-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 736, \"height\": 528, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-008-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 794, \"height\": 706, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-008-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1653, \"height\": 919, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-008-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1638, \"height\": 1481, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-008-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1025, \"height\": 458, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-008-4f1d598f919a-vision-and-language-navigation-a-survey-of-tasks-methods-and-future-directions/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1637, \"height\": 931, \"label\": \"Table\"}]"
motivation: 构建能与人类自然语言交流并感知环境执行任务的智能体是AI长期目标，VLN作为跨学科基础方向，亟需系统梳理任务与方法。
method: 广泛收集并分析VLN领域现有文献，从任务、评价指标、方法等维度进行结构化综述，总结进展并指出局限。
result: 揭示了VLN方法在语言理解、感知泛化与鲁棒性等方面的局限，并梳理了未来研究方向。
conclusion: 本文为VLN社区提供全面参考，促进跨领域合作，推动智能体向具身化与语言交互发展。
---

## 摘要
人工智能研究的长期目标之一是构建能够用自然语言与人类交流、感知环境并执行现实世界任务的智能体。视觉与语言导航（VLN）是实现这一目标的基础性和跨学科研究课题，日益受到自然语言处理、计算机视觉、机器人学和机器学习领域的关注。本文综述了VLN这一新兴领域中的当代研究，涵盖任务、评估指标、方法等。通过对当前进展和挑战的结构化分析，我们指出了当前VLN的局限性以及未来工作的机遇。本文旨在为VLN研究社区提供一份全面的参考资料。

## Abstract
A long-term goal of AI research is to build intelligent agents that can communicate with humans in natural language, perceive the environment, and perform real-world tasks. Vision-and-Language Navigation (VLN) is a fundamental and interdisciplinary research topic towards this goal, and receives increasing attention from natural language processing, computer vision, robotics, and machine learning communities. In this paper, we review contemporary studies in the emerging field of VLN, covering tasks, evaluation metrics, methods, etc. Through structured analysis of current progress and challenges, we highlight the limitations of current VLN and opportunities for future work. This paper serves as a thorough reference for the VLN research community.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：人工智能的长期目标是构建能够使用自然语言与人类交流、感知物理环境并执行现实世界任务（如家务、递送、危险环境作业）的智能体。视觉与语言导航（VLN）是实现这个目标的基础性跨学科研究课题，它连接了自然语言处理、计算机视觉和机器人学等多个领域。
- **核心问题**：如何让一个具身智能体（embodied agent）在真实或仿真的3D环境中，通过理解自然语言指令（或进行对话交互），感知视觉环境，并自主规划路径进行导航，最终完成任务目标。研究面临的挑战包括：多模态信息的有效理解与对齐（视觉、语言、动作）、复杂的推理与决策、训练数据稀缺（人工标注昂贵），以及模型从“已见过”环境泛化到“未见过”环境的能力不足。
- **整体含义**：本文并非提出单一新算法，而是对VLN领域进行了一次全面、系统的结构化综述，旨在梳理截至论文撰写时（2022年）的主要工作任务、评估标准、方法体系和发展脉络，为研究人员提供权威的参考，并指明待解决的关键问题和未来可拓展的方向。

## 二、论文提出的方法论
- **核心思想**：采用“结构化综述”的方法论，对VLN领域进行系统性的分类和梳理。论文从任务定义、评估方法和现有技术三个维度进行解构。
- **任务分类框架**：论文提出了一个创新的二维分类框架，从 **“通讯复杂度”**和 **“任务目标”** 两个轴对现有基准测试（benchmark）进行划分。
    - **通讯复杂度**：分三个级别：
        1.  **初始指令**：智能体在开始导航前只接收一次自然语言指令。
        2.  **Oracle 指导**：智能体在不确定时可以发送简单信号（如`[help]`）请求指导。
        3.  **人类对话**：智能体可以使用自由形式的自然语言向指导者（Oracle）提问和互动。
    - **任务目标**：分三个级别：
        1.  **细粒度导航**：指令包含详细的“分步路线描述”，智能体需严格遵循路线到达目标。
        2.  **粗粒度导航**：指令只包含模糊的目标描述（如“去厨房”），智能体需要自主推理路径，可能需要更多帮助。
        3.  **导航与物体交互**：除了导航到目标，智能体还需要与环境中的物体互动（如打开抽屉拿勺子、切苹果）。
- **方法分类体系**：论文将现有VLN方法分为四大类和若干子类：
    - **表示学习**：帮助智能体理解多模态信息之间的关系。
        - **预训练**：
            - **单模态**：使用预训练的视觉模型（如ResNet、ViT）或语言模型（如BERT、GPT）进行初始化。
            - **多模态**：使用视觉-语言预训练模型（如ViLBERT、VLN-BERT、PREVALENT）提供联合表示。
        - **语义理解**：提取或聚焦于任务相关的高层次语义特征，如室内物体、方向词、地标等，并通过注意力机制进行跨模态对齐。
        - **图表示**：构建环境地图或知识图谱，显式建模导航节点之间的关系以及视觉和语言元素的关联。
        - **记忆增强模型**：利用LSTM、Transformer或专用记忆模块存储和利用导航历史信息。
        - **辅助任务**：通过添加额外损失函数（如预测下一步动作、估算任务进度）来提高模型能力。
    - **动作策略学习**：帮助智能体在复杂环境中做出决策。
        - **强化学习**：将VLN建模为马尔可夫决策过程。论文讨论了如何设计奖励函数（如目标导向的外部奖励和遵循指令的内部奖励）来解决稀疏奖励和信用分配问题。
        - **探索中**：在导航过程中进行局部探索来收集环境信息。使用了如学生强制（Student-forcing）、回溯（Backtracking）等策略。
        - **导航规划**：预测航点、未来视觉状态或规划路径结构，例如通过预测终点或使用语言指令标记里程碑。
        - **请求帮助**：使用动作概率或专用模型来判断何时发出帮助信号或提出自然语言问题。
    - **数据为中心的学习**：解决VLN中数据稀缺和泛化问题。
        - **数据增强**：
            - **轨迹-指令增强**：训练一个“说话者”模型为现有路径生成新的指令，并用对齐筛选器提高质量。
            - **环境增强**：通过视觉特征屏蔽、场景混洗、风格变换等方式创造新的训练环境。
        - **课程学习**：按任务难度从易到难组织训练，如从短指令到长指令。
        - **多任务学习**：在相关VLN任务间共享知识以提高泛化能力。
        - **指令解释**：将长指令分解为子指令，或将指令重新解释为更易于理解的形式。
    - **先验探索**：允许智能体在测试的“未见”环境中进行预观察和适应，从而减少训练与测试环境的性能差距。这通过自监督模仿学习、环境采样适应或构建环境地图完成。
- **评估指标**：论文详述了VLN的评估指标，分为两类：
    - **面向目标的指标**：衡量智能体接近目标的程度。指标包括成功率、目标进度、路径长度、最短路径距离、加权的成功率、固定编辑距离成功率等。
    - **路径保真度指标**：衡量智能体遵循特定路径的程度。指标包括路径覆盖率与长度分数的乘积、归一化的动态时间扭曲、加权的归一化动态时间扭曲等。

## 三、实验设计
- **数据集与场景**：论文本身并非提出新实验，而是综述了VLN社区使用的核心基准测试。这些数据集在不同的通讯复杂度和任务目标组合下进行了分类。
    - **室内数据集**：最广泛使用的是基于Matterport3D模拟器的**房间到房间（R2R）** 及其变体（如Room-for-Room, Room-Across-Room, VLNCE）。
    - **室外数据集**：主要基于Google Street View，例如 **TOUCHDOWN**、StreetLearn、StreetNav。
    - **物体交互数据集**：基于AI2-THOR的 **ALFRED**、TEACh、DialFRED；基于House3D的EmbodiedQA。
    - **对话数据集**：如**CVDN**、RobotSlang。
- **基准**：论文多次引用并展示了**R2R**数据集公开排行榜（Leaderboard）上的结果对比。这是VLN领域事实上的标准评估平台。
- **对比的方法**：论文综述了从2018年至2022年初的数十种代表性方法。在R2R排行榜（附录C的表4）中，通过表格形式对比了包括Sequence-to-Sequence基线、Speaker-Follower、RCM (2019)、EnvDrop (2019)、PREVALENT (2020、VLN-BERT）、HAMT (2021) 以及CMG-AAL (2020）等方法的性能。

## 四、资源与算力
- **未明确说明**：作为一篇综述论文，本文本身不包含自己的实验运行，因此没有报告任何关于训练其自身模型所使用的具体算力资源信息，如GPU型号、数量或训练时长。
- **间接提及**：文中提到的其他研究论文通常会说明其计算资源，但本文未将这些细节纳入综述内容。例如，很多前期工作在单个或多个NVIDIA V100/RTX 2080 Ti等GPU上进行。

## 五、实验数量与充分性
- **实验数量**：本文并未进行实验，而是对**大量已有实验结果的总结分析**。它引用了众多论文中报告的实验结果，并汇集成了较大的对照表。例如，附录表4展示了超过20种方法在R2R上的多个指标（SR/SPL等）的量化对比。
- **充分性评价**：
    - **充分性（宽泛）**：作为一篇综述，其对VLN方法的梳理非常系统和全面，覆盖了该领域从任务定义、模型设计到评估方法的各个环节。从分析现有研究的角度看，其覆盖范围是充分的。
    - **局限性（缺乏统一性）**：由于是总结性的对比，不同论文的代码环境和训练设置（如不同的模拟器版本、补全策略）并不完全一致，因此排行榜上的直接数字对比并非严格公平。此外，综述的一些表格中出现了数据缺失，使对比不完美。
- **客观性与公平性**：
    - 综述对不同方法（如基于RL的、基于预训练的、数据增强的）的优点和缺陷进行了相对客观的评价，没有明显偏向某一特定流派。
    - 在R2R排行榜的对比中，明确标出了“先验探索”和“束搜索”方法，指出它们与“单次运行”方法不可直接比较，这种区处理是客观和公正的。

## 六、论文的主要结论与发现
- **VLN领域已取得巨大进步**：从初步的“跟随指令”任务（R2R）发展到了涉及对话、交互和复杂推理的多种任务。
- **任务多样性与耦合性**：VLN任务可按通讯复杂度和任务目标的组合进行划分，不同任务对智能体的能力要求不同。当前的最强方法（如HamT）通常集成了预训练、语义理解、记忆模块和强化学习等多种技术。
- **泛化仍是核心挑战**：模型在“未见”环境中的性能普遍低于“已见过”环境，表明过拟合和环境特异性是关键障碍。数据增强（EnvDrop）和先验探索等方法被证明对此有所帮助。
- **数据稀缺是瓶颈**：VLN数据集规模小且标注成本高，推动了对数据增强、课程学习和多任务学习等数据为中心策略的研究。
- **从模拟到现实（Sim-to-Real）存在巨大鸿沟**：大多数仿真使用预定义的导航图（不连续动作、假定完美定位），与现实世界的连续、动态、有噪声环境存在巨大差异。
- **未来方向明确**：论文指出了多个充满潜力的未来方向，包括协作式多智能体VLN、模拟到真实的迁移（连续动作空间、环境动态变化）、伦理与隐私保护（避免敏感数据泄露）、跨文化/语言VLN以及对物体交互的更精细研究（“拿起勺子”而非“找到勺子”）。

## 七、优点
- **全面性与系统性**：这是截至发布时点（2022年）对VLN领域最系统、最全面的综述之一。它不仅涵盖了任务、数据集和评估，还提供了一个清晰、多层级的方法分类体系（表示学习、策略学习、数据学习、先验探索），非常便于刚入门的研究者理解领域全貌。
- **分类框架的创新性**：提出的“通讯复杂度 vs. 任务目标”二维任务分类框架（表1和表2）是本文的重要贡献，直观地解释了不同VLN任务间的核心差异和内在联系，为领域提供了统一的谈讨论语言。
- **结构化分析**：论文对每个方法子类别（如强化学习中的奖励设计、视觉-语言预训练的种类）都进行了深入的结构化分析，点出了其子问题的关键挑战和解决方案思路，这比单纯罗列参考文献更有价值。
- **提供实用资源**：论文附上了持续更新的Github仓库链接，用于跟踪最新进展，并整理了详细的附录（包括所有基准的统计表格、模拟器介绍和R2R排行榜），使其成为高质量的实用参考手册。

## 八、不足与局限
- **时效性受限（截至2022年）**：作为一篇综述，其内容在撰写时为最新，但对于现在（2024年底）的读者而言，可能缺少2022年下半年至今的最新进展，如更先进的预训练模型、更复杂的连续空间导航方法等。
- **结论的非确定性**：作为综述，它没有提出一个统一的理论或新的最佳解决方案，而是归纳了多种思路。对于“哪种方法最好”这个具体问题，它给出的答案部分取决于具体的数据集和使用的子技术组合，缺乏一个最终的裁判结论。
- **实验比较的公平性**：尽管附录中的排行榜提供了量化对比，但如文中所说，“先验探索”和“束搜索”等方法与标准设置不可直接对比，这限制了排行榜的直接解读价值。同时，不同方法在超参数、奖励函数设计等方面的细微差异也可能被忽略。
- **深度受限**：由于综述覆盖面太广，它对每个具体方法的技术细节讨论较浅，没有提供具体的公式推导或模型结构图。对于更深层次的技术原理（如某个特定注意力机制如何工作），读者需要去阅读原文进一步了解。

（完）
