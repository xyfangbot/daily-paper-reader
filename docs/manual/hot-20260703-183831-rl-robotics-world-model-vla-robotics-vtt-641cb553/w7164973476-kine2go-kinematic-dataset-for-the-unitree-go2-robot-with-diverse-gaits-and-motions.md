---
title: "Kine2Go: Kinematic dataset for the Unitree Go2 robot with diverse gaits and motions"
title_zh: Kine2Go：面向Unitree Go2机器人的多步态运动学数据集
authors: "Władysław Pałucki, Paweł Siwak, Krzysztof Ciebiera, Marek Cygan"
date: 2026-06-12
pdf: "https://arxiv.org/pdf/2606.14433"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=title; institutions=Warsaw University of Technology, University of Warsaw; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 四足机器人研究需要大量演示数据，但获取运动学与电机动作数据困难且耗时。Kine2Go数据集通过转换不同形态四足数据，结合强化学习训练40个策略，为Unitree Go2生成800种多样化步态轨迹。该数据包含鲁棒扰动下的运动学信息及对应电机动作，降低了数据获取门槛，促进了模仿学习等研究。
source: openalex
selection_source: hot_paper_scout
motivation: 获取四足机器人多样化步态的演示数据（运动学与电机动作）需要复杂管道且耗时，限制了基于学习的研究。
method: 接受不同四足形态的运动数据并转换为Go2格式，使用强化学习训练40个策略生成多样化轨迹，收集鲁棒扰动下的运动学与电机动作。
result: 构建了Kine2Go数据集，包含800种不同步态的运动轨迹和对应电机动作，覆盖多种运动模式。
conclusion: 为Unitree Go2提供了高质量、多样化的演示数据，降低了数据获取成本，支撑机器人学习研究。
---

## 摘要
近年来机器人的普及，结合机器人硬件成本的稳步下降，降低了机器人研究的准入门槛，并推动了该领域的快速发展。其中一个典型例子是Unitree Go2四足机器人，常被研究人员用于移动、导航、控制等领域。许多研究者将Go2机器人与模仿学习、强化学习、行为克隆等技术结合，使机器学习系统能够完全控制机器人。同时，这些技术大多需要包含机器人运动学信息以及作用于电机上的动作的演示数据。获取此类数据较为困难，需要构建复杂的数据处理流程，且耗时较长。为支持此类研究，我们提出了Kine2Go——一个包含800条多样化步态轨迹运动学数据的Go2机器人数据集，这些数据源自40种不同的策略。我们的数据处理流程可接收来自不同四足形态的数据，并将其转换为Go2兼容格式。随后使用强化学习训练策略以遵循给定运动，最终从这些策略中收集数据，从而获得带扰动且包含对应电机级动作的鲁棒运动学数据。

## Abstract
The recent popularity of robotics, combined with the steadily decreasing cost of robotic hardware, has lowered the entry barrier to robotics research and enabled rapid advancements in the field. One of the primary examples is the Unitree Go2 quadruped robot, which is often used by researchers in the areas of locomotion, navigation, control, and others. Many researchers use the Go2 robot in combination with techniques like imitation learning, reinforcement learning, and behavioral cloning to allow machine learning systems to take full control of the robot. At the same time, many of those techniques require demonstration data consisting of the robot's kinematics information and actions applied to the motors. Obtaining such data is difficult, requires building complex pipelines, and can take significant time. To aid in those kinds of efforts, we present Kine2Go - a dataset with 800 diverse gait kinematics trajectory motion data for the Unitree Go2 robot, derived from 40 distinct policies. Our pipeline accepts data from various quadruped morphologies and translates them to a Go2-compatible format. Then we use Reinforcement Learning to train policies following a given motion, and finally we gather data from those policies, which grants robust, perturbed kinematic data with corresponding motor-level actions.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 机器人与强化学习结合时，常需要演示数据（包含运动学信息和电机动作）来训练策略。然而，获取这类数据需要构建复杂的数据采集管道，耗时且门槛高。
- 当前四足机器人领域缺少像人形机器人领域那样的大规模、多样化的运动学数据集，导致基于数据驱动的行为克隆、运动模仿和基座模型研究受限。
- 作者旨在为Unitree Go2机器人创建一个高质量、多样化的运动学-动作数据集，降低四足机器人运动学习的研究门槛。

## 二、论文提出的方法论
- **核心思想**：通过一个三阶段管道，将不同来源的四足运动数据（狗、马、Solo8机器人、交互控制仿真）转化为Go2机器人可用的运动轨迹，并用强化学习训练策略生成带鲁棒扰动的数据集。
- **关键技术细节**：
  1. **运动学重定位（Kinematic Retargeting）**：为每个数据源定义映射类，逐帧将源姿态通过逆运动学（IK）转换为Go2的12自由度关节配置，保留步态特征，输出连续参考轨迹（但不含动作数据）。
  2. **运动模仿强化学习**：对每条参考轨迹训练一个独立的策略。采用基于PPO（Proximal Policy Optimization）的模仿学习框架，奖励函数由关节位置、关节速度、末端执行器、根部位姿、根部速度的跟踪误差加权组成（具体权重见论文附录C.1）。策略观察空间包含当前本体状态和未来1、2、10、30步的参考姿态。使用Genesis物理引擎并行训练8192个环境，每条策略训练约20亿环境步（10000次迭代），周期性地回绕参考运动以生成任意长度轨迹。
  3. **轨迹收集与过滤**：每个策略随机化初始朝向，部署20条独立轨迹（长度根据运动类型5-20秒），记录本体状态和电机动作。通过人工检查视频过滤出不稳定的轨迹，并去掉前0.5秒“热身”帧。数据存储为引擎无关格式。
- **公式**：奖励函数定义见论文式(1)-(8)，包含多个指数项加权求和。

## 三、实验设计
- **数据集/场景**：使用四种来源的原始运动数据：(1) AI4Animation（狗运动捕捉，15条修剪后的运动）；(2) VHDC（马运动捕捉，6个trot和6个walk）；(3) Solo8机器人数据（8自由度，提供了爬行、跳跃等难复现运动）；(4) AI4Animation交互式仿真（用户控制狼动画走复杂路径，7个运动）。所有运动均需保证首尾帧关节相似以保证循环平滑。
- **基准/对比方法**：本文不涉及与其他方法的对比，而是专注于数据集构建。主要参照了Peng等人2020年的DeepMimic框架进行运动模仿，并在Genesis引擎中复现。
- **实验数量**：总共训练了40个独立的RL策略（每种来源的数量：AI4Dog 22个，Solo8 6个，VHDC 12个），每个策略生成20条轨迹，共计800条轨迹，覆盖走、跑、小跑、转弯、旋转、游荡、跳跃等多种步态。还提供了一个包含8个运动（每个来源2个）的样本子集。

## 四、资源与算力
- **训练硬件**：NVIDIA A100 GPU。每个策略平均训练3小时，使用Genesis引擎并行8192个环境。后续轨迹采样和视频渲染在无GPU加速的消费级工作站上完成。
- **数据大小**：完整数据集（含视频）约30 GB。

## 五、实验数量与充分性
- 实验数量：40个策略、800条轨迹，来源覆盖4种不同形态，多样性较好。每个策略生成20条轨迹，随机化朝向，考虑了随机性覆盖状态空间。
- 充分性评估：手动过滤了不稳定的轨迹，并去除了热身帧；但由于RL训练中跳跃运动模仿质量不佳而排除该类别，且限于平坦地形。实验在单一仿真引擎（Genesis）上进行，未在真实机器人上验证数据集有效性（因为数据集本身是供后续研究使用的训练数据）。整体而言，数据集构建过程严谨，但缺乏不同引擎或真实世界的迁移验证。

## 六、论文的主要结论与发现
- 成功构建了Kine2Go数据集：800条Go2机器人运动轨迹，包含完整运动学状态和电机动作，来源于多种四足形态的重定位数据。
- 验证了所提出的三阶段管道（重定位、RL模仿、轨迹收集）的有效性和可扩展性，能够在消费级GPU上运行，且易于扩展至新数据源。
- 该数据集旨在作为四足机器人行为基础模型的训练数据，类似于AMASS和MoCapAct在人形机器人领域的作用，弥补了四足领域大规模数据集的空白。

## 七、优点
- **多样性**：融合了狗、马、Solo8以及交互控制仿真四种不同来源的运动，覆盖多种步态和复杂路径（圆、椭圆、8字、方、侧向移动等）。
- **开箱即用**：提供了Go2兼容的运动学状态和电机动作，无需后续处理即可直接用于行为克隆、离线控制等方法。
- **管道可复用**：整个管道在Genesis引擎上实现，GPU加速且开源，便于研究人员移植到其他机器人形态或添加新数据源。
- **质量保证**：通过人工过滤和修剪首帧，保证轨迹稳定性和循环平滑性。

## 八、不足与局限
- **未覆盖的运动类型**：缺少跳跃（空中无支撑相）、坐下等运动，因为RL模仿质量差或重定位导致关节穿透地面。
- **环境局限**：所有轨迹均在平地上收集，未包含粗糙地形、斜坡、楼梯等复杂环境。
- **传感器数据缺失**：未模拟足底压力传感器，因此数据集中不包含压力信息。
- **验证不足**：数据集本身仅是训练数据，未在真实Go2机器人上进行迁移或评估，其实际有效性取决于后续研究。
- **数据来源有限**：仅包含四种相对较小的原始运动源，且部分来源（如VHDC）只使用了子集，可能未充分覆盖全部运动模式。
- **人工筛选依赖**：轨迹过滤依赖人工观看视频，可能引入主观偏差，且不易规模化。

（完）
