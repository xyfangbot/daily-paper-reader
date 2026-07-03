---
title: "MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse Footholds"
title_zh: MARCH：基于模型辅助强化学习的人形机器人稀疏立足点感知控制
authors: "Codrin Crismariu, Ryan K. Cosner"
date: 2026-06-09
pdf: "https://arxiv.org/pdf/2606.10288"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; institutions=Tufts University; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 双足机器人在稀疏立足点地形上行走面临挑战：基于模型的方法精确但易受不确定性影响，无模型方法鲁棒但难以发现安全约束运动。本文提出MARCH模型辅助强化学习框架，分三步：用简化模型生成安全参考轨迹，基于控制Lyapunov函数(CLF)奖励训练特权教师策略，再蒸馏为视觉学生策略。该方法提升样本效率，减少对复杂学习课程的需求，实现更平滑的行走行为，在稀疏立足点性能与无模型基线相当。在Unitree G1人形机器人上成功部署，验证了横向约束下的稀疏立足点导航，为感知双足控制提供了有效结合模型与RL优势的解决方案。
source: openalex
selection_source: hot_paper_scout
motivation: 模型方法精确但脆弱，无模型方法鲁棒但难以学习精确约束运动，需要结合二者实现稀疏立足点上的安全行走。
method: 先利用简化模型生成安全参考轨迹，再基于CLF奖励训练特权教师策略，最后蒸馏为仅用视觉输入的学生策略。
result: 该方法提升样本效率，简化学习课程，行走更平滑，稀疏立足点性能与无模型基线相当，并在Unitree G1机器人上成功部署。
conclusion: 提出MARCH模型辅助RL框架，有效结合模型精确性与RL鲁棒性，实现了人形机器人在稀疏立足点上的安全感知行走。
---

## 摘要
在稀疏地形上的感知双足运动仍然是一个困难的挑战：基于模型的方法精确但对不确定性脆弱，而无模型方法鲁棒但难以发现安全关键运动所需的精确、受约束的动作——其中微小误差可能导致灾难性失败。我们提出了一种模型辅助强化学习（RL）框架，通过三个步骤结合两种视角：（1）使用简化模型生成安全参考轨迹；（2）在安全参考轨迹基础上，通过控制李雅普诺夫函数（CLF）奖励训练特权教师策略；（3）将教师策略蒸馏为基于视觉的学生策略。我们表明，这种模型辅助过程产生了物理合理的运动，提高了样本效率，减少了对复杂学习课程的需求，并在达到与无模型基线相当的踏脚石性能的同时，实现了更平滑的运动行为。我们在仿真中验证了该方法，并展示了在宇树G1人形机器人上成功部署，该机器人在带有侧向约束的稀疏立足点上导航。

## Abstract
Perceptive bipedal locomotion over sparse terrain remains a difficult challenge: model-based methods are precise but brittle to uncertainty, while model-free methods are robust but struggle to discover the precise, constrained motions required for safety-critical locomotion where small errors can cause catastrophic failures. We propose a model-assisted reinforcement learning (RL) framework that combines both perspectives in three steps: (1) generate a safe reference trajectory using simplified models; (2) train a privileged teacher policy guided by a control Lyapunov function (CLF) reward built around the safe reference trajectory; and (3) distill the teacher into a vision-based student policy. We show that this model-assistance procedure produces physically grounded locomotion, improving sample efficiency, reducing the need for a complex learning curriculum, and achieving smoother locomotion behavior alongside stepping stone performance comparable to model-free baselines. We validate our approach in simulation and demonstrate successful deployment on a Unitree G1 humanoid robot navigating sparse footholds with lateral constraints.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：双足机器人在稀疏立足点（如踏脚石）上的安全感知运动。该场景对落足点有严格的前向和侧向约束，微小的落足误差可能导致灾难性失败。
- **研究动机**：现有方法存在明显割裂——基于模型的方法（如MPC、CLF）精确但依赖精确已知模型和环境地图，对不确定性脆弱；无模型强化学习方法鲁棒但难以发现安全关键场景所需的精确约束运动，且训练需要复杂课程和大量采样。
- **本文目标**：提出一种模型辅助强化学习（MARCH）框架，将模型方法的精确性与无模型方法的鲁棒性有机结合，实现视觉引导下在人形机器人上穿过稀疏、带侧向约束的踏脚石地形，并提升样本效率和运动平滑性。

## 二、论文提出的方法论

- **核心思想**：三步流程，如图2所示：
  1. **模型生成安全参考轨迹**：利用简化的离散时间单积分器（规划落足点序列）和混合线性倒立摆（HLIP）模型（生成质心运动参考），构建包含脚位置、质心、骨盆/脚姿态、上半身关节的目标轨迹。
  2. **训练特权教师策略**：在仿真中，教师策略（MLP）有权访问参考轨迹和完整状态信息。引入控制李雅普诺夫函数（CLF）灵感奖励：\( r_{\text{clf}} = \exp(-\min(V(\eta), V_{\text{max}})/V_{\text{max}}) \) 和 \( r_{\text{dclf}} = -\max(\dot{V}(\eta,a)+\alpha V(\eta),0)/V_{\text{dmax}} \)，其中 \(V(\eta)=\frac12\eta^T P\eta\)，\(\eta\)为仿真与参考的误差。该奖励促使策略跟踪参考轨迹，同时保留RL的探索能力。使用PPO优化。
  3. **蒸馏为学生策略**：学生策略（CNN提取深度图像特征 + Transformer融合历史 proprioception + MDN输出双峰动作分布）仅依靠体装深度相机和5步历史关节数据。通过最小化负对数似然蒸馏损失，学习教师动作分布，不依赖参考轨迹和真值地图。
- **关键技术细节**：
  - 规划器采用随机采样（N=4步，16次贪婪 rollout）近似求解非凸优化问题。
  - HLIP模型用于预-后碰撞质心状态预测，产生连续质心参考。
  - 教师策略训练包含领域随机化（质量、摩擦、延迟、推扰等），见表2。
  - MDN输出两个高斯模式，使策略能在不同落脚选择间切换。

## 三、实验设计

- **仿真环境**：基于 mjlab 框架和 MuJoCo 物理引擎，使用 Unitree G1 人形机器人模型。地形由两个平台和中间一系列随机尺寸/间隙/高度的踏脚石组成，包含并排石墩以考验左右脚选择。
- **基准对比**：无模型 PPO 基线（类似 [6] 方法），采用相同的教师-学生蒸馏框架，但不含 CLF 奖励。由于 [6] 未开源，作者自行复现并比较。
- **实验类型**：
  - **消融实验**（图3）：学生策略中分别移除 Transformer（换为MLP）和 MDN（换为确定性回归），比较1000个蒸馏 episode 后的总奖励。证实 Transformer 和 MDN 均显著提升学生性能。
  - **基线对比**（图4）：模型辅助方法与无模型方法比较三个指标：平均行走距离（两者最终相近）、平均关节力矩（模型辅助低至少12%）、平均角加速度/急动度（低至少39%）。评估基于2048次 rollout。
  - **硬件实验**：在 Unitree G1 真实机器人上，使用4个摆放成左右交替图案的踏脚石。学生策略50Hz运行。展示成功穿越的视频记录。

## 四、资源与算力

- **硬件**：单一 NVIDIA RTX 5090 GPU。
- **并行环境**：4096个并行仿真环境。
- **总训练时间**：约24小时，包含教师策略训练（10000个episode）和学生蒸馏（1500个迭代）。
- **计算库**：使用 GPU 加速的 rsl-rl 库。

## 五、实验数量与充分性

- **仿真实验**：
  - 消融实验：3种学生架构（完整、无Transformer、无MDN），各1500个蒸馏迭代，每100次评估一次奖励，曲线展示了趋势。
  - 基线对比：模型辅助教师训练10000 episode，无模型训练20000 episode。蒸馏阶段每500迭代统计力矩和急动度，使用4倍标准误差，样本量2048次 rollout。
- **硬件实验**：单次演示（视频记录），未报告重复次数或成功率统计。
- **充分性评价**：仿真消融和基线对比设计合理，样本量充足，统计误差合理。但硬件实验缺乏定量重复性评估（作者在局限中也承认），且缺乏与其他最新方法（如 [6]）的直接复现性能数据对比（仅引用其 preprint，无法直接跑分）。

## 六、论文的主要结论与发现

1. **模型辅助 RL 框架（MARCH）** 能够有效结合模型精确性和无模型鲁棒性，实现人形机器人在稀疏、带侧向约束的踏脚石地形上的感知行走。
2. **显著提升样本效率**：教师策略仅需约10000 episode 即可达到与无模型20000 episode 相当的行走距离。
3. **产生更平滑运动**：最终策略的关节力矩降低至少12%，角加速度/急动度降低至少39%，运动更加流畅。
4. **成功迁移到真实硬件**：在宇树 G1 机器人上验证了视觉策略的执行能力。

## 七、优点

- **方法设计创新**：将 CLF 奖励引入稀疏横向约束场景，与 Transformer + MDN 流结合，提升了策略对多步安全和多模态（左右脚选择）的处理能力。
- **实验验证全面**：包含仿真消融、基线对比和硬件部署，且展示了平滑性、力矩等多维度指标，不局限于任务成功率。
- **实用性强**：整个框架在单个消费级 GPU 上24小时内完成训练，成本可控；蒸馏为学生策略后仅需深度相机和 proprioception，易于硬件部署。
- **开源精神**：提供视频演示链接，附录详细给出所有超参数和领域随机化范围，便于复现。

## 八、不足与局限

- **传感器视野限制**：相机朝前下方，无法学习倒退或侧向行走，且视野有限妨碍长 horizon（>4步）机动规划。作者建议未来主动调整相机方向。
- **模型假设限制**：HLIP 模型不含飞行阶段，导致参考轨迹无法包含跳跃动作，限制了动态能力。
- **训练时间相近**：虽然样本效率提高（所需 episode 数减少），但每个 episode 因模型计算开销，总训练时间与无模型方法相当。
- **硬件实验重复性不足**：只展示了单次成功案例，未报告成功率或统计结果，作者归因于相机延迟与精度，期望在未来提升鲁棒性。
- **缺乏与其他顶级模型辅助方法（如 Walk the Planc [8]）的直接比较**：论文只与无模型基线对比，未与同样使用 CLF-RL 的前向约束工作 [8] 比较性能差异。
- **仿真与真实差距**：虽然使用领域随机化，但硬件实验仍存在 repeatability 问题，sim-to-real 转移的鲁棒性需进一步验证。

（完）
