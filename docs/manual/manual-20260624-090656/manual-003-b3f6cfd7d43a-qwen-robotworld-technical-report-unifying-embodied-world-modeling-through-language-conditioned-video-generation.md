---
title: "Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation"
title_zh: Qwen-RobotWorld技术报告：通过语言条件视频生成统一具身世界建模
authors: Qwen Team
date: 2026-06-24
pdf: "https://arxiv.org/pdf/2606.17030v3"
arxiv_id: 2606.17030v3
arxiv_url: "https://arxiv.org/abs/2606.17030v3"
manual_pdf_url: assets/manual-pdfs/manual-20260624-090656/003-003-qwen-robotworld-technical-report_-unifying-embodied-world-modeling-through-language-conditioned-video-generation-b3f6cfd7d43a.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2606.17030v3", "query:language-conditioned video generation", "query:embodied world model", "query:action-language mapping", "query:multimodal diffusion transformer", "query:cross-task generalization"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 针对具身智能领域统一世界建模的挑战，Qwen-RobotWorld提出语言条件视频世界模型，以自然语言为统一动作接口，预测机器人操作、自动驾驶、室内导航和人机迁移中的未来视觉轨迹。通过双流MMDiT与MLLM动作编码、EWK数据集和通用+专家渐进式课程学习实现。在EWMBench和DreamGen Bench上排名第一，WorldModelBench和PBench上超越所有开源模型，展现强大泛化能力。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1646, \"height\": 413, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1585, \"height\": 767, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1639, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1626, \"height\": 1186, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1629, \"height\": 1079, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1613, \"height\": 1571, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1591, \"height\": 826, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1644, \"height\": 466, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1642, \"height\": 461, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1642, \"height\": 408, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1646, \"height\": 432, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1643, \"height\": 197, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1635, \"height\": 204, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1632, \"height\": 201, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1643, \"height\": 199, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1640, \"height\": 713, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1621, \"height\": 1023, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1621, \"height\": 703, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1680, \"height\": 1345, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1077, \"height\": 387, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1645, \"height\": 568, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1647, \"height\": 505, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-003-b3f6cfd7d43a-qwen-robotworld-technical-report-unifying-embodied-world-modeling-through-language-conditioned-video-generation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1649, \"height\": 518, \"label\": \"Table\"}]"
motivation: 现有具身世界模型缺乏统一接口，难以跨任务泛化。
method: 提出语言条件视频世界模型，含双流MMDiT、MLLM编码、EWK数据集及渐进课程学习。
result: EWMBench等四个基准第一或最优，优于所有开源模型。
conclusion: 语言统一建模有效，具身世界模型泛化性强，可用于数据生成、仿真测试和规划。
---

## 摘要
我们提出了QWEN-ROBOTWORLD，一种用于具身智能的语言条件视频世界模型。它以自然语言作为统一动作接口，从当前观测中预测物理基础的未来视觉轨迹，涵盖机器人操作、自动驾驶、室内导航以及人机迁移。这种统一形式提供了三个有前景的应用方向：用于策略训练增强的合成数据生成、用于策略评估的可扩展虚拟环境，以及用于下游机器人控制的语言引导规划信号。这通过三部分设计实现：a) 采用MLLM动作编码的双流MMDiT，b) 具身世界知识(Ewk)数据集，以及c) 通用+专家渐进式课程。该模型在EWMBench和DreamGen Bench上总体排名第一，在WorldModelBench和PBench上优于所有开源模型，并展现出鲁棒的泛化能力。

## Abstract
We introduce QWEN-ROBOTWORLD, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for policy evaluation, and language-guided planning signals for downstream robot control. This is achieved through a three-part design: a) Double-Stream MMDiT with MLLM Action Encoding, b) Embodied World Knowledge (EWK) dataset, and c) General+Expert Progressive Curriculum. The model ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open-source models on WorldModelBench and PBench, and demonstrates robust generalization.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 具身智能要求智能体在物理环境中感知、推理和行动，但真实世界训练成本高、效率低且存在安全风险。世界模型作为一种可扩展的替代方案，通过学习环境动态来提供交互式训练平台。
- 现有世界模型面临根本性矛盾：通用视频生成模型能学习丰富的视觉先验，但无法准确建模具身物理（如接触动力学、刚体结构约束）；领域特定的具身模型则针对单一场景（如桌面操作或驾驶）设计，依赖机器人特定的动作表示（如关节角度或航点），无法跨具身类型或任务类别泛化，限制了其作为跨平台仿真环境的实用性。
- 弥合这一鸿沟需要将多样的具身体验锚定在通用视觉先验中，并以自然语言作为统一动作接口，实现跨场景和跨任务的整合。不同具身领域提供互补的物理知识：操作教授精细接触物理，自动驾驶教授大尺度多智能体动力学和3D场景几何，室内导航教授房间级空间推理。这些领域共享语言接口，可以联合训练，相互强化。

## 二、论文提出的方法论
- **核心思想**：提出QWEN-ROBOTWORLD，一种语言条件视频世界模型，以自然语言作为统一动作接口，将机器人操作、自动驾驶、室内导航和人机迁移统一在同一框架下。模型预测给定当前观测和语言动作后的未来视觉轨迹，支持合成数据生成、策略评估和动作规划三类应用。
- **模型架构（双流MMDiT + MLLM动作编码）**：
  - 使用**双流多模态扩散Transformer（MMDiT）** 作为主干。理解流处理由冻结的Qwen2.5-VL提取的丰富语义特征（表示动作），生成流处理来自视频VAE的视觉潜变量（表示视觉状态）。两流通过每层的联合注意力交互，实现整个去噪过程中的双向跨模态融合。
  - 采用**MLLM（Qwen2.5-VL）** 作为动作编码器，优势：深度语言理解能力可准确解析复杂组合指令；内化的世界知识（如机器人臂是刚体）隐含约束物理上合理的状态转移，结合文本到图像（T2I）联合训练可防止物体变形，无需显式几何提示。
- **数据集（EWK：具身世界知识数据集）**：
  - 构建约**860万视频-文本对**（超2亿帧），包含四个具身领域和通用视频数据（占总量的30%）：操作（约590万样本，20+机器人形态，1300+技能）、自动驾驶（约20万样本）、室内导航（6000+语言引导片段）、人机迁移数据（通过自动化的MANO到机器人流水线，覆盖14种机器人形态）。
  - 核心贡献是**动作-语言映射框架**：将20+机器人形态、500+动作类别标准化为统一自然语言接口。采用分层五层注释流水线（任务目标层、动作细节层、物理反馈层、综合描述、简洁描述），确保每个字幕作为完整、自包含的动作规范。
- **训练策略（通用+专家渐进式课程）**：
  - **预训练阶段**：在通用领域数据上联合训练T2I、T2V和TI2V任务，建立基础视觉先验。T2I特别固定了正确的物体形态，可迁移到视频生成。
  - **SFT（微调+继续训练）阶段**：通过四阶段混合调度逐步引入具身数据（70%具身，30%通用）：单视图操作 → 多视图扩展 → 多视图拼接生成 → 复杂任务及跨域数据。具身部分操作约占90%采样权重，多视图拼接及导航/驾驶各占约5%，实现领域间稳定协同训练。
  - 使用**异步3D RoPE位置编码**和多视图拼接训练，实现同步相机视角的几何一致合成，无需架构修改。
- **Scene2Robot多段条件机制**：用于跨具身视频合成。输入序列分为三个连续段（场景条件F帧、机器人参考F帧、生成F帧），利用索引机制将条件token分配给时间步t=0并排除在损失计算外，生成段通过联合注意力同时关注场景外观和机器人运动轨迹，产生语义一致的跨具身合成。

## 三、实验设计
- **基准评测**：在四个已建立基准上评估：
  - **EWMBench**：评估具身世界模型的场景一致性、运动正确性和语义对齐，包含21个样本覆盖7个任务。
  - **DreamGen Bench**：评估机器人视频质量和物理对齐，使用GR1机器人形态的三个子集（环境泛化、物体泛化、行为泛化），使用Qwen2.5-VL作为评估器。
  - **PBench**：评估领域理解（通过QA对在6个领域上）和视觉质量（8个VBench指标）。
  - **WorldModelBench**：评估指令遵循、常识和物理一致性（5种违规类型：牛顿定律、质量守恒、流体动力学、穿透、重力），包含350个实例覆盖7个领域56个子领域。
- **对比方法**：
  - 通用视频生成模型：Sora2、Veo3、Wan2.6、Kling、LTX-2。
  - 具身世界模型：Cosmos、WoW、LVP、Vidar、GigaWorld。
- **定性分析**：进行了细粒度语言接地、跨具身/任务/视角泛化、零样本鲁棒性（RoboTwin-IF基准）评测，以及跨领域泛化（人机迁移、自动驾驶、室内导航）示例。
- **实现细节**：模型总参数量为MLLM 7B + VAE 127M + MMDiT 20B，上下文长度支持最多48,360个视频token。采用6层双流MMDiT块（24注意力头，头维度128，隐藏大小3072，补丁大小2×2）。训练使用flow matching目标，采用Megatron-LM和混合并行策略，选择性激活重计算以平衡内存和吞吐量。

## 四、资源与算力
- 论文**未明确说明**使用的具体GPU型号、数量及训练时长（如多少块A100、H100或训练天数）。提到使用Megatron-LM框架和混合并行策略，但未给出具体计算资源消耗。仅提及训练时应用选择性激活重计算以平衡内存使用和训练吞吐量，但无具体数值。

## 五、实验数量与充分性
- **实验数量**：在四个标准基准上进行了定量评估，包含多个维度和指标（如EWMBench有7个指标，PBench有8个质量指标，每个基准均与多种基线对比）。此外进行了定性分析（多个场景），消融性分析并未明确以单独实验形式呈现，但训练策略中四个阶段的渐进式注入本身就是一种隐式消融。还进行了零样本RoboTwin-IF评估。
- **充分性与公平性**：
  - 对比方法涵盖了当前主流通用和具身模型，包括多个闭源和开源模型。
  - 定量表格清晰标注最佳值（粗体）和次佳（下划线），结果可复现。
  - 定性示例直观展示了模型能力，且进行了零样本对比（与LVP和Cosmos2.5-14B），增强了说服力。
  - 但缺少严格的消融实验（如去掉人机迁移数据、去掉多视图训练、去掉MLLM编码器等）来验证各组件贡献，因此充分性稍显不足。此外，定性示例中未见失败案例的讨论，可能存在选择性展示。

## 六、论文的主要结论与发现
- QWEN-ROBOTWORLD在四个基准上达到了领先性能：
  - **EWMBench**：总体得分4.60，排名第一，比第二名LVP（4.05）高+0.55，在运动保真度（HSD：0.566，比LVP高33%）和场景一致性（SceneC：0.914）方面领先。
  - **DreamGen Bench**：总体得分4.952，排名第一，在GR1-Object子集的指令遵循（IF）上最高（0.878），物理对齐在所有子集上一致。
  - **WorldModelBench**：总体得分8.99，在所有开源模型中最高，仅次于闭源的Wan2.6和Veo3，物理一致性得分完美（四个类别均为1.00）。
  - **PBench**：总体得分0.804，在所有开源模型中最高，领域理解排名第三（0.857），运动平滑度排名第二（0.990）。
- 零样本RoboTwin-IF评估显示更强的指令遵循、动作真实感和跨视角一致性。
- 定性结果展示了细粒度语言接地、跨具身/任务/视角泛化、以及人机迁移、自动驾驶、室内导航等跨领域泛化能力。
- **核心发现**：使用自然语言作为统一动作接口，联合训练不同具身领域（操作、驾驶、导航、人机迁移）可以使模型获得互补的物理泛化能力，这是单领域模型无法达到的。通用+专家联合训练范式能够稳定地协同训练。

## 七、优点
- **统一框架的创新性**：首次将自然语言作为完全统一的动作接口，将机器人操作、自动驾驶、室内导航和人机迁移整合在单一视频生成模型中，无需任何领域特定的控制接口，为跨平台仿真提供了可能。
- **数据集构建的系统性**：EWK数据集规模大（860万对、2亿帧）、多样性高（20+机器人形态、500+动作类别），并且提出了动作-语言映射框架，标准化了异构动作表示，是重要的数据贡献。
- **训练策略的有效性**：通用+专家渐进式课程训练在保持广泛视觉先验的同时注入深度具身知识，避免了知识遗忘，并通过多阶段注入实现了稳定的多领域协同。
- **架构设计的合理性**：双流MMDiT充分发挥了MLLM的语义理解能力（冻结Qwen2.5-VL）和扩散模型的生成能力，通过联合注意力实现有效跨模态融合。异步3D RoPE和多视图拼接训练无需架构修改即可处理多视图一致性。
- **性能全面领先**：在多个基准上达到一流水平，尤其物理一致性得分完美，并且零样本泛化能力强。

## 八、不足与局限
- **计算资源未披露**：论文未提供具体的训练算力需求（GPU型号、数量、时长），增加了外界评估其可复现性和实际成本的难度。
- **缺乏消融实验**：虽然训练策略有四阶段渐进式注入，但并未提供严格的消融分析来量化各组件（如MLLM编码器 vs 轻量编码器、多视图数据、人机迁移数据、通用与具身数据比例等）的贡献，削弱了对方法设计的充分验证。
- **定性分析可能存在选择性偏差**：展示的所有生成案例均为成功案例，未呈现任何失败或边界情况，可能高估了模型的真实能力。
- **分辨率限制**：模型被指出输出分辨率低于通用视频生成模型，导致VBench等指标（美学质量、成像质量）较低。虽然论文声称分辨率足够下游控制任务，但在更广泛的使用场景（如高清仿真）中存在局限。
- **长期行为泛化短板**：在DreamGen Bench的GR1-Behavior子集中指令遵循分数低于LVP和GigaWorld，说明长期行为泛化仍是一个需要改进的方向。
- **跨领域覆盖不均衡**：操作数据占主导（约90%的具身部分），自动驾驶和室内导航数据占比很小（各约5%），可能导致在这些领域上的泛化能力相对较弱。

（完）
