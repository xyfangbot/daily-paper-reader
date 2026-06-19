---
title: Vision-and-Dialog Navigation
title_zh: 视觉与对话导航
authors: "Jesse Thomason, Michael Murray, Maya Cakmak, Luke Zettlemoyer"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/001-2019_thomason_cvdn-b71b2b2b-60a40f2493ba.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Dialog Navigation", "query:Cooperative Vision-and-Dialog Navigation", "query:Navigation from Dialog History", "query:Human-Robot Interaction", "query:Embodied Navigation"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 针对机器人在人类环境中导航时需用语言求助并理解回应的问题，构建了Cooperative Vision-and-Dialog Navigation数据集，包含2000多个在模拟真实家庭环境中的具身人机对话。任务中Navigator提问，Oracle提供最短路径规划器建议。提出Navigation from Dialog History任务，要求根据目标对象和对话历史推断导航动作。设计多模态序列到序列模型，实验表明利用更长对话历史可显著提升导航性能，为具身导航语言理解提供重要基准。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-001-60a40f2493ba-vision-and-dialog-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1445, \"height\": 654, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-001-60a40f2493ba-vision-and-dialog-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1396, \"height\": 287, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-001-60a40f2493ba-vision-and-dialog-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1441, \"height\": 325, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-001-60a40f2493ba-vision-and-dialog-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1295, \"height\": 928, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-001-60a40f2493ba-vision-and-dialog-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1346, \"height\": 435, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-001-60a40f2493ba-vision-and-dialog-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1352, \"height\": 423, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-001-60a40f2493ba-vision-and-dialog-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1439, \"height\": 491, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-001-60a40f2493ba-vision-and-dialog-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1433, \"height\": 798, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-001-60a40f2493ba-vision-and-dialog-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1228, \"height\": 1207, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-001-60a40f2493ba-vision-and-dialog-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1261, \"height\": 385, \"label\": \"Table\"}]"
motivation: 现有导航代理缺乏利用语言对话获取动态环境信息的能力，需要引入人机协作的对话式导航任务。
method: 构建Cooperative Vision-and-Dialog Navigation数据集，定义从对话历史中推理导航动作的序列到序列模型，融合视觉与文本模态。
result: 多模态序列到序列模型在数据集上实现有效导航，利用更长对话历史可提升目标定位准确率。
conclusion: 该工作验证了对话历史对导航决策的重要性，为未来人机协作导航研究提供了数据与基线模型。
---

## 摘要
在人类环境中导航的机器人应使用语言寻求帮助，并能够理解人类的回应。为研究这一挑战，我们引入了协作式视觉与对话导航数据集，该数据集包含超过2000个在模拟的逼真家居环境中进行的具身人人对话。导航者向他们的搭档——先知提问，后者根据最短路径规划器拥有关于导航者应采取的最佳下一步行动的特权信息。为训练在环境中搜索目标位置的智能体，我们定义了基于对话历史的导航任务。给定一个目标对象以及人类协作寻找该对象时的对话历史，智能体必须在未探索的环境中推断出通往目标的导航动作。我们建立了一个初始的多模态序列到序列模型，并证明在对话历史中回溯更远有助于提升性能。

## Abstract
Robots navigating in human environments should use language to ask for assistance and be able to understand human responses. To study this challenge, we introduce Cooperative Vision-and-Dialog Navigation, a dataset of over 2k embodied, human-human dialogs situated in simulated, photorealistic home environments. The Navigator asks questions to their partner, the Oracle, who has privileged access to the best next steps the Navigator should take according to a shortest path planner. To train agents that search an environment for a goal location, we define the Navigation from Dialog History task. An agent, given a target object and a dialog history between humans cooperating to find that object, must infer navigation actions towards the goal in unexplored environments. We establish an initial, multi-modal sequence-to-sequence model and demonstrate that looking farther back in the dialog history improves performance.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 研究动机：机器人在人类环境中导航时，需要具备使用自然语言寻求帮助并理解人类回应的能力。现有的导航任务大多依赖单一指令，缺乏动态对话交互，无法处理模糊、未完全指定的导航指令。
- 整体含义：构建一个包含人-人对话的协作式导航任务，为训练能够通过对话获取环境信息的导航智能体提供数据基础，推动具身对话导航研究。

## 二、论文提出的方法论
- 核心思想：引入 **Cooperative Vision-and-Dialog Navigation (CVDN)** 数据集，包含2050个在真实模拟家居环境中的人-人导航对话；并定义 **Navigation from Dialog History (NDH)** 任务——给定目标对象和对话历史，智能体需在未探索环境中推断导航动作以接近目标。
- 关键技术细节：
    - 对话收集：两名人类（Navigator 和 Oracle）协作，Navigator 可移动和提问，Oracle 能看到最短路径规划器的下一步建议并回答。
    - 数据集结构：每个对话由导航动作、提问、回答交替组成（N0, Q1, A1, N1, …, Qk, Ak, Nk），从中提取 NDH 实例（共7415个）。
    - 监督信号：提供三种路径监督——Oracle 最短路径 Oi、Navigator 人类路径 Ni、混合路径 Mi（当人类路径覆盖了 Oracle 路径终点时用 Ni，否则用 Oi）。
- 模型架构：使用序列到序列（Seq2Seq）模型，LSTM 编码器编码对话历史（包括特殊标记<NAV>, <ORA>, <TAR>, <EOS>），LSTM 解码器以 ResNet-152 提取的视觉帧特征为输入，输出导航动作。编码器初始化解码器隐状态。

## 三、实验设计
- 数据集/场景：CVDN 数据集，基于 Matterport 模拟器中的83个房屋扫描；NDH 任务拆分为训练（4742）、seen 验证（382）、unseen 验证（907）、unseen 测试（1384）实例，按房屋扫描划分，保持 R2R 的划分方式。
- Benchmark：最短路径智能体（上界）、随机智能体（非学习基线）、单模态消融（仅视觉、仅语言、零模态）。
- 对比方法：
    - 不同对话历史输入：仅目标对象 to、仅最后回答 Ai、最后问答对 (Qi, Ai)、完整历史 (Q1:i-1, A1:i-1, Qi, Ai)。
    - 不同监督信号：Oracle 路径、Navigator 路径、混合路径。
    - 同时对比了加入导航历史编码的变体（实验中发现单纯拼接无效）。
- 评估指标：目标进展（Progress），即从路径起点到终点与目标区域距离的减少量（米），采用拓扑距离。

## 四、资源与算力
- 论文未明确说明使用的 GPU 型号、数量及训练时长。
- 训练设置：batch size 100，训练 20000 次迭代，每 100 次迭代评估一次验证集，选择最佳 epoch 用于测试。使用学生强制训练（student-forcing），与 Anderson et al. (2018) 相同的超参数（优化器、学习率、隐层大小等）。
- 数据收集成本：超过 7000 美元（每对工人 1.25 美元）。

## 五、实验数量与充分性
- 实验组数：主要实验包含 3 种监督信号 × 5 种语言输入变体（至、最后回答、最后问答、完整历史、单模态消融），以及 seen/unseen 验证和测试三个评估集，共计约 45 个主要结果表格（表3）。
- 此外还进行了：加入导航历史编码的额外实验（表4）、路径长度分布统计、对话现象注解分析（100个对话，Cohen’s κ=0.738）。
- 充分性：
    - 进行了广泛的消融实验，覆盖不同对话历史长度、不同监督信号、不同模态组合。
    - 使用了 paired t-test 和 Benjamini–Yekutieli 过程控制错误发现率，统计检验充分。
    - 但未与其他现有 VLN 方法（如注意力机制、强化学习）对比，仅提供基于 Seq2Seq 的初始基线。

## 六、论文的主要结论与发现
- 使用完整的对话历史（而非仅最后回答或最后问答对）在 unseen 测试环境下显著优于仅使用目标对象（p<0.05），验证了对话历史对导航决策的重要性。
- 混合监督（Mi）在所有环境设置中均显著优于单独使用 Oracle 或 Navigator 监督，表明结合人类探索直觉与规划器短程准确性可提升性能。
- 多模态模型显著优于单模态消融（仅视觉或仅语言），证明视觉与语言结合的必要性。
- 当前 Seq2Seq 模型在 unseen 环境下与人类表现仍有较大差距（最短路径上界约8-10米，模型约2米左右），表明存在提升空间。

## 七、优点
- 数据集创新：首个包含双向人-人对话的具身导航数据集，对话具有模糊性、欠指定性和多种复杂现象（如修复、历史引用、离题等），真实反映人机交互场景。
- 任务设计巧妙：NDH 任务从对话中提取自然切片，提供多层次监督（规划器/人类/混合），为后续强化学习等高级方法奠定基础。
- 实验严谨：进行了统计显著性检验（paired t-test + FDR控制），确保结论可靠；消融实验覆盖多个维度（对话历史、监督信号、模态）。
- 开源：代码和在线接口公开（https://cvdn.dev/），便于复现和扩展。

## 八、不足与局限
- 模拟环境局限：基于离散导航图（Matterport），与现实世界连续运动、传感器噪声、定位误差等有差距，迁移至真实机器人需额外映射和校准。
- 初始模型简单：仅使用 Seq2Seq 基线，未探索注意力机制、强化学习、跨模态对齐等先进技术，性能与人类差距较大。
- 导航历史融合失败：尝试直接拼接导航历史编码并未提升性能，说明需要更精细的跨模态对齐建模。
- 对话理解局限：模型未显式建模修复、指代消解等对话现象，仅靠 LSTM 隐式编码。
- 数据收集成本较高（7000美元），且仅覆盖83个房屋，目标物体分布不均衡（如“床”出现频率远高于其他物体）。
- 任务仅关注导航，未涉及问题提问和回答的联合训练，未来工作可扩展至双向智能体协作。

（完）
