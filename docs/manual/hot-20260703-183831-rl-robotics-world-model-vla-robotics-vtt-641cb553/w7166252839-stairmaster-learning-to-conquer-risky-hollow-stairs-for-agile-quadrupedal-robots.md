---
title: "StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots"
title_zh: StairMaster：学习征服危险空心楼梯的敏捷四足机器人
authors: "X W Tang, Youhan Xie, Zhengjie Shu, Wanyu Li, Lai Jiang, Wenkang Hu, Yitong Li, Ruigang Yang"
date: 2026-06-24
pdf: "https://arxiv.org/pdf/2606.25765"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: "Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning。"
source: openalex
selection_source: hot_paper_scout
motivation: "摘要线索：Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise。"
method: "摘要线索：In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains。"
result: "摘要线索：To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments。"
conclusion: "摘要线索：To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments。"
---

## 摘要
对于四足机器人而言，攀爬空心楼梯仍是一个具有挑战性的问题，原因在于腿部被卡住的高风险、深度信息极度稀疏以及高频深度传感噪声。本文提出StairMaster，一种新颖的三阶段强化学习框架，用于在此类极端不连续地形上实现稳定运动。我们的架构集成了交叉注意力机制，从含噪深度数据中提取结构特征，并配备空间感知循环单元（SRU），通过维护鲁棒的时空记忆来缓解感知盲区。为弥合深度感知中的仿真到现实差距，我们提出一种高保真的仿真到现实深度传感器建模流程，能够真实模拟真实世界传感器伪影。此外，我们采用3D航路点引导的主动感知奖励以实现主动感知，并引入空心间隙运动学与楼梯边缘惩罚以确保精确的落脚点放置。我们成功将StairMaster部署于Unitree Go2机器人上，通过零样本迁移展示了其征服倾斜角高达55°的空心楼梯的能力。据我们所知，这是首个在现实环境中实现如此陡峭空心楼梯攀爬的基于强化学习的策略。项目网站：https://sivan666666.github.io/StairMaster/。

## Abstract
Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a Cross-Attention mechanism to extract structural features from noisy depth data, alongside a Spatial-aware Recurrent Unit (SRU) that maintains robust spatio-temporal memory to mitigate perception blind spots. To bridge the sim-to-real gap in depth perception, we propose a high-fidelity sim-to-real depth sensor modeling pipeline that faithfully replicates real-world sensor artifacts. Additionally, we employ a 3D waypoint-guided active perception reward for proactive sensing, alongside hollow gap kinematic and stair edge penalties to ensure precise foothold placement. We successfully deployed StairMaster on a Unitree Go2 robot, demonstrating its ability to conquer hollow stairs with an unprecedented incline of up to 55$^\circ$ through zero-shot transfer. To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments. Project Website: https://sivan666666.github.io/StairMaster/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：四足机器人在工业场景（如电厂、建筑工地）中需要攀爬空心楼梯，但这种楼梯因缺少垂直踏板，存在巨大的物理空隙，极易导致机器人腿部卡入、跌倒甚至硬件损坏。
- **问题挑战**：1）**腿部卡入风险**：微小落脚误差就可能导致腿落入空隙；2）**深度感知稀疏**：空心楼梯常用反光或格栅材料，深度相机产生大量像素丢失和极端噪声；3）**视觉盲区**：前向摄像头视野有限，当楼梯穿过机器人腹部后，后腿落脚点完全不可见，需要时空记忆推断。
- **现有方法不足**：传统视觉运动控制框架（如Extreme Parkour）难以应对真实世界的深度传感器噪声、剧烈振动引起的图像畸变，且缺乏主动感知和长时间空间记忆能力。

## 二、论文提出的方法论
- **核心思想**：提出一个三阶段强化学习框架 **StairMaster**，结合交叉注意力、空间感知LSTM、高保真深度噪声建模和定制化奖励函数，实现零样本迁移的真实世界陡峭空心楼梯攀爬。
- **技术细节**：
  - **三阶段训练**：
    1. **阶段一（教师策略）**：使用PPO算法，基于特权高度图和本体感受训练教师策略。
    2. **阶段二（学生蒸馏）**：学生网络仅使用含噪深度图+本体感受，通过MSE损失模仿教师动作，并集成交叉注意力+空间感知LSTM。
    3. **阶段三（微调）**：使用PPO对学生网络进行强化学习微调，弥补蒸馏性能差距。
  - **视觉空间编码器**：
    - **交叉注意力**：以本体感受embedding为Query，深度图像CNN特征为Key/Value，动态聚焦楼梯边缘等关键几何结构。
    - **空间感知LSTM（SRU）**：引入可学习的空间变换门 $s_t = \sigma(W_s f_t + b_s)$，对历史隐藏状态和细胞状态进行元素级空间对齐，隐式维护时空记忆，弥补视觉盲区。
  - **高保真深度噪声建模**：
    - 模拟高斯/均匀噪声、空洞噪声（像素缺失）、边缘噪声（深度不连续处的散射）等静态伪影。
    - 模拟立体匹配噪声和振动引起的**高斯位移噪声**（随机平移像素位置），迫使网络学习振动不变特征。
  - **定制奖励函数**（在标准奖励之外添加）：
    - **3D航路点主动感知奖励 $r_{pitch}$**：以第二个台阶中心为目标航路点，计算相对向量同时监督偏航和俯仰角。当机器人到航路点距离 $d < d_{th}$ 时，根据俯仰偏差给出指数惩罚，迫使机器人提前抬头，获得前瞻视野。
    - **空心间隙运动学惩罚 $r_{hollow}$**：若任何脚落入预定义的空隙包围盒 $B_{hollow}$，则给予固定惩罚 $-c_{hollow}$。
    - **楼梯边缘惩罚 $r_{edge}$**：若脚落点距台阶边缘小于安全阈值 $d_{safe}$，则施加惩罚 $-c_{edge}$，鼓励落脚于台阶中心。
  - **地形课程设计**：从平地逐步增加坡度（最高55°），并注入随机高度/间隙噪声，防止记忆化步态。

## 三、实验设计
- **仿真环境**：Isaac Gym模拟器，构建了不同坡度的空心楼梯（0°、20°、30°、40°、50°、55°）和随机混合楼梯（随机高度和水平间隙）。
- **对比方法**：Extreme Parkour（视觉两阶段框架）、HIMLoco（盲运动策略），以及三个消融变体（去掉$r_{pitch}$、去掉$r_{foothold}$、去掉深度噪声建模）。
- **评估指标**：成功率（到达顶部终点）、平均到达台阶百分比、平均碰撞次数。
- **真实世界实验**：Unitree Go2机器人+Intel RealSense D435深度相机+Jetson Orin NX计算模块，控制频率50Hz。测试37°和55°两种真实空心楼梯，与内置MPC、内置RL、Extreme Parkour、HIMLoco对比，每项10次试验。

## 四、资源与算力
- 训练使用 **单张 NVIDIA RTX 4090 GPU**（文中未明确说明训练时长或训练步数）。
- 真实世界部署使用 **Jetson Orin NX** 模块，深度相机10Hz，控制频率50Hz，PD控制器增益 $K_p=40, K_d=1$。

## 五、实验数量与充分性
- **仿真实验**：进行了全面的对比（表I）和消融实验（表II、图6、图7）。在6种坡度+混合地形上重复评估，每个条件未明确具体重复次数，但从标准差和百分比看应有多次。
- **噪声鲁棒性实验**（图7）：测试0%~200%噪声水平下平均到达台阶百分比，对比Ours、Ours w/o depth noise和Extreme Parkour，证明噪声建模的关键作用。
- **真实世界实验**：两种坡度各10次试验，结果如表III。但样本量较小（10次），55°下成功率40%可能存在偶然性；且仅测试了两种坡度，缺乏更广坡度范围的验证。
- **公平性**：对比基线均在同一条件下重新训练（但保留其原始奖励和设置），符合公平原则。消融实验设计合理，验证了每个组件的必要性。
- **充分性**：实验覆盖了主要挑战（感知噪声、盲区、边缘风险），但真实世界场景单一（仅两种楼梯），且未与其他视觉-本体融合方法（如RMA、MLP）进行横向对比。

## 六、论文的主要结论与发现
- StairMaster在仿真中实现55°空心楼梯97.5%成功率，20°~55°下均接近100%；真实世界37°下80%，55°下40%成功率，是首个基于RL实现在55°空心楼梯上零样本迁移的方法。
- 盲策略（HIMLoco）完全失败，证明视觉对不连续地形的必要性；Extreme Parkour因缺乏时空记忆和主动感知在20°以上全部失败。
- 奖励函数设计显著影响性能：$r_{pitch}$提升陡坡地形等级，大幅减少碰撞；$r_{foothold}$降低落脚风险；深度噪声建模是零样本迁移的关键，去除后真实世界成功率从80%降至40%（37°）和从40%降至10%（55°）。
- 空间感知LSTM和交叉注意力有效解决了视觉盲区和噪声下的特征提取问题。

## 七、优点
1. **问题针对性强**：专门针对空心楼梯的腿部卡入、感知稀疏、盲区三大挑战设计，而非通用方案。
2. **系统设计完整**：从多模态特征融合（交叉注意力）到时空记忆（空间感知LSTM）再到仿真-真实噪声桥接，形成一个闭环。
3. **定制化奖励创新**：3D航路点主动感知奖励首次将俯仰角纳入优化目标，同时实现运动优化和主动感知；空心间隙和边缘惩罚直接规避最危险失效模式。
4. **仿真-真实迁移效果好**：高保真深度噪声建模让零样本迁移成为可能，在真实噪声200%下仍能完成99.8%的台阶。
5. **实时性好**：在Jetson Orin NX上以50Hz控制频率运行，满足敏捷运动需求。

## 八、不足与局限
1. **真实世界成功率偏低**：55°下仅40%，仍有较大风险，样本量小（10次）可能不足以代表性能。未披露失败原因分析（如是卡腿还是踏空）。
2. **实验场景单一**：仅测试两种实际坡度（37°和55°），且未评估不同台阶宽度、间隙长度、材料表面等变化，泛化性存疑。
3. **硬件依赖性**：深度噪声建模可能针对Intel D435特定特性，在其他深度相机上迁移效果未知；仅使用Unitree Go2平台。
4. **对比基线有限**：未与近期先进的视觉运动方法（如PIE、WMP、PLANC）比较，也未与纯像素级方法对比；仅有Extreme Parkour一个视觉基线，且其原始奖励未针对空心楼梯调整，可能不公平。
5. **训练细节缺失**：未报告训练步数、奖励系数具体值、课程学习参数等超参数，难以复现。
6. **计算需求**：虽单GPU训练，但三阶段耗时可能较长，文中未提及，实际工程部署成本未评估。

（完）
