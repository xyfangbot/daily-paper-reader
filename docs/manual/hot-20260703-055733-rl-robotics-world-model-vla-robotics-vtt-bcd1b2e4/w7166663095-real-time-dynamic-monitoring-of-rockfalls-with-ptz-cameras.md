---
title: Real-time dynamic monitoring of rockfalls with PTZ cameras
title_zh: 使用PTZ摄像机的落石实时动态监测
authors: "Sicong Huang, Zongwang Yi, Xiaoqi Zhou, Xi Zhang, Qingshan Guo, Gang Xiao, P C. Chen"
date: 2026-06-30
pdf: "https://www.nature.com/articles/s41598-026-49008-x.pdf"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; institutions=Chongqing Bureau of Geology and Minerals Exploration; query=reinforcement learning for UAV path planning and control"
tldr: 落石灾害威胁生命与基础设施，需要实时动态监测。本文利用低成本、灵活的PTZ摄像头与深度学习，提出融合运动感知和物理约束的检测跟踪框架：在YOLOv8中加入轻量时序模块增强对小运动目标的感知，用欧氏距离和运动方向匹配替代传统IoU提升ByteTrack稳定性，并通过帧差补全机制减少轨迹断裂。实验在自制数据集上表现优越，泛化能力强，部署于NVIDIA Orin边缘平台实现实时预警，为地质灾害监测提供实用方案。
source: openalex
selection_source: hot_paper_scout
motivation: 落石目标小、背景相似且运动快速复杂，现有方法难以实现稳定实时监测，需提升检测跟踪的鲁棒性。
method: 在YOLOv8中加入时序模块捕捉微小运动目标；用欧氏距离和运动方向匹配替代IoU改进ByteTrack；通过帧差补全和泛化训练增强稳定性与适应性。
result: 在真实监控与模拟落石数据集上检测精度高、跟踪鲁棒，泛化到未见环境表现良好，边缘设备上实现实时运行。
conclusion: 该框架有效提升了PTZ相机对落石的动态监测能力，为地质灾害预警提供了低成本、高可靠的技术支撑。
---

## 摘要
落石是一种常见的地质灾害，威胁生命与基础设施。除静态评估外，实时动态监测对于捕捉突发事件、确保及时预警和降低风险至关重要。凭借低成本、灵活部署和高时空分辨率，PTZ（云台变焦）摄像机结合深度学习提供了一种潜在的解决方案。然而，落石目标尺寸小、背景相似度高、运动快速且复杂，给可靠监测带来了重大挑战。为解决这些问题，本文提出了一种融合运动感知与物理约束的落石检测与跟踪框架。首先，将轻量级时序模块融入YOLOv8，以增强对弱小运动目标的感知能力。其次，提出一种基于欧氏距离和运动方向的新型匹配策略，替代ByteTrack中的传统交并比（IoU），以提高跟踪稳定性。通过基于帧差法的轨迹补全机制，减轻因漏检导致的轨迹断裂问题。通过泛化训练策略进一步增强了在未见环境中的适应性。构建了一个结合真实监测与模拟落石的自定义数据集。实验表明，该方法在复杂背景和有限帧率下具有优越的目标检测、稳健的跟踪和强大的泛化能力。部署于NVIDIA Orin边缘平台可促进实时监测，并支持基于PTZ的地质灾害实用化预警。

## Abstract
Rockfall is a prevalent geological hazard threatening lives and infrastructure. Beyond static assessment, real-time dynamic monitoring is crucial to capture sudden events, ensuring timely warning and risk mitigation. Leveraging low cost, flexible deployment, and high spatiotemporal resolution, PTZ (Pan-Tilt-Zoom) cameras combined with deep learning provide a potential solution. However, the small size, background similarity, rapid and complex motion of rockfall objects present significant challenges for reliable monitoring. To tackle these issues, this paper proposes a rockfall detection and tracking framework integrating motion awareness and physical constraints. First, a lightweight temporal module is incorporated into YOLOv8 to enhance perception of small and dim moving objects. Second, a novel matching strategy based on Euclidean distance and motion direction replaces the traditional IoU in ByteTrack to improve tracking stability. Trajectory fragmentation caused by missed detections is mitigated via a frame-difference-based completion mechanism. Adaptability to unseen environments is further bolstered through a generalization training strategy. A custom dataset combining real-world surveillance and simulated rockfalls was constructed. Experiments demonstrate superior detection, robust tracking, and strong generalization under complex backgrounds and limited frame rates. Deployment on NVIDIA Orin edge platforms facilitates real-time monitoring and supports practical PTZ-based early warning for geological hazards.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 落石是山区常见的地质灾害，具有突发性、偶发性，威胁生命和基础设施。现有监测方法（地面传感器、遥感、无人机、地面激光等）存在成本高、覆盖有限、时间分辨率低等局限。
- PTZ摄像机结合深度学习提供低成本、灵活部署、高时空分辨率的潜在解决方案。但落石目标尺寸小、与背景相似、运动快速且复杂，导致传统基于静态图像的检测方法效果差。
- 现有研究多依赖外观建模，难以捕捉真实落石场景中的运动信息。跟踪方面，传统IoU匹配对快速小目标失效，匈牙利算法忽略运动合理性。
- 本文核心问题：如何在PTZ视频流中实现小目标、弱外观、快运动落石的可靠检测与跟踪，并保证实时性和泛化能力。

## 二、论文提出的方法论
- **整体框架**：提出运动感知检测与物理约束跟踪框架，包含四个主要模块。
- **运动感知目标检测**：
  - 将连续三帧RGB图像沿通道方向堆叠（9通道输入），轻量级建模局部时序动态，无需修改网络架构。
  - 卷积核自动捕捉帧间颜色和位置变化的时序差异，增强动态区域显著性，提升对弱小运动目标的检测。
  - 基于YOLOv8实现，仅修改输入通道数，计算量基本不变。
- **物理约束目标跟踪**：
  - 基于ByteTrack框架，用欧氏距离替代IoU作为主要匹配标准，解决小物体快速运动导致IoU接近零的问题。
  - 引入运动方向约束：通过奇异值分解（SVD）估计历史轨迹主方向，计算当前检测方向与主方向的夹角，筛选符合惯性方向的目标。
  - 两阶段匹配：第一阶段用较小距离阈值快速匹配；第二阶段对剩余候选进行方向一致性检查，并构建联合代价（归一化距离×归一化角度）进行贪婪匹配。
- **帧差补全机制**：
  - 使用三帧差分法提取运动候选区域，经二值化、形态学处理、轮廓提取、面积过滤、冗余框抑制后，与低置信度检测一起送入ByteTrack第二阶段。
  - 成功匹配的候选视为漏检补偿，更新轨迹，提高召回率和连续性。
- **泛化训练策略**：
  - **预训练阶段**：使用任务无关数据增强（亮度抖动、随机缩放、翻转、马赛克）和背景多样化（真实监测图像）、虚拟行人合成（用Penn-Fudan Ped数据集行人模拟干扰）。
  - **微调阶段**：针对目标场景，采用复制-粘贴合成（从模拟视频中提取三帧连续目标切片，随机缩放到新背景上并保持相对位移），加轻度增强。
  - 两者结合实现从通用到特定场景的适应，同时减少对行人干扰的误报。

## 三、实验设计
- **数据集**：
  - 自建多源落石数据集：PTZ摄像机部署于重庆山区和三峡库区（15个监测场景）。包含40段模拟落石视频（约10500帧，人工标注）和10段真实无落石监控视频（约5000帧，用于背景多样性和假阳性评估）。
  - 白天不同天气（晴、阴、风）录制，分辨率1440×2560（2K），原始帧率25fps，模拟边缘设备限制下采样至10fps处理。
  - 训练/验证/测试集按6:3:1划分，测试场景与训练验证不重叠。训练验证集共8885个标注实例，测试集1033个实例。物体大小绝大多数小于50×50像素，呈小目标特征。
- **对比方法**：
  - 检测对比：三帧差分法、单帧YOLOv8、单帧YOLOv8+三帧差分、三帧YOLOv8+三帧差分、DSF-Net（3D卷积时序模型）。
  - 跟踪对比：原始IoU匈牙利匹配（vanilla ByteTrack）、欧氏距离匹配、本文物理约束匹配。
  - 消融实验：基线→+运动感知→+泛化训练→+物理约束跟踪→+帧差补全。
  - 帧率影响实验：25/10/5/3/1 fps下事件级检测性能。
  - 方向阈值θ_th影响实验：10°~170°扫描。
- **评价指标**：检测采用精确率P、召回率R、F1；跟踪采用MOTA、IDF1、ID Switch（IDs）；事件级检测采用事件召回率和事件精确率。
- **训练配置**：YOLOv8s，SGD优化器，初始学习率0.01，余弦退火，batch size 8，300 epochs；检测置信度阈值0.3，NMS阈值0.5；跟踪置信度阈值0.5。

## 四、资源与算力
- 训练服务器：NVIDIA TITAN RTX GPU（文中未明确数量，推测至少1张），Ubuntu 20.04，Python 3.10，PyTorch 2.0，CUDA 11.7。
- 推理部署：NVIDIA Orin边缘设备，采用Int8量化和多线程并行优化，用于验证实时性能。
- 模型复杂度：三帧YOLOv8参数11.14M，FLOPs 261.04G；单帧YOLOv8参数11.13M，FLOPs 255.94G；DSF-Net FLOPs 1426.24G。
- 训练时长未明确说明。

## 五、实验数量与充分性
- 实验组数较多：整体消融实验（5个模块累积）、检测方法对比（5种方法）、跟踪匹配策略对比（3种）、帧率影响（5个水平）、方向阈值影响（9个水平）、泛化训练策略分阶段分析（预训练4种组合、微调5种组合）。总计约15组以上。
- 实验覆盖了核心模块、关键参数、场景泛化、帧率鲁棒性、边缘部署实时性等方面，比较充分。
- 公平性：对比实验使用相同网络架构和训练配置；测试场景与训练验证不重叠，避免数据泄露；消融实验采用累积添加方式，清晰展示每个模块贡献。
- 不足：缺少与近期其他落石检测方法的直接对比（如基于注意力机制的YOLOv7变体等）；跟踪实验仅在同一检测结果上对比匹配策略，未在不同检测器下联合评估；方向阈值选择基于经验扫描，未提供自动优化机制。

## 六、论文的主要结论与发现
- 运动感知检测（三帧输入）比单帧YOLOv8显著提升F1（从60.09%到82.99%），验证时序信息对小目标检测的重要性。
- 泛化训练策略（预训练+微调）有效解决跨场景泛化问题，测试集F1从45.09%提升至79.22%。
- 物理约束跟踪（欧氏距离+方向）相比IoU匹配（完全失效）和纯距离匹配（MOTA 35.22%、ID Switch 35），实现MOTA 68.40%、ID Switch 11，大幅提升跟踪稳定性。
- 帧差补全机制进一步将MOTA提升至69.13%，ID Switch降至6，减少轨迹断裂。
- 帧率实验表明：≥10 fps时事件级召回接近100%；低于5 fps性能急剧下降。
- 方向阈值θ_th存在最佳范围（约70°~90°），平衡轨迹连续性与ID稳定性；过小导致断裂，过大增加误关联。
- 边缘部署：三帧YOLOv8在Orin上Int8量化达12.39 FPS，结合跟踪后约12 FPS，满足实时需求。

## 七、优点
- **方法创新**：轻量级时序模块（三帧堆叠）简单有效，不改变网络结构，易于集成；用欧氏距离+方向约束替代IoU，针对落石运动物理特性设计，解决了快速小目标跟踪难题；帧差补全机制与泛化训练策略实用性强。
- **实验设计全面**：多维度消融、帧率敏感性、参数扫描、泛化分析，结论扎实。
- **工程实用性**：在边缘设备上实现实时运行，验证了PTZ系统应用于地质灾害预警的可行性。
- **数据集建设**：构建了包含真实监控和模拟落石的多场景数据集，涵盖小目标分布，为后续研究提供基准。
- **可解释性**：跟踪行为可视化（自由落体、滚落、弹跳三种运动状态），直观展示算法鲁棒性。

## 八、不足与局限
- **实验覆盖不足**：缺少与近期更先进方法（如YOLOv11、3D卷积跟踪器）的比较；未分析夜间、雨雾、灰尘遮挡等恶劣天气下的性能。
- **对复杂事件建模有限**：未处理岩石碰撞碎裂（单目标变多目标）场景；红外夜间监控下昆虫聚集造成密集运动噪声问题未解决。
- **方向阈值依赖经验**：阈值选择对性能敏感，且不同场景最优值可能不同，文中未提供自适应策略。
- **数据集规模有限**：真实落石事件稀少，模拟数据与真实场景仍有差异，可能导致泛化能力仍不足。
- **跟踪延迟问题**：帧差补全机制引入额外处理，系统FPS略有下降（23.52 vs 33.09），在更高分辨率或更低算力设备上可能成为瓶颈。
- **未公开代码或数据集**：仅声明数据按需提供，可复现性受限。

（完）
