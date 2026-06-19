---
title: "NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models"
title_zh: NavGPT：基于大型语言模型的视觉与语言导航显式推理
authors: "Gengze Zhou, Yicong Hong, Qi Wu"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/024-2024_zhou_navgpt-f23c6558-89aae6efbd2b.pdf
tags: ["query:手动上传", "paper:PDF", "query:vision-and-language navigation", "query:large language models", "query:zero-shot learning", "query:reasoning", "query:embodied agent"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉-语言导航(VLN)要求智能体理解指令并推理环境，现有方法多依赖特定训练。NavGPT利用大型语言模型(GPT-4)进行显式推理，将视觉观察、导航历史和候选方向转化为文本输入，零样本预测导航动作。在多个VLN基准上，无需额外训练即可达到与有监督方法相当的性能，展示了LLMs在复杂具身任务中的通用推理能力。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1421, \"height\": 834, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1442, \"height\": 623, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1432, \"height\": 557, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1424, \"height\": 437, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1401, \"height\": 442, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1335, \"height\": 1878, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 586, \"height\": 2165, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1388, \"height\": 2255, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 611, \"height\": 2275, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1381, \"height\": 2254, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 604, \"height\": 2260, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 609, \"height\": 2248, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1081, \"height\": 395, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 796, \"height\": 173, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-024-89aae6efbd2b-navgpt-explicit-reasoning-in-vision-and-language-navigation-with-large-language-models/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 799, \"height\": 168, \"label\": \"Table\"}]"
motivation: 现有VLN方法缺乏显式推理且需大量训练，而LLMs展现出强大推理能力，可用于零样本导航。
method: 将视觉观察、历史轨迹和候选方向序列化为文本，输入LLM进行状态推理并输出导航动作。
result: 在多个VLN数据集上零样本导航，性能接近有监督方法，验证了LLM的推理有效性。
conclusion: LLMs可作为通用推理引擎，为具身导航提供新范式，推动通用智能体发展。
---

## 摘要
通过前所未有的数据规模训练，ChatGPT和GPT-4等大型语言模型（LLM）从模型扩展中展现出显著推理能力的涌现。这一趋势凸显了训练具有无限语言数据的LLM的潜力，推动了通用具身智能体的发展。在这项工作中，我们介绍了NavGPT，一种纯基于LLM的指令跟随导航智能体，通过执行零样本顺序动作预测来揭示GPT模型在复杂具身场景中的推理能力，用于视觉与语言导航（VLN）。每一步，NavGPT将视觉观察的文本描述、导航历史和未来可探索方向作为输入，推理智能体当前状态，并做出接近目标的决策。

## Abstract
Trained with an unprecedented scale of data, large language models (LLMs) like ChatGPT and GPT-4 exhibit the emergence of significant reasoning abilities from model scaling. Such a trend underscored the potential of training LLMs with unlimited language data, advancing the development of a universal embodied agent. In this work, we introduce the NavGPT, a purely LLM-based instruction-following navigation agent, to reveal the reasoning capability of GPT models in complex embodied scenes by performing zero-shot sequential action prediction for vision-and-language navigation (VLN). At each step, NavGPT takes the textual descriptions of visual observations, navigation history, and future explorable directions as inputs to reason the agent’s current status, and makes the decision to approach the target.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：视觉与语言导航（Vision-and-Language Navigation, VLN）要求智能体根据自然语言指令在未知环境中进行顺序动作预测。现有方法大多依赖大量监督训练、数据增强或预训练，缺乏显式推理能力，且决策过程不透明。
- **动机**：大型语言模型（LLM）如GPT-4因海量文本训练展现出强大的涌现推理能力，有望作为通用具身智能体的核心引擎。作者希望探索LLM能否在零样本（zero-shot）条件下理解交互世界、动作及后果，并直接解决VLN任务。
- **整体含义**：证明了LLM可显式执行导航规划（子目标分解、常识整合、地标识别、进度跟踪、异常处理），为构建可解释、可泛化的通用导航智能体提供了新范式。

## 二、论文提出的方法论
- **核心思想**：构建一个纯LLM驱动的零样本导航系统NavGPT，将视觉观察、导航历史和候选方向全部转化为文本，输入LLM进行状态推理并输出下一步动作。
- **关键技术细节**：
  - 系统架构：包含视觉基础模型（VFMs，如BLIP-2用于图像描述、Faster-RCNN用于目标检测、深度估计）、历史缓冲区、GPT-3.5摘要器（压缩长历史）和提示管理器。
  - 视觉翻译：每个视点获取24张图像（8方向×3俯仰角），BLIP-2生成每张图像描述，再用GPT-3.5摘要为一个方向语句；同时提取目标类别、距离（3米内）和深度信息。
  - 推理与动作协同（ReAct）：定义动作空间 `Ã = A ∪ R`，其中R为语言推理轨迹。每个步骤先输出Thought（推理），再输出Action（选择视点ID移动）。
  - 提示管理器：组装导航系统原则（P）、指令（W）、视觉描述（F(O)）、历史（H）为单一prompt，格式固定，强制LLM按格式输出。
- **公式表示**：  
  `<R_{t+1}, A_{t+1}> = LLM( M(P), M(W), M(F(O_t)), M(H_{≤t}) )`  
  其中M为提示管理器，F为VFMs，H为历史三元组（观察、推理、动作）。

## 三、实验设计
- **数据集与基准**：
  - 使用R2R-VLN数据集（7197条轨迹，每个轨迹3条指令），涵盖训练集（61场景）、验证已知（56场景）、验证未知（11场景）、测试未知（18场景）。
  - 主要评估在验证未知集的783条轨迹上进行。
- **评估指标**：路径长度（TL）、导航误差（NE）、成功率（SR）、Oracle成功率（OSR）、SPL（成功率加权路径长度）。
- **对比方法**：
  - 有监督方法：Seq2Seq、Speaker Follower、EnvDrop、PREVALENT、VLN-BERT、HAMT、DuET等。
  - 零样本基线：DuET（利用LXMERT初始化，无训练）以及NavGPT自身变体。
- **消融实验**：
  - 视觉粒度对比：FoV@60（12视图）、FoV@30（36视图）、FoV@45（24视图）。
  - 视觉组件影响：Baseline（仅BLIP-2描述）、+Obj（添加目标检测）、+Obj+Dis（再添加深度距离）。
- **定性分析**：展示GPT-4在导航中的推理轨迹，包括短/长指令进度跟踪、子目标分解、常识推理、异常处理；额外测试GPT-4生成导航指令和绘制俯视轨迹的能力。

## 四、资源与算力
- **未明确说明**：论文未提及具体GPU型号、数量或训练时长。因为NavGPT是纯零样本系统，不进行任何模型训练，所有生成均通过调用GPT-4/GPT-3.5 API完成，视觉模型使用预训练模型BLIP-2 ViT-G FlanT5XL和Faster-RCNN，这些本身需要预训练资源但论文未讨论。
- 实验中使用GPT-3.5进行摘要和消融，GPT-4用于主要定性及定量对比，需要API费用，具体计算量未报告。

## 五、实验数量与充分性
- **实验数量**：
  - 主定量对比（表1）：在R2R验证未知集上，NavGPT与8种有监督方法及1个零样本基线对比。
  - 消融实验（表2、表3）：各3组变体（视觉粒度、视觉组件），每组在216个样本（72场景×3指令）上评估。
  - 定性分析：大量展示推理示例（图3、图4），包括成功案例（图11-17）和失败案例（图10）。
- **充分性与公平性**：
  - 对比方法均为当时SOTA，涵盖训练/微调/预训练派别，但NavGPT是零样本，性能差距较大，对比公平性需注意。
  - 消融实验规模较小（216条），虽覆盖72场景，但每条轨迹仅一个样本，可能存在方差。
  - 定性分析详细，但缺少统计显著性检验。
  - 总体实验较充分，验证了LLM推理能力，但零样本性能与有监督方法差距明显，作者也承认这一局限。

## 六、论文的主要结论与发现
- **主要结论**：LLM（特别是GPT-4）能够零样本执行VLN任务，展现出显式推理能力：
  - 可将指令分解为子目标、整合常识（如知道楼梯是向上走的）、识别地标、跟踪进度、异常时调整计划。
  - GPT-4还能根据导航历史生成高质量指令描述和准确的俯视轨迹地图，证明其空间和时间感知能力。
- **性能对比**：NavGPT零样本SR=34%，SPL=29%，远低于有监督方法（如DuET SR=72%），但优于无训练DuET baseline（SR=1%）。
- **瓶颈**：视觉描述的信息丢失（BLIP-2对目标细节的遗漏）和历史摘要导致的精细跟踪能力下降。

## 七、优点
- **方法创新**：首次纯LLM+ReAct框架实现VLN零样本导航，决策过程完全可解释（输出自然语言思考过程），不依赖任何VLN数据训练。
- **系统设计完整**：提示管理器、历史缓冲区、摘要器、多视觉模型集成，展示了如何将多模态信息转化为LLM可理解的文本。
- **定量+定性分析丰富**：不仅报告指标，还深入分析推理轨迹，揭示LLM的高层规划能力（子目标、常识、异常处理）。
- **在线生成能力**：证明LLM可反向生成导航指令和轨迹地图，有希望用于数据增强。

## 八、不足与局限
- **性能差距大**：零样本SR=34%，远低于有监督方法，实际应用中不可靠。
- **信息损失严重**：依赖BLIP-2描述，目标易被遗漏；历史摘要进一步丢失细节，导致agent在长指令中失去上下文。
- **环境限制**：仅在R2R模拟环境中测试，未在连续空间或真实机器人上验证泛化性。
- **算力未透明**：依赖GPT-4 API，成本高且不公开计算资源，实验可重复性受限。
- **实验规模有限**：消融实验仅216条样本，且未在测试集上报告；对比方法仅选“无训练”版本作为基线，不完全公平。
- **依赖强LLM**：GPT-4版本表现优于GPT-3.5，说明对模型规模敏感，较小LLM可能无法胜任。
- **未见讨论**：未见对failure modes的统计分类，如因描述不完整导致的探索无限循环、地标错认等未量化。

（完）
