---
title: "Vision-and-Language Navigation Today and Tomorrow: A Survey in the Era of Foundation Models"
title_zh: 视觉与语言导航的今天与明天：基础模型时代的综述
authors: "Yue Zhang, Ziqiao Ma, Jialu Li, Yanyuan Qiao, Zun Wang, Joyce Chai, Qi Wu, Mohit Bansal, Parisa Kordjamshidi"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/007-2024_zhang_vln_foundation_models_survey-e0642dd6-98211cc436e0.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Foundation Models", "query:Embodied AI", "query:Survey", "query:World Model"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航（VLN）要求智能体依据自然语言指令在复杂环境中执行导航任务，深度学习与基础模型的突破为这一领域注入新动力。本综述从具身规划与推理的顶层框架出发，系统梳理了近年来VLN方法如何利用基础模型（如大语言模型和视觉语言模型）应对指令解析、视觉感知、路径规划等核心挑战。关键成果表明，基础模型在零样本泛化、动态环境适应与长程规划方面展现显著优势，为VLN研究提供了新范式。本文旨在归纳当前进展、揭示开放问题，并为相关领域研究者提供参考与启示。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-007-98211cc436e0-vision-and-language-navigation-today-and-tomorrow-a-survey-in-the-era-of-foundation-models/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 859, \"height\": 690, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-007-98211cc436e0-vision-and-language-navigation-today-and-tomorrow-a-survey-in-the-era-of-foundation-models/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1699, \"height\": 801, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-007-98211cc436e0-vision-and-language-navigation-today-and-tomorrow-a-survey-in-the-era-of-foundation-models/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1660, \"height\": 840, \"label\": \"Table\"}]"
motivation: VLN面临环境复杂性与指令歧义等挑战，基础模型带来了新机遇，亟需系统性综述来梳理方法、探讨未来方向。
method: 采用具身规划与推理的顶层框架，分类讨论利用基础模型（如LLM、VLM）解决VLN中感知、推理、记忆等子问题的方法。
result: 总结了基础模型在零样本泛化、长程规划及多模态对齐上的优势，同时指出数据稀缺、动态场景适应等开放挑战。
conclusion: 基础模型为VLN开辟新范式，未来需强化多模态融合与跨场景泛化，推动从仿真到真实世界的迁移。
---

## 摘要
视觉与语言导航（VLN）近年来受到越来越多的关注，许多方法涌现以推动其发展。基础模型的显著成就塑造了VLN研究的挑战和方法。在本综述中，我们提供了一种自上而下的回顾，采用了一个具身规划与推理的原则框架，并强调了利用基础模型应对VLN挑战的当前方法和未来机遇。我们希望我们的深入讨论能够提供宝贵的资源和见解：一方面，记录进展并探索基础模型在这一领域的机遇和潜在角色；另一方面，为基础模型研究者组织VLN中的不同挑战和解决方案。

## Abstract
Vision-and-Language Navigation (VLN) has gained increasing attention over recent years and many approaches have emerged to advance their development. The remarkable achievements of foundation models have shaped the challenges and methods for VLN research. In this survey, we provide a top-down review that adopts a principled framework for embodied planning and reasoning, and emphasizes the current methods and future opportunities leveraging foundation models to address VLN challenges. We hope our in-depth discussions could provide valuable resources and insights: on the one hand, to document the progress and explore opportunities and potential roles for foundation models in this field, and on the other, to organize different challenges and solutions in VLN to foundation model researchers.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 视觉与语言导航（VLN）要求智能体依据自然语言指令在真实或仿真的三维环境中完成导航任务，是具身智能领域的核心问题之一。
- 传统VLN方法面临视觉环境复杂性、指令歧义、记忆建模困难、跨环境泛化能力弱等挑战。
- 随着BERT、CLIP、GPT-4等基础模型（Foundation Models）的兴起，为VLN带来了新的机遇，包括更强的多模态理解、常识推理和零样本泛化能力。
- 然而，现有综述多聚焦于基础模型出现之前的方法，未能系统梳理基础模型在VLN中的应用。
- 本文旨在采用一个系统化的框架（LAW框架：World Model, Human Model, Agent Model）对VLN研究进行自上而下的综述，探讨基础模型如何应对核心挑战，并展望未来方向。

## 二、论文提出的方法论
- **核心思想**：将VLN任务分解为三个相互关联的组件——世界模型（World Model）、人类模型（Human Model）和VLN智能体（Agent Model），并分别考察基础模型在每个组件中的作用。
- **世界模型**：
  - 目标：学习并表示视觉环境的记忆与动态，实现对未知环境的泛化。
  - 方法：使用基于Transformer的架构编码导航历史（如递归状态令牌、全景编码器、历史编码器）；引入图结构记忆（拓扑图、语义地图、栅格地图）；通过环境增强（EnvEdit、EnvMix、Pathdreamer等）合成新环境数据；利用CLIP等预训练视觉表示提高跨环境对齐。
- **人类模型**：
  - 目标：理解和解释人类提供的自然语言指令，处理歧义并适应不同语言风格。
  - 方法：利用CLIP匹配视觉语义与文本以消除歧义（如VLN-Trans、LANA+）；借助LLM的常识推理补充缺失信息（如SayCan、NavCoT）；设计信息寻求机制（何时问、问什么、谁回答），并使用LLM或VLM作为回答器或提问器（如VLN-Copilot、Fan et al.）。
  - 指令泛化：通过预训练文本表示（BERT、PREVALENT）增强语言理解；通过指令生成（Speaker-Follower、Marky、SRDF）合成多样化训练数据。
- **VLN智能体**：
  - 目标：实现语言-视觉的显式语义对齐、动态规划与决策。
  - 方法：显式语义接地（如动作原子概念学习、语法信息利用）；预训练VLN基础模型（HOP、LOViS、实体感知预训练）；基于图规划器（全局拓扑图、空间Transformer）和基于LLM的规划器（LLM-Planner、ThinkBot、SayNav）相结合；将VLM或LLM直接作为智能体后端（NavGPT、MapGPT、DiscussNav、Nav-CoT），并探索零样本、少样本或微调策略。

## 三、实验设计
- 本文为综述论文，不包含自主实验，而是系统调研并总结了现有VLN基准和方法。
- **数据集/场景**：覆盖了代表性室内外VLN基准（R2R、RxR、REVERIE、CVDN、VLN-CE、ALFRED、TEACh、TouchDown、Street Nav、AerialVLN等），并详细分类了每个基准的领域、环境、交互模式、动作空间和收集方式。
- **Benchmark**：以R2R为主要基准，评估指标包括导航误差（NE）、成功率（SR）、SPL、CLS、nDTW、sDTW等。
- **对比方法**：综述了从LSTM时代到Transformer再到基础模型时代的各种方法，并比较了其在核心挑战上的表现差异（如世界模型记忆编码、指令泛化、零样本规划等）。但未提供统一的数值表格，而是以定性分类和趋势分析为主。

## 四、资源与算力
- 本文未提及自身实验所使用的算力资源（GPU型号、数量、训练时长等）。
- 仅作为调研综述，无需训练或推理，因此未涉及算力说明。

## 五、实验数量与充分性
- 作为综述，本文覆盖了近40个基准、上百篇相关论文，从三个维度（世界模型、人类模型、智能体）进行了系统分类。
- 对每个维度下的子挑战（如历史编码、指令合成、规划策略）均列举了代表性方法，并讨论了优缺点和未解决问题。
- 实验分析的充分性：虽然未提供定量对比，但通过分类和趋势讨论，客观展现了当前方法的进展与局限。覆盖范围广泛，逻辑层次清晰，分析深度足够。
- 公平性：综述按照统一框架组织，对不同类型的方法进行了相对平衡的讨论，没有明显偏向某一特定方法。

## 六、论文的主要结论与发现
- 基础模型（尤其LLM和VLM）显著提升了VLN在零样本泛化、指令理解、动态规划等方面的能力，成为推动VLN发展的关键驱动力。
- 世界模型方面，从LSTM隐式记忆发展到Transformer显式历史编码，再结合图结构和环境增强数据，泛化能力大幅提升。
- 人类模型方面，基础模型提供了丰富的感知上下文和常识推理，有效缓解了指令歧义，并支持信息寻求和指令自动合成。
- 智能体方面，VLM直接作为导航骨干、LLM作为调度或规划器展示了强大潜力，但面临缺乏具身体验、产生幻觉等挑战。
- 未来方向：需要更统一和动态的基准、从2D到3D世界表示的跃迁、从指令到对话的扩展、以及基础模型在真实机器人上的部署。

## 七、优点
- **系统性框架**：采用LAW框架，将VLN问题结构化地拆分为世界模型、人类模型和智能体，逻辑清晰、覆盖全面。
- **前沿性**：聚焦基础模型时代，及时总结了LLM/VLM在VLN中的最新应用（如NavGPT、MC-GPT、Nav-CoT等），弥补了以往综述的空白。
- **细节丰富**：对每个子问题都给出了技术演进脉络，从传统方法到基础模型方法的转变均有说明。
- **未来导向**：明确指出了当前基准的局限性、数据偏差、动态场景缺失、真机部署难题等，为后续研究提供了清晰的方向。
- **资源开放**：提供了GitHub仓库，方便研究者快速获取相关文献和代码链接。

## 八、不足与局限
- **缺乏定量对比**：作为综述，没有提供统一的实验结果表格，读者难以横向比较不同方法在同一基准上的性能差异。
- **覆盖广度与深度平衡**：虽然覆盖了多个维度，但对某些具体方法的分析不够深入，例如对VLM微调策略的具体实现细节描述较少。
- **未涉及自身实验**：由于是综述性质，没有对文中观点进行实证验证，部分判断（如方法有效性）依赖作者主观分析。
- **潜在偏见风险**：主要引用近年的英文文献，对非英文或早期经典工作的覆盖可能不足，且未讨论不同基础模型间的公平性比较。
- **应用限制**：讨论的多数方法仍在仿真环境（如Matterport3D）中评估，对真实世界部署的挑战（感知差距、硬件限制、安全）提及有限，未深入分析。

（完）
