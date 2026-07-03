---
title: "Kine2Go: Kinematic dataset for the Unitree Go2 robot with diverse gaits and motions"
title_zh: Kine2Go：面向Unitree Go2机器人的多步态与运动学数据集
authors: "Władysław Pałucki, Paweł Siwak, Krzysztof Ciebiera, Marek Cygan"
date: 2026-06-12
pdf: "https://arxiv.org/pdf/2606.14433"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=title; institutions=Warsaw University of Technology, University of Warsaw; query=reinforcement learning based controller for humanoid robot locomotion"
tldr: 针对Unitree Go2四足机器人运动学演示数据获取困难的问题，提出Kine2Go数据集构建方法。该方法通过管道将多种四足形态的运动数据转换为Go2兼容格式，利用强化学习训练40种运动策略，并收集鲁棒的轨迹数据及电机动作。最终得到800条不同步态的轨迹数据，为模仿学习和行为克隆研究提供高质量基准，显著降低数据获取门槛。
source: openalex
selection_source: hot_paper_scout
motivation: 获取Go2机器人运动学演示数据需要复杂流水线且耗时，阻碍了模仿学习等技术的应用。
method: 设计数据管道将不同四足形态运动映射到Go2，并用强化学习训练策略以生成带扰动的鲁棒运动数据。
result: 构建了包含800条轨迹和40种策略的Kine2Go数据集，涵盖多种步态和电机动作信息。
conclusion: Kine2Go降低了四足机器人运动学数据获取难度，为强化学习和行为克隆研究提供重要资源。
---

## 摘要
近年来，机器人技术的普及与硬件成本的持续下降，降低了机器人研究的准入门槛，并推动了该领域的快速发展。其中一个典型代表是Unitree Go2四足机器人，常被研究人员用于运动控制、导航、控制等领域。许多研究者将Go2机器人与模仿学习、强化学习、行为克隆等技术结合，使机器学习系统能够完全控制机器人。然而，这类技术通常需要包含机器人运动学信息及电机动作的演示数据。获取此类数据难度较大，需要构建复杂的流程，且耗时较长。为助力此类研究，我们推出了Kine2Go——一个包含800条不同步态运动轨迹数据的Unitree Go2机器人数据集，这些数据源自40种不同策略。我们的流程可接收来自不同四足形态的数据，并将其转换为Go2兼容格式。随后使用强化学习训练遵循指定运动的策略，最终从这些策略中采集数据，从而获得稳健且包含扰动信息的运动学数据及其对应的电机级动作。

## Abstract
The recent popularity of robotics, combined with the steadily decreasing cost of robotic hardware, has lowered the entry barrier to robotics research and enabled rapid advancements in the field. One of the primary examples is the Unitree Go2 quadruped robot, which is often used by researchers in the areas of locomotion, navigation, control, and others. Many researchers use the Go2 robot in combination with techniques like imitation learning, reinforcement learning, and behavioral cloning to allow machine learning systems to take full control of the robot. At the same time, many of those techniques require demonstration data consisting of the robot's kinematics information and actions applied to the motors. Obtaining such data is difficult, requires building complex pipelines, and can take significant time. To aid in those kinds of efforts, we present Kine2Go - a dataset with 800 diverse gait kinematics trajectory motion data for the Unitree Go2 robot, derived from 40 distinct policies. Our pipeline accepts data from various quadruped morphologies and translates them to a Go2-compatible format. Then we use Reinforcement Learning to train policies following a given motion, and finally we gather data from those policies, which grants robust, perturbed kinematic data with corresponding motor-level actions.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：四足机器人（如Unitree Go2）的强化学习和模仿学习研究需要大量包含运动学信息和电机动作的演示数据，但获取此类数据需要构建复杂的管道，耗时且门槛高。现有大型数据集多集中于视觉操作和高级行为，缺乏面向低层腿部运动控制的、可直接用于Go2机器人的运动学-动作数据。
- **整体含义**：通过构建Kine2Go数据集，填补四足机器人领域缺乏大规模、多样化、高质量运动学轨迹数据的空白，为行为克隆、离线控制、运动条件策略学习及基础运动模型的训练提供关键资源，从而降低四足机器人运动控制研究的准入门槛，推动基础行为模型的发展。

## 二、论文提出的方法论
- **核心思想**：构建一个从多源运动捕捉数据到Go2机器人兼容运动学轨迹及策略动作的端到端管道，利用强化学习模仿参考运动，生成鲁棒的、含噪声的轨迹数据。
- **关键技术细节**：
  1. **运动学重定向**：针对不同四足形态（狗、马、Solo8机器人等）的运动数据，通过逆运动学（IK）求解器，将足端位置等任务空间目标映射到Go2的12自由度关节空间，逐帧生成Go2兼容的参考轨迹，保留原始步态特征。
  2. **强化学习运动模仿**：采用Peng et al.（2020）的方法，为每个参考运动训练独立的PPO策略。状态空间包括当前本体感受与未来4个时间步（t+1, t+2, t+10, t+30）的参考姿态；奖励函数为加权和的指数形式，惩罚关节位置、速度、足端位置、根部位姿、线速度与角速度的跟踪误差。
  3. **轨迹收集与过滤**：训练后的策略在Genesis引擎中执行随机滚动，记录每帧的关节配置、基座运动学、控制动作及全局状态。通过人工查看视频筛选出物理合理、跟踪偏差小的轨迹，并裁剪掉前0.5秒的“预热”帧。
- **算法流程**：输入源运动数据 → 帧级逆运动学重定向 → 用PPO在GPU并行环境中训练模仿策略 → 策略生成随机滚动 → 记录并过滤轨迹 → 形成最终数据集。

## 三、实验设计
- **数据集与场景**：
  - **数据来源**：四个不同形态的MoCap数据集，包括AI4Animation（狗）、VHDC（马）、Solo8机器人、AI4Animation交互式演示（狼）。共提取40个参考运动（如慢跑、转弯、踱步、跑、行走、爬行、跳跃等），每个运动经重定向后作为训练目标。
  - **生成数据集**：每个训练好的策略生成20条随机初始航向的独立轨迹，共800条轨迹，每条轨迹包含5-20秒的稳态运动。
- **基准与对比**：论文未设置显式benchmark对比其他方法，强调其数据集本身作为资源，可用于训练基础运动模型（如Meta Motivo）或行为克隆方法。提出的评估指标包括均方误差（MSE）和Earth Mover's Distance（EMD），但未在文中进行数值对比实验。
- **实验充分性**：覆盖了行走、跑、小跑、转弯、旋转、侧向移动、椭圆/方形路径等多种步态，但未包含跳跃、坐姿等运动。实验集中于平坦地形，缺乏崎岖地面或复杂环境下的数据。

## 四、资源与算力
- **算力使用**：
  - 训练阶段：每项策略在NVIDIA A100 GPU上训练约3小时，共40项策略，总GPU训练时长约120小时。使用8,192个并行环境，每个策略训练10,000次迭代（约20亿环境步）。
  - 轨迹采样与视频渲染：在无GPU加速的消费级工作站上完成。
  - 仿真引擎：Genesis（GPU加速物理引擎），支持大规模并行计算。

## 五、实验数量与充分性
- **实验数量**：训练了40个独立策略，每个策略生成20条轨迹，总计800条轨迹。每个轨迹的帧数因运动而异（如571帧、1171帧、300帧等）。
- **客观性与公平性**：
  - 所有策略使用相同的PPO超参数和奖励函数权重，保证训练一致性。
  - 通过手动视频筛选去除不稳定轨迹，保证数据质量；但人工筛选引入主观偏差。
  - 未进行消融实验（如不同奖励权重、不同重定向方法的影响），也未与其他数据集生成方法进行对比，实验设计偏向展示数据集本身而非验证方法最优性。

## 六、论文的主要结论与发现
- 成功构建了面向Unitree Go2的800条运动学-动作轨迹数据集，涵盖多种步态，可“开箱即用”支持行为克隆、离线强化学习等研究。
- 所提出的管道可轻松扩展至新数据源和新机器人形态，借助Genesis引擎的并行能力，即使使用消费级GPU也能高效生成数据，降低了机器人数据获取的硬件门槛。
- 该数据集有望成为四足机器人领域的基础行为模型（如Meta Motivo、BFM-Zero）的训练和正则化工具，推动更自然、多样化的运动控制研究。

## 七、优点
- **数据多样性**：融合四种不同形态的运动数据（狗、马、Solo8、虚拟狼），重定向至Go2，覆盖广泛步态，包括直线、转弯、椭圆路径等。
- **实用性强**：提供完整的运动学状态（关节位置、速度、基座姿态、根部位移）与电机动作（归一化命令），可直接用于时域控制任务。
- **管道可复现与可扩展**：代码开源，管道设计模块化（重定向类、训练脚本、过滤工具），易于适配新机器人或新数据源。
- **大规模并行训练**：利用Genesis引擎实现8192个并行环境，大幅缩短训练时间，使数据集生成在消费级GPU成为可能。
- **格式通用**：主轨迹数据以引擎无关格式存储，支持跨平台复现。

## 八、不足与局限
- **运动覆盖不全**：未包含跳跃、后空翻等动态动作（因强化学习模仿质量低），也未包含坐姿（因形态差异导致脚接地）。所有轨迹均采集于平坦地形，缺少楼梯、斜坡等复杂环境数据。
- **无压力传感器数据**：Go2机器人的足底气压传感器信息未模拟，限制了接触力相关任务的应用。
- **评估方法不完善**：论文未提供数值实验（如行为克隆的MSE，或基础模型的EMD分数），也未与其他数据集或方法进行对比，缺乏定量验证。
- **主观过滤风险**：轨迹筛选依赖人工观看视频，可能引入主观偏好，且对大数量轨迹扩展不够高效。
- **重定向可能失真**：对于形态差异大的数据源（如Solo8），逆运动学重定向可能导致部分运动特征丢失或动作不符合Go2机器人动力学约束。

（完）
