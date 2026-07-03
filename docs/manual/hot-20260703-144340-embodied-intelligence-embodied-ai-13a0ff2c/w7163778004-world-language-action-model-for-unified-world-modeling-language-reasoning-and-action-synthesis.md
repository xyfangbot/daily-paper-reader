---
title: "World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis"
title_zh: 统一世界建模、语言推理与动作合成的世界-语言-动作模型
authors: "Yi Yang, Zhihong Liu (112690), Siqi Kou, Yiyang Chen, Yanzhe Hu, Jianbo Zhou, Boyuan Zhao, Zhijie Wei, Xiao Xia, Xueqi Li, Pengfei Liu, Zhijie Deng"
date: 2026-06-04
pdf: "https://arxiv.org/pdf/2606.05979"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; query=generalist robot policy"
tldr: "现有具身模型难以同时具备世界建模与语言推理能力。本文提出World-Language-Action (WLA)模型，以自回归Transformer为骨干，联合预测文本子任务、子目标图像和机器人动作，并引入World Expert监督物理动态以辅助动作生成。WLA-0在仿真和真实环境取得最优性能，RoboTwin2.0 Clean成功率92.94%，RMBench成功率56.5%，推理延迟仅40ms。该方法还支持从无动作标注的跨实体视频学习新任务，显著拓展了具身学习的应用范围。"
source: openalex
selection_source: hot_paper_scout
motivation: 统一世界建模与语言推理，解决复杂长时程任务中状态预测与动作生成的耦合问题。
method: 基于自回归Transformer联合预测文本、图像和动作，利用World Expert监督物理动态并辅助Action Expert。
result: "WLA-0在RoboTwin2.0 Clean和RMBench分别达92.94%和56.5%成功率，推理速度40ms。"
conclusion: 实现了世界建模、语言推理与动作合成的统一，可从无标注跨实体视频直接学习新任务。
---

## 摘要
我们提出世界-语言-动作（WLA）模型作为一类新的具身基础模型。WLA将文本指令、图像和机器人状态作为输入，联合预测文本子任务、子目标图像和机器人动作，结合了世界建模接口（从大量自我中心视频中学习，如世界-动作模型（WAM））和语言推理能力（解决复杂长时域任务，如视觉-语言-动作（VLA）模型）。WLA的核心是自回归（AR）Transformer主干网络，而非WAM中的双向扩散Transformer，用于预测下一状态，包括语义级文本意图和互补的细粒度物理动态。物理动态通过基于专用世界专家的世界建模目标进行监督，并用于简化动作专家对状态-动作相关性的表征。WLA利用元查询使世界预测隐式影响动作生成，从而在推理时可禁用世界预测。世界预测也可被激活，以实现测试时缩放，从而改进机器人控制。我们的WLA-0原型具有2B活跃参数，在NVIDIA RTX 5090上每次推理仅需40毫秒。在模拟和真实环境中的评估表明，WLA-0达到了最先进的多任务和长时域学习能力，例如在RoboTwin2.0 Clean上成功率为92.94%，在RMBench上成功率为56.5%。WLA-0还具有直接从跨形态机器人视频中学习新任务的能力，无需动作标注。

## Abstract
We propose world-language-action (WLA) models as a new class of embodied foundation models. WLA takes textual instructions, images, and robot states as inputs to jointly predict textual subtasks, subgoal images, and robot actions, conjoining the \emph{world modeling interface} to learn from extensive egocentric videos as in the world-action model (WAM) and the \emph{language reasoning} capacities to solve complex long-horizon tasks as in vision-language-action (VLA) models. At the core of WLA lies an \emph{autoregressive (AR)} Transformer backbone, instead of a bidirectional diffusion Transformer as in WAMs, to predict the \emph{next state}, comprising the \emph{semantic-level} textual intention and complementary \emph{fine-grained} physical dynamics. The physical dynamics are supervised by the world modeling objective based on a dedicated World Expert, and are leveraged to ease the characterization of the state-action correlation for the Action Expert. WLA leverages meta-queries to make the world prediction \emph{implicitly} impact the action generation so that the former can be disabled during inference. The world prediction can also be activated to enable test-time scaling for improved robot control. Our WLA-0 prototype, with 2B active parameters, achieves 40 ms per inference on an NVIDIA RTX 5090. Evaluations across simulated and real-world environments demonstrate that WLA-0 achieves state-of-the-art multi-task and long-horizon learning abilities, e.g., 92.94\% success rate on RoboTwin2.0 Clean and 56.5\% success rate on RMBench. WLA-0 also holds the promise to learn novel tasks directly from \emph{cross-embodiment robot videos} without action annotations.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：现有具身基础模型分为两类：世界-动作模型（WAM）擅长利用大量自我中心视频进行世界建模，但缺乏语言推理能力，难以处理复杂长时域任务；视觉-语言-动作模型（VLA）具备语言理解和规划能力，却难以捕获物理动态，缺乏视觉监督信号。如何统一世界建模、语言推理与动作合成，是当前具身智能的核心挑战。
- **核心问题**：设计一种新的基础模型，既能从视频中学习世界动态，又能利用语言进行高层规划和推理，同时实现高效、低延迟的机器人控制，并支持从无动作标注的跨实体视频中学习新任务。
- **整体含义**：本文提出世界-语言-动作（WLA）模型，通过联合预测文本子任务（语义级下一状态）、未来视觉帧（物理动态）和机器人动作，统一了三类能力，在多种仿真和真实环境中取得最优性能，并为可扩展的跨实体机器人学习提供了新范式。

## 二、论文提出的方法论
- **核心思想**：以自回归（AR）Transformer 为骨干网络，替代 WAM 中的双向扩散Transformer（DiT）。AR Transformer 同时支持文本生成和序列预测，能够预测下一状态的两种互补表示：**高层的文本意图**（分解为文本子任务）和**低层的物理动态**（捕捉视觉状态之间的核心过渡信息）。
- **关键技术细节**：
  - **文本意图学习**：利用预训练 VLM 初始化骨干，将原始指令分解为子任务序列，模型预测覆盖当前动作窗口的连续子任务窗口，并用记忆缓冲区递归更新，支持长时域任务。
  - **物理动态建模**：在骨干上附加一组**元查询（Meta-queries）**，通过因果注意力聚合上下文，输出物理动态表示 $h_t$。该表示作为潜在动作，驱动世界专家（World Expert）预测未来视觉帧 $o_{t+n}$，同时引导动作专家（Action Expert）生成显式动作 $a_{t:t+n}$。世界专家使用轻量扩散Transformer（SANA-600M），预测静态未来帧而非完整视频，并学习VAE特征而非语义特征。
  - **隐式影响机制**：通过共享参数训练，使世界预测隐式影响动作生成，推理时可完全丢弃世界专家，仅用骨干和动作专家，大幅降低延迟（约40ms）。若计算资源充足，可激活测试时缩放（TTS）模式：采样多个候选动作，用世界专家预测未来帧，用价值模型打分，选择最佳动作执行。
- **训练目标**：联合优化三个损失：子任务生成交叉熵损失、世界建模流匹配损失、动作预测流匹配损失，权重为 $\mathcal{L} = \mathcal{L}_{act} + \alpha \mathcal{L}_{wm} + \beta \mathcal{L}_{lang}$，其中 $\alpha=0.1$, $\beta=0.005$。

## 三、实验设计
- **数据集与基准**：
  - **仿真实验**：
    - RoboTwin 2.0：50个双机械臂操作任务，含Clean和Rand（强随机化）设置，常用多任务训练和评估。
    - LIBERO：四个套件（Spatial, Object, Goal, Long），每个10个任务，评估多任务泛化能力。
    - RMBench：长时域、依赖记忆的双臂操作基准，四个任务需反复探索、试错恢复、长期记忆。
  - **真实世界实验**：四个长时域任务（拧瓶盖、打包物体、堆叠杯子、扔垃圾），每个任务在标准设置、OOD物体、OOD场景三种条件下评估。
  - **跨实体视频学习**：RoboTwin 2.0 的5个未见任务，使用相同实体（Aloha-AgileX）或跨实体（ARX-X5）的机器人视频，以及人类自我中心视频。
- **对比方法**：
  - WAM基线：π0, π0.5, Motus, LingBot-VA, Fast-WAM。
  - VLA基线：π0.5, X-VLA, Mem-0。
  - 自身消融变体：-L_wm（去除世界专家损失）、-L_lang（去除子任务预测损失）、+TTS（测试时缩放模式）。
- **评估指标**：任务成功率、完成时间、推理延迟。

## 四、资源与算力
- **模型参数**：WLA-0总参数3.4B，活跃参数2B（推理时丢弃世界专家）。骨干为RynnBrain-2B（2.1B），世界专家为SANA-600M（900M含VAE），动作专家为流匹配头（390M）。元查询数64，动作块大小：LIBERO为8，其他为32。
- **硬件**：单个NVIDIA RTX 5090 GPU进行推理（约40ms/次训练），训练使用多GPU（未明确数量）和DeepSpeed分布式训练框架。
- **训练细节**：优化器AdamW（权重衰减1e-8，梯度裁剪1.0），学习率余弦调度（基5e-5，最小5e-6，1000步预热）。训练步数因任务而异：RoboTwin 2.0 100k步，LIBERO 100k步（30k即达强性能），RMBench 单任务30k步，真实世界任务50k步，跨实体学习50k步。全局批量大小256或448（RMBench）。文中未明确给出GPU数量或总训练时长。

## 五、实验数量与充分性
- **实验数量**：覆盖三大仿真基准（RoboTwin 2.0, LIBERO, RMBench）和四个真实世界任务，每个任务设置三种难度（标准、OOD物体、OOD场景），还包含跨实体视频学习实验（四种设置）以及人类视频尝试。消融实验包括去除世界专家损失、去除子任务损失、测试时缩放等。每个实验报告100或50次试验的平均成功率，以及10次真实世界试验的平均成功次数。
- **充分性与公平性**：
  - 对比了强基线和同类最新方法（π0, π0.5, Motus等），在多个标准benchmark上取得最佳或持平结果。
  - 消融实验验证了世界专家和子任务预测各自的重要性，测试时缩放带来进一步提升。
  - 跨实体学习实验设计合理，验证了从无动作视频学习新任务的能力，且对比了相同/跨实体视频、人类视频的效果差异。
  - 真实世界实验考虑了OOD泛化，并评估了推理效率和完成时间，具有实际意义。
  - 局限性：真实任务数量较少（仅4个），以成功率为主，缺乏更细粒度指标；跨实体学习在人类视频上失败，分析原因但未深入解决；未提供标准偏差或置信区间；部分实验（如RMBench）每任务仅100次试验，可能不够充分。

## 六、论文的主要结论与发现
- WLA模型通过联合预测文本子任务和物理动态，显著提升了长时域、记忆依赖的任务性能（RMBench 56.5%成功率，接近最优基线的两倍），同时保持了实时推理能力（40ms）。
- WLA-0在RoboTwin 2.0 Clean成功率92.94%，LIBERO平均98.6%，均达到或超过使用更多参数和预训练的基线。
- 世界专家损失可有效引导动作生成，去除后性能下降；子任务预测对长时域任务至关重要，去除后RMBench成功率从56.5%降至17.25%。
- 测试时缩放（TTS）可进一步改善结果（LIBERO 98.6%→98.9%）。
- WLA能够从无动作标注的跨实体机器人视频学习新任务，成功率达34.4%（相同实体）和28.8%（跨实体），显著超过仅使用动作监督的基线（13.0%），展现了零样本跨模态和跨实体泛化能力。
- 人类自我中心视频因域差异未能有效学习，表明需进一步对齐。

## 七、优点
- **方法创新**：首次将AR Transformer用于世界建模与动作合成统一框架，巧妙结合文本意图与物理动态，通过元查询和隐式影响机制实现高效推理。
- **高效性**：推理时丢弃世界专家，仅2B参数，40ms延迟，适合实时控制；测试时缩放方案灵活可调。
- **数据适应性强**：支持多种异构数据（图像-文本对、机器人演示、自我中心视频、无动作视频），可跨实体学习新任务，降低数据采集成本。
- **实验全面**：覆盖多种仿真和真实环境，含OOD泛化和效率评估，消融实验充分验证各模块贡献。
- **开源与可复现**：提供了代码链接，技术细节丰富（附录含加速技术、超参数等）。

## 八、不足与局限
- **真实世界实验规模有限**：仅在单个双机械臂平台上评估4个任务，缺乏更多实体、更多场景（如移动操作、复杂动态环境）的验证，泛化性有待进一步证明。
- **跨实体学习对域差异敏感**：人类自我中心视频因与仿真环境差异大而失败，未探索如何缩小这一差距（如域适应、迁移学习）。
- **缺乏不确定性量化**：实验报告点估计成功率，未提供方差或置信区间，难以评估结果的稳定性。
- **长时域任务依赖手工子任务定义**：RMBench的子任务分解需事先定义，限制了完全端到端自动规划的能力。
- **计算资源细节不透明**：未明确给出训练GPU数量、总时间等，不利于其他研究者复现或横向比较效率。
- **价值模型训练需额外数据**：测试时缩放需用模型自身 rollout 训练价值模型，增加了实施复杂度。

（完）
