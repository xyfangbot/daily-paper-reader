---
title: Steering Generative Reinforcement Learning into Stable Robotic Controller
title_zh: 将生成式强化学习引导至稳定的机器人控制器
authors: "Yixuan Wang, Shutong Ding, Ke Hu, Tianxiang Gui, Yi-Xiang Wang, Y Shi"
date: 2026-06-15
pdf: "https://arxiv.org/pdf/2606.16572"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 扩散/流式生成策略在强化学习中可诱导随机探索，但其动作随机性导致高维机器人控制不稳定、运动不一致。为此提出SteerGenPO框架，用学习到的潜在确定性actor替换生成策略的随机潜在采样，实现训练时随机探索与部署时稳定控制的分离。在六个Isaac Lab基准和Unitree G1运动任务上，SteerGenPO不仅超越经典强化学习与生成式强化学习基线，且确定性引导产生更平稳的推理行为和更可靠的命令响应。该方法为生成式策略在机器人精确控制中的实际应用提供了有效途径。
source: openalex
selection_source: hot_paper_scout
motivation: 扩散策略的随机性导致高维机器人动作累积不一致和鲁棒性降低，亟需将生成式策略转化为稳定确定性控制器以兼顾探索与精确控制。
method: 提出SteerGenPO，通过学习一个状态相关的潜在actor来替代训练好生成策略中的随机潜在采样，从而在部署时输出确定性潜在输入进行稳定控制。
result: 在六个Isaac Lab基准和Unitree G1运动任务上，SteerGenPO在回报和稳定性上均超过经典RL和生成RL基线，且推理行为更一致、命令响应更可靠。
conclusion: 潜在空间中的确定性引导有效将生成式强化学习转化为稳定鲁棒的机器人控制器，解决了随机生成策略在精确控制中的固有缺陷。
---

## 摘要
基于扩散和流的生成式策略通过迭代动作生成引发丰富的随机探索，为强化学习提供了强大的策略类。然而，扩散策略的随机性并不适用于高维机器人系统中的稳定和精确控制，因为微小的动作变化可能累积成不一致的运动并降低鲁棒性。为解决此问题，我们提出了SteerGenPO，一种潜空间强化学习框架，它将训练好的生成式策略引导为鲁棒的确定性机器人控制器。关键思想是用学习到的潜空间动作器替换训练好的生成式策略的随机潜空间采样，该动作器为生成式策略预测一个依赖于状态的潜空间输入。这实现了探索与控制的分离：随机生成式采样在策略学习期间提供多样化的动作建议，而确定性潜空间引导在部署时提供稳定且自适应的控制。我们在六个Isaac Lab基准和一个Unitree G1运动任务上评估了SteerGenPO。结果表明，SteerGenPO相比经典强化学习和生成式强化学习基线均有改进，同时其确定性潜空间引导产生了更稳定的推理时行为和更可靠的命令响应。

## Abstract
Diffusion and flow-based generative policies provide a powerful policy class for reinforcement learning by inducing rich stochastic exploration through iterative action generation. However, the stochasticity of diffusion policies is not suitable for stable and precise control in high-dimensional robotic systems, where small action variations can accumulate into inconsistent motion and reduced robustness. To address this issue, we propose SteerGenPO, a latent-space reinforcement learning framework that steers a trained generative policy into a robust deterministic robotic controller. The key idea is to replace stochastic latent sampling of the trained generative policy with a learned latent actor that predicts a state-dependent latent input for the generative policies. This separates exploration and control: stochastic generative sampling provides diverse action proposals during policy learning, while deterministic latent steering provides stable and adaptive control at deployment. We evaluate SteerGenPO on six Isaac Lab benchmarks and a Unitree G1 locomotion task. The results show SteerGenPO improves over both classical RL and generative RL baselines, while its deterministic latent steering produces more stable inference-time behaviors and more reliable command responses.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 扩散和流式生成策略（如GenPO）通过迭代动作生成提供丰富的随机探索，在高维机器人控制中能建模复杂多峰动作分布。
- 然而，生成式策略的随机性在部署时会导致小动作变化累积，产生不稳定接触、不一致运动、扭矩振荡等问题，不适用于需要稳定精确控制的真实机器人。
- 现有解决方案如固定零潜向量可减少方差，但零向量并非针对任务回报优化，解码后的动作可能次优。
- 本文提出SteerGenPO，将随机生成策略引导为确定性稳定控制器，同时保留生成策略的表达能力，实现训练时探索与部署时稳定的分离。

## 二、论文提出的方法论
- 整体框架为两阶段训练：
  - 第一阶段：采用GenPO训练生成式策略（基于流匹配），通过随机潜采样学习多峰动作分布，使用精确的增强动作似然、KL自适应学习率、虚拟动作压缩损失等组件。
  - 第二阶段：固定第一阶段已收敛的生成策略，训练一个状态条件化的高斯潜动作器（均值网络μ_ϕ(s)），通过强化学习优化其均值输出，作为部署时的确定性潜输入。
- 核心思想：将潜采样视为新MDP的动作空间，构建潜动作MDP（M_Z），其中转移和奖励通过冻结的生成策略映射得到。在该MDP上使用PPO优化潜动作器。
- 关键技术细节：
  - 潜动作器输出均值μ_ϕ(s)，探索时加入固定方差Σ，推理时直接使用均值。
  - 引入潜空间正则化（惩罚项−λ_z‖z‖²），防止动作器探索超出可靠潜区域。
  - 采用同策略PPO训练，无需额外的潜价值函数或回放缓冲区，梯度仅通过潜高斯动作器传播。
- 算法流程：
  1. 在原始环境训练GenPO策略，更新生成策略和价值网络。
  2. 冻结生成策略，定义潜动作MDP。
  3. 训练潜动作器：采样z～π_ϕ(·|s)，通过冻结生成策略得到执行动作，计算潜奖励（加入潜惩罚），用PPO更新潜动作器和新价值网络。

## 三、实验设计
- 基准任务：六个Isaac Lab任务（Ant、Humanoid、Franka Arm、Anymal-D、Unitree Go2、Unitree H1），涵盖运动、双足、四足机器人操控；以及Unitree G1人形机器人速度跟踪任务（MuJoCo仿真和真实部署）。
- 对比方法：PPO（经典高斯策略）、GenPO（生成式强化学习基线）、以及SteerGenPO。
- 评估指标：训练回报曲线、最终回报均值与标准差；闭环路径跟随精度（三角形、八字形、方形、S曲线、锯齿形路径）；真实机器人行走稳定性。
- 消融实验：潜输入消融（随机潜 vs 零潜 vs 学习潜）；潜初始探索标准差消融。

## 四、资源与算力
- 训练硬件：服务器配备两个Intel Xeon Gold 5218R CPU（40物理核/80逻辑核），8块NVIDIA GeForce RTX 4090 GPU（24GB显存/块），CUDA 12.9，总计503 GiB系统内存。
- Isaac Lab任务：每个训练运行使用2048并行环境。
- Unitree G1任务：使用2块RTX 4090 GPU，每GPU 4096并行环境，共8192环境；硬件为Intel Xeon Platinum 8368Q CPU（152逻辑核）和8块RTX 4090（48GB/块，文中可能有笔误，应为24GB），CUDA 12.8。
- 训练轮次：GenPO/PPO最多20000次迭代；SteerGenPO第二阶段最多10000次迭代。

## 五、实验数量与充分性
- 共进行6个Isaac Lab任务+1个Unitree G1任务的主实验，每个任务报告5个随机种子的均值与标准差，统计合理。
- 消融实验包括：潜输入选择（随机/零/学习的三种，在6个任务上做比较）；潜初始标准差调节（在某个任务上做，结果如图6）。
- 附加实验：真实Unitree G1部署（定性结果，未量化指标），以及MuJoCo下的闭环路径跟随（含5种路径定性与定量）。
- 总体来说实验覆盖多种形态（双足、四足、机械臂）、多维度（回报、一致性、路径跟踪、真实部署），消融实验针对核心设计变量，结果客观公平，种子重复确保了统计显著性。不足在于真实部署仅为定性演示，缺乏与基线对比的定量数据。

## 六、论文的主要结论与发现
- SteerGenPO在所有6个Isaac Lab任务上最终回报均优于PPO和GenPO，提升幅度最高达88.6%（相对于PPO）和16.9%（相对于GenPO）。
- 确定性潜引导在闭环路径跟随中产生更精确的命令响应和更稳定的轨迹跟踪，尤其在急转弯、重复定向等场景下优势明显。
- 潜输入消融表明：学习的潜动作器优于随机潜和零潜，零潜是强基线但非最优；潜初始标准差需要适中（约0.3）以平衡探索与稳定性。
- 在真实Unitree G1上部署无需额外微调即可产生稳定步行，验证了仿真到真实的可行性。
- 核心发现：将生成式策略的随机潜采样替换为学习的状态相关确定性潜输入，可有效解决生成策略部署不稳定的问题，同时保留其表达能力强、探索好的优点。

## 七、优点
- 方法设计巧妙：明确分离训练时的随机探索和部署时的确定性控制，既保持了生成策略的多峰表达能力，又获得了高斯策略的稳定推理特性。
- 两阶段循序渐进，第二阶段仅需训练轻量潜动作器，不需要重新训练整个生成模型，计算高效。
- 引入潜空间正则化项，避免动作器偏离生成策略先验分布，增强训练稳定性。
- 实验全面：覆盖多种机器人形态（双足、四足、机械臂）、多个基准、闭环路径跟踪和真实部署，消融实验针对核心设计变量。
- 清晰识别生成策略部署时的根本问题（零潜不是价值最优），并提出原理性解决方案，优于简单使用零潜的启发式方法。

## 八、不足与局限
- 依赖第一阶段生成策略的质量和覆盖范围：若生成策略未能探索到高回报区域，潜引导无法恢复新行为。
- 引入第二阶段的额外训练步骤，尽管代价低，但增加了部署前的流程复杂度。
- 真实部署实验仅做定性展示，未提供定量指标（如成功步数、速度跟踪误差），与基线对比不充分。
- 潜初始标准差消融仅在一个任务上展示，泛化性证据稍弱。
- 方法基于流匹配的生成策略，对其他形式扩散策略（如DDPM）的适用性未探讨。
- 实验中未与DSRL等最新潜空间强化学习方法除定性区别外进行直接数值对比（仅提到DSRL并说明区别，无实验结果对照）。
- 未讨论对高频实时控制任务的延迟影响（潜动作器+生成策略前向过程可能比简单高斯策略多一步变换）。

（完）
