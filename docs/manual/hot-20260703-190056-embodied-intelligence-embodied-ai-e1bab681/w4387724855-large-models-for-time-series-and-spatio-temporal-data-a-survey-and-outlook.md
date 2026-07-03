---
title: "Large Models for Time Series and Spatio-Temporal Data: A Survey and Outlook"
title_zh: 面向时间序列与时空数据的大模型：综述与展望
authors: "Ming Jin, Qingsong Wen, Yuxuan Liang, Chaoli Zhang, Siqiao Xue, Xue Wang, James Zhang, Yi Wang, Haifeng Chen, Xiaoli Li, Shirui Pan, Vincent S. Tseng, Yu Zheng, Lei Chen, Hui Xiong, Qingsong Wen"
date: 2026-06-23
pdf: "https://doi.org/10.1145/3821637"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:alibaba group"]
score: 9.0
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=35; institution_filter=company; company_relation_match=alibaba group; relation_source=affiliation; institutions=Griffith University, Center for Inquiry; query=embodied intelligence"
tldr: 时间序列与时空数据在众多实际场景中广泛存在，大语言模型等基础模型正加速其分析。本综述从数据类型、模型类别、模型范围及应用领域四个维度系统梳理了专用大模型，划分为LM4TS和LM4STD两大组，并区分通用与领域专用模型。此外整理了相关数据集与工具资源，为该领域的后续研究提供全面参考。
source: openalex
selection_source: hot_paper_scout
motivation: 时间序列和时空数据由大量物理与虚拟传感器生成，传统方法难以充分挖掘其丰富信息，大模型有望提升跨域模式识别和推理能力。
method: 按数据类型、模型类别、模型范围和应用领域四个维度组织文献，将现有工作分为LM4TS和LM4STD，并进一步区分通用与领域专用模型，同时整理相关资源。
result: 梳理了大量针对时间序列和时空数据的大模型，包括通用及领域专用模型，并汇总了主流数据集、模型实现和工具，按应用领域分类。
conclusion: 该综述系统总结了基于大模型的时间序列分析进展，突出了基础、应用、资源和开放研究机会，为推进相关领域研究提供了全面指导。
---

## 摘要
时间序列与时空数据等时序数据在现实应用中无处不在。物理传感器与虚拟传感器生成的海量数据记录了动态系统行为，并支撑着广泛的下游任务。有效分析此类数据对于挖掘其丰富的信息内容至关重要。大语言模型及其他基础模型的最新进展加速了它们在时间序列与时空数据挖掘中的应用。这些方法不仅提升了跨领域的模式识别与推理能力，还促进了能够理解并处理时序数据的人工通用智能的发展。本综述从数据类型、模型类别、模型范围及应用领域/任务四个维度，对面向时间序列与时空数据定制或适配的大模型进行了全面且时新的梳理。我们将现有工作分为两大主要类别：用于时间序列分析的大模型（LM4TS）与用于时空数据挖掘的大模型（LM4STD），并进一步区分通用模型与领域专用模型。我们还按主要应用领域整理了相关资源，包括数据集、模型实现及工具。总体而言，本综述整合了近期进展，并突出了以大模型为中心的时序数据分析的基础、应用、资源及开放研究机遇。

## Abstract
Temporal data — including time series and spatio-temporal data — are pervasive in real-world applications. Generated in massive volumes by physical and virtual sensors, they record dynamic system behaviors and enable a wide range of downstream tasks. Effectively analyzing such data is crucial to unlocking their rich information content. Recent advances in large language models and other foundation models have accelerated their use in time series and spatio-temporal data mining. These approaches not only improve pattern recognition and reasoning across diverse domains but also support progress toward artificial general intelligence that can understand and process temporal data. In this survey, we present a comprehensive, up-to-date review of large models tailored or adapted for time series and spatio-temporal data along four dimensions: data types, model categories, model scopes, and application areas/tasks. We organize existing work into two main groups: large models for time series analysis (LM4TS) and for spatio-temporal data mining (LM4STD), and further distinguish general-purpose from domain-specific models. We also curate related resources, including datasets, model implementations, and tools, organized by major application areas. Overall, this survey consolidates recent advances and highlights foundations, applications, resources, and open research opportunities in large model–centric temporal data analysis.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- 时序数据（包括时间序列和时空数据）在现实应用中无处不在，由物理和虚拟传感器大规模生成，记录动态系统行为，支撑广泛的下游任务。
- 传统方法难以充分挖掘其丰富的信息内容，大语言模型和其他基础模型的快速发展为时间序列与时空数据挖掘带来了新的机遇。
- 本文是一篇综述，旨在从数据类型、模型类别、模型范围和应用领域四个维度，系统梳理面向时序数据定制或适配的大模型，并整理相关资源，为该领域后续研究提供全面参考。

## 二、论文提出的方法论

- 本文为综述论文，并未提出新的方法或算法。
- 其方法论体现在对现有工作的系统化组织方式：将现有工作分为两大组——用于时间序列分析的大模型（LM4TS）和用于时空数据挖掘的大模型（LM4STD）。
- 进一步区分通用模型（如Chronos、MOMENT）与领域专用模型（如用于医疗、金融、气象等领域的模型）。
- 同时从数据类型、模型类别、模型范围、应用任务四个维度对文献进行分类，并整理了相关数据集、模型实现和工具资源。

## 三、实验设计

- 作为综述论文，本文没有设计新的实验。
- 文章引用了大量已有工作的实验设置，例如在UCR时间序列存档、M4竞赛、MIMIC-III医疗数据集、LargeST交通数据集等标准基准上的结果。
- 对比的方法包括传统统计方法、深度学习方法以及各种大模型变体，但本文并未进行统一的实验对比。

## 四、资源与算力

- 本文未提及具体计算资源（如GPU型号、数量、训练时长），因为这不是一篇实验性论文。
- 文中引用的各原始工作可能有各自的算力说明，但本文未汇总。

## 五、实验数量与充分性

- 综述覆盖了数百篇相关文献（参考文献列表长达296条），从分类和讨论的角度看是较为充分的。
- 但作为综述，未进行统一的实验验证，因此不能评价实验的客观性与公平性。其价值在于系统梳理和未来方向指引。

## 六、论文的主要结论与发现

- 大模型在时序数据分析中展现出巨大的潜力，能提升跨域模式识别和推理能力，并推动通用人工智能的发展。
- 现有工作可系统分为LM4TS和LM4STD两类，通用模型与领域专用模型各有优势。
- 未来开放研究方向包括：多模态融合、模型可解释性、算力效率、稀疏数据适应、长序列建模、因果推理等。
- 提供了丰富的资源列表（数据集、模型实现、工具），有助于研究者快速进入该领域。

## 七、优点

- 结构清晰：从四个维度（数据类型、模型类别、模型范围、应用领域）组织文献，逻辑性强。
- 覆盖面广：囊括了时间序列和时空数据两大主线，并区分通用与领域专用，全面反映了2026年前后的最新进展。
- 实用性强：整理了开源数据集、模型实现和工具，便于研究者复现和对比。
- 视角前瞻：强调了向人工通用智能（AGI）发展的趋势，并对未来研究方向给出了明确指引。

## 八、不足与局限

- 作为综述论文，没有进行统一的实验评估，难以直接判断不同方法的相对优劣。
- 对某些新兴方向（如视频时空数据、知识图谱时序推理）的覆盖可能不够深入，主要聚焦于数值时间序列与结构化时空数据。
- 资源整理可能随时间推移而失效，需持续更新。
- 未深入讨论模型部署、计算成本、隐私保护等实际落地问题。

（完）
