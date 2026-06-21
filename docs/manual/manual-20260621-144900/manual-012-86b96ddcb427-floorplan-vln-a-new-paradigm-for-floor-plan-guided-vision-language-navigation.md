---
title: "FloorPlan-VLN: A New Paradigm for Floor Plan Guided Vision-Language Navigation"
title_zh: FloorPlan-VLN：一种基于楼层平面图引导的视觉-语言导航新范式
authors: "Kehan Chen, Yan Huang, Dong An, Jiawei He, Yifei Su, Jing Liu, Nianfeng Liu, Liang Wang"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2603.17437v1"
arxiv_id: 2603.17437v1
arxiv_url: "https://arxiv.org/abs/2603.17437v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/012-2026_chen_floorplan_vln-f09f5de4-86b96ddcb427.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2603.17437v1", "query:Vision-Language Navigation", "query:Floor Plan", "query:Spatial Intelligence", "query:Multimodal Large Language Models"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "现有视觉语言导航依赖冗长指令，缺乏对楼层平面图等全局空间先验的利用。为此，提出FloorPlan-VLN新范式，构建包含10k余条轨迹和语义楼层平面图的数据集，并设计FP-Nav方法，通过双视图时空对齐视频序列与辅助推理任务对齐观测、平面图和指令。实验表明，该方法在导航成功率上相对最优基线提升超60%，且在噪声和真实场景中表现鲁棒，展现了楼层平面图引导导航的有效性。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1826, \"height\": 820, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1859, \"height\": 575, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 906, \"height\": 287, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 904, \"height\": 580, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1853, \"height\": 696, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 909, \"height\": 742, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 908, \"height\": 386, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 903, \"height\": 464, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 897, \"height\": 387, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1840, \"height\": 433, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 902, \"height\": 1648, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1747, \"height\": 690, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 851, \"height\": 786, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1821, \"height\": 512, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1873, \"height\": 218, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1863, \"height\": 192, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1869, \"height\": 468, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 921, \"height\": 708, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 923, \"height\": 195, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 924, \"height\": 264, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 925, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 924, \"height\": 189, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-012-86b96ddcb427-floorplan-vln-a-new-paradigm-for-floor-plan-guided-vision-language-navigation/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 915, \"height\": 192, \"label\": \"Table\"}]"
motivation: 现有视觉语言导航忽略楼层平面图等全局空间先验，导致对空间结构推理能力不足。
method: 构建FloorPlan-VLN数据集，提出FP-Nav方法，使用双视图时空对齐视频序列及辅助推理任务对齐观测、平面图和指令。
result: "在FloorPlan-VLN基准上相对最优基线导航成功率提升超60%，且对执行漂移和平面图失真鲁棒。"
conclusion: 楼层平面图引导导航能有效提升空间智能，为更智能的导航系统奠定基础。
---

## 摘要
现有视觉-语言导航(VLN)任务要求智能体遵循冗长的指令，忽略了某些可能有用的全局空间先验，限制了它们推理空间结构的能力。虽然人类可读的空间示意图（例如楼层平面图）在真实建筑中无处不在，但当前智能体缺乏理解和利用它们的认知能力。为弥补这一差距，我们引入FloorPlan-VLN，一种新范式，利用结构化语义楼层平面图作为全局空间先验，仅凭简洁指令即可实现导航。我们首先构建FloorPlan-VLN数据集，包含72个场景中的超过1万个片段。它将100多张语义标注的楼层平面图与基于Matterport3D的导航轨迹以及省略逐步指导的简洁指令配对。然后，我们提出一种简单而有效的方法FP-Nav，它使用双视图、时空对齐的视频序列和辅助推理任务来对齐观测、楼层平面图和指令。在该新基准下评估时，我们的方法显著优于调整后的最先进VLN基线，导航成功率相对提升超过60%。此外，全面的噪声建模和真实世界部署证明了FP-Nav对执行漂移和楼层平面图失真的可行性和鲁棒性。这些结果验证了楼层平面图引导导航的有效性，并突显FloorPlan-VLN作为迈向更具空间智能导航的有前景的一步。

## Abstract
Existing Vision-Language Navigation (VLN) task requires agents to follow verbose instructions, ignoring some potentially useful global spatial priors, limiting their capability to reason about spatial structures. Although human-readable spatial schematics (e.g., floor plans) are ubiquitous in real-world buildings, current agents lack the cognitive ability to comprehend and utilize them. To bridge this gap, we introduce FloorPlan-VLN, a new paradigm that leverages structured semantic floor plans as global spatial priors to enable navigation with only concise instructions. We first construct the FloorPlan-VLN dataset, which comprises over 10k episodes across 72 scenes. It pairs more than 100 semantically annotated floor plans with Matterport3D-based navigation trajectories and concise instructions that omit step-by-step guidance. Then, we propose a simple yet effective method FP-Nav that uses a dual-view, spatio-temporally aligned video sequence, and auxiliary reasoning tasks to align observations, floor plans, and instructions. When evaluated under this new benchmark, our method significantly outperforms adapted state-of-the-art VLN baselines, achieving more than a 60% relative improvement in navigation success rate. Furthermore, comprehensive noise modeling and real-world deployments demonstrate the feasibility and robustness of FP-Nav to actuation drift and floor plan distortions. These results validate the effectiveness of floor plan guided navigation and highlight FloorPlan-VLN as a promising step toward more spatially intelligent navigation.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有视觉‑语言导航（VLN）任务严重依赖冗长的逐步指令，智能体无法利用全局空间先验（如楼层平面图），导致对空间结构的推理能力不足。
- 现实生活中人类可读的楼层平面图广泛存在于商场、医院等建筑中，但当前导航智能体缺乏理解和使用这类结构化示意图的能力。
- 论文提出一种新范式 **FloorPlan-VLN**：将结构化语义楼层平面图作为全局空间先验，使智能体仅需“起始区域‑目标区域‑停止条件”这样的简洁指令即可完成导航，从而降低人机交互负担，并提升空间智能。

## 二、论文提出的方法论
- **核心思想**：将楼层平面图作为统一空间接口，利用多模态大语言模型（MLLM）对齐抽象平面图、自我中心观测和简洁指令，实现区域级别的导航。
- **数据集构建**：
  - 从 Matterport3D 中提取矢量化的楼层平面图（每个区域用多边形、类型和唯一标识符表示）。
  - 从 R2R-CE 和 RxR-CE 数据集收集导航轨迹，过滤跨楼层和冗余探索路径，只保留单楼层轨迹。
  - 使用 Qwen-2.5-VL 将原始冗长指令简化为仅含起始区域、目标区域和停止条件的简洁指令（10种模板）。
  - 最终得到 FloorPlan-R2R 和 FloorPlan-RxR 两个子集，共超过 10k 个片段，覆盖 70+ 建筑、130+ 楼层平面图、30 种区域类型。
- **FP-Nav 方法**：
  - 基础架构：基于 Qwen-2.5-VL-7B（MLLM），包括视觉编码器、MLP 投影器和大语言模型。
  - **时空对齐双视图视频流**：将每一时刻的自我中心观测图像与标注了当前位姿和历史的楼层平面图像水平拼接，形成同步的双视图帧序列，作为视频输入。
  - 对比了四种输入策略（静态分离、双流、交错、双视图对齐），最终选择对齐策略实现最佳对齐。
  - **辅助任务**（三个）：
    1. 区域定位：要求模型根据当前观测描述区域类型。
    2. 轨迹推理：要求模型总结已访问区域、当前区域和下一步计划。
    3. 指令摘要：要求模型从成功导航视频中重建原始简洁指令。
  - **统一训练目标**：将所有任务视为下一词元预测（NTP），使用任务平衡采样联合训练。
  - **噪声建模**：引入执行噪声（平移/旋转扰动）和楼层平面图噪声（全局尺度偏移、几何抖动），评估鲁棒性。

## 三、实验设计
- **仿真环境**：Habitat 模拟器（连续状态空间）。
- **数据集**：FloorPlan-R2R 和 FloorPlan-RxR 的 validation-seen / validation-unseen 划分。
- **评价指标**：导航误差（NE）、成功率（SR）、或acles成功率（OSR）、SPL。
- **对比方法**：
  - 零样本基线：Qwen-zs、NaVILA-zs、StreamVLN-zs、InternVLA-N1-zs、Navid-zs。
  - 微调基线：Navid-ft（在 FloorPlan-VLN 数据上微调 Navid）。
  - 自身变体：FP-Nav（冻结视觉编码器）、FP-Nav-v（解冻视觉编码器）、FP-Nav-v-rxr（额外使用 FloorPlan-RxR 长轨迹）。
- **实验种类**：（详见第五节）：
  - 主实验结果对比（表III）。
  - 噪音鲁棒性实验（执行噪声、尺度噪声、几何抖动）（表IV）。
  - 输入策略消融（表V）。
  - 是否真正使用楼层平面图的验证（遮挡/随机平面图）（表VI）。
  - 辅助任务影响（表VII）。
  - 不同参数训练效果（MLP/LLM/视觉编码器）（表VIII）。
  - 真实世界部署（表IX）：在 1370㎡ 建筑中，6个位置25个片段，对比 Navid-ft 和 FP-Nav-v-rxr。

## 四、资源与算力
- 论文明确说明：使用 **4块 H100 GPU** 训练 **20小时**（共 80 GPU 小时）。
- 训练数据：约 350K 行动 QA 样本，174K 辅助任务样本，9K 指令摘要样本。

## 五、实验数量与充分性
- **总实验组数**：主实验 + 噪音实验 + 不同输入策略 + 平面图依赖验证 + 辅助任务 + 参数配置 + 真实部署，共约 7 大类，每类包含 4~6 个子实验。
- **充分性与公平性**：
  - 消融实验覆盖了方法核心组件（输入、辅助任务、训练参数），验证了各组件必要性。
  - 与多个最强零样本和微调基线对比，并控制了网络结构差异（如选择 Qwen 作为统一骨干）。
  - 噪声实验模拟了现实中的执行误差和地图不精确，增强了结论可靠性。
  - 真实世界实验在复杂的多层区建筑中进行，跨区域导航，验证了可行性。
- 不足：未见跨楼层导航实验；真实世界实验仅25个片段，统计显著性有限；未对MLLM backbone做多模型对比（仅用Qwen）。

## 六、论文的主要结论与发现
- **FloorPlan-VLN 新范式有效**：利用楼层平面图作为全局先验，智能体仅凭简洁指令即可完成导航，比传统VLN更自然。
- **FP-Nav 显著超越基线**：在 FloorPlan-R2R unseen 上 SR 达到 28.8%（FP-Nav-v-rxr），比最佳基线（Navid-ft）提升 69% 相对值；在 seen 上提升 138%。
- **时空对齐双视图输入是关键**：相比分离、交错等策略，双视图拼接大幅提升性能（SR增加 18.7 个百分点）。
- **辅助任务强化对齐**：区域定位、轨迹推理、指令摘要三个任务联合训练带来 3.1 个点 SR 提升。
- **对噪声鲁棒**：执行噪声、平面图尺度/几何噪声下性能仅小幅下降，表明模型学习的是布局不变性而非精确坐标。
- **真实场景可行**：零样本部署在四足机器人上，SR 24.0%，与仿真 unseen 结果接近，验证了实际部署潜力。

## 七、优点
- **问题新颖且有实际意义**：首次将标准结构化楼层平面图引入 VLN，提出简洁指令范式，降低人机交互难度。
- **方法设计巧妙**：
  - 利用 MLLM 的预训练能力，避免重新训练平面图编码器；通过视觉提示（颜色、数字）将结构化信息可微地融入图像。
  - 双视图对齐策略简单有效，无需复杂注意力机制。
  - 辅助任务自然且标签可由自动流程生成，无需人工额外标注。
- **实验全面**：覆盖仿真、噪声模拟、真实世界部署；对比基线包括通用 MLLM 和专用导航模型；消融实验系统深入。
- **开源数据集贡献**：提供首个楼层平面图+简洁指令的 VLN 基准，促进后续研究。

## 八、不足与局限
- **单楼层假设**：论文明确限定单楼层导航，而实际建筑中常有多楼层需求。跨楼层导航只占数据集的2.2%，但论文直接排除，限制了范式的通用性。
- **依赖位姿信息**：在训练和推理中使用地面真值位姿或 LiDAR 里程计投影到平面图上，未解决完全无位姿情况下的定位问题。论文虽做了噪声实验，但未提出主动定位方法。
- **真实世界实验规模小**：仅在单一建筑中做 25 个片段，统计差异较大，且未与其他基线（如 Navid-ft）在真实环境充分对比。
- **MLLM 骨干单一**：仅使用 Qwen-2.5-VL，未验证其他 MLLM（如 LLaVA、InternVL）是否同样有效，结论的泛化性有待检验。
- **计算资源需求高**：80 GPU 小时对于实际部署仍显昂贵；推理延迟在边缘设备上可能不满足实时要求（论文使用外部 GPU 和 eGPU）。
- **未考虑动态变化**：楼层平面图是静态的，无法反映物体移动或临时遮挡，在某些场景下可能误导导航。

（完）
