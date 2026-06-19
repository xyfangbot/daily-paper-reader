---
title: "SOON: Scenario Oriented Object Navigation with Graph-based Exploration"
title_zh: SOON：基于图探索的场景导向目标导航
authors: "Fengda Zhu, Xiwen Liang, Yi Zhu, Qizhi Yu, Xiaojun Chang, Xiaodan Liang"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/015-2021_zhu_soon-64da9de8-468876b83da2.pdf
tags: ["query:手动上传", "paper:PDF", "query:Scenario Oriented Object Navigation", "query:Graph-based Exploration", "query:Vision-Language Navigation", "query:Embodied Navigation", "query:Object Navigation"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有视觉导航任务多从固定起点出发并依赖详细指令，偏离真实场景。本文提出场景导向物体导航（SOON）任务，要求代理从任意位置根据场景描述导航至目标。为解决该任务，提出基于图的探索（GBE）方法，将导航状态建模为图并学习子最优轨迹稳定训练。同时构建大规模FAO数据集，提供丰富语义场景描述。实验表明GBE在FAO和R2R数据集上优于多种最新方法。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1633, \"height\": 644, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1264, \"height\": 479, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 501, \"height\": 416, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1541, \"height\": 587, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 542, \"height\": 392, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1137, \"height\": 373, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1770, \"height\": 558, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1765, \"height\": 526, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1764, \"height\": 447, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 852, \"height\": 272, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-015-468876b83da2-soon-scenario-oriented-object-navigation-with-graph-based-exploration/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 848, \"height\": 277, \"label\": \"Table\"}]"
motivation: 现有导航基准从固定起点出发且依赖逐步指令，无法模拟人类仅根据场景描述从任意位置导航的复杂需求。
method: 提出基于图的探索（GBE）方法，将导航状态建模为图，通过图结构学习知识并利用子最优轨迹稳定训练。
result: GBE在FAO和R2R数据集上超越多种最新方法，消融实验验证了FAO数据集的质量。
conclusion: SOON任务和GBE方法推动了从任意位置基于场景描述导航的研究，FAO数据集为未来工作提供基准。
---

## 摘要
像人类一样能够在3D具身环境中从任意位置向语言引导的目标导航的能力是智能机器人的“圣杯”目标之一。然而，大多数视觉导航基准测试关注的是从固定起点出发，根据详细的逐步指令导航到目标。这种方法偏离了现实世界的问题——在现实中，人类只描述物体及其周围环境的样子，并请求机器人从任意位置开始导航。因此，本文引入了一种场景导向目标导航（SOON）任务。在该任务中，智能体需要从3D具身环境中的任意位置出发，根据场景描述定位目标。为了解决这一任务，我们提出了一种新颖的基于图的探索（GBE）方法，该方法将导航状态建模为图，并引入了一种基于图的探索方法来从图中学习知识，并通过学习次优轨迹来稳定训练。我们还提出了一个名为“从任意位置到目标”（FAO）的新大规模基准数据集。为了避免目标歧义，FAO中的描述提供了丰富的语义场景信息，包括：物体属性、物体关系、区域描述和附近区域描述。我们的实验表明，所提出的GBE在FAO和R2R数据集上均超越了多种最先进方法。在FAO上的消融研究验证了数据集的质量。

## Abstract
The ability to navigate like a human towards a language-guided target from anywhere in a 3D embodied environment is one of the ‘holy grail’ goals of intelligent robots. Most visual navigation benchmarks, however, focus on navigating toward a target from a fixed starting point, guided by an elaborate set of instructions that depicts step-by-step. This approach deviates from real-world problems in which human-only describes what the object and its surrounding look like and asks the robot to start navigation from anywhere. Accordingly, in this paper, we introduce a Scenario Oriented Object Navigation (SOON) task. In this task, an agent is required to navigate from an arbitrary position in a 3D embodied environment to localize a target following a scene description. To give a promising direction to solve this task, we propose a novel graph-based exploration (GBE) method, which models the navigation state as a graph and introduces a novel graph-based exploration approach to learn knowledge from the graph and stabilize training by learning sub-optimal trajectories. We also propose a new large-scale benchmark named From Anywhere to Object (FAO) dataset. To avoid target ambiguity, the descriptions in FAO provide rich semantic scene information includes: object attribute, object relationship, region description, and nearby region description. Our experiments reveal that the proposed GBE outperforms various state-of-the-arts on both FAO and R2R datasets. And the ablation studies on FAO validates the quality of the dataset.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有视觉导航基准（如 R2R、CVDN）大多从固定起点出发，依赖逐步的详细指令，偏离了真实场景——在现实世界中，人类通常仅描述目标物体及其周围环境的外观，期望机器人从任意位置自主探索并找到目标。
- 为此，论文提出了“场景导向物体导航”（SOON）任务：要求智能体在 3D 具身环境中，从任意起始点，仅根据一段包含物体属性、关系、区域和邻居区域描述的自然语言指令，定位目标物体。
- 任务包含两个子任务：导航（到达目标附近 3m 内）和定位（在全景图中正确识别目标物体方向）。
- 同时构建大规模基准数据集 From Anywhere to Object（FAO），提供 3,848 组包含层次语义的指令和 40K 轨迹，指令平均长度 38 词（远超 R2R 的 18 词），轨迹平均步数 9.6（R2R 为 6.0），更具挑战性。

## 二、论文提出的方法论
- **核心思想**：提出基于图的探索（Graph-based Exploration, GBE）方法，将导航过程中的状态建模为动态语义图，通过对图的显式建模和探索实现稳定、鲁棒的策略学习。
- **关键技术细节**：
  - **图规划器（Graph Planner）**：维护节点特征集 V（存储已访问和邻居节点的视觉特征）、边集 E（根据导航拓扑动态更新）和节点嵌入集 M（通过 GCN 基于 V 和 E 更新）。每一步，视觉编码器提取当前节点和邻居节点的特征并加入 V，边链接根据可达性建立。
  - **图输出特征**：对当前节点及其所有邻居节点的嵌入取平均，得到图级特征 `f^g_t`，与语言特征 `f^l_t` 进行跨模态匹配后用于动作预测和目标定位。
  - **动作空间**：候选动作为所有已观察到但未访问的节点（加上停止动作），数量随图动态变化。
  - **图探索（Graph-based Exploration）**：在训练中，采样自当前策略（非教师强制），然后通过图规划器计算各候选节点到目标的最短 Dijkstra 距离，选择最近节点作为教师动作，从而将探索与最优导向结合。
  - **训练目标**：组合三种损失：
    - 模仿学习损失（监督标准动作 `a^*`）
    - 强化学习损失（A2C 优势函数）
    - 图探索损失（监督图教师动作 `ˆa`）
  - **定位分支**：使用极坐标表示目标方向（航向角、俯仰角），以 MSE 损失回归。

## 三、实验设计
- **数据集**：
  - **FAO**（本文提出）：基于 Matterport3D 仿真器，90 个房屋，3,848 组指令，40K 轨迹。划分训练、验证（seen instruction、seen house、unseen house）和测试集。
  - **R2R**（标准 VLN 基准）：用于与现有方法对比。
- **对比方法**：
  - R2R 上：Seq2Seq、Ghost、Speaker-Follower、RCM、Monitor、Regretful、EGP（带 * 的表示使用了额外合成数据）。
  - FAO 上：Random、Speaker-Follower、RCM、AuxRN、GBE w/o GE（无图探索）、GBE（完整模型）。
- **评价指标**：
  - 导航：导航误差（NE）、Oracle 成功率（OSR）、成功率（SR）、按路径长度加权的成功率（SPL）。
  - 定位：定位成功率（Sloc），以及综合指标 SFPL（成功定位加权路径长度）。
- **消融实验**：
  - 模态消融（无视觉、无语言、两者均有）。
  - 信息粒度消融（仅物体名、加属性和关系、加区域信息、使用改写完整的指令）。

## 四、资源与算力
- 论文未明确说明使用的 GPU 型号、数量或训练时长。
- 仅提及训练配置：所有模型在训练集上训练 10K 次交互（interactions），优化器为 RMSProp，学习率 1e-4。

## 五、实验数量与充分性
- **实验数量**：
  - 在 R2R 上进行了主实验结果对比（见表 2），与 7 种以上方法比较。
  - 在 FAO 上进行了主实验（5 种基线 + 2 种 GBE 变体）以及人类性能参考（见表 3）。
  - 两组消融实验：输入模态消融（4 种组合，表 4）、信息粒度消融（4 种组合，表 5）。
- **充分性与公正性**：
  - 对比方法覆盖了模仿学习、强化学习、图方法、辅助任务等多种类型，具有代表性。
  - 在 R2R 上复现了标准设置；在 FAO 上使用统一训练步数和优化器。
  - 消融实验设计合理，逐步分析各模态和描述层次的贡献。
  - 不足之处：未在更多数据集（如 TouchDown、CVDN）上验证；对比方法中部分使用了额外数据（带 *），但论文已标注；未提供统计显著性检验。

## 六、论文的主要结论与发现
- GBE 在 R2R（无预训练/辅助任务）上优于所有对比方法，SPL 达 43.4%（测试集）。
- 在 FAO 测试集上，完整 GBE 比去掉图探索的版本在 OSR、SR、SPL、SFPL 上分别提升 0.7%、0.5%、1.5%、0.6%，验证了图探索的有效性。
- 人类性能（SR 90.4%，SPL 59.2%）远超所有模型，存在明显的人机差距，说明 SOON 任务具有挑战性。
- 消融实验表明：视觉与语言模态缺一不可；包含物体属性和关系的描述对导航性能至关重要；完整的自然语言改写指令优于拼接式描述。

## 七、优点
- **任务新颖性**：首次提出从任意位置根据场景描述进行物体导航的任务，更贴近真实机器人应用场景。
- **数据集质量高**：FAO 指令包含多层次语义（属性、关系、区域、邻居区域），平均长度更长、轨迹更复杂，且通过五步标注流程保证自然性和多样性。
- **方法创新**：GBE 将导航状态建模为图，利用 GCN 维护结构知识，并首创基于图的探索方法——在采样自非完美策略的轨迹中通过学习最优（Dijkstra最短）动作来稳定强化学习训练。
- **实验充分**：在两个数据集上与多种强基线对比，消融实验覆盖关键因素，且公开了人类性能作为上界。

## 八、不足与局限
- **泛化性**：仅在 Matterport3D 场景上评估，未在更多具身环境（如 Gibson、Habitat）或室外场景验证。
- **计算资源未说明**：缺乏 GPU 型号、数量及训练时间等重要可复现性信息。
- **局部最优风险**：图探索的教师动作依赖 Dijkstra 距离，在部分场景中可能引导至局部最优，尤其当目标可从多个位置观察到时（论文已考虑多目标位置，但未深入分析）。
- **定位分支简化**：定位仅回归中心点极坐标，未利用目标形状或大小信息，可能影响精度。
- **人机差距大**：模型性能远低于人类水平，说明当前方法尚不能可靠解决该任务，实际部署需更多突破。
- **数据规模限制**：FAO 仅 3K 指令、90 栋房屋，相比 R2R（7K 指令、90 栋）略少，且未提供大规模预训练数据。

（完）
