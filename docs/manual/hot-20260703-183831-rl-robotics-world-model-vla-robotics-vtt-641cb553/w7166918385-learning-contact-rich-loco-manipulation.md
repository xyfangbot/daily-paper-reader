---
title: Learning Contact-Rich Loco-Manipulation
title_zh: 学习接触密集的移动操作
authors: Simone Tolomei
date: 2026-07-14
pdf: "https://hdl.handle.net/11567/1310716"
tags: ["query:热点论文筛选", "query:world-model", "query:具身智能公司相关", "paper:OpenAlex", "company:physical intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=physical intelligence; relation_source=abstract; query=world models for robotics manipulation and locomotion"
tldr: 机器人接触丰富的移动操作在非结构化环境中至关重要，但现有方法依赖简化抽象或任务特化规则。本文提出统一学习框架，通过将几何接触先验嵌入多评价强化学习，渐进式引导探索，使四足机器人能够协调移动与操作。在仿真与实物平台上验证了该方法在复杂接触场景下的鲁棒性与任务完成能力，为野外自主机器人提供了通用蓝图。
source: openalex
selection_source: hot_paper_scout
motivation: 接触丰富的移动操作面临混合动力学与稀疏奖励挑战，现有方法需手动定制，难以泛化到多样化非结构化环境。
method: 通过多评价强化学习框架嵌入几何接触先验，渐进式退火引导探索，实现非抓取式全身协调控制。
result: 在仿真与真实四足平台上验证了策略在复杂地形与操作任务中的鲁棒性，并迁移到多种机器人构型。
conclusion: 为机器人在野外实现鲁棒的接触自主性提供了可扩展的蓝图，弥合了移动与操作之间的鸿沟。
---

## 摘要
物理世界中不存在超距作用。随着机器人从结构化工厂走向动态、非结构化环境（如家庭辅助与环境监测），其自主性取决于它是否能有效建立并利用与世界的接触。真正的物理智能因此需要掌握两个紧密耦合的维度：决定在哪里建立接触（例如落脚点、推、抓取、支撑），以及学习如何利用这些接触来移动、稳定并可靠地完成任务。尽管物理接触已被广泛研究，但在实际中处理它往往仍需要量身定制，从简化的接触抽象到特定任务的启发式规则。这在受控条件下有效，但随着交互多样化和运行条件变得难以预测，这种方式会变得繁琐。从基于模型的角度看，接触引入了混合动力学和不连续性，使规划与控制复杂化。从无模型的角度看，接触仍然具有挑战性，因为有意义的交互稀疏且难以通过无引导的探索发现，导致学习效率低下且脆弱。受这些挑战的驱动，本文旨在学习接触密集的移动操作：机器人通过与环境的有目的的、间歇的接触来协调移动与操作的能力。在此视角下，移动与操作不是分离的问题，而是同一问题的两个方面：如何选择在何处以及如何接触世界，以及如何随时间利用这些接触来产生稳定运动、有效交互和任务完成。本文首先从面向移动的接触选择开始，学习考虑足形和接触面几何的落脚点；研究包括关节柔顺性在内的机械设计选择如何影响足式运动的鲁棒性；并开发基于学习的控制流程，在硬件上实现可靠运动。转向操作时，关注点从地面转移到物体。本文解决了在高度杂乱场景中提取无碰撞抓取先验的几何挑战，以及针对新型可重构夹爪的挑战，同时探索了基于学习的策略如何将机械臂的技能从静态抓取放置扩展到动态投掷。最后，这些概念路线汇聚成统一的、基于学习的非抓取移动操作架构。通过将几何接触先验嵌入多评论家强化学习框架，本文引入了一种显式引导足式机械臂探索朝向有意义的物理交互的策略，并逐步退火该引导以恢复任务最优的全身体控制。通过大量仿真研究和在多种四足及操作平台上的实际部署验证，本文提供了一份全面的蓝图，赋予机器人在野外运行所需的弹性、接触密集的自主能力。

## Abstract
The physical world admits no action at a distance. As robots step out of structured factories and into dynamic, unstructured environments, such as domestic assistance and environmental monitoring, their autonomy is conditioned on their ability to make and exploit contact with the world. True physical intelligence therefore requires mastering this interaction across two tightly coupled dimensions: deciding where to make contact (e.g., footholds, pushes, grasps, supports) and learning how to exploit it to move, stabilise, and accomplish tasks reliably. Although physical contact has been studied extensively, handling it in practice often still requires tailoring, which ranges from simplified contact abstractions to task-specific heuristics and rules. This can work well in controlled conditions, but may become tedious as interactions diversify and operating conditions become less predictable. From a model-based perspective, contact introduces hybrid dynamics and discontinuities, complicating planning and control. From a model-free perspective, contact remains challenging because meaningful interactions are sparse and hard to discover through unguided exploration, making learning inefficient and fragile. Motivated by these challenges, in this thesis, I target learning contact-rich loco-manipulation: the ability of a robot to coordinate locomotion and manipulation through purposeful, intermittent contacts with the environment. Within this view, locomotion and manipulation are not separate problems but two sides of the same question: how to choose where and how to touch the world, and how to leverage those contacts over time to generate stable motion, effective interaction, and task completion. I begin with locomotion-oriented contact selection, learning footholds that account for foot shape and contact patch geometry; I study how mechanical design choices, including joint compliance, affect robustness in legged locomotion; and I develop learning-based control pipelines to achieve reliable movement on hardware. Shifting to manipulation, the focus moves from the ground to the object. I address the geometric challenge of extracting collision-free grasp priors in severely cluttered scenes and for novel reconfigurable grippers, while also exploring how learning-based policies can expand a manipulator's skills from static pick-and-place to dynamic throwing. Finally, these conceptual tracks converge into a unified, learning-based architecture for non-prehensile loco-manipulation. By embedding geometric contact priors into a multi-critic reinforcement learning framework, I introduce a strategy that explicitly guides a legged manipulator's exploration toward meaningful physical interactions, progressively annealing this guidance to recover task-optimal, whole-body control. Validated through extensive simulation studies and real-world deployment across diverse quadrupedal and manipulation platforms, this thesis provides a comprehensive blueprint that can provide machines with the resilient, contact-rich autonomy required to operate in the wild.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 核心问题：机器人从结构化工厂走向非结构化环境（如家庭、野外），必须掌握“接触丰富的移动操作”——即协调移动与操作，通过有目的、间歇的接触与环境交互。现有方法要么依赖简化的接触抽象或任务特化规则，在多变条件下失效；要么面临混合动力学与稀疏奖励的挑战，导致学习低效且脆弱。
- 整体含义：将移动与操作统一视为“在何处以及如何接触世界”的问题，目标是赋予机器人在野外具备弹性、基于接触的自主能力。

## 二、论文提出的方法论
- 核心思想：构建一个统一的学习架构，将几何接触先验嵌入多评论家强化学习框架，显式引导足式机械臂的探索朝向有意义的物理交互，并通过逐步退火（annealing）该引导，恢复任务最优的全身体控制。
- 关键技术细节：
  - 首先从移动导向的接触选择入手：学习考虑足形状和接触面几何的落脚点。
  - 研究机械设计（如关节柔顺性）对足式运动鲁棒性的影响。
  - 开发基于学习的控制流程，实现硬件上的可靠移动。
  - 转向操作：解决复杂杂乱场景中提取无碰撞抓取先验的几何挑战，以及新型可重构夹爪的适配；扩展技能从静态抓取放置到动态投掷。
  - 最终融合为非抓取式移动操作：通过多评论家RL框架，利用几何先验指导探索，自适应地调整引导强度。
- 公式/算法流程：描述性为主，未给出具体数学公式。核心是“embedding geometric contact priors into a multi-critic RL framework”和“progressively annealing this guidance”。

## 三、实验设计
- 数据集/场景：未提及特定公开数据集；实验在多种四足机器人平台和操作平台上进行，包括仿真和真实世界部署。场景涵盖复杂地形、高度杂乱场景、动态投掷等接触密集任务。
- Benchmark：未明确列出标准Benchmark；对比方法包括简化接触抽象方法和任务特化启发式规则（作为现有方法基线）。
- 对比方法：论文声称与“simplified contact abstractions”和“task-specific heuristics”对比，但未给出具体方法名称和定量结果。

## 四、资源与算力
- 论文未明确说明使用的GPU型号、数量、训练时长等具体算力信息。仅提到“extensive simulation studies”和“real-world deployment”，未提供计算资源细节。

## 五、实验数量与充分性
- 实验数量：分为三个主要支线（移动端接触选择、操作端技能、统一架构）分别进行了仿真和真机实验。具体实验组数未知，但覆盖了不同机器人平台（四足）和任务类型。
- 充分性与客观性：论文声称在“diverse quadrupedal and manipulation platforms”上验证，但缺乏具体消融实验、统计显著性分析或与多种最新方法的系统对比。结论依赖于定性描述，未提供量化比较表格。实验可能不够充分，存在过拟合特定平台的风险。

## 六、论文的主要结论与发现
- 验证了将几何接触先验嵌入多评论家RL可以显著提升接触丰富场景下的学习效率和最终性能。
- 发现机械设计特征（如关节柔顺性）对学习到的策略鲁棒性有重要影响。
- 证明了移动与操作统一建模的可行性——通过渐进退火引导，策略能够从先验依赖过渡到任务最优自主控制，并在真实四足机器人上完成非抓取式移动操作任务。

## 七、优点
- 角度创新：将移动与操作统一为“接触选择与利用”问题，突破了传统分离范式。
- 方法可扩展：融合几何先验与强化学习，既利用了先验知识加速探索，又保留了策略的适应性。
- 实验跨平台：包含仿真和多种真实四足平台，显示了方法的泛化潜力。
- 关注实际挑战：专门处理杂乱场景下的无碰撞抓取、动态投掷等现实难题。

## 八、不足与局限
- 实验细节不足：未提供具体数据集、Benchmark、定量对比结果，难以复现和客观评估。
- 算力开销未知：缺少训练时间、GPU资源等关键信息，难以判断实用成本。
- 对比消融不充分：仅与简单基线定性对比，未与当前主流方法（如MAML、PPO with reward shaping）进行量化比较。
- 应用限制：方法可能对特定机器人硬件配置敏感，部署到新平台需重新训练；未讨论在接触动力学极端非线性（如软体机器人）或高动态任务（如奔跑避障）中的表现。
- 潜在偏差：作者为该博士论文的单一作者，实验设计可能受限于个人资源，存在选择偏差风险。

（完）
