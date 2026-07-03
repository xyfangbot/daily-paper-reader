---
title: "Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models"
title_zh: Qwen-RobotManip技术报告：对齐解锁机器人操作基础模型的规模
authors: "Haoqi Yuan, Zhixuan Liang, Anzhe Chen, Ye Wang, Haoyang Li, Pei Lin, Yiyang Huang, Zixing Lei, T Zhang, Jiazhao Zhang, Jie Zhang, Jiahao Fan, Gengze Zhou, Qihang Peng, Chenxu Lv, Xiaoyue Chen, An Yang, Fei Huang, J X C Lin, D Liu"
date: 2026-06-16
pdf: "https://arxiv.org/pdf/2606.17846"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:alibaba group"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=alibaba group; relation_source=branded-title; query=Qwen-RobotManip"
tldr: "机器人操作基础模型如何实现规模化泛化是核心难题，数据异构、昂贵且多样性窄。Qwen-RobotManip创新性地引入统一对齐框架，在表示、运动和动作三个维度对齐多源数据，并利用人类到手演示合成多种机器人平台的轨迹，构建约38,100小时预训练语料。该模型展现出零样本指令跟随、对扰动的鲁棒性、主动错误恢复以及跨本体迁移等涌现泛化能力。在RoboCasa365等OOD基准上全面超越π0.5等SOTA，RoboChallenge夺冠且相对提升20%，在多种真实机器人平台已验证。"
source: openalex
selection_source: hot_paper_scout
motivation: 机器人操作数据异构、昂贵且多样性窄，使得对齐和规模化难以兼得，缺乏真正泛化的基础模型。
method: Qwen-RobotManip提出统一对齐框架对齐表示、运动和动作维度的多源数据，并通过人类演示合成轨迹构建大规模预训练语料。
result: "在RoboCasa365等OOD基准上全面超越π0.5，RoboChallenge夺冠且相对提升20%，在多种真实机器人平台验证零样本泛化。"
conclusion: 通过统一对齐框架实现大规模异构数据训练，证明对齐是解锁机器人操作基础模型涌现泛化能力的关键。
---

## 摘要
语言和多模态基础模型通过统一公式对齐异构数据并进行大规模训练，实现了强大的泛化能力。在本报告中，我们探究这种扩展方法是否适用于机器人操作任务以实现真正的泛化。这具有挑战性，因为与文本不同，操作数据本质上是异构的，收集成本高昂且多样性狭窄，使得对齐和规模化同时变得困难。我们提出了Qwen-RobotManip，一个基于Qwen-VL构建的可泛化视觉-语言-动作基础模型。Qwen-RobotManip引入了一个统一的跨表示、运动和操作行为维度的对齐框架，使大规模多源训练变得协调一致而非相互冲突。这种对齐能力进而使Qwen-RobotManip能够吸收先前训练机制无法维持规模的操作数据。一个人到机器人的合成流程将15个平台上的自我中心手部演示转换为机器人轨迹，一个严格的策展流程则协调了异构数据集。仅使用开源数据集和人类视频，无需专有数据收集，Qwen-RobotManip构建了约38,100小时的预训练语料库，并展现出新兴的泛化能力，包括零样本指令跟随、对扰动的鲁棒性、反应性错误恢复以及跨实体迁移。我们发现标准基准无法捕捉预训练质量，因此采用包括RoboCasa365、LIBERO-Plus、EBench、RoboTwin-Clean2Rand、RoboTwin-IF和RoboTwin-XE在内的分布外（OOD）设置。Qwen-RobotManip在所有OOD设置上显著优于先前的最先进模型（包括π0.5），在RoboChallenge中排名第一，相对提升20%，并在包括AgileX ALOHA、Franka、UR和ARX在内的真实机器人平台上得到验证。

## Abstract
Foundation models in language and multimodality achieve strong generalization by aligning heterogeneous data under a unified formulation and training at scale. In this report, we investigate whether this scaling recipe can be applied to robotic manipulation to achieve genuine generalization. This is challenging because, unlike text, manipulation data is heterogeneous by nature, expensive to collect, and narrow in diversity, making alignment and scale simultaneously difficult. We present Qwen-RobotManip, a generalizable Vision-Language-Action foundation model built on Qwen-VL. Qwen-RobotManip introduces a unified alignment framework across the representation, motion, and behavioral dimensions of manipulation, making large-scale multi-source training coherent rather than conflicting. This alignment capability in turn enables Qwen-RobotManip to absorb manipulation data at a scale that prior training regimes could not sustain. A human-to-robot synthesis pipeline converts egocentric hand demonstrations into robot trajectories across 15 platforms, and a rigorous curation pipeline harmonizes heterogeneous datasets. Using only open-source datasets and human videos without proprietary data collection, Qwen-RobotManip constructs a ~38,100-hour pretraining corpus and exhibits emergent generalization capabilities, including zero-shot instruction following, robustness to perturbations, reactive error recovery, and cross-embodiment transfer. We find that standard benchmarks fail to capture pretraining quality and instead adopt OOD settings including RoboCasa365, LIBERO-Plus, EBench, RoboTwin-Clean2Rand, RoboTwin-IF, and RoboTwin-XE. Qwen-RobotManip substantially outperforms prior state-of-the-art models, including $π$0.5, across all OOD settings, ranks 1st in RoboChallenge with a 20% relative improvement, and is validated on real-robot platforms including AgileX ALOHA, Franka, UR, and ARX.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：语言和多模态基础模型通过统一公式对齐异构数据并大规模训练实现了强大泛化，但机器人操作数据本质异构、收集成本高、多样性狭窄，使得对齐和规模化难以同时实现，导致缺乏真正泛化的操作基础模型。
- **整体含义**：探索将上述缩放（scaling）方法应用于机器人操作以达成真正泛化。作者认为对齐是解锁大规模训练和涌现泛化能力的关键，并通过提出Qwen-RobotManip验证了这一假设。

## 二、论文提出的方法论
- **核心思想**：提出一个统一的跨表示（representation）、运动（motion）和行为（behavioral）维度的对齐框架，使大规模多源操作数据训练协调一致，而非相互冲突。
- **关键技术细节**：
  - 基于Qwen-VL构建视觉-语言-动作（Vision-Language-Action）基础模型。
  - 人-机合成流程：将15个机器人平台上的自我中心手部演示（egocentric hand demonstrations）转换为机器人轨迹。
  - 严格策展流程：协调异构数据集（开源自数据+人类视频），构建约38,100小时的预训练语料库。
  - 仅使用开源数据集和人类视频，无需专有数据收集。
- **算法流程（文字描述）**：
  1. 收集多源异构数据（包括真实机器人数据、人类演示视频等）。
  2. 通过统一对齐框架在表示、运动、行为三个维度将数据对齐为统一格式。
  3. 利用合成流程将人类到手演示转为机器人平台可执行的轨迹。
  4. 对衍生轨迹进行严格策展，确保质量与一致性。
  5. 使用上述混合语料对Qwen-VL进行预训练，得到Qwen-RobotManip模型。
  6. 在推理时，输入视觉观测和语言指令，直接输出机器人动作序列。

## 三、实验设计
- **数据集/场景**：使用开源的机器人操作数据集和人类视频数据构建预训练语料（~38,100小时）。评估采用分布外（OOD）设置，包括RoboCasa365、LIBERO-Plus、EBench、RoboTwin-Clean2Rand、RoboTwin-IF、RoboTwin-XE。
- **基准（Benchmark）**：除了上述OOD基准，还在RoboChallenge综合排行榜上测试。
- **对比方法**：包括π0.5等先前最先进模型（SOTA）。
- **真实机器人验证平台**：AgileX ALOHA、Franka、UR、ARX。
- **主要结果**：在所有OOD设置上全面超越π0.5等SOTA；在RoboChallenge中排名第一，相对提升20%。

## 四、资源与算力
- 文中**未明确说明**使用的GPU型号、数量、训练时长等具体算力信息。仅提及使用了开源数据集和人类视频，未进行专有数据收集。

## 五、实验数量与充分性
- **实验数量**：作者在多个OOD基准（至少6个）和4个真实机器人平台上进行了评估，并在RoboChallenge竞赛中验证。但摘要中未提及消融实验或详细分组实验。
- **充分性与公平性**：
  - 覆盖了合成数据、仿真环境、真实机器人多种场景，实验范围较广。
  - 对比了当前最强的基线（π0.5），对比设置相对公平。
  - 提出标准基准无法捕捉预训练质量，因此采用更具挑战性的OOD设置，实验设计具有一定合理性。
  - 不足：未提供消融研究（如对齐框架各维度的贡献、不同数据量的影响等），实验的完整性有待增强。

## 六、论文的主要结论与发现
- **主要结论**：统一对齐框架是实现大规模异构数据训练并涌现泛化能力的关键。通过跨表示、运动、行为三个维度的对齐，Qwen-RobotManip能够吸收此前训练机制无法维持规模的操作数据。
- **发现**：模型展现出零样本指令跟随、对扰动具有鲁棒性、主动错误恢复、跨本体迁移等涌现泛化能力。在多个OOD基准上显著超越SOTA，并在真实机器人上验证了零样本泛化。

## 七、优点
- **方法亮点**：
  1. 提出统一对齐框架，有效协调异构、多源的操作数据。
  2. 利用人类到手演示合成机器人轨迹（人-机合成流程），大幅降低数据采集成本，无需专有数据。
  3. 仅使用开源数据即构建了约38,100小时的大规模预训练语料，具有可复现性。
- **实验亮点**：
  4. 采用OOD设置评估，更能反映模型真实泛化能力。
  5. 在仿真和多种真实机器人上验证，全面且具有说服力。
  6. 击败了π0.5等强基线，在RoboChallenge夺冠，性能提升明显。

## 八、不足与局限
- **实验覆盖**：
  - 未提供消融实验，难以量化对齐框架各组件或不同数据量对性能的影响。
  - 未报告在常见标准基准（如RLBench、CALVIN等）上的结果，仅强调OOD设置，可能缺乏与更广泛社区工作的直接对比。
- **偏差风险**：
  - 人-机合成数据可能引入人类演示的偏差，未必完全适配所有机器人平台（尽管文中提到跨本体迁移）。
  - 仅基于Qwen-VL构建，模型能力受限于基座模型，且未与其他架构（如扩散策略）的比较。
- **应用限制**：
  - 文中未提及在杂乱或高度动态环境下的表现。
  - 算力消耗未公开，不利于其他团队复现或评估资源需求。
  - 对未见过的极端物体或任务泛化能力未知。

（完）
