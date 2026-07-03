---
title: "StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots"
authors: "X W Tang, Youhan Xie, Zhengjie Shu, Wanyu Li, Lai Jiang, Wenkang Hu, Yitong Li, Ruigang Yang"
date: 2026-06-24
pdf: "https://arxiv.org/pdf/2606.25765"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 四足机器人攀爬空心楼梯面临腿卡陷、深度稀疏和感知噪声等挑战。本文提出StairMaster，一个三阶段强化学习框架，集成Cross-Attention机制提取结构特征，并引入Spatial-aware Recurrent Unit维持鲁棒时空记忆以缓解感知盲区。通过高保真深度传感器建模缩小仿真与现实差距，结合3D路点主动感知奖励与空心底层几何惩罚实现精确落脚。零样本迁移至Unitree Go2，成功攀爬55°倾斜空心楼梯，为同类任务首个RL策略。
source: openalex
selection_source: hot_paper_scout
motivation: 克服空心楼梯因腿部易卡陷、深度信息稀疏且噪声大导致的四足机器人运动不稳定性。
method: 三阶段强化学习框架，融合Cross-Attention与SRU处理深度数据，采用高保真传感器建模及主动感知奖励与几何惩罚。
result: 在Unitree Go2上零样本迁移，首次以RL策略攀爬55°空心楼梯，超越现有方法。
conclusion: 证明了仿真训练策略可鲁棒部署于真实极端不连续地形，显著拓展四足机器人攀爬能力。
---

## Abstract
Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a Cross-Attention mechanism to extract structural features from noisy depth data, alongside a Spatial-aware Recurrent Unit (SRU) that maintains robust spatio-temporal memory to mitigate perception blind spots. To bridge the sim-to-real gap in depth perception, we propose a high-fidelity sim-to-real depth sensor modeling pipeline that faithfully replicates real-world sensor artifacts. Additionally, we employ a 3D waypoint-guided active perception reward for proactive sensing, alongside hollow gap kinematic and stair edge penalties to ensure precise foothold placement. We successfully deployed StairMaster on a Unitree Go2 robot, demonstrating its ability to conquer hollow stairs with an unprecedented incline of up to 55$^\circ$ through zero-shot transfer. To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments. Project Website: https://sivan666666.github.io/StairMaster/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- 四足机器人攀爬空心楼梯面临三大核心挑战：腿部极易卡入踏板间的空心间隙、深度感知严重稀疏（反射/格栅材料导致像素丢失和极端噪声）、以及因前向相机视野有限导致的视觉盲区（踏板在机器人经过其下方时完全消失）。
- 现有视觉-运动控制框架在处理上述复合困难时表现不佳：无法应对剧烈姿态变化引起的深度传感器噪声、缺乏维持空间连续性的时空记忆、且缺乏主动调整俯仰角来提前观察地形的能力。
- 本文提出 StairMaster，一个专为高风险空心楼梯设计的三阶段强化学习框架，目标是实现从仿真到真实世界的零样本迁移，首次让四足机器人实际攀爬倾斜角达 55° 的空心楼梯。

## 二、论文提出的方法论

- 三阶段训练流水线：
  1. **第一阶段（特权教师策略训练）**：使用 PPO 算法，教师网络可访问本体感知状态（角速度、重力向量、速度指令、关节位置/速度、上一动作）以及特权高度图。利用自定义奖励函数训练出专家策略。
  2. **第二阶段（学生策略蒸馏）**：学生网络仅依赖含噪声的深度图像和本体感知，通过 MSE 损失模仿教师策略的动作。学生网络集成：
     - **Cross-Attention 机制**：将本体感知嵌入作为 Query，深度图像 CNN 特征作为 Keys/Values，动态聚焦于与当前位姿相关的结构特征（如稀疏楼梯边缘）。
     - **空间感知 LSTM（SRU）**：通过可学习空间门控对历史隐藏状态和细胞状态进行空间对齐，隐式注册连续帧的表示，构建时空记忆以弥补视觉盲区。
     - **高保真仿真到现实深度噪声建模**：包括高斯/均匀噪声、孔洞噪声、边缘噪声、立体匹配噪声、以及因冲击振动导致的高斯偏移噪声，并统一预处理（裁剪、缩放、高斯模糊）。
  3. **第三阶段（微调）**：使用 PPO 算法与环境交互微调学生网络，纠正蒸馏导致的次优行为，输出最终关节角度指令。

- 自定义奖励函数（针对空心楼梯）：
  - **3D 路点主动感知奖励 (r_pitch)**：以第二个即将踏上的踏板中心为 3D 路点，通过距离激活阈值控制，仅当机器人距路点足够近时，惩罚当前俯仰角与目标俯仰角的偏差，从而促使机器人提前仰头观察前方地形，同时优化重心分布。
  - **空心间隙运动学惩罚 (r_hollow)**：如果任何一只脚进入预定义的空心区域边界框，施加固定负奖励，迫使安全高摆腿轨迹。
  - **楼梯边缘惩罚 (r_edge)**：如果落足点距踏板边缘小于安全阈值，施加固定负奖励，鼓励落脚于踏板中心。

- 训练细节：采用地形课程（从平地逐渐增至 55° 倾斜，并注入随机高度和水平间隙噪声）、全面域随机化（摩擦、质量、电机强度、外力推、动作延迟、相机内参等）。

## 三、实验设计

- 训练环境：Isaac Gym 仿真器。
- 真实硬件：Unitree Go2 四足机器人，搭载 Intel RealSense D435 深度相机（10 Hz）、NVIDIA Jetson Orin NX 计算模块（50 Hz 控制频率，PD 控制器 Kp=40, Kd=1）。
- 对比基线：
  - Extreme Parkour（两阶段视觉 parkour 框架）
  - HIMLoco（纯本体感知盲策略）
  - Ours w/o r_pitch（去掉俯仰奖励）
  - Ours w/o r_foothold（去掉空心间隙惩罚和边缘惩罚）
  - Ours w/o depth noise（去掉深度噪声建模）
- 评估场景与指标：
  - 仿真：平地、标准化空心楼梯（20°–55°）、随机混合楼梯（随机台阶高度和水平间距）。
  - 指标：成功率（到达顶部路点百分比）、平均到达步数百分比、平均碰撞次数。
  - 仿真对比实验：在 0°–55° 及混合楼梯上测试所有方法。
  - 深度噪声鲁棒性实验：在 30° 楼梯上注入 0%–200% 的噪声，对比 Ours、Ours w/o depth noise 和 Extreme Parkour 的平均到达步数。
  - 真实世界实验：37° 和 55° 空心楼梯，每种楼梯进行 10 次试验，记录成功率。额外对比机器人自带的 MPC 和内置 RL 策略。

## 四、资源与算力

- 仿真训练使用 **单个 NVIDIA RTX 4090 GPU**。
- 论文未明确说明训练时长（如迭代次数或小时数），仅提及 2000 次迭代的可视化曲线（图6）。
- 真实部署使用 Jetson Orin NX 作为板载计算单元。

## 五、实验数量与充分性

- 仿真实验覆盖广泛：包含 6 种不同倾斜角度（0°–55°）和混合随机楼梯，每种方法都有多次独立测试（Success Rate 和 Average Reached Steps 来自多次试验）。
- 消融实验系统：分别验证了俯仰奖励（r_pitch）、落脚点奖励（r_foothold）、深度噪声模型三个组件的重要性，并提供了平均碰撞次数对比（表 II）和噪声鲁棒性曲线（图7）。
- 真实实验：每个楼梯 10 次试验，虽然次数不多，但已经能反映趋势；对比了 5 个基线（包括自带策略），说明公平。
- **充分性评价**：仿真实验设计较为全面，消融实验完整，噪声鲁棒性实验有说服力。但真实实验仅测试了两个角度（37° 和 55°），且未在其他环境（如不同材质、不同台阶尺寸、夜间光照等）验证，测试范围有限。另外，缺乏对运动速度、能耗等定量指标的评估。总体而言实验较充分但仍有完善空间。

## 六、论文的主要结论与发现

- StairMaster 在仿真和真实世界中均显著优于所有基线，在仿真 55° 楼梯上达到 97.5% 成功率，在真实 55° 楼梯上达到 40% 成功率（首次实现 RL 策略攀爬该斜率空心楼梯）。
- 深度噪声建模对零样本迁移至关重要：去掉噪声建模后，真实世界 37° 楼梯成功率从 80% 降至 40%，55° 从 40% 降至 10%。
- 3D 路点主动感知奖励有效地引导机器人主动调整俯仰角，提前捕捉楼梯结构（在 T=2.2s 时已抬头），避免了视觉盲区导致的失败。
- 落脚点奖励（空心惩罚+边缘惩罚）显著降低了碰撞次数（表 II），提高了落脚精度。
- 纯本体感知方法（HIMLoco、内置 RL）和传统视觉方法（Extreme Parkour）均无法应对空心楼梯的稀疏性和几何不连续性。

## 七、优点

- **方法创新**：提出三阶段训练框架（教师-蒸馏-微调），有效结合特权信息、蒸馏和自主探索；引入空间感知 LSTM 实现隐式时空对齐，无需显式里程计。
- **工程实用性**：高保真模拟深度噪声建模显著缩小仿真到现实差距，实现零样本直接部署；域随机化和地形课程保证策略鲁棒性。
- **奖励设计巧妙**：3D 路点奖励兼顾主动感知与运动学优化；空心惩罚和边缘惩罚直接针对主要失败模式（腿卡陷和滑落）。
- **实验对比全面**：在仿真中与多个主流方法对比，消融实验验证每个模块贡献；深度噪声鲁棒性实验证明模型强抗噪能力。
- **结果显著**：首次实现四足机器人攀爬 55° 空心楼梯，突破性贡献。

## 八、不足与局限

- **真实实验覆盖不够广泛**：仅测试了两种倾斜角度（37° 和 55°），未包括不同台阶宽度、不同材质（如湿滑表面）、不同环境光照等变量，可能高估了策略的泛化能力。
- **成功率仍有提升空间**：真实 55° 楼梯成功率为 40%，说明在极端条件下决策仍不稳定，可能存在未揭示的失败模式（如侧向漂移、掉落）。
- **缺乏动力学性能定量评估**：未报告攀爬速度、能耗、关节负载等指标，难以评估策略的效率和安全性。
- **依赖深度相机特定型号**：噪声建模基于 Intel D435，若迁移到其他深度传感器可能需要重新校准；且深度相机在户外强光或透明表面下可能完全失效。
- **计算资源需求**：网络结构包含 Cross-Attention 和 LSTM，对板载 GPU（Jetson Orin NX）有依赖，可能限制在低算力平台的部署。
- **仿真与现实差异未完全消除**：尽管噪声建模有效，但在某些场景（如台阶边缘反光严重）仍可能失败，论文未分析失败案例的具体原因。
- **缺乏与多模态感知（如 RGB）结合的探索**：未来方向提到准备加入 RGB，说明当前仅使用深度信息可能遗漏纹理线索。

（完）
