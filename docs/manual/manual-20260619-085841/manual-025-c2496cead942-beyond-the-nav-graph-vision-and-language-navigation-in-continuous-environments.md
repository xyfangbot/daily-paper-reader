---
title: "Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments"
title_zh: 超越导航图：连续环境下的视觉与语言导航
authors: "Jacob Krantz, Erik Wijmans, Arjun Majumdar, Dhruv Batra, Stefan Lee"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/025-2020_krantz_vln_ce-acbfcd3a-c2496cead942.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Embodied Agents", "query:Continuous Environments"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有视觉语言导航任务基于稀疏导航图，假设已知拓扑和完美定位，导致性能高估。本文提出连续3D环境下的语言导航任务，要求智能体执行低级动作遵循指令。实验表明，在该设置下模型性能远低于图设置，揭示了先前成果被膨胀的事实。该工作为更真实的导航研究提供了基准。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-025-c2496cead942-beyond-the-nav-graph-vision-and-language-navigation-in-continuous-environments/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1254, \"height\": 319, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-025-c2496cead942-beyond-the-nav-graph-vision-and-language-navigation-in-continuous-environments/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1250, \"height\": 213, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-025-c2496cead942-beyond-the-nav-graph-vision-and-language-navigation-in-continuous-environments/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1257, \"height\": 353, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-025-c2496cead942-beyond-the-nav-graph-vision-and-language-navigation-in-continuous-environments/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1260, \"height\": 386, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-025-c2496cead942-beyond-the-nav-graph-vision-and-language-navigation-in-continuous-environments/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1125, \"height\": 694, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-025-c2496cead942-beyond-the-nav-graph-vision-and-language-navigation-in-continuous-environments/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1255, \"height\": 247, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-025-c2496cead942-beyond-the-nav-graph-vision-and-language-navigation-in-continuous-environments/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1139, \"height\": 233, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-025-c2496cead942-beyond-the-nav-graph-vision-and-language-navigation-in-continuous-environments/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1262, \"height\": 339, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-025-c2496cead942-beyond-the-nav-graph-vision-and-language-navigation-in-continuous-environments/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1262, \"height\": 533, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-025-c2496cead942-beyond-the-nav-graph-vision-and-language-navigation-in-continuous-environments/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1265, \"height\": 274, \"label\": \"Table\"}]"
motivation: 消除导航图设定中已知拓扑、短程导航和完美定位等不切实际的假设，建立更真实的连续环境导航任务。
method: 在连续3D环境中定义语言导航任务，智能体需通过低级动作（如移动、转向）执行自然语言指令。
result: "连续环境下模型性能显著低于导航图设置，幅度超过50%，表明先前成果因隐式假设而被高估。"
conclusion: 连续环境设定揭示了视觉语言导航的真实难度，并提供了更可靠的性能评估基准。
---

## 摘要
我们在连续3D环境中开发了一项语言引导的导航任务，其中智能体必须执行低级动作来遵循自然语言导航指令。通过置于连续环境中，该设置消除了先前工作中隐含的多项假设，这些假设将环境表示为稀疏的全景图，其中边对应可导航性。具体而言，我们的设置放弃了已知环境拓扑、短程先知导航和完美智能体定位的假设。为了将这一新任务置于背景中，我们开发了镜像先前设置中许多进展的模型以及单模态基线。虽然其中一些技术可以迁移，但我们发现在连续设置中绝对性能显著降低——这表明先前“导航图”设置中的性能可能因强隐式假设而被夸大。

## Abstract
We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions. By being situated in continuous environments, this setting lifts a number of assumptions implicit in prior work that represents environments as a sparse graph of panoramas with edges corresponding to navigability. Specifically, our setting drops the presumptions of known environment topologies, short-range oracle navigation, and perfect agent localization. To contextualize this new task, we develop models that mirror many of the advances made in prior settings as well as single-modality baselines. While some of these techniques transfer, we find significantly lower absolute performance in the continuous setting – suggesting that performance in prior 'navigation-graph' settings may be inflated by the strong implicit assumptions.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有Vision-and-Language Navigation（VLN）任务基于导航图（nav-graph）设定，隐含了已知环境拓扑、短程先知导航（oracle navigation）和完美智能体定位等不切实际的假设。这些假设使得任务过于简化，性能被高估，无法真实反映机器人实际导航的挑战。
- **研究动机**：为了更贴近真实世界中的机器人指令跟随场景，需要消除这些假设，在连续3D环境中重新定义语言引导导航任务。
- **整体含义**：本文提出了Vision-and-Language Navigation in Continuous Environments（VLN-CE），要求智能体通过低层级动作（如前进0.25m、旋转15°）自由导航，并仅依赖自我中心的RGB-D观测。该设置更真实地模拟了机器人的感知与控制，为评估和推动语言导航研究提供了更可靠的基础。

## 二、论文提出的方法论
- **核心思想**：将VLN任务从固定拓扑的导航图迁移到连续3D环境（基于Habitat模拟器），智能体可自由移动到任何无障碍点，动作空间为低级动作（move forward 0.25m, turn left/right 15°, stop）。智能体不获得位置或朝向信息，必须通过视觉和语言指令进行决策。
- **关键技术细节**：
  - **数据转换**：将Room-to-Room（R2R）数据集中的导航图轨迹转换为连续环境中的可导航路径。通过对每个节点向下投射射线寻找最近可导航点，并利用A*验证路径连通性。最终得到4475条成功转换的轨迹，平均动作长度约为55步（原R2R仅4-6步）。
  - **模型架构**：
    - **Seq2Seq基线模型**：使用ResNet50（ImageNet预训练）编码RGB，ResNet50（点目标导航预训练）编码深度。指令用LSTM编码，将视觉特征平均池化后与指令表示拼接，输入GRU策略网络输出动作。
    - **Cross-Modal Attention模型**：包含两个GRU，一个负责跟踪视觉观测，另一个基于注意力机制对指令和视觉特征进行跨模态融合。使用Bi-LSTM编码指令，并对指令、RGB和深度分别计算缩放点积注意力。
  - **训练增强**：
    - 模仿学习 + 拐点加权（inflection weighting）。
    - **DAgger**（数据集聚合）：收集策略轨迹并混合专家动作进行迭代训练。
    - **数据增强**：使用合成生成的约15万条轨迹（来自Tan et al. 2019）扩展训练数据。
    - **进度监控（Progress Monitor）**：辅助损失预测已完成轨迹比例，帮助判断停止时机。

## 三、实验设计
- **数据集与环境**：使用Matterport3D数据集，在Habitat模拟器中进行。VLN-CE数据集由R2R轨迹转换而来，共4475条轨迹，分为训练集、验证集（val-seen/val-unseen）和测试集。
- **评估指标**：路径长度（TL）、导航误差（NE）、oracle成功率（OS）、成功率（SR）、SPL（成功率加权路径长度）、nDTW（归一化动态时间规整）。
- **对比方法**：
  - 无学习基线：随机动作、手工规则（随机朝向+前进）。
  - 单模态消融：去除RGB、深度、指令或全部视觉。
  - 模型对比：Seq2Seq vs Cross-Modal Attention。
  - 训练增强消融：仅教师强迫、加入进度监控、DAgger、数据增强及组合。
  - 跨设置对比：将VLN-CE模型路径转换回导航图，与VLN已有方法（如VLN-Seq2Seq、Self-Monitoring、RCM、Back-Translation）在VLN验证集和测试集上比较。

## 四、资源与算力
- **明确说明**：论文未明确提及所使用的GPU型号、数量或训练时长。仅提到使用Adam优化器，学习率2.5×10⁻⁴，batch size为5条完整轨迹。最大训练30个epoch（教师强迫），DAgger迭代6-10轮。训练细节中未指定硬件资源。

## 五、实验数量与充分性
- **实验组数较多**：共包含：
  - 表2：7种输入条件（随机、手工、完整Seq2Seq及其4种消融）。
  - 表3：Seq2Seq和Cross-Modal Attention在5种训练增强组合下的结果（共12行），覆盖验证集seen和unseen。
  - 表4：将最佳模型与VLN已有方法在三个测试集（val-seen、val-unseen、test）上对比。
  - 此外包含定性示例（图5）及路径转换可视化。
- **充分性与公平性**：
  - **充分**：多维度消融（输入模态、模型架构、训练策略），并跨设置对比，实验设计较为全面。
  - **客观**：采用标准指标，对比基线包括无学习方法和公开方法，结论清晰。但未测试真实机器人，也未与强化学习（RL）或其他高级规划方法进行对比。

## 六、论文的主要结论与发现
- **连续环境大幅降低了性能**：最佳模型在val-unseen上SR约32%、SPL 0.30，而导航图设置（如RCM）可达到SR 42%、SPL 0.38，差距显著，表明先前结果被nav-graph假设高估。
- **深度信号至关重要**：去掉深度后模型成功率低于1%（几乎随机），而去掉RGB仍有17%成功率，说明深度是学习导航的基础。
- **某些VLN技术迁移效果不佳**：进度监控和数据增强单独使用反而降低性能，但与DAgger组合后有效。DAgger是唯一稳定提升的技术。
- **导航图提供了强先验结构**：随机/手工基线在VLN-CE中成功率仅3%，而在VLN中可达16%，说明导航图隐式提供了环境布局信息。

## 七、优点
- **问题定义清晰且合理**：摆脱了导航图的不现实假设，更贴近真实机器人场景，为后续研究提供了更真实的基准。
- **数据集和处理流程严谨**：仔细处理了R2R轨迹到连续环境的转换（98.3%节点成功映射，77%轨迹可导航），并公开了代码和模型（GitHub）。
- **实验设计全面**：涵盖了输入模态、模型架构、训练增强的多种消融，并与原VLN设置进行跨任务对比，揭示了性能差异的根本原因。
- **结论具有启发性**：明确指出了导航图设定下性能被高估的问题，并提供了连续环境下的基线结果。

## 八、不足与局限
- **未探索模块化方法**：所有模型采用端到端映射，未探讨将高级指令传递至运动控制器的模块化方案，而后者可能更接近实际系统。
- **未考虑真实机器人噪声**：虽设计了低级动作，但模拟器中的动作是完美的（无打滑、无传感器噪声），忽略了真实执行误差。
- **动作空间较为简单**：仅四种动作，不包括更复杂的操作（如转弯幅度可变、后退、侧移等），限制了动作表达的丰富性。
- **部分轨迹不可用**：约23%的原始R2R轨迹因环境重建问题或节点无法映射而被排除，可能引入偏差（例如排除的轨迹可能包含更多困难场景）。
- **计算资源未报告**：不利于复现和效率比较。
- **训练增强相关性不足**：数据增强（合成指令）和进度监控的负面效果未得到充分解释，实验未分析过拟合的根本原因。

（完）
