---
title: Energy-Efficient Arm Reaching for a Humanoid Robot via Deep Reinforcement Learning with Identified Power Models
authors: "Nestor N. Deniz, Simon Parsons, Fernando Auat Cheein"
date: 2026-06-14
pdf: "https://arxiv.org/pdf/2606.15918"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: "人形机器人野外操作（如苹果采摘）受电池续航限制，需要高效手臂伸展。本文为Unitree G1左臂（7自由度）提出端到端能量感知强化学习框架，结合基于物理的电力模型和SAC策略，在Pinocchio模拟器中训练。模拟中成功率69.9%，平均能耗98.16J；在真实机器人上验证，平均能耗71.5±48.3J，位置误差2.64±1.04cm，姿态误差6.92±1.33°，在训练容忍度内。该工作是向人形机器人能量感知强化学习手臂伸展迈出的第一步。"
source: openalex
selection_source: hot_paper_scout
motivation: 人形机器人在电池供电下执行田间操纵任务（如苹果采摘）时，手臂伸展运动数量受能源严重限制，需降低能耗以延长单次充电可执行次数。
method: 结合实验辨识的电力模型与SAC算法，在Pinocchio模拟器中训练7自由度左臂，采用增量关节位置动作空间和混合星座奖励（四点头端距离+扭矩范数能量代理）。
result: "模拟中5×10^6步训练后，对1000个随机目标成功率达69.9%，成功回合均耗98.16J；物理机器人三批共30个目标平均能耗71.5±48.3J，位置误差2.64±1.04cm，姿态误差6.92±1.33°。"
conclusion: 该能量感知强化学习框架首次实现了人形机器人手臂伸展，验证了在真实机器人上的有效性和低能耗，为野外长期作业奠定基础。
---

## Abstract
Humanoid robots performing in-field manipulation tasks, such as robotic apple harvesting, face severe energy constraints that directly limit the number of reaching motions that can be executed per battery charge. This paper presents an end-to-end, energy-aware reinforcement learning framework for the 7-degree-of-freedom left arm of the Unitree~G1 humanoid robot, combining a physics-based, experimentally identified electrical power model with a Soft Actor-Critic (SAC) policy trained in a Pinocchio-based rigid-body dynamics simulator. The RL policy operates on an incremental joint-position action space and is trained with a Hybrid Constellation Reward that combines a four-point end-effector constellation distance with a torque-norm energy proxy; after % $5\times10^6$ training it reaches a $69.9\%$ success rate over $1\,000$ random targets in kinematic simulation, at a mean energy of \SI{98.16}{\joule} on successful episodes. Finally, on the physical Unitree~G1, the policy is validated over three independent 10-target batches, achieving a mean energy of $71.5 \pm 48.3$\,J, an end-effector position error of $2.64 \pm 1.04$\,cm, and an orientation error of $6.92 \pm 1.33^\circ$ -- within the \SI{4}{\centi\metre}/$8.6^\circ$ training tolerance. These results constitute a first step toward energy-aware reinforcement-learning-based arm reaching for humanoid robots.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 人形机器人在野外执行田间操作任务（如苹果采摘）时，受限于固定电池容量，需要执行数百次手臂伸展运动，能耗变量大，严重限制单次充电可完成的工作量。
- 传统运动规划方法（如最小关节力矩、MPC）依赖精确动力学模型，在线优化计算开销大；深度强化学习可在离线训练后以极低计算开销在线执行，但现有工作缺乏针对人形机器人手臂的端到端能量感知训练与真实机器人验证。
- 本文首次提出结合实验辨识电力模型的强化学习框架，目标是在保证任务成功率的前提下降低每次伸展的能耗，延长人形采摘平台的有效工作时间。

## 二、论文提出的方法论
- **核心思想**：将实验辨识的7自由度左臂电气功耗模型嵌入强化学习环境，使用SAC算法训练能量感知策略，并通过增量关节位置动作空间与混合星座奖励设计实现位置/姿态联合优化。
- **关键技术**：
  - **电力模型**（公式1）：将净功率分解为机械功率、铜损、库仑摩擦、粘滞摩擦和关节间耦合项，参数基于真实机器人数据辨识（R²=0.933），用作评估度量而非训练奖励。
  - **状态空间**（公式3）：包含归一化关节角度、速度、笛卡尔位置误差、姿态误差（旋转向量）和剩余时间分数。
  - **动作空间**（公式5-7）：增量关节位置目标，通过比例控制器生成期望速度并限幅，保证不超出最大速度。
  - **混合星座奖励**（公式14-20）：结合六项——星座距离下降奖励、残差位置惩罚、指数星座奖励、步长成本、速度平滑惩罚、扭矩范数能量代理、终端成功奖励。其中星座距离使用末端的四个虚拟点，同时敏感于位置与姿态误差，避免分别调权重。
  - **SAC算法**：最大熵强化学习，自动调节温度参数α_ent，促进在狭窄成功区域（4cm/8.6°）的探索。网络结构为[256,256] MLP。

## 三、实验设计
- **场景与数据集**：
  - 训练与评估在Pinocchio刚性体动力学仿真器中完成，目标位姿通过随机采样关节配置并前向运动学生成，排除距肩部过近点（<0.15m）。
  - 模拟评估：1,000个随机目标（n=1000）。
  - MuJoCo动力学验证：使用完整Unitree G1 MJCF模型（29自由度，浮动基座），对200个目标进行PD增益扫描（4组增益），另对受限任务包络进行20个目标测试。
  - 真实机器人验证：三批各10个目标（n=30），从受限可达工作空间（x≥0.1m，IK残差<2cm）采样。
- **基准方法**：关节空间最小急动度轨迹（Jerk-minimizing），已知目标关节配置，可视为“特权”能量高效参考。
- **对比内容**：RL策略 vs. 最小急动度基线在模拟中的成功率、能耗、误差等指标；不同PD增益下的MuJoCo成功率、饱和率、能耗对比；工作空间可达性分析（IK求解80个随机点）。

## 四、资源与算力
- 训练使用8个并行环境（SubprocVecEnv），在桌面级NVIDIA RTX系列GPU上运行，吞吐量约1,000-1,700步/秒。
- 总训练步数为5×10^6步，每5×10^5步保存一次检查点，使用EvalCallback选择最高平均奖励的检查点。
- 文中未明确GPU具体型号、训练时长（小时数）及电能消耗。

## 五、实验数量与充分性
- **实验数量**：
  - 模拟评估：n=1000，单一检查点（确定性策略）。
  - MuJoCo动力学验证：全工作空间n=200；PD扫描n=100（4组）；额外大样本验证n=200。
  - 受限包络MuJoCo筛选：n=20。
  - 真实机器人验证：n=30（三批独立试验）。
- **充分性与公平性**：
  - 模拟评估样本量足够，但仅使用单一seed和检查点，未报告多次训练统计。
  - 最小急动度基线具备关节空间先验知识（特权信息），RL仅知笛卡尔位姿，因此两者不可直接视为同等条件下的对比，而是“参考上限”。
  - 消融实验不足：未比较α>0（直接使用完整电力模型奖励）的情况，未进行域随机化或真实数据微调。
  - 真实机器人样本量较小（n=30），但也提供了每个试验的详细误差分布，足以证明可行性。
  - PD增益扫描系统量化了动态差距，工作空间可达性分析解释了主要失败原因，实验设计较为完整。

## 六、论文的主要结论与发现
- 训练后的SAC策略在模拟中达到69.9%成功率（n=1000），成功回合平均能耗98.16J，但最小急动度基线达100%成功率且能耗更低（21.95J），主要因RL缺乏关节空间先验。
- MuJoCo动力学验证显示，由于仿真训练假设“完美跟踪”，导致成功率下降约20-25个百分点，且姿态误差（11-13°）超过训练容忍度（8.6°），且与PD增益选择无关。
- 工作空间可达性分析表明：仅30%的随机采摘框内点可通过位置IK在2cm内达到，几何不可达是比动态跟踪更大的失败因素。
- 将评估限制在可达任务包络后，MuJoCo筛选恢复95%成功率（n=20），真实机器人上所有30次试验均落在容忍度内：位置误差2.64±1.04cm，姿态误差6.92±1.33°，能耗中位数54.9J。
- 硬件上能耗分布向低频段移动（中位数54.9J vs. 模拟98.16J），主要由软PD控制器和扭矩限制所致，能量构成从铜损主导转向更均衡的混合模式。

## 七、优点
- **端到端能量感知框架**：从仿真训练到实物部署的一整条验证链条，首次在真实人形机器人手臂上实现了基于强化学习的能量高效伸展。
- **实验辨识电力模型的质量**：R²=0.933，持出R²=0.965，能够准确捕捉不同扭矩/速度操作点下的功耗组成。
- **混合星座奖励设计**：将位置和姿态误差融合为一个几何量（星座距离），无需手动调权重，简化了奖励工程。
- **系统的sim-to-real差距分析**：通过PD增益扫描、工作空间可达性分析量化了动态与几何两大差距来源，指出了完美跟踪假设和几何可达性限制是主要瓶颈。
- **硬件验证充分**：30次独立试验均成功，误差分布清晰，并报告了原始数据（位置/姿态误差图），透明性强。

## 八、不足与局限
- **真实机器人样本量较小**（n=30），不足以统计精确的成功率，仅为可行性演示。
- **未直接训练α>0的完全电力模型奖励**：代理项λτ‖τ‖²与真实功耗相关性仅限于铜损部分，可能抑制进一步能效提升，且未进行对比消融。
- **仅使用单一初始姿势和工作空间包络**：起始位置固定于中性姿势附近，任务包络限于苹果采摘近似范围，泛化能力未验证。
- **未进行域随机化或真实数据微调**：从仿真到实物的直接迁移依赖PD增益选择，但姿态误差仍接近容忍度上限（8.58°），对工作空间边缘可能失效。
- **基准对比不公平**：最小急动度基线拥有关节空间先验，RL仅知笛卡尔位姿，因此无法直接衡量RL的能量优化相对优势。
- **无多次训练重复**：仅报告一次训练的结果，未提供多次随机种子下的方差，影响统计可靠性。

（完）
