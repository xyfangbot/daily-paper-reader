---
title: Learning-Based Hybrid Locomotion Control for a Heavy Wheeled-Legged Robot in Challenging Terrains
title_zh: 面向挑战性地形的重型轮腿机器人基于学习的混合运动控制
authors: "Jinmian Hou, Kang Wang, Hui Chai, Wei Xu, Yuxia Li, Rui Song, T Liu, Guoteng Zhang"
date: 2026-07-01
pdf: "https://doi.org/10.1007/s10846-026-02423-8"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:beijing academy of artificial intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=beijing academy of artificial intelligence; relation_source=affiliation; institutions=Shandong University, Ministry of Education; query=robot"
tldr: 轮腿机器人兼具轮式效率和腿式适应性，但现有研究多基于轻量平台。本文针对重达340kg以上的重型轮腿机器人，首次成功部署强化学习控制器，提出包含启发式奖励结构和特权学习状态估计器的端到端框架。仿真验证了精确速度跟踪、抗扰鲁棒性及慢响应下的优雅退化，实地实验在戈壁、砾石、草地、湿地等挑战地形达到3.80m/s速度。工作为重型机器人在真实约束下部署RL建立了基准。
source: openalex
selection_source: hot_paper_scout
motivation: 现有轮腿机器人研究多限于轻量平台，缺乏针对重型系统（超340kg）的RL控制方法，急需验证其鲁棒性与地形适应性。
method: 提出端到端RL控制框架，设计启发式奖励结构，并通过特权学习训练状态估计器，实现混合运动控制。
result: 仿真中速度跟踪准确、抗扰动强；实地实验在戈壁、砾石、草地等挑战地形达到3.80m/s，验证了鲁棒性与可部署性。
conclusion: 首次在重型轮腿机器人上成功部署RL控制器，为重型机器人系统在真实约束下应用强化学习提供了基准与可行方案。
---

## 摘要
摘要 轮腿机器人因其结合轮子效率与腿部适应性的潜力而受到关注。然而，大多数先前研究集中于轻量级平台。本文首次成功在重量超过340公斤的重型轮腿机器人上部署强化学习控制器，据我们所知，这是文献中报告的最大、最重的轮腿机器人之一，展示了基于学习的混合运动控制。我们提出了一种鲁棒的端到端控制框架，结合启发式奖励结构和通过特权学习训练的状态估计器。仿真实验展示了准确的速度跟踪性能、对外部干扰的强鲁棒性以及在慢响应执行下的优雅性能退化。现场实验包括在戈壁沙漠、砾石地、草地和湿地的高原试验，进一步证明了策略的鲁棒性、地形适应性以及现实世界的可部署性，在户外测试中达到了3.80米/秒的最高测量速度。这些仿真和现场结果为在真实世界约束下将强化学习部署到重型机器人系统建立了基准。

## Abstract
Abstract Wheeled-legged robots have gained attention for their potential to combine the efficiency of wheels with the adaptability of legs. However, most prior research has focused on lightweight platforms. In this work, we present the first successful deployment of a reinforcement learning (RL) controller on a heavy wheeled-legged robot weighing over 340 kg, which, to the best of our knowledge, is one of the largest and heaviest wheeled-legged robots reported in the literature to demonstrate RL-based hybrid locomotion control. We propose a robust end-to-end control framework, incorporating a heuristic reward structure and a state estimator trained via privileged learning. Simulation experiments demonstrate accurate speed tracking performance, strong robustness to external disturbances, and graceful performance degradation under slow-response actuation. Field experiments, including plateau trials on gobi deserts, gravel, meadows, and wetlands, further demonstrate the policy’s robustness, terrain adaptability, and real-world deployability, with a maximum measured speed of 3.80 m/s achieved in outdoor tests. These simulation and field results establish a benchmark for deploying RL on heavy robotic systems under real-world constraints.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 轮腿机器人结合了轮式移动的效率与腿式步态的适应性，是移动机器人领域的热点方向，但现有研究绝大多数集中在轻量级平台（如几十公斤级）。
- 本文的核心问题：如何在超过340公斤的重型轮腿机器人上，首次成功部署基于强化学习的混合运动控制器，并验证其在真实挑战性地形下的鲁棒性与实用性。
- 研究意义：填补重型轮腿机器人强化学习控制的空白，为工业级、户外极端环境下的重型机器人自主移动提供可行的技术路线和基准参考。

## 二、论文提出的方法论
- 核心思想：设计一个端到端的强化学习控制框架，将状态估计、运动规划与底层控制联合学习，实现从感知到关节指令的直接映射。
- 关键技术创新：
  - 启发式奖励结构：专门针对重型机器人设计的奖励函数，鼓励平滑运动、能量效率和地形适应，避免剧烈冲击和失稳。
  - 特权学习（Privileged Learning）训练的状态估计器：在训练时利用机器人全局状态（如地面接触力、地形高度）作为“教师信号”，推理时仅依靠本体感知（关节位置、惯性测量单元、轮速等）实时估计状态。
  - 混合运动模式：同时输出轮式滚动与腿部踏步的协调指令，实现轮腿混合步态。
- 公式或算法流程（文字描述）：
  1. 在仿真环境中，使用教师-学生（teacher-student）范式：教师策略以完整状态观测输入训练；学生策略以受限观测（如缺失地形信息）模仿教师行为，同时学习隐式状态表征。
  2. 学生策略输出关节位置/速度目标，由底层PD控制器执行。
  3. 训练完成后，直接部署到实物机器人，无需调参。

## 三、实验设计
- 数据集/场景：
  - 仿真实验：在虚拟物理引擎中设置多种地形（随机高度场、斜坡、台阶、碎石）以及外部扰动（推力、拖拽）。
  - 实地实验：高原环境下的戈壁沙漠、砾石地、草地、湿地等四种典型挑战地形。
- Benchmark：未明确列出对比方法，主要通过与自身设定速度指令对比跟踪误差、与扰动注入对比恢复能力。
- 对比方法：未提及与其他基线方法（如模型预测控制、传统状态机）的定量对比，更多是自身消融与鲁棒性验证。

## 四、资源与算力
- 未明确说明：文中未提及使用的GPU型号、数量、训练时长等具体算力信息。可能为单机多卡或集群，但细节不可得。

## 五、实验数量与充分性
- 实验数量：
  - 仿真中包含速度跟踪、扰动鲁棒性、执行器延迟退化等多组定量测试。
  - 实地实验覆盖四种不同地形（戈壁、砾石、草地、湿地），并记录了最高3.80 m/s的实测速度。
- 充分性评估：
  - 仿真实验较为充分，测试了多个性能维度。
  - 实地实验地形多样但数量有限（仅四种），且未进行长时间连续运行测试或重复性测试。缺少与其他模型的对比实验，因此客观性有待增强。
  - 总体而言，实验设计重点在于验证可行性与鲁棒性，而非全面系统的消融或对比。

## 六、论文的主要结论与发现
- 首次在超过340公斤的重型轮腿机器人上成功部署端到端强化学习控制器，证明RL方案能够扩展至重型系统。
- 所提框架在仿真中实现了精确的速度跟踪、强大的抗扰能力，并在执行器响应慢的情况下仍能保持稳定（优雅退化）。
- 实地实验中，机器人在戈壁、砾石、草地、湿地等非结构化地形下稳定行走，最高速度3.80 m/s，验证了策略的强鲁棒性与真实部署可能性。
- 工作为重型轮腿机器人使用强化学习提供了一个实践基准，表明RL在工业级机器人上的应用可行。

## 七、优点
- 突破性规模：率先应用RL于340kg级重型轮腿机器人，远超此前主流轻量平台。
- 端到端简化：无需手工设计步态或状态机，通过启发式奖励实现自适应混合运动。
- 特权学习实用化：通过教师-学生框架解决真实世界中状态不完全观测问题，可移植性好。
- 实地验证充分：在真实高原极端地形（戈壁、湿地等）实测，证据可信度高。

## 八、不足与局限
- 对比基线缺失：未与模型预测控制、传统基于优化的方法进行定量比较，难以量化RL带来的具体增益。
- 算力资源未公开：不利于其他团队复现或评估计算成本。
- 实验覆盖有限：实地地形仅四种，且未测试极端恶劣天气（雨雪、泥泞）、连续爬坡或越障等高难度任务。
- 部署偏差风险：仿真与实物的随机性差异（sim-to-real gap）未详细讨论，只以一次性实测结果说明鲁棒性，缺乏重复性统计。
- 应用限制：机身超340kg，灵活性有限；未提及电池续航与持续运行时间，实用性评估不足。
- 伦理声明：仅提及“无竞争利益”，但未讨论大型机器人可能的安全风险与监管问题。

（完）
