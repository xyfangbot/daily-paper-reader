---
title: "OmniNav: A Unified Framework for Prospective Exploration and Visual-Language Navigation"
title_zh: OmniNav：面向前瞻探索与视觉语言导航的统一框架
authors: "Xinda Xue, Junjun Hu, Minghua Luo, Shichao Xie, Jintao Chen, Zixun Xie, Kuichen Quan, Wei Guo, Mu Xu, Zedong Chu"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2509.25687v3"
arxiv_id: 2509.25687v3
arxiv_url: "https://arxiv.org/abs/2509.25687v3"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/001-2025_xue_omninav-3d190d98-f64824a47bbf.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2509.25687v3", "query:Embodied Navigation", "query:Visual-Language Navigation", "query:Fast-Slow System", "query:Waypoint Prediction", "query:Frontier-based Exploration"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有导航模型难以统一处理多种范式，成功率低且泛化有限。OmniNav提出统一框架，采用轻量级策略预测连续空间航点，并设计快慢系统实现高效规划。通过联合多任务训练提升指令和物体理解，显著提升成功率与鲁棒性。在多个基准和真实场景中达到最先进性能，为通用具身智能提供可扩展路径。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-001-f64824a47bbf-omninav-a-unified-framework-for-prospective-exploration-and-visual-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1678, \"height\": 877, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-001-f64824a47bbf-omninav-a-unified-framework-for-prospective-exploration-and-visual-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1650, \"height\": 856, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-001-f64824a47bbf-omninav-a-unified-framework-for-prospective-exploration-and-visual-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1701, \"height\": 1040, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-001-f64824a47bbf-omninav-a-unified-framework-for-prospective-exploration-and-visual-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1679, \"height\": 1244, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-001-f64824a47bbf-omninav-a-unified-framework-for-prospective-exploration-and-visual-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1715, \"height\": 1083, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-001-f64824a47bbf-omninav-a-unified-framework-for-prospective-exploration-and-visual-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1725, \"height\": 599, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-001-f64824a47bbf-omninav-a-unified-framework-for-prospective-exploration-and-visual-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1226, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-001-f64824a47bbf-omninav-a-unified-framework-for-prospective-exploration-and-visual-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 674, \"height\": 283, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-001-f64824a47bbf-omninav-a-unified-framework-for-prospective-exploration-and-visual-language-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1460, \"height\": 326, \"label\": \"Table\"}]"
motivation: 现有导航模型无法统一解决指令目标、物体目标等异质范式，导致低成功率和弱泛化。
method: 提出OmniNav框架，包含预测连续航点的轻量策略、快慢双系统设计，并联合大规模通用数据训练。
result: 在多个导航基准上取得最先进性能，真实部署验证有效，控制频率达5Hz。
conclusion: 揭示导航瓶颈在于指令理解而非策略学习，联合多任务训练是关键，为通用机器人导航提供实用方案。
---

## 摘要
具身导航是智能机器人面临的基础挑战，要求具备理解视觉环境、遵循自然语言指令以及自主探索的能力。然而，现有模型难以在异构导航范式上提供统一解决方案，往往导致低成功率与有限的泛化能力。我们提出OmniNav，一个在单一架构内处理指令目标、物体目标、点目标导航以及基于前沿探索的统一框架。首先，我们引入了一种轻量级、低延迟的策略，能够高精度地预测连续空间路径点（坐标与朝向），在精度上优于动作分块方法，并支持高达5 Hz控制频率的实际部署。其次，在架构层面，OmniNav提出快慢系统设计：快速模块根据较短视野的视觉上下文与子任务生成路径点，而慢速模块则利用长视野观测与候选前沿进行深思熟虑的规划，以选择下一个子目标与子任务。这种协作在探索与记忆密集型场景中提高了路径效率并维持了轨迹连贯性。值得注意的是，我们发现主要瓶颈不在于导航策略学习本身，而在于对通用指令与物体的稳健理解。为了增强泛化能力，我们将大规模通用训练数据集（包括用于图像描述、指代与基础的数据集）纳入联合多任务训练机制，这大幅提升了成功率与鲁棒性。大量实验表明，该方法在多种导航基准测试中达到了最先进性能，实际部署进一步验证了该方法的有效性。OmniNav为具身导航提供了实用见解，并为通往通用、高度可泛化的机器人智能指明了一条可扩展的路径。

## Abstract
Embodied navigation is a foundational challenge for intelligent robots, demanding the ability to comprehend visual environments, follow natural language instructions, and explore autonomously. However, existing models struggle to provide a unified solution across heterogeneous navigation paradigms, often yielding low success rates and limited generalization. We present OmniNav, a unified framework that handles instruct-goal, object-goal, point-goal navigation, and frontier-based exploration within a single architecture. First, we introduce a lightweight, low-latency policy that predicts continuous-space waypoints (coordinates and orientations) with high accuracy, outperforming action-chunk methods in precision and supporting real-world deployment with control frequencies up to 5 Hz. Second, at the architectural level, OmniNav proposes a fast-slow system design: a fast module performs waypoint generation from relatively short-horizon visual context and subtasks, while a slow module conducts deliberative planning using long-horizon observations and candidate frontiers to select the next subgoal and subtask. This collaboration improves path efficiency and maintains trajectory coherence in exploration and memory-intensive settings. Notably, we find that the primary bottleneck lies not in navigation policy learning per se, but in robust understanding of general instructions and objects. To enhance generalization, we incorporate large-scale general-purpose training datasets including those used for image captioning and referring/grounding into a joint multi-task regimen, which substantially boosts success rates and robustness. Extensive experiments demonstrate state-of-the-art performance across diverse navigation benchmarks, and real-world deployment further validates the approach. OmniNav offers practical insights for embodied navigation and points to a scalable path toward versatile, highly generalizable robotic intelligence.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 具身导航是智能机器人面临的基础挑战，要求机器人能够理解视觉环境、遵循自然语言指令并自主探索，但现有模型难以在异构导航范式（指令目标、物体目标、点目标）上提供统一解决方案。
- 当前方法存在以下问题：点目标导航依赖显式坐标，实际中不常用；指令目标导航泛化能力差；物体目标导航最为实用但需要鲁棒的目标识别与高效路径规划；许多方法依赖于任务特定数据，跨任务迁移能力有限。
- 研究者发现，导航的主要瓶颈不在于策略学习本身，而在于对通用指令和开放词汇物体的稳健理解。
- 论文旨在提出一个统一的、高效的框架，能够同时支持多种导航范式，在实时性、快慢系统协作和泛化能力上取得突破。

## 二、论文提出的方法论
- **统一架构**：OmniNav在单一架构内同时支持指令目标（instruct-goal）、物体目标（object-goal）、点目标（point-goal）导航以及基于前沿的探索（frontier-based exploration）。
- **快慢双系统设计**：
  - 快速系统（Fast System）：基于VLM骨干网络和流匹配策略（flow-matching policy），输入较短期视觉上下文和子任务，并行生成5个连续空间路径点（坐标与朝向），控制频率可达5 Hz。
  - 慢速系统（Slow System）：利用长期观测和候选前沿（frontier）进行深思熟虑的规划，通过VLM的链式思维（CoT）推理，选择下一个子目标和子任务；维护3D占据地图和记忆库，进行语义与空间推理。
  - 两者通过中央记忆模块（KV cache）耦合，提供必要的时空上下文，实现局部敏捷与全局一致的决策。
- **多模态输入分词化**：将文本、坐标和视觉历史转化为统一的大语言模型可消费的离散tokens；坐标通过MLP处理为密集嵌入。
- **路径点预测**：采用条件流匹配策略，训练去噪Transformer（DiT）对路径点序列建模，输出包括2D位置、朝向（正弦-余弦编码）和完成标志，通过欧拉积分生成路径点。
- **联合训练**：采用两阶段训练。第一阶段用自回归目标预测离散变量（动作块、通用语义数据等）；第二阶段附加流匹配策略预测连续路径点，并保留20%第一阶段离散数据以防止基础VLM能力退化。
- **通用数据增强**：引入大规模通用训练数据（图像描述、指代/接地数据等），提升指令理解和开放词汇物体感知能力。

## 三、实验设计
- **评估指标**：成功率（SR）、oracle成功率（OS）、路径长度加权成功率（SPL）、导航误差（NE）。
- **数据集与基准**：
  - 指令目标：R2R-CE（Val-Unseen）和RxR-CE（Val-Unseen）基准，使用Matterport3D场景。
  - 物体目标：HM3D-OVON基准（Val-Seen、Val-Seen-Synonyms、Val-Unseen）。
  - 点目标：CityWalker基准（开放集评估，MAOE指标）。
- **对比方法**：
  - 指令目标：与HPN+DN、CMA、Sim2Sim、GridMM、DreamWalker、Reborn、ETPNav、HNR、Uni-NaVid、NaVILA、StreamVLN、CorrectNav等14种以上方法对比。
  - 物体目标：与BC、DAgger、RL、DAgRL、BCRL、VLFM、DAgRL+OD、Uni-NaVid*、MTU3D*等方法对比。
  - 点目标：与CityWalker方法对比。
- **消融实验**：
  - 对快速系统中的动作块vs连续路径点生成进行对比。
  - 对慢系统（有无前沿和长期记忆）进行消融。
  - 对通用数据和CoT进行消融。
  - 对训练数据各组件（Embodied Q&A、Grounding/Referring、General MLLM）单独消融。
  - 对模型规模（3B vs 7B）进行消融。
- **真实世界部署**：在四足机器人上部署快速系统，验证零样本导航性能。

## 四、资源与算力
- 第一阶段训练：使用96块NVIDIA H20 GPU，训练120小时。
- 第二阶段训练：使用64块NVIDIA H20 GPU，训练48小时（较低学习率）。
- 实践中的部署：快速系统（VLM + 策略头）部署在云服务器（RTX 3090 GPU），历史缓冲区最多20帧，当前输入为三视图（480×426），运行频率超过5 Hz。

## 五、实验数量与充分性
- 论文在三个主要基准（R2R-CE、RxR-CE、HM3D-OVON）和一个点目标基准（CityWalker）上进行了系统性评估，覆盖4种导航任务。
- 消融实验覆盖了策略头、慢系统、通用数据、CoT、训练数据组件、模型规模等关键因素，共约10组以上消融实验（主消融表3、附录表4、表5）。
- 实验设计较为充分：在标准基准和公共数据集上公平对比了多种现有方法，并设置了多个验证集（Val-Seen、Val-Unseen、Synonyms）来测试泛化能力。
- 真实世界部署提供了定性验证，但无法像模拟器那样进行定量对比。
- 总体而言，实验较为充分、客观，覆盖了主要变体和关键因素；但缺乏在更多真实场景（如室外、动态环境）的定量评估，以及慢系统完整部署的消融分析。

## 六、论文的主要结论与发现
- OmniNav在多个导航基准上取得了最先进性能：R2R-CE Val-Unseen上SR达69.5%（提升4.4%），RxR-CE Val-Unseen上SR达73.6%（提升4.3%）；HM3D-OVON Val-Unseen上SR达59.2%（超越最强方法18.4%）；CityWalker点目标MAOE指标优于基准。
- 关键发现：导航策略学习本身并非主要瓶颈，对通用指令和开放词汇物体的理解才是关键；联合多任务通用数据训练显著提升成功率和鲁棒性。
- 连续路径点预测优于离散动作分块，流匹配策略实现了高精度和低延迟。
- 快慢双系统协作在长视野探索任务中提升路径效率，避免局部循环，减少冗余探索。
- 链式思维推理提供了可解释性和自我纠正能力，在复杂语义任务中稳定提升性能。
- 模型在3B与7B规模上，在包含通用数据后性能接近，说明数据充足时模型大小不是主要瓶颈。

## 七、优点
- **统一性**：单一框架同时处理四种异构导航范式，无需任务特定定制，有良好的跨任务迁移潜力。
- **创新架构**：快慢双系统设计结合前沿探索与连续路径点预测，兼顾实时性与长程规划，符合“系统1-系统2”认知理论。
- **高效策略**：流匹配策略避免了离散动作的精度降低和延迟累积，支持5 Hz实时闭环控制，且可生成平滑轨迹。
- **数据策略**：系统性地引入通用视觉-语言数据（图像描述、指代/接地）进行联合训练，显著提升泛化能力，具有可推广性。
- **推理可解释**：慢系统采用显式链式思维推理，使子目标选择过程透明，支持自我纠正。
- **实际部署验证**：在真实机器人上展示了零样本导航能力，验证了工程可行性。

## 八、不足与局限
- **实验范围局限**：主要在模拟器（Habitat、Matterport3D、HM3D）中进行定量评估，真实世界部署仅对快速系统进行定性验证，缺乏真实场景的定量对比和慢系统完整部署分析。
- **资源需求高**：训练阶段需要大量GPU（96+64块H20），对计算资源需求较高，可能限制可复现性。
- **对深度/里程计依赖**：慢系统需要深度和里程计信息构建占据地图，限制了仅用RGB的纯视觉场景应用。
- **附录消融显示不足**：虽进行消融，但未提供更多真实场景（如动态障碍物、室外环境）的实验，长期部署下的鲁棒性未充分验证。
- **模型规模的消融不充分**：仅比较3B和7B，未探索更大模型（如13B、72B）的规律，也未系统研究数据质量与组合的影响。
- **应用限制**：论文承认对“衣服”、“地毯”等纹理复杂物体的识别仍不稳定；慢系统完整部署需要额外工程整合（如与LiDAR/深度估计实时集成），尚未解决实际系统中延迟和频率权衡问题。

（完）
