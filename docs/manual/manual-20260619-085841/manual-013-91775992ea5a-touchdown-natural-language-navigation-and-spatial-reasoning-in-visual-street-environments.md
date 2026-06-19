---
title: "TOUCHDOWN: Natural Language Navigation and Spatial Reasoning in Visual Street Environments"
title_zh: TOUCHDOWN：视觉街道环境中的自然语言导航与空间推理
authors: "Howard Chen, Alane Suhr, Dipendra Misra, Noah Snavely, Yoav Artzi"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/013-2019_chen_touchdown-ce6f187d-91775992ea5a.pdf
tags: ["query:手动上传", "paper:PDF", "query:navigation", "query:spatial reasoning", "query:instruction following", "query:visual environment", "query:dataset"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "针对自然语言导航与空间推理的联合推理问题，提出TOUCHDOWN任务和数据集，要求智能体在真实城市环境中先遵循导航指令，再根据自然语言描述定位隐藏物体。数据集包含9,326个英文指令与演示对，实证表明现有方法难以应对，且数据比同类资源包含更丰富的空间推理。该工作为视觉语言导航与空间推理提供了新的挑战性基准。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 757, \"height\": 1041, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 661, \"height\": 467, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1814, \"height\": 1325, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 829, \"height\": 312, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 859, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1506, \"height\": 259, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1506, \"height\": 263, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1254, \"height\": 2258, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1769, \"height\": 384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1769, \"height\": 383, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1768, \"height\": 371, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1768, \"height\": 384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1771, \"height\": 383, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1770, \"height\": 384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1768, \"height\": 372, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1771, \"height\": 381, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1770, \"height\": 386, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1769, \"height\": 386, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1769, \"height\": 373, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1774, \"height\": 383, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1772, \"height\": 385, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 1770, \"height\": 381, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 1769, \"height\": 371, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 1775, \"height\": 381, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 1771, \"height\": 383, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 1770, \"height\": 383, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 1770, \"height\": 371, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 1772, \"height\": 381, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 1771, \"height\": 385, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 1769, \"height\": 383, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-031.webp\", \"caption\": \"\", \"page\": 0, \"index\": 31, \"width\": 1769, \"height\": 373, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/fig-032.webp\", \"caption\": \"\", \"page\": 0, \"index\": 32, \"width\": 1772, \"height\": 381, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 849, \"height\": 236, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 650, \"height\": 197, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 800, \"height\": 298, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1799, \"height\": 627, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 876, \"height\": 616, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 507, \"height\": 514, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1222, \"height\": 528, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 490, \"height\": 300, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-013-91775992ea5a-touchdown-natural-language-navigation-and-spatial-reasoning-in-visual-street-environments/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 670, \"height\": 253, \"label\": \"Table\"}]"
motivation: 现有方法在联合语言与视觉的导航和空间推理上能力不足，需要更具挑战性的真实环境数据集。
method: "构建TOUCHDOWN数据集，包含9,326个导航指令和空间描述与演示的配对样本，在真实城市环境中执行任务。"
result: 实证分析显示现有方法在该数据集上表现不佳，且数据集中的空间推理比相关资源更丰富。
conclusion: TOUCHDOWN为视觉语言导航和空间推理研究提供了开放挑战，推动了领域发展。
---

## 摘要
我们研究了通过导航和空间推理任务共同推理语言和视觉的问题。我们引入了TOUCHDOWN任务和数据集，其中智能体必须首先在真实的视觉城市环境中遵循导航指令，然后识别自然语言描述的位置，以在目标位置找到隐藏的物体。数据包含9,326个英语指令和空间描述示例，并配有演示。实证分析表明，该数据对现有方法提出了开放式挑战，定性语言分析显示，与相关资源相比，该数据展示了更丰富的空间推理使用。

## Abstract
We study the problem of jointly reasoning about language and vision through a navigation and spatial reasoning task. We introduce the TOUCHDOWN task and dataset, where an agent must first follow navigation instructions in a real-life visual urban environment, and then identify a location described in natural language to find a hidden object at the goal position. The data contains 9,326 examples of English instructions and spatial descriptions paired with demonstrations. Empirical analysis shows the data presents an open challenge to existing methods, and qualitative linguistic analysis shows that the data displays richer use of spatial reasoning compared to related resources.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 研究动机：现有视觉-语言推理工作大多基于简单视觉输入（如物体聚焦的照片或模拟环境），缺乏真实世界复杂场景下的导航与空间推理研究。真实城市环境不仅增加了视觉挑战，还改变了语言本身的复杂性和推理需求。
- 核心问题：如何让智能体在真实城市街道环境中，同时完成两项子任务——1）根据自然语言导航指令移动至目标位置；2）在目标位置根据空间描述定位隐藏物体（玩具熊Touchdown）。这要求智能体理解物体、空间关系、自我中心与物体中心的空间推理。
- 研究意义：构建了一个更具挑战性的真实环境基准，推动视觉语言导航和空间推理领域向更接近人类日常生活的场景发展。

## 二、论文提出的方法论
- 核心思想：设计一个基于Google Street View的交互式视觉导航环境，通过众包流程收集自然语言指令和空间描述，并定义导航任务（遵循指令到达目标）和空间描述解析任务（SDR，从全景图中定位描述位置）。
- 关键技术细节：
  - 环境构建：使用纽约市29,641个全景图节点和61,319条边，每个节点有360°RGB全景图，节点间通过有向边连接。
  - 众包数据收集：分为四个任务——指令写作（路线跟随+隐藏Touchdown并写指令）、目标传播（将Touchdown位置标注到相邻全景图）、验证（人类工作者跟随指令寻找Touchdown）、分割（将指令分为导航段和描述段）。采用奖金激励，保证指令质量。
  - 导航任务：动作空间为{FORWARD, LEFT, RIGHT, STOP}，状态为(全景图，朝向)，转移函数确定。评估指标：任务完成率(TC)、最短路径距离(SPD)、成功加权编辑距离(SED)。
  - 空间描述解析任务：给定全景图I和描述文本，预测Touchdown的像素坐标(x,y)。评估指标：不同半径（40,80,120像素）下的准确率/一致性、平均欧氏距离。
- 模型方法：
  - 导航基线：非学习基线（STOP, RANDOM, FREQUENT）和两种学习模型——GA（门控注意力）和RCONCAT（借鉴Mirowski等人的地标导航模型，修改为指令驱动）。
  - SDR模型：提出LINGUNET架构（语言条件UNET），利用双向LSTM编码文本，使用ResNet18提取图像特征，通过多层卷积/反卷积和文本条件卷积核，输出像素级概率分布，训练使用KL散度最小化。对比基线包括非学习基线（随机、中心、平均）、UNET（无语言）、CONCAT、CONCATCONV、TEXT2CONV。

## 三、实验设计
- 数据集与场景：使用自行收集的TOUCHDOWN数据集，包含9,326个完整示例（导航+描述），其中训练集6,526、开发集1,391、测试集1,409。SDR任务有25,575个示例（含多次传播）。环境为纽约市真实街道。
- Benchmark：无外部标准基准，文章将自身与R2R、Talk the Walk、SAIL、LANI等数据集进行统计和语言分析对比。
- 对比方法：
  - 导航：STOP、RANDOM、FREQUENT（非学习）；GA、RCONCAT（学习模型）。还进行了单模态消融（仅语言或仅视觉）。
  - SDR：RANDOM、CENTER、AVERAGE（非学习）；UNET、CONCAT、CONCATCONV、TEXT2CONV、LINGUNET。
- 完整任务评估：将最好导航模型（RCONCAT）与最好SDR模型（LINGUNET）流水线组合，在80px阈值下完成准确率为4.5%，而人类表现约为92%。

## 四、资源与算力
- 文中未明确说明使用的具体GPU型号、数量或训练时长，仅在附录中提及使用异步训练（6个客户端）和HOGWILD!策略进行导航模型训练，以及使用ADAM优化器。SDR模型使用单层LSTM、ResNet18等，但未报告硬件资源或训练时间。

## 五、实验数量与充分性
- 实验数量：
  - 导航：对比3种非学习基线 + 2种学习模型，在开发集和测试集上报告三项指标；额外进行了RGB图像输入实验和单模态消融实验。
  - SDR：对比3种非学习基线 + 5种学习模型（含UNET），同样在开发集和测试集上报告多项指标。
  - 完整任务：组合流水线评估。
  - 语言学分析：对25个样本进行11种现象的人工标注（与R2R、SAIL、LANI对比）。
- 充分性评估：实验设计较为全面，涵盖了多种基线和消融，但导航模型的性能较低（TC约10%），说明任务难度大且现有方法远未解决。消融实验证明了两种模态的必要性。然而，仅有25个样本的语言学分析样本量较小，可能存在偏差。总体实验较为客观公平。

## 六、论文的主要结论与发现
- TOUCHDOWN数据集比现有数据集（如R2R、SAIL、LANI）具有更长的指令、更大的词汇量、更多的实体引用和更丰富的空间推理（尤其是自我中心和物体中心空间关系）。
- 现有导航方法在该任务上表现较差（最佳RCONCAT任务完成率仅10.7%），表明真实城市环境导航的挑战性。
- LINGUNET在SDR任务上显著优于所有基线（最佳准确率27.8% @120px），但仍有很大提升空间。
- 人类表现（92%）与最佳模型（4.5%完整任务）之间的巨大差距表明当前模型在联合推理上严重不足。
- 数据集中的语言现象（如条件、计数、顺序、比较、状态验证等）远多于现有导航数据集，为未来研究提供了丰富挑战。

## 七、优点
- 真实环境数据：基于Google Street View的真实城市图像，比模拟环境更接近实际应用。
- 任务设计创新：将导航与空间描述解析结合，且两个子任务分别侧重自我中心和物体中心推理，覆盖不同空间语义。
- 数据收集流程严谨：通过多阶段众包（写作、传播、验证、分割）和奖金激励，保证了指令质量和标签准确性。
- 丰富的语言分析：通过11种语言学现象系统量化了数据集的复杂性，并与多个现有数据集对比。
- 模型对比全面：在导航和SDR任务上均对比了非学习基线和多种学习模型，并进行了消融实验。

## 八、不足与局限
- 实验覆盖局限：导航模型仅测试了两种学习架构（GA和RCONCAT），未尝试更先进的模型（如基于Transformer、强化学习或预训练视觉语言模型）。SDR模型仅基于LINGUNET家族，未测试现代分割或目标检测方法。
- 算力资源未报告：缺乏GPU型号、数量、训练时间等细节，影响可复现性。
- 小样本语言分析：仅标注25个样本进行语言现象统计，样本量过小，可能无法充分代表整体数据分布。
- 完整任务评估简单：仅用流水线组合，未尝试端到端训练或联合优化。
- 数据偏差风险：数据仅来自纽约市一条街道网络，环境多样性有限；工人偏好（如常放置Touchdown在垃圾桶、标志牌等特定物体上）可能导致模型学习位置偏差。
- 应用限制：导航环境依赖预定义的图结构和固定全景图，无法扩展至任意城市；SDR任务假设目标不可见（隐藏在图像中），与真实定位任务存在差距。

（完）
