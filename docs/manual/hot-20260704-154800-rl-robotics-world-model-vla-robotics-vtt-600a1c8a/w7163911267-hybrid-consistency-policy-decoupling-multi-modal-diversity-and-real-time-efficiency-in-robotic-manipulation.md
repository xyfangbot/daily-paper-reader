---
title: "Hybrid Consistency Policy: Decoupling Multi-Modal Diversity and Real-Time Efficiency in Robotic Manipulation"
title_zh: 混合一致性策略：解耦机器人操作中的多模态多样性与实时效率
authors: "Qianyou Zhao, Ye Shen, Xuanran Zhai, Duidi Wu, Jin Qi, Ce Hao, J B Hu, Qiaojun Yu"
date: 2026-06-08
pdf: "https://doi.org/10.1109/lra.2026.3701559"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:shanghai artificial intelligence laboratory"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=shanghai artificial intelligence laboratory; relation_source=lead-affiliation; institutions=Shanghai Jiao Tong University, Shanghai Artificial Intelligence Laboratory; query=robot learning policy"
tldr: 在机器人视觉运动策略学习中，扩散模型虽能捕获多模态行为但采样缓慢。为此提出混合一致性策略（HCP），先执行短随机扩散前缀，再在自适应切换时间后单步一致性跳跃生成动作，并通过时变一致性蒸馏联合轨迹一致性与去噪匹配目标进行训练。实验表明，HCP使用25步SDE加一跳即可接近80步DDPM教师模型在精度与模式覆盖上的表现，同时显著降低延迟。
source: openalex
selection_source: hot_paper_scout
motivation: 解决扩散策略在机器人模仿学习中快速采样与保持多模态行为之间的冲突。
method: 提出混合一致性策略，利用自适应切换时间结合随机前缀与一致性跳跃，并采用时变蒸馏对齐相邻预测与局部保真度。
result: 在仿真和真实机器人上，HCP用25步加一跳达到80步DDPM的精度和模式覆盖，延迟大幅降低。
conclusion: 多模态不需要慢推理，通过解耦模式保留与速度可实现实用的准确-效率权衡。
---

## 摘要
在视觉运动策略学习中，基于扩散的模仿学习因其捕捉多样化行为的能力而被广泛采用。然而，基于普通随机去噪过程的方法难以同时实现快速采样和强多模态性。为了解决这些挑战，我们提出了混合一致性策略（HCP）。HCP运行一个短随机前缀直到自适应切换时间，然后应用一步一致性跳跃来产生最终动作。为了对齐这种一步跳跃生成，HCP执行时变一致性蒸馏，结合了轨迹一致性目标（保持邻近预测的一致性）和去噪匹配目标（提高局部保真度）。在仿真和真实机器人上，采用25步SDE加一步跳跃的HCP在准确性和模式覆盖方面接近80步DDPM教师，同时显著降低延迟。这些结果表明，多模态性并不需要慢速推理，切换时间将模态保留与速度解耦。它为机器人策略提供了实用的精度-效率权衡。项目网站：https://sites.google.com/view/hybrid-cp.

## Abstract
In visuomotor policy learning, diffusion-based imitation learning has become widely adopted for its ability to capture diverse behaviors. However, approaches built on ordinary and stochastic denoising processes struggle to jointly achieve fast sampling and strong multi-modality. To address these challenges, we propose the Hybrid Consistency Policy (HCP). HCP runs a short stochastic prefix up to an adaptive switch time, and then applies a one-step consistency jump to produce the final action. To align this one-jump generation, HCP performs time-varying consistency distillation that combines a trajectory-consistency objective to keep neighboring predictions coherent and a denoising-matching objective to improve local fidelity. In both simulation and on a real robot, HCP with 25 SDE steps plus one jump approaches the 80-step DDPM teacher in accuracy and mode coverage while significantly reducing latency. These results show that multi-modality does not require slow inference, and a switch time decouples mode retention from speed. It yields a practical accuracy–efficiency trade-off for robot policies. Project website:https://sites.google.com/view/hybrid-cp.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 在视觉运动策略学习中，扩散模型（如扩散策略 DP）被广泛用于模仿学习，因其能够捕获多模态动作分布，具有强大的表达能力。
- 然而，标准扩散模型基于随机微分方程（SDE）进行迭代去噪，推理时通常需要数十到数百步才能生成高质量动作，导致延迟高、难以满足实时控制需求（尤其在资源受限平台上）。
- 现有方法在减少采样步数时，往往牺牲多模态多样性或精度，无法同时实现快速采样与强多模态保留。因此，论文旨在解耦“多模态多样性保持”与“实时推理效率”之间的矛盾。

## 二、论文提出的方法论
- **核心思想**：提出混合一致性策略（HCP），将采样过程分为两个阶段：先运行一个短随机扩散前缀（有限步SDE），然后在自适应切换时间后执行一步一致性跳跃（one-step consistency jump），直接生成最终动作。通过切换时间解耦模态保留（第一阶段）与速度（第二阶段）。
- **关键技术细节**：
  - 自适应切换时间：决定何时从精细去噪切换到单步跳跃，可动态调整以平衡精度与效率。
  - 时变一致性蒸馏（Time-varying Consistency Distillation）：为对齐单步跳跃生成，训练时联合优化两个目标：
    - 轨迹一致性目标：保持相邻时间步预测的连贯性。
    - 去噪匹配目标：提高局部保真度，使单步跳跃的输出更接近教师模型（如DDPM）的长期去噪结果。
  - 整体流程：给定观测，HCP先执行25步SDE去噪（随机前缀），再执行一步一致性跳跃输出最终动作序列。
- **公式/算法流程**（文字说明）：训练时，HCP通过蒸馏教师扩散模型（80步DDPM）的知识，学习一个从任意中间噪声状态到最终去噪状态的映射，并利用时变权重平衡两个损失。推理时，仅需25步随机采样加一步直接跳转，大幅减少计算量。

## 三、实验设计
- **数据集/场景**：
  - 仿真环境：具体任务和benchmark在摘要中未详细列出，但提及在仿真场景中进行了评估。
  - 真实机器人：在真实机器人平台上进行了实际部署验证。
- **基准/对比方法**：
  - 教师模型：80步DDPM（标准扩散模型，作为精度和多模态覆盖的上限）。
  - 对比方法：文中只明确提及与DDPM对比（80步 vs HCP 25步+1跳），未列出其他基线（如一致性模型、更少步数的扩散策略等）。可能更多细节在全文实验部分。
- **评估指标**：准确率、模式覆盖率、延迟（推理时间）。关键词强调“accuracy–efficiency trade-off”。

## 四、资源与算力
- 论文摘要及元数据中**未明确说明**使用的GPU型号、数量、训练时长等具体算力信息。可能在实际全文的实验设置部分有提及，但本次提供的文本片段不包含这些细节。建议查阅完整论文获取。

## 五、实验数量与充分性
- 从摘要可知，实验至少包含两个场景：仿真+真实机器人。但未给出具体任务数量、消融实验数量等。
- 关于消融实验：可能包括对比不同切换时间、不同步数前缀、不同蒸馏目标等，但摘要中未明确；文中只强调“HCP with 25 SDE steps plus one jump approaches the 80-step DDPM teacher”。
- **充分性评价**：实验覆盖了仿真和真实平台，验证了方法的有效性。但由于摘要篇幅有限，缺乏详细的统计结果（如多次运行的平均值、方差）、与其他先进方法的系统性对比（如快速扩散策略、一致性模型），因此实验的全面性和严谨性需要全文来确认。从现有信息看，实验是初步支撑论文主要论点的，但可能不够详尽。

## 六、论文的主要结论与发现
- 多模态多样性不需要慢速推理：通过解耦模态保留（随机前缀）与快速生成（一致性跳跃），可以在保持接近教师模型性能的同时大幅降低延迟。
- HCP在仿真和真实机器人上均验证了有效的精度-效率权衡，表明所提混合策略是实用的。
- 自适应切换时间和时变一致性蒸馏是性能的关键：前者平衡模式覆盖与速度，后者保证单步跳跃的质量。

## 七、优点
- **创新性**：提出混合采样框架，将一致性模型与扩散SDE结合，巧妙利用切换时间解耦矛盾。
- **实用性**：在保持多模态表达能力的同时显著提升推理速度，适合部署到计算资源有限的机器人平台。
- **蒸馏方法**：时变一致性蒸馏联合轨迹一致性与去噪匹配，为单步跳跃提供了有效的训练信号，相比直接缩减步数更鲁棒。
- **项目开源**：提供了项目网站，便于验证与复现。

## 八、不足与局限
- **实验细节缺失**：从摘要中无法得知具体的benchmark任务种类、环境复杂度、对比基线数量，以及是否与当前最先进的快速策略（如Consistency Models、Rectified Flow等）进行公平比较。
- **算力和训练成本未披露**：训练HCP需要蒸馏教师模型，教师模型（80步DDPM）本身计算成本较高，论文未讨论训练总成本。
- **可能偏差**：切换时间的自适应机制如何确定？是否存在规律或需要手动调参？文中未说明。
- **应用限制**：HCP假设任务可离线收集多模态数据，且蒸馏需要预先训练好的高步数教师，对于数据稀缺或需要在线学习的场景可能受限。
- **可扩展性**：未讨论在长时域任务、高维动作空间或复杂接触任务上的表现，仅以简单或中等难度任务验证。

（完）
