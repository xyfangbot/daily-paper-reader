---
title: "AerialVLN: Vision-and-Language Navigation for UAVs"
title_zh: "AerialVLN: 无人机的视觉与语言导航"
authors: "Shubo Liu, Hongsheng Zhang, Yuankai Qi, Peng Wang, Yanning Zhang, Qi Wu"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/010-2023_liu_aerialvln-d57f653d-444a5e932af8.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:UAV navigation", "query:Aerial navigation", "query:Cross-modal learning", "query:Embodied AI"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有视觉语言导航任务主要针对地面场景，忽略了空中无人机导航需求。本文提出AerialVLN，一个基于无人机的室外视觉语言导航任务，并开发了包含25个城市级场景的3D模拟器，支持连续导航和灵活扩展。基于跨模态对齐方法构建基线模型，实验表明模型性能与人类表现存在显著差距，证实了该任务的挑战性。该工作填补了空中导航的空白，为无人机应用提供了新的研究方向。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-010-444a5e932af8-aerialvln-vision-and-language-navigation-for-uavs/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 815, \"height\": 332, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-010-444a5e932af8-aerialvln-vision-and-language-navigation-for-uavs/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 807, \"height\": 380, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-010-444a5e932af8-aerialvln-vision-and-language-navigation-for-uavs/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1693, \"height\": 552, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-010-444a5e932af8-aerialvln-vision-and-language-navigation-for-uavs/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 820, \"height\": 284, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-010-444a5e932af8-aerialvln-vision-and-language-navigation-for-uavs/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1698, \"height\": 856, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-010-444a5e932af8-aerialvln-vision-and-language-navigation-for-uavs/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1705, \"height\": 443, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-010-444a5e932af8-aerialvln-vision-and-language-navigation-for-uavs/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1700, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-010-444a5e932af8-aerialvln-vision-and-language-navigation-for-uavs/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 807, \"height\": 230, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-010-444a5e932af8-aerialvln-vision-and-language-navigation-for-uavs/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1706, \"height\": 535, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-010-444a5e932af8-aerialvln-vision-and-language-navigation-for-uavs/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 814, \"height\": 261, \"label\": \"Table\"}]"
motivation: 现有VLN任务局限于地面，无法满足空中导航需求，而空中导航需考虑飞行高度和复杂空间推理，因此提出无人机VLN任务。
method: 开发基于25个城市级场景的3D模拟器，支持连续导航和环境扩展；采用跨模态对齐方法构建基线模型。
result: 基线模型与人类性能存在显著差距，表明AerialVLN具有挑战性。
conclusion: AerialVLN填补了空中视觉语言导航空白，为无人机在货物配送、巡逻等应用提供了新基准。
---

## 摘要
最近兴起的视觉与语言导航（VLN）任务引起了计算机视觉和自然语言处理领域的广泛关注。现有的VLN任务是为在地面（室内或室外）导航的智能体设计的。然而，许多任务需要智能体在空中执行，例如基于无人机的货物配送、交通/安全巡逻和风景游览等。空中导航比地面导航更为复杂，因为智能体需要考虑飞行高度和更复杂的空间关系推理。为了填补这一空白并促进该领域的研究，我们提出了一项名为AerialVLN的新任务，该任务基于无人机且面向室外环境。我们开发了一个由25个城市场景的近真实图片渲染的3D模拟器。该模拟器支持连续导航、环境扩展和配置。我们还基于广泛使用的跨模态对齐（CMA）导航方法提出了一个扩展的基线模型。我们发现基线模型与人类表现之间仍存在显著差距，这表明AerialVLN是一项新的具有挑战性的任务。

## Abstract
Recently emerged Vision-and-Language Navigation (VLN) tasks have drawn significant attention in both computer vision and natural language processing communities. Existing VLN tasks are built for agents that navigate on the ground, either indoors or outdoors. However, many tasks require intelligent agents to carry out in the sky, such as UAV-based goods delivery, traffic/security patrol, and scenery tour, to name a few. Navigating in the sky is more complicated than on the ground because agents need to consider the flying height and more complex spatial relationship reasoning. To fill this gap and facilitate research in this field, we propose a new task named AerialVLN, which is UAV-based and towards outdoor environments. We develop a 3D simulator rendered by near-realistic pictures of 25 city-level scenarios. Our simulator supports continuous navigation, environment extension and configuration. We also proposed an extended baseline model based on the widely-used cross-modal-alignment (CMA) navigation methods. We find that there is still a significant gap between the baseline model and human performance, which suggests AerialVLN is a new challenging task.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **现有VLN任务的局限**：当前视觉与语言导航（VLN）任务（如R2R、RxR、TouchDown等）均面向地面智能体（室内或室外），未考虑空中场景。然而，无人机应用（货物配送、交通巡逻、风景游览等）日益普及，需要智能体在空中执行复杂导航任务。
- **空中导航的独特挑战**：相比地面导航，空中导航需要额外考虑飞行高度、更大的动作空间（升降、侧移）、更长的路径（平均661.8米）、更复杂的空间关系推理（鸟瞰视角下的物体参照），以及动态交互环境（天气、光照变化、3D避障）。
- **研究空白**：缺乏面向无人机、基于自然语言指令的室外连续导航数据集与任务。为填补此空白，作者提出**AerialVLN**，一个城市级无人机VLN任务与数据集。

## 二、论文提出的方法论
- **核心思想**：构建一个支持连续导航的3D仿真环境（基于Unreal Engine 4 + AirSim），收集由持有AOPA证书的无人机驾驶员手动飞行生成的轨迹，再通过AMT众包为每条轨迹标注3条自然语言指令，形成大规模数据集。在此基础上，扩展经典跨模态对齐（CMA）模型，引入**前瞻引导**（Look-ahead Guidance, LAG）策略来改进训练。
- **关键技术细节**：
  - **模拟器**：提供RGB图像、深度图像（感知距离100米），支持动态环境（气候、光照变化）；动作空间包括8种基本动作：前进、左转、右转、上升、下降、左移、右移、停止（持续移动距离：前进/侧移5单位，升降2单位，转弯15度）。
  - **数据集生成**：由AOPA执照飞行员在模拟器中手动飞行，经过多个预设地标生成路径；去除冗余动作后离散化为元动作序列；AMT工作者观看视频后编写自然语言指令，每条路径有三条不同指令；所有指令经人工质检。
  - **基线模型扩展（LAG）**：针对标准学生强制训练中“最短路径”行动标签与指令不符的问题，提出前瞻引导。当智能体偏离真实路径时，计算从当前位置返回真实路径的最短路径，然后沿真实路径向前看10步得到目标点，再计算当前位置到该目标点的最短路径，取第一步作为伪真实行动。该策略与CMA模型结合形成LAG基线。
- **算法流程（文字说明）**：CMA基线包含视觉跟踪LSTM（接收RGB、深度特征和上一步动作嵌入）与指令编码（BiLSTM生成词级隐藏状态）。通过缩放点积注意力交互计算文本与图像上下文特征，拼接后经另一LSTM输出动作概率分布。LAG则在训练时动态生成伪真实行动标签，替代静态最短路径标签。

## 三、实验设计
- **数据集与场景**：AerialVLN包含25个城市场景（城市中心、工厂、公园、村庄等），870多种物体；总计8446条路径、25338条指令，平均指令长度83词，词汇量4470。按标准划分：训练集17场景（5460路径/16380指令）、验证集可见17场景（606路径/1818指令）、验证集不可见8场景（770路径/2310指令）、测试集不可见8场景（1610路径/4830指令）。另外提供**AerialVLN-S**小型场景版本（路径更短、场景更小）。
- **评估指标**：成功率（SR，20米内算成功）、预言成功率（OSR，轨迹上任一点距目标<20米）、导航误差（NE，平均终点距离）、成功加权归一化动态时间规整（SDTW，考虑路径相似性）。
- **对比方法**：6种基线（在AerialVLN-S上评估8种）：
  1. **Random**：随机选取动作。
  2. **Action Sampling**：按训练集动作分布采样。
  3. **LingUNet**：原用于LANI的空中VLN模型，改为逐步骤范式。
  4. **Seq2Seq**：标准序列到序列模型（ResNet RGB + ResNet Depth + LSTM指令编码 + GRU动作预测）。
  5. **CMA**：跨模态注意力模型（双向LSTM指令编码+注意力+双向LSTM决策）。
  6. **Seq2Seq-DA / CMA-DA**：添加数据集聚合（DA）策略（采样预测动作而非真实动作进行训练）。
  7. **LAG**（本文提出）：CMA + 前瞻引导。
  此外，与**人类表现**对比（测试集上人类SR约80.8%）。
- **消融实验**：在CMA模型上分别移除RGB、深度、RGB+深度（纯视觉）、语言指令，测试模态贡献。
- **额外分析**：按路径长度分组长/短路径的SR对比；定性可视化成功案例与失败原因分析。

## 四、资源与算力
- 论文中**未明确说明**训练所用的GPU型号、数量、训练时长等算力信息。仅提及基于PyTorch实现，未提供硬件细节。

## 五、实验数量与充分性
- **实验数量**：主要结果表（Table 4）包含：
  - AerialVLN全数据上5种方法（Random、Action Sampling、Seq2Seq、CMA、Human）在验证可见/不可见、测试集上的5个指标。
  - AerialVLN-S上8种方法（S1~S8）的同样指标。
- **消融实验**：1组模态消融（Table 5，5种配置，报告验证不可见集上的4个指标）。
- **额外分析**：路径长度对成功率的影响、失败原因定性分析、语言现象统计（Table 2）、数据集对比（Table 1）。
- **充分性与公平性**：
  - 覆盖了随机、统计、经典VLN基线、空中专用基线（LingUNet）、强化学习变体（DA）、人类上限，方法种类较全。
  - 在相同数据划分、相同评估协议下比较，公平性较好。
  - 消融实验验证了RGB、深度、语言各模态的必要性。
  - 但**缺乏对LAG方法的更深入消融**（如不同look-ahead步长的对比、是否与其他DA策略结合等），实验数量偏少。

## 六、论文的主要结论与发现
1. **AerialVLN极具挑战性**：随机模型成功率0%，学习基线SR仅1.0%~3.9%，而人类表现约80.8%，存在巨大差距。
2. **空中导航比地面导航难得多**：CMA-DA在AerialVLN-S上SR仅4.5%，远低于连续R2R上的27%。
3. **语言与视觉模态均至关重要**：移除任一模态导致性能显著下降（SR从4.5%降至2.1%或1.3%）。
4. **RGB信息比深度更重要**：移除RGB后SR降至3.2%，移除深度后SR为3.0%（OSR降低更多）。
5. **前瞻引导（LAG）有效**：在验证不可见集上SR提升至5.1%（优于CMA-DA的4.5%），SDTW提升至1.4%。
6. **长路径是主要失败因素**：长路径组SR仅1.8%，短路径组达7.4%；且模型常错过目标点（OSR远高于SR，说明经过目标但未停止）。
7. **数据聚合（DA）带来一定提升**：在AerialVLN-S上，DA使可见集SR提升约6%，但不可见集提升有限（约1%）。

## 七、优点
- **任务新颖且有实际价值**：首次提出面向无人机的室外连续VLN任务，填补研究空白，场景覆盖广（25个城市场景），路径长、指令丰富，反映真实应用需求。
- **数据质量高**：路径由AOPA持证飞行员手动飞行，指令由AMT众包且经人工验证，保证自然性与可靠性；子路径与子指令对应关系支持细粒度对齐学习。
- **模拟器功能强大**：基于Unreal Engine 4 + AirSim，支持动态环境（天气、光照变化）、连续导航、4-DOF动作，接近真实无人机飞行。
- **基线丰富**：评估了从随机到黄金标准的多种方法，并提出了改进的LAG策略，为社区提供参考基准。
- **消融充分**：通过模态消融清晰揭示了RGB、深度、语言各自的贡献。
- **开源代码与数据集**：便于后续研究者复现与扩展。

## 八、不足与局限
1. **实验覆盖不足**：
   - 仅对比了单步决策模型（Seq2Seq、CMA），未尝试更先进的方法（如基于Transformer的分层策略、强化学习方法（R2R中的DRL）、预训练模型（VLN-BERT等）。
   - LAG策略仅在CMA上测试，未与其他基线结合；也未对比不同look-ahead步长的影响。
   - 仅在AerialVLN-S上测试了DA和LAG，全数据AerialVLN上未报告DA或LAG结果（Table 4中#5行Human对应全数据，但LAG只在AerialVLN-S中）。
2. **资源信息缺失**：未报告训练硬件与时间，不利于复现与公平比较。
3. **评估指标可能不全面**：未使用动态时间规整（DTW）或归一化DTW的原始版本，仅用了SDTW；未报告推理速度或模型参数量。
4. **潜在偏差**：指令由AMT工人编写，可能包含文化或语言偏差；环境虽然是25个城市级场景，但均是虚拟合成，与真实无人机视觉风格仍有差距（sim-to-real gap未讨论）。
5. **应用限制**：假设20米成功半径（对应于直升机停机坪尺寸），但在某些密集城区可能不合理；未考虑风、能耗、实际无人机动力学约束（如最大倾斜角、转速等）。
6. **缺乏与真实无人机实验的验证**：所有实验均在仿真环境中进行，无法证明模型在实际无人机上的可迁移性。

（完）
