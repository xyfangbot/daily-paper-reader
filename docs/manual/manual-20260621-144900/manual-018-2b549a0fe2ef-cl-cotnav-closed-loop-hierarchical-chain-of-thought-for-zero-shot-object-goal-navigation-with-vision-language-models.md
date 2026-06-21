---
title: "CL-CoTNav: Closed-Loop Hierarchical Chain-of-Thought for Zero-Shot Object-Goal Navigation with Vision-Language Models"
title_zh: CL-CoTNav：基于视觉语言模型的零样本物体目标导航的闭环分层思维链
authors: "Yuxin Cai, Xiangkun He, Maonan Wang, Hongliang Guo, Wei-Yun Yau, Chen Lv"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2504.09000v1"
arxiv_id: 2504.09000v1
arxiv_url: "https://arxiv.org/abs/2504.09000v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/018-2025_cai_cl_cotnav-fd81a2e1-2b549a0fe2ef.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2504.09000v1", "query:Vision-based navigation", "query:foundation models", "query:autonomous agents", "query:Object Goal Navigation", "query:zero-shot generalization"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "视觉目标导航的决策策略常因依赖记忆而难以泛化到新环境。本文提出CL-CoTNav框架，通过人类示范轨迹微调视觉语言模型，引入层级Chain-of-Thought推理与闭环置信度加权反馈。在AI Habitat实验中，导航成功率和SPL提升22.4%，显著增强了零样本泛化能力。该方法为VLM驱动的导航提供了结构化推理的新思路。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-018-2b549a0fe2ef-cl-cotnav-closed-loop-hierarchical-chain-of-thought-for-zero-shot-object-goal-navigation-with-vision-language-models/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 890, \"height\": 588, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-018-2b549a0fe2ef-cl-cotnav-closed-loop-hierarchical-chain-of-thought-for-zero-shot-object-goal-navigation-with-vision-language-models/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1829, \"height\": 1019, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-018-2b549a0fe2ef-cl-cotnav-closed-loop-hierarchical-chain-of-thought-for-zero-shot-object-goal-navigation-with-vision-language-models/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 900, \"height\": 364, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-018-2b549a0fe2ef-cl-cotnav-closed-loop-hierarchical-chain-of-thought-for-zero-shot-object-goal-navigation-with-vision-language-models/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 892, \"height\": 366, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-018-2b549a0fe2ef-cl-cotnav-closed-loop-hierarchical-chain-of-thought-for-zero-shot-object-goal-navigation-with-vision-language-models/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 860, \"height\": 441, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-018-2b549a0fe2ef-cl-cotnav-closed-loop-hierarchical-chain-of-thought-for-zero-shot-object-goal-navigation-with-vision-language-models/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 568, \"height\": 332, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-018-2b549a0fe2ef-cl-cotnav-closed-loop-hierarchical-chain-of-thought-for-zero-shot-object-goal-navigation-with-vision-language-models/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 920, \"height\": 647, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-018-2b549a0fe2ef-cl-cotnav-closed-loop-hierarchical-chain-of-thought-for-zero-shot-object-goal-navigation-with-vision-language-models/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 855, \"height\": 296, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-018-2b549a0fe2ef-cl-cotnav-closed-loop-hierarchical-chain-of-thought-for-zero-shot-object-goal-navigation-with-vision-language-models/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 835, \"height\": 202, \"label\": \"Table\"}]"
motivation: 传统端到端方法依赖记忆空间模式，缺乏结构化推理，导致泛化到新环境和新物体类别时性能差。
method: 微调VLM于人类示范轨迹的多轮问答数据，采用层级Chain-of-Thought提示和闭环置信度加权反馈机制。
result: "在AI Habitat实验中，导航成功率和SPL相比最先进方法提升22.4%。"
conclusion: CL-CoTNav通过结构化推理和闭环反馈，有效实现零样本目标导航，在未见环境和新物体类别上展现强泛化能力。
---

## 摘要
视觉物体目标导航（ObjectNav）要求机器人利用自我中心的观察在未知环境中定位目标物体。然而，决策策略往往难以迁移至未知环境和新型目标物体，这是核心的泛化问题。传统的端到端学习方法加剧了这一问题，因为它们依赖记忆空间模式而非采用结构化推理，限制了有效泛化的能力。本文提出闭环分层思维链导航（CL-CoTNav），一种由视觉语言模型（VLM）驱动的ObjectNav框架，将结构化推理和闭环反馈整合到导航决策中。为了增强泛化能力，我们使用从人类示范轨迹导出的多轮问答（QA）数据微调VLM。这一结构化数据集支持分层思维链（H-CoT）提示，系统性地提取组合知识以优化感知和决策，灵感来源于人类通过迭代推理步骤定位目标物体的认知过程。此外，我们提出闭环H-CoT机制，将检测和推理置信度分数融入训练。这种自适应加权策略引导模型优先处理高置信度数据对，减轻噪声输入的影响，并增强对幻觉或错误推理的鲁棒性。在AI Habitat环境中的广泛实验表明，CL-CoTNav在未见场景和新物体类别上具有卓越的泛化能力。我们的方法在导航成功率（SR）和路径长度加权成功率（SPL）上持续优于现有最优方法22.4%。我们在项目页面上发布数据集、模型和补充视频。

## Abstract
Visual Object Goal Navigation (ObjectNav) requires a robot to locate a target object in an unseen environment using egocentric observations. However, decision-making policies often struggle to transfer to unseen environments and novel target objects, which is the core generalization problem. Traditional end-to-end learning methods exacerbate this issue, as they rely on memorizing spatial patterns rather than employing structured reasoning, limiting their ability to generalize effectively. In this letter, we introduce Closed-Loop Hierarchical Chain-of-Thought Navigation (CL-CoTNav), a vision-language model (VLM)-driven ObjectNav framework that integrates structured reasoning and closed-loop feedback into navigation decision-making. To enhance generalization, we fine-tune a VLM using multi-turn question-answering (QA) data derived from human demonstration trajectories. This structured dataset enables hierarchical Chain-of-Thought (H-CoT) prompting, systematically extracting compositional knowledge to refine perception and decision-making, inspired by the human cognitive process of locating a target object through iterative reasoning steps. Additionally, we propose a Closed-Loop H-CoT mechanism that incorporates detection and reasoning confidence scores into training. This adaptive weighting strategy guides the model to prioritize high-confidence data pairs, mitigating the impact of noisy inputs and enhancing robustness against hallucinated or incorrect reasoning. Extensive experiments in the AI Habitat environment demonstrate CL-CoTNav's superior generalization to unseen scenes and novel object categories. Our method consistently outperforms state-of-the-art approaches in navigation success rate (SR) and success weighted by path length (SPL) by 22.4%. We release our datasets, models, and supplementary videos on our project page.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：视觉物体目标导航（ObjectNav）要求机器人在未知环境中仅依靠自我中心视觉观察定位目标物体。现有决策策略难以泛化到未见环境和新型目标物体（零样本泛化问题），传统端到端学习方法依赖记忆空间模式而非结构化推理，泛化能力有限。
- **研究动机**：人类能通过语义关系推理（如厨房通常靠近客厅）高效导航，而现有方法缺乏类似的结构化推理和不确定性估计机制。作者希望借助视觉语言模型（VLM）的常识推理能力，同时解决推理过程中的幻觉和噪声问题。
- **整体含义**：提出一种VLM驱动的导航框架，通过从人类示范轨迹中提取多轮问答数据，构建分层思维链（H-CoT）推理，并引入闭环置信度反馈，提升零样本物体目标导航的泛化能力和鲁棒性。

## 二、论文提出的方法论

- **核心思想**：将物体目标导航分解为结构化多轮问答步骤，模拟人类迭代推理定位目标的认知过程；并引入置信度加权的自适应性损失函数，减少噪声和错误推理的影响。
- **关键技术细节**：
  - **层级思维链（H-CoT）提示**：分为两阶段：
    - 感知阶段（Perception Rounds）：通过多轮QA识别当前RGB观察中的显著子目标物体，推断房间类型（如电视和沙发暗示客厅），并基于常识建立物体-目标和物体-场景的语义共现关系，为每个子目标物体分配相关性分数。
    - 规划阶段（Planning Rounds）：基于感知阶段积累的上下文，生成高层导航建议（如“向左转”或“探索另一个房间”），再离散化为可执行的控制动作，并与人类示范动作对齐。
  - **数据集生成**：使用预训练模型（Qwen-VL-Chat用于子目标检测，Qwen-7B用于语义猜测，ChatGPT-3.5-turbo用于高层动作建议）对原始人类示范轨迹进行标注，获得结构化的多轮QA对。
  - **闭环H-CoT机制**：
    - 对每个QA序列，根据检测和推理的一致性计算置信度分数 \(c_i \in [0,1]\)（通过比较模型生成的文本动作建议与人类示范动作的语义对齐程度，结合视觉检测确定性）。
    - 设计自适应损失函数：\(L_{\text{adaptive}} = \frac{1}{1+\exp(-\alpha(c_i-\beta))} \times (-\log \hat{y}_{i,y_i})\)，其中\(\alpha,\beta\)为超参数。该函数对高置信度样本赋予更高权重，降低低置信度样本的影响。
- **算法流程**（文字说明）：
  - 输入：当前RGB图像、机器人位姿、目标物体类别 → 经过H-CoT多轮QA生成结构化推理输出和置信度分数 → 使用LoRA微调InternVL2（2B参数）作为导航策略网络，输出离散动作（前进、左转、右转、上/下看、停止）。

## 三、实验设计

- **数据集与场景**：
  - 使用**Matterport3D (MP3D)** 环境中的**MP3D-HD**人类示范轨迹数据集（70k+轨迹）。
  - 场景泛化实验：训练集分别使用28、40、56个场景（对应35k/50k/70k轨迹），测试集为MP3D-Val（11个未见场景，2195个episode）。
  - 物体泛化实验：将21个物体类别分为16个可见类和5个未见类，训练集MP3D-HD-35k-C16（仅含可见类），测试集MP3D-HD-35k-C05（含未见类：counter, bed, toilet, chest of drawers, plant）。
- **Benchmark**：标准零样本物体目标导航评估协议，使用Success Rate (SR)和Success Weighted by Path Length (SPL)作为主要指标，此外还使用Soft SPL。
- **对比方法**：
  - Baseline [19]：基于PPO的端到端RL方法。
  - Habitat-Web [6]：模仿学习方法（IL），从人类示范直接学习。
  - VLFM [23]：基于冻结BLIP-2的模块化VLM框架。
  - SSNet [20]：零样本RL方法，整合物体检测和词嵌入相似度。
  - DivScene [27]：引入思维链推理的VLM方法（基于最短路径监督）。
- **实验类型**：
  - 训练结果对比（Table III）。
  - 零样本泛化测试（Table IV）：两个设置（新物体类别、新场景）。
  - 消融研究（Table V）：对比纯人类标注、标准CoT、仅H-CoT、完整CL-CoTNav。
  - 定性结果（图3）：展示了零样本导航路径示例。

## 四、资源与算力

- **计算资源**：
  - 导航策略微调使用**4块NVIDIA V100 GPU**。
  - 基于**InternVL2**框架微调一个**2B参数**的视觉语言模型。
  - 训练设置：batch size=16，训练3个epoch，MP3D-HD-50k数据集上训练耗时约**19小时**。
  - LoRA超参数：rank=8，scaling factor=16，dropout=0.05，学习率3×10⁻⁴，权重衰减0.006，warmup steps=500。
- **数据集生成**：使用Qwen-VL-Chat、Qwen-7B和ChatGPT-3.5-turbo等预训练模型生成多轮QA标注，但未明确给出这些模型的推理算力需求。

## 五、实验数量与充分性

- **实验数量**：
  - 训练结果对比：包含5种方法，覆盖不同训练规模（35k/50k/70k）及两类设置（物体目标、场景）。
  - 零样本测试：对比6种方法在2个设置下的结果。
  - 消融研究：4种变体对比（纯文字、标准CoT、H-CoT、完整方法）。
  - 共约3张主要表格和1张定性图。
- **充分性与公平性**：
  - 充分：覆盖了主流基准方法（RL、IL、VLM），且在多个训练数据量下评估。
  - 客观：遵循标准零样本设置，训练和测试集不重叠，指标公开。
  - 公平：对比方法均使用相同环境（Habitat）和数据集。但未与更近期的VLM方法（如OpenFMNav等）比较，可能不够全面。消融实验清晰地验证了各组件的贡献。
  - 注意：所有实验均在模拟器中进行，未涉及真实机器人实验，可能影响结论的泛化性。

## 六、论文的主要结论与发现

- **主要发现**：CL-CoTNav在零样本导航任务上显著优于现有方法，在未见场景和新物体类别上**SR和SPL提升22.4%**。
- **结构化推理有效**：层级思维链（H-CoT）带来的提升远大于标准CoT，因为其分离了感知和规划阶段，更接近人类认知。
- **闭环反馈有益**：置信度加权学习（Closed-Loop H-CoT）进一步提升了泛化性能，对噪声和幻觉更鲁棒。
- **数据规模影响**：从35k增加到50k轨迹改进明显，但50k到70k改进幅度降低，说明纯数据规模存在饱和，结构化监督更重要。
- **实际可行性**：2B模型的多轮推理时间约**1.2秒**，适合实用部署。

## 七、优点

- **方法创新**：首次将分层思维链（H-CoT）与闭环置信度反馈结合用于物体目标导航，构建了结构化推理+自适应学习的新框架。
- **数据集设计**：从人类示范轨迹中自动生成多轮QA标注，避免昂贵的人工标注，且包含丰富的语义推理信息。
- **鲁棒性增强**：通过置信度加权抑制VLM的幻觉和错误关联，提高在未见环境中的决策可靠性。
- **实验设计合理**：分别在物体泛化和场景泛化两个维度评估，消融实验清晰验证了每个组件的贡献。
- **性能显著**：在标准Hardware（AI Habitat）上SR和SPL提升22.4%，结果可复现（公开数据集和模型）。

## 八、不足与局限

- **实验覆盖局限**：仅在MP3D模拟环境中评估，未在真实机器人平台上验证（仅在结论中提到“未来计划”）。
- **对比方法不足**：未与近期同样基于VLM的导航方法（如OpenFMNav）详细比较，且缺少在更多数据集（如Gibson、HM3D）上的结果。
- **依赖模仿学习**：仍受限于示范数据集的质量和覆盖范围，无法处理训练数据之外的复杂场景。
- **计算开销**：多轮推理（1.2秒/步）对于实时高频率控制可能仍显慢，且多步推理累积可能导致延迟。
- **超参数敏感性**：自适应损失中的α、β需要调参，文中仅给出默认值，未进行敏感性分析。
- **偏差风险**：VLM预训练模型可能存在对常见物体/场景的偏差，导致对罕见物体或非典型布局的推理不准确。
- **未报告统计显著性**：实验结果仅有数值比较，未提供多次运行的标准差或置信区间。

（完）
