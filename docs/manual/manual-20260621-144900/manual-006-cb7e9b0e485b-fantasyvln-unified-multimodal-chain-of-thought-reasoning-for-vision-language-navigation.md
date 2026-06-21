---
title: "FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-Language Navigation"
title_zh: FantasyVLN：面向视觉语言导航的统一多模态思维链推理
authors: "Jing Zuo, Lingzhou Mu, Fan Jiang, Chengcheng Ma, Mu Xu, Yonggang Qi"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2601.13976v2"
arxiv_id: 2601.13976v2
arxiv_url: "https://arxiv.org/abs/2601.13976v2"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/006-2026_zuo_fantasyvln-e4ac27f8-cb7e9b0e485b.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2601.13976v2", "query:Vision-and-Language Navigation", "query:Chain-of-Thought Reasoning", "query:Multimodal Reasoning", "query:Implicit Reasoning", "query:Visual AutoRegressive Model"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航中现有链式思维推理方法存在文本CoT缺乏空间接地、多模态CoT令牌膨胀导致实时性差的问题。本文提出FantasyVLN统一隐式推理框架，利用预训练视觉自回归模型将想象视觉令牌编码到紧凑潜在空间，在多CoT策略下联合训练，实现无显式开销的推理感知导航。在LH-VLN上成功率与效率提升，推理延迟比显式CoT方法降低一个数量级。该工作实现了推理感知与实时性兼顾的导航，为多模态CoT推理开辟新路径。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1415, \"height\": 647, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1433, \"height\": 609, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1415, \"height\": 790, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1426, \"height\": 314, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1392, \"height\": 970, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 680, \"height\": 300, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 694, \"height\": 339, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1065, \"height\": 323, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 895, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 871, \"height\": 182, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-006-cb7e9b0e485b-fantasyvln-unified-multimodal-chain-of-thought-reasoning-for-vision-language-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 790, \"height\": 277, \"label\": \"Table\"}]"
motivation: 现有CoT推理在VLN中面临空间接地不足或令牌膨胀问题，难以平衡推理能力与实时性。
method: 提出FantasyVLN，通过VAR将想象视觉令牌压缩到潜在空间，统一多模态CoT联合训练，实现隐式推理。
result: 在LH-VLN上，成功率与效率显著提升，推理延迟较显式CoT方法降低一个数量级。
conclusion: FantasyVLN实现了推理感知与实时导航的统一，为多模态CoT推理提供了高效范式。
---

## 摘要
在视觉语言导航（VLN）中实现人类级别的性能需要具身智能体在长动作序列推理过程中联合理解多模态指令和视觉空间上下文。近期工作如NavCoT和NavGPT-2展示了思维链（CoT）推理在提升可解释性和长程规划方面的潜力。此外，多模态扩展如OctoNav-R1和CoT-VLA进一步验证了CoT作为通向类人导航推理的有前景途径。然而，现有方法存在关键缺陷：纯文本CoT缺乏空间基础，容易过拟合稀疏的标注推理步骤，而多模态CoT通过生成想象的视觉观测导致严重的token膨胀，使得实时导航不切实际。在这项工作中，我们提出FantasyVLN，一个统一的隐式推理框架，在无显式token开销的情况下保留CoT推理的优势。具体来说，在CoT推理训练期间，使用预训练的视觉自回归模型（VAR）将想象的视觉token编码到紧凑的潜在空间中，并在统一的多CoT策略下联合从文本、视觉和多模态CoT模式中学习。在推理时，我们的模型执行直接的指令到动作映射，同时仍然享有推理感知的表示。在LH-VLN上的大量实验表明，我们的方法实现了推理感知且实时的导航，提高了成功率和效率，同时与显式CoT方法相比，推理延迟降低了一个数量级。

## Abstract
Achieving human-level performance in Vision-and-Language Navigation (VLN) requires an embodied agent to jointly understand multimodal instructions and visual-spatial context while reasoning over long action sequences. Recent works, such as NavCoT and NavGPT-2, demonstrate the potential of Chain-of-Thought (CoT) reasoning for improving interpretability and long-horizon planning. Moreover, multimodal extensions like OctoNav-R1 and CoT-VLA further validate CoT as a promising pathway toward human-like navigation reasoning. However, existing approaches face critical drawbacks: purely textual CoTs lack spatial grounding and easily overfit to sparse annotated reasoning steps, while multimodal CoTs incur severe token inflation by generating imagined visual observations, making real-time navigation impractical. In this work, we propose FantasyVLN, a unified implicit reasoning framework that preserves the benefits of CoT reasoning without explicit token overhead. Specifically, imagined visual tokens are encoded into a compact latent space using a pretrained Visual AutoRegressor (VAR) during CoT reasoning training, and the model jointly learns from textual, visual, and multimodal CoT modes under a unified multi-CoT strategy. At inference, our model performs direct instruction-to-action mapping while still enjoying reasoning-aware representations. Extensive experiments on LH-VLN show that our approach achieves reasoning-aware yet real-time navigation, improving success rates and efficiency while reducing inference latency by an order of magnitude compared to explicit CoT methods.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- 视觉语言导航（VLN）要求具身智能体在长动作序列中联合理解自然语言指令和视觉空间上下文，进行长程推理。多阶段、长程导航场景对多模态推理能力要求尤其高。
- 现有CoT推理方法存在关键缺陷：
  - 纯文本CoT（如NavCoT、NavGPT-2）：缺乏空间接地，容易过拟合稀疏的标注推理步骤，泛化性差。
  - 多模态CoT（如CoT-VLA、WorldVLA）：需要迭代生成和解析想象的中间观测，导致严重的token膨胀（一个推理步骤可扩展到3k-5k tokens），使实时导航不可行。
- 因此，需要一种既能保留CoT推理优势、又避免显式token开销的统一框架，实现推理感知且实时的导航。

## 二、论文提出的方法论

- 核心思想：提出FantasyVLN，一个统一隐式推理框架。在训练时让模型在多模态CoT模式下学习，但推理时直接进行指令到动作映射，不生成CoT序列，从而隐式利用推理能力。
- 关键技术细节：
  - 紧凑视觉CoT（CompV-CoT）：使用预训练的视觉自回归模型（VAR）将想象观测编码到紧凑的潜在空间（仅30个token），替代像素级预测，大幅降低token数量，提高训练和推理效率。
  - 统一多CoT策略：引入两个二进制门控信号（gT, gV）控制文本和视觉推理的激活，支持非CoT、文本CoT、视觉CoT、多模态CoT四种模式，所有模式共享网络参数。
  - 交叉模态对齐约束：用非CoT推理的动作预测作为软标签，对齐其他CoT模式的动作预测，确保不同推理模式学习到一致、模态不变的表示，防止模式冲突。
  - 训练流程：交替优化非CoT目标和交叉模态对齐联合目标，实现隐式推理能力的内化。推理时仅使用非CoT模式，实现高效实时导航。
- 算法流程（文字描述）：
  1. 从训练数据集中采样指令、观测、文本推理、视觉推理、动作。
  2. 通过非CoT前向得到动作预测并计算交叉熵损失，更新参数。
  3. 收敛后，冻结非CoT分支的软标签，然后对不同CoT模式执行前向，计算文本、视觉、多模态推理的交叉熵损失，以及动作预测对齐损失（与软标签的交叉熵），联合更新参数。
  4. 重复直到收敛。

## 三、实验设计

- 数据集/场景：LH-VLN基准，特点是多阶段任务和长导航轨迹。在线评估，任务和场景均未见（unseen）。
- Benchmark：LH-VLN提供的测试集，指标包括成功率（SR）、独立成功率（ISR）、条件成功率（CSR）、CSR加权地面真值（CGT），以及动作每秒（APS）衡量推理效率。
- 对比方法：
  - 文本CoT：Aux-Think。
  - 视觉CoT：CoT-VLA、WorldVLA。
  - 记忆方法：MGDM。
  - 其他基线：GLM-4v prompt、NaviLLM、GPT-4+NaviLLM。
  - 所有方法在相同训练集上训练，验证集选择最佳检查点。

## 四、资源与算力

- 论文明确说明训练配置：
  - 基础模型：Qwen2.5-VL（7B参数）。
  - 调优方法：LoRA参数高效微调，语言层和视觉语言投影模块。
  - 硬件：64块H20 GPU，每块141GB内存。
  - 优化器：AdamW，学习率1e-4，权重衰减0.1，余弦调度，5% warmup。
  - 批大小：每设备4，32个数据加载worker。
  - 精度：bfloat16，梯度检查点，DeepSpeed ZeRO-2。
- 训练时长：论文未明确说明总训练时长。

## 五、实验数量与充分性

- 主要结果：表2展示8种方法在4个指标上的比较，FantasyVLN全面领先。
- 消融研究：
  - 不同推理模式组合（表3）：验证了集成所有四种模式效果最佳。
  - VAR尺度选择（图3）：实验了尺度1-10，尺度4最优，并给出了重建图像定性对比（图4）支撑。
  - 交叉模态对齐约束（表5）：有/无对齐约束对比，对齐带来巨大提升。
  - 训练效率对比（图5）：与WorldVLA对比，FantasyVLN收敛更快、更稳定。
  - 显式vs隐式推理（表6）：在三种CoT模态下分别比较，隐式推理普遍优于显式。
- 实验充分性：覆盖了核心设计点的消融，对比了多种相关方法，使用了面向长程任务的特定基准。实验设计客观、公平，所有对比方法在同一数据设置下实验。

## 六、论文的主要结论与发现

- FantasyVLN在LH-VLN基准上大幅超越所有基线，SR达2.44（次优为0.98），ISR达11.01（次优8.26），CSR达9.64，CGT达8.99。
- 隐式推理在效率上远优于显式CoT（APS≈1 vs 0.19），同时导航准确性更高。
- 多模态CoT联合训练并通过交叉模态对齐约束，可以有效将推理能力内化到直接预测中。
- 紧凑视觉CoT（CompV-CoT）通过VAR潜在空间压缩显著提升了训练效率和稳定性。
- 隐式推理避免了显式CoT在长轨迹上的累积误差，更适应数据量有限的场景。

## 七、优点

- 创新性地提出统一多模态隐式CoT框架，首次将文本、视觉、多模态CoT集成在一个模型中，训练时间共享参数，推理零开销。
- 使用VAR模型进行视觉潜在空间压缩，较以往像素级预测大幅提升效率，同时保持空间推理能力。
- 交叉模态对齐约束巧妙利用非CoT分支作为软目标，促进不同模式的一致性学习。
- 实验设计全面，消融研究覆盖方法各个组件，且对比了当前主流方法，结果具有说服力。
- 推理延迟降低一个数量级，满足了VLN实时性的关键需求。

## 八、不足与局限

- 实验仅在LH-VLN单一基准上进行，未在更广泛VLN基准（如R2R、RxR、VLN-CE等）上验证泛化性。
- 训练数据规模较小（仅18k轨迹切片），可能限制了显式CoT学习的上限，但隐式推理部分受益于对齐约束，数据效率仍有待进一步提升。
- VAR压缩虽然高效，但仍存在一定重建误差（MSE 0.039），可能对视觉推理的精度有影响。
- 隐式推理虽然高效，但在需要显式可解释推理链的任务（如错误分析、人机交互）中可能无法提供中间状态，应用场景受限。
- 算力要求较高（64块H20），对一般研究团队可复现性有一定挑战。

（完）
