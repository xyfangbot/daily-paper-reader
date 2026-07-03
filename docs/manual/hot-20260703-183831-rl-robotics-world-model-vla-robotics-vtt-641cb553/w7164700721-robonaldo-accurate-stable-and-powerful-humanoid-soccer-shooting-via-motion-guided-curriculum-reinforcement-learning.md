---
title: "RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning"
title_zh: "RoboNaldo: 通过运动引导的课程强化学习实现精准、稳定且强力的类人足球射门"
authors: "Yichao Zhong, Yidan Lu, Ye Lu, Tianyang Tang, Haoguang Mai, Yixuan Pan, Tianyu Li, L Lin-Lin Chen, Yi-Xiang Wang, Zhongyu Li, Peng Lu, Hongyang Li"
date: 2026-06-09
pdf: "https://arxiv.org/pdf/2606.11092"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: "人形机器人足球射门需要在全身稳定、高冲击交互和准确性上达到平衡，但现有运动跟踪或任务奖励方法难以兼顾。RoboNaldo提出三阶段运动引导课程强化学习框架，以人类踢球参考为脚手架逐步优化射门性能：先学习稳定的全身先验，再适应静止球自由踢，最后扩展到移动球射门。模拟中自由踢误差降低48.6%、射门速度提升2.96倍；真实Unitree G1机器人在3米距离上，自由踢和移动球平均误差分别为0.73米和0.86米，球速达13.10米/秒（约为职业球员的59-71%）。该方法实现了高冲击、准确且稳定的人形机器人射门，且低层策略可便捷适配不同高层控制器。"
source: openalex
selection_source: hot_paper_scout
motivation: 现有方法难以同时满足人形机器人射门的全身稳定、高冲击力交互和准确性要求。
method: 提出三阶段运动引导课程强化学习，从人类参考先验逐步过渡到移动球射门。
result: "模拟中自由踢误差降低48.6%、速度提升2.96倍；真实机器人3米距离射门误差约0.8米，球速13.1 m/s。"
conclusion: RoboNaldo实现了高冲击、准确且稳定的人形机器人射门，性能接近专业球员。
---

## 摘要
精英级别的类人足球射门需要全身稳定性、高冲量的全身交互以及对目标的精准度。基于运动跟踪的强化学习（RL）提供了全身运动协调的稳定性，但固定的参考动作使其难以适应不同的球位和触球时机；相反，基于任务奖励的RL则难以从零开始探索和发现有效的射门动作。因此，我们提出了RoboNaldo，一种用于高冲量类人交互的三阶段运动引导课程强化学习框架。该框架以单个人类射门动作为支架，并逐步将优化目标转向射门性能。课程首先学习稳定的全身射门前置动作，然后将射门适应到自由球场景（球静止在随机位置），最后通过运动指令与射门触发接口扩展到移动球射门。在训练过程中，一个高级启发式规划器控制该接口，而在推理时，替代的高级控制器可驱动相同的低级策略。在仿真中，RoboNaldo的自由球射门误差比先前的基线方法低48.6%，射门速度提高了2.96倍。在真实世界中，搭载板载感知的Unitree G1上，RoboNaldo在自由球和移动球情况下从3米外射门的平均目标误差分别为0.73米和0.86米。触球后球速达到13.10米/秒，相当于已报道专业比赛射门速度的59-71%。项目页面：https://opendrivelab.com/RoboNaldo。

## Abstract
Elite humanoid soccer shooting requires whole-body stability, high-impulse whole-body interactions, and accuracy to targets. Motion tracking-driven reinforcement learning (RL) provides stability in whole-body movement coordination, but a fixed reference makes it hard to adapt to varied ball positions and strike timings; in contrast, task reward-driven RL struggles to explore and discover valid kicks from scratch. We therefore introduce RoboNaldo, a three-stage motion-guided curriculum RL framework for high-impulse humanoid interaction. A single human-kick reference is used as a scaffold and progressively shifts optimization towards shooting performance. The curriculum first learns a stable whole-body kicking prior, then adapts the kick to free-kick settings where the ball is stationary at random positions, and finally extends it to moving-ball shooting through a locomotion-command and kick-trigger interface. A high-level heuristic planner controls this interface during training, while alternative high-level controllers can drive the same low-level policy at inference. In simulation, RoboNaldo demonstrates free-kick shot error 48.6% lower and shoot velocity 2.96x than prior work baselines. In real world on a Unitree G1 with onboard perception, RoboNaldo attains 0.73 m and 0.86 m average target shooting error from 3 m away in free-kick and moving-ball cases, accordingly. And the post-contact ball velocity reaches 13.10 m/s, which is 59-71% of reported professional open-play shot speed. Project page: https://opendrivelab.com/RoboNaldo.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：人形机器人足球射门需要在全身稳定性、高冲量交互（短时强冲击）和目标精度之间取得平衡。现有方法存在明显缺陷：运动跟踪驱动的强化学习（RL）虽能提供稳定的全身协调，但固定参考动作难以适应不同的球位和触球时机；任务奖励驱动的RL则因稀疏奖励和高维控制空间而难以从零探索有效射门。
- **研究动机**：已有系统（如PAiD、HumanX等）在射门精度、速度和场景泛化（如移动球、室外部署）上存在局限，未能同时实现稳定性、精度、力量和泛化能力。RoboNaldo旨在填补这一空白，提出一个统一的RL框架来解决这些挑战。
- **整体含义**：这项工作展示了通过结构化课程学习，人形机器人能够掌握接近专业球员水平的射门技能（球速达13.10 m/s，约为职业球员的59-71%），并为高冲量人机交互任务提供了可扩展的范式。

## 二、论文提出的方法论
- **核心思想**：将射门学习分解为三个有序阶段，每个阶段利用不同的学习信号（运动跟踪、任务奖励、行为触发）逐步增强技能，避免单一信号导致的探索或稳定问题。
- **关键技术细节**：
  1. **三阶段课程学习**：
     - **阶段1（运动跟踪）**：使用从人类视频重定向的侧脚射门动作为参考，学习稳定的全身射门先验（无球和无任务奖励）。
     - **阶段2（射门适应）**：引入球、目标和射门奖励，随机化球位置，让策略学习调整触球点、方向和力度以实现自由球精准射门。
     - **阶段3（任务泛化）**：将射门问题转化为“接近-触发-射门-稳定”流程，通过高层运动指令和踢球触发信号取代固定参考动作，使策略能处理移动球射击。
  2. **奖励设计**：包括运动跟踪奖励（指数核）、正则化奖励（平滑性、足部滑动等）和射门任务奖励。后者包含**即时交互奖励**（公式1）和**密集化射门奖励**（通过弹道外推预测球到达球门线的位置以提前提供梯度）。
  3. **高层规划接口**：训练时使用启发式规划器（基于预测接触距离、球高度和相位），推理时可替换为其他高层控制器（如人类命令或神经策略），而无需重新训练低层策略。
- **公式/算法流程（文字说明）**：
  - 即时交互奖励将接触全生命周期（接近、冲击、结果）的奖励通过加法和除法组合，确保在短时接触窗口内仍有梯度信号。
  - 密集化射门奖励在每个后接触步将当前球速弹道外推至球门线，并与目标计算指数距离奖励，解决了稀疏奖励的信用分配问题。
  - 阶段转换依据奖励收敛、动作噪声标准差稳定和行为出现决定。

## 三、实验设计
- **仿真实验**：
  - 环境：Isaac Lab，4096个并行环境，物理步长5ms（200Hz），控制频率50Hz。
  - 任务：自由球（静止球在1m×1m前方正方形内随机采样）和移动球（球以0-5m/s速度射向2m×2m区域）。
  - 目标：在5米外的8m×2m球门平面上随机采样。
  - 评估指标：存活率、射门误差（平均每幕最近球-目标距离）、成功率（误差<0.5/1.0m）、峰值球速、接触率。
  - 对比方法：PPO、AMP、PAiD、纯运动跟踪（阶段1）、阶段2零样本迁移、阶段3完整策略。
  - 消融实验：课程结构（跳过阶段1/2）、阶段3机制（有无规划器、自适应采样、稳定阶段）、奖励设计（HDMI风格对比即时交互奖励）。
- **真实世界实验**：
  - 硬件：Unitree G1机器人（29自由度，35kg），板载感知（头戴Livox MID-360 LiDAR和胸前RealSense D435相机），使用ONNX模型以50Hz运行。
  - 场景：室内地板和室外足球场，球为5号足球，目标为AprilTag标记板。
  - 实验类型：自由球（136次尝试，124次有效射门）和移动球（27次尝试，20次有效射门）。左/中/右三个目标区域分别统计。
  - 指标：同仿真，但精度计算仅限于有效射门尝试，接触率和存活率基于总尝试。
- **Benchmark**：与STOFT、Reactive、Striker、HumanX、PAiD在目标精度、速度、移动球能力、自感知、室外部署五个维度对比（表1）。

## 四、资源与算力
- 仿真训练：在NVIDIA RTX 4090单卡上训练，使用4096个并行环境，每个阶段最多10^5次迭代，每隔10^3次迭代保存检查点。未明确说明总训练时长。
- 真实部署：推理在Unitree G1板载计算单元上运行ONNX模型，控制频率50Hz，无需外部动捕或离线状态估计。
- 论文未提供详细GPU数量、集群信息或总功耗数据，仅提及单张RTX 4090用于仿真训练。

## 五、实验数量与充分性
- **仿真实验量**：16,384个保留测试幕用于评估，多次随机种子重复。主对比包含4种基线方法（PPO、AMP、PAiD、阶段1运动跟踪），并报告均值和标准差。消融实验包含6组（课程、机制、奖励），每组均有详细指标。
- **真实实验量**：自由球136次尝试（124次有效），移动球27次尝试（20次有效），分左/中/右区域统计。此外还进行了室外足球场展示（图5）。
- **充分性评价**：
  - **充分**：仿真实验覆盖了多种基线、消融设计，统计指标全面（误差、速度、成功率、接触率、存活率），且分不同阶段和机制进行对比。真实实验涵盖了从室内校准到室外移动球的全流程，且使用了板载感知回路。
  - **客观公平**：与最新系统PAiD等进行了对比，并在精度和速度上显著优于它们。消融实验揭示了每个组件的重要性。
  - **不足**：移动球真实实验样本量较小（仅27次），可能受限于人为传递球的变异性；未在更复杂场景（如多人传球、高速球）下测试；感知模块针对回射球，泛化性有限。

## 六、论文的主要结论与发现
- 三阶段课程学习框架RoboNaldo能够训练出稳定、精准且强力的人形机器人射门策略，在仿真的自由球和移动球任务中误差分别低至0.899m和1.131m，峰值球速达14.79m/s。
- 在真实机器人上，从3米外射门的平均误差为自由球0.73m、移动球0.86m，峰值球速13.10m/s（约47.2km/h），达到职业球员射门速度的59-71%。
- 与基线方法相比，RoboNaldo在精度上（误差降低48.6%）和速度上（提升2.96倍）有显著优势。
- 消融实验表明：每个阶段、阶段3的规划器/自适应采样/稳定机制、以及即时交互奖励都是性能的关键；跳过任何组件都会导致核心指标大幅下降。
- 所提出的模块化高层规划接口使同一低层策略可被不同高层控制器复用，提高了灵活性。

## 七、优点
- **方法亮点**：
  1. **三阶段渐进课程**：合理分离了运动先验学习、射门适应和时序泛化，有效解决了混合学习信号冲突的问题。
  2. **即时交互奖励**：专门设计用于短时高冲量接触，通过组合接近、冲击和结果奖励避免了HDMI风格奖励在3-5物理步内的稀疏性问题。
  3. **密集化射门奖励**：通过弹道外推提前提供目标精度梯度，缓解了稀疏奖励的信用分配困难。
  4. **模块化高层接口**：允许训练时使用启发式规划器，部署时无缝切换为其他高层控制器，增强了实用性。
- **实验亮点**：
  1. **仿真+真实双重验证**：在大规模仿真（16K测试幕）和真实机器人（163次尝试）上都进行了评估，统计详尽。
  2. **与多个基线公平对比**：包括PPO、AMP、PAiD等，且消融实验系统全面。
  3. **真实世界感知-控制闭环**：使用板载LiDAR+相机，无需离线状态估计，验证了sim-to-real的可行性。
  4. **性能量化清晰**：报告了误差分布、成功率、球速、接触率、存活率多维度指标，并提供了热力图和轨迹可视化。

## 八、不足与局限
- **实验覆盖**：
  - 移动球真实实验样本量小（仅27次），统计置信度有限；未经受更高球速（>5m/s）或复杂球路（曲线、反弹）的测试。
  - 未在多人协作、守门员对抗、战术决策等更真实的足球场景中评估。
- **方法局限**：
  - 当前仅依赖单一参考射门动作（侧脚踢），无法执行多种射门技巧（如内脚背、外脚背、挑射等）。
  - 高层触发策略为手工设计的启发式规则，缺乏自主学习和适应能力，限制了复杂场景下的决策。
  - 感知模块高度定制化（基于回射球的LiDAR和IR相机），不具备通用性；无法感知自然足球或在多变光照/天气下工作。
- **偏差风险**：
  - 训练中球和目标的随机化范围有限（如自由球仅1m×1m区域），可能导致对极端位置泛化不足（如目标热力图显示侧向和高目标误差增大）。
  - 真实实验中机器人表现为右脚优势（左侧射门速度更快、右侧精度较低），可能源自参考运动或训练数据的不平衡。
- **应用限制**：整体系统依赖Unitree G1硬件和特定感知栈，迁移到其他平台需重新适配；Sim-to-real对动力学和感知随机化的依赖可能导致在未覆盖环境下性能下降。

（完）
