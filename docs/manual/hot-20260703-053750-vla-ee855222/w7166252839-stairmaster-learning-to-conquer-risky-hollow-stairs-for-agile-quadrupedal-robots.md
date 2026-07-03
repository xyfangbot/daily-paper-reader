---
title: "StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots"
title_zh: StairMaster：学习征服危险空心楼梯的敏捷四足机器人
authors: "X W Tang, Youhan Xie, Zhengjie Shu, Wanyu Li, Lai Jiang, Wenkang Hu, Yitong Li, Ruigang Yang"
date: 2026-06-24
pdf: "https://arxiv.org/pdf/2606.25765"
tags: ["query:热点论文筛选", "query:VLA方向", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=multimodal robot manipulation policy"
tldr: 四足机器人攀爬镂空楼梯面临腿卡陷、深度稀疏和深度噪声等严峻挑战。本文提出StairMaster，一种三阶段强化学习框架，通过交叉注意力提取噪声深度结构特征、空间感知循环单元维持鲁棒时空记忆，并引入高保真深度传感器建模弥合仿真-现实差距。在Unitree Go2上零样本迁移实现史无前例的55°陡峭镂空楼梯攀爬，为首个在真实环境中完成该任务的基于强化学习的策略。
source: openalex
selection_source: hot_paper_scout
motivation: 解决四足机器人在极端不连续镂空楼梯上稳定运动时面临的腿卡陷风险、深度传感器数据稀疏与高频噪声难题。
method: 提出三阶段强化学习框架StairMaster，集成交叉注意力机制与空间感知循环单元，结合高保真深度传感器建模、3D路点引导主动感知奖励及镂空间隙运动学惩罚。
result: 在Unitree Go2机器人上零样本迁移，成功攀爬倾斜度高达55°的镂空楼梯，为首个在真实环境中实现此目标的强化学习方法。
conclusion: 所提框架通过感知与记忆增强、仿真-现实深度对齐及主动奖励设计，显著提升了四足机器人在极端地形上的攀爬能力。
---

## 摘要
由于腿部卡住的高风险、深度稀疏性严重以及高频深度感知噪声，四足机器人攀爬空心楼梯仍然是一个具有挑战性的问题。本文提出StairMaster，一种新颖的三阶段强化学习框架，用于在此类极端不连续地形上实现稳定运动。我们的架构集成了交叉注意力机制，可从噪声深度数据中提取结构特征，同时配备了空间感知循环单元（SRU），该单元维持稳健的时空记忆以减轻感知盲区。为弥合深度感知的仿真到现实差距，我们提出了一种高保真度的仿真到现实深度传感器建模流程，该流程忠实地复制了真实世界传感器的伪影。此外，我们采用3D航点引导的主动感知奖励进行主动感测，并结合空心间隙运动学与楼梯边缘惩罚以确保精确的落脚点。我们成功将StairMaster部署在Unitree Go2机器人上，通过零样本迁移展示了其征服坡度高达55度的空心楼梯的能力。据我们所知，这是首个在真实环境中实现如此陡峭空心楼梯攀爬的基于强化学习的策略。项目网站：https://sivan666666.github.io/StairMaster/。

## Abstract
Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a Cross-Attention mechanism to extract structural features from noisy depth data, alongside a Spatial-aware Recurrent Unit (SRU) that maintains robust spatio-temporal memory to mitigate perception blind spots. To bridge the sim-to-real gap in depth perception, we propose a high-fidelity sim-to-real depth sensor modeling pipeline that faithfully replicates real-world sensor artifacts. Additionally, we employ a 3D waypoint-guided active perception reward for proactive sensing, alongside hollow gap kinematic and stair edge penalties to ensure precise foothold placement. We successfully deployed StairMaster on a Unitree Go2 robot, demonstrating its ability to conquer hollow stairs with an unprecedented incline of up to 55$^\circ$ through zero-shot transfer. To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments. Project Website: https://sivan666666.github.io/StairMaster/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：四足机器人在工业场景（如电厂、建筑工地）中常遇到镂空楼梯，这种楼梯没有垂直踢面，踏板之间存在巨大空隙。机器人爬行面临三大挑战：
  1. **腿部卡陷风险**：即使微小的落脚点误差也会导致腿插入空隙，造成硬件损坏。
  2. **深度感知严重退化**：材料反射或格栅结构导致深度相机像素缺失和极端噪声；剧烈姿态变化引起的振动进一步恶化深度数据质量。
  3. **视觉盲区**：前视摄像头视野有限，踏板在机器人经过后完全消失，导致后腿必须在完全遮挡下执行极端精准的落脚。
- **研究背景**：现有视觉-运动控制框架（如Extreme Parkour、PIE等）难以应对上述复合挑战，主要失败原因包括：对传感器噪声鲁棒性差、缺乏时空记忆以维持稀疏地形的空间连通性、缺乏主动视觉感知能力、未显式处理垂直和水平大间隙导致的可行落点稀缺。
- **整体含义**：该论文提出首个能在真实环境中实现高达55°陡峭镂空楼梯攀爬的强化学习策略，解决了四足机器人在极端不连续地形上的感知、记忆与控制协同难题。

## 二、论文提出的方法论
- **核心思想**：提出StairMaster，一个**三阶段端到端强化学习框架**，从原始深度图像和本体感受直接生成联合角度指令，专门针对镂空楼梯的独特挑战设计。
- **关键技术细节**：
  1. **三阶段训练流水线**：
     - 阶段1（特权教师策略训练）：使用PPO算法，教师策略有权访问本体感受和特权高度图，利用定制奖励函数训练专家行为。
     - 阶段2（学生策略蒸馏）：学生策略仅依赖有噪声的深度图像和本体感受，通过交叉注意力机制融合多模态特征，并使用空间感知LSTM（SRU）维护时空记忆，同时引入高保真仿真-现实深度噪声建模。
     - 阶段3（微调）：使用PPO对学生策略进行强化学习微调，纠正蒸馏带来的次优行为。
  2. **视觉空间编码器架构**：
     - **交叉注意力机制**：将本体感受嵌入作为查询，CNN提取的深度特征图作为键和值，动态聚焦与当前运动相关的结构特征（如稀疏楼梯边缘）。
     - **空间感知LSTM（SRU）**：引入可学习的空间变换门\(s_t = \sigma(W_s f_t + b_s)\)，与前一隐藏状态和单元状态逐元素相乘，隐式对齐历史记忆与当前视角，构建全尺度时空记忆缓冲区，从而推断完全遮挡下的三维踏板位置。
  3. **高保真深度噪声建模**：
     - 模拟真实传感器伪影：高斯噪声、均匀噪声、孔洞噪声（模拟反射表面像素丢失）、边缘噪声（模拟深度不连续的模糊效应）。
     - 动态噪声：立体匹配噪声（模拟运动模糊导致的匹配歧义）、高斯偏移（模拟冲击振动导致像素空间抖动）。
     - 预处理统一：裁剪、深度值裁剪、空间缩放、高斯模糊。
  4. **定制化奖励函数**：
     - **3D路点引导主动感知奖励（\(r_{pitch}\)）**：以第二个即将到来的踏板中心为3D路点，同时监督偏航角和俯仰角。当机器人距离路点小于阈值\(d_{th}\)时，惩罚当前俯仰与目标俯仰的偏差。作用：优化运动学（主动抬头有利于重心分布和后腿迈过）和主动感知（提前捕获远距离踏板结构）。
     - **镂空间隙运动学惩罚（\(r_{hollow}\)）**：若任一足轨迹进入预定义的空隙包围盒，施加硬惩罚\(-c_{hollow}\)，强制高抬腿完全越过间隙。
     - **楼梯边缘惩罚（\(r_{edge}\)）**：若落脚点距踏板边缘小于安全裕度\(d_{safe}\)，施加惩罚，鼓励朝向踏板中心落足。
- **训练细节**：
  - **地形课程**：从平地（0°）开始，逐步增加台阶高度、减小踏板深度和宽度，最终达到55°；注入随机垂直高程和水平间隙噪声防止记忆步态。
  - **域随机化**：扰动摩擦、质量、电机强度、外部推力、动作延迟、深度相机视场角和安装位姿。

## 三、实验设计
- **实验场景与数据集**：
  - 仿真环境：Isaac Gym，包含三种地形：平地基线、标准镂空楼梯（20°~55°）、随机混合楼梯（随机台阶高度和水平间隙）。
  - 真实环境：Unitree Go2机器人，Intel RealSense D435深度相机（10Hz），机载NVIDIA Jetson Orin NX计算模块。真实楼梯坡度37°和55°。
- **Benchmark与对比方法**：
  1. **Extreme Parkour**：两阶段教师-学生蒸馏视觉框架。
  2. **HIMLoco**：基于混合内部模型的盲运动策略。
  3. **消融变体**：Ours w/o \(r_{pitch}\)（无主动感知奖励）、Ours w/o \(r_{foothold}\)（无镂空惩罚和边缘惩罚）、Ours w/o depth noise（无深度噪声建模）。
  4. **真实实验额外对比**：Built-in MPC（机器人内置模型预测控制）和Built-in RL（优必选盲RL策略）。
- **评估指标**：
  - **成功率**：成功到达顶部路点的试验百分比。
  - **平均到达步数（%）**：成功越过踏板中心的平均百分比。
  - **平均碰撞次数**（仅消融实验）。

## 四、资源与算力
- 论文明确提及：训练在单个**NVIDIA RTX 4090 GPU**上进行，未提及具体训练时长（小时/天数）。但提到使用Isaac Gym仿真器进行大规模并行训练，典型的四足机器人RL训练通常需要数小时至数天，具体时长未给出。

## 五、实验数量与充分性
- **仿真实验**：
  - 主对比实验在6种坡度（0°、20°、30°、40°、50°、55°）和混合地形上评估成功率和平均到达步数。
  - 消融实验：分别移除\(r_{pitch}\)、\(r_{foothold}\)、深度噪声建模，在同一套地形上对比。
  - 额外噪声鲁棒性实验：在30°镂空楼梯上注入0%~200%的人工深度噪声，对比3种方法。
- **真实实验**：
  - 每种方法在37°和55°楼梯上各进行10次连续试验（根据描述推测，具体试验次数未明说，但表III给出的成功率表明至少10次每条件）。
  - 对比方法包括6种，覆盖自身消融、已有SOTA、基线。
- **充分性评估**：
  - 仿真实验覆盖了多种坡度、混合地形、噪声等级，消融设计完整，能够验证各组件贡献。
  - 真实实验对比充分，但试验次数可能偏少（仅10次），统计显著性未报告；未见泛化性测试（不同机器人个体、不同环境光照等）。总体而言，实验设计比较客观、公平，但结论外推需谨慎。

## 六、论文的主要结论与发现
- 在仿真中，StairMaster在55°镂空楼梯上达到**97.5%成功率**，在混合地形上达**86.5%**，远优于Extreme Parkour（0%）和HIMLoco（0%）。
- 消融实验证实：\(r_{pitch}\)明显提升地形平均等级和降低碰撞次数；\(r_{foothold}\)降低混合地形碰撞；深度噪声建模极大提升对极端噪声（200%）的鲁棒性（平均到达步数99.8% vs 无建模的7.3%）。
- 真实世界：StairMaster在37°楼梯上成功率**80%**，55°楼梯上**40%**，而Built-in RL仅在37°上成功70%，55°完全失败；其他基线全部为0%。
- 视觉时空记忆和主动感知是克服遮挡和稀疏地形的关键；高保真噪声建模是零样本迁移的必备条件。

## 七、优点
- **方法创新性**：
  - 首次将空间感知LSTM（SRU）引入四足机器人攀爬任务，隐式对齐时空特征，解决盲区记忆问题。
  - 3D路点主动感知奖励同时优化运动学和视觉感知策略，是一种隐式主动视觉机制。
  - 高保真深度噪声建模涵盖静态和动态噪声（振动偏移），有效缩小仿真-现实差距。
- **实验充分性**：
  - 消融实验覆盖所有关键组件（奖励、噪声建模），验证每个设计的必要性。
  - 在极端噪声（200%）下对比，凸显鲁棒性。
- **实际应用价值**：首个在真实55°镂空楼梯上成功的RL策略，代码和视频已公开，具有工程意义。

## 八、不足与局限
- **实验覆盖**：
  - 真实试验次数较少（每条件10次？），未提供统计置信区间，可能存在随机波动。
  - 只测试了Unitree Go2一个平台，未验证在不同尺寸/形态机器人上的泛化性。
  - 未考虑楼梯磨损、湿度、不同材料（如带水表面）等实际噪声变化。
- **方法限制**：
  - 三阶段训练流程较为复杂，训练时间可能较长（未报告具体时长）。
  - 依赖深度相机，在强光照或透明/镜面材料上可能失败；论文虽提出噪声建模，但未测试完全透明或镜面台阶。
  - 仅感知前向深度，未利用RGB信息（论文未来方向提及），可能错过颜色/纹理线索。
- **偏差风险**：使用Isaac Gym仿真，地形课程和域随机化设定可能偏向特定楼梯几何形态，真实环境多样化不足。

---

（完）
