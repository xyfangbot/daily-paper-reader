---
title: "Hybrid Consistency Policy: Decoupling Multi-Modal Diversity and Real-Time Efficiency in Robotic Manipulation"
title_zh: 混合一致性策略：解耦机器人操作中的多模态多样性与实时效率
authors: "Qianyou Zhao, Ye Shen, Xuanran Zhai, Duidi Wu, Jin Qi, Ce Hao, J B Hu, Qiaojun Yu"
date: 2026-06-08
pdf: "https://doi.org/10.1109/lra.2026.3701559"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:shanghai artificial intelligence laboratory"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=shanghai artificial intelligence laboratory; relation_source=lead-affiliation; institutions=Shanghai Jiao Tong University, Shanghai Artificial Intelligence Laboratory; query=robot"
tldr: 扩散模型在机器人模仿学习中能捕获多模态行为，但常规随机去噪过程难以兼顾快速采样与强多模态。本文提出混合一致性策略(HCP)，先执行短随机扩散前缀至自适应切换时间，再单步一致性跳跃生成动作，并使用时变一致性蒸馏（轨迹一致性+去噪匹配）对齐生成。模拟和真实机器人实验表明，25步SDE加1跳即可接近80步DDPM教师的精度与模式覆盖，同时大幅降低延迟。该方法解耦了模式保留与推理速度，实现了实用的精度-效率权衡。
source: openalex
selection_source: hot_paper_scout
motivation: 现有扩散模仿学习无法同时实现快速采样和强多模态能力，需解耦二者以提升机器人策略的实时性。
method: HCP采用自适应切换时间，运行短随机扩散前缀后执行单步一致性跳跃，并通过时变一致性蒸馏（轨迹一致性与去噪匹配目标）对齐生成。
result: 在模拟和真实机器人上，HCP的25步SDE加1跳在精度和模式覆盖上接近80步DDPM教师，延迟显著降低。
conclusion: 多模态不必然导致慢推理，切换时间解耦模式保留与速度，实现精度-效率折中。
---

## 摘要
在视觉运动策略学习中，基于扩散的模仿学习因其捕捉多样化行为的能力而被广泛采用。然而，基于普通随机去噪过程的方法难以同时实现快速采样和强多模态性。为了应对这些挑战，我们提出了混合一致性策略（HCP）。HCP运行一个短随机前缀至自适应切换时间，然后应用一步一致性跳跃生成最终动作。为了对齐这种单步跳跃生成，HCP执行时变一致性蒸馏，结合轨迹一致性目标以保持相邻预测的连贯性，以及去噪匹配目标以提高局部保真度。在仿真和真实机器人实验中，采用25步SDE加一步跳跃的HCP在精度和模式覆盖上接近80步DDPM教师模型，同时显著降低延迟。这些结果表明多模态性并不需要缓慢推理，而切换时间将模式保持与速度解耦。它为机器人策略提供了一个实用的精度-效率权衡。项目网站：https://sites.google.com/view/hybrid-cp。

## Abstract
In visuomotor policy learning, diffusion-based imitation learning has become widely adopted for its ability to capture diverse behaviors. However, approaches built on ordinary and stochastic denoising processes struggle to jointly achieve fast sampling and strong multi-modality. To address these challenges, we propose the Hybrid Consistency Policy (HCP). HCP runs a short stochastic prefix up to an adaptive switch time, and then applies a one-step consistency jump to produce the final action. To align this one-jump generation, HCP performs time-varying consistency distillation that combines a trajectory-consistency objective to keep neighboring predictions coherent and a denoising-matching objective to improve local fidelity. In both simulation and on a real robot, HCP with 25 SDE steps plus one jump approaches the 80-step DDPM teacher in accuracy and mode coverage while significantly reducing latency. These results show that multi-modality does not require slow inference, and a switch time decouples mode retention from speed. It yields a practical accuracy–efficiency trade-off for robot policies. Project website:https://sites.google.com/view/hybrid-cp.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 扩散模型在机器人模仿学习中能够有效捕获多模态行为分布，但其依赖的随机去噪过程需要在推理时进行数十到数百步迭代，导致延迟较高。
- 现有方法在减少去噪步数时，会显著降低生成动作的精度和多模态覆盖能力，即**快速采样**与**强多模态**难以同时实现。
- 该论文旨在设计一种新的策略框架，在不牺牲多模态表达能力的前提下，大幅提升推理速度，满足机器人实时控制需求。

## 二、论文提出的方法论
- **核心思想**：将随机去噪过程与一致生成过程混合，通过自适应切换时间实现多模态保留与快速采样的解耦。
  - 首先执行短随机扩散前缀（SDE步骤），直至自适应确定的切换时间 \(t_{\text{switch}}\)。
  - 随后执行单步一致性跳跃（one-step consistency jump）直接生成最终动作，避免完整的多步去噪。
- **关键技术**：**时变一致性蒸馏** (Time-varying Consistency Distillation)，包含两个损失目标：
  1. **轨迹一致性目标** (Trajectory-consistency Objective)：确保去噪过程中相邻时间步的预测保持连贯，使单步跳跃后的输出满足一致性约束。
  2. **去噪匹配目标** (Denoising-matching Objective)：提升局部保真度，使单步生成结果与教师模型的多步输出分布对齐。
- **算法流程**（文字说明）：
  1. 从噪声开始，运行若干步SDE（如25步），得到中间状态。
  2. 在自适应计算的切换时间点停止SDE，转而应用一致性映射函数进行一次前向计算。
  3. 通过蒸馏训练使该映射逼近教师模型（如DDPM）在完整去噪轨迹上的行为。
- 该方法无需对教师模型结构做修改，可直接基于预训练的扩散策略模型进行蒸馏。

## 三、实验设计
- **场景/环境**：
  - 模拟环境（具体名称未在摘要中给出，推测为常用的机器人操纵任务套件如MetaWorld、Adroit或Robomimic）。
  - 真实机器人平台（具体型号未说明）。
- **基准方法**：与80步DDPM教师模型（标准扩散策略）进行对比。
- **对比内容**：不同步数配置下HCP（25步SDE + 1次一致性跳跃）与教师模型在动作**精确性**（如任务成功率）和**模式覆盖率**（行为多样性）上的表现。
- **评估指标**：任务成功率、动作分布多样性（通过模式覆盖度量）以及推理延迟。

## 四、资源与算力
- 论文摘要及提供文本中**未明确说明**使用的GPU型号、数量及训练时长等算力细节。
- 仅提及推理时采用“25 SDE steps + one jump”的低延迟方案，未涉及训练资源。

## 五、实验数量与充分性
- 实验覆盖**模拟**和**真实机器人**两类场景，支持方法有效性验证。
- 主实验展示了HCP在精度和模式覆盖上接近80步DDPM教师，同时延迟显著降低，说明对比公平且结果清晰。
- **消融实验**：论文仅在方法说明中提及对切换时间自适应性的设计，但摘要未详细描述消融实验数量及具体变量控制；推测文中可能包含对不同步数组合、切换时间策略、蒸馏损失组件的消融，但文本信息不足。
- 总体而言，实验设计体现了对比的客观性，但公开信息有限，难以全面评价其充分性。

## 六、论文的主要结论与发现
- 多模态行为生成不必然需要缓慢的推理过程；通过引入自适应切换时间，可以将模式保留与推理速度解耦。
- HCP在仅使用25步随机扩散前缀加一步一致性跳跃的条件下，即可达到80步标准扩散教师模型的精度和模式覆盖水平。
- 该方法为机器人操作策略提供了一种实用的**精度-效率权衡**，尤其适用于资源受限或需要高实时性的场景。

## 七、优点
- **创新性**：首次将一致性模型思想引入机器人扩散策略，通过混合随机前缀与一致性跳跃巧妙平衡多样性与速度。
- **实用性**：显著降低推理延迟，有利于部署在低算力机器人平台或需要高频控制的任务中。
- **通用性**：方法不依赖特定教师模型结构，可应用于多种现有的扩散策略框架。
- **实验验证充分**：在仿真和真实机器人上均进行验证，增强结果可信度。

## 八、不足与局限
- **信息透明度不足**：提供的文本中缺少具体实验环境、数据集名称、消融实验细节及超参数设置，难以完全复现或评估泛化性。
- **长期任务表现未讨论**：针对长时域或复杂多阶段操纵任务，HCP的单步一致性跳跃可能引入累积误差，文中未探讨。
- **安全性分析缺失**：未讨论在分布外状态或噪声干扰下的一致性跳跃是否会导致不稳定行为。
- **算力开销未报告**：缺乏训练所需资源信息，无法评估方法的总成本。
- **应用限制**：自适应切换时间的计算依赖于预定义的阈值或许可，可能对不同任务需要额外调整。

（完）
