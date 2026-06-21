---
title: "LiveVLN: Breaking the Stop-and-Go Loop in Vision-Language Navigation"
title_zh: LiveVLN：打破视觉语言导航中的走走停停循环
authors: "Xiangchen Wang, Weiye Zhu, Teng Wang, TianTian Geng, Zekai Zhang, Zhiyuan Qi, Jinyu Yang, Feng Zheng"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2604.19536v1"
arxiv_id: 2604.19536v1
arxiv_url: "https://arxiv.org/abs/2604.19536v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/019-2026_wang_livevln-7533bec4-e20e23dfd397.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2604.19536v1", "query:Vision-Language Navigation", "query:Continuous control", "query:Streaming inference"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: "现有多模态导航系统因感知-推理-执行阻塞循环导致实际部署时频繁停顿。LiveVLN通过多步动作连续策略，将新观测处理与当前动作执行重叠，无需额外训练即可实现更流畅导航。在R2R/RxR基准上保持原有性能，实际场景中平均等待时间降低77.7%，总耗时缩短12.6%-19.6%。该框架即插即用，为连续具身导航提供了有效解决方案。"
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-019-e20e23dfd397-livevln-breaking-the-stop-and-go-loop-in-vision-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 864, \"height\": 620, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-019-e20e23dfd397-livevln-breaking-the-stop-and-go-loop-in-vision-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 769, \"height\": 550, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-019-e20e23dfd397-livevln-breaking-the-stop-and-go-loop-in-vision-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1640, \"height\": 633, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-019-e20e23dfd397-livevln-breaking-the-stop-and-go-loop-in-vision-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 875, \"height\": 578, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-019-e20e23dfd397-livevln-breaking-the-stop-and-go-loop-in-vision-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1132, \"height\": 495, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-019-e20e23dfd397-livevln-breaking-the-stop-and-go-loop-in-vision-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1704, \"height\": 266, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-019-e20e23dfd397-livevln-breaking-the-stop-and-go-loop-in-vision-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 882, \"height\": 300, \"label\": \"Table\"}]"
motivation: 现有导航系统因阻塞式感知-推理-执行循环导致实际部署时频繁停顿，亟需减少等待时延。
method: 提出LiveVLN，利用多步动作延续，将动作执行与新观测处理重叠，使动作流持续可用。
result: "在R2R/RxR保持基准性能；实际部署平均等待时间降低77.7%，总耗时缩短12.6%-19.6%。"
conclusion: LiveVLN即插即用，在不牺牲性能前提下显著提升导航连续性，适用于实际机器人系统。
---

## 摘要
最近的导航系统在基准测试中取得了强劲的结果，然而在实际部署中往往仍然呈现出明显的走走停停现象。这一瓶颈源于感知-推理-执行循环仍然是阻塞的：在每次新观察后，控制器必须等待感知、传输和推理完成后才能继续运动。因此，仅降低动作生成的代价并不能消除多余的等待。为了解决这个问题，我们提出了LiveVLN，一种无需训练、通过增强预训练VLM导航器实现多步动作延续的连续具身导航框架。LiveVLN不再为每个完整的感知与推理回合暂停，而是将执行与新到达观察的处理重叠在一起，使得在当前可执行前缀耗尽之前，可以传递刷新的未来动作。这种设计使得动作在运动过程中持续可用，减少了空闲等待，实现了更平滑的在线执行。该框架在运行时运行，可与兼容的预训练VLM导航器集成。在R2R和RxR上，LiveVLN在保持基准测试性能的同时，减少了等待时间并提高了动作可用性。在实际部署中，它在StreamVLN上平均减少每集等待时间高达77.7%，在NaVIDA上缩短挂钟时间12.6%，在部署中实现了更连贯的执行代码可在https://github.com/NIneeeeeem/LiveVLN获取。

## Abstract
Recent navigation systems achieve strong benchmark results, yet real-world deployment often remains visibly stop-and-go. This bottleneck arises because the sense-inference-execution loop is still blocking: after each new observation, the controller must wait for sensing, transmission, and inference before motion can continue. Reducing action-generation cost alone therefore does not remove redundant waiting. To address this issue, we present LiveVLN, a training-free framework for more continuous embodied navigation by augmenting pretrained VLM navigators with multi-step action continuation. Instead of pausing for each full sense-and-inference round, LiveVLN overlaps execution with the processing of newly arrived observations, allowing refreshed future actions to be handed off before the current executable prefix is exhausted. This design keeps actions continuously available during motion, reducing idle waiting and enabling smoother online execution. The framework operates at runtime and can be integrated with compatible pretrained VLM navigators. Across R2R and RxR, LiveVLN preserves benchmark performance while reducing waiting time and improving action availability. In real-world deployments, it cuts average episode waiting time by up to 77.7% and shortens wall-clock episode time by 12.6% on StreamVLN and 19.6% on NaVIDA, yielding more coherent execution during deployment. Code is available at https://github.com/NIneeeeeem/LiveVLN.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究背景**：视觉语言导航（VLN）旨在使具身智能体根据语言指令和第一人称视觉观察进行导航。近年来，基于更强跨模态预训练和Transformer推理的模型（如VLN-BERT、DUET）以及面向部署的视频VLM/VLA架构（如StreamVLN、NaVIDA）在R2R、RxR等基准上取得了优异表现。
- **核心问题**：尽管策略能力提升，但在实际流式部署中，机器人仍表现出明显的“走走停停”（stop-and-go）行为。其根本原因并非单纯计算成本问题，而是系统架构层面的**阻塞式感知-推理-执行（Sense-Inference-Execution）循环**。每次新观测后，控制器必须等待完整的感知、传输、预处理和动作生成完成后才能继续运动，导致大量空闲等待时间。
- **整体含义**：连续执行不仅取决于策略质量，更取决于运行时框架能否隐藏感知-推理延迟。论文通过真实机器人诊断发现，NaVIDA的等待时间占比高达30.5%，94.9%的推理轮次存在停走现象，证实了运行时优化的必要性。

## 二、论文提出的方法论
- **核心思想**：提出 **LiveVLN**，一种无需训练（training-free）的运行时框架。通过将当前执行与下一轮感知-推理过程**重叠**（overlap），使得在耗尽可能执行前缀之前，后台线程即可刷新并移交未来的动作序列，从而保持动作持续可用，减少空闲等待。
- **关键技术细节**：
    - **短视动作状态（Short-horizon Action State）**：将动作连续体分解为三个运行时角色：
        - **已执行动作（Executed Actions）**：当前短视状态中已消耗的动作。
        - **保护缓冲区（Guard Buffer）**：当前由控制器持有并正在执行的已释放动作前缀，提供连续运动的预算。
        - **可修正尾部（Revisable Tail）**：尚未释放给控制器的动作后缀，可被新观测结果覆盖。
    - **双线程架构**：
        - **线程A**：持续执行当前保护缓冲区中的动作，不中断。
        - **线程B**：使用最新观测并行执行推理，生成下一轮连续动作。
    - **受保护交接（Guarded Handoff）**：当后台推理在保护缓冲区耗尽前完成时，当前保护缓冲区晋升为已执行动作，刷新后的前缀成为新的保护缓冲区，剩余尾部保持可修正状态。
    - **实时自适应（Real-Time Adaptation）**：保护缓冲区的大小不是固定的，而是根据**近期感知-推理延迟的指数移动平均**动态调整。目标是使保护缓冲区的预计执行时间能够覆盖下一轮隐藏推理的预算时间（`ψ_{t+1} = ˜ℓ_{t+1,SI} + δ`），其中 `˜ℓ` 是平滑后的推理延迟，`δ` 是安全裕度。通过选取满足 `T(k)_{t+1} >= ψ_{t+1}` 的最短前缀作为保护缓冲区。
- **算法流程（文字描述）**：
    1.  后台线程B基于新观测和当前上下文生成完整连续动作 `ˆut+1`。
    2.  测量当前轮次的感知-推理延迟，更新滑动平均估计 `˜ℓ`，并计算下一个保护预算 `ψ`。
    3.  根据每个动作单元的预计执行时间 `τ(a)`，寻找满足累积执行时间覆盖 `ψ` 的最短前缀 `k*`，将 `ˆut+1` 拆分为 `[ˆgt+1 | ˆrt+1]`。
    4.  检查当前后台推理是否在已有保护缓冲区耗尽前完成。若满足条件，则释放新的保护缓冲区 `ˆgt+1`，将 `ˆrt+1` 保留为可修正尾部；否则触发备用动作或停止。

## 三、实验设计
- **数据集与场景**：
    - **仿真基准测试**：在 **R2R** 和 **RxR** 数据集的 `val_unseen` 划分上进行评估，模拟**连续环境（VLN-CE）**下的流式接口。
    - **真实机器人部署**：在 **Unitree G1** 机器人上，搭配Intel RealSense D455f相机（RGB输入）、NVIDIA RTX 5090 GPU（云端推理）进行流式部署。场景为共享办公环境，每项评估40次运行（8条指令×5次重复）。
- **基准测试（Benchmark）**：采用标准指标：导航误差（NE）、Oracle成功率（OS）、成功率（SR）、按路径加权的成功率（SPL）和归一化动态时间扭曲（nDTW）。
- **对比方法**：
    - 仿真基准：对比了NaVid、MapNav、NaViLA（含及不含额外数据）、UniNaVid、StreamVLN（含及不含额外数据）和NaVIDA。
    - 真实机器人：对比了各自**原生运行时（native blocking runtime）**下的**StreamVLN**和**NaVIDA**。LiveVLN使用完全相同的预训练检查点进行包装。

## 四、资源与算力
- 论文**未明确说明**用于预训练或全量仿真的具体算力信息（如GPU型号、数量、总训练时长等）。
- 在真实机器人部署部分，提及使用**NVIDIA RTX 5090 GPU**作为远程推理服务器，但未提及训练资源。

## 五、实验数量与充分性
- **实验数量**：
    - **仿真基准**：在R2R和RxR两个数据集的`val_unseen`上进行评估，对比了7个以上的基线方法（含不同变体）。
    - **真实机器人流式部署**：对两种导航器（StreamVLN和NaVIDA）分别进行原生运行时和LiveVLN包装的对比，共4个主要配置，每个配置重复40次运行。
    - **消融实验**：在NaVIDA上进行了4种变体的消融测试（原生、更多轮次阻塞、完整LiveVLN、无可修正尾部、无实时自适应）。
- **实验充分性**：实验设计较为全面，覆盖了标准性能评估、实际部署连续性评估和核心组件贡献分析。仿真结果证明了性能无损，真实机器人结果证明了连续性（等待时间、暂停次数）的大幅改进。消融实验有效分离了两个核心机制（可修正尾部和实时自适应）的贡献。
- **公平性**：在仿真和真实机器人对比中，LiveVLN均使用与对比方法完全相同的预训练检查点，排除了因策略质量差异带来的干扰，确保了对比的公平性。同时，报告了部署相关的连续性指标（等待时间、等待比例、暂停计数），超越了仅依赖导航成功率的传统评估。

## 六、论文的主要结论与发现
- **结论1：基准性能无损**。LiveVLN作为运行时框架，在不进行任何重新训练或架构修改的情况下，在R2R和RxR基准测试上保持了与原生运行时相当的导航性能，确认了改进主要来自运行时而非策略能力提升。
- **结论2：实际部署连续性显著提升**。在真实机器人上，LiveVLN将**平均等待时间降低了超过70%**（StreamVLN：77.7%，NaVIDA：72.8%），**暂停次数大幅减少**（StreamVLN：从6.75降至0.80；NaVIDA：从9.25降至1.20），**挂钟总时长缩短12.6%-19.6%**。
- **结论3：停走问题本质上是运行时问题**。论文明确指出，VLN中的走走停停不仅是策略质量问题，更是一个由于阻塞式感知-推理-执行循环导致的**运行时问题**。提升刷新频率但保持阻塞模式反而会增加等待时间。
- **结论4：核心机制的有效性**。消融实验表明，**异步重叠本身不足**以解决问题，必须结合**可修正尾部**（主要贡献于任务成功）和**实时自适应保护缓冲区**（主要贡献于隐藏延迟）才能最佳工作。
- **结论5：连续性和效率应作为一等部署指标**。论文建议，部署导向的VLN评估应将动作可用性相关的时序指标（如暂停计数、等待时间）视为与SR、SPL同等重要的指标。

## 七、优点
- **即插即用的运行时框架**：LiveVLN是一种**无需训练（training-free）**的方法，可直接应用于兼容的预训练VLM导航器（StreamVLN、NaVIDA等），无需任何重训练或架构修改，实用性和推广性极强。
- **双机制设计的巧妙性**：通过**受保护交接与可修正尾部**和**实时自适应**两个机制的协同工作，既保证了动作的连续可用性（隐藏延迟），又保留了基于新观测进行在线修正的能力（保持任务性能）。通过选取最短必要前缀作为保护缓冲区，实现了灵活性与可靠性的平衡。
- **侧重运行时而非策略**：论文的第一个核心贡献在于将“停走”问题的视角从策略质量转向了运行时架构，为后续的VLN部署研究提供了一个新的、正交的研究方向。
- **全面且公平的实验**：实验不仅关注标准导航性能，更引入了面向部署的连续性指标（等待时间、暂停计数等）。所有对比均使用相同检查点，确保了公平性。消融实验设计清晰，有效验证了各组件的独立贡献。
- **诊断性实验有力**：通过真实机器人的精细时序分析（`ℓ_gap`、`ℓ_infer`等），直观且定量地揭示了阻塞式运行时的问题根源和LiveVLN的有效性。

## 八、不足与局限
- **真实场景实验规模有限**：真实机器人评估仅在一个共享办公场景中进行，指令数量和重复次数相对有限（8条指令×5次重复=40次运行），泛化到更多样化、更复杂真实环境（如拥挤、动态变化环境）的效果尚不明确。
- **未完全解决执行瓶颈**：论文承认，减少等待时间后，物理执行时间（`T_execution`）仍然是主导因素，因此挂钟总时长的缩短存在上限。LiveVLN优化的是“隐藏”等待，而非加速实际运动。
- **对网络环境和硬件依赖**：保护缓冲区大小的自适应依赖于对感知-推理延迟的准确估计。通信抖动（论文中控制在50ms内）或硬件性能波动可能影响估计精度和实际表现。
- **泛化边界未充分探索**：LiveVLN的假设是导航器能输出有序的多步动作序列。该方法是否适用于输出非结构化动作或概率分布的策略尚不清楚。此外，论文未探讨对非VLM或传统方法的适用性。
- **未评估定位漂移与恢复能力**：论文主要关注运动连续性，但对因连续运动可能加剧的控制器漂移、以及漂移后的恢复能力未进行深入分析和评估。虽然在挂钟时间内完成了任务，但更长的动作执行序列可能引入累积误差。
- **计算资源细节缺失**：论文未提供仿真实验所耗算力（GPU、时间、能耗）等具体信息，不利于他人复现或评估资源成本。

（完）
