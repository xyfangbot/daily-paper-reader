---
title: "StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots"
title_zh: StairMaster：学习征服危险空心楼梯的敏捷四足机器人
authors: "X W Tang, Youhan Xie, Zhengjie Shu, Wanyu Li, Lai Jiang, Wenkang Hu, Yitong Li, Ruigang Yang"
date: 2026-06-24
pdf: "https://arxiv.org/pdf/2606.25765"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=humanoid robot policy"
tldr: 四足机器人攀爬空心楼梯面临腿部卡住、深度数据稀疏与高频噪声等挑战。本文提出StairMaster三阶段强化学习框架，通过Cross-Attention提取结构特征、空间感知循环单元维持鲁棒时空记忆，并设计高保真深度传感器建模缩小虚实差距。结合3D航点主动感知奖励与空心间隙运动学惩罚，在Unitree Go2上零样本迁移实现55°陡峭空心楼梯攀爬，为首次基于RL达成此难度。
source: openalex
selection_source: hot_paper_scout
motivation: 解决四足机器人在空心楼梯等极端不连续地形上稳定运动难题，防止腿部陷入和感知盲区导致的失稳。
method: 三阶段强化学习框架：Cross-Attention融合噪声深度特征，SRU维护时空记忆；高保真深度传感器建模、主动感知奖励及运动学惩罚实现精准落足。
result: 在Unitree Go2机器人上零样本迁移，成功攀爬55°空心楼梯，达到业内最高坡度。
conclusion: 所提框架有效克服感知噪声与地形不连续性，为四足机器人攀登极端阶梯提供可行方案。
---

## 摘要
由于腿部卡住的高风险、深度稀疏严重以及高频深度感知噪声，攀登空心楼梯对于四足机器人仍是一个具有挑战性的问题。在本文中，我们提出StairMaster，一种新颖的三阶段强化学习框架，用于在此类极端不连续地形上实现稳定运动。我们的架构集成了交叉注意力机制，以从噪声深度数据中提取结构特征，并结合空间感知循环单元（SRU），该单元保持稳健的时空记忆以减轻感知盲点。为了弥合深度感知中的仿真到现实差距，我们提出了一种高保真的仿真到现实深度传感器建模流水线，能够忠实地复现真实世界的传感器伪影。此外，我们采用3D航点引导的主动感知奖励来实现主动感知，同时结合空心间隙运动学和楼梯边缘惩罚以确保精确的落脚点放置。我们成功将StairMaster部署在Unitree Go2机器人上，通过零样本迁移展示了其征服倾斜度高达55°的空心楼梯的能力。据我们所知，这是首个在真实环境中实现如此陡峭空心楼梯攀爬的基于强化学习的策略。项目网站：https://sivan666666.github.io/StairMaster/。

## Abstract
Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a Cross-Attention mechanism to extract structural features from noisy depth data, alongside a Spatial-aware Recurrent Unit (SRU) that maintains robust spatio-temporal memory to mitigate perception blind spots. To bridge the sim-to-real gap in depth perception, we propose a high-fidelity sim-to-real depth sensor modeling pipeline that faithfully replicates real-world sensor artifacts. Additionally, we employ a 3D waypoint-guided active perception reward for proactive sensing, alongside hollow gap kinematic and stair edge penalties to ensure precise foothold placement. We successfully deployed StairMaster on a Unitree Go2 robot, demonstrating its ability to conquer hollow stairs with an unprecedented incline of up to 55$^\circ$ through zero-shot transfer. To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments. Project Website: https://sivan666666.github.io/StairMaster/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：四足机器人在攀爬空心楼梯（无竖直踢脚板、踏板之间存在大间隙）时面临三大挑战：1) 腿部极易卡入空心间隙导致硬件损坏；2) 反射/格栅材质导致深度相机像素大面积缺失和极端噪声；3) 前向摄像头视野有限，踏板在机器人经过后完全消失，造成后腿在视觉盲区下的精确落足困难。
- **研究动机**：现有视觉-运动控制框架（如 Extreme Parkour、HIMLoco）难以应对实际部署中的深度传感器噪声、剧烈姿态变化引起的振动噪声以及长期视觉盲区；且缺乏主动感知能力，无法提前调整俯仰角观察前方楼梯。
- **整体含义**：本文旨在提出一个端到端强化学习框架，使四足机器人能够在极端不连续地形（空心楼梯）上实现稳定、敏捷的运动，并首次通过零样本迁移在真实环境中成功攀爬55°陡峭空心楼梯。

## 二、论文提出的方法论
- **整体框架**：StairMaster 采用三阶段训练流水线：
  1. **阶段一（特权教师策略训练）**：使用 PPO 算法，教师网络可访问特权高度图与本体感觉，利用定制奖励函数学习专家行为。
  2. **阶段二（学生策略蒸馏）**：学生网络仅依赖噪声深度图像和本体感觉，通过 MSE 损失模仿教师动作。学生网络集成 Cross-Attention 机制融合深度与本体特征，以及 Spatial-Aware LSTM（SRU）维持时空记忆，同时采用高保真深度噪声建模。
  3. **阶段三（微调）**：在仿真环境中通过 PPO 进一步优化学生策略，弥补蒸馏性能差距，最终输出目标关节角度用于零样本真实部署。
- **关键技术细节**：
  - **Visuospatial Encoder**：包含 Cross-Attention（以本体感觉嵌入为查询，深度CNN特征为键/值，动态关注任务相关几何结构）和 SRU（通过可学习空间门控隐式对齐历史记忆与当前视角，维护时空记忆）。
  - **高保真深度噪声建模**：包括高斯/均匀噪声、空洞噪声（随机像素缺失）、边缘噪声、立体匹配噪声、高斯偏移（模拟振动位移），以及统一预处理（裁剪、值裁剪、缩放、高斯模糊）。
  - **定制奖励函数**：
    - 3D航点引导主动感知奖励（$r_{\text{pitch}}$）：基于距离阈值激活，通过目标航点同时监督偏航和俯仰角，促使机器人提前抬头观察。
    - 空心间隙运动学惩罚（$r_{\text{hollow}}$）：当足端进入预定义空心区域时施加硬性惩罚，避免腿部卡入。
    - 楼梯边缘惩罚（$r_{\text{edge}}$）：落足点距踏板边缘小于安全阈值时施加惩罚，鼓励踩踏踏板中央。
- **训练细节**：地形课程（坡度从0°渐进至55°，注入随机噪声），领域随机化（摩擦、质量、电机强度、外力、动作延迟、相机参数等）。

## 三、实验设计
- **仿真环境**：基于 Isaac Gym，评估三种地形：平坦地面、标准化空心楼梯（20°–55°）、随机混合楼梯（随机步高和水平间隙）。
- **对比方法**：
  - Extreme Parkour（两阶段视觉-教师-学生架构）
  - HIMLoco（基于混合内模型的盲运动策略）
  - 内置MPC（Unitree Go2自带）
  - 内置RL（Unitree盲运动策略）
  - 本文消融版本（移除$r_{\text{pitch}}$、移除$r_{\text{foothold}}$（即$r_{\text{hollow}}+r_{\text{edge}}$）、移除深度噪声建模）
- **评估指标**：
  - **成功率**：机器人成功到达顶部航点的平均百分比。
  - **平均到达步数（%）**：成功穿越的踏板数量占总踏板数的百分比。
  - **碰撞次数**（消融实验）。
- **噪声鲁棒性测试**：在30°空心楼梯上注入0%–200%的额外噪声，比较 Ours、Ours w/o depth noise、Extreme Parkour。
- **真实世界实验**：在Unitree Go2机器人上，使用Intel RealSense D435深度相机（10Hz），Jetson Orin NX机载计算（控制频率50Hz）。测试37°和55°两座空心楼梯，每种策略各跑10次试验。

## 四、资源与算力
- **训练硬件**：单张NVIDIA RTX 4090 GPU，在Isaac Gym仿真器中训练。
- **训练时长**：论文未明确给出总训练时间，只提到策略在仿真中训练至收敛。
- **部署算力**：机载平台为NVIDIA Jetson Orin NX计算模块。

## 五、实验数量与充分性
- **仿真实验**：
  - 在主对比实验（表I）中，对6种方法在7种地形（平坦+5种坡度+混合）上评估，每种条件未明确重复次数，但通常PPO训练中多次随机种子的平均结果。消融实验（表II）记录了平均碰撞次数。
  - 噪声鲁棒性实验（图7）在多个噪声水平下对比3种方法。
  - 训练过程中的地形等级曲线（图6）展示了奖励项对收敛的影响。
- **真实世界实验**：
  - 2种楼梯坡度，每种方法各10次试验（表III），共6种方法×2坡度×10次=120次试验。其中Ours全版本在37°和55°上的试验次数分别为10次。
- **充分性评价**：仿真实验覆盖了多坡度、混合地形、噪声鲁棒性，消融实验完整，对比基线合理。但真实世界试验次数较少（每条件10次），可能受随机因素影响较大，统计显著性有限。此外，未与PLANC等最新多阶段框架对比，但PLANC针对人形机器人，对比可能不完全公平。

## 六、论文的主要结论与发现
- 本文提出的三阶段强化学习框架StairMaster能够通过零样本迁移使Unitree Go2机器人成功攀爬55°空心楼梯，为首次基于RL实现此难度。
- 相比盲策略（HIMLoco、内置RL）和现有视觉策略（Extreme Parkour），StairMaster在空心楼梯上显著提升成功率和步数穿透率，有效避免腿部卡住和碰撞。
- Cross-Attention与SRU的结合有效克服了视觉盲区，在踏板消失在视野后仍能维持稳定的落足。
- 高保真深度噪声建模对真实世界迁移至关重要：移除后成功率从80%/40%降至40%/10%（37°/55°）。
- 定制奖励函数（$r_{\text{pitch}}$、$r_{\text{foothold}}$）显著减少碰撞次数，提升训练效率。

## 七、优点
- **方法创新性**：首次针对空心楼梯的极端几何与感知挑战设计专门的三阶段RL框架，整合了Cross-Attention、SRU、高保真深度噪声建模。
- **主动感知机制**：3D航点引导的俯仰奖励让机器人“主动抬头”，提前观察楼梯结构，而非被动反应。
- **高保真噪声建模**：不仅模拟静态噪声，还模拟动态振动位移，显著缩小sim-to-real差距，实现零样本迁移。
- **奖励设计**：针对腿部卡住和边缘滑落设计硬惩罚，有效防止灾难性故障。
- **实验完整性**：在仿真中进行了多角度对比、消融和噪声鲁棒性测试，真实世界成功展示了目前最高坡度（55°）的空心楼梯攀爬。

## 八、不足与局限
- **真实世界实验规模较小**：每个场景仅10次试验，样本量不足以进行严格的统计分析，可能存在偶然性。
- **泛化性未充分验证**：仅在Unitree Go2一种机器人平台上测试，未在其他型号或重量级四足机器人上验证，且楼梯类型仅限于金属格栅/反射材质。
- **对比基线选择**：未对比PLANC等近期多阶段视觉框架（尽管其针对人形），且未与Blind policy（如HIMLoco）在真实世界进行广泛对比（仅在仿真中对比）。
- **未融合RGB信息**：仅依赖深度图像，未来工作提到可集成RGB增强环境感知，当前方法在光照极端变化下可能鲁棒性不足。
- **算力与训练细节欠缺**：未报告训练总时长、GPU利用率、超参数敏感性分析，不利于复现。
- **长期稳定性未知**：实验仅为单次爬升（约4-5个踏板），未测试多次连续攀爬或多楼层场景下的表现。
- **网格/反光材质假设**：深度噪声建模针对特定材质设计，若楼梯材质不同（如透明或吸光）可能失效。

（完）
