---
title: "StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots"
title_zh: StairMaster：学习攻克危险空心楼梯的敏捷四足机器人
authors: "X W Tang, Youhan Xie, Zhengjie Shu, Wanyu Li, Lai Jiang, Wenkang Hu, Yitong Li, Ruigang Yang"
date: 2026-06-24
pdf: "https://arxiv.org/pdf/2606.25765"
tags: ["query:热点论文筛选", "query:具身智能", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=humanoid robot"
tldr: 针对四足机器人攀爬空心楼梯时腿部卡住、深度稀疏和传感器噪声难题，提出StairMaster三阶段强化学习框架。框架融合交叉注意力机制提取噪声深度结构特征，空间感知循环单元缓解感知盲点，并设计3D路标点主动感知奖励及空心间隙膝盖惩罚实现精确足部放置。采用高保真深度传感器建模弥合仿真现实差距。在Unitree Go2上零样本迁移成功攀爬55度空心楼梯，为首次在真实环境中实现陡峭空心楼梯攀登的RL策略，实验证明其在极陡坡度下可靠运行。
source: openalex
selection_source: hot_paper_scout
motivation: 四足机器人攀爬空心楼梯存在腿部卡住、深度稀疏和高噪声问题，现有方法难以应对极端不连续地形。
method: 提出三阶段强化学习框架，集成交叉注意力、空间感知循环单元、3D路标点主动感知奖励和运动学惩罚，并采用高保真深度传感器建模。
result: 在Unitree Go2上零样本迁移成功攀爬55度空心楼梯，首次在真实环境实现如此陡峭攀爬。
conclusion: StairMaster通过感知与运动学习融合有效解决空心楼梯攀爬难题，在极端坡度下展现鲁棒性。
---

## 摘要
由于腿部卡住的高风险、严重的深度稀疏性以及高频深度感知噪声，攀爬空心楼梯对于四足机器人仍然是一个具有挑战性的问题。在本文中，我们提出了StairMaster，一种新颖的三阶段强化学习框架，用于在此类极端不连续地形上实现稳定运动。我们的架构集成了交叉注意力机制，用于从噪声深度数据中提取结构特征，同时结合空间感知循环单元（SRU）以维持稳健的时空记忆，从而减轻感知盲区。为了弥合深度感知中的仿真到现实差距，我们提出了一个高保真的仿真到现实深度传感器建模管道，忠实地复制了真实世界的传感器伪影。此外，我们采用了3D路径点引导的主动感知奖励来实现主动感知，同时结合了空心间隙运动学与楼梯边缘惩罚以确保精确的立足点放置。我们成功地将StairMaster部署在Unitree Go2机器人上，通过零样本迁移展示了其攻克倾角高达55°的空心楼梯的能力。据我们所知，这是首个在真实世界环境中实现如此陡峭空心楼梯攀爬的基于强化学习的策略。项目网站：https://sivan666666.github.io/StairMaster/。

## Abstract
Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a Cross-Attention mechanism to extract structural features from noisy depth data, alongside a Spatial-aware Recurrent Unit (SRU) that maintains robust spatio-temporal memory to mitigate perception blind spots. To bridge the sim-to-real gap in depth perception, we propose a high-fidelity sim-to-real depth sensor modeling pipeline that faithfully replicates real-world sensor artifacts. Additionally, we employ a 3D waypoint-guided active perception reward for proactive sensing, alongside hollow gap kinematic and stair edge penalties to ensure precise foothold placement. We successfully deployed StairMaster on a Unitree Go2 robot, demonstrating its ability to conquer hollow stairs with an unprecedented incline of up to 55$^\circ$ through zero-shot transfer. To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments. Project Website: https://sivan666666.github.io/StairMaster/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：四足机器人在攀爬工业场景中常见的空心楼梯（开放式踏板楼梯）时，面临三大严峻挑战：腿部卡入踏板间空洞的风险极高、深度相机因反射材质导致像素缺失严重、机器人本体向上攀爬时前向相机视野消失引发的感知盲区。
- **动机**：现有视觉-运动控制框架（如Extreme Parkour、HIMLoco）在真实空心楼梯上表现乏力，无法处理严重深度噪声、缺乏时空记忆来维持对已消失踏板的追踪，且缺乏主动感知机制来提前观察即将面临的楼梯结构。
- **背景**：此项研究旨在填补零样本迁移条件下、无预先数据采集的四足机器人攀爬陡峭空心楼梯（最大倾角55°）的技术空白，这是首次基于RL策略在真实环境中实现这一壮举。

## 二、论文提出的方法论
- **核心思想**：提出三阶段强化学习框架StairMaster，通过端到端方式从原始深度图像和本体感受直接输出关节角度指令。核心是构建高保真深度噪声建模、融合交叉注意力与空间感知LSTM的视空间编码器，以及针对空心楼梯定制的奖励函数。
- **关键技术细节**：
  - **三阶段训练管道**：
    1. **特权教师训练**（Stage 1）：在模拟器中利用特权高度图与PPO算法训练教师策略，获得专家行为。
    2. **学生策略蒸馏**（Stage 2）：学生网络仅能访问噪声深度图像和本体感受，通过MSE损失模仿教师动作。学生网络引入交叉注意力机制动态融合深度与本体特征，并使用空间感知LSTM维持时空记忆。
    3. **微调阶段**（Stage 3）：对蒸馏后的学生策略使用PPO进行在线微调，纠正次优行为，最终输出关节命令用于零样本真实部署。
  - **视空间编码器架构**：
    - 交叉注意力：将本体感受嵌入作为查询，深度CNN特征作为键和值，动态关注任务相关结构（如楼梯边缘）。
    - 空间感知LSTM：引入可学习空间门控$s_t = \sigma(W_s f_t + b_s)$，对隐藏状态和细胞状态进行空间变换，隐式对齐历史记忆与当前视角，构建全尺度时空记忆。
  - **高保真深度噪声建模**：模拟真实深度传感器在反射表面、运动模糊下的伪影，包括高斯/均匀噪声、孔洞噪声、边缘噪声、立体匹配噪声、高斯移位（模拟振动导致像素平移）。预处理包括裁剪、值裁剪、空间缩放和高斯模糊，统一模拟与真实数据。
  - **定制奖励函数**：
    - **3D路标点主动感知奖励**$r_{pitch}$：以第二块踏板中心为目标，通过计算当前俯仰角与目标俯仰角的偏差惩罚，仅在距离小于阈值$d_{th}$时触发。作用：优化运动学与主动感知。
    - **空心间隙运动学惩罚**$r_{hollow}$：任意足部落入空心区域（预定义包围盒$B_{hollow}$）则施加固定惩罚$-c_{hollow}$。
    - **楼梯边缘惩罚**$r_{edge}$：足部接触点距踏板边缘小于安全裕度$d_{safe}$时施加惩罚$-c_{edge}$。

## 三、实验设计
- **实验场景与数据集**：在Isaac Gym模拟器中训练，地形采用渐进式课程学习（从0°平地逐步增至55°空心楼梯，同时随机化台阶高度、宽度、水平间隙）。真实实验采用Unitree Go2四足机器人，搭载Intel RealSense D435深度相机，机载NVIDIA Jetson Orin NX计算模块（控制频率50Hz）。
- **对比方法**：
  - Extreme Parkour：两阶段视觉跑酷框架。
  - HIMLoco：纯盲走混合内部模型基线。
  - 消融变体：Ours w/o $r_{pitch}$、Ours w/o $r_{foothold}$（移除空洞与边缘惩罚）、Ours w/o depth noise（移除深度噪声建模）。
- **评估指标**：成功率（到达顶部终点）、平均到达步数百分比、平均碰撞次数（消融实验）。在三种模拟环境测试：平地、标准空心楼梯、随机混合楼梯（随机台阶高度与水平间隙）。真实实验：倾角37°和55°空心楼梯各10次试验。

## 四、资源与算力
- 训练使用**单块NVIDIA RTX 4090 GPU**（论文明确提及），在Isaac Gym模拟器中进行。
- 未明确说明训练总时长、迭代次数或具体GPU数量（仅一块）。学生策略微调阶段需要额外PPO训练，但具体耗时未提供。
- 真实部署平台为Jetson Orin NX，算力有限，但策略以50Hz实时运行。

## 五、实验数量与充分性
- **模拟实验**：进行了全面比较，包括成功率、平均到达步数、平均碰撞数（表I、表II）。消融实验涵盖三个主要组件（pitch奖励、foothold奖励、深度噪声），并在多个难度等级（20°~55°）和混合地形上测试。
- **深度噪声鲁棒性测试**：在30°楼梯上对三种方法施加0%~200%噪声，记录平均到达步数（图7），覆盖了极端噪声条件。
- **真实实验**：37°和55°各10次试验（表III），对比了5种基线（包括内置MPC、内置RL、Extreme Parkour、HIMLoco以及自身消融版本）。成功支持零样本迁移。
- **充分性评价**：模拟实验场景多样、消融完整、噪声测试深入；真实实验次数较少（每坡度10次），但考虑物理机器人的高风险，可接受。数据点足够支撑主要结论，但缺乏跨机器人、跨楼梯材质（如不同反射率）的泛化测试。实验总体比较公平，对比基线均为公开SOTA方法。

## 六、论文的主要结论与发现
- StairMaster在模拟环境下在55°空心楼梯上达到97.5%成功率，在随机混合地形上86.5%成功率，远超所有基线（其他方法成功率为0%）。
- 消融实验证明每个组件不可或缺：缺少pitch奖励导致碰撞次数大幅上升；缺少foothold惩罚导致足部放置精度下降；缺少深度噪声建模在真实世界成功率骤降（55°从40%降至10%）。
- 真实实验中，StairMaster在37°楼梯成功率80%（高于内置RL盲走70%），在55°达成40%成功率，而所有对比基线在55°均为0%。
- 主动感知奖励使机器人提前调整俯仰角，在55°坡上实现流畅攀爬（<4秒完成），有效缓解感知盲区。
- 深度噪声建模显著提升对传感器噪声的鲁棒性：即使在200%噪声下仍保持99.8%完成率，而未建模版本仅7.3%。

## 七、优点
- **方法创新**：首次将交叉注意力与空间感知LSTM结合用于四足机器人视觉运动控制，有效处理感知盲区；三阶段训练管道（教师→学生→微调）确保稳定蒸馏与在线优化。
- **工程实用性**：高保真深度噪声建模精确匹配真实传感器伪影，实现零样本迁移；定制奖励函数直接针对空心楼梯的致命危险（腿部卡住、边缘滑落）。
- **实验设计**：包含详尽的消融分析、噪声鲁棒性测试、多个基线对比，结果量化充分且可视化（故障模式图示）。
- **突破性能**：首次在真实场景实现55°空心楼梯攀爬，展示了四足机器人应对极端基础设施的能力。

## 八、不足与局限
- **真实实验统计力较低**：每次坡度仅10次试验，可能存在随机波动（55°成功率40%，可信区间较宽）。未进行多次重复试验以评估统计显著性。
- **场景泛化局限**：未测试不同楼梯材质（如不同反射率、格栅型踏板）、不同机身体型（仅Unitree Go2）、更复杂连续阶梯（如螺旋空心梯）。
- **传感器依赖**：仅依赖深度相机；论文提及未来工作将融合RGB图像以增强环境感知，说明当前策略在纹理丰富场景下可能表现不佳。
- **计算资源需求**：三阶段训练管道需大量模拟迭代，但论文未详细报告训练时间与能耗，难以评估可复现性与效率。
- **故障恢复缺失**：策略在真实世界失败后（40%失败率）如何自主恢复未探讨，实际部署中可能需要安全保护机制。

（完）
