---
title: "Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning"
title_zh: Hydra-Nav：通过自适应双过程推理实现物体导航
authors: "Zixuan Wang, Huang Fang, Shaoan Wang, Yuanfei Luo, Heng Dong, Wei Li, Yiming Gan"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2602.09972v1"
arxiv_id: 2602.09972v1
arxiv_url: "https://arxiv.org/abs/2602.09972v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/020-2026_wang_hydra_nav-3d4d7d50-4a2fb87e7d86.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2602.09972v1", "query:Object Goal Navigation", "query:Large Vision-Language Models", "query:Temporal-Spatial Reasoning", "query:Dual-Process Reasoning", "query:Adaptive Reasoning"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "针对现有基于VLM的目标导航在效率和效果上的不足，提出Hydra-Nav统一架构，通过自适应切换深思熟虑的慢系统和反应式的快系统来平衡规划与执行。采用三阶段课程训练：空间-动作对齐、记忆推理集成和迭代拒绝微调。在HM3D、MP3D和OVON基准上超越次优方法11.1%-21.2%。引入SOT新指标衡量搜索效率，表明自适应推理显著提升效率。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1714, \"height\": 605, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1380, \"height\": 634, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1705, \"height\": 651, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1555, \"height\": 583, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1385, \"height\": 391, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1551, \"height\": 760, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 861, \"height\": 711, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1720, \"height\": 677, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1706, \"height\": 401, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1714, \"height\": 1541, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1713, \"height\": 1031, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1440, \"height\": 478, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1711, \"height\": 985, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1708, \"height\": 439, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1235, \"height\": 247, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-020-4a2fb87e7d86-hydra-nav-object-navigation-via-adaptive-dual-process-reasoning/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1791, \"height\": 342, \"label\": \"Table\"}]"
motivation: 现有VLM导航方法效率低且对未见物体定位不佳，缺乏时空推理，而注入推理的方法带来高计算开销。
method: Hydra-Nav架构自适应切换慢系统（高层规划）和快系统（高效执行），通过三阶段课程训练增强推理与效率。
result: "在HM3D、MP3D、OVON基准上SOTA，分别提升11.1%、17.4%、21.2%，新指标SOT证明自适应推理提升搜索效率。"
conclusion: 自适应双过程推理可有效平衡导航的准确性和效率，为VLM导航提供了新范式。
---

## 摘要
尽管大型视觉语言模型在物体目标导航方面显示出潜力，但当前方法仍然面临成功率低和未见物体定位效率低下的问题——这些失败主要归因于弱的时间空间推理。同时，最近尝试向基于VLM的智能体中注入推理的方法提高了成功率，但带来了显著的计算开销。为了解决现有方法的低效性和低效性，我们引入了Hydra-Nav，一种统一的VLM架构，它能够在分析探索历史并制定高层计划的深思熟虑的“慢系统”和用于高效执行的反应式“快系统”之间自适应切换。我们通过三阶段课程训练Hydra-Nav：(i) 空间-动作对齐以加强轨迹规划，(ii) 记忆-推理整合以增强长程探索中的时空推理，以及(iii) 迭代拒绝微调以在关键决策点实现选择性推理。大量实验表明，Hydra-Nav在HM3D、MP3D和OVON基准测试中达到了最先进的性能，分别比第二名方法高出11.1%、17.4%和21.2%。此外，我们引入了SOT（操作时间加权成功率），一种新的度量标准，用于衡量不同推理强度下VLM的搜索效率。结果表明，与固定频率基线相比，自适应推理显著提高了搜索效率。

## Abstract
While large vision-language models (VLMs) show promise for object goal navigation, current methods still struggle with low success rates and inefficient localization of unseen objects—failures primarily attributed to weak temporal-spatial reasoning. Meanwhile, recent attempts to inject reasoning into VLM-based agents improve success rates but incur substantial computational overhead. To address both the ineffectiveness and inefficiency of existing approaches, we introduce Hydra-Nav, a unified VLM architecture that adaptively switches between a deliberative “slow system” for analyzing exploration history and formulating high-level plans, and a reactive “fast system” for efficient execution. We train Hydra-Nav through a three-stage curriculum: (i) spatial-action alignment to strengthen trajectory planning, (ii) memory-reasoning integration to enhance temporal-spatial reasoning over long-horizon exploration, and (iii) iterative rejection fine-tuning to enable selective reasoning at critical decision points. Extensive experiments demonstrate that Hydra-Nav achieves state-of-the-art performance on the HM3D, MP3D, and OVON benchmarks, outperforming the second-best methods by 11.1%, 17.4%, and 21.2%, respectively. Furthermore, we introduce SOT (Success weighted by Operation Time), a new metric to measure search efficiency across VLMs with varying reasoning intensity. Results show that adaptive reasoning significantly enhances search efficiency over fixed-frequency baselines.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有基于大型视觉语言模型(VLM)的物体目标导航方法面临两个核心矛盾：一是成功率低且对未见物体定位不佳，主要原因在于时空推理能力不足；二是为了提升成功率而注入推理（如Chain-of-Thought）虽然有效，但会带来巨大的计算开销，导致搜索效率低下。
- 因此，论文旨在同时解决**低效与低效果**问题，寻求一种既能保持高成功率又能降低推理开销的导航架构。

## 二、论文提出的方法论
- **整体架构：Hydra-Nav**，一个统一VLM架构，支持双过程推理（dual-process reasoning）：
  - **慢系统（Slow System）**：在关键决策点进行深思熟虑的推理，包括回顾历史记忆、分析当前观测、制定高层探索计划。
  - **快系统（Fast System）**：在其他时刻执行快速反应式低层控制动作（如移动、旋转）。
- **自适应切换机制**：通过一个特殊Token `obs`触发从快系统到慢系统的切换（全景扫描更新记忆），模型自学习何时触发推理，而非固定频率。
- **三阶段课程训练流水线**：
  1. **阶段1：空间-动作对齐（Spatial-action Alignment）**：使用A*规划器生成的500K轨迹，训练基础VLM（Qwen2.5-VL-7B）生成低层动作，实现导航基础能力。
  2. **阶段2：推理-记忆集成（Reasoning-memory Integration）**：使用启发式路径选择算法生成包含探索行为的轨迹，并通过Qwen3-VL-235B-Thinking合成高质量的推理文本（包含记忆总结、当前分析、未来规划），训练模型具备时空推理和记忆能力。
  3. **阶段3：自适应推理（Adaptive Reasoning via Iterative Rejection Fine-tuning, IRFT）**：通过在线策略回滚检测“停滞点”（重复探索或缺乏进展），在停滞点触发推理并修复失败轨迹，迭代训练模型自适应地决定何时使用慢系统。
- **记忆机制**：维护一个序列化的里程碑图（landmark nodes + action edges），每个里程碑包含全景图像，动态修剪保留最多10个节点。
- **动作空间**：混合空间，包括低层动作（MoveAhead, TurnLeft/Right, End）和系统切换token obs。

## 三、实验设计
- **数据集与场景**：使用三个标准基准：
  - HM3D（Habitat-Matterport 3D）
  - MP3D（Matterport3D）
  - OVON（Open-Vocabulary Object Navigation，包含Val-Seen、Val-Synonyms、Val-Unseen三个子集）
- **对比方法**：与多种现有方法对比，包括VoroNav、InstructNav、VLMnav、L3MVN、VLFM、GAMap、SG-Nav、UniGoal、CompassNav、BeliefMapNav、TriHelper、MTU3D、WMNav、CogNav、NavFoM、Nav-R2、Nav-R1、zson、Navid、PixNav、ESC、Uni-Navid等。
- **评估指标**：
  - 传统指标：成功率(SR)和成功率加权路径长度(SPL)。
  - 新提出指标：**SOT（成功加权操作时间）**，考虑机器人执行时间与模型推理延迟，衡量搜索效率。
- **实验分组**：包括主实验对比、消融实验（记忆模块、数据收集策略、训练阶段、共训练等）、多轮迭代IRFT效果分析、实际机器人部署展示。

## 四、资源与算力
- **基础模型**：Qwen2.5-VL-7B（阶段1、2），阶段3基于阶段2模型。
- **硬件**：
  - 阶段1：128块GPU
  - 阶段2：96块GPU
  - 阶段3：64块GPU
- **训练成本**：
  - 阶段1：约140小时（500K轨迹，20.1B tokens）
  - 阶段2：约100小时（565K混合样本，8.3B tokens）
  - 阶段3：约50小时（每轮约60K轨迹，4.5B tokens）
- **推理硬件**：单块NVIDIA H20 GPU，用于推理延迟计时（τ=0.015s/token）。
- **优化器**：AdamW（β1=0.9, β2=0.95），bfloat16精度，余弦学习率调度，warmup 0.1，权重衰减0.1，梯度裁剪1.0。

## 五、实验数量与充分性
- 实验覆盖**三个主流基准的多个子集**，总共报告了超过10种对比方法的性能。
- 消融实验分组全面：记忆容量影响（有无记忆、L=5/10/15）、数据收集策略（探索vs.最短路径）、训练阶段跳跃（无阶段1）、共训练数据影响。
- 多轮迭代IRFT（共3轮）的效果分析随轮次变化。
- 实际机器人部署（Unitree Go2 + Intel RealSense D457）展示零样本迁移能力。
- **充分性评价**：实验设计较为充分，覆盖了主要变体和消融维度，对比方法更新至2025-2026年的SOTA，指标包括SR、SPL和新增的SOT，考虑了效率维度。但所有仿真实验仅在Habitat模拟器中完成，缺乏其他仿真器（如IsaacSim）和更真实环境的验证，这是一个明显的限制。

## 六、论文的主要结论与发现
- Hydra-Nav在所有三个基准上均取得新SOTA：
  - HM3D Val：SR 84.8%（+11.1% vs. Uni-Navid）
  - MP3D Val：SR 64.0%（+17.4% vs. CogNav）
  - OVON Val-Unseen：SR 66.3%（+21.1% vs. NavFoM）
- 三阶段课程训练逐级提升性能：阶段2引入推理与记忆后SR大幅提升；阶段3自适应推理（IRFT）不仅进一步提升SR（约10-15个百分点），而且显著提升搜索效率（SOT从12.3%提升至22.2%）。
- 自适应推理相比固定频率推理可大幅减少推理开销（推理比例仅3.0%），同时保持高成功率。
- 记忆模块对搜索效率至关重要（无记忆时SPL低）。
- 探索数据（启发式路径选择）比仅用最短路径数据显著提升成功率（+25.4% on HM3D）。
- 共训练通用VQA数据有助于维持基础VLM的图像理解能力。

## 七、优点
- **创新性**：首次在单一VLM内统一自适应慢-快双过程推理，避免了模块化系统的架构碎片化和僵化切换。
- **实用性**：新提出的SOT指标综合考虑了机器人执行时间和模型推理延迟，更贴合实际部署。
- **效率显著**：IRFT使推理比例降至约3%，极大降低计算成本，同时性能反超固定频率方法。
- **数据合成方法**：利用更强的VLM（Qwen3-VL-235B）以“隐藏未来信息”的方式生成高质量推理文本，防止信息泄露。
- **课程训练设计合理**：三个阶段逐步增强能力，从基础动作到推理再到自适应，并且每个阶段都有明确目标和数据格式。
- **实际部署验证**：在真实机器人上零样本迁移成功，增加了可信度。

## 八、不足与局限
- **仿真环境单一**：所有量化评估均在Habitat模拟器中进行，缺乏在更逼真仿真器（如IsaacSim）或物理世界的系统评估（仅有少量演示），存在仿真到真实的泛化风险。
- **硬件依赖性**：SOT指标中的τ值基于特定GPU（H20），不同硬件下结果可能变化；论文虽做了敏感性分析（τ从0.0075s到0.48s），但仍需更多实验验证。
- **长尾场景**：论文未分析在极端长尾或异常环境（如杂物极多、目标极隐蔽）下的性能。
- **状态检测依赖**：停滞点检测的阈值（Tstag=20，δstag=0.5m）和U(20,35)分布可能不是最优的，未进行详细灵敏度分析。
- **记忆修剪策略**：最多保留10个里程碑，在超大场景中可能丢失重要历史信息，论文未讨论记忆上限对长程探索的影响。
- **可复现性**：虽然开源了训练配置和部分提示词，但未提供完整训练代码或检查点，可能影响复现。

（完）
