---
title: Learning-Based Hybrid Locomotion Control for a Heavy Wheeled-Legged Robot in Challenging Terrains
title_zh: 基于学习的大型轮腿机器人在复杂地形中的混合运动控制
authors: "Jinmian Hou, Kang Wang, Hui Chai, Wei Xu, Yuxia Li, Rui Song, T Liu, Guoteng Zhang"
date: 2026-07-01
pdf: "https://doi.org/10.1007/s10846-026-02423-8"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:beijing academy of artificial intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=beijing academy of artificial intelligence; relation_source=affiliation; institutions=Shandong University, Ministry of Education; query=robot"
tldr: 重型轮腿机器人兼具轮式高效和腿式适应性的潜力，但此前研究多限于轻量平台。本文在重达340kg以上（已知最大之一）的轮腿机器人上首次实现强化学习混合运动控制，提出端到端框架，含启发式奖励结构和特权学习训练的状态估计器。仿真验证了精确速度跟踪、抗干扰能力及慢响应下的性能退化，实地试验（戈壁、碎石、草地、湿地）证明鲁棒性与地形适应性，室外最高速度达3.80m/s。该工作为在真实约束下将RL部署于重型机器人建立了基准。
source: openalex
selection_source: hot_paper_scout
motivation: "现有轮腿机器人控制技术多针对轻量平台，缺乏在重型（>340kg）机器人上应用强化学习的有效方法。"
method: 提出端到端强化学习控制器，结合启发式奖励函数与通过特权学习训练的状态估计器，实现鲁棒混合运动控制。
result: 仿真中速度跟踪精准、对外扰鲁棒，真实戈壁、碎石、草地、湿地等复杂地形测试最高速度3.80m/s，验证部署可行性。
conclusion: 首次在重型轮腿机器人上成功部署强化学习控制器，为重型系统在实际约束下的自主运动控制奠定了基准。
---

## 摘要
摘要 轮腿机器人因其结合轮子效率与腿部适应性的潜力而受到关注。然而，以往的研究主要集中在轻型平台上。在本工作中，我们首次成功将强化学习（RL）控制器部署于一台重量超过340公斤的大型轮腿机器人上，据我们所知，这是文献中报道的基于强化学习的混合运动控制中最大、最重的轮腿机器人之一。我们提出了一种鲁棒的端到端控制框架，结合了启发式奖励结构以及通过特权学习训练的状态估计器。仿真实验展示了精确的速度跟踪性能、对外部干扰的强大鲁棒性，以及在慢响应执行机构下的性能优雅退化。实地实验——包括在戈壁沙漠、砾石地、草地和湿地的高原测试——进一步验证了策略的鲁棒性、地形适应性以及在真实世界的可部署性，室外测试中最大测量速度达到3.80米/秒。这些仿真和实地结果为在真实世界约束下将强化学习部署于大型机器人系统建立了基准。

## Abstract
Abstract Wheeled-legged robots have gained attention for their potential to combine the efficiency of wheels with the adaptability of legs. However, most prior research has focused on lightweight platforms. In this work, we present the first successful deployment of a reinforcement learning (RL) controller on a heavy wheeled-legged robot weighing over 340 kg, which, to the best of our knowledge, is one of the largest and heaviest wheeled-legged robots reported in the literature to demonstrate RL-based hybrid locomotion control. We propose a robust end-to-end control framework, incorporating a heuristic reward structure and a state estimator trained via privileged learning. Simulation experiments demonstrate accurate speed tracking performance, strong robustness to external disturbances, and graceful performance degradation under slow-response actuation. Field experiments, including plateau trials on gobi deserts, gravel, meadows, and wetlands, further demonstrate the policy’s robustness, terrain adaptability, and real-world deployability, with a maximum measured speed of 3.80 m/s achieved in outdoor tests. These simulation and field results establish a benchmark for deploying RL on heavy robotic systems under real-world constraints.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 轮腿机器人结合了轮式的高效性与腿式的越障适应性，是移动机器人研究热点。
- 现有控制方法多针对轻型轮腿平台（数十公斤级），在重型机器人（>340 kg）上部署强化学习（RL）控制器仍属空白。
- 实际应用（如戈壁、湿地等复杂地形）对机器人的鲁棒性、地形适应性和实时控制提出更高要求。
- 本文首次在已知最大、最重的轮腿机器人之一（>340 kg）上成功实现基于RL的混合运动控制，旨在验证重型平台下RL控制器的可行性与性能。

## 二、论文提出的方法论
- **核心思想**：提出一个端到端的强化学习控制框架，直接由机器人状态输出关节/轮子动作，实现混合运动（轮式滚动+腿部行走/支撑）。
- **关键技术细节**：
  - **启发式奖励结构**：设计包含速度跟踪、能量效率、姿态稳定、足端触地惩罚等项的综合奖励函数，引导策略学习鲁棒行为。
  - **特权学习训练的状态估计器**：利用特权学习（Privileged Learning）方法，在仿真中通过完整状态信息训练一个学生网络，使其在部署时仅依靠本体感知（IMU、编码器等）估计基座速度、接触状态等关键量。
  - **控制策略网络**：采用PPO（Proximal Policy Optimization）算法，在物理仿真环境中训练，并通过域随机化增强对现实差异的鲁棒性。
- **流程**：仿真环境（包含地形、执行器延迟、噪声）→ 训练策略与状态估计器 → 零样本迁移到真实机器人。

## 三、实验设计
- **使用的数据集/场景**：
  - **仿真实验**：多种地形（平面、斜坡、障碍物），测试速度跟踪精度、对外部推/拉干扰的鲁棒性、以及执行器慢响应下的性能退化表现。
  - **实地实验**：高原实地环境，包括戈壁沙漠、砾石地、草地、湿地共4种典型复杂地形。
- **Benchmark**：未明确设置公开基准数据集或对比方法；论文定位为重型轮腿平台RL控制的首次成功部署，主要进行自身性能验证。
- **对比的方法**：未与其他RL或基于模型的方法进行定量对比；仅展示了所提框架在不同地形和干扰下的表现。

## 四、资源与算力
- 论文正文中未明确说明训练所使用的GPU型号、数量、训练时长或仿真平台细节。
- 仅能从研究机构（山东大学、中国北方车辆研究所等）推断可能使用常规计算资源，但具体数据缺失。

## 五、实验数量与充分性
- **实验数量**：
  - 仿真实验：未明确列出具体组数，但包含速度跟踪测试（多个速度指令）、抗干扰测试（外力扰动大小）、执行器延迟测试（不同延迟量）。
  - 实地实验：4种地形（戈壁、砾石、草地、湿地），每种地形进行多次测试，并记录最高速度3.80 m/s。
- **充分性评估**：
  - 覆盖了关键性能维度（速度精度、鲁棒性、适应性、极端条件退化的优雅性），实地地形多样，具有代表性。
  - 缺乏与传统方法（如MPC、WBC）的对比实验，说服力稍弱；未进行消融实验（如去掉特权学习或部分奖励项）以验证各组件贡献。
  - 实验数量总体合理，但受限于单次部署成本（重型机器人），属于典型“少实验、高成本”场景。

## 六、论文的主要结论与发现
- 首次在重型（>340 kg）轮腿机器人上成功部署RL控制器，实现稳定鲁棒的混合运动控制。
- 仿真验证了精确速度跟踪、强抗干扰能力以及执行器慢响应下的性能优雅退化。
- 实地实验中，机器人在戈壁、砾石、草地、湿地等未训练地形上均能有效运行，最高室外速度达3.80 m/s，证明了策略的泛化性和部署可行性。
- 该工作为RL在重型机器人系统投入实际应用建立了基准参考。

## 七、优点
- **重大应用突破**：填补了重型轮腿机器人RL控制的空白，机器人重量（>340 kg）为文献已知最大之一。
- **端到端框架简洁实用**：无需手动设计复杂的步态规划器，简化了控制流程。
- **特权学习状态估计器**：解决了重型机器人昂贵/不精确传感器问题，仅依靠低成本本体感知即可实现稳健估计。
- **实地验证充分**：在四种真实复杂地形上测试，且包含高原条件，结果具有较高可信度。
- **性能优雅退化**：考察了执行器慢响应这一现实问题，并展示了策略的graceful degradation，体现出工程考虑。

## 八、不足与局限
- **缺乏对比基线**：未与Model Predictive Control（MPC）、传统WBC或轻量平台RL方法在同等条件下对比，难以证明所提方法的相对优势。
- **资源与算力信息缺失**：没有提供训练成本（GPU、时间），不利于其他研究者复现或评估效率。
- **消融实验不足**：未分析各部分（奖励项、状态估计器、域随机化策略等）对整体性能的具体贡献，因果关系不够清晰。
- **实验数据不够详尽**：实地测试仅报告了最高速度，缺乏如成功次数、失败案例、地形统计等定量指标；未提供仿真与实地的量化一致性对比。
- **泛化性有限**：未测试更多非结构化地形（如泥泞、冰雪、陡坡），且未评估控制系统对不同负载或机械磨损的鲁棒性。
- **方法创新性一般**：采用PPO+特权学习的经典组合，在轻量机器人中已有先例，本文主要贡献在于重型平台的工程部署而非算法创新。

（完）
