---
title: "MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse Footholds"
title_zh: MARCH：面向稀疏落脚点的人形机器人感知控制的模型辅助强化学习
authors: "Codrin Crismariu, Ryan K. Cosner"
date: 2026-06-09
pdf: "https://arxiv.org/pdf/2606.10288"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; institutions=Tufts University; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 感知双足机器人在稀疏踏脚石上行走时，基于模型的方法虽精确但易受不确定性干扰，而无模型方法鲁棒却难以学习精确约束运动。作者提出模型辅助强化学习框架，通过简化模型生成安全参考轨迹，结合控制李雅普诺夫函数奖励训练特权教师策略，再蒸馏出基于视觉的学生策略。该方法显著提升样本效率，避免复杂课程学习，产生更平滑的运动行为，且踏脚石性能与无模型基线相当。最终在仿真和Unitree G1人形机器人上成功验证，展现了应对横向约束稀疏地形的能力。
source: openalex
selection_source: hot_paper_scout
motivation: 现有方法难以兼顾稀疏地形行走的精确性与鲁棒性，模型方法脆弱，无模型方法难以发现精确约束运动。
method: 三步框架：简化模型生成安全轨迹；基于控制李雅普诺夫函数奖励训练教师策略；知识蒸馏为视觉学生策略。
result: 提升样本效率，无需复杂课程，运动更平滑，踏脚石性能媲美无模型基线，仿真与真实机器人部署成功。
conclusion: 模型辅助强化学习有效融合模型精确性与RL鲁棒性，实现人形机器人稀疏踏脚石的感知控制。
---

## 摘要
在稀疏地形上的感知双足运动仍然是一项艰巨的挑战：基于模型的方法精确但对不确定性脆弱，而无模型方法鲁棒但难以发现安全关键运动所需的精确、受约束的运动，因为微小错误可能导致灾难性失败。我们提出了一种模型辅助强化学习框架，通过三个步骤结合了这两种视角：(1) 使用简化模型生成安全参考轨迹；(2) 训练一个特权教师策略，该策略由基于安全参考轨迹构建的控制李雅普诺夫函数（CLF）奖励引导；(3) 将教师策略蒸馏到基于视觉的学生策略中。我们展示了这种模型辅助过程能产生物理合理的运动，提高了样本效率，减少了对复杂学习课程的需求，并在踏脚石性能上与无模型基线相当的同时实现了更平滑的运动行为。我们在仿真中验证了我们的方法，并展示了在具有侧向约束的稀疏落脚点导航的Unitree G1人形机器人上的成功部署。

## Abstract
Perceptive bipedal locomotion over sparse terrain remains a difficult challenge: model-based methods are precise but brittle to uncertainty, while model-free methods are robust but struggle to discover the precise, constrained motions required for safety-critical locomotion where small errors can cause catastrophic failures. We propose a model-assisted reinforcement learning (RL) framework that combines both perspectives in three steps: (1) generate a safe reference trajectory using simplified models; (2) train a privileged teacher policy guided by a control Lyapunov function (CLF) reward built around the safe reference trajectory; and (3) distill the teacher into a vision-based student policy. We show that this model-assistance procedure produces physically grounded locomotion, improving sample efficiency, reducing the need for a complex learning curriculum, and achieving smoother locomotion behavior alongside stepping stone performance comparable to model-free baselines. We validate our approach in simulation and demonstrate successful deployment on a Unitree G1 humanoid robot navigating sparse footholds with lateral constraints.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 感知双足机器人在稀疏地形（如踏脚石）上的行走是一个安全关键但极具挑战的任务。
- 现有方法分为两派：基于模型的方法精确但易受模型不确定性和感知噪声影响，难以直接部署到真实机器人；无模型（强化学习）方法鲁棒但难以自动发现安全关键运动所需的精确约束（如精确的脚部放置），通常需要复杂的课程学习和大量采样。
- 本文试图结合两者优势：利用简化模型提供的安全参考轨迹引导强化学习训练，同时保留RL的鲁棒性，最终实现视觉驱动的、能在横向约束稀疏落脚点行走的控制器。

## 二、论文提出的方法论
- **核心思想**：提出一个三步模型辅助强化学习框架（MARCH）：
  1. **参考轨迹生成**：使用离散时间单积分器模型规划安全落脚点序列（随机投射法求解短时域非凸优化），再结合混合线性倒立摆（HLIP）模型生成质心轨迹、摆动脚轨迹、骨盆/脚部朝向及上半身参考轨迹。
  2. **教师策略训练**：在仿真中训练一个特权教师策略（MLP架构），其奖励函数包含标准RL奖励和基于控制李雅普诺夫函数（CLF）设计的额外奖励项：
     - \( r_{clf} = \exp(-\min(V(\eta), V_{\max}) / V_{\max}) \) 鼓励跟踪误差小；
     - \( r_{dclf} = -\max(\frac{dV}{dt}(\eta,a) + \alpha V(\eta)}{V_{\max}^d}, 0) \) 鼓励误差收敛。
     其中 \( V(\eta)=\frac12 \eta^T P \eta \)，\(\eta\) 为真实状态与参考轨迹之差。教师策略通过PPO算法训练，拥有5步历史位姿数据和完整的参考轨迹作为输入。
  3. **学生蒸馏**：将教师策略蒸馏为仅依赖深度图像和本体感知的学生策略。学生架构包括：CNN提取深度图像特征、Transformer融合图像特征与历史位姿数据、最终由混合密度网络（MDN）输出双模态动作分布，使策略能够区分不同落脚模式（如左/右脚选择）。训练使用负对数似然蒸馏损失。

## 三、实验设计
- **仿真环境**：基于mjlab和MuJoCo，4,096个并行环境，随机生成两端平台连接序列踏脚石的地形，包含难度递增的课程（石块尺寸、间隙、高度变化、并排石块以产生横向选择）。
- **对比方法**：
  - 模型无关基线：与本文相同教师-学生框架但去掉CLF奖励（类似[6]方法）。
  - 消融实验：去掉Transformer（替换为MLP）或去掉MDN（替换为确定性输出）的学生变体。
- **硬件实验**：Unitree G1人形机器人，胸戴Intel Realsense D435i深度相机，4个踏脚石以伪随机左右交替排列，机器人运行在Jetson Orin Nx上，控制频率约50Hz。
- **评估指标**：平均行走距离、平均关节扭矩绝对值、平均角加速度绝对值（衡量平滑性）。

## 四、资源与算力
- **计算资源**：单张NVIDIA RTX 5090 GPU。
- **并行环境数**：4,096个并行仿真环境。
- **训练时间**：教师训练+学生蒸馏总共约24小时（教师训练10,000 episodes，学生蒸馏1,500 iterations）。

## 五、实验数量与充分性
- 仿真实验：完整对比模型-informed vs model-free（图4）展示了训练过程中的平均距离、扭矩、角加速度，基于2048次 rollout 的评估；消融实验（图3）对比三种学生架构，基于1000次 episode 的蒸馏训练。
- 硬件实验：一次成功部署演示（视频可见），但未提供多次重复试验的统计结果。
- 充分性评价：消融和基线对比设计合理，结果数据量较大（2048 rollouts），公平性较好。但硬件实验仅演示单次成功，缺乏对重复性和失败率的统计分析，实验充分性相对有限。

## 六、论文的主要结论与发现
- 模型辅助框架（CLF奖励）使得教师策略在10,000 episodes内收敛，而模型无关方法需要20,000 episodes，显著提升样本效率。
- 最终学生策略的行走距离与模型无关基线相当，但关节扭矩降低至少12%，角加速度降低至少39%，即运动更平滑。
- 消融实验表明：Transformer和MDN组件对学生性能均有正向贡献，去掉任一组件都会导致奖励下降。
- 硬件部署成功验证了该方法从仿真到真实的迁移能力。

## 七、优点
- **方法创新**：将CLF-RL奖励与教师-学生蒸馏结合，首次用于横向约束的稀疏落脚点场景，并用MDN处理多模态落脚选择。
- **样本效率高**：相比纯RL方法减少一半训练迭代，且无需手工设计的复杂课程。
- **运动平滑**：CLF奖励引导导致更低扭矩和角加速度，减少了震荡和冲击。
- **架构合理**：Transformer增强时序依赖建模，MDN允许策略在不同落脚模式间选择，提升泛化性。
- **硬件演示**：在真实人形机器人上成功实现视觉感知的稀疏踏脚石行走，验证了实用性。

## 八、不足与局限
- **感知局限性**：相机固定前下方，无法支持向后或侧向行走，且视野有限，难以进行长时域（>4步）的主动规划。
- **模型限制**：HLIP模型不包含腾空阶段，因此参考轨迹不能产生跳跃行为。
- **计算效率**：虽然采样效率提升，但总体训练时间（24小时）与模型无关方法相近，主要原因可能是MDN和Transformer的额外计算开销。
- **硬件可靠性**：硬件实验重复性不如仿真，作者归因于相机延迟与精度问题，说明现有鲁棒性仍不充分。
- **实验覆盖**：仅测试了一种地形（固定高度的踏脚石），未涉及更大高度差、斜面、障碍物等更复杂场景；硬件实验只演示一次成功，缺乏统计显著性的定量评估。

（完）
