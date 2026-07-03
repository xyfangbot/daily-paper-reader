---
title: "From Pixels to Concepts: Growing Rich 3D Semantic Scene Graph Forests utilizing Foundation Models"
title_zh: 从像素到概念：利用基础模型构建丰富的3D语义场景图森林
authors: "David Oberacker, Meike Deitersen, Niklas Spielbauer, Tristan Schnell, Georg Heppner, Arne Roennau"
date: 2026-06-22
pdf: "https://arxiv.org/pdf/2606.23312"
tags: ["query:热点论文筛选", "query:VLN方向", "query:具身智能公司相关", "paper:OpenAlex", "company:boston dynamics"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=boston dynamics; relation_source=abstract; query=zero-shot semantic navigation robot"
tldr: 现有3D场景图局限于预定义关系类别，忽略因果、环境等语义连接。本文提出利用VLM识别实例概念节点与关系，LLM推理抽象概念节点，构建层次化3D场景图森林。在uHumans2和ScanNet上验证关系准确性，并在开放词汇目标检索任务中展示实效。该方法拓展了场景图的表达深度，提升了机器人对复杂环境的语义理解能力。
source: openalex
selection_source: hot_paper_scout
motivation: 现有3D场景图局限于预定义关系类，缺乏因果、环境等语义连接，限制了机器人对复杂环境的深层次理解。
method: 先用VLM识别实例概念节点与关系，再用LLM推理抽象概念节点及关系，组装为包含概念节点的层次化3D场景图森林。
result: 在uHumans2和ScanNet数据集上验证了生成关系的准确性与相关性；在Boston Dynamics Spot机器人上成功完成开放词汇目标检索任务。
conclusion: 利用基础模型构建更丰富语义的3D场景图森林，有效提升了机器人对环境的语义理解和任务执行能力。
---

## 摘要
在复杂的真实世界环境中操作要求机器人从功能语义层面理解其周围环境。这需要一个详细的多层世界模型来捕捉环境中的复杂关系。层次化3D场景图通过在统一的空间框架内整合几何、语义和关系数据来解决这一挑战。然而，当前的3D场景图方法通常局限于预定义关系类别的刚性结构，大多忽略了重要的语义联系，如因果联系或环境上下文。本文探索了利用基础模型构建具有开放语义关系的3D场景图森林的潜力，以提升场景理解和机器人任务执行。我们提出了一种方法，其中首先由VLM识别特定实例的概念节点和关系，然后由LLM进行扩展，通过推理推断出更广泛、更抽象的概念节点和关系。这些对象节点、概念节点和关系随后被组装成一个层次化3D场景图森林，并通过概念节点增强以表示抽象概念。在uHumans2和ScanNet室内数据集上进行了评估，验证了生成关系的准确性和相关性。场景图森林在机器人应用中的下游适用性通过一个开放词汇的对象检索任务得到了证明，该任务利用了ScanNet数据以及使用波士顿动力Spot的真实室内部署。本文利用基础模型创建更具表现力、语义更深的3D层次化场景图，并展示了它们在提升机器人语义和环境理解方面的潜力。

## Abstract
Operating in complex real-world environments requires robots to understand their surroundings on a functional semantic level. This demands a detailed multi-layer world model capturing the complex relations of its surroundings. Hierarchical 3D scene graphs address this challenge by integrating geometric, semantic, and relational data within a unified spatial framework. However, current 3D scene graph approaches often restrict themselves to rigid structures of pre-determined relationship classes, mostly neglecting important semantic connections, like causal connections or environmental contexts. This paper explores the potential of foundation models to build forests of 3D scene graphs with open semantic relationships to improve scene understanding and robotic task execution. We propose a method where instance-specific concept-nodes and relationships are first identified by a VLM and extended upon by a LLM, inferring broader, more abstract concept-nodes and relationships through reasoning. These object-nodes, concept-nodes, and relationships are then assembled into a forest of hierarchical 3D scene graphs, enhanced with concept-nodes to represent abstract concepts. Evaluations were conducted on the uHumans2 and ScanNet indoor dataset, validating the accuracy and relevance of the generated relationships. Downstream suitability of scene-graph forests for robotics applications is demonstrated in an open-vocabulary object-retrieval task utilizing both ScanNet data and a real-world indoor deployment using a Boston Dynamics Spot. This paper leverages foundation models to create more expressive, semantically deep 3D hierarchical scene graphs and demonstrates their potential to advance semantic and environmental understanding in robotics.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有 3D 场景图（3D Scene Graph）方法大多采用刚性预定义关系类别（如空间关系、固定本体），缺乏对因果联系、环境上下文等深层次语义连接的建模，限制了机器人对复杂环境的理解。
- 机器人需要在功能语义层面理解环境，以执行复杂多步任务。因此需要一种更灵活、表达能力更强的场景表示，能够自主抽象出远超对象层级的语义概念。
- 该论文旨在利用视觉语言模型（VLM）和大型语言模型（LLM）构建“3D 语义场景图森林”，即多个并行、层次化的场景图，其中对象节点连接到开放词汇的概念节点，从而表达丰富的语义关系。

## 二、论文提出的方法论
- **核心思想**：将场景图从单一刚性结构扩展为“森林”（forest），每个子图代表一种概念层次，叶节点为环境中的物理对象（object nodes），内部节点为抽象概念（concept nodes），关系类型完全开放词汇。
- **关键技术流程**（四步）：
  1. **对象节点提取**：使用 YOLO-E（开放词汇目标检测）从 RGB-D 图像中检测对象，结合 vdb_mapping 构建 3D 体素地图，进行多目标跟踪，得到每个对象的 6D 位姿、类别标签。
  2. **实例概念节点与关系生成**：将当前帧图像、检测掩膜和对象信息输入 VLM（Qwen3-VL 8B），零样本推断对象属性（如颜色、材质、可操纵性等），生成“对象 → 概念”边（如“椅子 → has_color → 棕色”）。
  3. **元概念节点与关系生成**：将已生成的概念节点输入推理式 LLM（Qwen3-Coder 32B），借助其世界知识和推理能力生成更高层的抽象概念（如“可握持”、“运动”、“材质”等）和关系（如“has_affordance”、“is_type_of”）。
  4. **场景图组装**：将所有关系三元组（对象/概念 → 关系 → 概念）组织成无环的层次化图结构，对象节点作为叶子，元概念节点作为根，形成多个语义子图（森林）。关系类型可随时扩展，无需固定本体。
- **公式表示**：森林 ℱ = { (𝒪, 𝒞, ℛ) }，其中 𝒪 为对象节点（含位姿、类标签），𝒞 为概念节点（只有标签），ℛ 为关系三元组。森林不构成正式森林，但概念节点子集 ℱ𝒞 形成无环层次图。

## 三、实验设计
- **使用的数据集**：
  - uHumans2（公寓环境）
  - ScanNet（单卧室公寓场景）
  - 真实世界室内环境（波士顿动力 Spot 机器人）
- **Benchmark 与评估方式**：
  - **关系质量**：对每对关系进行人工“正确/错误”标注（人机回环标注），计算准确率。其中“has_class”关系默认正确（不惩罚检测错误）。
  - **下游任务**：开放词汇对象检索任务。给定自然语言查询（如“把绿色的青蛙玩偶拿过来”），测试三种访问场景图的方式：
    1. Flat no attributes：仅提供对象列表（传统方法）
    2. Flat with attributes：提供对象及其实例概念属性（相当于我们的部分方法）
    3. Graph-based：提供图形遍历工具（完全利用森林结构）
- **对比方法**：三种方法之间对比，未与 ConceptGraphs 等外部方法直接对比准确率（仅在分析中提及 ConceptGraphs 节点准确率 61-71%）。

## 四、资源与算力
- **文中未明确说明训练资源**（如 GPU 型号、数量、训练时长等），只强调使用了推理模型（VLM: Qwen3-VL 8B；LLM: Qwen3 32B 思考模型）。
- 系统基于 ROS 2 实现，处理流程非实时（非在线流式），依赖高算力推理。作者指出未来会转向连续实时处理以降低移动机器人对带宽的依赖。

## 五、实验数量与充分性
- **关系质量实验**：在 uHumans2 和 ScanNet 各进行了 3 次独立运行（共 6 次），统计生成关系数量、正确数量、准确率均值与标准差。样本量中等，但未做跨场景、跨配置的消融（如不同模型、不同提示策略）。
- **下游任务实验**：每个场景进行 3 轮，每轮 20 次查询，共 60 个查询。ScanNet 场景中有 80 个对象被跟踪。真实世界场景中对象较少。实验设计较充分，但缺少与其他开放词汇场景图方法（如 ConceptGraphs）的直接对比，仅内部对比三种访问方式。
- **公平性**：人工标注可能存在主观偏差，且“has_class”默认正确会夸大准确率。实验覆盖了仿真和真实场景，但真实场景仅一次部署，可重复性不够。

## 六、论文的主要结论与发现
- 方法能够生成大量新颖、语义相关、对机器人有用的概念节点和关系。综合准确率约 61.4%，平均每个场景生成约 462 个关系，其中正确 276 个。
- 不同关系类型准确率差异大：视觉相关关系（颜色、材质、类型）准确率高（57%-73%），但知识依赖关系（affordance）准确率极低（16.3%）。
- 在下游对象检索任务中，“flat with attributes”比“flat no attributes”准确率提升约 13%（ScanNet 上 73.3% → 86.6%），说明实例概念节点有助于消歧。真实场景中 graph-based 方法达到 100% 准确率（对象数量少），但仿真中因图过大（约 400 节点）导致 agent 步数耗尽，准确率仅 70%。
- 层次化概念结构为 LLM agent 提供了有指导的推理路径（如图 6 所示），减少幻觉，提升结构化推理。

## 七、优点
- **完全开放词汇**：无需预定义本体，关系类型和概念标签均可自由生成，灵活适应各种环境。
- **层次化与多图并行**：通过“森林”结构同时表示多个语义维度（颜色、材质、功能等），便于按概念检索对象。
- **利用基础模型强大推理能力**：VLM 处理视觉属性，LLM 处理抽象推理，互补性强。
- **下游任务表现提升**：实例概念节点显著提高了对象检索准确率，证明了语义深度的价值。
- **可扩展性**：关系类型可轻松添加，未来可集成到实时 SLAM 框架中。

## 八、不足与局限
- **低层关系准确率低**：尤其是 affordance 关系（16.3%），表明纯知识推理在该类型上失效。
- **词汇变体导致节点重复**：如“grasp”与“grasping”，“push”与“pushing”未合并，造成图膨胀和语义冗余。
- **元概念生成不足**：meta-level 关系仍然稀疏，且对图大小敏感，在大图（如 ScanNet 约 400 节点）中 agent 无法有效遍历。
- **实验对比不充分**：未与 ConceptGraphs、Open3DSG 等方法进行定量对比（准确率、任务成功率），无法直接衡量相对优势。
- **实时性限制**：当前流程非实时（依赖离线或准离线推理），不适用于高动态环境。
- **评估有偏风险**：人工标注主观，且“has_class”默认正确可能会高估系统实际感知能力。真实世界部署只有单次实验，可推广性需进一步验证。

（完）
