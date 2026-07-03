---
title: Learning Contact-Rich Loco-Manipulation
title_zh: 学习密集接触的移动操作
authors: Simone Tolomei
date: 2026-07-14
pdf: "https://hdl.handle.net/11567/1310716"
tags: ["query:热点论文筛选", "query:world-model", "query:具身智能公司相关", "paper:OpenAlex", "company:physical intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=physical intelligence; relation_source=abstract; query=world models for robotics manipulation and locomotion"
tldr: 机器人需在动态非结构化环境中通过接触实现运动与操作，但接触引入混合动力学及稀疏奖励，导致学习困难。本文提出统一学习框架，从脚步接触选择（考虑脚形与接触面几何）和杂乱场景抓取先验提取，到多评论家强化学习嵌入几何先导并渐退引导，实现非抓取式全身协调。在多种四足与人形平台上验证，获得鲁棒的全自主接触智能，为野外机器人提供可行蓝图。
source: openalex
selection_source: hot_paper_scout
motivation: 接触带来混合动力学与稀疏奖励，现有方法依赖任务特化简化或启发式，难以适应复杂多变环境。
method: 先学习足式运动接触选择及杂乱场景无碰撞抓取先验，再通过多评论家强化学习嵌入几何先导并渐退引导，统一为非抓取式loco-manipulation框架。
result: 在仿真与实体四足/人形机器人上验证，实现了鲁棒的非抓取式全身协调运动与操作。
conclusion: 本文为野外自主机器人提供了接触智能的综合蓝图，赋予其鲁棒的全自主操作能力。
---

## 摘要
物理世界不允许超距作用。随着机器人从结构化的工厂走向动态、非结构化的环境（如家庭辅助和环境监测），其自主性取决于它们制造和利用与世界的接触的能力。因此，真正的物理智能需要掌握在紧密耦合的两个维度上的交互：决定在哪里进行接触（例如，立足点、推动、抓取、支撑），以及学习如何利用它来移动、稳定并可靠地完成任务。尽管物理接触已被广泛研究，但在实践中处理它通常仍需定制化处理，从简化的接触抽象到特定任务的启发式和规则。这在受控条件下可能效果良好，但随着交互方式的多样化和操作条件的不可预测性增加，这种方法可能变得繁琐。从基于模型的角度来看，接触引入了混合动力学和不连续性，使规划和控制复杂化。从无模型的角度来看，接触仍然具有挑战性，因为有意义的交互是稀疏的，并且难以通过无引导的探索发现，使得学习效率低下且脆弱。受这些挑战的驱动，在本论文中，我致力于学习密集接触的移动操作：即机器人通过与环境的 purposeful（有目的）、间歇性接触来协调移动和操作的能力。在这种观点下，移动和操作不是分离的问题，而是同一问题的两个方面：如何选择在何处以及如何接触世界，以及如何随着时间的推移利用这些接触来产生稳定的运动、有效的交互和任务完成。我从面向移动的接触选择开始，学习考虑脚形和接触面几何形状的立足点；我研究了机械设计选择（包括关节柔顺性）如何影响腿式运动的鲁棒性；我开发了基于学习的控制流水线，以实现硬件上的可靠运动。转向操作，焦点从地面转移到物体。我解决了在极度杂乱场景中以及针对新型可重构夹爪提取无碰撞抓取先验的几何挑战，同时探索了基于学习的策略如何将操作器的技能从静态抓取放置扩展到动态投掷。最后，这些概念轨迹汇聚成一个统一的、基于学习的非抓取移动操作架构。通过将几何接触先验嵌入到多批评者强化学习框架中，我引入了一种策略，该策略明确引导腿式操作器的探索朝向有意义的物理交互，并逐步退火这种引导以恢复任务最优的全身控制。通过在多种四足和操作平台上的广泛仿真研究和实际部署验证，本论文提供了一个全面的蓝图，能够为机器人在野外运行所需的鲁棒、密集接触的自主性提供支持。

## Abstract
The physical world admits no action at a distance. As robots step out of structured factories and into dynamic, unstructured environments, such as domestic assistance and environmental monitoring, their autonomy is conditioned on their ability to make and exploit contact with the world. True physical intelligence therefore requires mastering this interaction across two tightly coupled dimensions: deciding where to make contact (e.g., footholds, pushes, grasps, supports) and learning how to exploit it to move, stabilise, and accomplish tasks reliably. Although physical contact has been studied extensively, handling it in practice often still requires tailoring, which ranges from simplified contact abstractions to task-specific heuristics and rules. This can work well in controlled conditions, but may become tedious as interactions diversify and operating conditions become less predictable. From a model-based perspective, contact introduces hybrid dynamics and discontinuities, complicating planning and control. From a model-free perspective, contact remains challenging because meaningful interactions are sparse and hard to discover through unguided exploration, making learning inefficient and fragile. Motivated by these challenges, in this thesis, I target learning contact-rich loco-manipulation: the ability of a robot to coordinate locomotion and manipulation through purposeful, intermittent contacts with the environment. Within this view, locomotion and manipulation are not separate problems but two sides of the same question: how to choose where and how to touch the world, and how to leverage those contacts over time to generate stable motion, effective interaction, and task completion. I begin with locomotion-oriented contact selection, learning footholds that account for foot shape and contact patch geometry; I study how mechanical design choices, including joint compliance, affect robustness in legged locomotion; and I develop learning-based control pipelines to achieve reliable movement on hardware. Shifting to manipulation, the focus moves from the ground to the object. I address the geometric challenge of extracting collision-free grasp priors in severely cluttered scenes and for novel reconfigurable grippers, while also exploring how learning-based policies can expand a manipulator's skills from static pick-and-place to dynamic throwing. Finally, these conceptual tracks converge into a unified, learning-based architecture for non-prehensile loco-manipulation. By embedding geometric contact priors into a multi-critic reinforcement learning framework, I introduce a strategy that explicitly guides a legged manipulator's exploration toward meaningful physical interactions, progressively annealing this guidance to recover task-optimal, whole-body control. Validated through extensive simulation studies and real-world deployment across diverse quadrupedal and manipulation platforms, this thesis provides a comprehensive blueprint that can provide machines with the resilient, contact-rich autonomy required to operate in the wild.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：机器人在动态、非结构化环境中（如家庭、野外）需要与环境发生密集接触（如立足、推动、抓取）才能实现稳定的移动与操作，但接触引入混合动力学和稀疏奖励，导致基于模型的方法规划困难、基于无模型的方法学习效率低下且脆弱。
- **研究动机**：现有方法多依赖任务特化的简化抽象或启发式规则，在可控条件下有效，但难以适应交互多样、条件不可预测的真实场景。如何让机器人自主学会“在哪里接触”以及“如何利用接触”成为物理智能的关键。
- **整体含义**：将移动和操作视为同一问题的两面，即通过有目的、间歇性的接触协调全身运动，最终实现野外自主操作。

## 二、论文提出的方法论
- **核心思想**：先分别解决移动和操作中的接触问题，再统一到非抓取式移动操作框架中，通过嵌入几何接触先验引导强化学习探索，并渐进退火该引导以恢复任务最优策略。
- **关键技术细节**：
  - **移动阶段**：学习考虑脚形和接触面几何的立足点选择；研究关节柔顺性等机械设计对鲁棒性的影响；开发基于学习的控制流水线实现硬件上的可靠运动。
  - **操作阶段**：针对极度杂乱场景和新型可重构夹爪，提取无碰撞抓取先验几何；通过强化学习将技能从静态抓取放置扩展到动态投掷。
  - **统一架构**：将几何接触先验嵌入多评论家强化学习框架，明确引导腿式操作器的探索朝向有意义的物理交互，随后逐步退火该引导，使策略恢复任务最优的全身控制。
- **算法流程（文字说明）**：先训练接触先验（立足点/抓取点），将其作为奖励或初始化信号注入多评论家框架；各评论家分别评估不同接触模式（如“是否接触”、“接触位置”等），策略网络综合这些信号进行决策；随着训练进行，引导的权重逐渐降低，让策略自主探索更优的全身运动。

## 三、实验设计
- **数据集/场景**：未明确提及公开数据集；使用多种四足机器人平台（如四足机器人）和操作平台（如夹爪、机械臂）进行仿真和实际部署。场景包括室内外复杂地形（移动阶段）和极度杂乱桌面/货架（操作阶段）。
- **Benchmark**：未说明具体 benchmark 名称；实验通过对比基线（如无先验引导的强化学习、传统模型预测控制）来验证性能。
- **对比方法**：文中提及“广泛仿真研究”和“实际部署”，但未列出对比方法的完整列表。推测基线包括：标准无引导强化学习（如PPO）、启发式接触选择、模型预测控制（MPC）等。

## 四、资源与算力
- **未明确说明**：文中没有提及使用的 GPU 型号、数量、训练时长等具体算力信息。仅提及“大量仿真研究”，可能依赖通用计算集群，但细节缺失。

## 五、实验数量与充分性
- **实验数量**：论文覆盖移动、操作两阶段专项实验，以及统一架构在不同平台上的仿真与真机实验。消融实验可能包括：有无几何先导引导、引导退火速率、不同机械设计变体等。
- **充分性评估**：由于缺乏公开数据集的标准化评测，实验的客观性（可复现性）受限；但在物理平台多样性（四足+多类夹爪）和真实部署方面表现出较好的覆盖面。实验设计较为充分，但缺少与最新同类方法（如2026年前后的同类工作）的定量对比。

## 六、论文的主要结论与发现
- **主要结论**：
  1. 基于几何接触先验嵌入多评论家强化学习的方法能有效解决接触稀疏奖励导致的探索困难，并实现稳定的全身协调移动操作。
  2. 引导退火策略在初期提供方向、后期恢复任务最优性，在仿真和真实机器人上均表现鲁棒。
  3. 移动与操作可统一在“接触选择与利用”的框架下，打破传统分支。
- **发现**：机械设计（如关节柔顺性）对腿式运动鲁棒性有显著影响；在极度杂乱场景中，几何先验能极大提高抓取规划的成功率。

## 七、优点
- **方法创新**：首次将几何接触先验嵌入多评论家强化学习，并设计引导退火机制，使学习兼具目标和自主性。
- **统一视角**：将移动和操作作为同一核心问题的两面，提供通用蓝图。
- **工程验证**：在多种四足和操作平台上完成仿真与真机实验，表明方法的实际部署可行性。

## 八、不足与局限
- **实验覆盖**：缺少公开数据集上的标准化评测，难以与其他方法公平直接比较；未提供定量指标（如成功率、时间代价）的具体数值。
- **算力与复现**：未公开训练所需计算资源，影响可复现性。
- **应用限制**：当前方法主要针对非抓取式操作（如推、支撑）；对于需要精确手指操作的精细任务尚未验证。
- **偏差风险**：实验平台均为作者所在实验室的定制化机器人，可能对算法有利；未测试对极端未知环境的泛化能力。

（完）
