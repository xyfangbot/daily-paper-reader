---
title: "AstraNav-World: World Model for Foresight Control and Consistency"
title_zh: AstraNav-World：用于预见控制与一致性的世界模型
authors: "Jintao Chen, Junjun Hu, Haochen Bai, Minghua Luo, Xinda Xue, Botao Ren, Chengyu Bai, Shichao Xie, Ziyi Chen, Fei Liu, Zedong Chu, Xiaolong Wu, Mu Xu, Shanghang Zhang"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2512.21714v2"
arxiv_id: 2512.21714v2
arxiv_url: "https://arxiv.org/abs/2512.21714v2"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/011-2025_chen_astranav_world-e55ea6ab-509fa3e7db68.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2512.21714v2", "query:World Model", "query:Embodied Navigation", "query:Vision-Language Model", "query:Diffusion Model", "query:Video Generation"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 开放动态环境中具身导航需要准确预知世界演变和动作效果。AstraNav-World整合扩散视频生成器与视觉语言策略，通过双向约束同步生成未来视觉和动作序列。在多个导航基准上实现更高轨迹准确率和成功率，真实场景零样本适应。统一预测与规划，减轻解耦管道累积误差，为可靠通用具身智能提供新范式。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-011-509fa3e7db68-astranav-world-world-model-for-foresight-control-and-consistency/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1704, \"height\": 753, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-011-509fa3e7db68-astranav-world-world-model-for-foresight-control-and-consistency/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1717, \"height\": 1098, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-011-509fa3e7db68-astranav-world-world-model-for-foresight-control-and-consistency/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1703, \"height\": 437, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-011-509fa3e7db68-astranav-world-world-model-for-foresight-control-and-consistency/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 802, \"height\": 416, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-011-509fa3e7db68-astranav-world-world-model-for-foresight-control-and-consistency/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1712, \"height\": 1201, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-011-509fa3e7db68-astranav-world-world-model-for-foresight-control-and-consistency/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1417, \"height\": 196, \"label\": \"Table\"}]"
motivation: 现有“先预测后规划”解耦管道累积误差，需紧密耦合的视觉-动作模型。
method: 联合训练扩散视频生成与视觉语言策略，双向约束同步rollout。
result: 在导航基准上提升轨迹准确率和成功率，零样本适应真实场景。
conclusion: 统一预测与控制能提升导航鲁棒性和泛化性。
---

## 摘要
在开放动态环境中进行的具身导航要求对世界如何演化以及动作如何随时间展开具有准确的预见能力。我们提出AstraNav-World，一种端到端的世界模型，它在统一的概率框架中共同推理未来的视觉状态和动作序列。我们的框架将基于扩散的视频生成器与视觉-语言策略相结合，实现了同步的展开过程，其中预测的场景和计划的动作同时更新。训练优化了两个互补的目标：生成动作条件下的多步视觉预测，以及基于这些预测视觉推导轨迹。这种双向约束使得视觉预测可执行，并让决策基于物理一致且任务相关的未来，从而缓解了解耦的“先想象后规划”管道中常见的累积误差。在多种具身导航基准上的实验显示，轨迹精度和成功率均有提升。消融实验证实了紧密的视觉-动作耦合和统一训练的必要性，任一分支的移除都会降低预测质量和策略可靠性。在真实世界测试中，AstraNav-World展现了出色的零样本能力，无需任何真实世界微调即可适应未见过的场景。这些结果表明，AstraNav-World捕捉到了可迁移的空间理解和与规划相关的导航动态，而不仅仅是过拟合于模拟特定的数据分布。总体而言，通过将预见视觉和控制统一在单个生成模型中，我们向能够在开放真实世界环境中稳健运行的可靠、可解释且通用的具身智能体迈进了一步。

## Abstract
Embodied navigation in open, dynamic environments demands accurate foresight of how the world will evolve and how actions will unfold over time. We propose AstraNav-World, an end-to-end world model that jointly reasons about future visual states and action sequences within a unified probabilistic framework. Our framework integrates a diffusion-based video generator with a vision-language policy, enabling synchronized rollouts where predicted scenes and planned actions are updated simultaneously. Training optimizes two complementary objectives: generating action-conditioned multi-step visual predictions and deriving trajectories conditioned on those predicted visuals. This bidirectional constraint makes visual predictions executable and keeps decisions grounded in physically consistent, task-relevant futures, mitigating cumulative errors common in decoupled "envision-then-plan" pipelines. Experiments across diverse embodied navigation benchmarks show improved trajectory accuracy and higher success rates. Ablations confirm the necessity of tight vision–action coupling and unified training, with either branch removal degrading both prediction quality and policy reliability. In real-world testing, AstraNav-World demonstrated exceptional zero-shot capabilities, adapting to previously unseen scenarios without any real-world fine-tuning. These results suggest that AstraNav-World captures transferable spatial understanding and planning-relevant navigation dynamics, rather than merely overfitting to simulation-specific data distribution. Overall, by unifying foresight vision and control within a single generative model, we move closer to reliable, interpretable, and general-purpose embodied agents that operate robustly in open-ended real-world settings.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 具身导航在开放、动态环境中需要准确预见“世界如何演化”以及“动作如何随时间展开”。但现有工作大多采用“先想象后规划”（envision-then-plan）的解耦范式，即先预测未来视觉帧，再基于预测结果规划动作。这种管道容易导致物理不确定性和因果模糊性，并产生累积误差，最终使全局规划失效。
- 为克服这一问题，论文提出应将“预见未来”与“规划未来”紧密耦合在统一的概率框架中，通过双向约束（让视觉预测可执行，让动作规划基于物理一致的未来）来提升导航鲁棒性和一致性。

## 二、论文提出的方法论
- **核心思想**：提出AstraNav-World，一种端到端的统一生成式世界模型，联合建模多步未来视觉帧与动作序列。中心是一个强大的视觉语言模型（VLM）作为全局规划器（使用Qwen2.5-VL-3B），它编码指令和历史多视角观测生成视觉-语言嵌入，同时用于：（i）条件化一个扩散视频生成器（基于Wan2.2-TI2V-5B）进行状态预测；（ii）条件化一个策略头进行轨迹预测。两个流通过双向约束和同步展开进行联合优化。
- **关键技术细节**：
  - **VLM作为中央规划器**：处理指令和历史视觉，输出统一的视觉-语言嵌入，包含目标语义和空间上下文。
  - **视频生成器**：基于Wan2.2-TI2V-5B（扩散+DiT架构），用VLM嵌入替换原文本编码器。引入3D-RoPE重排策略处理多视角输入（左、前、右三视图），将当前三视图在宽度维度上并列。训练时使用流匹配（Flow Matching）损失，只对预测的未来帧加噪，历史帧保持低噪声。
  - **双策略头**：（1）Action Former：查询Transformer，输出确定性动作序列（位置、朝向、到达标志），使用L1损失、余弦相似度损失和二元交叉熵损失联合优化。（2）Diffusion Policy：基于扩散的策略，通过去噪生成概率性动作序列，并引入多模态融合交叉注意力（MMFCA）模块，在视频生成器与扩散策略的最后8个重叠块之间实现双向信息流（动作→视频、视频→动作）。MMFCA可通过开关γ控制（训练时50%概率开启，推理时可关）。
  - **整体训练**：两阶段。Stage 1：冻结VLM，分别预训练视频生成器和策略头。Stage 2：联合微调所有组件，总损失LTotal = LVG + λLPH（λ=1.0）。对扩散策略，训练时随机开启/关闭MMFCA。
  - **推理加速**：提出稀疏预见调度（SFS），仅在固定间隔（如每10步）激活视频生成器，中间步骤只运行策略头，实现6.7倍加速且几乎不降成功率。

## 三、实验设计
- **数据集与场景**：
  - 指令跟随导航：R2R-CE和RxR-CE（基于Habitat+MP3D室内场景）。
  - 开放词汇物体导航：HM3D-OVON。
  - 真实世界测试：物理机器人平台，零样本（无真实数据微调）。
- **Benchmark**：使用标准指标：成功率（SR）、Oracle成功率（OS）、按路径长度加权的成功率（SPL）、导航误差（NE）。
- **对比方法**：对比了HPN+DN、CMA、Sim2Sim、GridMM、DreamWalker、ETPNav、HNR、InstructNav、LAW、CM2、WS-MGMap、AO-Planner、NaVid、Uni-NaVid、NaVILA、StreamVLN、CorrectNav等十余种方法，以及VLA基线（无视频生成器）的3B/7B版本。

## 四、资源与算力
- 论文明确提及使用96块H20 GPU进行实验，学习率为1×10⁻⁵，采用余弦退火调度。未详细说明训练总时长或具体迭代步数。VLM采用全参数微调，视频生成器采用LoRA（秩和尺度均为128）微调。

## 五、实验数量与充分性
- **实验数量**：在三个主要benchmark（R2R-CE, RxR-CE, HM3D-OVON）上报告了主结果；对扩散策略和Action Former两种策略分别评估；消融实验包括：去除视频生成器（VG）的影响（在三个数据集上对比）；SFS不同间隔的效率和成功率；与参数规模的对比（3B vs 7B，加/不加VG）。此外有定性结果（展示生成帧与渲染帧的一致性）和一致性量化分析（通过VGGT估计相对相机姿态差异）。
- **充分性与公正性**：实验覆盖了多种主流导航任务（指令跟随和物体导航），对比了大量公开方法（包含早年的方法和最新的SOTA），消融设计合理。真实世界零样本测试增强了泛化性的说服力。但未进行跨主干网络（如不同VLM）的比较，也未报告多次运行的标准差。整体实验设计客观、公平。

## 六、论文的主要结论与发现
- **主要发现**：AstraNav-World在R2R-CE和RxR-CE上取得了最优SR/SPL（扩散策略分别达67.9%和72.9% SR），在HM3D-OVON上绝对提升4.9%（45.7% SR）。消融验证了视频生成器分支的不可或缺性——去除后三个数据集SR均下降。SFS可实现近7倍加速且维持约67% SR。与单纯扩大VLM参数（3B→7B）相比，加入世界模型（3B+VG）带来的收益（66.5%→67.9%）远超缩放参数的效果（66.5%→66.6%）。真实世界零样本测试展示了强泛化能力。
- **结论**：紧密耦合的“预见-规划”双向约束能有效降低累积误差，提升导航鲁棒性和一致性；世界模型具备了捕捉可迁移的空间理解和导航动态的能力，而非过拟合模拟数据。

## 七、优点
- **方法创新**：首次在统一框架内实现视觉预测与动作预测的深度耦合和双向约束（通过MMFCA），克服了解耦管道的固有缺陷。
- **设计巧妙**：3D-RoPE重排解决了多视角输入的位置编码问题；SFS策略实现了计算效率与性能的平衡；双策略头提供了确定性/概率性灵活选择。
- **实验充分**：涵盖多种任务、对比大量方法、消融设计清晰，并包含真实世界零样本验证，增强了论文说服力。
- **结果突出**：在三个基准上均显著超越之前SOTA，且零样本能力验证了世界模型的泛化本质。

## 八、不足与局限
- **计算开销**：尽管有SFS加速，完整联合推理仍依赖视频生成，在实时性要求极高的场景下可能存在延迟瓶颈。论文未报告实际推理帧率。
- **实验覆盖有限**：仅测试了MP3D和HM3D两种室内场景，未涉及更大规模或更复杂的室外场景（如自动驾驶）。未进行在多个VLM主干上的比较（仅用了Qwen2.5-VL-3B）。
- **偏差风险**：训练数据全部来自模拟器（Habitat），真实世界零样本仅做了定性演示，缺乏与模拟到真实迁移的其他基线对比。泛化性可能受限于模拟环境的多样性。
- **方法局限性**：当前架构依赖大规模预训练VLM作为规划器，可能带来高昂的训练成本和参数规模。双向约束机制（MMFCA）是否会引入额外训练不稳定仍需更多分析。
- **消融深度**：虽验证了VG的必要性，但对不同噪声策略、3D-RoPE变体、MMFCA开启概率等超参数的影响未做系统探索。

（完）
