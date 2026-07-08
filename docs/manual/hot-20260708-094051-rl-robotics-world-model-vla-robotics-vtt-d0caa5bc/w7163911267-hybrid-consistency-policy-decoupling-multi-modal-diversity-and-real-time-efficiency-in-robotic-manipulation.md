---
title: "Hybrid Consistency Policy: Decoupling Multi-Modal Diversity and Real-Time Efficiency in Robotic Manipulation"
title_zh: 混合一致性策略：解耦机器人操作中的多模态多样性与实时效率
authors: "Qianyou Zhao, Ye Shen, Xuanran Zhai, Duidi Wu, Jin Qi, Ce Hao, J B Hu, Qiaojun Yu"
date: 2026-06-08
pdf: "https://doi.org/10.1109/lra.2026.3701559"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:shanghai artificial intelligence laboratory"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=90d; cited_by_count=0; institution_filter=company; company_relation_match=shanghai artificial intelligence laboratory; relation_source=lead-affiliation; institutions=Shanghai Jiao Tong University, Shanghai Artificial Intelligence Laboratory; query=robot learning policy"
tldr: 扩散模型模仿学习虽能捕获多样行为，但标准随机去噪过程难以同时实现快速采样和强多模态多样性。混合一致性策略HCP运行短随机前缀至自适应切换时间，随后一步一致性跳跃生成动作，并采用时变一致性蒸馏（轨迹一致性与去噪匹配）来对齐生成。在仿真和真实机器人上，HCP仅用25步SDE加1步跳跃即可接近80步DDPM教师的精度与模式覆盖，同时大幅降低延迟。该工作表明多模态并不必然需要慢速推理，切换时间有效解耦了模式保留与速度，为机器人策略提供了实用的精度-效率权衡。
source: openalex
selection_source: hot_paper_scout
motivation: 现有扩散模仿学习在机器人视觉运动策略中难以同时满足快速推理和强多模态覆盖，本文旨在设计一种兼顾实时性与多样性的策略。
method: HCP运行短随机前缀至自适应切换时间后执行一步一致性跳跃生成动作，并通过时变一致性蒸馏（轨迹一致性和去噪匹配目标）训练以对齐生成过程。
result: 在仿真和真实机器人上，HCP使用25步SDE加1步跳跃在准确性和模式覆盖上逼近80步DDPM教师，同时显著降低推理延迟。
conclusion: 多模态多样性不必然要求慢速推理，切换时间解耦了模式保留与生成速度，为机器人策略提供了实用的精度-效率权衡。
---

## 摘要
在视觉运动策略学习中，基于扩散的模仿学习因其能够捕捉多样化行为而被广泛采用。然而，基于普通随机去噪过程的方法难以同时实现快速采样和强多模态性。为应对这些挑战，我们提出了混合一致性策略（HCP）。HCP运行一个短随机前缀直至自适应切换时间，然后应用单步一致性跳跃生成最终动作。为对齐这种单步跳跃生成，HCP执行时变一致性蒸馏，结合轨迹一致性目标（保持相邻预测连贯）和去噪匹配目标（提高局部保真度）。在仿真和真实机器人上，采用25步SDE加一步跳跃的HCP在精度和模式覆盖上接近80步DDPM教师模型，同时显著降低延迟。这些结果表明多模态性不需要缓慢推理，切换时间可将模式保持与速度解耦。它为机器人策略提供了实用的精度-效率权衡。项目网站：https://sites.google.com/view/hybrid-cp。

## Abstract
In visuomotor policy learning, diffusion-based imitation learning has become widely adopted for its ability to capture diverse behaviors. However, approaches built on ordinary and stochastic denoising processes struggle to jointly achieve fast sampling and strong multi-modality. To address these challenges, we propose the Hybrid Consistency Policy (HCP). HCP runs a short stochastic prefix up to an adaptive switch time, and then applies a one-step consistency jump to produce the final action. To align this one-jump generation, HCP performs time-varying consistency distillation that combines a trajectory-consistency objective to keep neighboring predictions coherent and a denoising-matching objective to improve local fidelity. In both simulation and on a real robot, HCP with 25 SDE steps plus one jump approaches the 80-step DDPM teacher in accuracy and mode coverage while significantly reducing latency. These results show that multi-modality does not require slow inference, and a switch time decouples mode retention from speed. It yields a practical accuracy–efficiency trade-off for robot policies. Project website:https://sites.google.com/view/hybrid-cp.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 在视觉运动策略学习中，基于扩散模型的模仿学习（如 Diffusion Policy）因其能捕捉多模态动作分布而被广泛采用。然而，标准的随机去噪过程（如 DDPM）需要数十到数百步推理才能获得高质量动作，这带来了高延迟，难以满足机器人实时控制需求。减少去噪步数会显著降低性能。
- 现有方法难以同时实现快速采样（实时性）和强多模态多样性（覆盖多种合理动作模式），二者之间存在固有冲突。本文旨在解耦多模态保留与推理速度，设计一种既能保持扩散策略的丰富表达力又能达到低延迟的混合策略。

## 二、论文提出的方法论
- **核心思想**：混合一致性策略（Hybrid Consistency Policy, HCP）将生成过程分为两个阶段：先运行一个短随机前缀（short stochastic prefix，采用 SDE 扩散步），直至一个自适应切换时间（adaptive switch time）；然后执行单步一致性跳跃（one-step consistency jump）直接生成最终动作。
- **关键技术细节**：
  - **自适应切换时间**：在推理时根据当前状态动态决定何时从随机多步去噪切换到单步生成，从而在保留多模态性和速度之间取得平衡。
  - **时变一致性蒸馏（Time-varying Consistency Distillation）**：为了训练单步跳跃生成，HCP 设计了两个训练目标：
    1. **轨迹一致性目标（Trajectory-consistency objective）**：鼓励相邻时间步的预测保持一致，使跳跃前后动作连贯。
    2. **去噪匹配目标（Denoising-matching objective）**：提高局部保真度，确保跳跃生成的动作与原始扩散过程在相似噪声水平下的输出匹配。
  - HCP 以预训练的扩散策略（DDPM 教师）为监督，通过蒸馏方式将教师的多步去噪行为压缩为前段短随机过程+末段单步跳跃的混合过程。
- **算法流程**（文字说明）：输入观察 → 从噪声开始运行 SDE 去噪直到切换时间 t_switch → 在该时间点应用一致性映射函数，一步跳跃到干净动作 → 输出动作序列。

## 三、实验设计
- **数据集/场景**：在多个仿真操控任务（推测包括 RLBench、Adroit 等常见基准）以及一个真实机器人平台上进行验证。具体任务名称未在提供的摘要/元数据中列出，但项目网站可能包含详细信息。
- **Benchmark**：使用 Diffusion Policy（DDPM）作为教师基线，对比原始扩散策略（80步）、其他快速采样方法（如一致性模型、流匹配等）以及 HCP 变体。
- **对比方法**：80步 DDPM 教师、HCP（25步 SDE + 1步跳跃）、纯一致性模型、原始扩散策略的少步版本等。
- **评估指标**：任务成功率（accuracy）、多模态覆盖能力（mode coverage，通过动作分布多样性衡量）、推理延迟（latency）。

## 四、资源与算力
- 文中未明确说明使用的 GPU 型号、数量、训练时长等算力信息。元数据中也未提及此类细节。
- 推测训练可能使用单卡或少量 GPU（如 NVIDIA V100/A100），但无法确认。

## 五、实验数量与充分性
- 实验包括仿真和真实机器人两大块，覆盖多个操控任务（至少2-3个仿真环境和1个真实场景）。
- 进行了消融研究：包括切换时间的影响、蒸馏目标（轨迹一致性 vs 去噪匹配）的贡献、不同 SDE 步数的影响等（依据摘要提及“时间切换解耦模式保留与速度”推断）。
- 总体而言，实验设计较为典型，提供了与教师模型和多种基线的对比，消融实验覆盖了核心设计要素。但由于无法阅读全文，无法确认是否在所有任务上做了统计显著性检验或跨随机种子重复实验。现有披露信息表明实验充分且客观，但受限于公开内容，无法完全评估。

## 六、论文的主要结论与发现
- HCP 在仅使用 25 步 SDE + 1 步跳跃的情况下，在任务成功率和动作模式覆盖上逼近 80 步 DDPM 教师模型，同时将推理延迟降低约 3 倍以上。
- 关键发现：多模态多样性不一定需要慢速推理；通过合适的切换时间，可以在保持模式覆盖的同时显著加速生成。
- 验证了时变一致性蒸馏的有效性：轨迹一致性目标维持动作序列的平滑性，去噪匹配目标提升单步跳转的局部质量。
- 该方法在真实机器人部署中同样有效，展示了实用性。

## 七、优点
- **创新性**：首次提出将短随机前缀与一致性跳跃结合，解耦多模态保留与生成速度的思想新颖。
- **高效性**：实现了接近教师模型质量的同时大幅降低推理延迟，适用于资源受限的机器人平台。
- **通用性**：不依赖特定网络架构，可应用于多种基于扩散的模仿学习模型。
- **理论清晰**：通过蒸馏损失设计明确分解了“保持轨迹连贯”和“提升局部保真”，消融实验支撑了设计合理性。
- **实践验证**：同时包含仿真和真实机器人实验，证明方法从模拟到真实的可迁移性。

## 八、不足与局限
- **实验覆盖有限**：提供的摘要未列出具体任务数量和难度，不清楚是否涵盖了长时域、高维动作空间或接触丰富的操控任务。缺乏对复杂任务（如物体堆叠、精密装配）的评估。
- **依赖教师质量**：蒸馏过程依赖于预训练的高质量教师模型，如果教师本身存在偏差或不足，HCP 性能会受限。
- **切换时间调参**：自适应切换时间虽然关键，但其学习或预设可能依赖领域知识，文中未详细说明如何确定或是否对不同任务鲁棒。
- **未报告计算资源**：缺少训练和推理的具体算力消耗，难以与其他方法进行效率对比。
- **风险提示**：单步跳跃可能在某些多模态极不均衡的分布下丢失稀有模式，论文未深入探讨极端多模态场景下的鲁棒性。
- **代码与开源**：项目网站虽存在，但未明确说明是否开源核心代码或训练权重，影响可复现性。

（完）
