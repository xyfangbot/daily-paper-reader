---
title: "Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation"
title_zh: Qwen-RobotWorld技术报告：通过语言条件视频生成统一具身世界模型
authors: "Jie Zhang, Xiaoyue Chen, Anzhe Chen, Chenxu Lv, Deqing Li, Gengze Zhou, Hang Yin, Haoqi Yuan, Haoyang Li, Jiahao Li, Jiazhao Zhang, Jingren Zhou, Kaiyuan Gao, Kun Yan, Lihan Jiang, Ningyuan Tang, Pei Lin, Qihang Peng, Shengming Yin, Tianhe Wu"
date: 2026-06-15
pdf: "https://doi.org/10.48550/arxiv.2606.17030"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:alibaba group"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=alibaba group; relation_source=branded-title; query=Qwen-RobotWorld"
tldr: 具身智能面临多任务世界建模挑战，现有模型难以统一。Qwen-RobotWorld以自然语言为统一动作接口，通过双流MMDiT架构融合Qwen2.5-VL语义与视频VAE潜在，结合8.6M视频文本数据集EWK和渐进训练策略，预测未来视觉轨迹。在多个基准上排名第一，并展现出强零样本泛化与多视角一致性。该方法为策略训练数据生成、虚拟环境评估和机器人规划提供了统一框架。
source: openalex
selection_source: hot_paper_scout
motivation: 现有具身世界模型缺乏统一语言接口，难以泛化到多种任务和实体。Qwen-RobotWorld旨在通过语言条件视频预测统一世界建模。
method: 采用60层双流MMDiT，耦合冻结Qwen2.5-VL与视频VAE；构建8.6M视频文本数据集EWK；设计General+Expert渐进训练两阶段策略。
result: 在EWMBench和DreamGen Bench排名第一，WorldModelBench和PBench超越开源模型，RoboTwin-IF零样本泛化表现优异。
conclusion: 语言条件视频世界模型统一了多种具身任务，为数据生成、评估和规划提供可行方案。
---

## 摘要
我们介绍了Qwen-RobotWorld，一个面向具身智能的语言条件视频世界模型。它以自然语言作为统一动作接口，从当前观测（涵盖机器人操作、自动驾驶、室内导航以及人-机器人迁移）中预测基于物理规律的未来视觉轨迹。这一统一框架提供了三个有前景的应用方向：用于策略训练增强的合成数据生成、用于策略评估的可扩展虚拟环境，以及用于下游机器人控制的语言引导规划信号。该模型通过三部分设计实现：a) 双流MMDiT与多模态大语言模型动作编码——一个60层双流扩散变换器通过逐层联合注意力将冻结的Qwen2.5-VL语义与视频VAE潜变量耦合；b) 具身世界知识（EWK）——包含860万条视频文本语料（超过2亿帧），涵盖20余种具身形态和500多种动作类别的动作-语言映射；c) 通用+专家渐进式课程——两阶段训练策略，先学习通用视觉先验，再在共享语言接口下注入具身专长。大量结果表明其具有强竞争力：在EWMBench和DreamGen Bench上整体排名第一，在WorldModelBench和PBench上优于所有开源模型。在RoboTwin-IF基准上的额外零样本分析进一步支持了其稳健的泛化能力和多视角一致性。

## Abstract
We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for policy evaluation, and language-guided planning signals for downstream robot control. This is achieved through a three-part design: a) Double-Stream MMDiT with MLLM Action Encoding, where a 60-layer double-stream diffusion transformer couples frozen Qwen2.5-VL semantics with video-VAE latents through layer-wise joint attention; b) Embodied World Knowledge (EWK), an 8.6M video-text corpus (200M+ frames) with action-language mapping over 20+ embodiments and 500+ action categories; and c) General+Expert Progressive Curriculum, a two-stage training strategy that first learns general visual priors and then injects embodied specialization under a shared language interface. Extensive results show strong competitiveness: ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open-source models on WorldModelBench and PBench. Additional zero-shot analyses on RoboTwin-IF benchmark further support robust generalization and multi-view consistency.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 具身智能面临多任务世界建模挑战：现有模型难以统一处理机器人操作、自动驾驶、室内导航、人-机迁移等多种具身形态下的未来状态预测。
- 缺乏统一的动作接口：传统方法需要针对不同任务设计专门的动作空间，导致泛化能力受限，难以在异构场景间迁移。
- 论文动机：提出以自然语言作为统一动作接口，通过语言条件视频生成实现统一的具身世界建模，从而为策略训练数据生成、虚拟环境评估和下游规划提供通用框架。

## 二、论文提出的方法论
- 核心思想：构建一个语言条件视频世界模型，以当前观测图像和自然语言指令为输入，预测基于物理规律的未来视觉轨迹（视频序列）。
- 关键技术细节：
  - **双流 MMDiT 与 MLLM 动作编码**：采用 60 层双流扩散变换器（Double-Stream MMDiT），通过逐层联合注意力机制将冻结的 Qwen2.5-VL（多模态大语言模型）语义特征与视频 VAE 潜变量耦合，实现语言条件对视频生成过程的引导。
  - **具身世界知识（EWK）**：构建包含 860 万条视频-文本对（超过 2 亿帧）的大规模数据集，覆盖 20 余种具身形态和 500 多种动作类别，建立动作-语言映射关系。
  - **通用+专家渐进式课程（General+Expert Progressive Curriculum）**：两阶段训练策略。第一阶段学习通用视觉先验（大规模通用视频数据），第二阶段在共享语言接口下注入具身专长（使用 EWK 中的具身场景数据），平衡泛化性与专业性。
- 算法流程简述：输入当前图像帧 + 自然语言动作描述 → Qwen2.5-VL 编码语义 → 双流 MMDiT 通过扩散过程逐步去噪 → 输出未来多帧视频序列。

## 三、实验设计
- 使用数据集/场景：EWK 数据集（自建 860 万视频文本语料）、EWMBench、DreamGen Bench、WorldModelBench、PBench、RoboTwin-IF 基准。
- Benchmark 对比：与现有开源世界模型（未列出具体对比方法名称，但摘要指出在多个基准上排名第一或全面超越）进行比较。
- 评估指标：未在摘要中详细说明，但提及“排名”、“优于”等定性比较；零样本分析评估泛化能力与多视角一致性。

## 四、资源与算力
- 论文中未明确说明使用的 GPU 型号、数量、训练时长等具体算力信息。
- 仅可推断：训练 860 万视频文本语料（200M+ 帧）以及 60 层双流扩散变换器需要较高算力，但论文未披露细节。

## 五、实验数量与充分性
- 实验覆盖多个基准（4 个主要基准 + 1 个零样本基准），评估了排名和泛化能力，结果均显示领先。
- 未提供消融实验的明确数量或详细分析，仅提及“General+Expert Progressive Curriculum”两阶段设计，但缺少对每个组件效果的单独验证。
- 总体实验相对充分，涵盖多种具身任务场景，但内部消融和敏感性分析不够详实，公平性依赖公开基准，可能存在公开基准未覆盖的偏差。

## 六、论文的主要结论与发现
- 语言条件视频世界模型能够统一多种具身任务（机器人操作、自动驾驶、室内导航、人-机器人迁移）的世界建模。
- 所提出的三部分设计（双流 MMDiT、EWK 数据集、渐进课程）在多个公开基准上达到最优性能：EWMBench 和 DreamGen Bench 整体排名第一，WorldModelBench 和 PBench 全面超越开源模型。
- 零样本分析显示模型具备稳健的泛化能力和多视角一致性，验证了统一接口的有效性。
- 该框架为合成数据生成、策略评估和语言引导规划提供了可行方案。

## 七、优点
- 统一性：以自然语言为统一动作接口，首次将多种具身形态（机器人操作、自动驾驶、导航、人-机迁移）纳入同一世界模型框架。
- 方法设计创新：双流 MMDiT 融合大语言模型语义与视频潜变量，提供更精准的语言条件控制；渐进课程兼顾通用视觉先验与具身专长。
- 大规模数据支撑：构建 8.6M 视频文本语料（200M+ 帧），覆盖广泛的动作与具身形态，增强了模型多样性。
- 实验充分性：在多个权威基准上获得第一或超越开源，并进行了零样本评估，展示了较强的泛化能力。

## 八、不足与局限
- 算力与资源未公开：训练所需 GPU 型号、数量、时长未知，难以评估可复现性和实际部署成本。
- 消融实验缺乏：未对不同组件（如双流 MMDiT、数据集规模、课程策略）进行系统消融，无法量化各模块贡献。
- 实验覆盖有限：虽然涉及多种任务，但未详细说明在真实机器人平台上的物理部署验证，可能仅停留在仿真或视频预测阶段。
- 数据集偏差风险：EWK 数据集虽大规模但可能偏向特定动作和形态，导致在未见过的场景或罕见动作上表现下降。
- 零样本评估：仅提及 RoboTwin-IF 基准，缺乏对更多领域或极端情况的泛化测试。
- 应用限制：当前模型仅输出视频轨迹，未直接生成控制信号，需后续规划模块衔接；实时性未讨论，可能难以用于在线控制。

（完）
