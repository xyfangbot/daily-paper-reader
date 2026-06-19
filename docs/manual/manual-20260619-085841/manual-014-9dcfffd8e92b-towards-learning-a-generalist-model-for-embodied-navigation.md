---
title: Towards Learning a Generalist Model for Embodied Navigation
title_zh: 迈向具身导航的通用模型学习
authors: "Duo Zheng, Shijia Huang, Lin Zhao, Yiwu Zhong, Liwei Wang"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/014-2024_zheng_navillm-7d1c8a79-9dcfffd8e92b.pdf
tags: ["query:手动上传", "paper:PDF", "query:embodied navigation", "query:generalist model", "query:large language models", "query:schema-based instruction", "query:multi-task learning"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "现有具身导航模型多针对特定任务，泛化性不足。本文提出NaviLLM，首个通用导航模型，利用架构指令将多种任务统一为生成问题，并整合多数据集训练。在CVDN、SOON和ScanQA上达到最优，其中CVDN目标进展提升29%。此外，在未见任务如具身问答和3D描述上表现优异，展示了强泛化能力。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 808, \"height\": 608, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1778, \"height\": 651, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1585, \"height\": 950, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1794, \"height\": 843, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1771, \"height\": 366, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1812, \"height\": 321, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 759, \"height\": 322, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1592, \"height\": 242, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 896, \"height\": 235, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 854, \"height\": 469, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1435, \"height\": 162, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1428, \"height\": 343, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1426, \"height\": 549, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1431, \"height\": 462, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1424, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1896, \"height\": 750, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1894, \"height\": 373, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-014-9dcfffd8e92b-towards-learning-a-generalist-model-for-embodied-navigation/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1892, \"height\": 590, \"label\": \"Table\"}]"
motivation: 现有具身导航模型缺乏泛化性，难以适应未见场景，而大型语言模型为构建通用导航智能体提供了新机遇。
method: 提出NaviLLM，通过架构指令将导航任务转化为生成问题，统一多种任务并利用多数据集联合训练。
result: "在CVDN、SOON和ScanQA上达到最优，CVDN目标进展提升29%，并在具身问答等未见任务上表现优异。"
conclusion: NaviLLM是首个通用导航模型，通过统一任务框架和多样化数据训练，实现了强泛化性和高性能。
---

## 摘要
构建一个能与世界交互的通用智能体是人工智能系统的诱人目标，这推动了具身导航的研究，其中智能体需要根据指令导航或响应查询。尽管取得了重大进展，但以往的工作主要关注任务特定智能体，缺乏对未见场景的泛化能力。最近，LLMs在各个领域表现出卓越的能力，为具身导航提供了有希望的机遇。基于此，我们提出了第一个用于具身导航的通用模型NaviLLM。它通过引入基于模式的指令将LLMs适应于具身导航。基于模式的指令灵活地将各种任务转化为生成问题，从而统一了广泛的任务。这种方法使我们能够将来自不同数据集的多种数据源整合到训练中，使NaviLLM具备具身导航所需的广泛能力。我们进行了大量实验来评估模型的性能和泛化能力。实验结果表明，我们的统一模型在CVDN、SOON和ScanQA上达到了最先进的性能。具体来说，在CVDN上，它在目标进展方面比先前的最先进方法显著提高了29%。此外，我们的模型还展现出强大的泛化能力，并在未见任务上取得了令人印象深刻的结果，例如具身问答和3D描述。我们的代码可在https://github.com/LaVi-Lab/NaviLLM获取。

## Abstract
Building a generalist agent that can interact with the world is the intriguing target of AI systems, thus spurring the research for embodied navigation, where an agent is required to navigate according to instructions or respond to queries. Despite the major progress attained, previous works primarily focus on task-specific agents and lack generalizability to unseen scenarios. Recently, LLMs have presented remarkable capabilities across various fields, and provided a promising opportunity for embodied navigation. Drawing on this, we propose the first generalist model for embodied navigation, NaviLLM. It adapts LLMs to embodied navigation by introducing schema-based instruction. The schema-based instruction flexibly casts various tasks into generation problems, thereby unifying a wide range of tasks. This approach allows us to integrate diverse data sources from various datasets into the training, equipping NaviLLM with a wide range of capabilities required by embodied navigation. We conduct extensive experiments to evaluate the performance and generalizability of our model. The experimental results demonstrate that our unified model achieves state-of-the-art performance on CVDN, SOON, and ScanQA. Specifically, it surpasses the previous state-of-the-art method by a significant margin of 29% in goal progress on CVDN. Moreover, our model also demonstrates strong generalizability and presents impressive results on unseen tasks, e.g. embodied question answering and 3D captioning. Our code is available at https://github.com/LaVi-Lab/NaviLLM.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有具身导航模型多为任务特定设计（如仅处理R2R、CVDN或3D-QA），缺乏对未见场景和任务的泛化能力。  
- 大型语言模型（LLM）在文本理解和生成上展现了卓越能力，为构建统一、通用的具身导航智能体提供了新契机。  
- 本文旨在探索如何将LLM适应到具身导航中，训练一个能同时处理多种导航与交互任务的通用模型（generalist model），减少对任务特定设计的依赖。

## 二、论文提出的方法论
- **核心思想**：通过**基于模式的指令（schema-based instruction）** 将各类具身导航任务统一转化为文本生成问题，从而使一个模型能学习多种任务。  
- **模型架构**：由场景编码器（Scene Encoder）和LLM两部分组成。  
  - 场景编码器：使用冻结的EVA-CLIP ViT提取多视角图像特征，再通过一个2层Transformer编码器进行多视角融合，得到场景表示。  
  - LLM：基于Vicuna-7B-v0，将任务描述、当前观察、历史轨迹、输出提示等信息按固定模式组合成输入，预测下一步动作（如移动方向、对象ID、文本答案等）。  
- **Schema组成**：  
  - Task：任务的自然语言描述。  
  - Observation：当前视角的场景表示，带ID编号。  
  - History：历史步的观察表示序列。  
  - Output Hint：输出格式提示（如“从观察中选择一个方向”）。  
- **训练方式**：两阶段训练。  
  - 预训练（10,000步）：在CVDN、SOON、R2R、REVERIE、ScanQA及R2R/REVERIE的增强数据上进行教师强制学习。  
  - 多任务微调（5,000步）：在相同数据集加上LLaVA-23k数据上，交替使用教师强制和学生强制学习。  
- **统一优化目标**：对所有任务使用交叉熵损失，预测文本token。

## 三、实验设计
- **数据集与基准**：  
  - VLN：CVDN（对话导航）、SOON（场景目标导航）、R2R（逐步指令）、REVERIE（远程目标定位）。  
  - 3D-QA：ScanQA。  
  - EQA：MP3D-EQA（用于零样本测试）。  
- **对比方法**：  
  - VLN：PREVALENT、HAMT、DUET、AZHP、VLN-SIG、VLN-PETL等。  
  - 3D-QA：VoteNet+MCAN、ScanRefer+MCAN、3D-LLM等。  
- **评估指标**：  
  - VLN：Success Rate (SR)、SPL、Goal Progress (GP)、Oracle Success Rate (OSR)、Trajectory Length (TL)。  
  - 3D-QA：Exact Match (EM)、ROUGE-L、METEOR、CIDER、BLEU-4。  
  - EQA：导航SR、SPL，问答Accuracy。

## 四、资源与算力
- 训练硬件：8块Nvidia A100 GPU。  
- 训练时长：预训练10,000步 + 微调5,000步，总计约80小时。  
- Batch size：64。  
- 模型参数：LLM为7B级别，ViT约428M参数并冻结。

## 五、实验数量与充分性
- **主要对比实验**（表1）：在CVDN、SOON、R2R、REVERIE、ScanQA五个基准上分别对比多个SOTA方法。  
- **消融实验**（表5）：  
  1. 是否使用预训练LLM权重。  
  2. 是否进行多任务学习。  
  3. 是否进行预训练（增强数据）。  
  4. 进一步分析schema元素的作用（表6）。  
- **泛化能力实验**：  
  - 零样本的held-out实验（表3），分别排除CVDN/SOON/REVERIE进行测试。  
  - 零样本EQA实验（表4），结合导航和问答能力。  
- **可视化分析**（图3）：轨迹总结、对象导航、EQA、3D描述等。  
- **总体评价**：实验覆盖了多种任务、多种设置（域内、域外、零样本），消融设计合理，对比方法全面，实验充分且客观。

## 六、论文的主要结论与发现
- NaviLLM单模型在CVDN、SOON、ScanQA测试集上达到新SOTA，其中CVDN的Goal Progress比先前方法提升29%。  
- 在R2R和REVERIE上取得与最新任务特定模型相当的性能，尤其在指令复杂的CVDN和SOON上优势明显。  
- 多任务学习显著提升了所有任务的性能（表5 row1 vs. row3）。  
- LLM的预训练权重至关重要，随机初始化导致性能大幅下降（表5 row2 vs. row3）。  
- 增强数据预训练的收益有限，说明数据质量比数量更重要。  
- 模型展现出强大的零样本泛化能力：在未见过的任务（如EQA、3D描述）上也能取得合理结果。

## 七、优点
- **首创通用性**：首次提出用于具身导航的通用模型，统一了视觉语言导航、3D问答、轨迹总结、对象定位等多种任务。  
- **架构简洁有效**：基于schema-based instruction将不同任务统一为生成问题，无需复杂任务头。  
- **充分利用LLM知识**：通过微调Vicuna，模型能理解复杂语言指令（如CVDN的长对话），这是先前任务特定模型难以做到的。  
- **灵活的泛化能力**：零样本下可组合已学技能（如导航+问答）解决新任务，证明了模型的通用性潜力。  
- **实验设计全面**：包含域内对比、域外泛化、消融、可视化，验证了方法的有效性和鲁棒性。

## 八、不足与局限
- **在REVERIE上仍有差距**：相比DUET等方法，在简单指令的REVERIE上性能略低，可能因模型对短句的理解或目标定位分支尚需改进。  
- **增强数据收益有限**：论文归因于数据质量，但未深入分析如何更有效地利用大量无标签或弱标签数据。  
- **历史长度与视图数量的超参数依赖**：文中为不同任务设置了不同历史步数（15-30）和视图数（36），这些超参数可能影响泛化能力，未进行系统调优。  
- **计算资源开销大**：7B模型微调需要8卡A100训练80小时，资源门槛较高。  
- **未涉及真实机器人部署**：所有实验在模拟器（Habitat, Matterport3D）中进行，与真实物理世界的交互仍存在差距。  
- **任务覆盖仍有遗漏**：未包含类似“抓取”、“操作”等更复杂的具身任务，距离完全的通用智能体还有距离。

（完）
