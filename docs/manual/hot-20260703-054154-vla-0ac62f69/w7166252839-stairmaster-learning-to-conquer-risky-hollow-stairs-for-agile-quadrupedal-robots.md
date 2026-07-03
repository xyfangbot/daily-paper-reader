---
title: "StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots"
title_zh: "StairMaster: 学习征服具有高风险空心楼梯的敏捷四足机器人"
authors: "X W Tang, Youhan Xie, Zhengjie Shu, Wanyu Li, Lai Jiang, Wenkang Hu, Yitong Li, Ruigang Yang"
date: 2026-06-24
pdf: "https://arxiv.org/pdf/2606.25765"
tags: ["query:热点论文筛选", "query:VLA方向", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=multimodal robot manipulation policy"
tldr: 四足机器人攀爬空心楼梯面临腿部卡陷、深度数据稀疏且噪声大等挑战。提出StairMaster三阶段强化学习框架，利用Cross-Attention提取结构特征、空间感知循环单元维护时空记忆，并构建高保真仿真传感器建模弥合虚实差距。在Unitree Go2上零样本迁移，首次实现55°陡峭空心楼梯攀爬，为极端地形运动提供新范式。
source: openalex
selection_source: hot_paper_scout
motivation: 空心楼梯因易卡腿、深度稀疏和传感器噪声大，现有方法难以稳定攀爬。
method: 三阶段RL框架集成Cross-Attention与SRU，辅以高保真深度传感器建模和主动感知奖励。
result: 在Unitree Go2上零样本迁移，成功攀爬55°空心楼梯，超越此前所有工作。
conclusion: 首次基于RL实现极限陡峭空心楼梯攀爬，为四足机器人极端地形运动开辟新路径。
---

## 摘要
对于四足机器人而言，攀登空心楼梯仍然是一个具有挑战性的问题，主要是因为腿部卡入的高风险、严重的深度稀疏性以及高频深度感知噪声。在本文中，我们提出了StairMaster，一种新颖的三阶段强化学习框架，用于在此类极端不连续地形上实现稳定运动。我们的架构集成了交叉注意力机制，从噪声深度数据中提取结构特征，以及一个空间感知循环单元（SRU），用于维持鲁棒的时空记忆以减轻感知盲点。为了弥合深度感知中的模拟到现实差距，我们提出了一种高保真度的模拟到现实深度传感器建模流程，能够忠实复制真实世界的传感器伪影。此外，我们采用了一种3D路标引导的主动感知奖励，以实现主动感知，同时结合空心间隙运动学与楼梯边缘惩罚，确保精确的落脚点放置。我们成功地将StairMaster部署在Unitree Go2机器人上，展示了其通过零样本迁移征服高达55度前所未有斜度的空心楼梯的能力。据我们所知，这是首个在现实环境中实现如此陡峭空心楼梯攀爬的基于强化学习的策略。项目网站：https://sivan666666.github.io/StairMaster/。

## Abstract
Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a Cross-Attention mechanism to extract structural features from noisy depth data, alongside a Spatial-aware Recurrent Unit (SRU) that maintains robust spatio-temporal memory to mitigate perception blind spots. To bridge the sim-to-real gap in depth perception, we propose a high-fidelity sim-to-real depth sensor modeling pipeline that faithfully replicates real-world sensor artifacts. Additionally, we employ a 3D waypoint-guided active perception reward for proactive sensing, alongside hollow gap kinematic and stair edge penalties to ensure precise foothold placement. We successfully deployed StairMaster on a Unitree Go2 robot, demonstrating its ability to conquer hollow stairs with an unprecedented incline of up to 55$^\circ$ through zero-shot transfer. To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments. Project Website: https://sivan666666.github.io/StairMaster/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：四足机器人在攀爬空心楼梯（如工业环境中无垂直立板、存在巨大物理间隙的楼梯）时，面临三大挑战：腿部卡入风险极高、深度传感器数据稀疏且噪声严重（因反射材料和振动）、以及前向摄像头视野有限导致后腿落脚区域完全被遮挡。
- **研究动机**：现有视觉-运动控制方法（如Extreme Parkour）在固体楼梯上表现良好，但在空心楼梯上因感知盲区、缺乏时空记忆、对深度噪声敏感而彻底失败。纯本体感觉方法（如HIMLoco）则因无法感知间隙而容易卡腿或钻入楼梯下方。
- **整体含义**：本文旨在提出首个基于强化学习的端到端框架，使四足机器人能够在极端陡峭（55°）的空心楼梯上实现稳定、零样本迁移的攀爬，推动四足机器人在工业设施等复杂地形中的应用。

## 二、论文提出的方法论
- **核心思想**：采用三阶段强化学习训练流程（教师策略→学生蒸馏→微调），结合空间感知的视觉编码器与定制奖励函数，解决空心楼梯的特殊挑战。
- **关键技术细节**：
  1. **三阶段训练管道**：
     - 第一阶段：使用具有特权高度图信息的PPO训练教师策略，获得专家行为。
     - 第二阶段：学生策略通过Cross-Attention融合深度图像与本体感觉，并通过Spatial-Aware LSTM（SRU）构建时空记忆，使用MSE蒸馏损失模仿教师动作。
     - 第三阶段：在仿真环境中用PPO微调学生策略，修正蒸馏带来的次优行为，得到最终策略用于零样本真实部署。
  2. **视觉-空间编码器**：
     - **Cross-Attention**：以本体感觉嵌入为查询（Query），深度图像CNN特征为键值（Key-Value），动态聚焦于与当前运动姿态最相关的稀疏几何结构（如楼梯边缘）。
     - **Spatial-Aware LSTM (SRU)**：引入可学习的空间变换门 \( s_t = \sigma(W_s f_t + b_s) \)，对前一时刻的隐藏状态和单元状态进行逐元素变换（\( h_{t-1} \odot s_t, c_{t-1} \odot s_t \)），再输入标准LSTM，实现坐标系对齐的时空记忆，从而在完全遮挡时仍能推断后方楼梯位置。
  3. **高保真深度传感器建模**：
     - 在仿真深度图像上依次添加：高斯/均匀噪声、空洞噪声（随机像素丢失）、边缘噪声（模拟深度不连续处的散射）、立体匹配噪声（量化/匹配误差）、高斯偏移（模拟振动引起的像素随机位移）。最后统一裁剪、缩放、高斯模糊，使仿真深度与真实深度分布对齐。
  4. **定制奖励函数**：
     - **3D路标主动感知奖励 \( r_{\text{pitch}} \)**：基于机器人到第二个未来楼梯中心的距离，计算目标俯仰角偏差惩罚。只有当距离小于阈值 \( d_{\text{th}} \) 时才激活，引导机器人提前抬头使摄像头捕获远处楼梯结构，同时优化质心分布。
     - **空心间隙运动学惩罚 \( r_{\text{hollow}} \)**：若任一脚部落入预定义的空心间隙边界框，则施加大的负奖励 \( -c_{\text{hollow}} \)，强制生成高而安全的摆动轨迹。
     - **楼梯边缘惩罚 \( r_{\text{edge}} \)**：若脚部落点距离楼梯边缘小于安全阈值 \( d_{\text{safe}} \)，则施加惩罚 \( -c_{\text{edge}} \)，鼓励落脚于楼梯中心。

## 三、实验设计
- **仿真环境**：Isaac Gym仿真器，构建了从平地到55°斜坡的空心楼梯地形，并采用课程学习逐步增加难度（增加台阶高度、减小踏面深度和宽度、注入随机间隙噪声）。
- **真实平台**：Unitree Go2四足机器人，搭载Intel RealSense D435深度相机（10Hz），板载NVIDIA Jetson Orin NX计算模块，控制频率50Hz，PD参数 \( K_p=40, K_d=1 \)。
- **对比方法**：
  - Extreme Parkour：两阶段视觉跑酷框架（重新在空心楼梯地形上训练）。
  - HIMLoco：基于混合内模型的盲走策略。
  - 自身消融变体：Ours w/o \( r_{\text{pitch}} \)（无俯仰奖励）、Ours w/o \( r_{\text{foothold}} \)（无空心间隙和边缘惩罚）、Ours w/o depth noise（无深度噪声建模）。
- **评估指标**：成功率（Success Rate，到达顶部路标比例）、平均到达步数百分比（Average Reached Steps %）、平均碰撞次数（Average Collisions）。
- **测试场景**：仿真中测试平地、20°~55°空心楼梯、混合随机楼梯；真实世界测试37°和55°空心楼梯，各进行10次重复试验。

## 四、资源与算力
- **训练硬件**：单块NVIDIA RTX 4090 GPU（用于仿真训练）。
- **训练时间**：论文未明确给出训练时长（例如迭代次数、具体时间）。仅提到在Isaac Gym中训练，使用单GPU。
- **算力总结**：仅提及使用单GPU进行训练，未详述具体训练时长或并行规模。

## 五、实验数量与充分性
- **实验组数**：
  - 仿真对比实验：包含5种方法（Ours全量、两种消融、两个基线）在6种难度（20°-55°+混合）上的成功率和平均步骤，共约30组数据（表I）。
  - 平均碰撞次数消融（表II）：4种方法在6种地形上的结果，共24组。
  - 深度噪声鲁棒性测试（图7）：3种方法（Ours、Ours w/o depth noise、Extreme Parkour）在7种噪声水平（0%-200%）下的平均步骤。
  - 真实世界实验（表III）：6种方法在2种楼梯上的成功率，共12组（各10次试验）。
- **充分性与公平性**：
  - 充分：涵盖了主对比、消融、噪声鲁棒性、真实部署，验证了各模块必要性。
  - 公平：对比方法均在相同空心楼梯地形上重新训练，但保留了其原始奖励设置；消融严格控制变量。
  - 局限：真实世界每组仅10次试验，统计显著性有限；未在更多机器人型号或更多楼梯角度上测试；仿真中混合楼梯的随机范围可能不够全面。

## 六、论文的主要结论与发现
- 首次基于强化学习实现了四足机器人在现实环境中的55°空心楼梯攀爬（零样本迁移），成功率40%。
- 纯本体感觉方法（HIMLoco）在所有空心楼梯上完全失败，证明视觉感知不可或缺。
- Extreme Parkour等现有视觉方法因缺乏时空记忆和主动感知，在陡峭空心楼梯上成功率几乎为0。
- 消融实验证实：主动感知俯仰奖励（\( r_{\text{pitch}} \)）显著提升地形等级和减少碰撞；落脚点惩罚（\( r_{\text{hollow}} + r_{\text{edge}} \)）提高样本效率和着陆精度；深度噪声建模是零样本迁移的关键，200%噪声下全量方法仍完成99.8%步骤，而无噪声建模的变体仅完成7.3%。
- 真实世界37°楼梯成功率80%，55°楼梯40%，Built-in RL（盲走）在55°完全失败。

## 七、优点
- **创新性框架**：三阶段训练（教师-蒸馏-微调）结合了特权信息、模仿学习和交互式强化学习，兼顾专家知识与环境探索。
- **鲁棒的时空记忆**：Spatial-Aware LSTM通过可学习空间变换门隐式对齐不同时刻的视觉特征，在无显式里程计时仍能维持全局地形记忆，有效应对前向摄像头盲区。
- **高保真深度噪声建模**：系统性地模拟了静态和动态噪声（振动、匹配误差、边缘效应等），显著缩小了仿真与真实间的视觉域差距，实现零样本部署。
- **定制奖励设计**：3D路标主动感知奖励迫使机器人主动调整俯仰角以提前获取视觉信息，而空心间隙和边缘惩罚直接针对空心楼梯的关键失败模式，提升了安全性。
- **实验全面**：仿真和真实实验相结合，消融实验验证了每个组件的贡献，深度噪声鲁棒性测试展示了强泛化能力。

## 八、不足与局限
- **真实世界成功率较低**：55°楼梯仅40%，可能受限于单次试验随机性、硬件抖动或光照变化，鲁棒性有待进一步提高。
- **实验覆盖有限**：仅在Unitree Go2上测试；楼梯角度仅37°和55°；地形种类单一（未涉及转弯、多平台衔接等复杂场景）；样本量（每组10次）较小。
- **感知模态单一**：仅使用深度图像，未利用RGB信息或更广视野的传感器，可能在某些光照或纹理条件下受限。
- **缺乏与最新方法的完整对比**：未与PLANC等近期三阶段框架对比，也未与使用LiDAR或立体视觉的模块化方法对比。
- **计算与延迟分析缺失**：未报告板载推理延迟、功耗或算力占用，影响实际部署可行性评估。
- **依赖仿真保真度**：当前深度噪声建模仍为手工设计，未使用GAN或真实数据分布学习，可能在高动态场景下仍有残差。论文也指出未来需改进电机建模。

（完）
