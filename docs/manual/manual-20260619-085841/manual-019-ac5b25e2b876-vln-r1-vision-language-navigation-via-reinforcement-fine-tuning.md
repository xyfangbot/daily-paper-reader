---
title: "VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning"
title_zh: VLN-R1：通过强化微调进行视觉-语言导航
authors: "Zhangyang Qi, Zhixiong Zhang, Yizhou Yu, Jiaqi Wang, Hengshuang Zhao"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/019-2025_qi_vln_r1-244b3587-ac5b25e2b876.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-Language Navigation", "query:Reinforcement Fine-Tuning", "query:Large Vision-Language Models", "query:GRPO", "query:Embodied AI"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有视觉语言导航（VLN）方法依赖离散拓扑图，限制了路径规划的灵活性。本文提出VLN-R1，一个端到端框架，利用大型视觉语言模型（LVLM）将第一人称视频流直接映射为连续导航动作，采用GRPO训练策略。通过构建VLN-Ego数据集和长短期记忆采样，结合监督微调和带时间衰减奖励的强化微调，在VLN-CE基准上取得强性能。该方法证明了LVLM可有效驱动具身导航，并通过数据高效的后训练提升任务推理能力。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-019-ac5b25e2b876-vln-r1-vision-language-navigation-via-reinforcement-fine-tuning/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1419, \"height\": 827, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-019-ac5b25e2b876-vln-r1-vision-language-navigation-via-reinforcement-fine-tuning/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1157, \"height\": 997, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-019-ac5b25e2b876-vln-r1-vision-language-navigation-via-reinforcement-fine-tuning/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1441, \"height\": 687, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-019-ac5b25e2b876-vln-r1-vision-language-navigation-via-reinforcement-fine-tuning/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1390, \"height\": 309, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-019-ac5b25e2b876-vln-r1-vision-language-navigation-via-reinforcement-fine-tuning/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1398, \"height\": 332, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-019-ac5b25e2b876-vln-r1-vision-language-navigation-via-reinforcement-fine-tuning/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1366, \"height\": 561, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-019-ac5b25e2b876-vln-r1-vision-language-navigation-via-reinforcement-fine-tuning/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1373, \"height\": 973, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-019-ac5b25e2b876-vln-r1-vision-language-navigation-via-reinforcement-fine-tuning/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 613, \"height\": 780, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-019-ac5b25e2b876-vln-r1-vision-language-navigation-via-reinforcement-fine-tuning/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 682, \"height\": 778, \"label\": \"Table\"}]"
motivation: 现有VLN方法基于离散拓扑图，路径规划受限于预设节点连接，缺乏连续动作生成的灵活性。
method: 提出VLN-R1框架，使用LVLM直接输出连续动作，通过GRPO训练，并采用两阶段方式：SFT对齐专家演示，RFT结合时间衰减奖励机制。
result: 在VLN-CE基准上，VLN-R1取得了具有竞争力的导航成功率，验证了端到端连续动作生成的有效性。
conclusion: VLN-R1表明LVLM能够驱动具身导航任务，并通过奖励驱动的后训练高效提升特定任务推理能力。
---

## 摘要
视觉-语言导航（VLN）是具身人工智能中的核心挑战，要求智能体使用自然语言指令在真实环境中导航。当前基于语言模型的导航系统在离散拓扑图上运行，将路径规划限制在预定义的节点连接上。我们提出VLN-R1，一个端到端框架，利用大型视觉-语言模型（LVLM）直接将自我中心视频流转化为连续导航动作，并采用受DeepSeek-R1启发的基于GRPO的训练。为了实现有效训练，我们首先使用3D模拟器Habitat构建了VLN-Ego数据集，并提出长短时记忆采样以平衡历史与当前观测。虽然大型语言模型可以监督完整的文本指令，但缺乏细粒度的动作级控制。我们的框架采用两阶段训练方法：a）监督微调（SFT），使模型的动作序列文本预测与专家演示对齐；随后b）强化微调（RFT），增强有时间衰减奖励（TDR）机制，该机制策略性地加权多步未来动作。实验结果表明，VLN-R1在VLN-CE基准上取得了强劲性能。VLN-R1证明了LVLM能够驱动具身导航，并通过数据高效、奖励驱动的后训练增强任务特定推理。

## Abstract
Vision-Language Navigation (VLN) is a core challenge in embodied AI, requiring agents to navigate real-world environments using natural language instructions. Current language model-based navigation systems operate on discrete topological graphs, limiting path planning to predefined node connections. We propose VLN-R1, an end-to-end framework that leverages Large Vision-Language Models (LVLM) to directly translate egocentric video streams into continuous navigation actions, adopting GRPO-based training inspired by DeepSeek-R1. To enable effective training, we first construct the VLN-Ego dataset using a 3D simulator, i.e., Habitat, and propose Long-Short Memory Sampling to balance historical and current observations. While large language models can supervise complete textual instructions, they lack fine-grained action-level control. Our framework employs a two-stage training approach: a) Supervised fine-tuning (SFT) to align the model's action sequence text predictions with expert demonstrations, followed by b) Reinforcement fine-tuning (RFT) enhanced with a Time-Decayed Reward (TDR) mechanism that strategically weights multi-step future actions. Experimental results show VLN-R1 achieves strong performance on VLN-CE benchmark. VLN-R1 proves LVLMs can drive embodied navigation and enhance task-specific reasoning through data-efficient, reward-driven post-training.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **视觉-语言导航（VLN）** 是具身人工智能中的核心挑战，要求智能体根据自然语言指令在真实或模拟的3D环境中导航。
- **现有方法的局限**：当前基于语言模型的导航系统通常依赖**离散拓扑图**（预定义的节点连接），路径规划受限于固定连接，缺乏在连续环境中自由移动的灵活性；且许多方法需要额外的传感器信息（如深度图、导航地图）或依赖CLIP等专用模型进行视觉-语言对齐，限制了泛化能力和人机交互的通用性。
- **本文目标**：提出一个端到端框架VLN-R1，利用大型视觉语言模型（LVLM）直接处理**自我中心（ego-centric）视频流**，输出**连续的导航动作**（前进、左转、右转、停止），消除对离散图结构或额外传感器的依赖，并通过强化微调提升任务推理能力。

## 二、论文提出的方法论
- **核心思想**：采用两阶段训练范式：1）**监督微调（SFT）**：让LVLM输出的动作序列文本与专家演示（ground truth）对齐；2）**强化微调（RFT）**：基于DeepSeek-R1的GRPO策略优化，并设计**时间衰减奖励（TDR）** 机制，强化对多步动作序列中早期正确动作的奖励，改善长期导航决策。
- **关键技术与细节**：
  1. **VLN-Ego数据集构建**：利用Habitat 3D模拟器（基于Matterport3D场景）生成第一人称视频流与对应的未来动作序列标签。动作分为四种基本命令（FORWARD 25cm、TURN-LEFT 30°、TURN-RIGHT 30°、STOP）。每个样本包含系统提示、自然语言指令、历史帧序列、当前观测帧和未来6步动作的真值。
  2. **长短期记忆采样（Long-Short Memory Sampling）**：处理视频输入时，短期记忆以高采样率δ₁获取最近M帧中的关键帧，长期记忆以低采样率δ₂（δ₂ > δ₁）覆盖更早的历史帧，平衡实时敏感性与长期上下文。
  3. **SFT阶段**：最小化模型预测的动作序列文本与真值文本之间的交叉熵损失，监督动作标识符（A/B/C/D）及其对应的动作描述。
  4. **RFT阶段**：使用GRPO优化，无需价值模型或奖励模型，从策略模型生成G个候选动作序列，通过组内相对优势（normalized reward）指导策略更新。提出**TDR**奖励函数：\( R_{nav} = \sum_{k=0}^{n-1} \gamma^k \cdot \mathbb{I}(\alpha_{t+k} = \alpha^*_{t+k}) \)，其中γ为衰减因子（γ<1），对更近的正确动作赋予更高权重，强调时序一致性。
- **公式与算法流程**（文字说明）：
  - GRPO优化目标：对每个问题q生成G个回答，计算每个回答的奖励，并通过组内均值和标准差归一化得到优势值A；并采用裁剪和KL散度惩罚确保策略更新稳定。
  - TDR奖励：基于指数衰减权重γ^k，对预测的动作序列中的每个位置k，若预测动作与真值匹配则加γ^k，否则加0。

## 三、实验设计
- **数据集与场景**：
  - 训练数据集：**VLN-Ego**，来源于Habitat模拟器上的Matterport3D场景，包含R2R（Room-to-Room，7,189条路径，630K训练样本）和RxR（Room-across-Room，42,023条路径，1.2M训练样本）轨迹。共90个场景（训练61个，val-seen 11个，val-unseen 18个）。
  - 评估基准：**VLN-CE**（Continuous Environments）标准，在Val-Unseen（18个未见过场景）上评测。
- **评价指标**：
  - 主要指标：**SR↑（成功率）**、**OS↑（Oracle成功率）**、**SPL↑（按路径长度加权的成功率）**
  - 辅助指标：**NE↓（导航误差，米）**、**TL（轨迹长度，米）**
- **对比方法**：
  - 对比了一类**任务特定方法**（如AG-CMTP、R2R-CMTP、LAW、CM2、WS-MGMap、Seq2Seq、CMA、A2Nav等），这些方法通常需要里程计、深度图或地图等额外信息。
  - 比对了**EGO-view LVLM方法**，即仅使用RGB视频的同类方法（包括本框架SFT阶段结果）。
  - 模型使用**Qwen2-VL-2B**和**Qwen2-VL-7B**两种规模。

## 四、资源与算力
- **硬件**：7B模型训练部署在**8张NVIDIA A800 GPU**上，采用DeepSpeed ZeRO-3优化。
- **训练配置**：
  - SFT阶段：学习率5e-6，余弦调度（10%预热），per-GPU batch size 2，全局batch size 64（4梯度累积），1 epoch耗时约36小时。
  - RFT阶段：学习率1e-6，weight decay 0.01，β=0.04，GRPO每prompt采样8个响应，per-GPU batch size 1（无梯度累积），1 epoch耗时约12小时。
  - 训练数据量：SFT使用1.8M样本（R2R+RxR全量）；RFT随机选取各10K，共20K样本。

## 五、实验数量与充分性
- **实验数量**：
  - 在**两个数据集**（R2R和RxR）的Val-Unseen上进行主实验，对比了多种现有方法。
  - **消融实验**全面：
    - SFT阶段：动作空间（单步 vs 4/6/8步）和记忆采样策略（均匀采样、指数衰减、长短期记忆）的消融。
    - RFT阶段：GRPO生成数量（k=2,4,6,8）和奖励函数（硬奖励、均匀奖励、线性距离权重、指数衰减）的消融。
  - 还包含了**跨领域迁移实验**（在R2R上SFT后，仅用10K RxR样本进行RFT，结果优于全量RxR训练）。
- **充分性与公平性评价**：
  - 实验设计较为充分，覆盖了核心设计选择和超参数影响，且所有模型仅使用自我中心RGB视频，与需要额外传感器的任务特定方法公平对比（但后者性能基线本身就夹带了更多信息）。
  - 不足之处：缺乏在真实物理环境上的实验（仅在模拟器中），也未与其他基于LVLM的方法（如Navid、Uni-Navi）进行直接复现对比（那些方法可能使用了不同的动作空间或交互方式）。

## 六、论文的主要结论与发现
- VLN-R1在**仅使用RGB自我中心视频**的条件下，在VLN-CE R2R和RxR的Val-Unseen分割上均取得了**最先进的性能**。
- **强化微调（RFT）效果显著**：2B模型经过RFT后性能可媲美7B的SFT结果，体现了RL后训练对小模型的高效提升。
- **跨域泛化能力强**：仅在R2R上SFT后，使用少量（10K）RxR数据通过RFT即可超越在完整RxR数据集上训练的效果，说明RFT能够高效适配新领域。
- **提出的长短期记忆采样和时间衰减奖励（TDR）均优于现有的基线设计**，有利于长期导航中的决策一致性。

## 七、优点
- **端到端简化**：无需离散导航图或额外传感器（深度、地图等），直接从自我中心视频生成连续动作，更接近真实具身场景。
- **创新性训练策略**：首次将GRPO（来自DeepSeek-R1）和强化微调用于VLN任务，并设计时间衰减奖励，针对性解决多步动作序列的时序监督问题。
- **数据高效**：RFT阶段仅需少量样本（如20K）即可带来显著性能提升，并支持跨领域迁移。
- **公开资源**：提供了数据集（VLN-Ego）和代码（https://vlnr1.github.io），有利于社区复现和后续研究。

## 八、不足与局限
- **纯模拟环境**：所有实验仅在Habitat模拟器（基于Matterport3D）中进行，未在真实物理机器人上验证，真实世界中的光照、纹理、动态物体等挑战未被覆盖。
- **离散动作空间**：虽然动作是连续的（可指定距离和角度），但动作类型固定为四种简单原子命令（前进25cm、左/右转30°、停止），缺乏更精细的操控（如变速、旋转角度可变、抓取等），限制了复杂任务的执行。
- **只评测导航任务**：仅涉及VLN基准，未充分探讨对Embodied QA等下游任务的泛化能力（仅提及附录中有EQA结果，但未在正文详细展示）。
- **并未与最先进的仿真LVLM方法（如Navid、Uni-Navi）在同一设置下直接复现对比**：这些方法可能使用相同的Qwen2-VL等基础模型，但论文只是给出了自己SFT和RFT的对比，未与这些已有工作完全对齐基线。
- **缺乏对超参数鲁棒性的深入分析**：例如TDR中的衰减因子γ的实验未明确展示（只有不同奖励函数的整体消融），GRPO生成数量实验仅做到k=8，未能说明更大组数是否更好。

（完）
