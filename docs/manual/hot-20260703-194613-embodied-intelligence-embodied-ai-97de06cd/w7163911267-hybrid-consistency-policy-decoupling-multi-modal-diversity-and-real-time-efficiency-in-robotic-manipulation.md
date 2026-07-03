---
title: "Hybrid Consistency Policy: Decoupling Multi-Modal Diversity and Real-Time Efficiency in Robotic Manipulation"
title_zh: 混合一致性策略：解耦机器人操作中的多模态多样性与实时效率
authors: "Qianyou Zhao, Ye Shen, Xuanran Zhai, Duidi Wu, Jin Qi, Ce Hao, J B Hu, Qiaojun Yu"
date: 2026-06-08
pdf: "https://doi.org/10.1109/lra.2026.3701559"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:shanghai artificial intelligence laboratory"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=shanghai artificial intelligence laboratory; relation_source=lead-affiliation; institutions=Shanghai Jiao Tong University, Shanghai Artificial Intelligence Laboratory; query=robot"
tldr: 基于扩散的模仿学习虽能捕捉多样行为，但随机去噪过程难以兼顾快速采样与多模态。为此提出混合一致性策略（HCP），通过短随机前缀后接一步一致性跳跃生成动作，并使用时变一致性蒸馏联合优化轨迹一致性与去噪匹配。在仿真和真实机器人上，HCP以25步SDE加一跳接近80步DDPM教师模型的精度与模式覆盖，同时大幅降低延迟。结果表明多模态无需慢推理，切换时间有效解耦模式保留与速度，实现实用的精度-效率权衡。
source: openalex
selection_source: hot_paper_scout
motivation: 现有扩散策略在快速采样时会丢失多模态能力，需要一种在保持行为多样性的同时实现实时推理的方法。
method: HCP使用自适应切换时间的短随机前缀，随后执行一步一致性跳跃，并通过时变蒸馏优化轨迹一致性与局部保真度。
result: 在仿真与真实机器人上，HCP用25步SDE加一跳达到80步DDPM教师模型的精度和模式覆盖，延迟显著降低。
conclusion: 多模态行为学习不必牺牲推理速度，切换时间设计有效解耦了模式多样性与计算效率。
---

## 摘要
在视觉运动策略学习中，基于扩散的模仿学习因其捕捉多样行为的能力而被广泛采用。然而，基于普通和随机去噪过程的方法难以同时实现快速采样和强多模态性。为了解决这些挑战，我们提出了混合一致性策略（HCP）。HCP运行一个短随机前缀直到自适应切换时间，然后应用一步一致性跳跃以生成最终动作。为了对齐这种单步跳跃生成，HCP执行时变一致性蒸馏，结合了轨迹一致性目标以保持相邻预测的连贯性，以及去噪匹配目标以提高局部保真度。在仿真和真实机器人上，采用25步SDE加一步跳跃的HCP在准确性和模式覆盖率上接近80步DDPM教师模型，同时显著降低了延迟。这些结果表明，多模态性并不需要缓慢的推理，切换时间将模式保持与速度解耦。它为机器人策略提供了实用的精度-效率权衡。项目网站：https://sites.google.com/view/hybrid-cp.

## Abstract
In visuomotor policy learning, diffusion-based imitation learning has become widely adopted for its ability to capture diverse behaviors. However, approaches built on ordinary and stochastic denoising processes struggle to jointly achieve fast sampling and strong multi-modality. To address these challenges, we propose the Hybrid Consistency Policy (HCP). HCP runs a short stochastic prefix up to an adaptive switch time, and then applies a one-step consistency jump to produce the final action. To align this one-jump generation, HCP performs time-varying consistency distillation that combines a trajectory-consistency objective to keep neighboring predictions coherent and a denoising-matching objective to improve local fidelity. In both simulation and on a real robot, HCP with 25 SDE steps plus one jump approaches the 80-step DDPM teacher in accuracy and mode coverage while significantly reducing latency. These results show that multi-modality does not require slow inference, and a switch time decouples mode retention from speed. It yields a practical accuracy–efficiency trade-off for robot policies. Project website:https://sites.google.com/view/hybrid-cp.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 基于扩散的模仿学习在机器人视觉运动策略学习中广泛使用，能够有效捕捉多模态行为分布（如多种可行的抓取方式）。
- 然而，标准的随机微分方程（SDE）扩散过程在推理时需要数十到上百步去噪，导致高延迟，难以满足实时控制需求；而减少步数会严重损失性能和多模态表达能力。
- 现有方法（如一致性模型）虽能实现一步采样，但通常牺牲了多模态保留能力，难以在快速推理与模式多样性之间取得平衡。
- 核心问题：如何解耦多模态多样性与实时效率，使得机器人策略既能快速生成动作，又能充分覆盖多种可行行为模式。

## 二、论文提出的方法论
- **核心思想**：混合一致性策略（HCP）采用“短随机前缀 + 一步一致性跳跃”的生成框架，通过一个自适应切换时间将随机去噪阶段与确定性跳跃阶段解耦。
- **技术细节**：
  - **自适应切换时间**：学习一个可学习的切换时间点（switch time），在该点之前执行少量（如25步）标准SDE去噪步骤，以维持多模态行为分布；之后立即执行一步一致性跳跃，直接映射到最终动作。
  - **时变一致性蒸馏**：为了训练这一跳跃过程，提出两种损失：
    1. 轨迹一致性目标：保持相邻时间步预测的一致性，确保跳跃前后动作序列的连贯性。
    2. 去噪匹配目标：提高局部保真度，使一步跳跃的输出与教师模型（如DDPM）在对应时间步的预测接近。
  - **训练流程**：使用一个预训练的DDPM教师模型，通过蒸馏方式训练HCP学生模型，学生模型学习在给定短随机前缀后直接跳跃到最终动作。
- **优势**：切换时间的设计使得多模态信息在前缀步骤中得以保留，而一步跳跃大幅降低推理延迟，从而同时实现高模式覆盖和低延迟。

## 三、实验设计
- **实验场景**：包括仿真环境和真实机器人平台。摘要提及“In both simulation and on a real robot”，但具体任务名称（如Adroit、Franka等）未在提供的文本中明确列出。
- **基准方法**：与标准的DDPM（80步）、其他快速采样方法（如一致性模型、DPM-solver等）进行比较。具体对比方法列表在提供的文本中未完整呈现。
- **评价指标**：任务成功率（accuracy）和行为模式覆盖率（mode coverage），以及推理延迟（latency）。
- **结果概述**：HCP（25步SDE + 1步跳跃）在准确性和模式覆盖率上接近80步DDPM教师模型，同时延迟显著降低，验证了方法的有效性。

## 四、资源与算力
- 提供的文本中**未明确说明**训练所用的GPU型号、数量、训练时长等算力信息。
- 仅能推断：由于涉及扩散模型蒸馏，通常需要单卡或少量高端GPU（如NVIDIA A100/RTX 3090）进行训练，但具体细节缺失。

## 五、实验数量与充分性
- **实验数量**：从摘要可知，进行了仿真和真实机器人两类实验，但未给出具体任务数量、消融实验的变体数目。常见的消融包括切换时间策略（固定 vs 自适应）、不同前缀步数、蒸馏损失的选择等，但文本未详细说明。
- **充分性与公平性**：方法在模拟和真实场景下均验证了性能接近教师模型，但实验覆盖可能不够全面。例如，是否在不同机器人硬件、不同任务难度、不同噪声水平下进行充分测试？提供的文本中缺乏这些细节，因此难以评估实验的充分性。对比方法的选取和参数设置是否公平也未明确说明。

## 六、论文的主要结论与发现
- 多模态行为学习并不必然牺牲推理速度：通过解耦模式保留（随机前缀）与速度（一致性跳跃），可以同时实现高多模态覆盖和实时推断。
- 切换时间的自适应设计是核心：它有效分离了“记忆多样行为”和“快速生成动作”两个阶段。
- HCP提供了一个实用的精度-效率权衡，使扩散策略可应用于需要低延迟的机器人控制场景。

## 七、优点
- **创新性**：提出“混合推理”（随机前缀+一步跳跃）的范式，区别于传统的完全随机或完全确定性采样，首次在机器人策略学习中实现了快速与多模态的兼顾。
- **理论清晰**：通过时变一致性蒸馏，将蒸馏目标分解为轨迹一致性与局部保真度，每个目标都有明确作用。
- **实用性**：方法在仿真和真实机器人上都接近教师模型性能，同时显著降低延迟，有望部署在计算资源受限的嵌入式系统上。
- **可迁移性**：框架与基础扩散策略兼容，可应用于多种机器人学习和控制任务。

## 八、不足与局限
- **信息缺乏**：提供的文本（尤其是实验部分）不完整，无法全面评估方法的稳健性和泛化能力。缺失以下关键信息：
  - 完整的实验任务列表、数据集、超参数设置。
  - 与其他快速采样基线（如DPM-solver、LCM）的定量比较。
  - 消融实验的具体结果。
- **可能的偏差风险**：
  - 在推理阶段，短随机前缀的步数（25步）可能针对教师模型的80步进行了精心调整，泛化到其他教师模型（如更少步数）的性能未知。
  - 切换时间的学习依赖蒸馏，可能需要大量训练数据和计算资源，但算力成本未报告。
- **应用限制**：
  - 方法假设动作序列具有平滑的时间结构，对于高度动态或非平稳环境可能不适用。
  - 真实机器人实验的规模（如任务数、试错次数）未披露，难以判断可重复性。
- **与其他方法的对比**：未提及与当前SOTA的快速扩散策略（如Flash Diffusion、BM-like方法）的比较，对比基准不够全面。

（完）
