---
title: "RoboGPT-R1: Enhancing Robot Task Planning with Reinforcement Learning"
title_zh: "RoboGPT-R1: 通过强化学习增强机器人任务规划"
authors: "J M Liu, Bingyan Nie, Boyu Li, Yaran Chen, Yuze Wang, Shunsen He, Hui Li"
date: 2026-05-24
pdf: "https://arxiv.org/pdf/2510.14828"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:beijing academy of artificial intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=90d; cited_by_count=0; institution_filter=company; company_relation_match=beijing academy of artificial intelligence; relation_source=lead-affiliation; institutions=Beijing Academy of Artificial Intelligence; query=robot foundation model"
tldr: "当前大语言模型在长视野机器人操作任务中因常识和推理能力不足而表现不佳，基于监督微调的方法泛化性差且缺乏物理理解。为此提出RoboGPT-R1两阶段微调框架，先通过监督微调学习基础知识，再采用强化学习提升视觉-空间推理，并设计规则奖励函数确保动作序列一致性。在EmbodiedBench基准上，基于3B参数的模型超越GPT-4o-mini 21.33%，也超越基于7B参数的其他方法20.33%。该工作有效增强了具身智能体的长时推理与任务规划能力。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有监督微调方法在机器人长视野操作任务中泛化差、物理理解不足，需提升模型在复杂环境中的视觉-空间推理和动作序列一致性。
method: 提出两阶段微调框架RoboGPT-R1：先监督微调获取专家序列知识，再用强化学习优化视觉空间推理，设计考虑长时性能与环境约束的规则奖励函数。
result: "基于Qwen2.5-VL-3B的模型在EmbodiedBench上超越GPT-4o-mini 21.33%，超越基于Qwen2.5-VL-7B的其他方法20.33%。"
conclusion: 验证了强化学习结合监督微调能显著提升机器人长视野任务规划的推理与泛化能力，且小模型可通过方法优化超越大模型。
---

## 摘要
提高具身智能体的推理能力对于机器人在长视野操作任务中成功完成复杂的人类指令至关重要。尽管基于监督微调（SFT）的大语言模型和视觉语言模型在规划任务中取得了成功，但由于其有限的常识和推理能力，它们在复杂现实环境中执行长周期操作任务时仍面临挑战。考虑到通过监督微调将通用视觉语言模型对齐到机器人规划任务存在泛化性差和物理理解不足的问题，我们提出了RoboGPT-R1，一个用于具身规划的两阶段微调框架。在该框架中，监督训练通过专家序列获取基础知识，随后通过强化学习解决模型在视觉空间理解和推理方面的缺陷。为了在多步推理任务中实现物理理解和动作序列一致性，我们设计了一个基于规则的奖励函数，同时考虑长周期性能和环境中的动作约束。在Qwen2.5-VL-3B上训练的推理模型，在EmbodiedBench基准测试中显著优于更大规模的模型GPT-4o-mini，性能提升21.33%，并超过其他基于Qwen2.5-VL-7B训练的工作，性能提升20.33%。

## Abstract
Improving the reasoning capabilities of embodied agents is crucial for robots to complete complex human instructions in long-view manipulation tasks successfully. Despite the success of large language models and vision language models based on Supervised Fine-Tuning (SFT) in planning tasks, they continue facing challenges in performing long-horizon manipulation tasks in complex real-world environments, owing to their restricted common sense and reasoning capabilities. Considering that aligning general-purpose vision language models to robotic planning tasks via supervised fine-tuning suffers from poor generalization and insufficient physical understanding, we propose RoboGPT-R1, a two-stage fine-tuning framework for embodied planning. In this framework, supervised training acquires foundational knowledge through expert sequences, followed by RL to address the model's shortcomings in visual-spatial understanding and reasoning. To achieve physical understanding and action sequence consistency in multi-step reasoning tasks, we design a rule-based reward function that simultaneously considers long-horizon performance and action constraint in the environment. The reasoning model, trained on Qwen2.5-VL-3B, significantly outperforms the larger-scale model, GPT-4o-mini, by 21.33% and surpasses other work trained on Qwen2.5-VL-7B by 20.33% on the EmbodiedBench benchmark.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 当前视觉语言模型（VLM）在机器人长视野操作任务中，由于常识和推理能力不足，难以适应复杂真实环境。
- 仅基于监督微调（SFT）的范式主要模仿专家演示，缺乏动态环境下的自适应与自我纠错能力；现有的长周期奖励函数设计稀疏或与执行脱节，阻碍规划性能。
- 强化学习方法虽在数学、视频推理等领域有效，但转移到开放式的具身规划任务时，面临奖励函数设计困难（如简单字符串匹配会鼓励冗长且逻辑错误链）。
- 为此，提出 RoboGPT-R1：两阶段微调框架，通过 SFT 获取基础知识，再通过基于 GRPO 的强化学习提升视觉空间推理和动作序列一致性，克服 SFT 泛化差和物理理解不足的缺陷。

## 二、论文提出的方法论
- **核心思想**：采用两阶段训练范式——先进行监督微调（SFT）使模型具备基础规划能力，再使用 Group Relative Policy Optimization（GRPO）算法进行强化微调（RFT），让模型通过探索和自纠错提升推理能力。
- **数据准备**：使用基于 EmbodiedBench EB-ALFRED 任务蒸馏的 SFT 数据集（Base），以及 ALFRED 轨迹数据集扩充的 RFT 数据集（Aug），均采用 zero-shot 处理（去除示例），减少 token 消耗并避免模型过拟合。
- **关键技术细节**：
  - **SFT 阶段**：在 Base 数据集上全参数微调，使模型初步具备多步规划能力（约 1.5 小时）。
  - **RFT 阶段**：使用 GRPO 算法，采样 N 个候选响应，通过组内奖励归一化计算优势，优化策略参数。引入 KL 散度惩罚约束策略偏离。
- **奖励函数设计**（规则化、可验证）：
  - **格式奖励**（\(R_{format}\)）：由三部分组成：​**section 奖励**（检查是否包含四个必需字段）、​**type 奖励**（验证动作 id 和 name 格式）、​**有效性奖励**（检查动作 id-name 是否与预定义动作字典匹配）。权重：section 0.3, type 0.3, validity 0.4。
  - **精度奖励**（\(R_{lcs}\)）：基于最长公共子序列（LCS）计算预测与参考动作序列的匹配度，保持动作顺序一致性，优于严格逐前缀匹配。
  - **总奖励**：\(R = 0.2 \cdot R_{format} + 0.8 \cdot R_{lcs}\)。
- **算法流程**：GRPO 中，对每个问题采样 N 个输出，计算奖励均值标准差得到优势，按归一化裁剪目标优化，避免使用额外价值模型。

## 三、实验设计
- **基准与场景**：使用 EmbodiedBench 统一评价框架，包含两个子套件：
  - **EB-ALFRED**（室内场景、物体状态追踪、步骤依赖），视为域内测试。
  - **EB-Habitat**（3D 导航与交互，场景布局、动作语义差异大），视为域外泛化测试。
- **数据集**：SFT 阶段使用 Base 数据集（~5000 样本，含 4000+ 具身规划样本 + 其他任务样本）；RFT 阶段使用 Aug 数据集（~45000 样本，含全部 Base 数据）。
- **对比方法**：分为三类——
  - **通用闭源模型**：Gemini-2.0-flash、Qwen-VL-Max、GPT-4.1、GPT-4o、GPT-4o-mini。
  - **通用开源模型**：Llama-3.2-90B-Vision-Ins、InternVL2.5-8B、Gemma-3-12B-it、Qwen2.5-VL-72B/7B/3B-Ins。
  - **具身领域专有模型**：REBP、RoboBrain、TaPa、RoboGPT-R1（本文）。
- **评价指标**：成功率（%），涵盖六类子任务：基础（Base）、常见（Common）、复杂（Complex）、视觉（Visual）、空间（Spatial）、长周期（Long）。n_shots 在通用模型中使用最佳配置（10-shot），本文模型使用 0-shot。

## 四、资源与算力
- **SFT 阶段**：8 块 Ascend 910B3 64GB NPU，训练约 1.5 小时。
- **RFT 阶段**：4 块 NVIDIA H20 96GB GPU，训练约 25 小时，共 80 步迭代。
- **框架**：SFT 使用 LLaMA-Factory，RFT 使用 VERL（基于 GRPO 实现）。

## 五、实验数量与充分性
- **主实验**：在 EB-ALFRED 上 6 个子任务、域外 EB-Habitat 上 6 个子任务，对比 12+ 基线模型。
- **消融实验**：
  - **训练策略消融**：基模型（无微调）→ SFT 仅→ SFT+RFT，展示各阶段贡献。
  - **数据源消融**：仅 SFT with Base、仅 SFT with Aug、SFT+RFT with Base、SFT+RFT with Aug，证明 Aug 数据仅在 RFT 阶段有效。
  - **精度奖励对比**：步精确度、REBP 奖励、LCS 奖励（本文），固定其他条件，证明 LCS 优势（尤其在长周期任务上提升 24 个百分点）。
- **n-shots 影响分析**：对比通用模型 0/1/10-shot 表现，证明 0-shot 对通用模型完全失效，而本文模型适应 0-shot 且性能稳定。
- **失败案例分析**：提供可视化示例，分析多目标场景下模型注意力偏差问题。
- **充分性**：实验设计系统、对比方法全面、消融实验覆盖训练阶段、数据源和奖励设计，结论客观且可复现。

## 六、论文的主要结论与发现
- RoboGPT-R1（仅 3B 参数）在 EB-ALFRED 上平均成功率 55.33%，超越 GPT-4o-mini（34%）21.33%，超越同领域最佳 REBP（7B，35%）20.33%，接近 GPT-4.1（64.67%）。
- 在长周期任务上达到 50%，远超 REBP 的 6%。
- 在域外 EB-Habitat 上平均 22%，显著优于基模型 Qwen2.5-VL-3B（14.67%）和 REBP（18.33%），验证强化学习带来的泛化能力。
- SFT 建立基础规划能力，RFT 解决长周期推理瓶颈；近域数据仅在 RFT 中有效，SFT 单独使用效果差。
- LCS 奖励比步精确度和 REBP 奖励更适合具身规划，提供密集且顺序感知的信号。

## 七、优点
- **框架设计新颖**：将 SFT 与 GRPO 强化学习结合用于具身规划，克服 SFT 仅模仿的局限，有效激发推理能力；代码开源。
- **奖励函数精巧**：基于 LCS 的奖励保持动作顺序一致性，配合格式约束，提供密集、可验证的反馈；权重合理。
- **小参数高效**：3B 模型超越多个 7B/72B 开源模型及闭源模型 GPT-4o-mini，证明方法参数效率高，推理成本低。
- **实验严谨**：域内外双场景评估，消融实验解耦训练阶段、数据源和奖励组件，n-shots 控制变量分析，失败案例定性分析，确保结论可信。
- **零样本策略**：统一使用 zero-shot 训练和测试，减少 token 开销，避免示例干扰，提升泛化。

## 八、不足与局限
- **域外泛化仍有差距**：在 EB-Habitat 上（unseen 场景）相比 Qwen2.5-VL-72B 和 GPT-4.1 仍有显著差距（22% vs 50.33%/50.67%），说明面对大幅分布偏移时小模型能力有限。
- **仅仿真评估**：所有实验在模拟环境 EmbodiedBench 中进行，未在真实机器人上验证，存在 sim-to-real 鸿沟：状态估计误差、执行噪声等未被考虑。
- **失败案例分析显示特定缺陷**：多目标同类物体（如两个卷纸）时，模型易陷入局部循环，难以区分已完成与未完成的实例，体现多实例分辨和跨步状态跟踪的不足。
- **奖励设计依赖真实参考序列**：LCS 奖励需要已知的参考动作序列，在真实交互中无法直接获得，限制了在在线学习或无教师设置中的应用。
- **训练资源仍需一定规模**：虽然模型 3B，但 RFT 阶段需 4×H20 96GB GPU 训练 25 小时，对算力仍有需求。
- **未分析模型尺寸缩放规律**：仅基于 3B 模型实验，未探讨 7B 或更大模型在相同框架下的性能增益，可能限制结论通用性。

（完）
