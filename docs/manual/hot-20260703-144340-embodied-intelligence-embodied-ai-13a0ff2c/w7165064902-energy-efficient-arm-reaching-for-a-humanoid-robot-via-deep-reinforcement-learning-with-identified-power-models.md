---
title: Energy-Efficient Arm Reaching for a Humanoid Robot via Deep Reinforcement Learning with Identified Power Models
title_zh: 通过深度强化学习与辨识功率模型实现人形机器人节能手臂伸展
authors: "Nestor N. Deniz, Simon Parsons, Fernando Auat Cheein"
date: 2026-06-14
pdf: "https://arxiv.org/pdf/2606.15918"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=humanoid robot policy"
tldr: "人形机器人在野外作业如苹果采摘时受电池能量严重制约，每次充电可执行的到达动作数量有限。为此提出端到端能量感知强化学习框架，将实验辨识的电气功率模型与SAC算法结合，在Pinocchio模拟器中训练7自由度左臂。训练使用增量关节位置动作空间与混合星座奖励函数，模拟中成功率69.9%，均能98.16焦耳。实体Unitree G1验证均能71.5焦耳，位置误差2.64厘米，取向误差6.92度，为能量感知强化学习臂部到达奠定基础。"
source: openalex
selection_source: hot_paper_scout
motivation: 解决人形机器人在野外操作中因电池能量限制导致每次充电可执行到达运动次数有限的问题。
method: 结合实验辨识电气功率模型的SAC策略，在Pinocchio刚体动力学模拟器内使用增量关节位置动作空间和混合星座奖励函数训练。
result: "模拟5×10^6步训练后成功率达69.9%，均能98.16焦耳；实体机器人三批测试均能71.5±48.3焦耳，位置误差2.64±1.04厘米，取向误差6.92±1.33度。"
conclusion: 首次将能量感知强化学习成功应用于人形机器人臂部到达运动，为后续节能操作奠定基础。
---

## 摘要
人形机器人在野外执行操作任务（如机器人采摘苹果）时面临严重的能量限制，这直接限制了每充电一次可执行的伸展运动次数。本文针对Unitree G1人形机器人的7自由度左臂，提出了一种端到端的能量感知强化学习框架，结合了基于物理实验辨识的电功率模型与在基于Pinocchio的刚体动力学模拟器中训练的软演员-评论家（SAC）策略。该强化学习策略在增量关节位置动作空间上进行操作，并使用混合星座奖励进行训练，该奖励将四点末端执行器星座距离与扭矩范数能量代理相结合；在5×10^6次训练后，在运动学模拟中对1000个随机目标达到了69.9%的成功率，成功情节的平均能量为98.16焦耳。最后，在物理Unitree G1上，该策略在三个独立的10目标批次上进行了验证，平均能量为71.5 ± 48.3焦耳，末端执行器位置误差为2.64 ± 1.04厘米，定向误差为6.92 ± 1.33度——均在4厘米/8.6度的训练容差范围内。这些结果构成了迈向基于能量感知强化学习的人形机器人手臂伸展的第一步。

## Abstract
Humanoid robots performing in-field manipulation tasks, such as robotic apple harvesting, face severe energy constraints that directly limit the number of reaching motions that can be executed per battery charge. This paper presents an end-to-end, energy-aware reinforcement learning framework for the 7-degree-of-freedom left arm of the Unitree~G1 humanoid robot, combining a physics-based, experimentally identified electrical power model with a Soft Actor-Critic (SAC) policy trained in a Pinocchio-based rigid-body dynamics simulator. The RL policy operates on an incremental joint-position action space and is trained with a Hybrid Constellation Reward that combines a four-point end-effector constellation distance with a torque-norm energy proxy; after % $5\times10^6$ training it reaches a $69.9\%$ success rate over $1\,000$ random targets in kinematic simulation, at a mean energy of \SI{98.16}{\joule} on successful episodes. Finally, on the physical Unitree~G1, the policy is validated over three independent 10-target batches, achieving a mean energy of $71.5 \pm 48.3$\,J, an end-effector position error of $2.64 \pm 1.04$\,cm, and an orientation error of $6.92 \pm 1.33^\circ$ -- within the \SI{4}{\centi\metre}/$8.6^\circ$ training tolerance. These results constitute a first step toward energy-aware reinforcement-learning-based arm reaching for humanoid robots.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：人形机器人在野外执行操作任务（如苹果采摘）时，依赖电池供电，而每次充电可执行的臂部伸展运动次数受限于能量消耗。现有方法（如经典运动规划、模型预测控制）计算开销大或依赖高保真模型，难以兼顾低能耗与实时性。
- **整体含义**：本研究首次将实验辨识的电功率模型嵌入强化学习奖励中，实现端到端能量感知的臂部伸展策略，并通过从运动学模拟到实体机器人的四阶段验证，展示了该框架在节省能耗、延长续航方面的潜力，为农业机器人等应用提供了基础。

## 二、论文提出的方法论
- **核心思想**：基于深度强化学习的软演员-评论家（SAC）算法，在仿真环境中训练策略，使机器人臂能以低能量到达目标位姿；训练中使用了通过物理实验辨识得到的电功率模型作为评价指标，但奖励中仅使用扭矩范数作为能量代理，以保持奖励平滑。
- **关键技术与公式**  
  - **电功率模型**：P_net = Σ[ a_i τ_i ω_i + b_i Δτ²_i + c_i |ω_i| + d_i ω_i² ] + Σ_{i<j} e_ij |ω_i||ω_j|，包含机械功率、铜损、库仑摩擦、粘性摩擦及联合速度交互项。参数通过实验辨识（R²=0.933，RMSE=1.07W）。  
  - **Markov决策过程**：状态包括归一化关节角、速度、位置误差、方向误差、剩余时间；动作采用增量关节位置目标（Δq_max=0.1667 rad），通过比例控制器生成速度命令，再由RNEA计算扭矩。  
  - **混合星座奖励**：将4个虚拟点固定在末端执行器上，计算其当前位置与目标位置的平均平方距离（d_con），该距离同时反映位置和方向误差。奖励包含：d_con的减小、指数项、稀疏成功奖金（700）、恒定步长成本、平滑惩罚和扭矩范数能量代理（λτ=5×10⁻⁵）。  
  - **训练算法**：Algorithm 1详细描述了每步流程（采样动作、计算目标位置、命令速度、积分、RNEA扭矩、奖励、存储到回放缓冲、SAC更新）。超参数见表III：学习率3×10⁻⁴，折扣0.99，回放缓冲容量5×10⁵，网络结构[256,256]。

## 三、实验设计
- **训练与评估场景**  
  - **运动学模拟（Pinocchio）**：7自由度臂模型，忽略动力学，假设速度完美跟踪；随机采样1000个目标（关节空间随机配置经正向运动学得到位姿）。  
  - **动力学模拟（MuJoCo）**：完整29自由度Unitree G1模型，浮基固定；测试4种PD增益（30/50/100/400），对200个目标评测。  
  - **真实机器人（Unitree G1）**：3批次共30个独立目标（来自可到达工作空间子集，x≥0.1m，逆运动学残差<2cm）。  
- **基准方法**：关节空间最小加加速度轨迹（最小加加速度轨迹），具有完整目标关节角度（相当于特权信息），100%成功但计算量大。  
- **对比方法**：未与其他RL方法或经典规划器在相同能耗指标下严格比较；文中将RL策略与最小加加速度基线在运动学模拟中对比了成功率、能耗等。  
- **消融与分析**：  
  - PD增益扫查（表IV、图1）揭示模拟到真实差距主要源于完美跟踪假设，而非增益调优。  
  - 可达到工作空间分析（表VII）：80个随机点中仅30%在2cm内可到达，解释为何限制子集后成功率从46%升至95%。  

## 四、资源与算力
- **训练平台**：NVIDIA RTX系列GPU（未明确具体型号），8个并行环境（SubprocVecEnv），有效吞吐量约1000–1700步/秒。  
- **训练时长**：总计5×10⁶环境步（未报告具体墙钟时间）。  
- **硬件验证**：无额外算力需求，推理在CPU上前向传播<1ms。  

## 五、实验数量与充分性
- **运动学模拟**：1000个随机目标（n=1000），统计充分，成功率为69.9%。  
- **MuJoCo动力学**：200个目标（n=200），并额外在n=200时验证稳定趋势；覆盖4种PD增益。  
- **真实机器人**：30个目标（3×10），数量较少，作者承认属于可行性展示而非大规模统计估计。  
- **消融实验**：仅对PD增益和工作空间进行了系统分析；未对奖励函数中的能量代理权重（λτ）或是否直接使用功率模型（α>0）进行消融（因计算资源限制）。  
- **充分性评价**：在实验设计的系统性（四阶段验证、工作空间分析）方面较好，但在统计力度和消融全面性上有局限，尤其真实实验样本量不足。

## 六、论文的主要结论与发现
- **成功率**：运动学模拟69.9%；MuJoCo全工作空间降至46%；限制到可到达子集后恢复至95%（n=20）；真实机器人30次全部成功（均在4cm/8.6°容差内）。  
- **能耗**：成功情节平均能耗：运动学模拟98.16J，真实机器人71.5J（中位数54.9J），远低于运动学模拟值，表明软PD控制器和限制工作空间降低了实际扭矩。  
- **模拟到真实差距**：主要源于完美跟踪假设（速度命令不能瞬时实现），PD增益扫查显示差距基本与增益无关。工作空间不可达性（几何原因）是另一个重要因素。  
- **能量分解**：运动学模拟中以铜损为主（87.6%），真实机器人上变为铜损46.1%、粘性摩擦20.4%、机械功17.5%，证明功率模型在不同操作区域鲁棒。  

## 七、优点
- **功率模型辨识**：基于物理的电气功率模型实验辨识准确（R²=0.933），且5项物理项在实际中展现出不同贡献，验证了模型泛化性。  
- **混合星座奖励**：通过虚拟点距离巧妙耦合位置和方向误差，免去了手工调节权重。  
- **增量关节位置动作空间**：保证不超出速度极限，避免了动作饱和问题。  
- **系统性验证**：从运动学模拟、动力学模拟（带PD增益扫查）、工作空间限制分析到真实机器人，四阶段清晰展示差距来源和性能。  
- **可达到工作空间分析**：识别出几何不可达性，并将其从控制问题中分离，对于部署具有指导意义。  
- **显著节能**：真实机器人能耗均值71.5J（成功情节），比运动学模拟低27%，且所有试验均在容差内，证明了实际可行性。

## 八、不足与局限
- **真实验证样本量小**：仅30次独立试验（3批次×10），不足以提供统计显著的成功率估计，作者也明确表示属于可行性演示。  
- **奖励能量代理不完美**：训练中未直接使用辨识功率模型（α=0），使用了扭矩范数代理，可能导致策略不是真正面向功率模型最优；作者提到未来可尝试α>0。  
- **完美跟踪假设**：运动学训练假设速度瞬时执行，导致在现实控制器下出现3–5°的方向跟踪误差，尽管通过PD增益选型和限制工作空间部分缓解，但未从根本上解决。  
- **缺乏完整采摘系统集成**：论文只关注到达运动，未涉及感知、抓取、躯干/基座定位等，且目标位姿通过合成采样而非真实果实检测。  
- **计算资源细节缺失**：未报告确切GPU型号、训练墙钟时间，影响可复现性。  
- **消融实验不充分**：未对奖励中各项权重（如λτ、δcon）进行敏感性分析，也未对比不同RL算法（如PPO）。  
- **应用限制**：工作空间限制（x≥0.1m、IK残差<2cm）使得仅小部分名义工作空间可用，需结合基座移动才能扩大操作范围。

（完）
