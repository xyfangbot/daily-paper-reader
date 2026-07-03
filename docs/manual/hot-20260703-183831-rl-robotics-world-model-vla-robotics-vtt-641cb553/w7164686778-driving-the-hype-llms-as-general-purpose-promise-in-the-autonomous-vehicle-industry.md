---
title: "Driving the hype: LLMs as ‘general-purpose’ promise in the autonomous vehicle industry"
title_zh: 驱动炒作：大型语言模型在自动驾驶汽车行业中的“通用”承诺
authors: "Alex Gekker, Sam; id_orcid 0000-0001-8347-3695 Hind"
date: 2026-06-22
pdf: "https://www.tandfonline.com/doi/pdf/10.1080/1369118X.2026.2689026?needAccess=true"
tags: ["query:热点论文筛选", "query:world-model", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; institutions=University of Amsterdam, University of Manchester; query=find world models used in autonomous driving and interactive simulation"
tldr: 自动驾驶行业在十年挫败后转向LLM技术以重启商业化。本文技术图像分析Nvidia GTC 2024及41份灰色文献，研究Wayve和Waabi如何借用LLM“通用性”声称克服AV 1.0限制。他们依赖基础模型、多模态、并行分词、知识蒸馏等假设（AV 2.0），但缺乏实证，言论高度投机。揭示LLM通用性话语构成行业炒作，为审视AI技术推广提供分析视角。
source: openalex
selection_source: hot_paper_scout
motivation: 揭示自动驾驶企业如何利用LLM的‘通用性’话语克服前期失败，并批判其创新主张的投机性。
method: 对Nvidia GTC 2024进行技术图像分析，并结合41份灰色文献（企业通讯、技术预印本、行业期刊、监管文件）。
result: Wayve和Waabi大量引入基础模型、多模态等LLM假设，但这些技术尚未在自动驾驶领域证实，创新主张高度投机。
conclusion: LLM的‘通用性’叙事在自动驾驶行业中属于炒作，它为企业提供了将LLM嵌入新领域的论述模板。
---

## 摘要
自动驾驶汽车的支持者正宣告一个新时代的到来，其驱动力源自大型语言模型（LLMs）的创新。在经历了十年高度公开的失败以及资本和注意力同步转向生成式AI之后，自动驾驶汽车行业的企业已将LLM风格的技术视为重新启动商业化努力的基础。通过对年度行业活动Nvidia GTC 2024的技术图志分析以及41份相关灰色文献（企业通讯、技术预印本、行业新闻和监管文件）的研究，我们考察了两家自动驾驶汽车公司Wayve和Waabi如何通过话语框架将这些技术描述为能够克服迄今为止阻碍完全自动驾驶未来（AV 1.0）的技术、经济、金融和监管限制。我们发现，这些主张在很大程度上依赖于LLM所谓的“通用性”，即将关于基础模型、多模态训练、并行分词和知识蒸馏（AV 2.0）广泛适用性的假设引入到一个这些技术尚未得到充分验证的领域。所讨论的创新在本质上具有高度投机性，并助长了围绕LLM风格方法在自动驾驶汽车行业可行性的炒作话语。通过宣扬通用性的主张，它们为支持者如何试图将LLM嵌入新行业和领域提供了蓝图。

## Abstract
Proponents of autonomous vehicles are proclaiming a new era, driven by innovations derived from large language models (LLMs). Following a decade of highly public failures and the concurrent redirection of capital and attention towards generative AI, firms in the autonomous vehicle industry have turned to LLM-style techniques as the basis for a rebooted commercialisation effort. Through a technographic analysis of an annual industry event, Nvidia GTC 2024, and 41 sources of related grey literature (firm communications, technical preprints, trade journalism, and regulatory documents), we examine how two autonomous vehicle firms, Wayve and Waabi, discursively frame these techniques as capable of overcoming the technical, economic, financial, and regulatory limits that have so far thwarted a fully-autonomous future (AV 1.0). We find that these claims draw heavily on the supposed ‘general-purposivity’ of LLMs, importing assumptions about the broad applicability of foundation models, multimodal training, parallel tokenisation, and epistemic distillation (AV 2.0) into a domain where they remain largely unproven. The innovations discussed are highly speculative in nature and contribute to the discursive hype around the viability of LLM-style approaches in the autonomous vehicle industry. In promoting claims of general-purposivity, they serve as a blueprint for how proponents are seeking to embed LLMs in new industries and domains.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：自动驾驶汽车行业在经历了十年高调失败后（技术、经济、金融、监管等多重限制），资本和注意力同步转向生成式AI。行业企业将大型语言模型（LLMs）风格技术视为重启商业化努力的基础，形成新的炒作话语。
- **核心问题**：自动驾驶企业如何通过话语框架将LLM的“通用性”属性引入该领域，以克服前期（AV 1.0）的限制？这种创新主张是否具有实质证据，还是属于投机性炒作？
- **整体含义**：揭示LLM通用性叙事在自动驾驶行业中的话语构建机制，展示该叙事如何为企业提供将LLM嵌入新领域和行业的论述模板，同时警示这种高度投机话语可能带来的误导。

## 二、论文提出的方法论
- **技术图志分析（Technographic Analysis）**：对年度行业活动Nvidia GTC 2024进行深度观察与记录，捕捉企业在技术发布会、演讲、演示中如何框架化其LLM相关技术。
- **灰色文献分析**：收集并分析41份来源，包括企业通讯（如新闻稿、博客）、技术预印本、行业新闻、监管文件，以补充和交叉验证活动中的话语。
- **分析框架**：聚焦于两家代表性自动驾驶企业Wayve和Waabi如何借用LLM的“通用性”声称，导入以下假设到自动驾驶领域：
  - 基础模型（foundation models）的广泛适用性
  - 多模态训练（multimodal training）的可行性
  - 并行分词（parallel tokenisation）的效率
  - 知识蒸馏（epistemic distillation）的有效性
- **无公式或算法流程**：论文属于定性话语分析，不涉及具体数学模型或计算机算法。

## 三、实验设计
- **数据集/场景**：无传统数值实验。研究对象为Nvidia GTC 2024活动中的发言、演示材料，以及41份跨来源灰色文献。
- **Benchmark**：无量化基准。以AV 1.0（传统自动驾驶技术路径）的技术、经济、金融、监管限制作为对比参照，分析AV 2.0（基于LLM的新主张）是否声称能克服这些限制。
- **对比方法**：比较Wayve和Waabi两家公司在话语上如何引入LLM假设；对比AV 1.0实际遭遇的失败与AV 2.0高度投机的主张之间的差距。
- **未涉及任何数值对比实验或消融实验**。

## 四、资源与算力
- **未提及**：论文未讨论任何GPU型号、数量、训练时长等算力资源。其分析对象为企业公开话语，而非技术实现细节或训练成本。

## 五、实验数量与充分性
- **定性分析样本**：1个年度行业活动（Nvidia GTC 2024）、41份灰色文献、2家主要企业（Wayve和Waabi）。样本量对于话语分析而言足够，但未覆盖所有自动驾驶企业或更多行业活动，可能遗漏部分声音。
- **充分性讨论**：论文仅关注话语层面，未通过实证实验验证技术可行性，因此无法评估这些创新主张的实际有效性。主观选择两家企业可能引入选择偏差，但作者明确说明其代表性。整体上，实验覆盖了核心论述来源，但缺乏跨领域或纵向时间对比，充分性有限。

## 六、论文的主要结论与发现
- **核心发现**：Wayve和Waabi大量引入基础模型、多模态训练、并行分词、知识蒸馏等LLM假设，但这些技术尚未在自动驾驶领域得到充分验证，创新主张高度投机。
- **话语特征**：这些主张强烈依赖LLM所谓的“通用性”（general-purposivity），将一般性假设不加证明地迁移到新领域，构成一种“AV 2.0”话语体系。
- **炒作本质**：讨论中的创新在本质上属于投机性炒作，助长了围绕LLM方法在自动驾驶行业可行性的非理性乐观情绪。
- **模板作用**：通过宣扬通用性主张，这些企业为其他支持者提供了将LLM嵌入新行业和领域的论述蓝本。

## 七、优点
- **视角新颖**：从话语分析角度切入，揭示了技术炒作背后的话语构建机制，而非仅关注技术本身，为批判性技术社会学研究提供范例。
- **方法适用**：技术图志与灰色文献结合，能捕捉行业活动中的即时话语与正式出版物中的论述，交叉验证提高了分析可靠性。
- **现实意义强**：及时识别出当前自动驾驶领域的LLM热潮中缺乏实证基础的问题，有助于政策制定者、投资者和公众保持理性。

## 八、不足与局限
- **缺乏实证验证**：论文仅停留于话语层面，未对Wayve和Waabi声称的LLM技术实际效果进行任何测试或评估，无法判断其技术可行性。
- **样本选择性偏差**：仅分析两家企业（Wayve和Waabi）及一个行业活动，可能无法代表整个自动驾驶行业（如未覆盖Cruise、Tesla、Mobileye等更大玩家）的叙事策略。
- **时间局限性**：数据采集于2024年，LLM技术发展迅速，后续可能已有实质进展，结论的时效性需注意。
- **应用限制**：论文结论适用于话语批评，但不能直接用于技术决策或投资判断。

（完）
