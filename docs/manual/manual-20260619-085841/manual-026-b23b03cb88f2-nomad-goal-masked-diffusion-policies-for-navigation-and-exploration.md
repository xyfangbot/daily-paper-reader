---
title: "NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration"
title_zh: "NoMaD: 面向导航与探索的目标掩蔽扩散策略"
authors: "Ajay Sridhar, Dhruv Shah, Catherine Glossop, Sergey Levine"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/026-nomad-4681be3b-b23b03cb88f2.pdf
tags: ["query:手动上传", "paper:PDF", "query:diffusion policy", "query:goal-conditioned navigation", "query:exploration", "query:robotic navigation", "query:visual navigation"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 机器人导航需要在陌生环境中完成目标导向的到达任务，也要进行无目标的探索以发现目标，传统方法通常用不同模型分别处理。本文NoMaD通过单一扩散策略统一这两类任务，基于Transformer和扩散模型解码器，从多机器人数据训练。在真实移动机器人平台上的实验表明，相比五种基线方法（包括生成子目标或潜变量模型），NoMaD在未知环境导航中表现更优，碰撞率更低，且模型更小。该工作证明了统一策略在机器人导航与探索中的潜力。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-026-b23b03cb88f2-nomad-goal-masked-diffusion-policies-for-navigation-and-exploration/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1822, \"height\": 435, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-026-b23b03cb88f2-nomad-goal-masked-diffusion-policies-for-navigation-and-exploration/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1829, \"height\": 494, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-026-b23b03cb88f2-nomad-goal-masked-diffusion-policies-for-navigation-and-exploration/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 891, \"height\": 413, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-026-b23b03cb88f2-nomad-goal-masked-diffusion-policies-for-navigation-and-exploration/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1759, \"height\": 549, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-026-b23b03cb88f2-nomad-goal-masked-diffusion-policies-for-navigation-and-exploration/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1820, \"height\": 533, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-026-b23b03cb88f2-nomad-goal-masked-diffusion-policies-for-navigation-and-exploration/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 871, \"height\": 341, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-026-b23b03cb88f2-nomad-goal-masked-diffusion-policies-for-navigation-and-exploration/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 871, \"height\": 196, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-026-b23b03cb88f2-nomad-goal-masked-diffusion-policies-for-navigation-and-exploration/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 610, \"height\": 227, \"label\": \"Table\"}]"
motivation: 现有导航方法通常将目标导向导航和探索分开建模，导致系统复杂且效率低下，需要统一的策略来简化流程并提升泛化能力。
method: 训练一个统一的扩散策略，使用Transformer编码和扩散模型解码器，同时处理目标条件导航和无目标探索，基于多地面机器人数据训练。
result: 在真实机器人平台上，NoMaD在未知环境导航中优于五种基线方法，碰撞率更低，且模型参数量更小。
conclusion: 统一的扩散策略能有效结合导航与探索任务，简化系统设计，并提升在未知环境中的导航性能和安全性。
---

## 摘要
在陌生环境中进行导航的机器人学习需要提供面向任务导向的导航（即到达机器人已定位的目标）和任务无关的探索（即在未知环境中搜索目标）两种策略。通常，这些角色由不同的模型处理，例如通过使用子目标提议、规划或单独的导航策略。在本文中，我们描述了如何训练一个单一统一的扩散策略来处理目标导向导航和任务无关探索，其中后者提供了在未知环境中搜索的能力，前者则提供了在目标被定位后到达用户指定目标的能力。我们表明，与使用生成模型的子目标提议或基于潜在变量模型的先前方法相比，这种统一策略在前往视觉指示目标的新环境中导航时，能获得更好的整体性能。我们通过使用基于Transformer的大规模策略来实现我们的方法，该策略在来自多个地面机器人的数据上进行训练，并采用扩散模型解码器来灵活处理目标条件化和任务无关的导航。我们在真实世界的移动机器人平台上进行的实验表明，与五种替代方法相比，在未见过的环境中导航更有效，并且尽管使用的模型比最先进的方法更小，但性能显著提升且碰撞率更低。

## Abstract
Robotic learning for navigation in unfamiliar environments needs to provide policies for both task-oriented navigation (i.e., reaching a goal that the robot has located), and task-agnostic exploration (i.e., searching for a goal in a novel setting). Typically, these roles are handled by separate models, for example by using subgoal proposals, planning, or separate navigation strategies. In this paper, we describe how we can train a single unified diffusion policy to handle both goal-directed navigation and goal-agnostic exploration, with the latter providing the ability to search novel environments, and the former providing the ability to reach a user-specified goal once it has been located. We show that this unified policy results in better overall performance when navigating to visually indicated goals in novel environments, as compared to approaches that use subgoal proposals from generative models, or prior methods based on latent variable models. We instantiate our method by using a large-scale Transformer-based policy trained on data from multiple ground robots, with a diffusion model decoder to flexibly handle both goal-conditioned and goal-agnostic navigation. Our experiments, conducted on a real-world mobile robot platform, show effective navigation in unseen environments in comparison with five alternative methods, and demonstrate significant improvements in performance and lower collision rates, despite utilizing smaller models than state-of-the-art approaches.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：在未知环境中，移动机器人需要同时具备两种能力：一是目标导向导航（依据用户指定的视觉目标图片抵达该位置），二是无目标探索（在未知环境中主动搜索，以发现潜在的目标）。传统方法通常将这两种能力分离，例如使用独立的子目标生成模型、高层规划器或不同的导航策略，导致系统复杂、效率低下且泛化性受限。
- **研究动机**：能否设计一个统一的单一策略，既能处理任务特异性行为（如前往视觉目标），又能处理任务无关行为（如自主探索），从而简化系统架构，提升在全新环境中的导航性能和鲁棒性？
- **整体含义**：本文提出NoMaD（Navigation with Goal Masked Diffusion），首次将扩散策略（Diffusion Policy）与目标掩蔽（Goal Masking）结合，在一个模型内统一了目标条件导航和无目标探索，并在真实机器人平台验证了其有效性。

## 二、论文提出的方法论
- **核心思想**：利用Transformer骨干网络编码视觉观测序列，并通过扩散模型对动作序列进行建模，同时引入二元“目标掩码”（goal mask）来控制是否利用目标图像，从而在一个策略中实现两种行为模式。
- **关键技术细节**：
  1. **视觉编码**：使用EfficientNet-B0分别对当前观测序列（过去5帧RGB图像）和目标图像提取特征，得到令牌序列。
  2. **目标掩蔽机制**：通过一个二元掩码m∈{0,1}控制Transformer注意力是否关注目标令牌。训练时m以0.5概率随机采样，使模型同时学习目标导向和任务无关行为；测试时根据需求设置m：m=1用于无目标探索，m=0用于目标导向导航。
  3. **扩散策略**：基于条件扩散模型建模动作分布p(a_t | c_t)，其中c_t为注意力编码后的上下文向量。从高斯噪声开始，经过K=10步去噪（使用Square Cosine Noise Scheduler），通过1D条件U-Net预测噪声，最终生成8步未来动作序列。去噪过程不生成图像，只生成动作，保证实时控制。
  4. **联合训练损失**：扩散噪声预测的MSE损失 + 时间距离预测的MSE损失（权重λ=10⁻⁴），采用AdamW优化器，学习率10⁻⁴，训练30个epoch，批量大小256。
  5. **高层规划**：与拓扑图记忆结合，采用基于前沿（frontier）的探索策略，由NoMaD提供局部动作分布，高层规划器选择探索子目标。
- **公式/算法流程**：去噪迭代公式为 a^{k-1} = α·(a^k - γ·ε_θ(c_t, a^k, k)) + N(0, σ²I)，其中ε_θ为噪声预测网络；训练时随机采样去噪步数k并添加对应噪声，优化均方误差。

## 三、实验设计
- **数据集**：使用GNM和SACSoN两个大规模异构数据集，包含超过100小时的真实世界轨迹，覆盖多种环境和机器人平台（包括行人密集场景）。所有基线均在该混合数据集上训练20个epoch。
- **场景与平台**：在6个不同的室内外真实环境中进行评测，使用LoCoBot移动机器人平台。
- **基准任务**：
  1. **探索（Exploration）**：在未知环境中无目标搜索，需自主覆盖环境并发现目标位置。
  2. **导航（Navigation）**：在已知环境中（已构建拓扑图）依据目标图像到达指定位置。
- **对比方法**：
  - VIB（变分信息瓶颈潜变量模型）
  - Masked ViNT（带目标掩蔽的ViNT点估计策略）
  - Autoregressive（离散化动作空间的回归预测）
  - Random Subgoals（随机选择子目标 + ViNT策略）
  - Subgoal Diffusion（图像扩散模型生成子目标 + ViNT策略，335M参数，15倍于NoMaD）
  - 以及单独训练的Diffusion Policy（无目标）和ViNT Policy（目标导向）作为统一策略对比
- **评价指标**：平均成功率（Success Rate）和平均碰撞次数（Collisions）。

## 四、资源与算力
- **计算资源**：论文提及使用Google TPU Research Cloud、NSF CloudBank以及Berkeley Research Computing项目提供的计算资源，未明确说明GPU型号、数量及单次训练的具体时长。
- **模型规模**：NoMaD总参数量约19M（Transformer 4层4头+EfficientNet-B0+U-Net），相比子目标扩散的335M模型小15倍以上，可在边缘设备（如NVIDIA Jetson Orin）上实时运行。

## 五、实验数量与充分性
- **实验组数**：主实验包含探索和导航两个任务，在6个室内外环境进行，对比了6种基线方法（其中5种有定量结果表I、表II、表III）。
- **消融实验**：进行了三组消融/分析实验：
  1. **统一 vs 专用策略**（表II）：比较统一训练的NoMaD与单独训练的Diffusion Policy（探索）和ViNT Policy（导航），证明统一策略性能不降低。
  2. **视觉编码器与目标掩蔽方式**（表III）：比较Late Fusion CNN、Early Fusion CNN、ViT三种编码器，证明NoMaD的Transformer+注意力掩蔽最优。
  3. **定性分析**：可视化动作分布（图5），展示NoMaD在多模态动作预测上的优势。
- **充分性评估**：实验较为充分。覆盖不同难度的室内外场景，对比了从简单点估计到复杂扩散模型的多种基线，并进行了关键消融。但仅使用单一机器人平台（LoCoBot），且未在仿真环境进行大规模统计测试，可能受限于真实实验的成本。

## 六、论文的主要结论与发现
- **Q1结论**：NoMaD在探索任务中平均成功率98%，优于最佳基线Subgoal Diffusion（77%）约25%，碰撞次数仅0.2次，远低于其他方法；在导航任务中与Subgoal Diffusion并列90%，但模型小了15倍，且能完全在边缘运行。
- **Q2结论**：统一训练的NoMaD在无目标探索和目标导向导航上分别达到98%和92%，与专用模型性能持平，证明共享表征有效。
- **Q3结论**：Transformer编码+注意力掩蔽的NoMaD显著优于CNN和ViT变体，后者成功率仅32%–68%，碰撞率高。
- **整体结论**：首次成功实现目标条件扩散策略的实物机器人部署，验证了统一策略在导航与探索中的高效性和泛化性。

## 七、优点
1. **创新性**：首次将目标掩蔽与扩散策略结合，实现单一模型对两种行为（目标导向和任务无关）的统一建模。
2. **性能优越**：在真实环境中比最先进方法（子目标扩散）高25%成功率，同时碰撞率最低。
3. **计算高效**：模型仅19M参数，相比335M的子目标扩散模型小15倍，可部署于低功耗边缘设备。
4. **表现力强**：扩散策略能自然建模多模态动作分布（如在交叉口同时预测左右转），而点估计或离散化方法难以做到。
5. **泛化能力**：在多个未见过的室内外环境中均表现鲁棒，表明了共享表征的有效性。

## 八、不足与局限
1. **目标模态单一**：目前仅支持视觉目标图像，未扩展到语言指令、GPS坐标等更自然的人机交互模态。
2. **高层规划简单**：采用标准的前沿探索策略，未利用语义信息或先验知识来智能选择探索区域，可能限制复杂场景效率。
3. **实验平台限制**：仅使用LoCoBot单一移动机器人平台，未验证在其他形态（如四足、轮式等）上的适用性。
4. **统计严谨性不足**：缺少多次重复实验的方差统计（例如标准误），且未在仿真环境中进行大规模对比以增强统计可靠性。
5. **训练细节不透明**：未给出完整的超参数敏感度分析和训练收敛曲线，计算资源使用未量化（GPU型号、训练天数等）。
6. **泛化边界未探讨**：对环境变化（如光照剧变、动态障碍物密度等）的鲁棒性未做系统性分析。

（完）
