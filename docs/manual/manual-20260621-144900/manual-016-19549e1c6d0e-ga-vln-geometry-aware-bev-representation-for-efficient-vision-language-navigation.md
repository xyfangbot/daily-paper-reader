---
title: "GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation"
title_zh: GA-VLN：面向高效视觉语言导航的几何感知BEV表示
authors: "Jiahao Yang, Zihan Wang, Xiangyang Li, Xing Zhu, Yujun Shen, Yinghao Xu, Shuqiang Jiang"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2605.22036v1"
arxiv_id: 2605.22036v1
arxiv_url: "https://arxiv.org/abs/2605.22036v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/016-2026_yang_ga_vln-9ca4c455-19549e1c6d0e.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2605.22036v1", "query:Vision-Language Navigation", "query:BEV representation", "query:Geometry-Aware", "query:3D foundation model", "query:Multimodal Large Language Model"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有视觉语言导航依赖密集RGB视频，产生大量补丁令牌且缺乏空间结构，导致计算冗余和空间推理受限。为此提出GA-BEV紧凑三维特征表示，通过RGB-D投影构建几何一致的鸟瞰图空间，并融入预训练3D模型的隐式结构先验。该方法显著减少令牌冗余并增强空间理解，在纯导航数据上达到最先进性能，无需额外数据增强。展示了数据高效性和鲁棒性。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 853, \"height\": 944, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1758, \"height\": 776, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1772, \"height\": 894, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1769, \"height\": 824, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1771, \"height\": 945, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1796, \"height\": 404, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1724, \"height\": 963, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1535, \"height\": 275, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1517, \"height\": 458, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 801, \"height\": 203, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1345, \"height\": 237, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 881, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 795, \"height\": 262, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 900, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-016-19549e1c6d0e-ga-vln-geometry-aware-bev-representation-for-efficient-vision-language-navigation/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 674, \"height\": 181, \"label\": \"Table\"}]"
motivation: 解决VLN中RGB视频令牌过多和空间推理不足的问题，降低计算开销。
method: 提出GA-BEV表示，结合显式深度投影和隐式3D基础模型先验，构建agent-centric BEV空间图。
result: 仅用导航数据实现SOTA，无需DAgger或混合VQA训练，表明数据高效性。
conclusion: GA-BEV紧凑且具有空间表达力，能显著提升导航效率与性能。
---

## 摘要
尽管视觉语言导航（VLN）取得了显著进展，现有方法仍依赖于密集的RGB视频，这会产生过多的patch标记且缺乏明确的空间结构，导致计算开销大且空间推理能力有限。为了解决这些问题，我们引入了几何感知BEV（GA-BEV）——一种紧凑的、基于3D的特征表示，它将显式和隐式几何线索整合到基于多模态大语言模型（MLLM）的导航系统中。我们通过将视觉特征投影到3D空间并将其聚合成以智能体为中心的布局，从RGB-D输入构建BEV空间地图，在保持几何一致性的同时减少标记冗余。为了进一步增强几何理解，我们将预训练3D基础模型的特征融入BEV空间，注入从大规模3D重建任务中学习到的结构先验。这些互补的线索——显式的基于深度的投影和隐式的学习先验——共同产生了紧凑且空间表达力强的表示，显著提高了导航效率和性能。实验表明，我们的方法仅使用导航数据即取得了最先进的结果，无需DAgger增强或混合VQA训练，证明了所提出的GA-VLN框架的鲁棒性和数据效率。

## Abstract
Despite significant progress in Vision-Language Navigation (VLN), existing approaches still rely on dense RGB videos that produce excessive patch tokens and lack explicit spatial structure, resulting in substantial computational overhead and limited spatial reasoning. To address these issues, we introduce the Geometry-Aware BEV (GA-BEV) – a compact, 3D-grounded feature representation that integrates both explicit and implicit geometric cues into multimodal large language model (MLLM) – based navigation systems. We construct BEV spatial maps from RGB-D inputs by projecting visual features into 3D space and aggregating them into an agent-centric layout that preserves geometric consistency while reducing token redundancy. To further enrich geometric understanding, we incorporate features from a pretrained 3D foundation model into the BEV space, injecting structural priors learned from large-scale 3D reconstruction tasks. Together, these complementary cues – explicit depth-based projection and implicit learned priors – yield compact yet spatially expressive representations that substantially improve navigation efficiency and performance. Experiments show that our method achieves state-of-the-art results using only navigation data, without DAgger augmentation or mixed VQA training, demonstrating the robustness and data efficiency of the proposed GA-VLN framework.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有视觉语言导航（VLN）方法依赖密集RGB视频作为输入，产生大量冗余的patch token，且缺乏显式的3D空间结构，导致计算开销大、多视图几何一致性差、空间推理能力受限。
- 尽管多模态大语言模型（MLLM）已被引入VLN以增强指令理解，但其“图像中心”范式仍然存在以上缺陷，阻碍了长时间导航中的环境记忆和空间推理。
- 本文旨在通过构建紧凑的、带3D几何信息的BEV（鸟瞰图）表示，解决上述冗余和空间结构缺失问题，从而提升导航效率和性能。

## 二、论文提出的方法论
- **核心思想**：提出Geometry-Aware BEV（GA-BEV），一种agent-centric的紧凑3D特征表示，融合显式深度引导的投影特征和隐式预训练3D模型的结构先验，替代传统密集RGB token，输入MLLM进行导航决策。
- **关键技术细节**：
  - **显式深度引导空间投影**：使用当前帧和历史帧的RGB-D观测，通过针孔相机模型将2D patch中心投影到3D世界坐标，获得3D空间中的视觉特征。
  - **隐式3D几何先验**：利用预训练3D基础模型（VGGT-1B）对图像序列编码，提取含多视图几何先验的patch特征，再通过投影层对齐维度后，同样投影到3D空间。
  - **网格BEV聚合**：将上述两类3D特征投影到agent-centric的2D BEV平面（x-z平面），划分均匀网格（默认0.25m×0.25m，范围[-10m,10m]），对落入同一网格的特征进行均值池化，并添加连续2D正弦位置编码，仅保留非空网格作为最终token。
  - **集成到MLLM导航框架**：采用两轮对话格式，第一轮使用指令、当前前视图像和GA-BEV特征预测4个动作；第二轮仅用更新后的前视图像和第一轮的BEV特征预测后续4个动作；BEV每8步更新一次。动作空间为{前进，左转，右转，停止}。
- **公式/算法流程**：文中有详细的3D投影公式（式1）、网格特征集定义（式2，实际为式4）、BEV表示公式（式3，实际为式5），以及两轮对话的输入输出说明。

## 三、实验设计
- **数据集与场景**：使用标准连续环境VLN基准R2R-CE、RxR-CE和NavRAG-CE，环境基于MP3D和HM3D数据集。训练数据混合：R2R-CE（10,819条轨迹）、RxR-CE（19,990）、EnvDrop（146,304）、ScaleVLN（155,098）、SRDF（319,022）；所有数据均为高质量导航数据，无DAgger增强或通用VQA数据集。
- **对比方法**：包括模块化规划器（CM2、LAW等）、3D端到端方法（VLN-3DFF、g3D-LF、MapNav、Dynam3D等）、基于图像MLLM的方法（NaVid、Uni-NaVid、NaVILA、StreamVLN、InternVLA-N1等）。指标：Navigation Error (NE)、Oracle Success Rate (OSR)、Success Rate (SR)、Success weighted by Path Length (SPL)。
- **消融实验**：验证BEV投影和3D几何先验的贡献、不同BEV网格大小、历史帧步数、融合策略、BEV更新步数、深度处理策略等。此外进行了传感器噪声鲁棒性测试和真实机器人定性实验。

## 四、资源与算力
- **文中未明确说明使用的GPU型号、数量、训练时长等具体算力信息**，仅提到模型基于LLaVA-Video-7B，视觉编码器SigLIP，3D基础模型VGGT-1B，训练优化使用cosine annealing学习率调度，视觉编码器学习率5e-6，其他组件2e-5，预训练2个epoch。
- 在效率分析中报告了每步推理的TFLOPs和延迟（GA-VLN约8.73 TFLOPs，258.7 ms/步），但无训练阶段资源信息。

## 五、实验数量与充分性
- 实验数量较多：主表对比（三个基准、多种方法）、消融（表2、表3、表6-9）、鲁棒性噪声测试（表4）、真实机器人实验（附图4-5）、以及大量超参数分析（网格大小、步长、融合策略等）。
- 实验设计较为充分：使用多种指标；消融覆盖关键组件；控制数据预算（是否含SRDF）证明架构贡献；在模拟器和真实机器人上验证；考虑传感器噪声鲁棒性。
- 但缺乏在不同环境类型（如室外、复杂障碍场景）上的泛化实验，且NavRAG-CE上的性能相对较低，可能存在分布偏移问题。实验公平性较好——对比方法均使用完全一致的验证集，但部分方法使用DAgger增强，而GA-VLN未使用，增加了优势。

## 六、论文的主要结论与发现
- GA-BEV表示能显著压缩视觉token（从约4000降至约500），同时提升导航性能，在R2R-CE上SR达61.0%（+4.1%相对提升），SPL达55.2%。
- GA-VLN仅用高质量导航数据即达到SOTA，无需DAgger或混合VQA，展现强数据效率和鲁棒性。
- 显式深度投影和隐式3D先验互补：仅用BEV投影即可提升性能，添加3D几何先验进一步改进，尤其在稀疏/噪声深度下更稳定。
- BEV网格大小0.25m、历史帧32步为最优权衡；融合策略采用全局均值池化优于分层均值池化。
- 真实机器人实验证明零样本泛化能力，但缺乏避障模块时路径优化不足。

## 七、优点
- **方法创新**：首次将紧凑3D BEV表示成功融入MLLM导航，结合显式和隐式几何信息，解决密集token冗余和空间缺失。
- **数据效率高**：无需DAgger或大规模VQA数据，仅用标准导航数据即达SOTA，降低工程成本。
- **计算效率高**：GA-BEV大幅减少MLLM输入token数，实测延迟和TFLOPs显著低于基线。
- **鲁棒性强**：对深度噪声、位姿漂移、旋转噪声仅轻微性能下降（<2% SR），得益于BEV聚合和3D先验的滤波作用。
- **真实世界验证**：在Hello Robot Stretch 3上成功部署，展示通用能力。

## 八、不足与局限
- **算力信息缺失**：未公开训练所需的GPU型号、数量、时长，影响可复现性评估。
- **实验覆盖有限**：主要在R2R-CE/RxR-CE/NavRAG-CE室内场景评估，缺乏对室外、动态障碍等更复杂环境的测试；NavRAG-CE上SR仅22.2%，明显低于其他基准，可能受指令风格分布偏移影响。
- **真实机器人局限性**：未集成避障模块，导致路径可能过近障碍物；离散动作粒度粗导致停止精确度不足；未与其他MLLM方法进行公平同硬件对比。
- **消融设计潜在偏差**：部分消融实验使用了不含SRDF数据集的设置，虽然说明与含SRDF趋势一致，但差异可能影响分析精确性。
- **未讨论与其他3D表示（如NeRF、高斯泼溅）的对比**，仅与部分3D端到端方法比较略简单。

（完）
