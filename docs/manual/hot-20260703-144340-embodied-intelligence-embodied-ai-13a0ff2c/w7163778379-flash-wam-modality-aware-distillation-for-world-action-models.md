---
title: "Flash-WAM: Modality-Aware Distillation for World Action Models"
title_zh: "Flash-WAM: 面向世界动作模型的模态感知蒸馏"
authors: "Arman Akbari, Zhang Ci, Arash Akbari, Lin Zhao, Yixiao Chen, Weiwei Chen, Xuan Zhang (56049), Geng Yuan, Yanzhi Wang"
date: 2026-06-03
pdf: "https://arxiv.org/pdf/2606.05254"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=generalist robot policy"
tldr: "世界动作模型通过迭代扩散联合生成视频和动作，但多步去噪导致推理延迟过高，无法用于实时控制。现有步数蒸馏方法因视频与动作流噪声调度不对称而失效。本文提出Flash-WAM，一种模态感知的蒸馏框架：为低噪声的动作流采用线性梯度缩放参数化，为高噪声的视频流采用方差保持参数化，将推理压缩为单步。在LingBot-VA上，延迟从8.1秒降至348毫秒（23倍加速），在仿真基准上保持85.5%和95.7%的成功率，真实世界性能恢复至60%，而朴素一致性蒸馏仅24%。Flash-WAM首次实现实时世界动作模型，解决了多模态蒸馏中的不对称问题。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有步数蒸馏方法无法处理视频与动作流噪声分布不对称，导致联合视频-动作模型推理速度无法满足实时控制需求。
method: 提出模态感知蒸馏框架Flash-WAM，基于一致性蒸馏为动作流选择线性梯度缩放参数化，为视频流选择方差保持参数化，匹配各自的噪声区间。
result: "将推理压缩到每模态单步，延迟从8.1秒降至348毫秒（23倍加速），在RoboTwin 2.0和LIBERO上保持85.5%和95.7%成功率，真实世界性能达60%。"
conclusion: Flash-WAM通过模态感知的蒸馏设计实现了实时世界动作模型，大幅提升推理速度且不牺牲性能，为机器人实时控制提供了可行方案。
---

## 摘要
世界动作模型（WAMs）通过迭代扩散联合生成未来视频和机器人动作，在操作基准测试中取得了强劲性能，但需要数十步去噪，这一成本阻碍了实时控制。步蒸馏已成为自然解决方案，但现成方法在联合视频-动作设置中失效，因为视频和动作流使用不同的信噪比偏移噪声调度，并且在训练时具有显著不同的边际噪声分布，这种非对称性是单模态蒸馏方法无法适应的。我们提出**Flash-WAM**，一种受一致性蒸馏启发的模态感知步蒸馏框架，为每个模态选择与其噪声状态匹配的一致性函数：针对动作流低噪声状态的线性梯度缩放参数化，结合针对视频流高噪声状态的方差保持参数化，这一切基于对一致性函数族的结构分析，该分析刻画了在一致性边界条件下可实现的梯度缩放。在LingBot-VA上实例化后，Flash-WAM将每个模态的推理压缩到单步。在RoboTwin 2.0上，这使得每块延迟从8.1秒降至在NVIDIA L40S上的348毫秒，实现了23倍的加速，支持实时推理。Flash-WAM在仿真基准测试中保持了任务成功率（RoboTwin 2.0为85.5%，LIBERO为95.7%），并在真实世界中大幅恢复性能（Unitree G1人形机器人平均60%），而在相同步预算下，朴素一致性蒸馏降至24%。

## Abstract
World-action models (WAMs) jointly generate future video and robot actions through iterative diffusion, achieving strong performance on manipulation benchmarks but requiring tens of denoising steps, a cost that precludes real-time control. Step distillation has emerged as the natural remedy, but off-the-shelf methods break down in the joint video-action setting because video and action streams use different SNR-shifted noise schedules and reach training with substantially different marginal noise distributions, an asymmetry that single-modality distillation methods cannot accommodate. We introduce \textbf{Flash-WAM}, a modality-aware step-distillation framework inspired by consistency distillation that selects the consistency function for each modality to match its noise regime: a linear-gradient-scaling parametrization for the action stream's low-noise regime, paired with a variance-preserving parametrization for the video stream's high-noise regime, grounded in a structural analysis of the consistency-function family that characterizes the achievable gradient scaling under the consistency boundary condition. Instantiated on LingBot-VA, Flash-WAM compresses inference to a single step in each modality. On RoboTwin 2.0, this reduces per-chunk latency from $8.1$ seconds to $348$ ms on NVIDIA L40S, a $23{\times}$ speedup that enables real-time inference. Flash-WAM preserves task success on simulation benchmarks ($85.5\%$ RoboTwin 2.0, $95.7\%$ LIBERO) and substantially recovers real-world performance ($60\%$ average on a Unitree G1 humanoid robot), while naive consistency distillation drops to $24\%$ at the same step budget.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 世界动作模型（WAMs）通过迭代扩散联合生成未来视频和动作序列，在操作任务上表现优异，但需要数十步去噪步骤（如LingBot-VA每块25视频步+50动作步），导致单块推理延迟高达8.1秒（NVIDIA L40S），无法满足实时控制需求（目标约500ms内）。
- 步蒸馏是自然解决方案，但现成的单模态蒸馏方法（如一致性蒸馏LCM）在联合视频-动作设置中失效。根本原因在于视频流和动作流使用了不同的信噪比偏移噪声调度（视频高偏移，动作低偏移），导致两者在训练时具有显著不同的边际噪声分布：视频集中在高噪声区，动作分散在低噪声区。标准一致性函数在低噪声区梯度信号随σ二次方消失（|b(σ)|=O(σ²)），使动作流得不到有效学习信号，造成任务成功率从91%骤降至24%。
- 因此，迫切需要一种能处理模态间噪声不对称性的蒸馏框架，在不牺牲性能的前提下大幅降低推理延迟。

## 二、论文提出的方法论
- **核心思想**：模态感知蒸馏（Flash-WAM），基于一致性蒸馏框架，为每个模态选择不同的一致性函数参数化，以匹配其噪声区间，确保在每个模态的训练集中都能提供足够的梯度信号。
- **关键技术细节**：
  - 动作流：采用线性梯度缩放参数化 `f_a(x_aσ, σ) = x_aσ - σ·v_θ(x_aσ, σ)`。该形式满足边界条件（a(0)=1, b(0)=0）且b′(0)≠0，达到最优线性梯度缩放（|b(σ)|=σ），在低噪声区提供非零梯度。
  - 视频流：采用标准LCM（Karras）参数化，即方差保持形式 `f_v(x_vσ, σ) = c_skip(σ)x_vσ + c_out(σ)ẑ_0`。该形式在高噪声区具有良好的稳定性（输出方差一致、有界），适合视频的高噪声训练分布。
  - 联合训练目标：视频和动作各自计算一致性损失（Huber损失），加权求和 `L = L_v + λ_a L_a`。教师模型使用有分类器引导的欧拉步生成目标，学生通过EMA目标训练。
  - 理论支撑：Proposition 1 证明在σ→0时，任何一致性函数可达到的最佳梯度缩放为线性（b=O(σ)），而LCM仅达到二次（O(σ²)），这解释了动作流训练信号消失的原因。

## 三、实验设计
- **仿真基准**：
  - RoboTwin 2.0：50个双手机械臂操作任务，分Clean（固定配置）和Randomized（随机扰动）两个评估设置。
  - LIBERO：四个任务套件（Spatial、Object、Goal、Long-horizon），每个套件500个演示。
- **真实世界评估**：Unitree G1人形机器人搭配Dex1-1夹爪，三个操作任务（开锅盖放土豆、挑红色瓶子（有黄色干扰物）、捡粉色物体放标记位置），各任务50个遥操作演示，每方法10次独立 rollout。
- **对比方法**：
  - 未加速教师：LingBot-VA（25v/50a 或 20v/50a）。
  - 蒸馏基线：Naive Joint LCM（视频和动作均用LCM参数化）、Video-only LCM（只蒸馏视频）、Video-only LCM+reg（加入动作MSE正则）、DMD2（分布匹配蒸馏，有视频DMD2+reg和无联合DMD2两种变体）。
  - 外部VLA基准：π0、π0.5、X-VLA、Motus。
- **评估指标**：任务成功率（%），推理延迟（ms），加速比。

## 四、资源与算力
- **训练硬件**：4台NVIDIA H100 GPU。
- **训练时长**：
  - LIBERO微调：每套件4,000步，约24小时。
  - Flash-WAM蒸馏：2,000步，每套件约24小时。
  - RoboTwin采用相同训练配置（蒸馏2,000步，4×H100）。
- **推理测试硬件**：单张NVIDIA L40S GPU（用于延迟测量）。
- **超参数**：学习率5e-6，有效batch size 48（4×H100），EMA衰减0.995，Huber损失c=0.001，CFG范围[2.0,10.0]。

## 五、实验数量与充分性
- **实验数量丰富**：
  - RoboTwin上报告了50个任务的平均成功率，并按任务horizon（1/2/3步）和Clean/Randomized分别呈现；还列出了全部50个任务的详细每任务成功率（附录表8）。
  - LIBERO上报告了四个套件的成功率，以及1v/2a和1v/1a两种配置。
  - 真实世界三个任务，分别报告1v/2a和1v/1a设置。
  - 消融实验（Table 4）比较了五种蒸馏策略（含Flash-WAM、Naive Joint LCM、Video-only LCM、Video-only LCM+reg、Joint DMD2），按horizon分解。
  - 额外附录B比较了所有方法在1v/1a时的完整结果。
- **充分性与公平性**：
  - 所有基线共享相同训练数据、基模型和训练迭代数，仅蒸馏目标不同，保证公平。
  - 真实世界评估中控制NFE配置一致，且与未加速模型直接对比。
  - 实验覆盖了仿真和真实场景、不同难度任务、不同步预算，类型全面。

## 六、论文的主要结论与发现
- **Flash-WAM实现接近教师的性能**：1v/2a时RoboTwin 2.0平均85.5%（教师91.25%），LIBERO 95.7%（教师98.6%）；1v/1a时分别81.4%和95.1%。
- **实时推理**：延迟从8.1秒降至348ms（23倍加速），满足实时控制预算（<500ms）。
- **优于所有蒸馏基线**：Naive Joint LCM在1v/2a即降至24.0%，DMD2仅78.7%，Video-only LCM 78.8%；Flash-WAM在所有配置和horizon上显著领先。
- **真实世界验证**：Flash-WAM在1v/2a达到60%平均成功率（教师66.7%），远优于无蒸馏的40%和Video-only LCM的43.3%。
- **理论根源确认**：动作流低噪声区梯度不足是朴素蒸馏失败的根本原因；线性参数化有效克服。

## 七、优点
- **理论严谨**：通过分析一致性函数族的梯度缩放行为，首次从理论上解释多模态蒸馏失败的原因，并给出最优选择条件（Proposition 1）。
- **设计简洁有效**：无需额外网络或对抗训练，仅通过改变一致性函数的参数化形式即解决不对称问题，集成到现有流匹配框架中。
- **大幅加速**：23倍加速下几乎不损失性能，为WAM实时控制铺平道路。
- **广泛验证**：在多个仿真基准和真实机器人上进行了全面比较，包括消融和不同步预算，显示鲁棒性。
- **可复现性好**：基于开源LingBot-VA模型，附录提供了详细的超参数和基线实现细节。

## 八、不足与局限
- **仿真为主**：主要实验在仿真中进行，真实世界任务仅三个，且操控相对简单；更复杂、更真实场景的性能有待验证。
- **仅限于共享骨干架构**：当前框架针对视频和动作共享Transformer骨干的WAM设计，未扩展到多模型架构（如Motus的混合专家结构）。
- **理论分析不完整**：仅刻画了低噪声区（动作）的最优梯度缩放；高噪声区（视频）的理论分析未给出（如Proposition仅针对σ→0），框架依赖性经验选择（LCM参数化）而非理论最优。
- **不适用于分布匹配蒸馏**：本文仅讨论一致性蒸馏；DMD2等其他蒸馏方法的模态感知扩展需要进一步研究（论文附录C）。
- **算力需求仍较高**：蒸馏仍需4×H100训练24小时，对资源有限的团队可能不够友好；推理加速虽大但训练成本未降低。
- **泛化性未充分验证**：真实世界仅测试了Unitree G1，未在其他机器人平台（如Franka、Spot）上验证；跨体姿、跨场景的泛化能力未知。

（完）
