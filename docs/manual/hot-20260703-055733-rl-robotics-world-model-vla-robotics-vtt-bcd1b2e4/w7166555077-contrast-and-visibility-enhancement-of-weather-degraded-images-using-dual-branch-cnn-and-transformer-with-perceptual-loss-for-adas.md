---
title: Contrast and Visibility Enhancement of Weather-Degraded Images Using Dual-Branch CNN and Transformer with Perceptual Loss for ADAS
title_zh: 面向ADAS的恶劣天气图像对比度与可见度增强：使用双分支CNN与Transformer结合感知损失
authors: "Anmol Jain, Veerendra Yadav, Harsh Khatter"
date: 2026-06-29
pdf: "https://irojournals.com/iroiip/article/download/2295/2101"
tags: ["query:热点论文筛选", "query:world-model", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; institutions=Shiv Nadar University, Noida International University, Gautam Buddha University; query=search for world model benchmarks and datasets for evaluation"
tldr: 恶劣天气导致ADAS摄像头图像退化。传统CNN难以保持全局上下文，Transformer计算成本高。提出双分支CNN-Transformer并行提取局部与全局特征，自适应门控融合模块整合，感知损失优化纹理与结构。在BDD100K和KITTI Foggy上PSNR 36.5 dB、SSIM 0.962、LPIPS 0.081，推理速度23.8 FPS。为自动驾驶提供高效且感知鲁棒的图像增强方案。
source: openalex
selection_source: hot_paper_scout
motivation: 现有方法不能同时兼顾全局上下文保持和实时性，需要一种高效且感知鲁棒的天气退化图像增强方法。
method: 双分支CNN和Transformer并行提取局部空间与全局语义特征，自适应门控融合模块整合，感知损失引导优化纹理、结构和视觉真实感。
result: 在BDD100K和KITTI Foggy数据集上PSNR 36.5 dB、SSIM 0.962、LPIPS 0.081，推理延迟42 ms/帧（23.8 FPS）。
conclusion: 提出框架为自动驾驶恶劣天气下的可见性增强提供了高效且感知鲁棒的解决方案，兼顾图像质量和实时性。
---

## 摘要
天气状况可好可坏。恶劣天气，包括雾、霾、雨或低光照，会导致道路场景中图像感知的显著退化，进而造成基于摄像头的先进驾驶辅助系统（ADAS）性能大幅下降。尽管依赖卷积神经网络（CNN）的传统改进技术无法在图像外观增强中有效保留全局上下文，而使用Transformer的技术则计算成本高昂。这限制了它们的应用，因为实时系统效率变得至关重要。本文提出了一种基于双分支CNN-Transformer的解决方案，该方案通过并行共享卷积网络和自注意力机制的经验，统一利用局部空间特征提取与全局语义建模。自适应门控融合模块通过可学习的空间权重整合这些互补的局部和全局表示，同时感知损失引导的优化强调纹理保真度、结构一致性和视觉真实性。该模型在真实驾驶图像数据集（如BDD100K和KITTI Foggy数据集）上进行了测试，并与最先进的去雾网络和通用天气条件恢复网络进行了比较。所提模型在NVIDIA RTX 4090 GPU上实现了PSNR为36.5 dB、SSIM为0.962、LPIPS为0.081，推理延迟为42毫秒/帧，对应23.8 FPS（约24 FPS）。定性评估进一步表明，在恶劣天气条件下，车道边界、车辆轮廓以及整体场景连贯性的恢复效果得到了改善。这些发现表明，所提框架为自动驾驶场景下的可见度增强提供了一种高效且感知鲁棒的解决方案。

## Abstract
Weather can be either poor or good. Poor weather, includING fog, hazE, rain, or low light, can cause dramatic degradation of image perception in road-level situations, leading to with significant performance loss in camera-based Advanced Driver-Assistance Systems (ADAS), Although traditional improvement techniques relying on Convolutional Networks (CNNs) cannot effectively preserve global context in image appearance improvement, techniques using transformers show high computational costs. This restricts their application as real-time system efficiency becomes critically important. In this paper, we propose a solution using the Dual-Branch CNN Transformer, which uniformly utilizes localized spatial features extraction together with global semantic modeling using parallel experience sharing of Convolutional Networks and Self Attention Mechanisms. An adaptive gated fusion module integrates these complementary local and global representations through learnable spatial weighting, while perceptual-loss-guided optimization emphasizes texture fidelity, structural consistency, and visual realism. The model was tested on real-world driving image datasets such as BDD100K and KITTI Foggy Datasets and compared with state-of-the-art dehaze networks and general weather condition restoration networks. The proposed model achieved a PSNR of 36.5 dB, an SSIM of 0.962, and an LPIPS of 0.081 while recording an inference latency of 42 ms/frame, corresponding to 23.8 FPS (~24 FPS) on an NVIDIA RTX 4090 GPU. Qualitative evaluation further demonstrated improved restoration of lane boundaries, vehicle contours, and overall scene coherence under adverse weather conditions. These findings indicate that the proposed framework provides an efficient and perceptually robust solution for visibility enhancement in autonomous driving scenarios.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 恶劣天气（雾、霾、雨、低光照）会严重降级车载摄像头图像质量，导致先进驾驶辅助系统（ADAS）的感知（如车道识别、目标检测、语义分割）性能大幅下降。
- 传统基于先验的物理模型（如暗通道先验）在复杂场景下易失效；基于CNN的方法虽有效，但受限于局部感受野，无法捕获全局语义上下文；基于Transformer的方法可建模全局依赖，但计算成本高，难以满足ADAS的实时性要求。
- 当前方法普遍忽视感知质量（如LPIPS）的优化，且缺乏针对ADAS场景的局部细节与全局一致性兼备的融合架构。
- **核心目标**：提出一种高效、感知鲁棒的双分支CNN-Transformer架构，在保持实时性的同时提升恶劣天气下图像的对比度与可见度，以支持ADAS应用。

## 二、论文提出的方法论
- **总体框架**：采用双分支并行结构——CNN分支负责提取局部纹理与边缘细节（如车道线、车辆轮廓），Transformer分支负责捕获全局语义与长程依赖（如道路几何、场景整体性）。
- **关键技术细节**：
  - CNN分支：使用堆叠的3×3卷积层、批归一化、ReLU激活和残差块，共计10层卷积，基本通道数64。
  - Transformer分支：将图像分割为16×16的patch，嵌入维度128，采用4个Transformer块、每块4个注意力头。
  - **自适应门控融合模块**：先将两个分支的特征图对齐到相同空间分辨率，然后通过1×1卷积和Sigmoid生成空间权重G，融合后特征为 F_f = G ⊙ F_c + (1-G) ⊙ F_t，实现每个位置局部与全局特征的动态平衡。
  - **损失函数**：总损失 ℒ_total = λ₁ℒ_L1 + λ₂ℒ_SSIM + λ₃ℒ_perc + λ₄ℒ_edge，其中ℒ_perc基于VGG/LPIPS特征空间距离，ℒ_edge为边缘梯度损失。
- **算法流程**：输入退化图像 → 预处理（resize至512×512，归一化） → 并行CNN和Transformer分支提取特征 → 自适应门控融合 → 重建头生成增强图像 → 计算总损失反向传播优化（使用Adam，lr=1e-4）。

## 三、实验设计
- **数据集**：
  - BDD100K：10万张真实驾驶场景，包含雾、雨、夜晚等多样天气，分辨率多样。
  - KITTI Foggy：2万+张合成雾天城市驾驶图像，雾分布均匀。
  - 数据划分：70%训练，30%验证/测试。使用随机水平翻转、随机裁剪、亮度变化进行数据增强。
- **Benchmark与对比方法**：
  - AOD-Net、GridDehazeNet、TransWeather、Restormer（主对比），另补充DehazeFormer、Uformer进行效率对比。
- **评价指标**：PSNR、SSIM、LPIPS（越低越好）、推理时间（毫秒/帧）和FPS。
- **实验设置**：输入分辨率512×512，batch size=8，学习率1e-4，Adam优化器，NVIDIA RTX 4090 GPU。

## 四、资源与算力
- 使用1块NVIDIA RTX 4090 GPU。
- 训练配置：batch size=8，学习率1e-4，Adam优化器。
- **训练时长未明确说明**。
- 推理延迟：42 ms/帧（约23.8 FPS），模型参数量3.1M。

## 五、实验数量与充分性
- **定量对比**（表6、表7）：在两个数据集上对比了7个模型，报告了PSNR、SSIM、LPIPS，分数据集给出详细结果。
- **消融实验**（表8）：移除Transformer分支、移除特征融合、直接拼接融合、移除感知损失，验证各组件贡献。
- **输入分辨率影响**（表2）：比较224×224、384×384、512×512，证明高分辨率的重要性。
- **注意力头数敏感性**（表9）：测试2、4、8个头，4头为最佳权衡。
- **收敛性对比**（图4、表11）：画出训练损失曲线，显示所提方法收敛最快且最终损失最低。
- **硬件效率分析**（表12）：对比GPU利用率、FPS、内存占用，显示所提方法在效率与精度间取得良好平衡。
- **实验充分性**：涵盖了多个维度（不同数据集、多种对比方法、消融、敏感性、收敛、硬件），对比方法选取了近年代表性工作，实验设置公平（相同GPU平台），消融实验直接验证了设计和感知损失的有效性。

## 六、论文的主要结论与发现
- 所提双分支CNN-Transformer架构在BDD100K和KITTI Foggy上达到PSNR=36.5 dB、SSIM=0.962、LPIPS=0.081，全面优于所有对比方法（包括Restormer、TransWeather等）。
- 推理速度约24 FPS（42ms/帧），满足实时ADAS需求，且参数量仅3.1M，优于其他Transformer模型。
- 定性结果（图5）显示：恢复后的车道线更清晰、车辆边界更锐利、场景整体一致性更好，显著改善雾天/雨天图像可见度。
- 自适应门控融合能有效平衡局部细节与全局语义；感知损失指导的优化提升了视觉真实感。
- 该方法为ADAS恶劣天气可见度增强提供了高效且感知鲁棒的解决方案。

## 七、优点
- **架构创新**：双分支并行设计兼顾局部纹理（CNN）与全局语义（Transformer），并通过可学习的空间门控进行自适应融合，而非简单的拼接或相加。
- **感知优化**：引入基于深度特征的感知损失（LPIPS）和边缘损失，使恢复结果更符合人类视觉感知，减少过度平滑和伪影。
- **实验全面**：除了标准定量指标，还进行了消融、敏感性、收敛性、硬件效率分析，论证了各设计的必要性和实际可行性。
- **实时性**：在RTX 4090上达到~24 FPS，接近实时推理，并评估了GPU利用率和内存占用，对车载嵌入部署有参考价值。

## 八、不足与局限
- **缺少下游任务评估**：论文仅评估了图像恢复指标，未在目标检测、车道分割等ADAS实际任务上验证增强效果的获益，这削弱了“为ADAS”的主张。
- **数据集局限性**：KITTI Foggy为合成雾图，与真实复杂天气（如混合雨雪、动态雾）存在差距；BDD100K虽是真实场景，但恢复结果在极端恶劣条件下的泛化能力未充分测试。
- **训练/推理硬件单一**：仅在RTX 4090上测试，未在低功耗边缘计算平台（如NVIDIA Xavier/Orin）上实际部署验证，论文中提及的“适用于嵌入系统”缺乏实证。
- **未对比所有最新方法**：部分近期工作（如DehazeFormer、Uformer）仅在效率对比中简单提及，未在全面定量表中并列比较PSNR/SSIM。
- **文内有少量笔误**：如“LIPPS”应为“LPIPS”，“Sigmoid”拼写等，虽不影响理解，但表明审校不够严谨。

（完）
