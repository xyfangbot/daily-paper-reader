---
title: Contrast and Visibility Enhancement of Weather-Degraded Images Using Dual-Branch CNN and Transformer with Perceptual Loss for ADAS
title_zh: 用于先进驾驶辅助系统的基于双分支CNN和Transformer结合感知损失的天气退化图像对比度与可见性增强
authors: "Anmol Jain, Veerendra Yadav, Harsh Khatter"
date: 2026-06-29
pdf: "https://irojournals.com/iroiip/article/download/2295/2101"
tags: ["query:热点论文筛选", "query:world-model", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; institutions=Shiv Nadar University, Noida International University, Gautam Buddha University; query=search for world model benchmarks and datasets for evaluation"
tldr: 恶劣天气导致ADAS图像退化，现有CNN难以保留全局上下文而Transformer计算成本高。提出双分支CNN-Transformer结构，并行提取局部空间特征和全局语义，通过自适应门控融合模块整合，并采用感知损失优化纹理和结构。在BDD100K和KITTI Foggy数据集上PSNR达36.5 dB、SSIM 0.962、LPIPS 0.081，推理速度23.8 FPS，有效恢复车道边界和车辆轮廓，为自动驾驶提供高效且感知鲁棒的能见度增强方案。
source: openalex
selection_source: hot_paper_scout
motivation: 传统CNN和Transformer分别存在全局上下文缺失或高计算开销，难以同时满足ADAS对实时性和图像恢复质量的要求。
method: 双分支CNN-Transformer并行提取局部与全局特征，通过自适应门控融合模块进行可学习空间加权集成，并引入感知损失指导优化以增强纹理和结构保真度。
result: PSNR 36.5 dB、SSIM 0.962、LPIPS 0.081，推理速度23.8 FPS，在恶劣天气下显著改善车道和车辆轮廓的恢复。
conclusion: 该框架有效平衡了效率与感知质量，为自动驾驶场景下的实时图像增强提供了鲁棒且实用的解决方案。
---

## 摘要
天气可能恶劣或良好。恶劣天气（包括雾、霾、雨或低光照）会严重降低道路场景中的图像感知质量，导致基于摄像头的先进驾驶辅助系统（ADAS）性能显著下降。尽管依赖卷积网络（CNN）的传统改进技术无法有效保留图像外观改善中的全局上下文，而使用Transformer的技术则计算成本较高。这限制了它们的应用，因为实时系统效率变得至关重要。本文提出了一种基于双分支CNN Transformer的解决方案，该方案通过卷积网络和自注意力机制的并行经验共享，统一利用局部空间特征提取与全局语义建模。自适应门控融合模块通过可学习空间加权整合这些互补的局部与全局表示，而感知损失引导的优化则强调纹理保真度、结构一致性和视觉真实性。该模型在真实驾驶图像数据集（如BDD100K和KITTI Foggy数据集）上进行了测试，并与最先进的去雾网络及通用天气条件恢复网络进行了比较。所提出的模型实现了36.5 dB的PSNR、0.962的SSIM和0.081的LPIPS，同时在NVIDIA RTX 4090 GPU上记录到42毫秒/帧的推理延迟，对应23.8 FPS（约24 FPS）。定性评估进一步表明，在恶劣天气条件下，车道边界、车辆轮廓和整体场景一致性的恢复效果得到改善。这些发现表明，所提出的框架为自动驾驶场景中的可见性增强提供了一种高效且感知稳健的解决方案。

## Abstract
Weather can be either poor or good. Poor weather, includING fog, hazE, rain, or low light, can cause dramatic degradation of image perception in road-level situations, leading to with significant performance loss in camera-based Advanced Driver-Assistance Systems (ADAS), Although traditional improvement techniques relying on Convolutional Networks (CNNs) cannot effectively preserve global context in image appearance improvement, techniques using transformers show high computational costs. This restricts their application as real-time system efficiency becomes critically important. In this paper, we propose a solution using the Dual-Branch CNN Transformer, which uniformly utilizes localized spatial features extraction together with global semantic modeling using parallel experience sharing of Convolutional Networks and Self Attention Mechanisms. An adaptive gated fusion module integrates these complementary local and global representations through learnable spatial weighting, while perceptual-loss-guided optimization emphasizes texture fidelity, structural consistency, and visual realism. The model was tested on real-world driving image datasets such as BDD100K and KITTI Foggy Datasets and compared with state-of-the-art dehaze networks and general weather condition restoration networks. The proposed model achieved a PSNR of 36.5 dB, an SSIM of 0.962, and an LPIPS of 0.081 while recording an inference latency of 42 ms/frame, corresponding to 23.8 FPS (~24 FPS) on an NVIDIA RTX 4090 GPU. Qualitative evaluation further demonstrated improved restoration of lane boundaries, vehicle contours, and overall scene coherence under adverse weather conditions. These findings indicate that the proposed framework provides an efficient and perceptually robust solution for visibility enhancement in autonomous driving scenarios.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：恶劣天气（如雾、霾、雨、雪、低光照）导致车载摄像头采集的图像对比度、能见度严重下降，进而影响ADAS（先进驾驶辅助系统）中的车道识别、物体检测和语义分割等感知任务。
- **现有方法局限**：
  - 传统基于物理模型的方法（如暗通道先验）在空间变化大或混合天气条件下失效。
  - 基于CNN的方法只能提取局部空间特征，缺乏全局语义建模能力，恢复结果缺乏场景一致性。
  - 基于Transformer的方法虽能捕捉全局依赖，但计算成本高，难以满足ADAS的实时性要求。
- **研究动机**：需要一种既能高效保留局部细节（车道边缘、车辆轮廓），又能捕获全局上下文（道路几何、场景语义），同时满足实时推理要求的图像增强方法。

## 二、论文提出的方法论
- **核心思想**：采用双分支并行架构（CNN分支 + Transformer分支），分别提取局部精细特征和全局语义特征，通过自适应门控融合模块进行可学习加权融合，并引入感知损失优化，以提升纹理保真度、结构一致性和视觉真实性。
- **关键技术细节**：
  - **CNN分支**：采用堆叠的3×3卷积层、批归一化、ReLU激活和残差块，提取局部纹理、边缘等空间细节。基础通道宽度64，共10个3×3卷积层。
  - **Transformer分支**：将图像分割为16×16的patch并嵌入，通过4个Transformer块（每个块4头自注意力）建模长程依赖，嵌入维度128。
  - **自适应门控融合模块**：将CNN特征图F_c和Transformer特征图F_t对齐到相同空间分辨率后，通过1×1卷积和sigmoid激活生成空间自适应门控权重G：
    - \( G = \sigma(\text{Conv}_{1\times 1}([F_c; F_t])) \)
    - 融合特征 \( F_f = G \odot F_c + (1 - G) \odot F_t \)
  - **重建头**：经融合的特征图通过反卷积和细化层生成增强图像。
  - **损失函数**：综合使用L1损失、SSIM损失、感知损失（基于VGG/LPIPS特征空间的欧氏距离）和边缘感知损失，总损失 \( \mathcal{L}_{\text{total}} = \lambda_1 \mathcal{L}_{L1} + \lambda_2 \mathcal{L}_{\text{SSIM}} + \lambda_3 \mathcal{L}_{\text{perc}} + \lambda_4 \mathcal{L}_{\text{edge}} \)。
- **算法流程**（简化）：
  1. 输入退化图像I，调整大小并归一化至512×512。
  2. 并行通过CNN分支得到局部特征F_c，通过Transformer分支得到全局特征F_t。
  3. 对齐特征空间，通过自适应门控融合获得F_f。
  4. 重建头生成增强图像ŝ。
  5. 在训练中计算总损失并反向传播优化模型参数。

## 三、实验设计
- **数据集**：
  - **BDD100K**：10万张真实驾驶场景图像，包含雾、雨、夜间等多样天气和光照条件。
  - **KITTI Foggy**：2万+张合成雾天城市驾驶图像。
  - 数据划分：70%训练，30%验证/测试。图像统一resize至512×512，并采用随机水平翻转、随机裁剪、亮度变化等数据增强。
- **对比方法**：
  - AOD-Net、GridDehazeNet、TransWeather、Restormer、DehazeFormer、Uformer。
  - 覆盖CNN类、Transformer类及混合类方法。
- **评估指标**：PSNR、SSIM、LPIPS（越低越好）、推理延迟（ms/frame）、FPS、参数量。
- **实验类型**：
  1. **整体定量对比**：在BDD100K和KITTI Foggy上计算平均指标（表6）。
  2. **数据集特定对比**：分别报告两个数据集上的指标（表7）。
  3. **消融实验**：移除Transformer分支、移除特征融合、直连拼接+1×1投影、移除感知损失，对比完整模型（表8）。
  4. **注意力头数敏感性分析**：2头、4头、8头对比（表9）。
  5. **输入分辨率影响实验**：224×224、384×384、512×512对比（表2）。
  6. **收敛性能对比**：各模型训练损失下降曲线及最终损失值（图4、表11）。
  7. **推理速度与复杂度对比**：PSNR、延迟、参数量联合对比（表10）。
  8. **硬件效率分析**：GPU利用率、FPS、内存占用（表12）。
  9. **定性可视化对比**：展示了多组雾天驾驶场景的增强结果图（图5）。

## 四、资源与算力
- **GPU型号**：NVIDIA RTX 4090（单卡）。
- **训练配置**：Batch size=8，学习率1e-4，优化器Adam。
- **推理速度**：42 ms/帧，即约23.8 FPS（~24 FPS）。
- **模型参数量**：3.1M。
- **其他资源**：未明确提及训练总时长或GPU数量，推测为单卡训练。

## 五、实验数量与充分性
- **实验数量**：共进行了9种以上的对比/分析实验，涵盖多数据集、多指标、多模块消融、超参数敏感性、效率和可视化。
- **充分性评估**：
  - **全面性**：对比了6种以上SOTA方法（CNN、Transformer、混合型），消融实验覆盖所有关键组件，敏感性分析包含注意力头数和输入分辨率。
  - **客观性**：使用了公开标准数据集（BDD100K、KITTI Foggy），指标选择主流（PSNR、SSIM、LPIPS），但缺少下游ADAS任务（如物体检测mAP、车道分割IoU）的定量验证。
  - **公平性**：对比方法均为原始论文报告或复现的基准结果，但未明确提及是否统一训练/测试环境（如相同输入尺寸、相同硬件平台）进行复现，部分数据注明“adapted from benchmark comparisons”。
  - **潜在偏差**：KITTI Foggy为合成数据，可能高估模型对真实复杂天气的泛化能力；BDD100K包含多种天气但未按严重程度分层评估。

## 六、论文的主要结论与发现
1. **性能领先**：所提双分支CNN-Transformer模型在BDD100K和KITTI Foggy上达到PSNR 36.5 dB、SSIM 0.962、LPIPS 0.081，全面优于AOD-Net、GridDehazeNet、TransWeather、Restormer等基线。
2. **实时性可行**：推理延迟42 ms（~24 FPS），满足ADAS近实时要求，且参数仅3.1M，比纯Transformer模型更轻量。
3. **局部与全局互补生效**：CNN分支有效保留车道边界、纹理细节；Transformer分支提升场景连贯性；自适应门控融合优于简单拼接。
4. **感知损失提升视觉质量**：使用LPIPS感知损失后，LPIPS指标从0.088降至0.081，视觉更真实。
5. **注意力头数建议**：4头为最优平衡点，8头提升微小但延迟增加明显。
6. **高分辨率输入有益**：512×512效果优于384和224，说明精细结构对恢复至关重要。

## 七、优点
1. **架构设计新颖**：首次在ADAS图像增强中采用并行双分支（CNN+Transformer）+自适应门控融合，兼顾细节与全局。
2. **损失函数全面**：综合L1、SSIM、感知损失和边缘损失，从像素、结构、感知、边缘多角度约束，提升恢复真实性。
3. **实时性保障**：在保持高精度（36.5 dB PSNR）前提下，推理速度达24 FPS，适合车载嵌入式场景。
4. **消融实验扎实**：对三大核心组件（Transformer分支、融合机制、感知损失）逐一验证，结论可靠。
5. **硬件效率分析**：额外报告GPU利用率、内存占用等指标，便于实际部署评估。

## 八、不足与局限
1. **缺少下游ADAS任务评估**：仅以图像质量指标评估，未在物体检测、车道分割等实际ADAS任务上验证增强效果，导致对系统级增益的论证不足。
2. **数据集局限性**：KITTI Foggy为合成数据，真实世界的复杂天气（如混合雨雪、镜头污渍、夜晚低照）可能未被充分覆盖。BDD100K虽真实但未按天气严重程度分层分析。
3. **对比实验公平性存疑**：未明确说明是否在相同计算资源、数据预处理和训练策略下复现所有基线方法的指标，部分数据直接引用原始论文，可能存在环境不一致。
4. **未进行跨域泛化测试**：仅在两个驾驶数据集上测试，未在非驾驶场景（如监控、地面交通）验证泛化性。
5. **潜在偏差风险**：模型可能过度拟合合成天气模式（KITTI Foggy），对真实极端天气（如夜间+浓雾复合条件）的鲁棒性有待验证。
6. **未讨论失败案例**：定性展示均为成功案例，未分析模型在极端遮挡、大面积过曝或水下等罕见情况下的表现。

（完）
