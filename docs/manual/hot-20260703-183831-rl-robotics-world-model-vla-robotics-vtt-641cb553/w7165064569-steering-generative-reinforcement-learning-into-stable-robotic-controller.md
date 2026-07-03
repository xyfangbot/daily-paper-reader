---
title: Steering Generative Reinforcement Learning into Stable Robotic Controller
title_zh: 引导生成式强化学习成为稳定的机器人控制器
authors: "Yixuan Wang, Shutong Ding, Ke Hu, Tianxiang Gui, Yi-Xiang Wang, Y Shi"
date: 2026-06-15
pdf: "https://arxiv.org/pdf/2606.16572"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 扩散策略在强化学习中提供随机探索以提升多样性，但其随机性导致高维机器人控制不稳定和动作累积误差。本文提出SteerGenPO，在潜在空间将训练好的生成策略转化为确定性控制器，通过学习状态依赖的潜在actor替代随机采样。在Isaac Lab和Unitree G1步骤任务上，该方法超越经典强化学习与生成强化学习基线，且推理时行为更稳定、命令响应更可靠。该方法有效分离探索与部署控制，提升了机器人控制的鲁棒性。
source: openalex
selection_source: hot_paper_scout
motivation: 扩散策略的随机性在高维机器人系统中引起动作累积误差，导致运动不一致和鲁棒性下降。
method: 提出SteerGenPO，学习一个潜在actor预测状态相关的确定性潜在输入，替换生成策略的随机潜在采样。
result: 在六个Isaac Lab基准和Unitree G1任务上，SteerGenPO超越经典RL和生成RL基线，并实现更稳定的推理行为。
conclusion: 通过分离探索与部署控制，SteerGenPO使生成策略在保持学习多样性的同时实现稳定精确的机器人控制。
---

## 摘要
基于扩散和流的生成式策略通过迭代动作生成引发丰富的随机探索，为强化学习提供了一类强大的策略类。然而，扩散策略的随机性不适用于高维机器人系统中的稳定和精确控制，在这种系统中，小的动作变化可能累积成不一致的运动并降低鲁棒性。为了解决这个问题，我们提出了SteerGenPO，一个潜在空间强化学习框架，它将训练好的生成式策略引导为鲁棒的确定性机器人控制器。关键思想是用学习到的潜在演员替换训练好的生成式策略的随机潜在采样，该潜在演员为生成式策略预测一个状态相关的潜在输入。这将探索和控制分离开来：随机生成采样在策略学习期间提供多样化的动作提案，而确定性潜在引导在部署时提供稳定和自适应控制。我们在六个Isaac Lab基准测试和一个Unitree G1运动任务上评估了SteerGenPO。结果表明，SteerGenPO在经典强化学习和生成式强化学习基线之上均有所改进，同时其确定性潜在引导产生了更稳定的推理时行为和更可靠的控制命令响应。

## Abstract
Diffusion and flow-based generative policies provide a powerful policy class for reinforcement learning by inducing rich stochastic exploration through iterative action generation. However, the stochasticity of diffusion policies is not suitable for stable and precise control in high-dimensional robotic systems, where small action variations can accumulate into inconsistent motion and reduced robustness. To address this issue, we propose SteerGenPO, a latent-space reinforcement learning framework that steers a trained generative policy into a robust deterministic robotic controller. The key idea is to replace stochastic latent sampling of the trained generative policy with a learned latent actor that predicts a state-dependent latent input for the generative policies. This separates exploration and control: stochastic generative sampling provides diverse action proposals during policy learning, while deterministic latent steering provides stable and adaptive control at deployment. We evaluate SteerGenPO on six Isaac Lab benchmarks and a Unitree G1 locomotion task. The results show SteerGenPO improves over both classical RL and generative RL baselines, while its deterministic latent steering produces more stable inference-time behaviors and more reliable command responses.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **问题**：扩散和基于流的生成式策略（如 GenPO）在强化学习（RL）训练时，通过随机潜在采样提供丰富的多模态探索，有助于发现高回报行为。但在部署到高维机器人系统（如人形机器人）时，其随机性会导致动作微小波动累积，引发不稳定接触、运动不一致、力矩振荡和鲁棒性下降。
- **背景**：现有方法如直接使用零潜在向量（固定采样）虽然降低方差，但零向量只是潜在先验的中心点，经过非线性生成变换后可能解码为次优动作，导致性能下降。因此，需要一种既能保留生成策略表达能力又能实现稳定确定性控制的方法。
- **整体含义**：本文提出在潜在空间中将随机生成策略“引导”（steer）为确定性控制器，实现探索与控制的分离。

## 二、论文提出的方法论
- **核心思想**：将生成策略视为潜在变量发生器 $a = G_\theta(s, z)$，其中 $z \sim p_0(z)$ 为高斯先验。在部署时，不采用随机采样或固定零向量，而是学习一个状态条件的高斯潜在策略 $\pi^Z_\phi(z|s) = \mathcal{N}(\mu_\phi(s), \Sigma)$，其均值 $\mu_\phi(s)$ 作为确定性潜在输入。
- **两阶段训练框架（SteerGenPO）**：
  1. **Stage I：生成策略训练**——使用 on-policy RL（GenPO）训练一个流或扩散策略，得到冻结的生成器 $D_\theta(s,z)$。训练时使用随机潜在采样促进探索。
  2. **Stage II：潜在引导策略训练**——冻结 Stage I 的生成器，定义潜在动作 MDP $M^Z_{\bar{\theta}}$：动作空间变为潜在变量 $z$，环境奖励和状态转移由冻结生成器诱导。使用 on-policy PPO 优化潜在策略 $\pi^Z_\phi$，目标函数为标准 PPO 损失加潜在正则项 $\lambda_z \|z\|_2^2$（鼓励潜在靠近先验可靠区域）。推理时直接使用 $\mu_\phi(s)$ 作为潜在输入。
- **关键技术细节**：
  - 使用可逆生成映射（如条件流）计算动作似然，支持 on-policy 更新。
  - Stage II 不需要额外的潜在价值网络（critic），直接训练状态价值函数 $V^Z(s)$ 并计算优势。
  - 引入“虚拟动作压缩损失” $L_{\text{comp}} = \mathbb{E}[\|x_t - y_t\|_2^2]$ 减少冗余探索（针对 GenPO 的双重动作结构）。
  - 潜在初始标准差 $\sigma_0$ 需要平衡探索与稳定（实验最优为 0.3 左右）。
- **算法流程**（Algorithm 1）：
  1. 初始化流模型 $F_\theta$ 和值网络 $V_\omega$。
  2. 循环：rollout 使用随机潜在采样，计算似然并更新 $F_\theta, V_\omega$，直至收敛。
  3. 冻结 $F_\theta$，定义 $D_\theta(s,z) = h(F_\theta(s,z))$。
  4. 初始化潜在策略 $\pi^Z_\phi$ 和 $V^Z$。
  5. 循环：采样 $z_t \sim \pi^Z_\phi(\cdot|s_t)$，执行 $a_t = D_\theta(s_t,z_t)$，使用带潜在惩罚的奖励 $\tilde{r}_t = r_t - \lambda_z \|z_t\|_2^2$ 更新 $\pi^Z_\phi$ 和 $V^Z$。

## 三、实验设计
- **基准测试（Benchmark）**：
  - **Isaac Lab 六任务**：Ant-v0、Humanoid-v0、Franka Arm（Lift Cube）、Anymal-D（平坦速度跟踪）、Unitree Go2（粗糙地形速度跟踪）、Unitree H1（粗糙地形速度跟踪）。涵盖经典运动、人形、四足、机械臂。
  - **Unitree G1 运动任务**：速度跟踪，在 MuJoCo 中闭环路径跟踪（三角形、8字、方形、S形、Z形路径），并在真实 G1 机器人上部署定性验证。
- **对比方法**：
  - 基线：PPO（经典高斯策略）、GenPO（生成式策略，与 SteerGenPO Stage I 相同）。
  - 消融变体：GenPO-random（随机潜在）、GenPO-zero（零潜在）、不同初始标准差。
- **评估指标**：最终回报（均值±标准差，5 个随机种子）、闭环跟踪轨迹定性比较。
- **实验设置**：Isaac Lab 使用 2048 并行环境，Unitree G1 使用 8192 并行环境。所有方法使用相同的 RSL-RL 框架和奖励函数。

## 四、资源与算力
- **硬件配置**（来自附录 A.2）：
  - CPU：2× Intel Xeon Gold 5218R（20 核/40 线程，2.10GHz 基础频率，4.00GHz 最大频率），总 80 逻辑核，503 GiB 内存。
  - GPU：8× NVIDIA GeForce RTX 4090（24GB 显存），PCIe 连接，CUDA 12.9/12.8，驱动版本 575.64.03/570.86.10。
- **训练算力**：
  - Isaac Lab 实验：所有方法在 8 块 RTX 4090 上运行，每任务使用全部 8 块 GPU。
  - Unitree G1 任务：每训练 run 使用 2 块 RTX 4090，每 GPU 运行 4096 并行环境，共 8192 环境。
- **训练时长**：未明确给出具体时长，但 Stage I 最多 20000 次迭代，Stage II 最多 10000 次迭代。附录表格给出各任务超参数（如 rollout length 24~32，学习率等）。

## 五、实验数量与充分性
- **主要实验**：6 个 Isaac Lab 任务（每个 5 种子），1 个 Unitree G1 任务（5 种子），共约 35 个独立训练 run。
- **消融实验**：
  - 潜在输入消融：在 6 个任务上比较随机潜在、零潜在、SteerGenPO 学习潜在（见表 9），控制生成器固定。
  - 潜在初始标准差消融：在某个任务上测试不同 $\sigma_0$ 值（图 6），寻找最佳平衡点。
- **定性实验**：5 种路径的闭环轨迹跟踪（图 3），真实机器人部署（图 4）。
- **充分性评价**：
  - **客观与公平**：统一使用 RSL-RL 框架、相同奖励函数、相同并行环境数，报告多次重复的均值与标准差，对比基线包括经典 PPO 和最优生成式基线 GenPO。
  - **覆盖范围**：任务多样（经典运动、四足、人形、机械臂），但所有仿真环境均为 Isaac Lab 和 MuJoCo，未涉及真实复杂地形或动态干扰。消融实验较完整，但缺少对潜在正则系数 $\lambda_z$ 的详细消融。
  - **局限性**：仅在 Unitree G1 上做了真实部署定性演示，未提供定量指标（如步态对称性、能耗等）。其他任务均未仿真到真实迁移。

## 六、论文的主要结论与发现
- SteerGenPO 在所有 6 个 Isaac Lab 任务和 Unitree G1 任务上均显著优于 PPO 和 GenPO：最终回报比 PPO 最高提升 88.6%，比 GenPO 最高提升 16.9%。
- 学习状态依赖的潜在输入（均值）比固定零潜在或随机潜在更优，表明零潜在只是先验中心而非价值最优。
- 在闭环路径跟踪中，SteerGenPO 产生更稳定的轨迹（更小的偏差、更精确的转向），真实部署实现稳定前向行走。
- 潜在引导训练（Stage II）仅需有限迭代即可提升性能，且比微调完整生成策略更高效。

## 七、优点
- **创新性**：首次将潜在空间 on-policy RL 应用于训练好的生成式策略，将随机探索与确定性部署分离，思路新颖。
- **实用性**：两阶段训练使得生成策略在训练时利用多模态探索优势，部署时保持确定性，兼顾性能与稳定性。
- **轻量级**：Stage II 仅训练小型潜在策略网络（高斯），冻结的生成器只做前向推理，计算开销小，易于集成到现有流水线。
- **理论完备**：形式化定义了潜在动作 MDP，并给出 on-policy PPO 的适配，无需额外潜在 critic。
- **实验充分**：涵盖多种机器人形态（四足、双足、机械臂），对比多个基线，消融实验验证核心设计的必要性；真实机器人部署验证 sim-to-real 可行性。

## 八、不足与局限
- **对第一阶段性能的依赖**：Stage II 只能在第一阶段训练好的生成策略所覆盖的动作流形内优化，若第一阶段探索不足或质量差，引导会受限。
- **额外训练阶段**：尽管 Stage II 比完整微调便宜，但仍需额外优化步骤，且需要手动调参（如潜在初始标准差、正则系数）。
- **实验覆盖有限**：
  - 未在多种真实环境（如崎岖地形、动态障碍）中定量评估，仅在平坦地面做定性演示。
  - 未与其他潜在空间优化方法（如 DSRL）直接对比（仅提及区别）。
  - 缺失对潜在正则系数的系统消融（仅给出一个固定值）。
- **鲁棒性风险**：潜在正则项鼓励潜在靠近原点，但若任务需要极端的潜在值（如快速转弯），正则可能限制性能；论文未讨论极端情况。
- **可扩展性**：方法依赖于可逆生成映射计算似然，若生成器非可逆则需近似，可能引入偏差。

（完）
