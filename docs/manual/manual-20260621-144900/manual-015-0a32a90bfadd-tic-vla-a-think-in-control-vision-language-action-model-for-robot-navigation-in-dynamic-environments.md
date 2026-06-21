---
title: "TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments"
title_zh: TIC-VLA：一种用于动态环境中机器人导航的思考与控制视觉-语言-动作模型
authors: "Zhiyu Huang, Yun Zhang, Johnson Liu, Rui Song, Chen Tang, Jiaqi Ma"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2602.02459v2"
arxiv_id: 2602.02459v2
arxiv_url: "https://arxiv.org/abs/2602.02459v2"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/015-2026_huang_tic_vla-ff12bcb8-0a32a90bfadd.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2602.02459v2", "query:Vision-Language-Action", "query:robot navigation", "query:dynamic environments", "query:latency-aware", "query:delayed semantic-control"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 在动态人机共融环境中，机器人需结合语言指令与实时控制，但视觉-语言-动作（VLA）模型存在语义推理延迟与实时动作不匹配的问题。本文提出TIC-VLA框架，显式建模延迟语义推理，通过定义延迟语义-控制接口，利用历史视觉-语言状态和延迟元数据补偿异步推理。配合延迟感知的训练流程，在模拟器DynaNav和真机上验证，多秒推理延迟下仍优于现有VLA模型，实现鲁棒实时控制。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 857, \"height\": 820, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1762, \"height\": 835, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 864, \"height\": 1358, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1773, \"height\": 609, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 865, \"height\": 522, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1752, \"height\": 614, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1767, \"height\": 697, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1752, \"height\": 554, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1757, \"height\": 1200, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1515, \"height\": 475, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1744, \"height\": 840, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1674, \"height\": 1066, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 859, \"height\": 556, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 853, \"height\": 243, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 861, \"height\": 288, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 822, \"height\": 172, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 733, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 865, \"height\": 173, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 545, \"height\": 538, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 543, \"height\": 498, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 439, \"height\": 538, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1469, \"height\": 597, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1159, \"height\": 297, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 951, \"height\": 238, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 958, \"height\": 234, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 772, \"height\": 244, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-015-0a32a90bfadd-tic-vla-a-think-in-control-vision-language-action-model-for-robot-navigation-in-dynamic-environments/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1192, \"height\": 233, \"label\": \"Table\"}]"
motivation: 现有VLA模型忽略语义推理延迟与实时控制的时间错配，导致动态环境中导航性能下降。
method: 提出TIC-VLA，包含延迟语义-控制接口和延迟一致性训练，在动作生成中显式利用历史视觉-语言状态和延迟信息。
result: 在DynaNav模拟器和真实机器人中，多秒推理延迟下TIC-VLA持续优于基线，保持实时控制能力。
conclusion: 延迟感知的VLA建模是异步推理下鲁棒导航的关键，TIC-VLA为动态开放环境提供了有效解决方案。
---

## 摘要
在动态、以人为中心的环境中，机器人必须遵循语言指令，同时保持实时反应式控制。视觉-语言-动作（VLA）模型提供了一个有前景的框架，但它们假设推理和控制是时间对齐的，尽管语义推理相对于实时动作本质上存在延迟。我们提出了思考与控制（TIC）-VLA，这是一个延迟感知框架，在动作生成过程中显式建模延迟的语义推理。TIC-VLA定义了一个延迟语义控制接口，该接口除了当前观测外，还基于延迟的视觉-语言语义状态和显式的延迟元数据来条件化动作生成，使策略能够补偿异步推理。我们还提出了一种延迟一致的训练流程，在模仿学习和在线强化学习过程中注入推理推理延迟，使训练与异步部署对齐。为了支持真实评估，我们提出了DynaNav，一个用于动态环境中语言引导导航的物理精确、照片级逼真的仿真套件。在仿真和真实机器人上的大量实验表明，TIC-VLA在数秒推理延迟下保持稳健的实时控制，始终优于先前的VLA模型。

## Abstract
Robots in dynamic, human-centric environments must follow language instructions while maintaining real-time reactive control. Vision-language-action (VLA) models offer a promising framework, but they assume temporally aligned reasoning and control, despite semantic inference being inherently delayed relative to real-time action. We introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly models delayed semantic reasoning during action generation. TIC-VLA defines a delayed semantic-control interface that conditions action generation on delayed vision-language semantic states and explicit latency metadata, in addition to current observations, enabling policies to compensate for asynchronous reasoning. We further propose a latency-consistent training pipeline that injects reasoning inference delays during imitation learning and online reinforcement learning, aligning training with asynchronous deployment. To support realistic evaluation, we present DynaNav, a physics-accurate, photo-realistic simulation suite for language-guided navigation in dynamic environments. Extensive experiments in simulation and on a real robot show that TIC-VLA consistently outperforms prior VLA models while maintaining robust real-time control under multi-second reasoning latency.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 在动态、以人为中心的环境中，机器人需要同时遵循自然语言指令并保持实时反应式控制。视觉-语言-动作（VLA）模型被视为有前景的统一框架，但现有VLA存在一个隐含且不切实际的假设：语义推理与实时控制在时间上是对齐的。
- 实际上，VLM推理（尤其是边缘设备上）可能耗时数秒，而控制回路需以10Hz以上频率连续运行，导致语义状态反映的是过去的观测，而非当前状态——这构成了系统性的思考与控制时间错配。
- 过往工作要么将导航简化为离散视角转换（忽略动态和时序），要么依赖强大算力并暂停执行等待推理完成（不适用于动态环境）。即使异步或双系统架构也隐含假设语义输出是新鲜的。
- 本文认为推理延迟不仅是工程低效问题，更是基础建模问题：若延迟未被显式表示和训练，理想同步监督下训练的策略在部署时会严重退化。TIC-VLA旨在通过延迟感知框架解决这一异步推理下的鲁棒导航问题。

## 二、论文提出的方法论
- **核心思想**：不强制VLM实时推理，而是将延迟作为控制问题的输入——定义**延迟语义-控制接口**，使得动作策略既能获得延迟的高层语义特征，又能获得显式延迟元数据（延迟时长、自运动偏移），从而在时间语境中正确解释过时信息。
- **系统架构**：采用双系统设计
  - **慢速推理模块**：基于InternVL3-1B（InternViT-300M + Qwen2.5-0.5B），接收延迟9秒窗口内的历史图像和语言指令，输出语义推理链以及未来航路点（以推理启动时刻为参考）；其最后一层KV缓存作为语义特征传递。
  - **快速动作策略**：6层交叉注意力Transformer，输入包括：（1）当前共享视觉编码器输出的视觉token；（2）当前机器人状态（线速度、角速度）；（3）缓存的最新VLM KV缓存特征；（4）显式延迟元数据（有效延迟Δt、自运动偏移Δx/Δy/Δθ）。输出未来3秒（30步）的动作块。
- **延迟语义-控制接口**：提供KV缓存特征（含丰富语义上下文）与延迟时间、机器人移动量，使策略能够将过时语义“重解释”到当前机器人坐标系下。
- **多阶段延迟一致性训练**：
  1. **VLM监督微调**：使用GPT-5自动生成长距语言指令和结构化推理注释（当前情景、关键物体、运动趋势、任务进展、下一步计划），训练VLM输出推理+航点或仅航点。
  2. **带延迟注入的模仿学习**：从演示轨迹中统一采样[0,10]秒的推理延迟，条件化策略于延迟的VLM KV缓存和延迟元数据，使用SmoothL1损失训练动作预测。
  3. **异步指导的在线强化学习**：仅微调动作策略（冻结视觉编码器和VLM），在DynaNav动态环境中执行PPO，注入随机VLM推理延迟以匹配边缘部署特性；奖励函数包含到达目标、进度、碰撞惩罚和速度惩罚。
- **异步执行**：VLM后台持续推理，动作策略以10Hz运行，从不阻塞。每次控制步使用缓存的最新KV缓存和计算出的延迟元数据。补充材料提供了详细的异步生成算法。

## 三、实验设计
- **训练数据集**：
  - SCAND：8.7小时社交合规导航数据
  - GND：11小时校园环境导航数据
  - DynaNav仿真数据：自行收集，5.1小时，覆盖仓库、医院、办公室、室外场景（310个20秒片段）
- **全新Benchmark：DynaNav仿真套件**
  - 基于Isaac Sim，支持物理交互、动态行人、两种机器人（Nova Carter轮式、Spot四足）。
  - 包含85个测试用例：4种场景（医院/办公室/仓库/室外）× 不同人群密度（0-200）× 不同导航距离。
  - 支持人类遥操作采集演示和端到端模型控制。
- **基线方法**：
  - 点目标方法：BC、RL、NavDP（需要特权目标位置）
  - 语言引导VLA：NaVILA（7B，分层）、Uni-NaVid、DualVLN（7B，双系统）、MobileVLA、OmniVLA
  - 同步变体TIC-VLA (Sync.)：执行时阻塞等待推理
  - TIC-VLA无RL版本
- **评估指标**：NE（导航误差）、SR（成功率）、SPL（成功率加权路径长度）、CR（碰撞率）
- **真实世界测试**：Unitree Go2四足机器人，四类任务（室内走廊、办公室、室外广场、室外人行道），各5次，计算平均成功率。对比DualVLN (7B) 和NaVILA (7B)，分别在Jetson Orin NX、RTX 4060、RTX A6000上部署。

## 四、资源与算力
- **VLM SFT**：全参数微调，8×NVIDIA L40S GPU，每GPU batch size 2，AdamW优化器，初始化学习率2×10⁻⁵，cosine学习率调度，1000步warm-up，共10个epoch。
- **动作专家IL训练**：16 batch per GPU，初始化学习率2×10⁻⁴。
- **在线RL微调**：1×NVIDIA L40S GPU，400次PPO迭代，每轮1024 rollout步，3个任务在3个环境中轮流训练。
- **真实部署**：RTX 4060 Laptop GPU (50W) 作为主要计算平台，Jetson Orin NX (25W) 板载，RTX A6000仅用于基线（因基线模型更大）。VLM推理时延在RTX4060上约3.4秒，动作策略推理85ms。

## 五、实验数量与充分性
- **模拟实验组数**：主表包含8种基线 + TIC-VLA变体共11种方法对比。消融实验涵盖6组：
  1. 延迟鲁棒性分析（5种延迟设置，有无RL）
  2. 语义接口与延迟意识（4种组合）
  3. 测试时推理有无（2种对比）
  4. 动作预测视界（1/3/5秒）
  5. 自运动偏移有无
  6. 额外消融在补充材料：动作策略架构（扩散/流/查询）、VLM骨干（SmolVLM2/InternVL3/Qwen2.5-VL）、动作专家层数（3/6/12）、里程计噪声影响
- **真实实验**：4类任务×5次 = 20次试验，对比2种基线。
- **公平性**：所有语言基线在相同训练数据集上微调，相同模拟设置评估；点目标方法使用特权信息以提供难度参考。同步变体作为上限对比。
- **充分性**：实验覆盖了模拟和真实，多维度消融验证每个设计选择。模拟场景多样性高，但真实世界规模有限。

## 六、论文的主要结论与发现
- 在DynaNav基准上，TIC-VLA（带RL）实现最高SR（55.29%）和最低CR（28.24%），优于所有语言引导基线。不带RL的版本已与点目标方法NavDP竞争力相当（SR 47.06% vs 54.12%）。
- 延迟鲁棒性分析显示：RL微调后，即使在5秒推理延迟下仍保持约45%的成功率，而未RL的版本随延迟增加显著下降。
- KV缓存特征优于仅用航点接口，显式延迟元数据进一步显著提升性能。
- 测试时开启推理可提高成功率（从40%增至55%），虽然增加延迟但延迟控制可补偿。
- 动作预测视界3秒最佳，过长或过短均会降低性能。
- 显式自运动偏移是必需的，去除后SR从47%降至41%。
- 真实世界零样本迁移：TIC-VLA在RTX4060上实现85%平均成功率，远优于DualVLN（50%）和NaVILA（35%）；在Jetson Orin NX上仍达75%。
- 异步部署关键：同步变体（阻塞执行）在仿真中仅32.94%成功率，说明实时性比最新语义更重要。

## 七、优点
- **问题视角创新**：将推理延迟从工程问题提升为建模问题，提出显式延迟语义-控制接口，是核心区别。
- **训练-部署一致性**：三个阶段均使策略接触延迟语义输入，解决分布漂移。
- **评估完整性**：开源DynaNav物理精确仿真器（含动态行人、多平台），提供可复现基准。
- **边缘部署可行性**：在低功耗Jetson Orin NX上验证，显示实际应用潜力。
- **丰富消融**：系统验证延迟感知接口、KV缓存、自运动偏移、推理有无、预测视界、动作架构等设计选择，证据链充分。

## 八、不足与局限
- **运行时优化空间**：当前系统尚未完全针对推理速度优化，VLM推理约3.4秒仍可压缩。
- **真实世界评估规模有限**：仅4个任务×5次，需更大规模长期部署验证鲁棒性。
- **任务领域限制**：仅针对导航任务，未扩展至操作或其他机器人应用。
- **安全性依赖人工监督**：虽通过延迟感知降低了误撞风险，但在关键安全场景仍需人工介入。
- **VLM限制**：依赖InternVL3-1B和GPT-5生成训练数据，可能继承大模型偏见；仅在100B参数级别内实验，更大模型未测试（但文中指出更大模型延迟更长反而有害）。
- **模拟到真实差距**：真实环境中的光照、纹理、动态复杂性等不如仿真可控，200次真人测试仍显不足。

（完）
