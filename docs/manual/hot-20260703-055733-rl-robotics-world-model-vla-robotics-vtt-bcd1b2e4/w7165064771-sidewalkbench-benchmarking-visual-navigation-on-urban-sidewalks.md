---
title: "SidewalkBench: Benchmarking Visual Navigation on Urban Sidewalks"
title_zh: SidewalkBench：城市人行道视觉导航基准测试
authors: "Z LIU, H. He, Vivek Alumootil, Akshat Pandya, Brad Squicciarini, Wayne Wu, Bolei Zhou"
date: 2026-06-15
pdf: "https://arxiv.org/pdf/2606.16953"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; query=reinforcement learning for drone navigation in dynamic environments"
tldr: 城市人行道导航因复杂布局和动态行人而困难，但缺乏统一基准。SidewalkBench基于NVIDIA Isaac Sim构建高保真模拟环境，包含程序生成与真实扫描场景及反应式行人事件。评估9个视觉导航模型在330个单元测试、800个行人反应和105个长距离场景，发现行人交互和长距离鲁棒性是关键瓶颈。该基准为可重复评估提供标准化平台，并指出合成数据扩展训练是有效方向。
source: openalex
selection_source: hot_paper_scout
motivation: 现有视觉导航模型缺乏统一基准，无法定量可重复评估城市人行道导航性能。
method: 基于NVIDIA Isaac Sim构建高保真模拟器，包含程序生成与真实扫描场景及反应式行人事件。
result: 评估9个模型，发现行人交互和长距离鲁棒性是瓶颈，合成数据训练有潜力。
conclusion: SidewalkBench为城市人行道导航提供标准化评估平台，推动定量研究。
---

## 摘要
由于复杂的结构布局、动态的行人行为以及长距离导航，城市人行道导航面临重大挑战。尽管最近的视觉导航模型提供了有前景的解决方案，但缺乏统一基准阻碍了定量和可重复的评估。为弥补这一空白，我们提出了SidewalkBench，一个专为城市人行道视觉导航设计的综合基准。基于NVIDIA Isaac Sim构建，SidewalkBench实现了多样化、高保真人行道环境的GPU加速仿真，包括程序化生成和真实世界扫描的场景。我们进一步用丰富的、基于事件的反应式行人行为以及灵活高效的动画填充场景，从而在逼真的现实世界设置下实现标准化模型评估。我们对9个视觉导航模型在330个单元测试场景、800个行人反应场景和105个长程场景上进行了全面评估。我们的研究结果表明，行人交互和长程鲁棒性仍然是现有模型的关键瓶颈，而利用合成数据扩展人行道训练是一种有前景的解决方案。

## Abstract
Urban sidewalk navigation presents significant challenges due to complex structural layouts, dynamic pedestrian behaviors, and long distances. While recent visual navigation models offer a promising solution, the lack of a unified benchmark hinders quantitative and reproducible evaluation. To bridge this gap, we propose SidewalkBench, a comprehensive benchmark designed for visual navigation on urban sidewalks. Built upon NVIDIA Isaac Sim, SidewalkBench brings GPU-accelerated simulation of diverse, high-fidelity sidewalk environments, including both procedurally generated and real-world scanned scenes. We further populate the scenes with rich, reactive event-based pedestrian behaviors and flexible, efficient animation, enabling standardized model evaluation under realistic real-world settings. We conduct a comprehensive evaluation of 9 visual navigation models on 330 unit-test scenarios, 800 pedestrian-reactive scenarios, and 105 long-horizon scenarios. Our findings highlight that pedestrian interaction and long-horizon robustness remain critical bottlenecks for existing models, and scaling up sidewalk training with synthetic data emerges as a promising solution.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：城市人行道上的移动机器人数量快速增长（如送货机器人、电动轮椅等），但安全导航仍面临巨大挑战，包括复杂的静态布局、动态行人的不确定行为以及长距离行驶。近年来的视觉导航基础模型（如 ViNT、CityWalker、OpenPilot 等）展现了一定潜力，但缺乏统一的基准来定量、可重复地评估这些模型在实际人行道场景中的表现。
- **核心问题**：现有评估大多规模小、缺乏场景多样性（如短距离、无行人互动），且没有标准化的测试协议，导致难以公平比较不同模型、隔离失败模式、指导未来研究。
- **整体含义**：本文旨在填补这一空白，通过建立一个综合的人行道视觉导航基准 SidewalkBench，提供标准化、高保真、可重现的评估平台，从而推动该领域的发展。

## 二、论文提出的方法论
- **核心思想**：基于 NVIDIA Isaac Sim 仿真引擎，构建包含丰富场景和动态行人的城市人行道仿真环境，并设计三类标准测试场景（单元测试、行人反应测试、长距离测试），用于系统评估视觉导航模型的各项能力。
- **关键技术细节**：
  - **场景生成**：两种互补场景类型：
    - 程序化生成场景：通过定义 7 种基本街区类型（直线、曲线、路口等），使用样条路由连接，并随机化功能区域布局和静态物体，生成 100 个 2km×2km 的大规模环境。
    - 真实扫描场景：利用 3DGS 技术从现实街道扫描重建 11 个 150m×150m 场景，保留真实几何与外观。
  - **行人模拟**：双层次架构：
    - 高层行为：采用“行为图”结合事件驱动，定义了 8 种标准化互动场景（如迎面、侧向、超越、队列、手势等），通过触发条件动态启动规则化轨迹。
    - 低层动画：基于 SMPL 人体模型，使用 MotionLCM 等运动生成模型，并通过 Nvdiffrast 高效渲染（相比原生 Isaac Sim 提升 60 倍），支持平行环境大规模仿真。
  - **测试场景设计**：
    - 单元测试：330 个短距离场景（10–20m），不含行人，评估车道跟随和静态避障。
    - 行人反应测试：800 个场景，每种行为 100 个，引入动态行人，评估社交互动能力。
    - 长距离测试：105 个场景（距离>100m），总长 36.5km，评估长时鲁棒性，计数碰撞、出界、冻结等失败类型。
  - **评价指标**：单元测试用路线完成率和成功率；行人测试用任务成功率；长距离用每100米平均失败次数和平均速度。

## 三、实验设计
- **数据集 / 场景**：
  - 程序化生成场景（PG）：100 个大规模环境
  - 真实扫描场景（Real）：11 个真实街道重建
  - 测试场景共 330 + 800 + 105 = 1235 个，覆盖多种结构和行人行为。
- **基准（Benchmark）**：本文提出的 SidewalkBench 本身就是一个新的统一基准。
- **对比方法**：9 个代表性视觉导航模型：
  - 通用导航模型：ViNT、NoMaD、MBRA、InternVLA-N1（VLA 模型）
  - 人行道专用模型：CityWalker、MIMIC、S2E、FlowPilot、OpenPilot
  - 各种模型在数据规模、架构（CNN/ViT）、目标编码器、动作解码器、参数量（8M 到 7B）上差异显著，有利于分析数据与架构的影响。
- **实验设置**：
  - 使用四轮送货机器人平台，PD 控制器转换预测航点。
  - 同步测试（忽略推理延迟），10 个并行环境，NVIDIA L40S GPU。
  - 调整推理帧率和图像分辨率以匹配各模型规格，提供非特权目标信息（随机中间目标或目标无关指令）。

## 四、资源与算力
- **仿真算力**：所有基准测试在单张 NVIDIA L40S GPU 上运行，使用 Isaac-Sim 6.0，每个实验开启 10 个并行环境。未明确给出总运行时长。
- **模型训练算力**：论文未报告所评估模型的训练算力。但在“合成数据微调”实验中，仅使用 500 条演示微调 FlowPilot，更新少量模块（动作编码器/解码器），在单 GPU 上进行 50 个 epoch，所需算力较低。
- **总体**：文中未提供详细算力消耗数据，主要贡献在于标准化评估框架，而非模型训练。

## 五、实验数量与充分性
- **实验数量**：三类场景共 1235 个测试案例（330+800+105），总距离 36.5km，覆盖程序化与真实扫描场景，对比 9 个模型，实验规模在同类导航基准中较大。
- **充分性**：
  - 单元测试和行人测试中每个子场景有 100 个案例，统计可靠。
  - 长距离测试数量相对较少（105 个）但总距离足够，且采用了失败计数而非单一成功/失败，更细致。
  - 实验设计系统化，分别分离了静态结构、行人行为、长路程等因素，便于分析失败模式。
  - 进行了初步的消融实验（微调前后对比），揭示了合成数据训练的有效性。
- **客观性与公平性**：
  - 使用标准化的仿真环境和统一的控制器，避免人为干扰。
  - 对目标导向模型提供随机目标以防止信息泄露，对 VLA 模型使用通用指令。
  - 但模型推理速度差异被忽略（同步测试），可能高估慢模型在实时部署中的表现。
- **综合评价**：实验设计较为充分，结论有据可依，但仍缺少针对环境参数（如行人密度、障碍物分布）的扩展敏感性分析。

## 六、论文的主要结论与发现
- **数据规模是关键**：人行道专用训练数据规模（1000 小时）的 OpenPilot 在绝大多数场景中表现最优，优于更复杂的 VLA 模型。通用导航模型（ViNT、NoMaD）几乎无法完成基本车道跟随。
- **行人交互是瓶颈**：所有模型在行人反应场景中成功率大幅下降，尤其侧向接近（12%）、人行横道（1%）、手势（5%）等场景。社交群体（交谈、排队）比单个静止行人更难。
- **长距离导航远未解决**：最佳模型（OpenPilot）每 100 米仍有 1.34 次失败，若用于实际送货任务（2km），需约 27 次人工接管。
- **程序化场景与真实场景表现相关**：两个场景上的排名基本一致，说明程序化仿真可作为有效代理评估。
- **合成数据训练有效**：通过仿真平台生成的演示数据微调，FlowPilot 在行人横穿和手势场景上的成功率从 0.11/0.12 提升至 0.69/0.49，且在真实世界测试中也有显著提升（从 0.00 到 0.40/0.50）。
- **架构不如数据重要**：轻量模型（OpenPilot，8M）通过大规模数据训练，性能优于大模型（InternVLA-N1，7B），后者的社会合规意识较好但控制精度不足。

## 七、优点
- **填补空白**：首个面向城市人行道视觉导航的综合基准，提供标准化、可重现的评估框架。
- **高保真仿真**：利用 NVIDIA Isaac Sim 实现 GPU 加速精确物理和渲染，结合程序化生成与真实扫描场景，视觉真实感强。
- **丰富的动态行人**：提出事件驱动的行人行为图和基于 SMPL 的高效动画，实现 8 种标准化互动场景，且渲染效率极高。
- **多层次测试设计**：从短距结构理解到行人互动再到长程鲁棒性，系统化隔离不同挑战因素，便于诊断失败模式。
- **大量模型对比**：涵盖 9 种主流方法，包括最新 VLA 模型，结果具有代表性。
- **实用导向**：长距离场景使用每100米失败次数，贴近真实部署评价。
- **开源可用**：代码和场景数据计划公开（见项目页面），方便后续研究者复现和扩展。

## 八、不足与局限
- **行人行为不够真实**：当前事件驱动的行人轨迹基于规则，缺乏真实世界中微妙、多样的交互模式（如目光交流、避让博弈），可能降低模型的泛化性。
- **视觉质量折衷**：为追求效率，基于 SMPL mesh 的行人渲染与 3DGS 背景结合时可能存在光照伪影，增大 sim-to-real 差距。
- **真实扫描场景数量有限**：仅 11 个场景，且平均规模 150m×150m，覆盖度不足，程序化场景仍是主要评估来源。
- **推理速度被忽略**：采用同步测试排除延迟影响，但实际部署中慢模型可能因低帧率导致更多失败，基准未考虑实时性约束。
- **缺少消融实验**：未对仿真参数（如行人密度、障碍物数量）进行系统变化，也未分析模型架构中各组件（如视觉编码器、动作解码器）的贡献。
- **单机器人平台**：仅使用一种四轮机器人底盘，未验证在其他形态（如双足、四足）上的适用性（虽在附录中展示了几张效果图，但没有定量结果）。
- **社会合规指标单一**：仅用了最小距离和碰撞率，缺乏对“交互自然性”的评估（如绕行幅度、车速平滑度等）。

（完）
