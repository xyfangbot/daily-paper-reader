---
title: "DecoVLN: Decoupling Observation, Reasoning, and Correction for Vision-and-Language Navigation"
title_zh: DecoVLN：为视觉-语言导航解耦观察、推理与修正
authors: "Zihao Xin, Wentong Li, Yixuan Jiang, Bin Wang, Runmin Cong, Jie Qin, Shengjun Huang"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2603.13133v3"
arxiv_id: 2603.13133v3
arxiv_url: "https://arxiv.org/abs/2603.13133v3"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/003-2026_xin_decovln-251993dd-6c227ebc1d7f.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2603.13133v3", "query:Vision-and-Language Navigation", "query:Adaptive Memory Refinement", "query:Corrective Fine-tuning", "query:Long-horizon Navigation", "query:State-Action Pair"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航面临长期记忆构建和复合误差两大挑战。本文提出DecoVLN框架，通过自适应细化机制从历史候选池中优化选择帧，并引入基于测地距离的状态-动作对纠正微调策略来解决这些问题。实验表明该方法有效，并在真实环境中部署。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1809, \"height\": 656, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 863, \"height\": 548, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 875, \"height\": 608, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 860, \"height\": 428, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1725, \"height\": 768, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 840, \"height\": 814, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1790, \"height\": 1075, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1762, \"height\": 213, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1767, \"height\": 213, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1756, \"height\": 213, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 769, \"height\": 201, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 801, \"height\": 288, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1869, \"height\": 1112, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 783, \"height\": 243, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 796, \"height\": 247, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 840, \"height\": 382, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-003-6c227ebc1d7f-decovln-decoupling-observation-reasoning-and-correction-for-vision-and-language-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1691, \"height\": 276, \"label\": \"Table\"}]"
motivation: 现有方法难以构建有效长期记忆且易受复合误差影响，导致长程导航性能受限。
method: 提出自适应细化机制优化帧选择，并设计基于测地距离的状态-动作对纠正微调策略。
result: 实验证明DecoVLN在多个基准上取得优势，并成功部署于真实环境。
conclusion: DecoVLN通过解耦观察、推理和修正，有效提升长程视觉语言导航的鲁棒性和准确性。
---

## 摘要
视觉-语言导航（VLN）要求智能体遵循长程指令并在复杂的3D环境中导航。然而，现有方法面临两大挑战：构建有效的长期记忆库以及克服累积误差问题。为解决这些问题，我们提出DecoVLN，一种专为长程导航中鲁棒流式感知与闭环控制设计的高效框架。首先，我们将长期记忆构建形式化为一个优化问题，并引入自适应精化机制，通过迭代优化统一评分函数从历史候选池中选择帧。该函数联合平衡三个关键标准：与指令的语义相关性、与所选记忆的视觉多样性以及历史轨迹的时间覆盖度。其次，为缓解累积误差，我们提出一种状态-动作对级别的修正微调策略。通过利用状态之间的测地距离精确量化与专家轨迹的偏差，智能体在信任区域内收集高质量的状态-动作对，同时过滤掉低相关性的污染数据。这提高了错误修正的效率和稳定性。大量实验证明了DecoVLN的有效性，并且我们已将其部署于真实环境中。

## Abstract
Vision-and-Language Navigation (VLN) requires agents to follow long-horizon instructions and navigate complex 3D environments. However, existing approaches face two major challenges: constructing an effective long-term memory bank and overcoming the compounding errors problem. To address these issues, we propose DecoVLN, an effective framework designed for robust streaming perception and closed-loop control in long-horizon navigation. First, we formulate long-term memory construction as an optimization problem and introduce adaptive refinement mechanism that selects frames from a historical candidate pool by iteratively optimizing a unified scoring function. This function jointly balances three key criteria: semantic relevance to the instruction, visual diversity from the selected memory, and temporal coverage of the historical trajectory. Second, to alleviate compounding errors, we introduce a state-action pair-level corrective finetuning strategy. By leveraging geodesic distance between states to precisely quantify deviation from the expert trajectory, the agent collects high-quality state-action pairs in the trusted region while filtering out the polluted data with low relevance. This improves both the efficiency and stability of error correction. Extensive experiments demonstrate the effectiveness of DecoVLN, and we have deployed it in real-world environments.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 视觉-语言导航（VLN）要求智能体根据自然语言指令在复杂3D环境中进行长程导航，现有方法面临两大核心挑战：
  - **长期记忆构建困难**：传统方法要么采用低频间断感知（“Stop‑and‑Think”），导致感知盲区；要么采用全历史流式处理，但均匀采样或固定策略会稀释上下文信息密度，损害长程推理。
  - **复合误差问题**：VLN是序贯决策任务，早期微小动作误差会随时间累积，导致智能体严重偏离目标路径。现有方法多依赖开环轨迹增强，缺乏有效的闭环反馈和在线修正能力。
- 作者将VLN形式化为部分可观测马尔可夫决策过程（POMDP），核心挑战在于动态记忆管理、高效动作推理和及时策略修正。
- 论文提出**DecoVLN**框架，通过显式解耦观察、推理和修正三个过程，实现鲁棒的流式感知与闭环控制，旨在提升长程导航的稳定性和准确性。

## 二、论文提出的方法论
- **核心思想**：将VLN中的长期记忆构建转化为一个优化问题，通过联合优化语义相关性、视觉多样性和时间覆盖度三个指标，在线筛选高信息密度的历史帧；同时引入基于状态-动作对的纠正微调策略，在信任区域内收集高质量修正样本，抑制复合误差。
- **关键技术细节**：
  1. **自适应记忆精化机制（Adaptive Memory Refinement, AMR）**：
     - 解耦观察流与推理流，允许智能体在运动时连续感知环境。
     - 每一帧到达时，通过统一评分函数从候选池中选择K帧构成精化记忆M。评分函数同时考虑：
       - **语义相关性**：计算候选帧视觉嵌入与指令嵌入的余弦相似度。
       - **视觉多样性**：惩罚与已选记忆帧视觉相似度高的候选帧（取最大余弦相似度）。
       - **时间覆盖度**：惩罚与已选记忆帧时间距离近的候选帧（基于时间差倒数）。
     - 公式：\( f^* = \arg\max_{f \in C \setminus M} [\lambda_R \cdot \text{SimSem}(f,I) - (1-\lambda_R)(w_V \cdot \text{SimVis}(f,M) + w_T \cdot \text{SimTemp}(f,M))] \)，其中 \(\lambda_R\) 权衡相关性 vs. 冗余度，\(w_V + w_T = 1\)。
  2. **状态-动作对纠正微调策略（Corrective Fine‑tuning, CF）**：
     - 核心思想：在步级别（而非情节级别）进行修正，利用环境几何约束（测地距离）量化状态偏差。
     - 算法流程（Algorithm 1）：
       - 专家轨迹 \(P_{\text{exp}} = \{s^*_0, s^*_1, ..., s^*_N\}\)。
       - 智能体从初始状态 rollout，每步计算当前状态与专家轨迹的最小测地距离 \(DM(s_t)\)。
       - 若 \(0 < DM(s_t) \leq \tau\)（信任阈值），则调用专家策略 \(\pi^*\) 获取修正动作 \(a_t^{\text{exp}}\)，将状态-动作对 \((s_t, a_t^{\text{exp}}, f_t)\) 存入修正数据集 \(D_c\)。
       - 若 \(DM(s_t) > \tau\)，则终止该 episode，避免污染数据。
     - 修正数据与原始导航数据混合，用于微调 VLM，同时引入 LLaVA‑Video‑178K 数据集缓解灾难性遗忘。
- 整体框架：以 LLaVA‑Video‑7B 为基础，输入包括指令、当前帧和自适应精化后的记忆库，输出动作块（4个连续动作），实现类人闭环控制。

## 三、实验设计
- **数据集与场景**：
  - **训练数据**：从 Matterport3D 环境收集，包含 R2R‑CE、R2R‑EnvDrop、RxR‑CE 三个子集，共约 360K 样本（SFT 阶段）。
  - **修正微调阶段**：额外使用 Habitat 最短路径跟随器作为专家，收集约 180K 修正样本；同时引入 LLaVA‑Video‑178K 视频问答数据集防止灾难性遗忘。
  - **测试基准**：
    - R2R‑CE Val‑Unseen（连续环境，离散动作空间）
    - RxR‑CE Val‑Unseen（多语言、更复杂指令）
    - 自建长程导航验证集（轨迹长度 > 18m，共 536 条，平均 23m）
    - 真实环境：Unitree GO2 四足机器人在复杂办公室场景部署。
- **对比方法**：
  - 包含两大类别：依赖多传感器输入的 waypoint 模型（如 HPN+DN、VLN BERT、CMA、HAMT+ScaleVLN 等）和仅使用 RGB 输入的 VLN 模型（如 NaVid、VLN‑R1、Uni‑NaVid、NaVILA、StreamVLN 等）。
  - 特别与 SOTA 方法 StreamVLN（RGB 及 RGB+Depth 版本）进行多方位对比。
- **评估指标**：成功率（SR）、SPL（成功加权路径长度）、导航误差（NE）、Oracle成功率（OS）、nDTW。

## 四、资源与算力
- 模型基于 **LLaVA‑Video‑7B**，在 **8 块 NVIDIA A800 GPU** 上训练。
- 总训练时长约 **600 GPU‑小时**。
- 推理阶段使用 **单张 RTX 4090 GPU** 在远程服务器上部署。
- 采用 **AdamW 优化器**，语言模型峰值学习率 2×10⁻⁵，视觉编码器峰值学习率 5×10⁻⁶，batch size 为 128，记忆库大小 K=8，信任阈值 τ=3。

## 五、实验数量与充分性
- **主要实验**：
  - 在 R2R‑CE 和 RxR‑CE 两个标准基准上与 20 多种方法对比（表 1），覆盖 RGB‑only 及多模态方法。
  - **消融实验**：
    - 模块消融（表 2）：基准 → +AMR → +CF，逐步提升。
    - 记忆长度 K 消融（表 3）：K=2,4,8,12 的对比。
    - 超参数 λ_R, w_V, w_T 消融（图 2）。
    - 信任阈值 τ 消融（表 4）：τ=1,3,6。
    - 与传统 DAgger 算法对比（表 5）并在不同数据规模（240K vs 180K）下比较。
  - **长程导航验证**（图 5）：构建 536 条长轨迹验证集，对比 StreamVLN。
  - **真实环境部署**（图 4,8）：零样本迁移至 Unitree GO2 机器人，展示定性结果。
- **充分性评估**：实验覆盖标准基准、长程场景、真实世界迁移，消融充分验证各组件贡献，对比基线全面且公平。但仍存在一定局限（见第八部分）。

## 六、论文的主要结论与发现
- DecoVLN 在 R2R‑CE Val‑Unseen 上达到 SR 56.3%、SPL 50.5%，在 RxR‑CE 上达到 SR 54.2%、SPL 46.3%，均超越所有先前方法，包括使用了多传感器或大规模预训练数据的方法。
- **自适应记忆精化机制**显著提升上下文信息密度：相比均匀采样，SR 提升 3.6%，SPL 提升 2.2%。
- **纠正微调策略**有效缓解复合误差：在基线基础上 SR 提升 9.0%，NE 下降 0.88%。
- 长程导航验证集上，DecoVLN 相较 StreamVLN 在 SR、OS、NE 上分别提升 12.5%、14.2%、5.1%，展示了优异的泛化能力。
- 真实环境部署中，机器人能够在零微调下理解指令、规划路径，并展现出闭环反馈行为（如主动调整姿态保持目标在视野内），证明较强的 sim‑to‑real 迁移能力。
- 论文强调：在不依赖额外大规模数据集（如 ScaleVLN）的情况下仍能达到最优性能，说明数据效率和泛化潜力。

## 七、优点
- **创新性框架**：首次显式解耦观察、推理与修正三个过程，突破了传统流式方法中“存储‑采样‑推理”紧耦合的瓶颈，显著降低 I/O 延迟和存储开销。
- **自适应记忆精化**：将长期记忆构建形式化为带有语义、视觉、时间三个约束的优化问题，从源头上保证上下文的高信噪比，优于流式方法中事后体素剪枝策略（后者仍需深度传感器且无法过滤与任务无关帧）。
- **步级别纠正微调**：通过测地距离量化偏差并设信任阈值，精准收集高质量修正样本，避免了传统 DAgger 因污染数据导致的收敛问题，且数据效率更高（180K 数据即胜过 240K 的 DAgger）。
- **实时性与平台无关性**：输出符号化动作块，可迁移至不同机器人平台；通过动作块整体解析为连续运动，提升真实环境执行稳定性。
- **实验全面且公平**：涵盖标准基准、长程场景、真实部署，消融实验深入，对比方法包括近期 SOTA 且不低估基线。

## 八、不足与局限
- **算力需求仍高**：基于 7B 参数 VLM，无法在边缘设备（如 Jetson Orin）上全量推理，依赖远程服务器通信，引入网络延迟和连接风险。论文自身也指出未来需探索模型蒸馏。
- **对视觉依赖较强**：在视觉标志消失或感知混淆等极端场景下，智能体仍可能丢失方向，缺乏深层次内省恢复机制（如基于 CoT 的失败回溯）。
- **记忆大小固定**：K=8 在标准尺度下有效，但在极长轨迹（>30m）或开放大场景中可能不足，且固定大小无法自适应轨迹长度变化。
- **真实实验覆盖有限**：仅在一个办公室环境进行定性展示，未提供定量成功率或对比基线，泛化性尚需更系统的真实世界评估。
- **数据偏差风险**：训练数据全部来自 Matterport3D 仿真环境（室内），对室外、动态场景等未见环境的泛化能力未验证。
- **对比方法覆盖不完整**：未包括近期基于强化学习的模型（如 VLN‑R1 虽列出但未详细分析），且部分方法使用了大规模预训练数据，公平性上论文虽注明但仍有潜在偏差。

（完）
