---
title: "Vision-and-Language Navigation Today and Tomorrow: A Survey in the Era of Foundation Models"
title_zh: 视觉与语言导航的今天和明天：基础模型时代的综述
authors: "Yue Zhang, Ziqiao Ma, Jialu Li, Yanyuan Qiao, Zun Wang, Joyce Chai, Qi Wu, Mohit Bansal, Parisa Kordjamshidi"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/030-vln_survey1-85ee05c5-37d06cbb7609.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Foundation Models", "query:Embodied AI", "query:World Model", "query:Human Model"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉与语言导航（VLN）任务要求智能体根据自然语言指令在真实环境中行动，基础模型的出现带来了新机遇与挑战。本综述采用具身规划与推理框架，系统梳理了利用基础模型解决VLN问题的当前方法，包括多模态感知、语义地图构建和基于大语言模型的决策等。文章总结了现有方法的优势与局限，并展望了未来研究方向，如视觉-语言预训练对齐、交互式学习等，为VLN研究提供了全面参考。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-030-37d06cbb7609-vision-and-language-navigation-today-and-tomorrow-a-survey-in-the-era-of-foundation-models/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 859, \"height\": 690, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-030-37d06cbb7609-vision-and-language-navigation-today-and-tomorrow-a-survey-in-the-era-of-foundation-models/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1699, \"height\": 801, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-030-37d06cbb7609-vision-and-language-navigation-today-and-tomorrow-a-survey-in-the-era-of-foundation-models/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1660, \"height\": 840, \"label\": \"Table\"}]"
motivation: 基础模型在VLN中展现潜力，但现有综述缺乏自上而下的具身推理视角，需系统整理其方法、挑战与未来机会。
method: 采用具身规划与推理框架，分类讨论预训练、多模态融合、动态规划等策略，并对比基础模型驱动的VLN方法优劣势。
result: 指出基础模型提升VLN泛化性，但在细粒度指令理解、动态环境适应上仍有瓶颈，需进一步发展持续学习与交互能力。
conclusion: 基础模型将成为VLN核心动力，未来应加强视觉-语言联合预训练与具身反馈循环，推动通用导航智能体落地。
---

## 摘要
视觉与语言导航（VLN）近年来受到越来越多的关注，许多方法涌现以推动其发展。基础模型取得的显著成就塑造了VLN研究的挑战和方法。在本综述中，我们提供了一个自上而下的回顾，采用了一个具身规划与推理的原则性框架，并强调了利用基础模型应对VLN挑战的当前方法和未来机遇。我们希望我们的深入讨论能够提供有价值的资源和见解：一方面，记录进展并探索基础模型在该领域的机遇和潜在角色；另一方面，向基础模型研究人员组织VLN中的不同挑战和解决方案。

## Abstract
Vision-and-Language Navigation (VLN) has gained increasing attention over recent years and many approaches have emerged to advance their development. The remarkable achievements of foundation models have shaped the challenges and methods for VLN research. In this survey, we provide a top-down review that adopts a principled framework for embodied planning and reasoning, and emphasizes the current methods and future opportunities leveraging foundation models to address VLN challenges. We hope our in-depth discussions could provide valuable resources and insights: on the one hand, to document the progress and explore opportunities and potential roles for foundation models in this field; on the other, to organize different challenges and solutions in VLN to foundation model researchers.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 视觉与语言导航（VLN）是具身AI的关键任务，要求智能体根据自然语言指令在三维环境中导航。
- 传统VLN方法受限于小型监督数据集、浅层多模态对齐和缺乏泛化能力。近年来，基础模型（如BERT、CLIP、GPT-4、LLaMA等）在多模态理解和推理上取得突破，为VLN带来新机遇。
- 现有VLN综述多来自“前基础模型时代”，缺乏对LLM/VLM在VLN中作用的系统整理。本文采用LAW框架（World Model – Human Model – Agent Model），自上而下地组织VLN挑战与解决方案，并重点分析基础模型如何服务于世界模型、人类模型和VLN智能体。
- 研究意义：一方面里程碑式记录基础模型推动的VLN进展，另一方面向基础模型研究者系统展示VLN中的关键问题和已有方案。

## 二、论文提出的方法论
- 核心思想：将VLN问题解构为三大核心组件——世界模型（学习与表示视觉环境）、人类模型（理解与交流）和VLN智能体（推理与规划），并围绕基础模型的四种角色（预训练视觉表示、感知上下文与常识、信息寻求、智能体模型）组织方法分类。
- 关键技术路线：
  - **世界模型**：历史与记忆编码（多模态Transformer、状态令牌、可检索记忆库；图结构历史如拓扑图、语义地图、栅格地图）；环境泛化（预训练视觉表示如CLIP；环境增强如EnvEdit、EnvMix、Pathdreamer；大规模域内预训练如Airbert、VLN-BERT）。
  - **人类模型**：解决模糊指令（利用CLIP的感知上下文和LLM的常识推理消歧；主动寻求帮助如VLN-Copilot、不确定性对齐）；指令泛化（预训练文本表示如BERT；指令合成如Marky、PASTS、Speaker-Follower框架）。
  - **VLN智能体**：语言-视觉-语义显式对齐（动作原子概念学习、空间关系建模）；VLN预训练（HOP、LOViS、实体感知预训练）；规划（图规划器利用全局信息；LLM规划器如LLM-Planner、Mic、SayNav分解子目标）；直接作为智能体（VLM作为核心如CLIP-NAV、Recurrent VLN-BERT；LLM作为零样本智能体如NavGPT、MapGPT、DiscussNav；或微调LLM如NavCoT、LangNav）。
- 算法流程描述：以NavGPT为例，将视觉观测转换为文本描述（标题+空间信息），拼接指令和历史，输入GPT-4，输出下一步动作或子目标，可结合链式思维（CoT）增强推理。
- 无公式或复杂伪代码，本文为综述性质，以分类框架和代表性方法介绍为主。

## 三、实验设计
- 本文是综述，自身不进行实验。但系统对比了各方法在公开VLN基准上的表现，主要基准包括：
  - **室内**：R2R（Matterport3D，离散图）、RxR（多语言）、REVERIE（目标导向）、VLN-CE（连续环境）、ALFRED（导航+操作）、TEACh/DialFRED（对话式）。
  - **室外**：TouchDown（Google街景）、Talk2Nav、AerialVLN（无人机）等。
- 评估指标：Navigation Error（NE）、Success Rate（SR）、Success rate weighted by Path Length（SPL）、Coverage Weighted by Length Score（CLS）、nDTW/sDTW。
- 对比方法层次：从LSTM-Seq2Seq（早期），到基于Transformer的预训练模型（PREVALENT、HOP、Airbert），再到LLM/VLM智能体（NavGPT、MapGPT、NavCoT、InstructNav）。文中提供了大量文献引用和定性比较，但未提供统一的定量表格。

## 四、资源与算力
- 本文为综述，未报告自身训练或推理所需算力。
- 提及的代表性工作通常使用：
  - 预训练阶段：多卡GPU（如8×V100或A100），训练数天至一周（如HOP、Airbert）。
  - LLM/VLM智能体：依赖闭源API（如GPT-4）或开源的7B~70B参数模型，零样本推理无需额外训练，但微调仍需4~8张A100。
- 部分研究（如NavCoT）使用LLaMA-2/3等模型进行指令微调，算力需求因模型大小而异。
- 总体而言，基础模型在VLN中的使用显著增加了计算开销，但本文未提供具体数字。

## 五、实验数量与充分性
- 本文作为综述，未设计自身实验，而是总结了数百篇论文的方法与结果。
- 覆盖广泛：从早期方法到最新LLM智能体，横跨室内外、单轮/多轮对话、离散/连续空间、静态/动态环境等多个维度。
- 充分性评价：分类详尽（世界模型、人类模型、智能体模型共三个大节，每小节包含多条技术路线），文献引用几乎涵盖主要VLN会议和期刊论文，具有权威性和系统性。
- 但以下方面存在局限：
  - 未提供统一测试集上的定量性能表格，难以直接比较不同家族方法的绝对优劣。
  - 对部分新兴基准（如HA-VLN、Hazard）的讨论较简略，可能因发表时间较早。
  - 消融实验和统计显著性分析缺失，因为综述本身不做实验。

## 六、论文的主要结论与发现
- 基础模型（尤其是LLM和VLM）已成为VLN研究的主流工具，显著提升了零样本能力、跨环境泛化、指令理解鲁棒性和规划灵活性。
- 核心结论：
  1. **预训练至关重要**：域内预训练（如Airbert、HOP、Masked Path Modeling）比通用VLM（如Oscar、LXMERT）更有效。
  2. **LLM作为规划器有效但受限**：LLM可以分解子目标、提供常识，但依赖视觉转文字，可能丢失空间细节，且存在幻觉问题。
  3. **交互式学习成为趋势**：多轮对话、主动询问、纠正错误是处理模糊指令的关键，基础模型可作为信息寻求者或助手。
  4. **3D表示仍是瓶颈**：当前主要使用2D预训练特征，3D基础模型（如3D-LLM、ConceptFusion）尚在探索，缺乏对空间关系和动态变化的深度建模。
  5. **现实部署差距大**：从仿真到真实机器人存在感知、体现代差和训练数据稀缺等挑战。

## 七、优点
- **系统性框架**：采用LAW（World–Human–Agent）原则性框架，逻辑清晰，便于理解VLN全貌。
- **时代恰当**：聚焦基础模型时代，填补了先前综述的空白，及时整理了LLM/VLM在VLN中的应用。
- **平衡讨论**：既展示进展，也明确指出局限性（数据偏差、幻觉、3D不足、真实部署困难）。
- **丰富分类**：从挑战、方法到未来方向层层递进，图表总结清晰（Table 1汇总基准，Figure 2展示方法分类）。
- **资源丰富**：提供了GitHub仓库和大量参考文献，便于研究者快速入门。

## 八、不足与局限
- **作为综述的固有局限**：未提供定量对比实验，无法直接比较不同方法的性能；未给出可复现的代码或配置文件。
- **覆盖深度参差**：对部分子领域（如室外导航、多智能体协作）讨论较浅，主要围绕室内静态场景。
- **数据偏差讨论不足**：虽指出R2R偏爱最短路径，但未深入分析数据集偏见对模型泛化的具体影响。
- **真实部署验证少**：仅简要提及机器人实验（如HELPER），缺乏对现实环境适应性、计算资源约束（边缘设备）的详细分析。
- **时效性**：部分最新工作（如2024年提出的NavGPT-2、BEHAVIOR-1K、Hazard）在综述中仅简要提及，可能存在滞后。
- **缺乏理论保证**：基础模型在VLN中多依赖经验效果，缺乏可解释性证明或跨任务迁移能力的理论分析。

（完）
