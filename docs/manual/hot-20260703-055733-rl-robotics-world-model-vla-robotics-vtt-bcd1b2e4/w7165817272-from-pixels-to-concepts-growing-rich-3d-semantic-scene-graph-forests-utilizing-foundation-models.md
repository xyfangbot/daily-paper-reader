---
title: "From Pixels to Concepts: Growing Rich 3D Semantic Scene Graph Forests utilizing Foundation Models"
title_zh: 从像素到概念：利用基础模型构建丰富的三维语义场景图森林
authors: "David Oberacker, Meike Deitersen, Niklas Spielbauer, Tristan Schnell, Georg Heppner, Arne Roennau"
date: 2026-06-22
pdf: "https://arxiv.org/pdf/2606.23312"
tags: ["query:热点论文筛选", "query:VLN方向", "query:具身智能公司相关", "paper:OpenAlex", "company:boston dynamics"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=boston dynamics; relation_source=abstract; query=zero-shot semantic navigation robot"
tldr: 现有3D场景图方法局限于预定义关系类别，忽略因果、环境等语义连接。本文利用基础模型（VLM+LLM）从像素生成实例概念节点和开放语义关系，再由LLM推理扩展出更抽象的概念节点，构建层次化3D场景图森林。在uHumans2和ScanNet数据集上验证了关系准确性和相关性，并在波士顿动力Spot机器人上展示了开放词汇物体检索的下游适用性。该方法提升了机器人对复杂环境的语义理解能力，为具身智能提供了更丰富的世界模型。
source: openalex
selection_source: hot_paper_scout
motivation: 现有3D场景图受限于固定关系类别，无法表达开放语义连接，限制了机器人对复杂环境的功能语义理解。
method: 利用VLM识别实例节点和关系，再经LLM推理生成抽象概念节点，构建包含概念节点的层次化3D场景图森林。
result: 在uHumans2和ScanNet上验证关系准确性和相关性，并在真实机器人Spot上成功实现开放词汇物体检索。
conclusion: 基础模型能构建语义更丰富、关系更开放的3D场景图森林，推动机器人场景理解与环境感知进步。
---

## 摘要
在复杂的真实世界环境中运行，要求机器人对其周围环境具备功能语义层面的理解。这需要一个详细的多层世界模型来捕捉其周围环境的复杂关系。层级三维场景图通过将几何、语义和关系数据整合到统一的空间框架中，解决了这一挑战。然而，当前的三维场景图方法通常局限于预定义关系类别的刚性结构，大多忽略了重要的语义连接，如因果联系或环境背景。本文探索了利用基础模型构建具有开放语义关系的三维场景图森林的潜力，以提升场景理解和机器人任务执行能力。我们提出了一种方法：首先由VLM识别特定实例的概念节点和关系，然后由LLM进行扩展，通过推理推断出更广泛、更抽象的概念节点和关系。然后将这些对象节点、概念节点和关系组装成一个层级三维场景图森林，并通过概念节点增强以表示抽象概念。在uHumans2和ScanNet室内数据集上进行了评估，验证了生成关系的准确性和相关性。通过利用ScanNet数据和波士顿动力Spot进行的真实室内部署，在开放词汇目标检索任务中展示了场景图森林在机器人应用中的下游适用性。本文利用基础模型构建更具表现力、语义更深的3D层级场景图，并展示了它们在提升机器人语义和环境理解方面的潜力。

## Abstract
Operating in complex real-world environments requires robots to understand their surroundings on a functional semantic level. This demands a detailed multi-layer world model capturing the complex relations of its surroundings. Hierarchical 3D scene graphs address this challenge by integrating geometric, semantic, and relational data within a unified spatial framework. However, current 3D scene graph approaches often restrict themselves to rigid structures of pre-determined relationship classes, mostly neglecting important semantic connections, like causal connections or environmental contexts. This paper explores the potential of foundation models to build forests of 3D scene graphs with open semantic relationships to improve scene understanding and robotic task execution. We propose a method where instance-specific concept-nodes and relationships are first identified by a VLM and extended upon by a LLM, inferring broader, more abstract concept-nodes and relationships through reasoning. These object-nodes, concept-nodes, and relationships are then assembled into a forest of hierarchical 3D scene graphs, enhanced with concept-nodes to represent abstract concepts. Evaluations were conducted on the uHumans2 and ScanNet indoor dataset, validating the accuracy and relevance of the generated relationships. Downstream suitability of scene-graph forests for robotics applications is demonstrated in an open-vocabulary object-retrieval task utilizing both ScanNet data and a real-world indoor deployment using a Boston Dynamics Spot. This paper leverages foundation models to create more expressive, semantically deep 3D hierarchical scene graphs and demonstrates their potential to advance semantic and environmental understanding in robotics.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 机器人在复杂真实环境中运行需要具备功能语义层面的理解，而传统3D场景图方法局限于预定义的关系类别（如空间关系），忽略了因果、环境等重要的开放语义连接。
- 现有开放词汇场景图方法（如ConceptGraphs、Open3DSG）虽然支持开放标签，但通常只生成对象间的成对关系，缺乏层级抽象结构，且大多只处理单一关系类型（如空间关系或功能关系）。
- 本文的核心动机是：利用基础模型（VLM + LLM）从像素级感知出发，自主生成包含非具身概念节点的层级化3D场景图森林，以提供更丰富、更结构化的语义环境模型，从而提升机器人的场景理解与下游任务执行能力。

## 二、论文提出的方法论
- **核心思想**：构建一个“森林”结构——多个并行的层级3D语义场景图，每个图以高层语义概念为根节点，以实例对象为叶节点，中间层为开放词汇的概念节点。对象之间不直接相连，而是通过概念节点实现语义传递，保持图的无环性质。
- **关键技术流程**：
  1. **对象节点提取**：使用YOLO-E进行开放词汇目标检测，结合vdb_mapping构建3D体素地图进行多目标追踪，获取每个对象的6D位姿、类别标签和边界框。VLM（Qwen3-VL）对每个检测类别进行确认。
  2. **概念节点与关系提取**：
     - **实例概念生成**：对每帧图像，VLM根据图像和检测掩码零样本预测对象属性（如颜色、材质、可操作性、语义子类），生成实例级概念节点和关系（如“椅子-具有材质-织物”）。
     - **元概念生成**：利用推理型LLM（Qwen3-Coder，32B，Thinking模式）基于已有概念节点生成更抽象的高层概念（如“颜色”“材质”“移动”“抓取”等），并建立跨概念的层级关系。关系类型示例包括：is type of, has color, has material, manipulable by, has affordance等。
  3. **场景图组装**：将所有唯一节点（对象节点+概念节点）和关系三元组组织成多个层级场景图，逐个添加关系并避免引入循环，最终形成森林结构。
- **关系类型定义**：论文明确空间关系被单独处理（通过3D体素地图），而概念关系注重功能、属性、类别等。关系表示为三元组 (subject, edge_label, object)，其中subject和object可以是对象节点或概念节点。

## 三、实验设计
- **数据集**：
  - **uHumans2**（Kimera中的公寓场景）：包含动态人类和物体，适合评估语义关系质量。
  - **ScanNet**（小型一居室公寓）：典型室内场景，用于评估关系生成准确性和下游任务。
  - **真实世界部署**：使用波士顿动力Spot机器人在室内环境进行开放词汇物体检索。
- **基准与对比方法**：
  - 对于关系生成，采用人工验证（人类在环）判断关系正确性，无自动基准方法。
  - 对于下游任务（物体检索），对比了三种方法：
    - Flat no attributes：仅提供对象列表（无任何属性）。
    - Flat with attributes（本文扩展）：提供对象及其关联的实例概念节点（属性）。
    - Graph-based（本文方法）：提供完整的图结构，通过ReAct风格智能体进行图遍历（从对象到概念或从概念到对象）。
- **评估指标**：关系生成准确率（%），物体检索准确率（%）。

## 四、资源与算力
- 论文未明确报告训练所用的GPU型号、数量、训练时长等具体算力信息。
- 文中提到使用了VLM（Qwen3-VL-8B-Instruct）和LLM（Qwen3-32B-Thinking），以及目标检测模型YOLO-E，所有模型均为预训练模型，论文未进行额外训练，仅进行零样本推理和少量微调（未说明）。
- 由于在ROS 2系统中实现，且需要处理RGB-D图像流，推断其使用了至少一台配备足够GPU（如A100或类似）的服务器进行实时/准实时推理。

## 五、实验数量与充分性
- **实验组数**：
  - 关系生成评估：每个数据集运行3次取平均，报告均值和标准差（表I）。uHumans2和ScanNet各做3次，共6次实验。
  - 物体检索任务：ScanNet场景20次查询 × 3种方法 = 60次；真实场景类似（推测也为20次查询 × 3种方法 = 60次）。总计约120次查询。
  - 关系类型准确率分解（表I下方）：对不同关系类型（has class, manipulable by, has material, has color, is type of, has affordance）分别统计。每种类型基于不同数量的生成关系。
- **充分性评价**：
  - **优点**：覆盖两个公开数据集（一个含动态元素，一个静态），以及真实场景验证；进行了重复运行统计方差；消融了不同访问方法对下游任务的影响。
  - **不足**：关系生成评估依赖人工标注，可能引入主观偏差；仅对比了自己提出的三种方法，未与ConceptGraphs、Open3DSG等基线进行直接对比（仅文本提及ConceptGraphs的节点准确率61-71%，但未在相同设置下比较）。下游任务仅测试了物体检索单一场景，未涵盖语义导航、任务规划等更复杂任务。

## 六、论文的主要结论与发现
- **关系生成**：整体准确率约61.4%，平均每个场景生成276.2个正确关系（基于约50个对象节点）。视觉相关的属性（颜色、材质）准确率较高（57%-60%），知识依赖的affordance准确率极低（16.3%）。节点重复（词汇变体）是主要问题，但语义上准确率更高。
- **下游任务**：Scene-graph-based方法在ScanNet上准确率70.0%（不如flat with attributes的86.6%），但在真实场景中达到100%（图遍历有效利用结构）。Flat with attributes（即加入实例概念节点）相比无属性基线提升13.3%。表明概念节点能显著帮助对象消歧。
- **总体结论**：基础模型能够生成大量语义正确、机器人相关的概念节点和开放关系，构建的场景图森林可有效支撑下游物体检索等任务，为具身智能提供更丰富的世界模型。

## 七、优点
- **创新性**：提出“场景图森林”概念，将多个层级场景图与抽象概念节点结合，突破传统单一图或固定关系类别的限制。
- **完全开放词汇**：节点和边标签均为自由生成，无需预定义本体，适应动态变化环境。
- **模块化设计**：VLM处理视觉信息生成实例概念，LLM进行推理生成抽象概念，分工明确，易于扩展新关系类型。
- **鲁棒的处理流程**：通过自验证（VLM确认检测类别）和循环检测避免重复节点，保证图的无环性。
- **实用性验证**：在真实机器人平台（波士顿动力Spot）上成功演示，说明方法具备现实部署可行性。
- **可解释性**：通过图结构和概念层级，智能体能够进行结构化推理（如链式思考），减少幻觉。

## 八、不足与局限
- **实验覆盖不足**：关系生成评估仅依赖人工判断，缺乏与最先进方法（如ConceptGraphs、Open3DSG）的直接定量对比。下游任务仅限于物体检索，未测试语义导航、任务规划等更典型机器人应用。
- **计算开销**：使用了VLM（8B参数）和LLM（32B参数）进行多轮推理，无法实现实时处理，限制了在边缘设备上的部署。论文承认这目前是非实时处理。
- **词汇变体问题**：生成的节点存在大量同义或近义变体（如“grasp” vs “grasping”），导致节点冗余，需增加后处理合并。
- **抽象关系生成困难**：高层元概念（如affordance）准确率极低（16.3%），表明LLM/VLM在高级功能推理上能力不足。
- **目标检测依赖**：当前依赖YOLO-E的检测结果，若检测失败则后续节点和关系均受影响，且未在论文中分析检测误差传播。
- **公平性局限**：在物体检索任务中，Graph-based方法在ScanNet上表现不如Flat with attributes，作者归因于图规模过大导致智能体步数限制，表明当前方法在处理大规模图时效率不足。

（完）
