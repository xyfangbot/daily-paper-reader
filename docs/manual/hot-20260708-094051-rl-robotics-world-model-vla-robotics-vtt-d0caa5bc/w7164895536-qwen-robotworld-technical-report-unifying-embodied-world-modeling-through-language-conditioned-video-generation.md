---
title: "Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation"
title_zh: Qwen-RobotWorld技术报告：通过语言条件视频生成统一具身世界建模
authors: "Jie Zhang, Xiaoyue Chen, Anzhe Chen, Chenxu Lv, Deqing Li, Gengze Zhou, Hang Yin, Haoqi Yuan, Haoyang Li, Jiahao Li, Jiazhao Zhang, Jingren Zhou, Kaiyuan Gao, Kun Yan, Lihan Jiang, Ningyuan Tang, Pei Lin, Qihang Peng, Shengming Yin, Tianhe Wu"
date: 2026-06-15
pdf: "https://doi.org/10.48550/arxiv.2606.17030"
tags: ["query:热点论文筛选", "query:VLA-robotics", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:alibaba group"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=90d; cited_by_count=0; institution_filter=company; company_relation_match=alibaba group; relation_source=branded-title; query=diffusion policy for robot action generation"
tldr: 具身智能需要统一的世界模型来预测未来视觉轨迹。我们提出Qwen-RobotWorld，以自然语言为统一动作接口，通过60层双流扩散transformer耦合Qwen2.5-VL与视频VAE，在8.6M视频文本数据集EWK上经通用+专家两阶段训练，实现机器人操作、自动驾驶等多场景视频预测。模型在EWMBench和DreamGen Bench上排名第一，WorldModelBench和PBench超越所有开源模型，零样本分析展现强泛化与多视角一致性。这一工作为策略训练增广、可扩展虚拟环境和语言引导规划提供了统一框架。
source: openalex
selection_source: hot_paper_scout
motivation: 现有具身世界模型缺乏统一语言接口和跨场景泛化能力，亟需一个能通过自然语言预测多形态机器人、自动驾驶等未来视觉轨迹的通用模型。
method: 采用双流MMDiT架构，通过层级联合注意力融合冻结的Qwen2.5-VL语义与视频VAE隐变量；构建8.6M视频文本语料库EWK（200M+帧，20+本体，500+动作类别）；设计通用+专家渐进课程，先学习视觉先验再注入具身专长。
result: 在EWMBench和DreamGen Bench上排名第一；WorldModelBench和PBench上超越所有开源模型；零样本RoboTwin-IF分析验证了强泛化能力和多视角一致性。
conclusion: 提出统一语言条件视频世界模型，为具身智能提供数据生成、虚拟评估和规划信号，展现了显著的竞争力与泛化能力。
---

## 摘要
本文介绍Qwen-RobotWorld，一个面向具身智能的语言条件视频世界模型。该模型以自然语言作为统一动作接口，能够从当前观测中预测机器人操作、自动驾驶、室内导航以及人机迁移等场景下具有物理基础的未来视觉轨迹。这一统一框架提供了三个有前景的应用方向：用于策略训练增强的合成数据生成、用于策略评估的可扩展虚拟环境，以及用于下游机器人控制的语言引导规划信号。这通过三部分设计实现：a) 双流MMDiT与MLLM动作编码，其中60层双流扩散变压器通过层级联合注意力将冻结的Qwen2.5-VL语义与视频-VAE潜变量耦合；b) 具身世界知识（EWK），一个包含860万视频-文本对（超2亿帧）的语料库，涵盖20余种具身形态和500余种动作类别，并建立动作-语言映射；c) 通用+专家渐进课程，一种两阶段训练策略，先学习通用视觉先验，再在共享语言接口下注入具身专业化知识。大量实验结果表明其强大竞争力：在EWMBench和DreamGen Bench上综合排名第一，在WorldModelBench和PBench上超越所有开源模型。在RoboTwin-IF基准上的额外零样本分析进一步支持了其鲁棒泛化能力和多视角一致性。

## Abstract
We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for policy evaluation, and language-guided planning signals for downstream robot control. This is achieved through a three-part design: a) Double-Stream MMDiT with MLLM Action Encoding, where a 60-layer double-stream diffusion transformer couples frozen Qwen2.5-VL semantics with video-VAE latents through layer-wise joint attention; b) Embodied World Knowledge (EWK), an 8.6M video-text corpus (200M+ frames) with action-language mapping over 20+ embodiments and 500+ action categories; and c) General+Expert Progressive Curriculum, a two-stage training strategy that first learns general visual priors and then injects embodied specialization under a shared language interface. Extensive results show strong competitiveness: ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open-source models on WorldModelBench and PBench. Additional zero-shot analyses on RoboTwin-IF benchmark further support robust generalization and multi-view consistency.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 具身智能（embodied intelligence）需要统一的世界模型来预测未来视觉轨迹，但现有工作缺乏统一的语言动作接口和跨场景泛化能力。
- 当前方法通常针对单一具身形态（如仅机器人操作或自动驾驶）训练，难以在不同任务（操控、导航、驾驶、人机迁移）间迁移。
- 作者提出以自然语言作为统一动作接口，将不同具身场景的“动作”映射为语言指令，从而实现一个能同时预测多种未来视觉轨迹的通用世界模型，为策略训练数据增强、虚拟环境评估和语言引导规划提供统一框架。

## 二、论文提出的方法论
- **核心思想**：构建语言条件视频生成世界模型，输入当前观测图像和自然语言动作指令，输出未来多帧视频。
- **关键技术细节**：
  - 双流MMDiT（Double-Stream MMDiT）架构：60层双流扩散变压器，通过层级联合注意力（layer-wise joint attention）将冻结的Qwen2.5-VL（多模态大语言模型）的语义特征与视频VAE的潜变量耦合。
  - MLLM Action Encoding：使用冻结的Qwen2.5-VL对自然语言动作指令进行编码，作为条件注入扩散过程。
- **数据集**：构建具身世界知识（EWK）语料库，包含860万视频-文本对（超过2亿帧），覆盖20余种具身形态（机器人、车辆、室内代理等）和500余种动作类别，并建立动作到自然语言的映射。
- **训练策略**：两阶段渐进课程（General+Expert Progressive Curriculum）：
  - 第一阶段：在通用视频数据上学习物理世界视觉先验（如物体运动、场景动力学）。
  - 第二阶段：在EWK数据集上注入具身专业知识，统一使用自然语言动作接口，使模型学会特定场景下的动作-视觉关联。

## 三、实验设计
- **数据集/场景**：使用EWK数据集训练，并在多个公开基准上评估。
- **Benchmark**：
  - EWMBench：综合排名第一。
  - DreamGen Bench：综合排名第一。
  - WorldModelBench：超越所有开源模型。
  - PBench：超越所有开源模型。
- **零样本分析**：在RoboTwin-IF基准上进行额外零样本测试，验证泛化能力和多视角一致性。
- **对比方法**：与所有开源视频世界模型进行比较（具体方法未在摘要中列出，但声称超越它们）。

## 四、资源与算力
- **文中明确说明**：摘要和提供的元数据中未提及具体的GPU型号、数量或训练时长。仅提到模型包含60层双流扩散变压器，以及使用了8.6M视频文本对进行训练。
- **推断**：由于论文来自阿里巴巴集团（Qwen团队），且模型规模较大（60层双流Transformer），推测训练需要大量GPU资源（如数百张A100或H800），但具体数据未公开。

## 五、实验数量与充分性
- **实验数量**：至少覆盖4个主要基准（EWMBench、DreamGen Bench、WorldModelBench、PBench）和一个零样本基准（RoboTwin-IF），并且进行了“大量”实验（原文“Extensive results”）。但未详细列出消融实验或详细的单场景分析。
- **充分性与公平性**：
  - 优点：在多个不同任务的基准上对比开源模型，结果表现出竞争力；零样本测试验证了泛化能力。
  - 不足：仅提供了综合排名，未提供详细数值或与基线模型的逐项对比（如均方误差、FVD等指标）；未说明消融实验（如去掉EWK数据集或两阶段训练的影响）。实验覆盖但细节公开较少。

## 六、论文的主要结论与发现
- Qwen-RobotWorld通过语言条件视频生成实现了多种具身场景的统一世界建模，在多个基准上达到开源最优。
- 统一的自然语言动作接口使模型能够处理机器人操作、自动驾驶、室内导航和人机迁移等异构任务。
- 模型展现出鲁棒的多视角一致性（零样本分析支持）和跨场景泛化能力，为具身智能的数据生成、虚拟评估和规划信号提供了可行方案。

## 七、优点
- **统一性**：首次以自然语言为统一动作接口，将多种具身形态的场景纳入同一框架，具有创新性。
- **架构设计**：双流MMDiT结合冻结MLLM编码，有效融合语义与视觉时空信息，参数量大但合理。
- **数据集构建**：EWK语料库规模大（200M+帧，20+形态，500+动作），为世界模型提供了丰富的训练资源。
- **训练策略**：两阶段课程学习先获得通用视觉知识再注入具身专长，平衡了泛化与专业化。
- **应用前景**：明确指出了三个应用方向（数据生成、虚拟评估、规划信号），实用价值高。

## 八、不足与局限
- **实验细节不足**：摘要中仅给出排名，未报告具体量化指标（如PSNR、SSIM、FVD等），也未提供与基线方法的详细对比表。
- **消融实验缺失**：未说明双流架构、两阶段训练、EWK语料库等关键设计是否经过系统消融，无法判断各组件贡献。
- **算力与资源未公开**：训练成本不透明，难以评估可复现性。
- **物理一致性未验证**：虽然声称“物理基础”（physically grounded），但未提供定量验证（如物体碰撞、重力、遮挡等物理规律是否符合现实）。
- **零样本分析局限**：仅在一个基准（RoboTwin-IF）上进行，泛化能力证据尚不充分。
- **代码与模型未开源**：作为技术报告，目前仅发布PDF，未提及模型权重或代码开源，限制了社区验证与应用。

（完）
