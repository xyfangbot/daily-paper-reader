---
title: "ABot-N0: Technical Report on the VLA Foundation Model for Versatile Embodied Navigation"
title_zh: ABot-N0：面向通用具身导航的VLA基础模型技术报告
authors: "AMAP CV Lab, Alibaba Group"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/004-2026_chu_abot_n0-63a070d7-a06d27aa6648.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-Language-Action (VLA) foundation model", "query:embodied navigation", "query:Grand Unification", "query:Flow Matching", "query:Agentic Navigation System"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 具身导航长期依赖任务特定架构。本文提出统一VLA基础模型ABot-N0，采用层次化“脑-动作”架构，结合LLM认知脑与流匹配动作专家，在16.9M轨迹和5.0M推理样本上训练。该模型在7个基准上取得新SOTA，并集成到具有拓扑记忆的智能体导航系统中，实现动态真实环境中的长程任务。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1708, \"height\": 656, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1702, \"height\": 857, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1703, \"height\": 1110, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1256, \"height\": 1000, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1610, \"height\": 1046, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1721, \"height\": 760, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 967, \"height\": 869, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 676, \"height\": 835, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1716, \"height\": 1005, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1708, \"height\": 1142, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1695, \"height\": 733, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 863, \"height\": 640, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1710, \"height\": 574, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1711, \"height\": 577, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1709, \"height\": 573, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1709, \"height\": 799, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1709, \"height\": 625, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1706, \"height\": 494, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1711, \"height\": 936, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1708, \"height\": 499, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1710, \"height\": 1365, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1493, \"height\": 381, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1309, \"height\": 385, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1731, \"height\": 1184, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1728, \"height\": 602, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1627, \"height\": 316, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-004-a06d27aa6648-abot-n0-technical-report-on-the-vla-foundation-model-for-versatile-embodied-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1704, \"height\": 550, \"label\": \"Table\"}]"
motivation: 解决具身导航任务碎片化问题，实现多种导航任务的统一。
method: 提出ABot-N0，采用层次化“脑-动作”架构，LLM作语义推理，流匹配生成连续轨迹。
result: 在7个导航基准上取得新SOTA，超越专用模型。
conclusion: 统一的VLA模型结合拓扑记忆与规划器，实现鲁棒真实环境长程导航。
---

## 摘要
具身导航长期以来被特定任务的架构所割裂。我们提出ABot-N0，一个统一的视觉-语言-动作（VLA）基础模型，在5个核心任务上实现了“大统一”：点目标、物体目标、指令跟随、兴趣点目标和人物跟随。ABot-N0采用层次化的“大脑-动作”架构，将基于LLM的认知大脑用于语义推理，与基于流匹配的动作专家相结合，实现精确、连续的轨迹生成。为了支持大规模学习，我们开发了ABot-N0数据引擎，在7802个高保真3D场景（10.7平方公里）中收集了1690万条专家轨迹和500万个推理样本。ABot-N0在7个基准测试中取得了新的最先进性能，显著优于专门模型。此外，我们的智能导航系统集成了具有层次拓扑记忆的规划器，能够在动态真实环境中实现稳健的长时程任务。

## Abstract
Embodied navigation has long been fragmented by task-specific architectures. We introduce ABot-N0, a unified Vision-Language-Action (VLA) foundation model that achieves a "Grand Unification" across 5 core tasks: Point-Goal, Object-Goal, Instruction-Following, POI-Goal, and Person-Following. ABot-N0 utilizes a hierarchical "Brain-Action" architecture, pairing an LLM-based Cognitive Brain for semantic reasoning with a Flow Matching-based Action Expert for precise, continuous trajectory generation. To support large-scale learning, we developed the ABot-N0 Data Engine, curating 16.9M expert trajectories and 5.0M reasoning samples across 7,802 high-fidelity 3D scenes (10.7 km2). ABot-N0 achieves new SOTA performance across 7 benchmarks, significantly outperforming specialized models. Furthermore, our Agentic Navigation System integrates a planner with hierarchical topological memory, enabling robust, long-horizon missions in dynamic real-world environments.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **现存问题**：具身导航研究长期被任务特定的独立架构所割裂。现有方法为点目标、物体目标、指令跟随等不同任务分别设计孤立模型，导致跨任务泛化能力受限，无法利用大规模异构数据提取统一的物理先验。
- **核心目标**：提出一个统一的视觉-语言-动作（VLA）基础模型，实现多种导航任务的“大统一”，并具备在真实世界中部署的实用能力。
- **整体含义**：该工作试图打破任务碎片化的范式，通过层次化“大脑-动作”架构和大规模数据引擎，让一个模型同时胜任点目标导航、物体目标导航、指令跟随导航、兴趣点（POI）导航和人物跟随导航五个核心任务，并进一步集成到智能体导航系统中完成长时程复杂任务。

## 二、论文提出的方法论
- **核心思想**：采用层次化“大脑-动作”设计哲学，将高层的语义推理与低层的连续运动控制解耦，通过共享的视觉-语言编码器统一处理异构输入，再分别用LLM进行认知推理、用流匹配生成精确轨迹。
- **三大支柱架构**：
  - **通用多模态编码器**：灵活视觉接口（支持全景/前视模式，含显式视觉历史记忆）+ 异构导航目标编码器（文本目标直接嵌入，点目标坐标经MLP投影）+ 推理任务编码器（注入任务描述激活相关推理回路）。
  - **认知大脑**：基于预训练LLM（Qwen3-4B），采用“任务条件式”设计，推理头和动作头并行而非严格串行。训练时监督显式推理任务（如可穿越性分析、社会规范理解），导航时利用物理化上下文直接条件化动作专家。
  - **动作专家**：采用流匹配（Flow Matching）预测局部BEV坐标系下的5个连续航点（含位置和偏航角）。流匹配的优势在于：连续精度支持平滑控制，能建模多模态分布（如左/右绕障）避免回归平均加剧碰撞风险。
- **数据引擎**：
  - **高保真3D场景生态系统**：7802个场景（室内6.25 km² + 室外4.42 km²），含住宅（HM3D、InteriorGS）、公共室内（办公室、商场、车站）、室外真实扫描（路口、公园）和动态虚拟城市（SocCity）。每个场景手动标注可通行导航图。
  - **轨迹数据集**：约1690万条专家轨迹，涵盖五项任务：
    - 点目标：400万条，来自互联网视频伪轨迹（π3+MoGe重建）、3D场景最优路径、真实机器人演示（SCAND、HuRoN、Recon、CityWalker）。
    - 指令跟随：150万条（VLN-CE R2R/RxR + 门穿越 + 语言引导人物搜索 + 短距原子动作）。
    - 物体目标：180万条（HM3D-OVON + InteriorGS，含OVON短距子集）。
    - POI目标：250万条（基于BridgeNav视频生成）。
    - 人物跟随：400万条（基于TrackVLA方法生成三距离三挑战类别）。
  - **推理数据集**：500万个样本，用于激活认知能力，包括可穿越区域分析（120万）、社会导航CoT（80万）、指令跟随推理（130万）、物体目标推理（10万）、POI定位（50万）、通用VQA（110万，来自Blip3、COCO、RefCOCO、ScanQA等）。
- **训练策略**（三阶段课程学习）：
  - **阶段1：认知预热**：冻结视觉编码器和动作专家，仅用推理数据集微调LLM，学习“看”和“推理”。
  - **阶段2：统一传感器运动SFT**：联合优化LLM（NTP损失）和动作专家（条件流匹配损失），轨迹数据和推理数据混合（约4:1比例）。
  - **阶段3：后训练价值对齐（SAFE-GRPO）**：冻结大脑，仅微调动作专家，在SocCity环境中用复合奖励函数（社会合规+专家相似度+平滑度+效率）强化社会规范遵守。

## 三、实验设计
- **数据集/场景与基准**：
  - 点目标：CityWalker基准（开放环MAOE指标）和SocNav基准（闭环SR、RC、SPL、社会合规DCR/TCR）。
  - 指令跟随：VLN-CE（R2R-CE和RxR-CE）Val-Unseen划分，指标NE、SR、SPL。
  - 物体目标：HM3D-OVON，三个验证集（Val-Seen、Val-Seen-Synonyms、Val-Unseen），指标SR、SPL。
  - POI目标：BridgeNav数据集，三个距离阈值下SR（0.1m/0.2m/0.3m）和轨迹偏差。
  - 人物跟随：EVT-Bench，三个难度（STT、DT、AT），指标SR、TR、CR。
- **对比方法**：
  - 点目标：GNM、ViNT、NoMaD、CityWalker。
  - 指令跟随：HPN+DN、CMA、Sim2Sim、GridMM、DreamWalker、Reborn、ETPNav、HNR、AG-CMTP、InstructNav、LAW、CM2、WS-MGMap、AO-Planner、Seq2Seq、CMA、NaVid、Uni-NaVid、NaVILA、StreamVLN、InternVLA-N1、NavFoM等。
  - 物体目标：BC、DAgger、RL、DAgRL、BCRL、VLFM、DAgRL+OD、Uni-NaVid、MTU3D、NavFoM。
  - POI目标：NoMaD、Citywalker、OmniNav。
  - 人物跟随：IBVS、PoliFormer、EVT、Uni-NaVid、TrackVLA、NavFoM、TrackVLA++。
- **评估设置**：均在未见过的场景/分布上进行闭卷或开卷评测，指标标准。

## 四、资源与算力
- **训练算力**：论文原文**未明确说明**用于训练的具体GPU型号、数量及训练时长。仅在部署部分提及：边缘端使用NVIDIA Jetson Orin NX（157 TOPS，16GB RAM），云服务器使用NVIDIA RTX 4090。
- **数据生成成本**：构建7802个3D场景、1690万条轨迹和500万推理样本需要大量算力，但具体细节缺失。
- **部署算力**：VLA模型在Orin NX上实现2Hz推理，神经控制器10Hz闭环控制，模型通过轻量视觉编码器（SigLIP-B/16）和token压缩实现。

## 五、实验数量与充分性
- **实验数量**：论文在5个任务共7个基准上进行了全面评测（点目标2个、指令跟随2个、物体目标1个、POI目标1个、人物跟随1个），每个基准都有多个对比方法。此外，在真实世界中进行了定性部署展示（多个场景可视化）。
- **充分性评估**：
  - **覆盖范围**：覆盖了五种核心导航范式，且每个任务都使用标准公开基准，实验设计较为全面。
  - **缺失项**：**没有进行任何消融实验**。论文未量化分析架构（如是否去掉流匹配、去掉推理数据、去掉SAFE-GRPO等）的贡献。也未分析不同数据来源（互联网视频 vs 3D场景 vs 真实机器人）的影响。这些缺失限制了结论的因果解释力。
  - **公平性**：对比方法均为各任务SOTA或主流模型，但部分方法使用了额外传感器（如深度、里程计），ABot-N0在多数任务中仅用RGB，对比时已注明观测配置，基本公平。
  - **统计充分性**：未报告多次运行的标准差或置信区间，无法判断结果稳定性。

## 六、论文的主要结论与发现
- **统一架构有效**：ABot-N0在全部7个基准上均取得新SOTA，超越专门模型，验证了“大统一”设计的可行性。
- **数据规模是关键**：1690万轨迹+500万推理样本的大规模数据引擎是泛化能力的基础。
- **层次化“大脑-动作”设计有效**：LLM推理与流匹配动作专家的结合，提升了语义理解与连续控制的协同。
- **价值对齐提升社会合规**：SAFE-GRPO显著提高了社会合规指标（DCR 85.1% vs 基线36.1%），使模型学会遵守社会规范。
- **真实部署可行性**：在Unitree Go2机器人上成功部署，实现长时程室内外混合任务（如“去奶茶店买饮料并占座”），展现了Agentic框架（规划器+拓扑记忆+自我反射）的实用性。

## 七、优点
- **任务统一性**：首次在一个架构内统一五个差异巨大的导航任务，避免了模型碎片化。
- **数据引擎规模与多样性**：构建了行业最大的导航数据集，涵盖室内外、静态动态、合成与真实数据，支撑了模型的鲁棒泛化。
- **技术组合创新**：将流匹配用于轨迹生成（而非传统回归）、结合SAFE-GRPO进行社会对齐、以及Agentic框架引入自我反射和重规划，均有实际价值。
- **工程落地完整**：从数据构建、训练策略到硬件部署的完整链路，体现了较强的工程能力。
- **真实部署验证**：不仅仅是仿真实验，还通过真实机器人演示了复杂长程任务，增强了可信度。

## 八、不足与局限
- **缺乏消融实验**：没有量化各个组件（如流匹配 vs 回归、推理数据、SAFE-GRPO、多任务联合训练等）的贡献，难以评估哪些设计最为关键。
- **训练细节不透明**：未报告训练GPU型号、数量、时长、超参数等，限制了可复现性和资源需求评估。
- **数据质量依赖自动生成**：大量数据由自动管道生成（如视频伪轨迹、VLM生成推理样本），可能存在噪声或偏差，但未进行系统性的质量审核分析。
- **社会合规基准局限**：社会合规评估仅在SocCity仿真环境中进行，真实世界的复杂社会交互（如非结构化的行人行为）未被充分测试。
- **人物跟随碰撞率较高**：在性能提升的同时，人物跟随任务中碰撞率（CR）相比TrackVLA有所增加（如STT: 8.54% vs 1.65%），可能存在安全折中。
- **部署硬件门槛高**：需要云端规划器+边缘端Orin NX，实时性依赖视觉token压缩（损失3%性能），在更廉价硬件上部署可能困难。
- **长期记忆更新机制未评测**：拓扑记忆动态维护机制已提出，但未提供定量指标（如更新成功率、错误恢复率等）来衡量其有效性。

（完）
