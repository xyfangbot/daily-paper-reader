---
title: "WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation"
title_zh: "WAM-Nav: 非对称潜在世界-动作建模用于统一视觉导航"
authors: "Ning Yang, Yan Huang, Kaiwen Peng, Ziheng He, Kai Wang, Cui Miao, Kailin Lyu, Guo Li, Xiaofeng Wang, Zheng Zhu, Jing Liu, Nianfeng Liu"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2606.04907v2"
arxiv_id: 2606.04907v2
arxiv_url: "https://arxiv.org/abs/2606.04907v2"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/008-2026_yang_wam_nav-5d966c01-3db70c2f3854.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2606.04907v2", "query:Embodied Visual Navigation", "query:World-Action Model", "query:Diffusion Transformer"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "视觉导航需生成平滑无碰撞轨迹，但反应式策略缺乏前瞻推理，模块化方法误差累积且推理低效。提出WAM-Nav，利用共享Diffusion Transformer进行非对称联合扩散，同时生成长程动作与短程视觉预象，避免自回归误差。引入双流上下文条件与统一目标对齐，支持多种导航目标。在ClutterScenes和InternScenes上Image-Goal和Point-Goal成功率分别提升15.7%和3.3%，真实环境零样本迁移成功率85%。该方法实现了高效鲁棒的统一视觉导航。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1438, \"height\": 607, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1441, \"height\": 603, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1433, \"height\": 523, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1428, \"height\": 529, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 664, \"height\": 822, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1096, \"height\": 287, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1069, \"height\": 815, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1097, \"height\": 255, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1466, \"height\": 187, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1453, \"height\": 602, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1458, \"height\": 877, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1452, \"height\": 274, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1453, \"height\": 296, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1452, \"height\": 283, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 648, \"height\": 266, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1457, \"height\": 440, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-008-3db70c2f3854-wam-nav-asymmetric-latent-world-action-modeling-for-unified-visual-navigation/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1454, \"height\": 241, \"label\": \"Table\"}]"
motivation: 现有视觉导航策略缺乏前瞻推理，模块化方法误差累积，急需联合学习动作与视觉预见的统一框架。
method: 提出WAM-Nav，基于共享Diffusion Transformer非对称联合扩散，同时生成长程动作与短程视觉预象，并引入双流上下文条件与统一目标对齐模块。
result: "在ClutterScenes和InternScenes上Image-Goal成功率提升15.7%，Point-Goal提升3.3%；真实环境零样本迁移成功率85%。"
conclusion: WAM-Nav通过联合隐式世界-动作建模，实现高效鲁棒视觉导航，显著提升泛化能力和部署性能。
---

## 摘要
视觉导航需要在复杂的几何和物理约束下生成平滑且无碰撞的轨迹。现有的直接将观测映射到动作的反应式策略缺乏预测性推理，限制了其主动避开障碍物的能力。虽然视觉想象提供了预测性前瞻，但传统的模块化方法将场景预测与策略学习分离，往往导致误差累积和推理效率低下。为解决这些局限，我们提出WAM-Nav，一种用于具身视觉导航的潜在世界-动作模型，它联合学习动作生成和潜在视觉前瞻，在不损害推理效率的情况下实现更鲁棒且具有前瞻性的导航决策。具体而言，WAM-Nav利用共享的扩散变换器进行非对称联合扩散，同时生成长视野动作和短视野视觉前瞻，减少了多步自回归展开中固有的推理延迟和视觉误差累积。为进一步鼓励轨迹生成的平滑性和一致性，我们引入了一种双流上下文条件机制，将片段的自我运动历史与连续的视觉观测相结合。结合统一的目标对齐模块，该模块在目标类型间保持平衡表示，WAM-Nav自然地在一个策略中支持图像目标、点目标和无目标探索。在具有挑战性的ClutterScenes和InternScenes基准上的大量实验证明了WAM-Nav的强大泛化能力，特别是在图像目标和点目标导航中，成功率分别提高了15.7%和3.3%。真实世界部署进一步验证了有效的零样本模拟到现实迁移，在多样化的室内和室外环境中实现了平均85%的任务成功率。

## Abstract
Visual navigation requires generating smooth and collision-free trajectories under complex geometric and physical constraints. Existing reactive policies that directly map observations to actions lack anticipatory reasoning, limiting their ability to proactively avoid obstacles. While visual imagination offers predictive foresight, conventional modular approaches separate scene prediction from policy learning, often leading to error accumulation and inefficient inference. To address these limitations, we propose WAM-Nav, a Latent World-Action Model for embodied visual navigation that jointly learns action generation and latent visual foresight, enabling more robust and foresighted navigation decisions without compromising inference efficiency. Specifically, WAM-Nav utilizes a shared Diffusion Transformer for asymmetric joint diffusion to concurrently generate long-horizon actions and short-horizon visual foresight, reducing the inference latency and visual error accumulation inherent in multi-step autoregressive rollouts. To further encourage smooth and consistent trajectory generation, we introduce a dual-stream contextual conditioning mechanism that integrates episode-level ego-motion history with sequential visual observations. Combined with a unified goal alignment module that preserves balanced representations across goal types, WAM-Nav naturally supports Image-Goal, Point-Goal, and No-Goal exploration within a single policy. Extensive experiments on the challenging ClutterScenes and InternScenes benchmarks demonstrate strong generalization of WAM-Nav, particularly on Image-Goal and Point-Goal navigation, where it improves success rates by 15.7% and 3.3%, respectively. Real-world deployment further validates effective zero-shot sim-to-real transfer, achieving an average 85% task success rate across diverse indoor and outdoor environments.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：视觉导航需要在复杂几何与物理约束下生成平滑且无碰撞的轨迹，但现有方法存在根本性缺陷：
  - **反应式策略**（直接映射观测到动作）：缺乏预测性推理，依赖瞬时感知，在杂乱环境中易陷入局部最优和碰撞。
  - **模块化世界模型方法**（先预测未来场景再规划动作）：将场景预测与策略学习分离，导致计算延迟和复合误差累积，推理效率低。
  - **现有统一框架局限性**：大多数导航方法仅支持单一目标类型（如图像目标、点目标），适应新任务需重新设计与训练；已有的多任务策略（如NavDP）存在不同任务间性能不均衡问题。
- **研究含义**：提出一种**联合学习动作生成和潜在视觉前瞻**的统一框架，在不牺牲推理效率的前提下赋予策略前瞻式决策能力，同时支持多种导航目标（图像目标、点目标、无目标探索）。

## 二、论文提出的方法论
- **核心思想**：WAM-Nav是一个**潜在世界-动作模型**，利用共享的扩散变换器（DiT）进行**非对称联合扩散**，同时生成长视野动作轨迹与短视野潜在视觉前瞻，将动作决策与视觉预测深度融合在一个迭代式生成过程中。
- **关键技术细节**：
  - **统一目标对齐（Unified Goal Alignment）**：将异构目标（图像、点坐标、空目标）编码为两个互补的查询嵌入：视觉语义查询（gV）用于视觉记忆检索，几何查询（gG）用于轨迹方向引导。通过模态特定特征提取器与线性映射投影，保持模态特定信息同时提供统一接口。
  - **双流上下文条件机制（Dual-Stream Contextual Conditioning, DSCC）**：在历史滑动窗口内融合两类上下文信息——1) **目标调制视觉记忆流**：用gV对DINOv2编码的RGB序列进行注意力加权残差更新；2) **轨迹感知运动历史流**：将绝对姿态转换为当前自我中心坐标系下的相对位移与航向变化序列，经因果Transformer编码后，用gG通过交叉注意力提取运动连续性矢量okin。最终okin通过Transformer解码器与视觉记忆融合，形成紧凑的条件上下文C。
  - **非对称动作-前瞻生成（Asymmetric Action-Foresight Generation）**：采用**流匹配（Flow-matching）**训练策略。在共享表示空间中，对长视野动作序列（Hact=24）和短视野潜在视觉状态（Hvis=1，由预训练Stable Diffusion VAE压缩）进行非对称联合去噪。在共享DiT内，动作令牌与视觉令牌通过共享自注意力、交叉注意力（条件化C）和自适应层归一化实现跨模态交互，潜在前瞻作为感知约束惩罚动作-场景不一致。
  - **训练目标**：最小化联合损失函数`Ltotal = E[||ûA - uA||² + λimg||ûZ - uZ||²] + λalign * Lalign`，包含流匹配速度回归项和模态间对称对比InfoNCE对齐损失。
  - **在线推理**：遵循滚动时域控制，每步采样16条候选轨迹，执行第一条，保持实时性（推理延迟0.26秒，TFLOPs仅0.7）。

## 三、实验设计
- **训练数据集**：VLN-N1大规模视觉导航数据集，基于六类3D场景资产（Replica、Matterport3D、Gibson、3D-FRONT、HSSD、HM3D），提供超过400小时、20万+条无碰撞平滑第一人称轨迹。
- **零样本评估平台**：基于IsaacSim仿真器，导航器为轮式机器人ClearPath Dingo。所有方法使用原始预训练权重直接评估，无额外微调。
- **两类评估场景**：
  - **ClutterScenes**：10个简单场景+10个困难场景（随机生成布局，障碍物密集）。
  - **InternScenes**：20个家庭场景+20个商业场景（窄通道、杂乱布局）。
  - 每场景随机采样100个导航片段，总计6000个评估片段。
- **评估指标**：图像目标/点目标导航：成功率(SR)与路径长度加权成功率(SPL)；无目标探索：探索时间和探索面积。
- **对比方法**：
  - 图像目标：GNM, ViNT, NoMaD, NWM, NavDP
  - 点目标：DD-PPO, iPlanner, ViPlanner, NavDP
  - 无目标探索：GNM, ViNT, NoMaD, NavDP
- **真实世界部署**：Unitree G1人形机器人+Intel RealSense D455摄像头，在会议室、仓库、大厅、停车场四类场景中每场景10次测试。

## 四、资源与算力
- **训练资源**：学习率1.5×10⁻⁴，**总训练成本约8×120 GPU小时**（文中未明确指定GPU型号，但结合论文上下文和标注的安装环境，推测为NVIDIA高端GPU，如A100或H100）。
- **模型规模**：总参数量234.9M（含冻结的DINOv2和Stable Diffusion VAE），可训练参数129.2M。推理时GPU内存占用约1.3GB。
- **注**：文中未提供具体GPU型号、数量或显存规格的明确说明。

## 五、实验数量与充分性
- **整体实验数量**：涵盖3大任务（图像目标、点目标、无目标探索）× 4个子场景（ClutterScenes简单/困难、InternScenes家庭/商业）× 每场景100个片段 = 超过6000个评估片段，结果呈现于主表和附录。
- **消融实验（附录F）**：包括(1) 组件消融（运动轨迹、潜在前瞻单独/组合效果）；(2) 目标对齐消融（仅gV、仅gG、两者结合）；(3) 历史窗口大小消融（k=4/8/16）；(4) 动作-前瞻耦合架构消融（解耦/部分共享/完全共享DiT）；(5) 视觉预测视野消融（Hvis=1/4/8/24）；(6) 不同难度级别性能；(7) 跨不同机器人形态（轮式Dingo、人形G1/H2）。
- **充分性与公平性**：
  - 对比方法覆盖多种主流范式（强化学习、反应式扩散、世界模型等），且均在零样本设置下用原始权重评估。
  - 所有实验均在统一仿真平台和机器人平台上完成，指标标准化。
  - 消融实验系统全面，验证了每个关键设计选择的有效性。
  - 真实世界实验进行了40次测试，平均成功率85%，与仿真结论一致。

## 六、论文的主要结论与发现
- **主要发现**：WAM-Nav在三种导航任务上均达到最优平均性能（图像目标SR 50.2%/SPL 48.2%，点目标SR 80.4%/SPL 78.0%，无目标探索面积171.1m²），尤其在图像目标导航中**成功率相对最佳基线NavDP提升15.7%**，点目标导航提升3.3%。
- **机制验证**：短视野潜在视觉前瞻（而非长自回归视觉展开）在导航中效果最佳，可提供可靠近景几何约束，同时避免长视野预测的误差累积与延迟。共享DiT架构使潜在前瞻直接正则化动作生成，优于解耦或部分共享变体。
- **泛化能力**：跨不同机器人形态（轮式、人形）无需重新训练即可保持优势；真实场景零样本迁移成功率达85%，验证了有效的仿真到现实迁移能力。
- **效率**：推理延迟0.26秒，TFLOPs仅0.7，满足实时导航需求，远优于NWM（1.43秒, 8.3 TFLOPs）。

## 七、优点
- **创新性**：首次将世界模型中的联合动作-视觉生成范式成功应用于导航领域，并针对导航特有的较大自我中心视角变化设计了非对称视野设计。
- **统一性与灵活性**：单一策略自然支持三种目标类型，避免了对不同任务的重设计与重训练，且通过解耦视觉语义和几何查询实现了任务间均衡性能。
- **鲁棒泛化**：在多种仿真场景（杂乱/商业/住宅）、不同难度、不同机器人形态上都表现出优于现有方法的泛化能力，且真实部署验证了域迁移效果。
- **实时高效**：通过潜在前瞻（而非像素级预测）和联合生成，在增加预测能力的同时保持了低推理延迟和计算开销，优于模块化方法。
- **实验充分严谨**：系统全面的消融实验、多任务对比、跨形态测试、真实部署验证，覆盖了方法的各个层面。

## 八、不足与局限
- **感知视野限制**：真实部署中发现，相机高度和视野局限影响对近地障碍物的感知，可能导致碰撞。
- **未显式建模机器人本体**：当前策略未考虑机器人完整形体（如宽度、高度），轨迹规划仅确保相机通过，可能导致机器人身体与障碍物碰撞。
- **应用推广风险**：方法在仿真和特定室内外场景已验证，但在更极端/无结构环境（如野外、废墟）中的泛化能力尚未测试。
- **评估集局限性**：虽涵盖多种室内场景，但仍未覆盖室外复杂动态环境（如人流、车辆），可能限制在开放世界应用中的通用性。
- **推理效率仍有提升空间**：虽然0.26秒已满足1Hz部署，但与NavDP（0.16秒）相比仍有1.6倍延迟，在高频控制场景下可能成为瓶颈。
- **对预训练视觉编码器的依赖**：性能依赖于DINOv2和Stable Diffusion VAE的表示质量，若底层视觉特征退化，模型性能可能下降。

（完）
