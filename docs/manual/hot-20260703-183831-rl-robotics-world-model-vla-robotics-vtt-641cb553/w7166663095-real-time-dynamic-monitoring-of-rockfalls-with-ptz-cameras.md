---
title: Real-time dynamic monitoring of rockfalls with PTZ cameras
title_zh: 基于PTZ摄像机的落石实时动态监测
authors: "Sicong Huang, Zongwang Yi, Xiaoqi Zhou, Xi Zhang, Qingshan Guo, Gang Xiao, P C. Chen"
date: 2026-06-30
pdf: "https://www.nature.com/articles/s41598-026-49008-x.pdf"
tags: ["query:热点论文筛选", "query:rl-robotics", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; institutions=Chongqing Bureau of Geology and Minerals Exploration; query=reinforcement learning for UAV path planning and control"
tldr: 落石灾害威胁生命与基础设施，需实时动态监测。本文提出结合运动感知与物理约束的PTZ相机落石检测跟踪框架：在YOLOv8中嵌入轻量时序模块增强小目标感知，用欧氏距离和运动方向替代IoU匹配以提升跟踪稳定性，通过帧差补全轨迹断裂，并采用泛化训练适应未知环境。在融合真实监控与模拟落石的数据集上，该方法在复杂背景和低帧率下检测跟踪性能优异，部署于NVIDIA Orin边缘平台实现实时监测，为地质灾害预警提供了实用方案。
source: openalex
selection_source: hot_paper_scout
motivation: 落石目标小、背景相似、运动复杂，现有方法难以可靠实时监测，亟需高效检测跟踪框架。
method: 在YOLOv8中嵌入轻量时序模块增强运动感知；用欧氏距离和运动方向替换IoU匹配；帧差补全轨迹断裂；泛化训练提升适应性。
result: 在自定义数据集上，复杂背景和低帧率下检测跟踪性能优异，边缘平台实现实时运行。
conclusion: 该框架有效解决了落石实时监测难题，为PTZ相机地质灾害预警提供了可行方案。
---

## 摘要
落石是一种常见的地质灾害，威胁生命和基础设施。除了静态评估外，实时动态监测对于捕捉突发事件、确保及时预警和减轻风险至关重要。利用低成本、灵活部署和高时空分辨率的优势，PTZ（云台变焦）摄像机结合深度学习提供了一种潜在的解决方案。然而，落石目标体积小、背景相似、运动快速且复杂，给可靠监测带来了显著挑战。为了解决这些问题，本文提出了一种融合运动感知和物理约束的落石检测与跟踪框架。首先，在YOLOv8中引入轻量级时间模块，以增强对微小和暗淡运动目标的感知。其次，基于欧氏距离和运动方向的新型匹配策略替代了ByteTrack中的传统IoU，以提高跟踪稳定性。通过基于帧差的补全机制，缓解了由漏检导致的轨迹碎片化。通过泛化训练策略进一步增强了在未见环境中的适应性。构建了一个结合真实监控和模拟落石的定制数据集。实验表明，在复杂背景和有限帧率下，该方法具有优异的检测性能、稳健的跟踪能力和强大的泛化能力。在NVIDIA Orin边缘平台上的部署实现了实时监测，并支持基于PTZ的实用地质灾害预警。

## Abstract
Rockfall is a prevalent geological hazard threatening lives and infrastructure. Beyond static assessment, real-time dynamic monitoring is crucial to capture sudden events, ensuring timely warning and risk mitigation. Leveraging low cost, flexible deployment, and high spatiotemporal resolution, PTZ (Pan-Tilt-Zoom) cameras combined with deep learning provide a potential solution. However, the small size, background similarity, rapid and complex motion of rockfall objects present significant challenges for reliable monitoring. To tackle these issues, this paper proposes a rockfall detection and tracking framework integrating motion awareness and physical constraints. First, a lightweight temporal module is incorporated into YOLOv8 to enhance perception of small and dim moving objects. Second, a novel matching strategy based on Euclidean distance and motion direction replaces the traditional IoU in ByteTrack to improve tracking stability. Trajectory fragmentation caused by missed detections is mitigated via a frame-difference-based completion mechanism. Adaptability to unseen environments is further bolstered through a generalization training strategy. A custom dataset combining real-world surveillance and simulated rockfalls was constructed. Experiments demonstrate superior detection, robust tracking, and strong generalization under complex backgrounds and limited frame rates. Deployment on NVIDIA Orin edge platforms facilitates real-time monitoring and supports practical PTZ-based early warning for geological hazards.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **落石灾害的严重性**：落石在山区频发，具有突发性、随机性，威胁人的生命和基础设施安全，可能成为大规模滑坡的前兆。实时动态监测对早期预警和风险缓解至关重要。
- **现有监测方法的局限**：地面传感器覆盖有限、维护成本高；遥感技术时间分辨率低；无人机受天气和续航限制；地面光学/激光系统成本高、处理复杂。视频监控（特别是PTZ摄像机）具备低成本、灵活部署、高时空分辨率优势，但当前基于深度学习的检测跟踪方法主要依赖静态图像外观建模，难以应对落石目标小、颜色与背景相似、运动快速且复杂（自由落体、弹跳、滚动等）的挑战。
- **核心问题**：如何在有限帧率（室外功耗受限导致低帧率）、复杂背景下，利用PTZ视频流实现小、暗淡、快速运动落石的可靠检测与稳定跟踪。
- **论文目标**：提出一个融合运动感知和物理约束的检测跟踪框架，并设计泛化训练策略提升跨场景适应性，最终在边缘计算平台实现实时动态监测。

## 二、论文提出的方法论
- **整体框架**：由运动感知检测（Motion-aware Detection）和物理约束跟踪（Physics-constrained Tracking）两个核心模块组成，辅以帧差补全机制和泛化训练策略。
- **运动感知检测**：
  - 核心思想：受生物视觉系统（无长突细胞实现时间高通滤波，神经节细胞保留运动变化）启发，利用连续多帧（三帧）堆叠输入YOLOv8，在通道维度拼接形成9×H×W输入，使卷积核能捕获像素与时颜色变化差异，增强动态目标的显著性。
  - 特点：轻量级，仅修改输入通道数，不改变网络结构；隐式编码短期RGB演化，无需光流或3D卷积；在保持实时性同时显著提升小目标/暗淡目标检测能力。
- **物理约束跟踪**：
  - 基础追踪器：ByteTrack（基于检测的跟踪），但原IoU匹配不适用于小、快速、非线性运动的落石（低帧率下IoU趋近于零）。
  - 创新匹配策略：采用欧氏距离（ED）和运动方向（Motion Direction）替代IoU，设计两阶段匹配：
    - 阶段1（快速匹配）：基于欧氏距离阈值d1进行贪婪匹配，处理稳定/慢速轨迹。
    - 阶段2（精细匹配）：对d1~d2范围内的候选，使用SVD估计轨迹主方向，计算检测点与历史方向夹角θ，若θ > θ_th则丢弃；对剩余候选计算归一化距离和角度的乘积作为联合代价Score，进行贪婪匹配。
    - 优点：不依赖外观特征，鲁棒性强且实时性好。
- **帧差补全机制**：
  - 问题：高速度+低帧率导致漏检，造成轨迹断裂。
  - 方法：采用三帧差分法提取运动候选区域（二值化、形态学操作、轮廓提取、面积过滤、与检测框IoU抑制），将运动候选作为低置信度检测加入ByteTrack第二阶段进行关联，成功匹配后更新轨迹，恢复漏检造成的断裂。
- **泛化训练策略**：
  - 两阶段训练：预训练（使用模拟落石视频+任务无关数据增强）→ 微调（针对目标场景使用拷贝粘贴合成 + 微弱增强）。
  - 数据增强技巧：背景多样化、虚拟行人合成（利用Penn-Fudan Pedestrian数据集，模拟行人运动以降低虚假报警）。
- **具体参数**：检测器YOLOv8s，SGD优化器，初始学习率0.01，训练300 epochs，batch size 8，余弦退火学习率调度；检测置信度阈值0.3，NMS阈值0.5；跟踪置信度阈值0.5。

## 三、实验设计
- **数据集**：自建多源落石数据集，包含15个典型地质环境场景（山区斜坡、冲沟、路边坡、水库岸边等），来自重庆活动山区和三峡库区。
  - 模拟落石视频：40段，约10,500帧，人工抛掷岩石并标注。
  - 真实监控视频：10段，约5,000帧（无落石事件，用于背景多样性）。
  - 图像分辨率：1440×2560像素（2K），原始帧率25fps，下采样至10fps处理。
  - 训练/验证/测试按6:3:1比例划分，测试场景与训练集无重叠（跨场景评估）。
  - 目标尺寸：绝大多数小于100×100像素，多数低于50×50像素（小目标特性）。
- **对比方法**：
  - 检测任务：三帧差分法、单帧YOLOv8、单帧YOLOv8+三帧差分、三帧YOLOv8+三帧差分、DSF-Net（3D卷积时序检测网络）。
  - 跟踪任务：原始IoU匈牙利匹配ByteTrack（vanilla）、基于欧氏距离的匹配、以及本文物理约束匹配。
  - 消融实验：逐步添加运动感知检测、泛化训练、物理约束跟踪、帧差补全机制。
  - 超参数分析：运动方向阈值θ_th从10°到170°；视频帧率从1到25fps。
- **评估指标**：
  - 检测：Precision (P), Recall (R), F1-score。
  - 跟踪：MOTA, IDF1, IDs（身份切换次数）。
  - 事件级评估（低帧率分析）：事件召回率、事件精确率。

## 四、资源与算力
- **训练服务器**：NVIDIA TITAN RTX GPU（24GB显存），Ubuntu 20.04，Python 3.10，PyTorch 2.0，CUDA 11.7。
- **边缘部署**：NVIDIA Orin边缘设备（具体型号未说明），采用Int8量化 + 多线程并行优化。
- **训练时长**：文中未明确给出单次训练时长，但300 epochs、batch size 8在单GPU上预计需要数小时（图像尺寸大2K）。
- **模型复杂度**：三帧YOLOv8参数11.14M，FLOPs 261.04G（略高于单帧11.13M/255.94G）；DSF-Net FLOPs 1426.24G，很大。跟踪阶段额外计算量较小（物理约束ByteTrack约33 FPS on server，帧差补全后23.52 FPS）。

## 五、实验数量与充分性
- **实验组数量**：总量充分。
  - 总体消融实验（表2）：5种配置（baseline + 运动检测 + 泛化训练 + 物理约束跟踪 + 帧差补全）在验证/测试集上检测与跟踪指标。
  - 检测对比（表3）：6种方法（三帧差分、单帧YOLOv8、三帧YOLOv8等）。
  - 训练策略分析（图7、图8）：预训练阶段3种增强组合；微调阶段5种组合。
  - 跟踪匹配策略对比（表4）：3种匹配方式。
  - 帧差补全效果（表5）：有无对比。
  - 帧率影响（表7）：5种帧率。
  - 方向阈值影响（表8）：9个阈值。
  - 模型复杂度与效率（表6）：8种Detector/Tracker组合。
  - 可视化分析（图9-15）：多种运动模式（自由落体、滚动、弹跳）及典型场景对比。
- **充分性**：实验设计比较全面，涵盖检测、跟踪、泛化、超参数、推理效率多个维度，且采用了跨场景测试（测试集场景未见于训练集），保证了公正性。但缺少与最新多目标跟踪方法（如BoT-SORT、StrongSORT）的对比；事件级评估仅用于帧率分析，未在全文跟踪消融中使用。
- **客观性与公平性**：对比方法为公认基线（YOLOv8、ByteTrack、DSF-Net），超参数固定，控制变量合理。但自己构建的数据集缺乏公开基准对比，难以直接与其他论文比较绝对数值。

## 六、论文的主要结论与发现
- 运动感知检测（三帧堆叠输入）相比单帧YOLOv8：在验证集F1从60.09%提升至82.99%（+22.9%），召回率提升超30%，且仅增加极少计算量。
- 泛化训练策略有效缓解域偏移：测试集F1从45.09%提升至79.22%（+34.1%）。
- 物理约束匹配（欧氏距离+方向）显著优于原始IoU匹配：MOTA从0%（IoU完全失败）提升至68.40%，IDF1达75.93%，ID从35降至11。
- 帧差补全机制进一步改善：Recall +1.6%，MOTA +0.73%，ID从11降至6。
- 事件级检测在10fps以上保持近100%召回，但低于5fps退化严重。
- 方向阈值在70°左右取得最佳平衡（MOTA 68.40%，IDF1 75.93%），过小导致轨迹断裂，过大导致ID混淆。
- 边缘部署：在NVIDIA Orin上，Int8量化+多线程优化后实现约12fps实时运行（2K分辨率），满足野外实时监测需求。

## 七、优点
- **创新性**：
  - 将多帧堆叠输入用于小目标运动感知，简单高效，不依赖额外模块。
  - 提出基于欧氏距离和运动方向的物理约束匹配策略，有效解决低帧率下小快速目标IoU失效问题。
  - 帧差补全机制利用传统运动检测补偿深度学习漏检，协同提升跟踪完整性。
  - 泛化训练结合拷贝粘贴合成和虚拟行人，增强跨场景鲁棒性并抑制虚假报警。
- **实用性**：整套方法在边缘设备上达到实时（12fps on Orin），具备实际部署价值。
- **实验充分**：消融实验系统全面，对各模块贡献给出量化评估；超参数分析（帧率、阈值）提供实用指导；可视化分析直观展示跟踪行为。

## 八、不足与局限
- **实验局限性**：
  - 数据集为自建，缺乏与公开落石基准（如Rockfall Detection Benchmark）的直接对比，绝对性能可比性弱。
  - 未与多目标跟踪SOTA（如BoT-SORT、StrongSORT、FairMOT）在相同框架下对比，仅对比了ByteTrack的变体。
  - 事件级评估仅用于帧率分析，未在跟踪指标中使用，可能掩盖低帧率下跟踪退化。
- **方法局限**：
  - 未处理落石碎裂（single-to-multiple transitions）导致的对象关联问题。
  - 未考虑碰撞引起的灰尘遮挡、夜间红外照明吸引昆虫导致的密集噪声、雨雪天气图像退化。
  - 弹跳引起的方向突变仅通过阈值松弛部分处理，缺乏离线轨迹重建机制（如StrongSORT中的轨迹合并）。
  - 依赖启发式规则（方向阈值手动设定），缺乏自适应调整方案。
- **应用限制**：仅针对简单运动模式（自由落体、滚动、弹跳），对更复杂场景（多落石同时运动、遮蔽等）鲁棒性待验证。

（完）
