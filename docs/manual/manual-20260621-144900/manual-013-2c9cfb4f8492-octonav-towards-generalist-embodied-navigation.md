---
title: "OctoNav: Towards Generalist Embodied Navigation"
title_zh: OctoNav：迈向通用具身导航
authors: "Chen Gao, Liankai Jin, Xingyu Peng, Jiazhao Zhang, Yue Deng, Annan Li, He Wang, Si Liu"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2506.09839v1"
arxiv_id: 2506.09839v1
arxiv_url: "https://arxiv.org/abs/2506.09839v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/013-2025_gao_octonav-144dea1a-2c9cfb4f8492.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2506.09839v1", "query:Generalist Embodied Navigation", "query:Multi-modal Instruction", "query:Think-Before-Action", "query:OctoNav-Bench", "query:OctoNav-R1"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 机器人导航研究长期分化为ObjNav、ImgNav、VLN等独立任务，缺乏通用性。本文提出OctoNav-Bench大规模基准和OctoNav-R1通用导航模型，通过自动标注管道构建含自由形式多模态指令与思考过程的数据集，并设计混合训练范式（含TBA-SFT、Nav-GPRO和在线强化学习阶段），使模型能基于2D观测输出底层动作。实验表明OctoNav-R1显著优于以往方法，为通用具身导航迈出关键一步。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1435, \"height\": 682, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1429, \"height\": 723, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1353, \"height\": 514, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1435, \"height\": 601, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1141, \"height\": 356, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1293, \"height\": 535, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1119, \"height\": 325, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1443, \"height\": 821, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 861, \"height\": 736, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1440, \"height\": 433, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1006, \"height\": 518, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 373, \"height\": 299, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1000, \"height\": 680, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1148, \"height\": 742, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1432, \"height\": 745, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1433, \"height\": 743, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1432, \"height\": 739, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1434, \"height\": 738, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1414, \"height\": 495, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1417, \"height\": 494, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1413, \"height\": 492, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1428, \"height\": 364, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1423, \"height\": 486, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 500, \"height\": 159, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 391, \"height\": 187, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1423, \"height\": 241, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 430, \"height\": 188, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1414, \"height\": 146, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1414, \"height\": 182, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 979, \"height\": 598, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-013-2c9cfb4f8492-octonav-towards-generalist-embodied-navigation/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1419, \"height\": 186, \"label\": \"Table\"}]"
motivation: 现有导航任务设置与模态割裂，缺乏能处理任意多模态多能力自由形式指令的通用导航智能体。
method: 提出OctoNav-R1，基于MLLM的VLA模型，利用TBA-CoT数据集进行思考-动作冷启动微调，再通过Nav-GPRO和在线RL提升推理与动作能力。
result: 在OctoNav-Bench上，OctoNav-R1的导航成功率与路径效率均超越基线方法，尤其在复杂指令下表现突出。
conclusion: 通过引入思考-动作机制与混合训练范式，首次实现具备推理能力的通用导航模型，为具身智能统一框架提供新方向。
---

## 摘要
具身导航是具身智能广泛追求中的基础支柱。然而，先前的导航研究被划分为不同的任务/能力，例如ObjNav、ImgNav和VLN，它们在任务设置/目标和模态上有所不同，导致数据集和方法各自独立设计。在这项工作中，我们朝着通用导航智能体迈出步伐，这些智能体能够遵循包含多模态和多能力任意组合的自由形式指令。为实现这一目标，我们提出了一个大规模基准和相应方法，称为OctoNav-Bench和OctoNav-R1。具体来说，OctoNav-Bench具有连续环境，并通过设计的自动标注流程构建。我们彻底构建了用于模仿学习的指令-轨迹对，其中指令是自由形式的，具有任意模态和能力。同时，我们在OctoNav-Bench内精心构建了一个“行动前思考”（TBA-CoT）数据集，以提供行动背后的思考过程。对于OctoNav-R1，我们基于多模态大语言模型构建，并将其适配为视觉-语言-动作类型模型，该模型仅基于2D视觉观察即可产生低级动作。此外，我们设计了一个混合训练范式，包括三个阶段：Action-/TBA-SFT、Nav-GPRO和在线RL阶段。每个阶段包含专门设计的学习策略和奖励。重要的是，对于TBA-SFT和Nav-GRPO设计，我们受到OpenAI-o1和DeepSeek-R1的启发，它们通过“回答前思考”展示了令人印象深刻的推理能力。因此，我们旨在研究如何在具身导航领域实现“行动前思考”，以提高模型向通用智能体的推理能力。具体来说，我们提出TBA-SFT，利用TBA-CoT数据集作为冷启动阶段微调模型，然后利用Nav-GPRO提升其思考能力。最终，OctoNav-R1相比先前方法表现出更优的性能。

## Abstract
Embodied navigation stands as a foundation pillar within the broader pursuit of embodied intelligence. However, previous navigation research is divided into different tasks/capabilities, e.g., ObjNav, ImgNav and VLN, where they differ in task settings/objectives and modalities, making datasets and methods are designed individually. In this work, we take steps toward generalist navigation agents, which can follow free-form instructions that include arbitrary compounds of multi-modal and multi-capability. To achieve this, we propose a large-scale benchmark and corresponding method, termed OctoNav-Bench and OctoNav-R1. Specifically, OctoNav-Bench features continuous environments and is constructed via a designed automatic annotation pipeline. We thoroughly craft instruction-trajectory pairs for imitation learning, where instructions are diverse in free-form with arbitrary modality and capability. Also, we elaborately construct a Think-Before-Action (TBA-CoT) dataset within OctoNav-Bench to provide the thinking process behind actions. For OctoNav-R1, we build it upon MLLMs and adapt it to a VLA-type model, which can produce low-level actions solely based on 2D visual observations. Moreover, we design a Hybrid Training Paradigm (HTP) that consists of three stages, i.e., Action-/TBA-SFT, Nav-GPRO, and Online RL stages. Each stage contains specifically designed learning policies and rewards. Importantly, for TBA-SFT and Nav-GRPO designs, we are inspired by the OpenAI-o1 and DeepSeek-R1, which show impressive reasoning ability via thinking-before-answer. Thus, we aim to investigate how to achieve thinking-before-action in the embodied navigation field, to improve model's reasoning ability toward generalists. Specifically, we propose TBA-SFT to utilize the TBA-CoT dataset to fine-tune the model as a cold-start phrase and then leverage Nav-GPRO to improve its thinking ability. Finally, OctoNav-R1 shows superior performance compared with the previous methods.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：现有具身导航研究被划分为多个独立任务（如 ObjNav、PointNav、ImgNav、Ins-ImgNav、VLN 等），各任务在设置、目标、输入模态上差异巨大，导致数据集和方法彼此割裂，无法构建能遵循自由形式、多模态、多能力指令的通用导航智能体。
- **核心问题**：如何设计一个统一的大规模基准和模型，使导航智能体能够同时处理任意组合的导航能力（如同时包含坐标、视觉、语言指令），并具备“行动前思考”的推理能力。
- **整体含义**：首次向通用导航智能体迈出系统性一步，提出了集数据、模型、训练范式于一体的完整方案，促进具身导航从碎片化走向统一。

## 二、论文提出的方法论
- **OctoNav-Bench 基准构建**：
  - 自动标注管道：通过能力采样器生成包含多种导航能力的指令模板，在 400+ 3D 场景（MP3D/HM3D/Gibson/ProcTHOR）中采样轨迹，将占位符（图像、坐标、物体类别）实例化为具体元素，最终得到 45k+ 指令-轨迹对。
  - TBA-CoT 数据集构建：利用 Qwen-VL 提取当前和历史图像描述，输入 DeepSeek-R1 生成结构化的思考文本（`<Think>...</Think><Action>...</Action>`），共 10k+ 条，用于监督模型培养行动前思考能力。
- **OctoNav-R1 模型设计**：
  - 基于 LLaMA-VID 的 VLA 架构：视觉编码器（EVA-CLIP）处理历史视频、当前图像、目标图像，通过 Q-Former 风格查询生成器得到查询令牌，与多模态指令嵌入一起送入 Vicuna-7B LLM，直接输出低级动作（前进/左转/右转/停止）及其幅度。
- **混合训练范式 (HTP)**：
  - **Stage I: Action-SFT**：使用指令-轨迹对进行监督微调，损失为交叉熵，使模型学会基本动作跟随。
  - **Stage I: TBA-SFT**：使用 TBA-CoT 数据微调模型以 `<Think>...</Think><Action>...</Action>` 格式输出，赋予思考能力。
  - **Stage II: Nav-GRPO**：采用分组相对策略优化，对每个样本采样 G 个输出，根据步进奖励函数（精确匹配得1，动作正确但幅度偏差得0.5，否则0）计算优势，加入 KL 散度约束，提升思考质量。
  - **Stage III: Online RL**：在连续模拟环境中使用 A2C 算法，以距离变化和成功与否设计即时奖励，引入评论家网络，进行在线试错学习。

## 三、实验设计
- **数据集与环境**：
  - 训练场景：MP3D、HM3D、Gibson、ProcTHOR 共 400+ 室内环境，测试在 40+ 未见过的场景上进行。
  - 数据量：45k+ 指令-轨迹对；10k+ TBA-CoT 样本；连续模拟环境（Habitat 模拟器）。
- **基准对比方法**：
  - 作为 MLLM Agent：Qwen-VL、Video-LLaVA、LLaVA-NeXT。
  - 面向离散环境的方法：NaviLLM*、NavGPT-2*（修改输出头适应连续环境并微调）。
  - 面向连续环境的方法：NaVid、Uni-NaVid（及其在 OctoNav-Bench 上微调的版本）。
- **评估指标**：成功率 (SR)、成功率加权路径长度 (SPL)、Oracle 成功率 (OSR)；分别计算总体及各能力子指标、不同难度指令（简单/中等/困难）的分项指标。

## 四、资源与算力
- **训练配置**：
  - 硬件：8 块 NVIDIA A800 40G GPU；在线 RL 阶段使用 1 块 A800。
  - 学习率：SFT 阶段 2e-5；在线 RL 阶段 2e-6。
  - 批次大小：每张 GPU 2。
  - 训练步数：Action-SFT 约 10k 步；TBA-SFT 约 6k 步；Nav-GRPO 1k 步；Online RL 500 步。
  - 参数高效微调：全部使用 LoRA。
- 文中未提及总训练时长或具体吞吐量，仅给出上述可复现细节。

## 五、实验数量与充分性
- **实验数量与覆盖**：共进行多组实验：
  - 主表格对比八种基线方法，报告总体和五种能力的 SR/SPL/OSR。
  - 消融实验：HTP 各阶段逐步添加（Base→Action-SFT→TBA-SFT→Nav-GRPO→Online RL）。
  - 奖励类型对比（严格/宽松/步进）、提示模板多样性对比、思考频率对比（每 10/20/40 步）、不同难度指令（简单/中等/困难）对比。
  - 附录中还包含更多可视化示例和详细数据分布分析。
- **充分性与公平性**：
  - 消融实验设计系统，逐级叠加验证每个组件贡献。
  - 基线方法经过公平改造（修改为连续环境输出、微调）和重新评估，避免直接套用原有接口。
  - 测试场景均为训练时未见过场景，确保泛化性考察。
  - 实验全面，分析角度多（能力分解、难度分层、奖励设计、思考频率），结论可信度较高。

## 六、论文的主要结论与发现
- **性能提升显著**：OctoNav-R1 在总体 SR 达 19.40%，远超最佳基线 Uni-NaVid†（9.20%），在所有子能力上均领先。
- **思考机制有效**：TBA-SFT 将总体 SR 从 8.80% 提升至 14.40%，Nav-GRPO 进一步提升至 17.00%，证明推理能力对复杂多模态导航至关重要。
- **混合训练必要**：在线 RL 进一步将 SR 提升至 19.40%，说明试错学习能优化策略效率。
- **思考频率不敏感**：每 20 步思考效果最佳（19.40% SR），但仍需未来研究动态思考时机。
- **Sim2Real 可行性**：真实机器人初步部署显示零微调下可完成多阶段指令，验证了基准和数据质量。

## 七、优点
- **统一性和通用性**：首次将五种导航能力融合在自由形式指令中，支持任意多模态组合，真正实现“通用”导航。
- **行动前思考机制**：借鉴 DeepSeek-R1 模式，将 CoT 推理引入具身导航，显著提升复杂任务完成率。
- **混合训练范式完整性**：从离线模仿到在线强化，到推理增强，逻辑严密、可复现。
- **数据质量高**：自动化管道生成+人工审核，TBA-CoT 通过多阶段融合生成高质量推理文本。
- **全面的实验验证**：消融充分，对比方法多样，包含 Sim2Real 部署验证，说服力强。

## 八、不足与局限
- **幻觉问题**：VLM 可能产生视觉幻觉，导致导航决策错误，论文未深入探索缓解方案。
- **思考频率固定**：当前采用固定步数思考，未实现自适应思考时机（如场景复杂时更频繁），该方向留待未来。
- **实验局限**：仅在室内场景测试，户外/动态障碍物场景未覆盖；Sim2Real 仅初步演示，未进行大规模真实世界量化评估。
- **计算资源消耗**：多阶段训练需多 GPU 长时间训练，对资源要求较高，可能限制平民化复现。
- **评估指标依赖**：成功距离阈值设定是否普适有待讨论；VLN 子任务对齐精度可能受轨迹采样偏差影响。

（完）
