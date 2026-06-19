---
title: "NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models"
title_zh: NavGPT：基于大语言模型的视觉与语言导航中的显式推理
authors: "Gengze Zhou, Yicong Hong, Qi Wu"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/021-navgpt-acd8bccb-8c04d692a0fd.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Large Language Models", "query:Zero-shot Learning", "query:Embodied Agent", "query:Reasoning"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航任务需要智能体理解指令与环境交互。现有方法依赖大量训练数据。本文提出NavGPT，利用大型语言模型（如GPT）的推理能力实现零样本导航。NavGPT将视觉观察、历史轨迹等转为文本输入，进行高层次规划，如分解子目标、识别地标、动态调整。实验表明其能生成高质量指令与轨迹地图，但零样本性能仍逊于监督学习模型。贡献在于揭示了LLM在具身推理中的潜力，并为多模态融合提供思路。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1421, \"height\": 834, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1442, \"height\": 623, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1432, \"height\": 557, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1424, \"height\": 437, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1401, \"height\": 442, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1335, \"height\": 1878, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 586, \"height\": 2165, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1388, \"height\": 2255, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 611, \"height\": 2275, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1381, \"height\": 2254, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 604, \"height\": 2260, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 609, \"height\": 2248, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1081, \"height\": 395, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 796, \"height\": 173, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-021-8c04d692a0fd-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 799, \"height\": 168, \"label\": \"Table\"}]"
motivation: 探索大语言模型在复杂具身场景中的推理能力，无需微调即可实现视觉语言导航任务。
method: 将视觉观测、导航历史等转为文本提示，输入GPT模型进行零样本顺序动作预测，并显式执行高层规划。
result: NavGPT能分解指令、融合常识、识别地标、跟踪进度并适应异常；零样本R2R任务性能不及有监督模型。
conclusion: LLM具备显式推理与规划能力，可辅助训练模型；未来需融合多模态输入以提升视觉导航效果。
---

## 摘要
通过前所未有的数据规模训练，像ChatGPT和GPT-4这样的大语言模型（LLMs）从模型扩展中展现出显著的推理能力。这一趋势突显了利用无限语言数据训练LLM的潜力，推动了通用具身智能体的发展。在本工作中，我们引入了NavGPT，一个纯粹基于LLM的指令跟随导航智能体，通过为视觉与语言导航（VLN）执行零样本顺序动作预测，揭示GPT模型在复杂具身场景中的推理能力。在每一步，NavGPT将视觉观察的文本描述、导航历史和未来可探索方向作为输入，推理智能体的当前状态，并做出接近目标的决策。通过全面的实验，我们证明了NavGPT可以显式地执行高级导航规划，包括将指令分解为子目标、整合与导航任务解决相关的常识知识、从观察场景中识别地标、跟踪导航进度，以及通过计划调整适应异常情况。此外，我们展示了LLM能够从路径上的观察和动作生成高质量的导航指令，并且能够根据智能体的导航历史绘制准确的俯视度量轨迹。尽管使用NavGPT进行零样本R2R任务的性能仍不及训练模型，但我们建议为LLM适配多模态输入以用作视觉导航智能体，并利用LLM的显式推理来有益于基于学习的方法。

## Abstract
Trained with an unprecedented scale of data, large language models (LLMs) like ChatGPT and GPT-4 exhibit the emergence of significant reasoning abilities from model scaling. Such a trend underscored the potential of training LLMs with unlimited language data, advancing the development of a universal embodied agent. In this work, we introduce the NavGPT, a purely LLM-based instruction-following navigation agent, to reveal the reasoning capability of GPT models in complex embodied scenes by performing zero-shot sequential action prediction for vision-and-language navigation (VLN). At each step, NavGPT takes the textual descriptions of visual observations, navigation history, and future explorable directions as inputs to reason the agent’s current status, and makes the decision to approach the target. Through comprehensive experiments, we demonstrate NavGPT can explicitly perform high-level planning for navigation, including decomposing instruction into sub-goal, integrating commonsense knowledge relevant to navigation task resolution, identifying landmarks from observed scenes, tracking navigation progress, and adapting to exceptions with plan adjustment. Furthermore, we show that LLMs is capable of generating high-quality navigational instructions from observations and actions along a path, as well as drawing accurate top-down metric trajectory given the agent’s navigation history. Despite the performance of using NavGPT to zero-shot R2R tasks still falling short of trained models, we suggest adapting multi-modality inputs for LLMs to use as visual navigation agents and applying the explicit reasoning of LLMs to benefit learning-based models.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：视觉与语言导航（VLN）中，现有方法通常依赖大量标注数据和复杂训练，缺乏可解释的推理过程。大语言模型（如 GPT-4）展示了强大的推理能力，但其在具身导航任务中的潜力尚未被充分探索。
- **整体含义**：本文旨在探索能否直接利用预训练 LLM 的推理能力，以零样本方式完成视觉与语言导航任务，同时显式揭示其规划过程，为构建通用具身智能体提供新思路。

## 二、论文提出的方法论
- **核心思想**：构建一个纯 LLM 驱动的导航系统 NavGPT，将视觉观测、导航历史、系统原则等信息全部转化为自然语言提示，输入 LLM（GPT-3.5/GPT-4），由 LLM 进行显式推理并输出下一步动作（选择导航图中的某个视点 ID）。
- **关键技术细节**：
  - **视觉感知**：使用 BLIP-2 将每个视点的 24 张 egocentric 图像（8 方向 × 3 俯仰角）转化为自然语言描述；同时使用 Faster-RCNN 检测物体并提取深度信息，辅助定位。
  - **提示管理器（Prompt Manager）**：将导航系统原则（任务定义、行为约束）、指令、历史轨迹（使用 GPT-3.5 摘要压缩）、当前观测拼接成结构化提示。
  - **推理与行动协同（ReAct）**：在每个步骤中，LLM 先输出“Thought”进行推理（如分解子目标、识别地标、跟踪进度），再输出“Action”选择下一个视点 ID。
  - **历史管理**：利用历史缓冲区存储 <观测摘要，推理，动作> 三元组，通过 GPT-3.5 摘要器压缩观测描述，避免提示过长。
- **公式或算法流程**：整体策略可表示为 `xRt+1, At+1y = LLM(M(P), M(W), M(F(Ot)), M(H<t+1))`，其中 M 为提示管理器，P 为系统原则，W 为指令，F 为视觉基础模型，H 为历史。

## 三、实验设计
- **数据集**：R2R（Room-to-Room）数据集，包含 7189 条轨迹，每条对应 3 条精细指令。实验主要在 **val unseen** 分割（11 个未见场景，783 条轨迹）上进行评测。
- **Benchmark 指标**：轨迹长度（TL）、导航误差（NE）、成功率（SR）、Oracle 成功率（OSR）、加权成功率（SPL）。
- **对比方法**：
  - **监督方法**：Seq2Seq、Speaker Follower、EnvDrop（仅用训练）；PREVALENT、VLN-BERT、HAMT、DuET（预训练+微调）。
  - **零样本基线**：DuET（初始化 LXMERT，无训练）作为参考。
- **额外实验**：
  - 消融实验分析视觉观测粒度（FoV 45° 24 views vs. 60° 12 views vs. 30° 36 views）。
  - 消融实验分析物体检测与深度信息的影响（Baseline vs. +Obj vs. +Obj+Distance）。
  - 定性质性分析：展示了 GPT-4 在多个案例中的推理轨迹（子目标分解、常识融合、异常处理等）。
  - 额外能力演示：用 GPT-4 根据历史生成导航指令和绘制俯视图。

## 四、资源与算力
- 论文未明确说明训练所用的 GPU 型号、数量和时长，因为 NavGPT 是零样本系统，**未进行任何微调**，仅使用预训练 LLM（GPT-3.5/GPT-4）进行推理；视觉基础模型（BLIP-2、Faster-RCNN）也使用预训练权重。因此论文没有报告训练算力开销。

## 五、实验数量与充分性
- **实验数量**：主要定量实验包括：
  1. 与 7 种监督方法在 R2R val unseen 上的对比（见表 1）。
  2. 3 组视觉粒度消融实验（表 2）。
  3. 3 组视觉组件消融实验（表 3，Baseline vs. +Obj vs. +Obj+Dist）。
  4. 大量定性案例分析（图 3 展示了 4 类推理模式，图 4 展示指令生成和地图绘制）。
- **充分性**：
  - 定量对比覆盖了主流的监督方法，为零样本方法提供了公平参考。
  - 消融实验有控制变量，验证了视觉粒度、物体检测、深度信息的重要性。
  - 定性分析充分展示了 LLM 的推理能力，并提供了具体案例。
  - 但零样本性能远低于监督方法，且未在 test unseen 分割上报告结果（仅用 val unseen），也未与其他零样本方法（如 CLIP-Nav、LGX）进行定量对比，存在一定不足。

## 六、论文的主要结论与发现
- **主要结论**：LLM（尤其是 GPT-4）在 VLN 中具备显式的高层规划能力，包括指令分解、常识整合、地标识别、进度跟踪、异常调整等。
- **发现**：
  - LLM 可以生成高质量的导航指令和准确的俯视轨迹图，说明其对历史与空间关系有良好感知。
  - NavGPT 的零样本性能（SR=34%，SPL=29%）仍远逊于监督方法（如 HAMT SR=66%），瓶颈在于视觉信号转语言时的信息损失以及历史摘要导致的信息衰减。
  - 物体检测和深度信息能显著提升性能（+Obj 使 SR 从 11.11% 升至 15.97%）。

## 七、优点
1. **可解释性**：通过显式的“Thought”输出，揭示了 LLM 在导航过程中的推理链条，使规划过程透明化。
2. **零样本能力**：无需任何 VLN 数据微调，直接利用预训练知识完成任务，展示了 LLM 的泛化潜力。
3. **模块化系统设计**：将视觉感知、历史管理、提示整理等功能解耦，便于集成不同的视觉基础模型。
4. **多任务扩展**：LLM 不仅用于导航决策，还能生成指令和绘制地图，展现了超出单一任务的能力。

## 八、不足与局限
1. **性能差距显著**：零样本 SR（34%）远低于监督模型（如 DuET 72%），难以直接应用于实际场景。
2. **信息损失严重**：视觉描述依赖 BLIP-2，丢失细节；历史摘要进一步压缩信息，导致长轨迹中目标跟踪困难。
3. **实验覆盖有限**：
   - 未在 R2R test unseen 以及更难的 R4R、RxR 数据集上评测。
   - 未与其他零样本 VLN 方法（如 CLIP-Nav、LGX）进行定量比较，缺少公平的零样本基线对比。
   - 仅使用 Matterport3D 模拟器，未在真实机器人上验证。
4. **计算成本**：推理时需多次调用 LLM（每一步一次），且使用 GPT-4 成本较高，不具备实时性。
5. **对提示工程敏感**：系统性能和推理质量高度依赖提示设计，可能在不同环境中不稳定。

（完）
