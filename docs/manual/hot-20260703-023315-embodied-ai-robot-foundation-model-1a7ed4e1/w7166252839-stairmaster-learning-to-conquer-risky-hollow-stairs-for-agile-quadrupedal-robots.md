---
title: "StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots"
title_zh: "StairMaster: 学习征服危险空心楼梯以实现敏捷四足机器人"
authors: "X W Tang, Youhan Xie, Zhengjie Shu, Wanyu Li, Lai Jiang, Wenkang Hu, Yitong Li, Ruigang Yang"
date: 2026-06-24
pdf: "https://arxiv.org/pdf/2606.25765"
tags: ["query:热点论文筛选", "query:具身智能", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=humanoid robot"
tldr: 四足机器人爬空心楼梯时易卡腿，且深度感知存在稀疏与噪声问题。本文提出StairMaster三阶段强化学习框架，利用交叉注意力与空间感知循环单元提取结构特征、维持时空记忆，并采用高保真深度传感器建模和主动感知奖励。在Unitree Go2上零样本转移成功爬升55度空心楼梯，为首次基于RL实现的陡峭空心楼梯爬行。
source: openalex
selection_source: hot_paper_scout
motivation: 现有方法难以处理空心楼梯的腿卡住风险和感知盲区，亟需鲁棒的感知与运动控制框架。
method: 三阶段RL结合交叉注意力提取深度特征、SRU维持时空记忆，高保真传感器建模及主动感知奖励与运动学惩罚。
result: 在Unitree Go2上零样本转移实现55度空前的陡峭空心楼梯爬行。
conclusion: StairMaster有效克服空心楼梯挑战，为极端地形四足机器人提供可行方案。
---

## 摘要
由于腿部被卡住的高风险、深度稀疏性以及高频深度感知噪声，爬空心楼梯对四足机器人来说仍然是一个具有挑战性的问题。本文提出StairMaster，一种新颖的三阶段强化学习框架，用于在此类极端不连续地形上实现稳定运动。我们的架构集成了交叉注意力机制，从噪声深度数据中提取结构特征，以及空间感知循环单元（SRU），通过保持鲁棒的时空记忆来缓解感知盲区。为了弥合深度感知中的仿真到现实差距，我们提出了高保真的仿真到现实深度传感器建模流程，忠实地复现真实传感器伪影。此外，我们采用3D航点引导的主动感知奖励以实现主动感知，同时引入空心间隙运动学和楼梯边缘惩罚以确保精确的足部落点。我们成功地将StairMaster部署在Unitree Go2机器人上，展示了其通过零样本迁移能够征服倾斜角高达55度的空心楼梯。据我们所知，这是首个在真实环境中实现如此陡峭空心楼梯攀爬的基于强化学习的策略。项目网站: https://sivan666666.github.io/StairMaster/

## Abstract
Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a Cross-Attention mechanism to extract structural features from noisy depth data, alongside a Spatial-aware Recurrent Unit (SRU) that maintains robust spatio-temporal memory to mitigate perception blind spots. To bridge the sim-to-real gap in depth perception, we propose a high-fidelity sim-to-real depth sensor modeling pipeline that faithfully replicates real-world sensor artifacts. Additionally, we employ a 3D waypoint-guided active perception reward for proactive sensing, alongside hollow gap kinematic and stair edge penalties to ensure precise foothold placement. We successfully deployed StairMaster on a Unitree Go2 robot, demonstrating its ability to conquer hollow stairs with an unprecedented incline of up to 55$^\circ$ through zero-shot transfer. To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments. Project Website: https://sivan666666.github.io/StairMaster/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：四足机器人在攀爬空心楼梯（Hollow Stairs）时面临三大挑战：① 楼梯无垂直踢面，腿部极易卡入间隙造成硬件损坏；② 空心楼梯多采用反光或格栅材料，深度相机出现严重像素丢失和噪声；③ 前向相机视野有限，楼梯台阶进入机器人下方后完全消失，导致后腿在完全视觉遮挡下执行精确落脚。
- **研究动机**：现有视觉-运动控制框架（如Extreme Parkour、HIMLoco）无法同时应对深度传感器噪声、视觉盲区、以及极度稀疏的落脚点。需要一种能主动感知、维持时空记忆并精确控制脚部落点的强化学习框架。
- **整体含义**：本文提出StairMaster，首次实现四足机器人在真实世界中零样本迁移攀爬倾斜角高达55°的空心楼梯，突破了现有RL方法在极端不连续地形上的能力边界。

## 二、论文提出的方法论
- **核心思想**：构建三阶段强化学习训练管线（Privileged Teacher → Student Distillation → Fine-tune），结合视觉-空间编码器、高保真深度噪声建模和定制化奖励函数，使机器人能够从噪声深度图像和本体感知中生成稳定运动指令。
- **关键技术细节**：
  - **Visuospatial Encoder**：包含两个模块：
    - *Cross-Attention*：将本体感知嵌入作为查询（Query），深度图像CNN特征作为键值（Keys/Values），动态关注与当前姿态最相关的几何结构（如楼梯边缘）。
    - *Spatial-Aware LSTM (SRU)*：引入可学习的空间变换门 \( s_t = \sigma(W_s f_t + b_s) \)，对上一时刻隐藏状态和细胞状态进行元素级空间对齐，再通过标准LSTM更新，从而在无显式自运动输入下维持跨帧的时空记忆。
  - **高保真深度噪声建模**：在仿真中模拟真实传感器伪影，包括：
    - 空间噪声：高斯/均匀噪声、孔噪声（随机像素丢失）、边缘噪声（模拟深度不连续处的晕染）。
    - 动态噪声：立体匹配量化误差、高斯偏移（模拟冲击振动导致的像素抖动）。
    - 预处理：裁剪、值剪裁、重采样、高斯模糊，统一仿真与真实深度输入。
  - **定制化奖励函数**（在标准奖励外新增三项）：
    - *3D航点主动感知奖励 \(r_{\text{pitch}}\)*：以第二级前方台阶中心为3D航点，引导机器人同时调整偏航和俯仰角。仅当距离小于阈值 \(d_{\text{th}}\) 时激活，惩罚当前俯仰与目标俯仰的偏差。作用：优化质心分布并使相机提前捕获台阶结构。
    - *空心间隙运动学惩罚 \(r_{\text{hollow}}\)*：任何脚部进入预定义的空心间隙包围盒 \(B_{\text{hollow}}\) 则施加固定惩罚 \(-c_{\text{hollow}}\)，迫使高抬腿安全跨越。
    - *楼梯边缘惩罚 \(r_{\text{edge}}\)*：若落脚点离台阶边缘距离小于安全阈值 \(d_{\text{safe}}\)，则施加惩罚 \(-c_{\text{edge}}\)，鼓励踩在台阶中心。
- **训练流程**：
  1. **Stage 1（教师策略）**：使用PPO，教师可访问特权高度图和本体感知，输出动作。
  2. **Stage 2（蒸馏）**：学生策略仅使用噪声深度图像+本体感知，通过MSE损失模仿教师动作；学生网络包含Cross-Attention和SRU。
  3. **Stage 3（微调）**：在模拟环境中用PPO对学生策略进行强化学习微调，补偿蒸馏性能损失，输出最终关节指令（50Hz控制频率，PD控制器解算力矩）。

## 三、实验设计
- **训练环境**：Isaac Gym模拟器，地形课程从平地（0°）逐步到55°空心楼梯，并注入随机高度和间隙噪声，每次重新采样难度防止过拟合。
- **评估场景**：
  - 模拟：平坦地面、标准化空心楼梯（0°~55°共7个坡度）、随机混合楼梯（随机台阶高度和水平间隙）。
  - 真实：37°和55°两套真实空心楼梯，各进行10次试验。
- **对比方法**：
  - Extreme Parkour（两阶段师生蒸馏视觉框架）
  - HIMLoco（纯本体感知盲走策略）
  - 机器人内置MPC和内置RL（Unitree自带）
  - 消融变体：Ours w/o \(r_{\text{pitch}}\)、Ours w/o \(r_{\text{foothold}}\)（同时去掉 \(r_{\text{hollow}}\) 和 \(r_{\text{edge}}\)）、Ours w/o depth noise（无深度噪声建模）
- **评估指标**：成功率（到达终点）、平均到达台阶百分比、碰撞次数（模拟消融中统计）。

## 四、资源与算力
- **训练硬件**：单块NVIDIA RTX 4090 GPU进行模拟训练。
- **部署硬件**：Unitree Go2四足机器人，搭载Intel RealSense D435深度相机（10Hz）、NVIDIA Jetson Orin NX机载计算模块。
- **训练时长**：论文未明确给出具体训练时间。

## 五、实验数量与充分性
- **模拟实验**：完整的成功率对比表（Table I）覆盖7个坡度+混合地形，每个方法的各坡度数据均有报告（未说明重复次数但推测多次）；消融实验对比了三个变体与两个基线。
- **深度噪声鲁棒性实验**：在30°楼梯上测试0%~200%噪声水平，绘制曲线（图7），对比完整模型、无噪声建模模型和Extreme Parkour。
- **真实世界实验**：每个楼梯10次试验（Table III），统计成功率。
- **充分性评价**：实验设计较为全面，覆盖了不同坡度、混合地形、噪声鲁棒性以及真实环境验证，并包含充分消融。但真实试验仅各10次，样本量较小；未在不同机器人平台上验证泛化性；未在更多楼梯类型（如不同材质、不同宽度）上测试。

## 六、论文的主要结论与发现
- **核心发现**：StairMaster首次实现了四足机器人在真实世界零样本迁移攀爬55°空心楼梯，成功率40%（37°时80%），而所有基线方法在55°楼梯上均完全失败。
- **消融结论**：
  - 无3D航点俯仰奖励（w/o \(r_{\text{pitch}}\)）导致碰撞次数显著增加，地形课程平均等级下降。
  - 无落脚点惩罚（w/o \(r_{\text{foothold}}\)）在混合地形上碰撞增多，成功率略低。
  - 无深度噪声建模（w/o depth noise）在200%噪声下仅完成7.3%台阶，而完整模型仍达99.8%，证明高保真噪声建模对零样本迁移至关重要。
- **视觉感知必要性**：纯本体感知方法（HIMLoco、内置RL）在空心楼梯上完全失败，凸显视觉/记忆对于稀疏地形的必要性。

## 七、优点
- **方法创新点**：
  - 首次将Cross-Attention与空间感知LSTM结合用于四足机器人攀爬场景，有效处理感知盲区。
  - 提出完整的高保真深度传感器噪声建模管线，包含多种真实伪影，显著缩小sim-to-real差距。
  - 引入3D航点主动感知奖励，使机器人主动调整俯仰角以提前观察地形，这是突破55°极限的关键。
- **实验设计亮点**：
  - 深度噪声鲁棒性实验系统改变噪声水平，直观展示稳定性提升。
  - 在模拟中统计碰撞次数（Table II），量化安全性能。
  - 真实世界对比了多种基线（包括商业内置策略），验证了实用性。
- **部署能力**：策略可实时运行于Jetson Orin NX上，实现零样本迁移，具备工程落地潜力。

## 八、不足与局限
- **实验覆盖局限**：
  - 真实环境仅测试37°和55°两种坡度，未在中低坡度（如20°、30°）上做系统真实对比。
  - 每个楼梯只进行了10次试验，统计稳定性不足；可能存在偶然性（例如55°成功率40%）。
  - 仅使用Unitree Go2一种机器人，未在不同型号（如宇树B2、四足大学等）上验证泛化性。
  - 未测试不同材质（如湿滑、积雪）或不同几何形态（如螺旋空心楼梯）的楼梯。
- **感知模态局限**：仅依赖深度图像，未融合RGB信息，也不具备语义理解（如区分台阶与空洞）。
- **奖励设计风险**：
  - 3D航点主动感知奖励依赖预定义的阈值 \(d_{\text{th}}\)，在不同地形下可能需手动调整。
  - 空心间隙惩罚需要预先定义间隙包围盒，场景扩展时需重新标注。
- **算力与效率**：未报告训练总时长，三阶段训练（教师+蒸馏+微调）可能耗时较长。
- **故障模式**：论文提到仍存在部分失败案例（如腿部卡住、侧滑），未分析失败的具体原因和比例。
- **迁移依赖**：高保真噪声建模需要精细调整参数以匹配真实传感器，可能在其他型号相机上需要重新标定。

（完）
