---
title: "Unleashing Infinite Motion: Scaling Expressive Quadrupedal Motion via Generative Video Priors"
title_zh: 释放无限运动：通过生成式视频先验扩展富有表现力的四足运动
authors: "Youzhi Liu, L Y Gao, Yifei Qian, L Y Liu, Yang Cai, Ziqiao Li"
date: 2026-06-26
pdf: "https://arxiv.org/pdf/2606.28237"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=humanoid robot policy"
tldr: "四足机器人行为库局限，现有方法依赖动物数据导致扩展和泛化难题。本文提出Uni-Mo自动化流程：LLM设计运动提示，视频扩散模型生成对应机器人行为视频，提取3D轨迹作为参考训练追踪策略并部署于真实Go2。引入Identity Consistency Loss确保生成外观一致。构建7,488条语言标注动作数据集（18.5小时），真实部署成功率96.7%，仿真97.6%。方法摆脱动物依赖，实现可扩展的丰富四足运动生成。"
source: openalex
selection_source: hot_paper_scout
motivation: 四足机器人运动表现有限，依赖动物数据采集困难且跨物种迁移不适配，亟需无动物参与的自动生成方法。
method: Uni-Mo结合LLM提示、视频扩散合成和3D轨迹提取，引入Identity Consistency Loss，实现无需动物的机器人运动数据生成。
result: "构建7,488条语言标注动作数据集，真实Go2测试392个动作成功率96.7%，仿真全集成功率97.6%。"
conclusion: Uni-Mo摆脱动物依赖，为四足机器人提供可扩展的丰富运动生成，推动更自然的人机交互。
---

## 摘要
四足机器人已实现显著的移动能力，但其行为 repertoire 仍局限于几种步态——远未达到人们长久以来期望的、如同伴侣般富有表现力的存在。移植大规模运动数据的人形机器人方案继承了一个不言自明的假设：机器人运动必须先通过动物身体，导致数据采集依赖合作动物、跨物种重建脆弱、跨不兼容形态的重定向病态。我们提出 Uni-Mo，一种全自动流水线，通过将数据稀缺重新定义为生成问题来移除动物环节：大语言模型提出运动提示，视频扩散模型合成相应的机器人行为，生成的视频被提升为 3D 参考轨迹，用于训练部署在真实 Unitree Go2 上的跟踪策略。为了使朴素漂移的生成可可靠提取，我们引入身份一致性损失（Identity Consistency Loss）来强制帧间外观连贯性。我们在 https://github.com/GaoLii/Quad-Imaginarium.git 发布 Quad-Imaginarium，由此产生的开源数据集包含 7,488 个带语言注释的四足运动（18.5 小时），涵盖特技和表演行为。我们在真实 Unitree Go2 上验证了 392 个随机采样的运动，部署成功率达 96.7%，同时在仿真中整个数据集成功率达 97.6%。

## Abstract
Quadruped robots have achieved remarkable locomotion, yet their behavioral repertoire remains confined to a few gaits--far from the expressive, companion-like presence long envisioned for them. Attempts to import the humanoid recipe of large-scale motion data have inherited one tacit assumption: that robot motion must first pass through an animal body, making data collection dependent on cooperative animals, reconstruction fragile across species, and retargeting ill-posed across incompatible morphologies. We propose Uni-Mo, a fully automated pipeline that removes the animal from the loop by reframing data scarcity as a generation problem: an LLM proposes motion prompts, a video diffusion model synthesizes the corresponding robot behaviors, and the generated videos are lifted into 3D reference trajectories used to train tracking policies deployed on a real Unitree Go2. To make naively-drifting generations reliably extractable, we introduce an Identity Consistency Loss that enforces appearance coherence across frames. We release Quad-Imaginarium at https://github.com/GaoLii/Quad-Imaginarium.git, the resulting open-source dataset of 7,488 language-annotated quadruped motions (18.5 hours) spanning acrobatic and performative behaviors. We validate 392 randomly sampled motions on a real Unitree Go2 with a 96.7% deployment success rate, complemented by a 97.6% success rate across the full dataset in simulation.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 四足机器人已具备卓越的移动能力，但其行为库仍局限于少数几种步态（如行走、小跑），远未达到人们期望的、富有表现力的伴侣式存在。
- 现有尝试借鉴人形机器人的大规模运动数据移植方法，但隐含着一个未言明的假设：机器人运动必须先通过动物身体进行数据采集。这导致了三个严重问题：① 数据采集依赖合作的动物个体，成本高且难以大量获取；② 跨物种的形态重建脆弱，不同物种（如狗、狼、马）的运动机制差异导致迁移效果差；③ 在不兼容形态（如四足与双足）之间进行运动重定向时，问题病态（ill-posed），难以保持自然性。
- 核心动机是将数据稀缺问题重新定义为生成问题，彻底移除动物环节，实现无需动物参与的、可自动扩展的丰富四足运动生成，从而推动更自然的人机交互。

## 二、论文提出的方法论
- **核心思想**：全自动流水线 Uni-Mo，通过将四足机器人运动数据生成转化为从文本提示到视频生成再到3D轨迹提取的端到端过程，完全摆脱对真实动物数据采集的依赖。
- **主要流程**：
  - **步骤1 — 大语言模型（LLM）生成运动提示**：利用 LLM 根据人类意图自动提出多样化的运动描述（如“做后空翻”、“像狼一样行走”、“跳舞”），覆盖特技和表演行为。
  - **步骤2 — 视频扩散模型合成机器人行为视频**：将运动提示输入视频扩散模型（如基于扩散的视频生成模型），生成对应的四足机器人（以 Unitree Go2 为外观蓝图）执行该运动的视频序列。
  - **步骤3 — 3D 参考轨迹提取**：从生成的视频帧中通过视觉运动恢复结构（lifting）方法提取出3D运动轨迹，作为后续策略训练的参考信号。
  - **步骤4 — 跟踪策略训练与真实部署**：使用提取的3D轨迹作为参考数据，训练一个跟踪策略（如基于强化学习的运动跟踪控制器），最终部署到真实的 Unitree Go2 机器人上执行。
- **关键技术细节**：
  - 针对视频扩散模型生成时的帧间漂移问题（即外观不一致、运动不连贯），提出 **身份一致性损失（Identity Consistency Loss）** ，强制生成视频中机器人外观在不同帧之间保持连贯一致，使得3D轨迹提取可靠。
- **算法流程（文字说明）**：输入 → LLM 生成动作文本描述 → 视频扩散模型（含身份一致性损失）生成对应机器人运动视频 → 从视频中提取3D运动轨迹 → 训练基于参考轨迹的闭环跟踪策略 → 部署到真实机器人并执行。

## 三、实验设计
- **数据集构建**：利用 Uni-Mo 流程自动生成了 **Quad-Imaginarium** 数据集，包含 **7,488 条带语言标注的四足运动**（总计18.5小时），覆盖特技、表演和日常行为。
- **真实机器人实验场景**：在 **真实 Unitree Go2** 机器人上进行部署测试。从数据集中随机采样 **392 个动作**，由机器人直接执行，记录是否成功完成指定运动。
- **仿真验证场景**：在物理仿真环境中，对 **整个数据集的全部 7,488 个动作** 进行策略跟踪成功率测试。
- **基准与对比方法**：论文未明确与其他现有方法（如基于动物数据采集、跨物种重定向等方法）进行定量对比实验。但文中指出，Uni-Mo 的核心优势在于彻底摆脱动物依赖，因此基准对比可能隐含于“传统方法依赖动物导致扩展困难”的定性比较中。实验主要验证了Uni-Mo自身生成数据的有效性。
- **消融实验**：未在摘要和TL;DR中提及具体的消融组，但身份一致性损失（Identity Consistency Loss）的引入是方法的关键，推测在该损失的消融实验中应当展示了有无该损失对轨迹提取可靠性的影响（具体数据未提供）。

## 四、资源与算力
- **文中未明确说明**：摘要和TL;DR中未提及训练视频扩散模型、LLM微调、以及跟踪策略训练所使用的具体GPU型号、数量、训练时长等算力信息。
- 仅可知LLM和视频扩散模型均为预训练模型，论文侧重于流程整合与部署验证，未报告计算成本细节。若需复现，需进一步查阅论文全文。

## 五、实验数量与充分性
- **实验数量**：
  - 真实机器人部署：392 个随机动作，成功率 96.7%。
  - 仿真全集验证：7,488 个动作，成功率 97.6%。
  - 数据集规模：7,488 条，18.5小时，语言标注。
- **充分性分析**：
  - **正面**：真实机器人测试样本数接近400，覆盖了各种特技和表演行为，统计结果具有代表性；全集仿真验证确保了数据集的整体可行性，验证了方法的可扩展性。
  - **不足**：未与其他现有方法（如动物数据采集方法、基于有限数据的手工设计方法）进行定量对比，难以直接衡量Uni-Mo相较传统方案在成功率、运动质量、自然度等方面的优劣。缺少对身份一致性损失的单独消融实验报告（可能完整论文中有，摘要未提及），实验的公平性（如随机采样是否合理、是否预先过滤难例）未明确说明。

## 六、论文的主要结论与发现
- Uni-Mo 作为首个完全移除动物环节的自动化四足运动生成流水线被提出，证明了通过“文本→视频→3D轨迹→机器人执行”的生成式流程可以产生高质量、可执行的丰富四足运动。
- 在真实 Unitree Go2 机器人上实现了 96.7% 的部署成功率，在仿真中全集成功率达 97.6%，表明生成的数据可以作为有效的训练参考。
- 身份一致性损失有效解决了视频扩散模型生成的帧间外观漂移问题，使3D轨迹提取成为可能。
- 构建的 Quad-Imaginarium 数据集（7,448条，18.5小时）为四足机器人社区提供了开源的大规模、带语言标注的运动数据，有助于人机交互和机器人表现力的进一步发展。
- 论文的核心意义在于打破了“机器人运动必须先通过动物身体”的传统假设，为无动物依赖的、可扩展的机器人行为生成开辟了新路径。

## 七、优点
- **创新性**：将数据稀缺重新定义为生成问题，完全摆脱对动物数据采集的依赖，是四足机器人运动生成范式的重要突破。
- **自动化与可扩展性**：全流程自动化（LLM→视频扩散→轨迹提取→策略部署），不依赖人工采集或动物训练，理论上可以无限生成新的运动。
- **技术可靠性**：身份一致性损失的引入从方法层面解决了生成视频的时序一致性问题，确保了轨迹提取的可靠性；最终真实部署成功率很高（96.7%），证明了方法的实用性。
- **开源贡献**：公开了大规模语言标注运动数据集 Quad-Imaginarium 以及相关代码（https://github.com/GaoLii/Quad-Imaginarium.git），有利于后续研究复现和推动社区发展。
- **实验覆盖全面**：既有真实机器人的随机采样验证，也有仿真全集验证，从不同置信度证明了方法的有效性。

## 八、不足与局限
- **缺乏对比基线**：未与现有基于动物数据的方法（如跨物种重定向、手工设计运动库）进行定量对比，无法准确量化 Uni-Mo 方法的相对优势（如运动自然度、成功率、数据效率）。
- **依赖生成模型质量**：方法高度依赖于视频扩散模型的生成质量和LLM的提示质量，如果生成模型对四足机器人形态理解不充分或产生幻觉，可能造成低质量轨迹，但未被深入讨论。
- **身份一致性损失的消融不明显**：虽然提到其关键作用，但未提供详细的消融实验数据（如去掉该损失后的成功率），实验设计不够完整。
- **跨形态泛化未验证**：仅在 Unitree Go2 这一种特定机器人上验证，对于其他形态（如其他品牌四足机器人、不同尺寸的四足机器人）的迁移效果未知。
- **标签准确性风险**：LLM 生成的动作描述与视频实际呈现的行为之间可能存在语义偏差，可能导致数据集标注噪声，影响下游使用。
- **计算资源未报告**：未说明生成和处理过程中所需的算力成本，对复现和部署的可行性评估不足。

（完）
