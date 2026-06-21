---
title: "AgentVLN: Towards Agentic Vision-and-Language Navigation"
title_zh: AgentVLN：迈向智能体视觉与语言导航
authors: "Zihao Xin, Wentong Li, Yixuan Jiang, Ziyuan Huang, Bin Wang, Piji Li, Jianke Zhu, Jie Qin, Shengjun Huang"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2603.17670v1"
arxiv_id: 2603.17670v1
arxiv_url: "https://arxiv.org/abs/2603.17670v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/010-2026_xin_agentvln-2e87ab92-73a08f336df1.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2603.17670v1", "query:Vision-and-Language Navigation", "query:Vision-Language Models", "query:Embodied Intelligence"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航面临空间感知不足和2D-3D表示不匹配的挑战。AgentVLN采用VLM-as-Brain范式，将高层语义推理与规划解耦，通过跨空间表示映射实现像素对齐提示，结合上下文自纠正和主动探索克服遮挡与误差累积。提出查询驱动感知链式思考解决空间歧义。在长程导航基准上取得一致最优结果，为轻量级部署提供新范式。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-010-73a08f336df1-agentvln-towards-agentic-vision-and-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 733, \"height\": 424, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-010-73a08f336df1-agentvln-towards-agentic-vision-and-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1253, \"height\": 606, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-010-73a08f336df1-agentvln-towards-agentic-vision-and-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1241, \"height\": 542, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-010-73a08f336df1-agentvln-towards-agentic-vision-and-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1260, \"height\": 568, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-010-73a08f336df1-agentvln-towards-agentic-vision-and-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 755, \"height\": 455, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-010-73a08f336df1-agentvln-towards-agentic-vision-and-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1120, \"height\": 1222, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-010-73a08f336df1-agentvln-towards-agentic-vision-and-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1177, \"height\": 867, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-010-73a08f336df1-agentvln-towards-agentic-vision-and-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1268, \"height\": 228, \"label\": \"Table\"}]"
motivation: 现有VLN方法受限于有限空间感知、2D-3D表示不匹配和单目尺度模糊，导致长程导航性能不佳。
method: 将VLN建模为部分可观测半马尔可夫决策过程，引入VLM作为大脑，设计跨空间表示映射和查询驱动感知链式思考，结合自纠正与主动探索。
result: 在多个长程VLN基准上，AgentVLN一致超越先前最先进方法，尤其在高难度场景中表现优越。
conclusion: AgentVLN通过模块化解耦与视觉-语言对齐，实现了高效且可部署的轻量级导航框架，推动了下一代具身导航模型的发展。
---

## 摘要
视觉与语言导航（VLN）要求具身智能体将复杂的自然语言指令在未知环境中转化为长程导航。尽管视觉-语言模型（VLM）提供了强大的2D语义理解能力，但当前的VLN系统仍受限于有限的空间感知、2D-3D表示不匹配以及单目尺度模糊性。本文提出AgentVLN，一种新颖且高效的具身导航框架，可在边缘计算平台上部署。我们将VLN建模为部分可观测半马尔可夫决策过程（POSMDP），并引入“VLM-作为-大脑”范式，通过即插即用的技能库将高层语义推理与感知和规划解耦。为解决多级表示不一致性，我们设计了跨空间表示映射，将感知层的3D拓扑路径点投影到图像平面，为VLM生成像素对齐的视觉提示。在此桥梁基础上，我们集成了上下文感知的自校正和主动探索策略，以从遮挡中恢复并抑制长轨迹上的误差累积。为进一步解决非结构化环境中指令的空间模糊性，我们提出了查询驱动的感知思维链（QD-PCoT）方案，赋予智能体元认知能力，使其主动获取几何深度信息。最后，我们构建了AgentVLN-Instruct，一个大规模指令微调数据集，具有基于目标可见性的动态阶段路由。大量实验表明，AgentVLN在长程VLN基准测试上持续优于先前的最先进方法（SOTA），为下一代具身导航模型的轻量级部署提供了实用范式。

## Abstract
Vision-and-Language Navigation (VLN) requires an embodied agent to ground complex natural-language instructions into long-horizon navigation in unseen environments. While Vision-Language Models (VLMs) offer strong 2D semantic understanding, current VLN systems remain constrained by limited spatial perception, 2D–3D representation mismatch, and monocular scale ambiguity. In this paper, we propose AgentVLN, a novel and efficient embodied navigation framework that can be deployed on edge computing platforms. We formulate VLN as a Partially Observable Semi-Markov Decision Process (POSMDP) and introduce a VLM-as-Brain paradigm that decouples high-level semantic reasoning from perception and planning via a plug-and-play skill library. To resolve multi-level representation inconsistency, we design a cross-space representation mapping that projects perception-layer 3D topological waypoints into the image plane, yielding pixel-aligned visual prompts for the VLM. Building on this bridge, we integrate a context-aware self-correction and active exploration strategy to recover from occlusions and suppress error accumulation over long trajectories. To further address the spatial ambiguity of instructions in unstructured environments, we propose a Query-Driven Perceptual Chain-of-Thought (QD-PCoT) scheme, enabling the agent with the metacognitive ability to actively seek geometric depth information. Finally, we construct AgentVLN-Instruct, a large-scale instruction-tuning dataset with dynamic stage routing conditioned on target visibility. Extensive experiments show that AgentVLN consistently outperforms prior state-of-the-art methods (SOTA) on long-horizon VLN benchmarks, offering a practical paradigm for lightweight deployment of next-generation embodied navigation models.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 视觉与语言导航（VLN）要求具身智能体在未知环境中根据自然语言指令进行长时域导航，具身智能体需理解2D图像语义并转换到3D物理空间。
- 现有VLN系统面临三大核心挑战：
  - **空间感知不足**：单目RGB观测缺乏可靠的深度线索，VLM难以推理3D几何和度量尺度。
  - **2D-3D表示不匹配**：双系统方法（如使用扩散模型生成3D轨迹并用VLM做全局规划）中，生成的3D轨迹与VLM的2D视觉表示之间存在跨空间脱节。
  - **单目尺度模糊**：涉及空间介词（如“在…前面几米”）的指令难以通过纯RGB图像解析。
- 主流范式（单系统端到端黑盒映射、双系统分层规划）均存在泛化性差、计算开销大、无法在边缘设备上实时推理等问题。
- 本文旨在提出一个轻量、高效、可部署的通用具身导航框架，使VLM作为中枢大脑（VLM-as-Brain），通过显式解耦高层推理与低层规划，解决上述缺陷。

## 二、论文提出的方法论
- **核心思想**：将VLN建模为部分可观测半马尔可夫决策过程（POSMDP），引入VLM作为中央控制器，通过即插即用的技能库交替调用感知层技能和规划层技能，实现从短时探索到长程导航的无缝缩放。
- **关键技术细节**：
  - **跨空间表示映射**：将感知层的3D全局路径点通过相机位姿逆变换和透视投影，显式映射到2D图像平面上，生成像素对齐的视觉提示（如绿色点标记），供VLM直接选择。无需在隐式高维空间中强制对齐多模态特征。
  - **上下文感知的自校正与主动探索**：当VLM无法在当前场景中找到与指令语义匹配的可行路径投影时，它会基于历史上下文和当前观测输出细粒度动作（前/左/右），进行局部探索或纠偏；一旦恢复全局路径映射，则重新切换回宏观技能调度。
  - **查询驱动感知思维链（QD-PCoT）**：在局部目标定位阶段，当模型检测到空间歧义时，主动生成自然语言查询（如“前面的椅子距离我几米？”）并调用感知层技能获取几何反馈，将多轮交互的显式推理结果集成到上下文，最终输出与指令一致的精确像素坐标，再通过反投影转换为3D目标点。
  - **AgentVLN-Instruct数据集**：基于Habitat模拟器构建，包含动态阶段路由机制（根据目标是否可见切换粗导航-精定位），并加入轨迹噪声、多轮推理问答，以对齐指令与技能调用。
- **公式流程**（文字说明）：
  - 决策公式：在每步决策时，VLM根据历史上下文、观测和指令输出技能调用指令 \(c_k \sim \pi_\theta(f|\mathcal{H}_{t_k}, o_{t_k}, \mathcal{I})\)，其中技能集分为感知技能（\(\tau=0\)）和规划技能（\(\tau>0\)）。
  - 规划技能执行：产生连续动作序列，通过终止条件 \(\beta_{f}(s_{t+\tau})\) 判断是否需VLM重新介入。
  - 3D-2D映射：3D路径点 \(\mathbf{P}_w\) 通过 \(s\cdot \mathbf{p}_{path}^{img} = K R_t^{-1}(\mathbf{P}_{path}^w - \mathbf{t}_t)\) 转为2D像素坐标。
  - 目标点反投影：从深度图提取深度 \(d_{target}\)，经逆投影 \(\mathbf{P}_{target}^c = d_{target} \cdot K^{-1} \mathbf{p}_{target}^{img}\) 再变换到世界坐标系。

## 三、实验设计
- **数据集**：R2R-CE（Room-to-Room Continuous Environment）和RxR-CE（Room-across-Room）的Val-Unseen（验证集未见环境）作为主要基准。同时构建了AgentVLN-Instruct（基于Habitat模拟器）用于指令微调，并加入LLaVA-Video-178K数据集以保持通用多模态能力。
- **基准（Benchmark）**：采用标准VLN指标：成功率（SR）、Oracle成功率（OS）、路径长度加权成功率（SPL）、导航误差（NE），以及nDTW（仅RxR）。
- **对比方法**：涵盖单系统方法（NaVid、Uni-NaVid、NaVILA、StreamVLN、NavFoM、DecoVLN、JanusVLN、EfficientVLN）和双系统方法（DualVLN、InternVLA-N1），以及基于多种传感器输入的方法（VLN BERT、CMA、Reborn、ETPNav、LAW等）。特别关注参数规模相近的轻量级模型。
- **真实世界部署**：在Unitree Go2四足机器人上搭载Intel RealSense D455相机，使用RTAB-Map进行SLAM，在室内外环境评估导航性能。
- **消融实验**：
  - 渐进式消融：逐个加入VLM-as-Brain、上下文细粒度策略、QD-PCoT，观察各模块贡献。
  - 时间上下文长度消融：测试2、4、8、10帧历史上下文的影响。

## 四、资源与算力
- **训练硬件**：32张NVIDIA A100 GPU。
- **训练设置**：使用AdamW优化器，batch size 128；学习率采用余弦退火策略，初始峰值 \(2\times10^{-5}\)，前3%步数进行warmup；冻结视觉编码器和多模态投影层，仅微调语言模型部分。
- **推理硬件**：可在Jetson嵌入式边缘板上实时本地推理，无需云端部署。
- **说明**：论文未明确报告总训练时间或具体迭代轮数，但指出模型采用Qwen2.5-VL-3B作为基座，参数规模仅3B，远小于现有7~8B模型。

## 五、实验数量与充分性
- **主要实验**：在R2R-CE和RxR-CE的Val-Unseen上报告完整导航指标，共两组表（Table 1和Table 2）。每组表格对比10+种主流方法。
- **消融实验**：一组渐进式模块消融（Table 3，4种设置），一组时间上下文长度消融（图5，4种长度）。
- **真实世界**：展示2个场景（室内、室外）的导航结果（图4），未量化指标但提供定性验证。
- **充分性分析**：
  - 覆盖了仿真和真实场景，对比方法全面，包括同架构（双系统）和不同规模模型。
  - 消融实验覆盖了核心模块（跨空间映射、自校正、QD-PCoT）和超参数（上下文长度）。
  - 实验设计相对客观公平：在相同基准下比较，使用标准指标，且AgentVLN参数更小却取得更好结果。
  - 局限性：仅在Val-Unseen上报告结果，未提供测试集（Test-Unseen）结果；真实世界实验只有定性展示，缺乏定量评估；未与其他方法在真实场景中横向对比。

## 六、论文的主要结论与发现
- AgentVLN在R2R-CE Val-Unseen上取得SR 67.2%、SPL 64.7%，超越所有对比方法（包括7B、8B规模模型），且参数仅3B。
- 在RxR-CE Val-Unseen上SR达69.5%、SPL 61.3%，同样优于EfficientVLN等轻量模型。
- 消融表明：每个模块（VLM-as-Brain、细粒度自校正、QD-PCoT）均带来显著提升；最佳时间上下文长度为8帧。
- 跨空间表示映射有效解耦了VLM的语义理解与3D几何推理，避免了隐式对齐的困难。
- QD-PCoT在不增加参数的前提下消除了单目深度歧义，提高了局部定位精度。
- 真实世界部署验证了AgentVLN可在室内外环境稳定运行，具备低延迟、无需云端的优势。

## 七、优点
- **轻量高效**：仅3B参数，可在Jetson边缘设备实时推理，无需远程云端，大幅降低通信和推理延迟。
- **模块化可扩展**：采用技能库机制，任务迁移只需更换感知/规划模块，无需重训VLM。
- **显式2D-3D对齐**：通过透视投影将3D路径点转成像素视觉提示，让VLM在熟悉的2D空间进行推理，解决了跨空间表示不一致问题。
- **主动纠错与元认知**：上下文自校正策略和QD-PCoT分别处理环境变化和空间歧义，增强了鲁棒性和可解释性。
- **数据构建创新**：AgentVLN-Instruct数据集引入动态阶段路由，模拟人类粗定位-精定位的导航习惯，对齐指令与技能调用。
- **实验充分且公平**：在多个仿真基准上全面对比，并完成真实世界验证，消融实验清晰展示各组件贡献。

## 八、不足与局限
- **未报告测试集结果**：论文仅在Val-Unseen上给出结果，未提供Test-Unseen（官方竞赛拆分）上的性能，无法确认模型在标准封闭测试集上的泛化水平。
- **真实世界评估不足**：仅有定性图片展示，缺乏定量指标（如成功率、路径长度、碰撞次数等），与其他方法的真实场景对比也未进行。
- **时间上下文长度敏感**：最佳长度为8帧，过短或过长均导致性能下降，说明模型对历史信息长度有较强依赖，可能影响极长序列的稳定性。
- **依赖深度传感器**：系统需要深度信息（D455相机或模拟器深度）进行3D-2D映射和目标定位，在无深度传感器的平台上部署受限（尽管论文声称可更换技能库，但未验证纯RGB方案）。
- **仅测试单一机器人平台**：真实部署仅在Unitree Go2上进行，未在轮式或其它足式机器人上验证，泛化至不同运动学结构的鲁棒性未知。
- **计算成本未详细说明**：虽然推理端轻量，但训练使用了32张A100 GPU，训练时间和成本未披露，可能对资源有限的研究者不够友好。
- **复杂度高的指令处理未深入**：QD-PCoT依赖VLM自身生成自然语言查询，当指令极其模糊或涉及复杂空间关系时，查询质量可能下降，论文未对此进行边界分析。

（完）
