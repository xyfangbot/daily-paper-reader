---
title: "Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System"
title_zh: Qwen-RobotNav技术报告：面向智能体导航系统的可扩展导航模型
authors: Designed for an Agentic Navigation System
date: 2026-06-24
pdf: "https://arxiv.org/pdf/2606.18112v2"
arxiv_id: 2606.18112v2
arxiv_url: "https://arxiv.org/abs/2606.18112v2"
manual_pdf_url: assets/manual-pdfs/manual-20260624-090656/002-002-qwen-robotnav-technical-report_-a-scalable-navigation-model-designed-for-an-agentic-navigation-system-0852aee56794.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2606.18112v2", "query:navigation model", "query:multi-task navigation", "query:vision-language models", "query:embodied navigation", "query:agentic systems"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "现有agentic导航系统需要基础模型在推理时能外部重配置观测策略，但传统方法无法动态调整。本文提出Qwen-RobotNav，基于Qwen3-VL构建，通过参数化接口（任务模式和可控观测参数）实现灵活重配置，训练时随机化所有参数确保鲁棒性。在VLN-CE RxR、EVT-Bench、NAVSIM上分别达到76.5%、90.0%、91.4 PDMS，并在Embodied Question Answering任务上相比此前最优方法提升10.8%-15.4%，同时减少77%导航步数。该模型具有良好的可扩展性和零样本迁移能力，为agentic导航系统提供了通用基础模块。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1650, \"height\": 745, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1481, \"height\": 859, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1620, \"height\": 716, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1651, \"height\": 963, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1654, \"height\": 737, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1242, \"height\": 771, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1648, \"height\": 549, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1641, \"height\": 802, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1474, \"height\": 772, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1635, \"height\": 770, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1511, \"height\": 2080, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1491, \"height\": 432, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1570, \"height\": 1408, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1575, \"height\": 1202, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1161, \"height\": 898, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1639, \"height\": 649, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1566, \"height\": 1002, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1564, \"height\": 918, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1556, \"height\": 473, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1556, \"height\": 471, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1591, \"height\": 1966, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1652, \"height\": 261, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1290, \"height\": 749, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1658, \"height\": 348, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1199, \"height\": 335, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 932, \"height\": 524, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1172, \"height\": 473, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 838, \"height\": 546, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1593, \"height\": 463, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1254, \"height\": 1018, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260624-090656-manual-002-0852aee56794-qwen-robotnav-technical-report-a-scalable-navigation-model-designed-for-an-agentic-navigation-system/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1391, \"height\": 264, \"label\": \"Table\"}]"
motivation: 导航模型需要在推理时动态切换观测策略以适应指令跟随、物体搜索、目标追踪等不同任务，但现有模型架构固定，无法外部重配置。
method: 基于Qwen3-VL构建，设计参数化接口包含任务模式和可控观测参数（如token预算、相机权重），训练时随机化所有参数，并联合视觉语言数据防止过拟合。
result: "在VLN-CE RxR成功率76.5%，EVT-Bench追踪率90.0%，NAVSIM PDMS 91.4；EQA任务上较最优方法提升10.8%-15.4%，步骤减少77%。"
conclusion: Qwen-RobotNav通过参数化接口和联合训练实现了可扩展、零样本迁移的导航模型，为agentic系统提供高效基础组件。
---

## 摘要
智能体导航系统需要一个基础导航模型，其观测策略能够在推理时从外部重新配置，因为指令跟随、物体搜索、目标跟踪和自动驾驶共享相同的感知-规划主干，但需要完全不同的策略来消费视觉流。我们提出Qwen-RobotNav，一个基于Qwen3-VL构建的可扩展导航模型，通过一个具有两个互补维度的参数化接口来解决这一问题：多个任务模式用于选择导航行为，以及可控的观测参数（例如，token预算、每相机权重）用于控制视觉历史如何编码。通过在训练时对所有参数进行随机化，Qwen-RobotNav对任何推理时配置都具有鲁棒性，无需对Qwen3-VL主干进行任何架构修改。我们在1560万个样本上训练Qwen-RobotNav；与视觉-语言数据共同训练可防止在仅轨迹训练中观察到的退化为反应式动作序列映射器。参数化接口也使得Qwen-RobotNav成为智能体系统的自然构建模块：对于长时域场景，上层规划器将目标分解为子任务，并在情节中动态切换Qwen-RobotNav的任务模式和上下文策略，通过重复调用同一模型组合复杂行为。大量实验表明，Qwen-RobotNav在主要导航基准上取得了新的最佳结果，在VLN-CE RxR上达到76.5%的成功率，在EVT-Bench上达到90.0%的跟踪率，在NAVSIM上达到91.4的PDMS。除了这些独立结果之外，一个基于Qwen-RobotNav构建的智能体导航系统在具身问答任务上取得了新的最佳结果，在HM-EQA上比先前最佳方法提高了10.8%，在EXPRESS-Bench上提高了15.4%，同时减少了77%的导航步骤。该模型在从2B到8B参数规模上表现出良好的扩展性，联合多任务训练发展出一个跨任务族共享的空间规划基底，并在多样环境中对真实世界机器人展现出强大的零样本泛化能力。

## Abstract
Agentic navigation systems require a base navigation model whose observation strategy can be externally reconfigured at inference time, because instruction following, object search, target tracking, and autonomous driving share the same perception-planning backbone yet demand fundamentally different strategies for consuming the visual stream. We present Qwen-RobotNav, a scalable navigation model built on Qwen3-VL that addresses it through a parameterised interface with two complementary dimensions: multiple task modes that select the navigation behaviour, and controllable observation parameters (e.g., token budget, per-camera weights) that govern how visual history is encoded. With training-time randomization over all parameters, Qwen-RobotNav is robust to any inference-time configuration requiring zero architectural modification to the Qwen3-VL backbone. We train Qwen-RobotNav on 15.6M samples; co-training with vision-language data prevents the collapse into reactive action-sequence mappers observed in trajectory-only training. The parameterised interface also makes Qwen-RobotNav a natural building block for agentic systems: for long-horizon scenarios, an upper-level planner decomposes goals into sub-tasks and dynamically switches Qwen-RobotNav’s task mode and context strategy mid-episode, composing complex behaviours from repeated calls to the same model. Extensive experiments show that Qwen-RobotNav sets new state-of-the-art results across major navigation benchmarks, achieving 76.5% success rate on VLN-CE RxR, 90.0% tracking rate on EVT-Bench, and 91.4 PDMS on NAVSIM. Beyond these standalone results, an agentic navigation system built with Qwen-RobotNav set a new state of the art on Embodied Question Answering, improving over the best prior method by 10.8% on HM-EQA and 15.4% on EXPRESS-Bench while requiring 77% fewer navigation steps. The model exhibits favourable scaling from 2B to 8B parameters, with joint multi-task training developing a shared spatial-planning substrate that transfers across task families, and demonstrates strong zero-shot generalisation to real-world robots across diverse environments.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有智能体导航系统需要基础模型在推理时能够从外部动态调整观测策略，因为指令跟随、物体搜索、目标跟踪、自动驾驶等任务共享相同的感知‑规划主干，却对视觉历史消费方式有根本不同的要求。
- 传统方法（如NavFoM均匀子采样、ABot‑N0滑动窗口）仅嵌入单一固定假设，无法在部署时调整，也难以适应任务间的切换。
- 长时域场景（如具身问答）要求导航模型作为更大智能体系统的核心模块，需要具备可参数化重配置的接口，而当前尚无模型满足此需求。
- 本文提出Qwen‑RobotNav，将多任务导航的核心挑战重新定义为**观测上下文建模**而非架构设计问题，通过参数化接口实现可控、可组合的导航行为。

## 二、论文提出的方法论
### 核心思想
- 将各类导航任务统一为**航点轨迹预测**（K=8个航点），并暴露一个**参数化接口**，包含两个互补维度：
  1. **任务模式**（VLN、PointNav、ObjNav、Tracking、Driving）：允许上层规划器选择行为类型。
  2. **可控观测参数**：视觉token预算 B、时间衰减 γ、每相机权重 wₓ₎ₕₑ、帧采样模式 m、单图token上下限 bmin/bmax。
- **训练时对所有参数进行独立随机化**，使模型对任意推理时配置鲁棒，无需任务特定微调。

### 关键技术细节
1. **模型架构**：继承Qwen3‑VL（SigLIP‑2视觉编码器 + LLM主干 + DeepStack注入），追加轻量4层MLP动作头输出24维航点（8航点×(x,y,θ)）。
2. **任务自适应观测编码**（Algorithm 1）：
   - 先子采样帧（T′≤T），计算时间权重 ωₜ = exp(γ·t/(T′−1))，γ越大越偏向近期帧。
   - 联合权重矩阵 W[t,c] = ωₜ · wₓ₎ₕₑ。
   - 通过受约束分配算法，先给每帧最低bmin token，剩余按W比例分配，超出bmax的单元迭代回收。
   - 根据分配的token数调整图像分辨率。
3. **视角与时间标识**：通过自然语言标签（如“Time step 0 Front View <image>”）插入，无需架构修改，利用预训练语言模型的空间语义。
4. **具身提示设计**：使用文本前缀区分机器人/小车等，如“Imagine you are a robot…”。
5. **联合训练目标**：L = Ltraj + λ LVL，轨迹MSE损失 + 下一token预测损失。训练数据85%导航轨迹 + 15%导航相关视觉语言推理。
6. **数据生成**：包括模拟器数据（R2R、RxR、PointNav、ObjectNav骨架探索、EVT‑Bench跟踪、nuScenes/OpenScene驾驶）和**T2V自动生成数据**（5阶段流水线：提示生成→视频合成→VLM过滤→单目位姿提取→运动学过滤）。
7. **智能体系统**：上层规划器（Qwen3.6‑Plus）分解任务、动态切换Qwen‑RobotNav的任务模式和观测参数，中间通过“航迹证据·记录本”实现上下文压缩。

## 三、实验设计
- **数据集与基准**：
  - VLN‑CE（R2R、RxR Val‑Unseen）、VLNVerse（细/粗粒度）、VLN‑PE（flash控制器）
  - 物体目标导航：MP3D、HM3D v1/v2、HM3D‑OVON（闭集和开集）
  - 主动视觉跟踪：EVT‑Bench（Single Target分集）
  - 具身问答：HM‑EQA、MT‑HM3D、EXPRESS‑Bench
  - 自动驾驶：NAVSIM（navtest）、AlpaSim（零样本跨域）
- **对比方法**：NavFoM、ABot‑N0、Uni‑NaVid、DualVLN、InternVLA‑N1、TrackVLA、AutoVLA、ReCogDrive等十余种专业或基础模型。
- **消融实验**：数据规模缩放（12.5%→100%）、token预算B与时间衰减γ的独立影响。
- **真实世界部署**：在四足机器人Go2上（云端/边缘部署）执行VLN任务，验证零样本迁移。

## 四、资源与算力
- 文中明确提到：**8B模型使用全局batch size 256，总共训练2,816 H100 GPU小时**。
- 未明确说明模型总参数量（2B/4B/8B对应配置）、多节点训练细节、数据生成阶段算力消耗，以及VLM过滤和视频合成的资源。

## 五、实验数量与充分性
- 实验覆盖**7大类任务、十余个基准、两个模型规模**，对比了多个现有最佳方法（包括闭源与开源）。
- 进行了**数据规模消融**（4个数据比例）和**控制参数消融**（B从2048到4608，γ从0.5到3.5），验证了设计动机。
- 真实世界部署提供了3个示例（展馆、公寓、智能体长时域导航），定性展示了零样本效果。
- **充分性评价**：实验较为全面，涵盖了主流导航场景，并与fair对比。但仍存在以下限制：
  - 消融实验仅在VLN‑CE R2R的500个episode上进行，规模偏小。
  - 未对训练时间随机化进行完整消融（如固定γ vs 随机γ的对比）。
  - 智能体系统部分的EQA实验未单独消融任务模式切换的效果。
  - AlpaSim零样本结果与专用模型有较大差距，未能展现强跨域鲁棒性。

## 六、论文的主要结论与发现
- Qwen‑RobotNav在多个基准上达到新最佳：VLN‑CE RxR 76.5% SR、EVT‑Bench 90.0% TR、NAVSIM 91.4 PDMS。
- 与上层规划器组成的智能体系统在EQA上超越先前方法10.8%~15.4%，同时减少77%导航步骤。
- **参数化接口**使同个模型能灵活在全局历史/近期焦点间切换，无需架构改动。
- **联合训练**（轨迹+视觉语言）防止了仅轨迹训练导致的“动作序列映射器”退化。
- **自然语言视角/时间标签**充分利用了预训练语言模型的空间语义，零成本实现结构化输入。
- **良好可扩展性**：从2B到8B参数性能持续提升，尤其在长时域任务上。
- **零样本迁移**到真实世界机器人得到验证。

## 七、优点
1. **创新性**：将导航模型设计为可参数化重配置的“原始组件”，而非固定策略，契合智能体系统需求。
2. **简洁有效**：视角/时间身份使用自然语言标签，无需额外嵌入层；训练随机化支持任意推理配置。
3. **数据多样性**：15.6M样本覆盖5大任务族、多种具身形态，并引入T2V自动生成流水线，降低模拟‑现实偏差。
4. **系统集成性**：提供了完整的“规划器‑执行器‑记忆压缩”框架，保持模块化与可扩展性。
5. **实验充分**：在学术基准和真实机器人上都做了验证，结果透明且具有可复现性（开源模型与代码）。
6. **部署灵活性**：支持云端（196ms）和边缘终端（204ms），在延迟与稳定性间提供选择。

## 八、不足与局限
1. **OVON上SPL较低**：骨架探索策略鼓励彻底搜索，导致路径长度增加，SPL低于贪心方法（如ABot‑N0）。
2. **跟踪成功率不如专用模型**：多任务训练引入权衡，SR低于TrackVLA++和ABot‑N0，可能因为跟踪任务中的“判定成功”标准更受保守行为影响。
3. **AlpaSim零样本差距大**：在长时间、高交互驾驶场景下，Qwen‑RobotNav的Close Encounter Rate和Off‑Road Rate显著高于专用模型，说明跨域泛化仍有提升空间。
4. **token分配算法为启发式**：论文承认当前基于权重的分配是经验性的，可能不是最优，可被更原则化的方法替代。
5. **依赖上层规划器**：智能体系统效果高度依赖上层LLM的分解与决策能力，未单独评估规划器的影响。
6. **训练/推理成本**：2,816 H100 GPU hours的训练成本较高，且推理时需部署Qwen3‑VL（8B）及上层LLM，资源需求大。
7. **实验局限性**：消融仅在单一基准上小样本进行；训练随机化未做系统消融；真实世界验证为定性示例，缺乏定量指标。

（完）
