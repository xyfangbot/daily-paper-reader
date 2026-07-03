---
title: "SidewalkBench: Benchmarking Visual Navigation on Urban Sidewalks"
title_zh: SidewalkBench：城市人行道上的视觉导航基准测试
authors: "Z LIU, H. He, Vivek Alumootil, Akshat Pandya, Brad Squicciarini, Wayne Wu, Bolei Zhou"
date: 2026-06-15
pdf: "https://arxiv.org/pdf/2606.16953"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; query=reinforcement learning for drone navigation in dynamic environments"
tldr: 城市人行道导航因复杂布局、动态行人和长距离而困难，现有模型缺乏统一评测基准。本文提出SidewalkBench基准，基于NVIDIA Isaac Sim构建高保真模拟环境，包含程序生成与真实扫描场景，并集成反应式行人行为。在330个单元测试、800个行人反应测试和105个长程测试上评估9个视觉导航模型，发现行人交互和长程鲁棒性是主要瓶颈。SidewalkBench提供了标准化可复现评测，并指出合成数据训练是提升导航性能的有前景方向。
source: openalex
selection_source: hot_paper_scout
motivation: 现有视觉导航模型在城市人行道上缺乏统一基准，难以进行定量和可复现评估。
method: 基于NVIDIA Isaac Sim构建高保真模拟环境，含程序生成与真实扫描场景，并集成反应式行人行为。
result: 评估了9个模型，发现行人交互和长程鲁棒性是关键瓶颈，合成数据训练表现出提升潜力。
conclusion: SidewalkBench提供了标准化评测，合成数据训练是解决城市人行道导航瓶颈的有效策略。
---

## 摘要
城市人行道导航面临复杂的结构布局、动态的行人行为以及长距离等显著挑战。尽管最近的视觉导航模型提供了有前景的解决方案，但缺乏统一基准阻碍了定量和可重复的评估。为弥补这一不足，我们提出了SidewalkBench，一个专为城市人行道视觉导航设计的综合基准测试。基于NVIDIA Isaac Sim构建，SidewalkBench提供了多种高保真人行道环境的GPU加速模拟，包括程序化生成和真实世界扫描的场景。我们进一步用丰富的、基于事件的反应式行人行为以及灵活高效的动画填充场景，从而在逼真的真实世界设置下实现标准化模型评估。我们在330个单元测试场景、800个行人反应式场景和105个长时域场景上对9个视觉导航模型进行了全面评估。我们的发现表明，行人交互和长时域鲁棒性仍然是现有模型的关键瓶颈，而利用合成数据扩大人行道训练成为一种有前景的解决方案。

## Abstract
Urban sidewalk navigation presents significant challenges due to complex structural layouts, dynamic pedestrian behaviors, and long distances. While recent visual navigation models offer a promising solution, the lack of a unified benchmark hinders quantitative and reproducible evaluation. To bridge this gap, we propose SidewalkBench, a comprehensive benchmark designed for visual navigation on urban sidewalks. Built upon NVIDIA Isaac Sim, SidewalkBench brings GPU-accelerated simulation of diverse, high-fidelity sidewalk environments, including both procedurally generated and real-world scanned scenes. We further populate the scenes with rich, reactive event-based pedestrian behaviors and flexible, efficient animation, enabling standardized model evaluation under realistic real-world settings. We conduct a comprehensive evaluation of 9 visual navigation models on 330 unit-test scenarios, 800 pedestrian-reactive scenarios, and 105 long-horizon scenarios. Our findings highlight that pedestrian interaction and long-horizon robustness remain critical bottlenecks for existing models, and scaling up sidewalk training with synthetic data emerges as a promising solution.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：城市人行道导航对移动机器人而言极具挑战性，面临复杂结构布局（如弯道、交叉口）、动态行人行为（社交群组、手势、突然横穿）以及长距离航行（>100m）等问题。近年来，视觉导航基础模型（如ViNT、CityWalker、InternVLA-N1等）仅依赖单目RGB相机并展现出较强泛化能力，但现有评估工作存在以下不足：测试场景尺度小（通常<10米）、缺乏结构多样性、未标准化行人行为定义、无统一协议，导致难以公平比较不同模型并准确定位性能瓶颈。  
- **核心问题**：缺乏一个统一、标准化、可复现的城市人行道视觉导航基准，以系统评估模型的避障能力、行人交互能力、长程鲁棒性。  
- **整体含义**：本文旨在通过构建SidewalkBench填补这一空白，提供一个涵盖多样化高保真场景（程序化生成与真实扫描）以及丰富行人行为的仿真平台，并在此平台对9个代表性视觉导航模型进行大规模评测，揭示现有模型在行人理解与长程稳健性上的关键不足，同时证明合成数据微调是有效的提升途径。

## 二、论文提出的方法论
- **核心思想**：基于NVIDIA Isaac Sim构建GPU加速的城市人行道仿真平台，集成两类场景（程序化生成场景与真实世界扫描场景）以及事件驱动的行人行为模拟，定义三层次标准化测试场景（单元测试、行人反应测试、长时域测试），对多种视觉导航模型进行系统评测。  
- **关键技术细节**：  
  1. **场景生成**：  
     - 程序化生成：定义7种原始街区类型（直道、弯道、交叉口等），通过样条曲线连接形成连续拓扑；将每个街区划分为5个功能区（道路、人行道、路缘、绿化带、临街区），随机化功能区布局并添加坡道、人行横道等；利用UrbanVerse-100K资产库随机采样天空HDRI、纹理、静态物体。共生成100个2km×2km的大规模环境。  
     - 真实扫描场景：使用XGRIDS空间相机（LiDAR+四目）扫描11个真实城市街区，利用3D Gaussian Splatting（3DGS）重建高保真视觉外观与几何，标注人行道/斑马线区域，转换为Isaac Sim可模拟格式（平均150m×150m）。  
  2. **行人仿真模块**：  
     - **高层行为**：基于行为图与事件驱动状态机，定义8种事件行为（如阻挡、交谈、排队、正面/侧面/超车、穿行、手势），根据机器人与行人的相对位置动态触发，确保标准化可复现。  
     - **底层动画**：采用SMPL人体模型控制骨架，利用MotionLCM等运动生成模型实时生成步行、站立等常见动作；对程序化场景使用SMPL网格纹理渲染（单环境50行人可达226.8 FPS），对真实扫描场景使用SMPL 3DGS化身（10.7 FPS），均远优于Isaac Sim原生管线（3.4 FPS）。碰撞检测使用半径0.3m圆柱简化。  
  3. **测试场景定义**：  
     - **单元测试（330个）**：短程（10-20米），不含行人，评估直线、弯道、斑马线三种基础结构下的车道保持与静态避障能力。  
     - **行人反应测试（800个）**：在直道或斑马线上添加不同事件行为（各100个），评估模型对行人行为的反应。  
     - **长时域测试（105个）**：起点与终点距离>100m，通过设置障碍物保证单一路径，不终止于失败而是记录失败次数（碰撞、出界、冻结），评估长程鲁棒性。  
  4. **评测指标**：  
     - 单元测试：路径完成率（RC）、成功率（SR）、SPL。  
     - 行人反应测试：成功率、行人碰撞率、最小行人距离。  
     - 长时域测试：平均每100m失败次数（分别统计碰撞、出界、冻结）及平均速度。  
  5. **模型评估协议**：使用四轮递送机器人平台（最大线速度2.5m/s，最大角速度0.65rad/s），所有模型通过PD控制器将预测路径点转为速度命令。采用同步测试（等待指令），10个并行环境在单张NVIDIA L40S GPU上运行，物理步长0.005s。

## 三、实验设计
- **使用的数据集/场景**：  
  - 程序化生成场景：100个2km×2km规模的大规模环境，用于单元测试、行人反应测试、长时域测试。  
  - 真实世界扫描场景：11个城市街区（平均150m×150m），用于单元测试（每类结构10个）和长时域测试（5个）。  
- **Benchmark结构**：  
  - 单元测试：共330个场景（程序化生成300个，真实扫描30个），覆盖直道、弯道、斑马线。  
  - 行人反应测试：800个场景（均为程序化生成，每种行为100个）。  
  - 长时域测试：105个场景（程序化100个，真实扫描5个），总路径长度36.5km。  
- **对比的方法（共9个模型）**：  
  - 通用视觉导航模型：ViNT、NoMaD、MBRA、InternVLA-N1（VLA模型）。  
  - 人行道专用模型：CityWalker、S2E、MIMIC、FlowPilot、OpenPilot。  
  - 模型在训练数据规模、架构（不同视觉编码器/动作解码器）、输入频率、参数量上差异显著（从8M到7B）。  
- **补充实验**：  
  - 合成数据生成实验：在FlowPilot上微调，收集仿真的“穿行”与“手势”场景各500个成功示范，冻结视觉骨干，仅更新轻量任务适应层和动作解码器（使用AdamW，学习率5e-6，余弦退火，50轮）。在仿真和真实世界中评估性能提升。

## 四、资源与算力
- **仿真底层的计算资源**：所有基准测试在**单张NVIDIA L40S GPU**上运行，使用Isaac Sim 6.0，**10个并行环境**同时模拟。  
- **行人渲染效率对比**：文本明确指出Mesh管线可达到226.8 FPS（单环境50行人），3DGS管线10.7 FPS，远快于Isaac Sim原生管线（3.4 FPS）。  
- **模型训练资源**：未报告各个模型原始训练所使用的具体算力。本文进行的合成数据微调实验仅使用了单GPU（具体型号未进一步说明），但提及冻结视觉骨干，仅更新少量参数，资源消耗较低。  
- **总体而言**，论文未详细披露完整训练时长或其他GPU数量，但实验部署资源明确且在附录中提供了详细配置。

## 五、实验数量与充分性
- **实验数量**：  
  - 单元测试：共330个场景，对9个模型分别测评，报告SR、SPL、RC。  
  - 行人反应测试：共800个场景，覆盖8种事件行为，每个模型均测评，额外报告行人碰撞率与最小距离。  
  - 长时域测试：共105个场景，每个模型测评，统计每100m失败次数及平均速度。  
  - 合成数据微调实验：在程序化生成和真实扫描场景中各对两种场景进行前后对比（每组10次真实世界试验）。  
- **充分性与公平性**：  
  - 场景覆盖了静态结构、动态行人、长距离三种核心维度，场景数量较大（总计1235个测试场景），且考虑了程序化与真实扫描的视觉差异。  
  - 模型选择全面，涵盖通用与专用导航模型以及VLA模型，从模型规模、架构、训练数据量上具有代表性。  
  - 实验中采用同步测试以消除推理延迟差异，并通过统一控制接口保证公平性。  
  - 所有评测协议公开，场景定义明确，利于复现。  
  - 但存在一定不足：真实扫描场景数量较少（仅11个街区，长时域仅5个），程序化生成场景的逼真度仍与真实世界存在差距。

## 六、论文的主要结论与发现
1. **数据规模至关重要**：行人道专用训练数据规模越大，模型性能越强（OpenPilot 1000小时数据 > FlowPilot 300小时 > MIMIC 50小时），而通用基础模型（ViNT、NoMaD）在行人道场景中几乎完全失效。  
2. **行人交互仍为关键瓶颈**：即使是单个静态行人（Obstructing）也会使平均成功率从0.42降至0.23；社交群体（Conversing/Queueing）进一步降至0.16/0.14；侧面接近（Lateral）和斑马线穿越（Ped-Crossing）最具挑战（平均成功率仅0.12和0.01）；手势理解（Gesturing）几乎普遍失败（成功率0.05），即使VLA模型InternVLA-N1也未成功。  
3. **长时域导航远未解决**：最佳模型OpenPilot每100m仍有1.34次失败（主要为碰撞，1.01次/100m），意味着一次典型2km交付任务约需26.6次人工干预；平均速度在真实扫描场景中下降（因真实地形更粗糙）。  
4. **合成数据微调有效**：FlowPilot在仿真和真实场景下经过微调后，“斑马线穿越”成功率从0.11提升至0.69（仿真）/0.40（真实），“手势”场景从0.12提升至0.49（仿真）/0.50（真实），展示了合成数据弥补真实数据不足的巨大潜力。  
5. **VLA模型具有推理优势但实时控制不足**：InternVLA-N1在行人反应测试中行人碰撞率低且保持较远距离，说明其社交推理能力更强，但成功率和控制精度较差，提示结合轻量级模型的底层能力与VLA的高层理解是重要方向。

## 七、优点
- **标准化与全面性**：首次为城市人行道视觉导航建立统一基准，涵盖结构、行人、长时域三大维度，场景定义明确、可复现。  
- **仿真平台创新**：结合程序化生成与真实扫描场景，引入事件驱动的行人行为和高效的SMPL动画管线（渲染速度提升60倍以上），可支持大规模并行评测。  
- **评测覆盖广泛**：系统考察了9个代表性模型在1235个测试场景上的表现，并提供了额外指标（行人碰撞率、最小距离、失败细分类），分析深入。  
- **实用性验证**：通过真实扫描场景与真实世界微调实验，检验了Sim-to-Real泛化能力；合成数据实验展示了平台对模型训练的直接贡献。  
- **开源与社区友好**：项目页面提供视频结果和代码（计划），有助于社区复现和进一步研究。

## 八、不足与局限
1. **行人行为真实性有限**：事件行为基于规则轨迹，缺乏自然出现的微妙交互（如犹豫、非语言沟通），与真实世界行人多样性仍有差距。  
2. **动画渲染质量折衷**：为追求效率，程序化场景中使用网格纹理（视觉伪影），真实场景使用3DGS（虽有改善但与原生渲染仍有差距），可能引入Sim-to-Real gap。  
3. **真实扫描场景数量少**：仅11个街区（且长时域仅5个），不足以完全反映真实世界的多样性。  
4. **地形简化**：程序化场景地面基本平坦，而真实场景中粗糙地形导致冻结失败增加，限制了长时域测评的真实性。  
5. **机器人同质化**：主要使用四轮递送机器人，虽提供了其他 embodiments 示例，但系统的迁移性尚未在多种硬件上验证。  
6. **计算资源细节不足**：未报告模型原始训练算力和完整的训练时间，微调实验仅描述了基本策略，缺乏更严格的超参数搜索。  
7. **未评测仿真到真实的直接迁移**：合成数据微调实验仅在FlowPilot上进行，其他模型未覆盖，且未评估完整的长时域场景在真实世界中的表现，微调后真实世界实验次数较少（各10次）。

（完）
