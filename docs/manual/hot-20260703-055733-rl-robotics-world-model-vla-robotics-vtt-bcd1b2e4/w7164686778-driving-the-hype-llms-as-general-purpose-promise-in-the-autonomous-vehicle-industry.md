---
title: "Driving the hype: LLMs as ‘general-purpose’ promise in the autonomous vehicle industry"
title_zh: 驱动炒作：大语言模型作为自动驾驶行业的‘通用’承诺
authors: "Alex Gekker, Sam; id_orcid 0000-0001-8347-3695 Hind"
date: 2026-06-22
pdf: "https://www.tandfonline.com/doi/pdf/10.1080/1369118X.2026.2689026?needAccess=true"
tags: ["query:热点论文筛选", "query:world-model", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; institutions=University of Amsterdam, University of Manchester; query=find world models used in autonomous driving and interactive simulation"
tldr: 自动驾驶行业在经历十年挫折与资金转向生成式AI后，将大型语言模型（LLM）技术视为重启商业化的关键。本研究通过技术图分析2024年Nvidia GTC大会及41份灰色文献（企业通信、技术预印本、贸易新闻、监管文件），考察Wayve和Waabi两家公司如何利用LLM的“通用目的性”声称克服技术、经济、金融和监管限制。研究发现，这些声称高度依赖基础模型、多模态训练、并行token化及知识蒸馏等未经验证的概念，构成AV 2.0阶段的炒作。该工作揭示了LLM被嵌入新产业时的话语构建模式，警示其投机性风险。
source: openalex
selection_source: hot_paper_scout
motivation: 探究自动驾驶企业如何利用LLM的通用性声称，克服此前失败的技术、经济、金融和监管限制以重启商业化。
method: 技术图分析Nvidia GTC 2024及41份灰色文献，聚焦Wayve和Waabi两家公司的技术话语构建。
result: 发现LLM通用性声称高度投机，依赖基础模型和多模态训练等未验证概念，形成AV 2.0炒作。
conclusion: LLM通用目的性话语助企业吸引资本，但技术可行性存疑，需警惕炒作风险。
---

## 摘要
自动驾驶汽车的支持者正宣告一个新时代的到来，这一时代由大语言模型（LLMs）驱动的创新所引领。在经历了十年高度公开的失败，以及资本和注意力同时转向生成式AI之后，自动驾驶行业的企业已将LLM风格技术作为重启商业化努力的基础。通过对年度行业活动Nvidia GTC 2024的技术志分析，以及41份相关灰色文献（企业通讯、技术预印本、行业新闻报道和监管文件）的研究，我们考察了两家自动驾驶企业Wayve和Waabi如何通过话语将这些技术框架描述为能够克服迄今为止阻碍完全自动驾驶未来（AV 1.0）的技术、经济、金融和监管限制。我们发现，这些主张很大程度上借鉴了LLM所谓的‘通用性’，将关于基础模型广泛适用性、多模态训练、并行分词和认知蒸馏（AV 2.0）的假设引入到一个尚未得到充分验证的领域。所讨论的创新本质上具有高度投机性，并助长了围绕LLM风格方法在自动驾驶行业可行性的讨论炒作。通过推广通用性的主张，它们为支持者如何寻求将LLM嵌入新行业和新领域提供了蓝图。

## Abstract
Proponents of autonomous vehicles are proclaiming a new era, driven by innovations derived from large language models (LLMs). Following a decade of highly public failures and the concurrent redirection of capital and attention towards generative AI, firms in the autonomous vehicle industry have turned to LLM-style techniques as the basis for a rebooted commercialisation effort. Through a technographic analysis of an annual industry event, Nvidia GTC 2024, and 41 sources of related grey literature (firm communications, technical preprints, trade journalism, and regulatory documents), we examine how two autonomous vehicle firms, Wayve and Waabi, discursively frame these techniques as capable of overcoming the technical, economic, financial, and regulatory limits that have so far thwarted a fully-autonomous future (AV 1.0). We find that these claims draw heavily on the supposed ‘general-purposivity’ of LLMs, importing assumptions about the broad applicability of foundation models, multimodal training, parallel tokenisation, and epistemic distillation (AV 2.0) into a domain where they remain largely unproven. The innovations discussed are highly speculative in nature and contribute to the discursive hype around the viability of LLM-style approaches in the autonomous vehicle industry. In promoting claims of general-purposivity, they serve as a blueprint for how proponents are seeking to embed LLMs in new industries and domains.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：自动驾驶行业在经历十年高度公开的失败（如福特Argo AI关闭、Cruise许可暂停、苹果Titan项目取消）后，资本和注意力转向生成式AI。企业试图通过将大语言模型（LLM）技术作为“通用目的技术”来重启商业化，形成所谓的“AV 2.0”叙事。论文旨在揭示这种话语炒作背后的机制，批判性地分析LLM“通用性”声称如何被用于克服AV 1.0的多重限制。
- **背景支撑**：2022年ChatGPT发布后，生成式AI吸引大量投资，自动驾驶行业面临技术、经济、金融、监管四重困境（如机器视觉依赖人工编码成本高、传统车企主导市场、利率上升导致资本枯竭、事故频发引发监管收紧）。企业如Wayve和Waabi声称LLM创新（视频提示、并行token化）能根本性解决这些问题，但这些声称高度投机且未经验证。
- **核心问题**：LLM的“通用目的性”话语如何被构建并嵌入自动驾驶领域？这种炒作在哪些节点上可能夸大技术可行性，从而引导投资和公共预期？

## 二、论文提出的方法论
- **核心思想**：采用“技术图分析”（technographic analysis）方法，融合媒体研究与STS传统，关注行业事件与灰色文献中的话语建构，而非技术本身的中立性。视技术声明为话语干预，构建特定创新、失败与重生的叙事。
- **关键技术细节**：
  - **分析对象**：Nvidia GTC 2024大会的Drive分会场（芯片巨头Nvidia的年度活动，被称为“AI的伍德斯托克”），以及41份灰色文献（包括企业通讯、技术预印本ArXiv、贸易新闻、监管文件）。
  - **选择标准**：聚焦两家明确使用“AV 2.0”术语并自称引领LLM创新的初创公司：英国Wayve（CEO Alex Kendall）和加拿大Waabi（CEO Raquel Urtasun）。它们被视为象征性而非代表性案例。
  - **分析框架**：归纳LLM四大创新属性——基础模型（foundations）、多模态训练（multimodality）、并行分词（parallel tokenization）、认知蒸馏（epistemic distillation）；对应AV 1.0的四大限制——技术、经济、金融、监管。
  - **分析过程**：通过对GTC演讲（如Wayve的GAIA 1.0、Waabi的CoPilot4D）及文献的迭代解读，考察企业如何将LLM方法包装为突破这些限制的关键，并揭露其中的投机性假设。
- **算法/流程**：无传统算法流程，属定性话语分析，强调“非监督学习”“世界模型”“token化一切”等技术话语的挪用与转化。

## 三、实验设计
- **数据集/场景**：无传统实验数据集。基于41份灰色文献（企业博客、技术报告、行业新闻、CPUC监管文件等），时间跨度2022–2026年。重点分析Nvidia GTC 2024的两场演讲（Wayve：“如何让LLM增强自动驾驶体验”；Waabi：“生成式AI加速自动驾驶新时代”）。
- **Benchmark**：无定量基准。对比的是AV 1.0时期的方法（如基于规则的对象分类、监督学习、模块化流水线）与AV 2.0声称的方法（视频提示、并行token化）。
- **对比方法**：未进行直接实验对比，而是通过文献对比LLM创新声称与历史失败案例（如Cruise事故、Argo AI倒闭）。强调LLM方法在现实世界中的未验证性（如“模型崩溃”“token指数化”问题）。

## 四、资源与算力
- **论文自身**：未使用计算资源，是纯粹的社科分析。
- **分析对象涉及的算力**：
  - Wayve声称依赖Nvidia GPU和软件堆栈训练十亿参数模型（如GAIA 1.0需“petabytes数据”），但未提供具体GPU型号、数量或时长。
  - Waabi的CoPilot4D因并行token化需实时处理“数万个token”，计算需求巨大，但未量化。
  - 论文指出这种算力依赖将加剧环境成本（数据中心能耗）和资源集中（Big Tech主导），但未给出具体测算。

## 五、实验数量与充分性
- **实验数量**：无传统实验组。进行了一次性话语分析，覆盖41份来源（19家企业文献、7篇技术预印本、11篇行业新闻、4份监管文件）。来源类型多样，附录完整列出。
- **充分性**：
  - **优点**：对两家核心企业的技术声称进行了深度解剖，与四项限制框架紧密对应；文献时间范围覆盖关键事件期（2022–2026）。附录提供了可验证的来源列表。
  - **局限**：仅选择Wayve和Waabi两家公司，未涉及Waymo、Cruise、Tesla等主流或历史企业，样本代表性受限。作者承认是“象征性”而非代表性案例。未进行定量验证（如比较不同方法在仿真环境中的性能），依赖企业公开声称，可能受营销夸大影响。此外，技术预印本（ArXiv）未经同行评议，但作者将其视为话语的一部分。

## 六、论文的主要结论与发现
- **核心结论**：LLM的“通用性”声称高度投机，大量未经验证的假设（如基础模型的多任务适用性、多模态训练可直接迁移、并行token化可低成本替代监督学习）从NLP领域直接引入自动驾驶，缺乏实际证据。
- **发现**：
  - Wayve的GAIA 1.0（视频提示生成合成数据）声称克服技术、经济、监管限制，但面临“模型崩溃”风险（合成数据导致性能退化）和对真实数据的持续依赖。
  - Waabi的CoPilot4D（并行token化实现世界模型）声称克服技术、金融限制，但面临“token指数化”（每帧Token数量远超文本）和实时计算瓶颈。
  - 这些创新本质上是AV 1.0失败的重新包装，通过话语炒作吸引资本，但可能重演泡沫周期。
  - 需要警惕谁在驱动炒作（如Nvidia作为芯片供应商受益于算力需求）及其目的（如掩盖人类劳动、环境成本）。
- **呼吁**：媒体学者应关注LLM通用性话语在具体行业中的修正与挪用，评估其社会风险（如幻觉导致事故、资产化加剧不平等）。

## 七、优点
- **方法创新**：将行业年会（Nvidia GTC）视为话语分析的关键节点，捕捉技术炒作与商业化的协同；技术图分析结合灰色文献，提供了对AI产业话语的实证视角。
- **框架系统性**：提出“四项LLM创新属性”与“四项AV 1.0限制”的对照框架，清晰揭示炒作如何通过对立叙事（“旧方法失败，新LLM方法万能”）构建。
- **批判深度**：不仅指出技术局限性（模型崩溃、token指数化），还揭示了背后的人类劳动隐没（减少对“验证员”和“远程操作员”的依赖）、环境成本（数据中心能耗）、资产化趋势（订阅制、数据租金）等社会政治问题。
- **文献详实**：41份来源分类整理并附完整附录，为后续研究提供了可追溯的资源池。

## 八、不足与局限
- **样本偏见**：仅分析Wayve和Waabi两家公司，未涵盖Waymo、Cruise、Tesla等行业龙头或倒闭企业（如Argo AI）。这些企业可能对LLM方法持不同立场或已有失败教训，排除导致结论的普遍性受限。
- **缺乏技术验证**：未进行定量实验或仿真比较来验证LLM方法的实际性能（如与监督学习在相同场景下的错误率对比）。所有技术声称来自企业公开材料，可能被夸大，论文依赖话语分析无法独立核实。
- **未讨论安全风险细节**：虽然提及“幻觉”的社会风险，但未深入分析LLM在自动驾驶中可能的具体故障模式（如对长尾事件的误判、对抗攻击鲁棒性），仅泛泛提及“社会风险”。
- **时间范围局限性**：分析截至2026年，而LLM和自动驾驶技术迭代迅速（如GPT-5、世界模型进展），论文结论可能随新兴证据变化。
- **未讨论监管互动**：尽管提到监管限制（CPUC许可、公民抗议），但未分析LLM方法可能引致的新监管挑战（如合成数据合规性、模型解释性要求）。

（完）
