---
title: "MindClaw: Closed-Loop Embodied Mental-State Reasoning for Precision Intervention"
title_zh: MindClaw：面向精准干预的闭环具身心智状态推理
authors: "Ruoxuan Zhang, Qiaoqiao Wan, Zhengguang Wang, Chenghao Yu, Hongxia Xie, Jianlong Fu, Wen-Huang Cheng"
date: 2026-05-31
pdf: "https://arxiv.org/pdf/2606.01063"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:microsoft research"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=90d; cited_by_count=0; institution_filter=company; company_relation_match=microsoft research; relation_source=lead-affiliation; institutions=Microsoft Research Asia (China); query=robot foundation model"
tldr: 理论心智(ToM)对于人机辅助交互至关重要，但现有基准主要评估离线问答或最终动作预测，缺乏对闭环环境、信念更新和干预时机的测试。本文提出MindClaw框架，集成多源输入、信念记忆、具身认知触发技能、心理推理和动作生成，使得智能体能够在动态环境中适时输出有益动作，否则保持沉默。实验表明直接视觉语言模型基线难以校准干预时机，而MindClaw通过优化触发技能获得了最佳整体性能。该工作为构建闭环具身心理状态推理与精准干预提供了重要思路。
source: openalex
selection_source: hot_paper_scout
motivation: 现有ToM基准多评估离线问答，缺乏对闭环环境、信念更新和干预时机的全面测试。
method: MindClaw连接多源输入、信念记忆、具身认知触发技能、心理推理与动作生成，实现精确干预。
result: MindClaw在任务意识和干预校准上优于直接VLM基线，达到最佳整体性能。
conclusion: 触发技能优化对闭环具身ToM辅助至关重要，可实现适时干预而避免不必要的帮助。
---

## 摘要
心智理论（ToM）使得智能体能够对他人的信念、目标和意图进行推理，这对于以人为中心的具身辅助至关重要。现有的ToM基准测试推动了文本与多模态心智状态识别的发展，但它们大多评估离线问答或最终动作预测，并未充分测试具身智能体能否持续感知动态环境、更新针对特定主体的信念、判断何时需要推理，以及仅在帮助有效时进行干预。基于MindPower，我们将以机器人为中心的ToM推理扩展到实时闭环场景，并引入MindClaw——一个面向精准干预的具身心智状态推理框架。MindClaw整合了多源输入、信念记忆、具身认知触发技能、心智推理与动作生成，使智能体能够在适当时刻输出有帮助的行动，同时在无需干预时保持静默。实验表明，直接使用视觉语言模型（VLM）基线方法在任务感知与干预校准方面存在困难，而MindClaw实现了最佳整体性能，证明了触发技能优化对于闭环具身ToM辅助的重要性。

## Abstract
Theory of Mind (ToM) enables an agent to reason about another actor's beliefs, goals, and intentions, which is essential for human-centered embodied assistance. Existing ToM benchmarks have advanced text and multimodal mental-state recognition, but they mostly evaluate offline question answering or final action prediction. They do not fully test whether an embodied agent can stay connected to a changing environment, update actor-specific beliefs, decide when reasoning is needed, and intervene only when help is useful. Building on MindPower, we extend robot-centric ToM reasoning to a real-time closed-loop setting and introduce MindClaw, a framework for embodied mental-state reasoning with precision intervention. MindClaw connects multi-source inputs, belief memory, an embodied cognitive trigger skill, mental reasoning, and action generation, allowing the agent to output helpful actions at the right time while remaining silent when intervention is unnecessary. Experiments show that direct VLM baselines struggle with task awareness and intervention calibration, while MindClaw achieves the best overall performance, demonstrating the importance of trigger-skill optimization for closed-loop embodied ToM assistance.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有 Theory of Mind (ToM) 基准主要评估离线问答或最终动作预测，未测试具身智能体能否在动态环境中持续感知、更新信念、判断推理时机、仅在需要时进行精准干预。
- **背景**：心智理论（ToM）对以人为中心的具身辅助至关重要，但当前基准（如 MindPower）仍停留在静态视频到动作的生成，缺乏实时闭环交互能力。
- **整体含义**：提出 MindClaw，将机器人中心推理扩展为实时闭环场景，实现“精准干预”——只在必要时生成帮助，否则保持沉默，是构建有用且非侵入性具身助理的关键。

## 二、论文提出的方法论
- **核心思想**：构建闭环具身心智状态推理框架，通过触发技能（trigger）决定何时更新信念、进行心理推理、生成动作或不做任何操作，实现干预时机的精确控制。
- **关键技术细节**：
  - **任务定义**：在可执行环境中，智能体接收多源输入（静态视频、模拟器流、人类输入），维护包含信念表（visual_facts 和 actor_beliefs）的运行时状态，通过触发循环输出内部认知操作（如 belief_create、reasoning_run、action_run、noop）和最终机器人动作 at。
  - **架构**：三部分——多源输入接口、Claw Layer（包含 Engine、Adapter、Memory、Trigger）、Reasoning Layer（包含 Observation、Mental Reasoning、Action Generation）。
  - **Trigger 实现**：将触发建模为具身认知技能，输入上下文 xt = (ot, Bt-1, Ht-1, Ct)，输出操作元祖 zt = (vt, it, jt, lt)。技能通过收集正确/错误轨迹，由 LLM 总结规则，并按强偏好、偏好、负条件三类组织，推理时先确定性匹配强规则，否则由模型预测。
  - **操作空间**：包括 belief_create_visual_fact、belief_update_actor_belief、reasoning_run、action_run、noop 等八种原子操作，所有槽位必须从候选集合中选取。
- **算法流程**：输入窗口→结构化观察→触发选择内部操作→执行操作（更新信念或调用推理/动作生成）→输出机器动作（可能为 none）。遵循“观察先于触发、信念操作先于推理、心理推理先于动作”的原则。

## 三、实验设计
- **数据集/场景**：使用 MindPower Benchmark（590 个视频-文本示例），包含 False-Belief Correction 和 Implicit Goal Inference & Completion 两类任务。
- **评估指标**：Task Accuracy (TA)、Precision Intervention Accuracy (PIA)、Closed-loop/Action Satisfaction (CS)。
- **对比方法**：直接 VLM 基线，包括 GPT-5.4、Gemini 3.1 Pro、Qwen3-VL-4/8/30B、VideoLLaMA3-7B、InternVL3.5-8B、Video-R1、OneThinker、VideoAuto-R1 等。
- **实现细节**：Trigger 使用 Qwen3-4B，Observation、Mental Reasoning、Action Generation 使用 GPT-5.5。

## 四、资源与算力
- **未明确说明**：论文未提及训练模型所用的 GPU 型号、数量、训练时长或功耗等算力资源细节。仅提到使用了 Qwen3-4B 和 GPT-5.5 进行推理，并可能进行了监督微调（SFT），但硬件配置未披露。

## 五、实验数量与充分性
- **实验组数**：
  - 主实验（表 II）：对比 11 个基线模型，报告 TA、PIA、CS 三项指标。
  - 信念表消融（表 III）：两个模型在有/无信念表下的性能对比。
  - 触发技能消融（表 IV）：6 种配置（包括无技能、技能引导、SFT、SFT+技能等），报告总准确率和非 noop 准确率。
- **充分性**：实验设计较为充分，覆盖了主要基线和关键消融，验证了信念表和触发技能的必要性。但缺少在真实机器人或更多模拟环境（如 ThreeDWorld）上的在线实验，且仅使用了 MindPower 单一基准。整体公平性良好，基线选择广泛。

## 六、论文的主要结论与发现
- **直接 VLM 基线**在任务理解和干预校准上表现差（TA 接近 0，PIA 较低），说明视觉识别不足以决定干预时机。
- **MindClaw 取得最优综合性能**：TA=14.36%，PIA=36.63%，CS=100%，显著优于所有基线。
- **信念表消融**：移除信念表后性能大幅下降（Qwen3-4B 从 9.51% 降至 1.64%），表明显式信念记忆对于触发决策至关重要。
- **触发技能消融**：加入技能规则后总准确率从 46.51% 提升至 77.71%，非 noop 准确率从 9.05% 提升至 41.61%，结合 SFT 与技能（GPT-5.5 指导）达到最佳（89.71% ACC、64.14% 非 noop）。
- **结论**：闭环具身 ToM 辅助需要显式的触发技能来管理干预时机，而非端到端视频到动作映射。

## 七、优点
- **问题定义新颖**：从离线推理转变为实时闭环精准干预，填补了现有 ToM 基准空白。
- **方法设计精细**：将触发建模为具身认知技能，结合确定性规则与概率预测，兼具精确性与灵活性。
- **架构清晰模块化**：分离输入接口、Claw 层（控制）与 Reasoning 层（感知/推理/生成），便于诊断错误来源。
- **实验消融充分**：通过信念表、触发技能等多角度消融，有力验证了各组件贡献。
- **性能显著**：在 CS 达到 100% 的同时大幅提升 TA 和 PIA，证明干预时机控制不牺牲动作有效性。

## 八、不足与局限
- **实验覆盖有限**：仅在 MindPower 一个基准上评测，缺乏在真实机器人或更多虚拟环境（如 ThreeDWorld、VirtualHome 在线交互）中的验证。
- **评估指标改进空间**：TA 和 PIA 绝对值仍较低（最高 PIA 36.63%），表明闭环 ToM 任务极具挑战性，现有方法仍有较大提升空间。
- **通用性未验证**：触发技能集合针对特定任务收集，迁移到其他场景（如协作任务、多角色交互）的泛化能力未知。
- **算力信息缺失**：未报告训练/推理所需计算资源，影响可复现性和能效评估。
- **偏差风险**：技能规则由 LLM 总结，可能引入语言模型固有的偏见；实验仅使用两类任务，未能覆盖更丰富的 ToM 场景。

（完）
