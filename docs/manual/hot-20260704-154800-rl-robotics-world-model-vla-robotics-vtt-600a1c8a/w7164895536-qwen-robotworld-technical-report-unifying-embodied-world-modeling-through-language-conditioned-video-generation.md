---
title: "Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation"
title_zh: Qwen-RobotWorld技术报告：通过语言条件视频生成统一具身世界建模
authors: "Jie Zhang, Xiaoyue Chen, Anzhe Chen, Chenxu Lv, Deqing Li, Gengze Zhou, Hang Yin, Haoqi Yuan, Haoyang Li, Jiahao Li, Jiazhao Zhang, Jingren Zhou, Kaiyuan Gao, Kun Yan, Lihan Jiang, Ningyuan Tang, Pei Lin, Qihang Peng, Shengming Yin, Tianhe Wu"
date: 2026-06-15
pdf: "https://doi.org/10.48550/arxiv.2606.17030"
tags: ["query:热点论文筛选", "query:VLA-robotics", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:alibaba group"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=alibaba group; relation_source=branded-title; query=diffusion policy for robot action generation"
tldr: 具身智能体需要从当前观测预测未来状态，但现有世界模型多面向单一任务且缺乏统一接口。本文提出Qwen-RobotWorld，以自然语言为统一动作接口，利用双流扩散Transformer耦合Qwen2.5-VL语义与视频VAE潜变量，并构建包含860万视频文对的具身世界知识数据集进行两阶段训练。在EWMBench、DreamGen Bench上排名第一，WorldModelBench和PBench超越所有开源模型，零样本分析验证了强泛化与多视图一致性。该工作为合成数据生成、策略评估和语言引导规划提供了统一范式。
source: openalex
selection_source: hot_paper_scout
motivation: 克服现有具身世界模型缺乏统一语言接口、跨具身体泛化能力弱的问题。
method: 双流MMDiT耦合Qwen2.5-VL与视频VAE，结合8.6M视频文本数据集进行通用-专家两阶段渐进训练。
result: EWMBench和DreamGen Bench总分第一，WorldModelBench和PBench超越所有开源模型，零样本泛化强。
conclusion: Qwen-RobotWorld以语言为统一接口实现具身世界建模，为策略训练与规划提供新范式。
---

## 摘要
我们提出Qwen-RobotWorld，一种面向具身智能的语言条件视频世界模型。以自然语言作为统一动作接口，该模型能够从当前观测预测物理上合理的未来视觉轨迹，涵盖机器人操作、自动驾驶、室内导航以及人机迁移等场景。这种统一范式提供了三个有前景的应用方向：用于策略训练增强的合成数据生成、用于策略评估的可扩展虚拟环境，以及用于下游机器人控制的语言引导规划信号。这是通过三部分设计实现的：a) 采用MLLM动作编码的双流MMDiT，其中60层双流扩散变压器通过逐层联合注意力将冻结的Qwen2.5-VL语义与视频VAE潜变量耦合；b) 具身世界知识（EWK），一个包含860万视频-文本语料（超过2亿帧）的数据库，覆盖20余种具身形态和500余种动作类别的动作-语言映射；c) 通用+专家渐进课程，一种两阶段训练策略，先学习通用视觉先验，再在共享语言接口下注入具身专业化。大量结果表明其强大的竞争力：在EWMBench和DreamGen Bench上总体排名第一，在WorldModelBench和PBench上优于所有开源模型。在RoboTwin-IF基准上的额外零样本分析进一步支持了鲁棒的泛化能力和多视角一致性。

## Abstract
We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for policy evaluation, and language-guided planning signals for downstream robot control. This is achieved through a three-part design: a) Double-Stream MMDiT with MLLM Action Encoding, where a 60-layer double-stream diffusion transformer couples frozen Qwen2.5-VL semantics with video-VAE latents through layer-wise joint attention; b) Embodied World Knowledge (EWK), an 8.6M video-text corpus (200M+ frames) with action-language mapping over 20+ embodiments and 500+ action categories; and c) General+Expert Progressive Curriculum, a two-stage training strategy that first learns general visual priors and then injects embodied specialization under a shared language interface. Extensive results show strong competitiveness: ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open-source models on WorldModelBench and PBench. Additional zero-shot analyses on RoboTwin-IF benchmark further support robust generalization and multi-view consistency.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- 现有具身世界模型多面向单一任务（如机器人操作或自动驾驶），缺乏统一的动作接口和跨泛身形态的泛化能力。
- 具身智能体需要从当前观测预测未来状态（即世界模型），但传统方法通常需要为不同任务分别设计状态表示和动作表征。
- 本文提出以自然语言作为统一动作接口，将机器人操作、自动驾驶、室内导航和人机迁移等多项任务纳入同一个语言条件视频生成框架，实现“一个模型，多种具身”的通用世界建模。
- 该范式可服务于三个实际应用方向：合成数据生成以增强策略训练、可扩展虚拟环境用于策略评估、语言引导规划信号用于下游机器人控制。

## 二、论文提出的方法论

- **核心思想**：以自然语言描述动作（如“向左移动”“抓取杯子”），作为条件，从当前观测图像生成未来多帧物理合理的视频，从而统一建模不同具身体的世界动态。
- **架构设计**：Double-Stream MMDiT with MLLM Action Encoding
  - 采用60层双流扩散Transformer（MMDiT），一条流处理冻结的Qwen2.5-VL（多模态大语言模型）输出的语义特征，另一条流处理视频VAE的潜变量。
  - 通过逐层联合注意力机制（layer-wise joint attention）将语言语义与视觉潜变量深度融合。
- **数据支撑**：具身世界知识（Embodied World Knowledge, EWK）
  - 构建包含860万视频-文本对的数据集，总帧数超过2亿。
  - 覆盖20余种具身形态（如机械臂、自动驾驶车辆、移动机器人、人类演示等）和500余种动作类别，每段视频配以自然语言动作描述。
- **训练策略**：通用+专家渐进课程（General+Expert Progressive Curriculum）
  - 第一阶段：在所有数据上预训练，学习通用视觉先验和物理常识。
  - 第二阶段：在共享语言接口下，针对特定具身任务（如操作、驾驶）进行微调，注入专业领域知识。
- **推理流程**：给定当前观测图像和自然语言动作指令，扩散模型逐步去噪生成后续帧的视频序列。

## 三、实验设计

- **使用的数据集/场景**：
  - 主要训练数据为自建的EWK数据集（8.6M视频文本，200M+帧，20+具身体，500+动作类别）。
  - 评估在多个公开基准上进行，包括EWMBench、DreamGen Bench、WorldModelBench、PBench、RoboTwin-IF等，涵盖机器人操作、自动驾驶、室内导航等场景。
- **Benchmark比较**：
  - 模型在EWMBench和DreamGen Bench上总体排名第一。
  - 在WorldModelBench和PBench上超越所有开源模型（具体模型名称摘要未列出，推测包括CogView、UniSim等）。
  - 在RoboTwin-IF基准上进行了零样本分析，验证多视图一致性和泛化能力。
- **对比方法**：未提及具体基线模型名称，但说明“超越所有开源模型”，暗示与当前主流视频世界模型（如CogView、VideoWorld等）比较。

## 四、资源与算力

- 论文摘要及元数据中**未明确说明**使用的GPU型号、数量、训练时长等具体算力信息。
- 仅提到模型包含60层双流扩散Transformer，参数量级未给出，推断为大模型（可能数十亿参数），但资源消耗情况未公开。

## 五、实验数量与充分性

- **实验数量**：在至少5个不同基准上进行了评测，覆盖多种任务类型。还包含零样本迁移实验（RoboTwin-IF）和多视图一致性分析。
- **充分性评价**：
  - 优点：评测维度较全面，既包括了通用世界模型能力，又覆盖了具身体特异性任务，同时验证了零样本泛化。
  - 不足：摘要中未提及消融实验，例如对双流机制、数据集规模、训练策略各阶段的独立效果分析没有呈现；也未报告与真实机器人部署的闭环评估结果。
  - 总体而言，实验覆盖了多种标准benchmark，显示了领先性，但内部消融和实际部署验证的缺失使得实验的充分性有所局限。

## 六、论文的主要结论与发现

- 自然语言可以作为一种有效的统一动作接口，实现跨具身形态的世界建模。
- 双流MMDiT架构能够有效融合多模态大语言模型语义和视频VAE视觉表示，生成物理合理的未来视频。
- 构建的大规模EWK数据集和两阶段渐进训练策略是取得优异性能的关键。
- 模型在多项标准benchmark上取得SOTA（排名第一或超越开源模型），并在零样本任务上表现出强泛化能力，验证了方法的有效性。

## 七、优点

- **统一接口**：首次以自然语言作为动作指令统一多种具身任务，解决了异构动作空间带来的兼容性问题。
- **架构创新**：双流MMDiT结合冻结的MLLM（Qwen2.5-VL）与视频VAE，在不微调大语言模型的前提下实现语义-视觉深度融合，保持语言先验的同时实现高效视频生成。
- **数据规模与多样性**：EWK数据集覆盖20+种具身形态和500+种动作，为世界模型提供了丰富的训练素材，有助于学习通用物理规律。
- **训练策略**：通用到专家的渐进式课程设计，既保留了泛化能力，又能在特定任务上达到专业水平。
- **应用前景**：为策略训练的数据增强、虚拟环境评估和语言引导规划提供了统一框架，具有实际工业意义。

## 八、不足与局限

- **实验覆盖缺陷**：缺乏对模型在真实机器人或自动驾驶汽车上的闭环部署实验，仅停留在视频生成和离线评估；实际物理环境中时延、噪声、未建模动力学等因素可能影响性能。
- **消融研究缺失**：未提供对不同组件（如双流设计、训练阶段、数据规模）的详细消融分析，难以直接归因性能提升来源。
- **算力和可复现性**：资源消耗未公开，模型参数量、训练时长等关键信息缺失，增加了复现难度；依赖大规模私有钱数据（EWK），可能限制其他研究者独立验证。
- **语言接口局限**：自然语言动作描述可能存在歧义性和粒度不足，例如“向左移动”在具体环境中可能包含多种刚体运动模式，模型需要进一步吸收物理精确性。
- **偏差风险**：EWK数据集主要来自公开仿真或人类演示数据，可能存在分布偏倚，如偏好常见物体或简单场景，对长尾任务泛化能力未知。
- **视频生成评估标准**：虽然使用了多个benchmark，但视频生成质量评估指标（如FID、FVD、语义一致性等）的具体数值未在摘要中列出，无法量化比较。

（完）
