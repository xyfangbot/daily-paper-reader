---
title: "REVERIE: Remote Embodied Visual Referring Expression in Real Indoor Environments"
title_zh: "REVERIE: 真实室内环境中的远程具身视觉指代表达"
authors: "Yuankai Qi, Qi Wu, Peter Anderson, Xin Wang, William Yang Wang, Chunhua Shen, Anton van den Hengel"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/011-2020_qi_reverie-afe090ce-1bdd8f6d3900.pdf
tags: ["query:手动上传", "paper:PDF", "query:Remote Embodied Visual Referring Expression", "query:Vision-and-Language Navigation", "query:Object Grounding", "query:Indoor Environments", "query:Robot Tasking"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 机器人需要理解自然语言并导航到目标物体，是长期挑战。REVERIE数据集提出基于真实图像的复杂导航任务，要求根据指令在未见环境中定位物体。现有模型表现不佳，新提出的Interactive Navigator-Pointer模型取得最佳结果，但仍远低于人类。该工作为推动人机交互研究提供了新基准。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 862, \"height\": 745, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 867, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 872, \"height\": 263, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 880, \"height\": 308, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1618, \"height\": 654, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 704, \"height\": 385, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 701, \"height\": 387, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 698, \"height\": 381, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 713, \"height\": 384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 706, \"height\": 385, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 707, \"height\": 382, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1691, \"height\": 639, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1782, \"height\": 969, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1453, \"height\": 77, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1488, \"height\": 843, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 896, \"height\": 165, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1477, \"height\": 2520, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1786, \"height\": 427, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1632, \"height\": 393, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1806, \"height\": 429, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-011-1bdd8f6d3900-reverie-remote-embodied-visual-referring-expression-in-real-indoor-environments/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 737, \"height\": 226, \"label\": \"Table\"}]"
motivation: 让机器人像人类一样通过自然语言在视觉世界中交互，需完成复杂导航指令任务。
method: 构建REVERIE数据集，包含自然语言描述的导航指代任务，并提出Interactive Navigator-Pointer基线模型。
result: 现有方法效果差，新模型在未见场景测试集上最优，但与人类性能差距显著。
conclusion: 任务难度大，模型提升空间广阔，为机器人视觉语言导航研究提供新方向。
---

## 摘要
机器人学的长期挑战之一是使机器人能够通过自然语言与人类在视觉世界中进行交互，因为人类是通过语言交流的视觉动物。克服这一挑战需要能够根据人类的各种指令执行各种复杂任务。为了推动人与机器人之间更灵活、更强大的交互，我们提出了一个包含多种复杂机器人任务的数据集，这些任务用自然语言描述，涉及大量真实图像中可见的物体。给定一个指令，成功需要导航通过一个未曾见过的环境来识别一个物体。这是一个实际挑战，但紧密反映了机器人学中的核心视觉问题之一。我们测试了几种最先进的视觉与语言导航和指代表达模型，以验证这一新任务的难度，但由于我们的任务与之前的任务存在许多根本性差异，没有一种模型显示出有希望的结果。我们还提出了一种新颖的交互式导航-指针模型，为该任务提供了强大的基线。所提出的模型在未见测试集上取得了最佳性能，但与人类表现相比仍有很大的改进空间。

## Abstract
One of the long-term challenges of robotics is to enable robots to interact with humans in the visual world via natural language, as humans are visual animals that communicate through language. Overcoming this challenge requires the ability to perform a wide variety of complex tasks in response to multifarious instructions from humans. In the hope that it might drive progress towards more flexible and powerful human interactions with robots, we propose a dataset of varied and complex robot tasks, described in natural language, in terms of objects visible in a large set of real images. Given an instruction, success requires navigating through a previously-unseen environment to identify an object. This represents a practical challenge, but one that closely reflects one of the core visual problems in robotics. Several state-of-the-art vision-and-language navigation, and referring-expression models are tested to verify the difficulty of this new task, but none of them show promising results because there are many fundamental differences between our task and previous ones. A novel Interactive Navigator-Pointer model is also proposed that provides a strong baseline on the task. The proposed model especially achieves the best performance on the unseen test split, but still leaves substantial room for improvement compared to the human performance.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 研究动机：使机器人能够像人类一样通过自然语言指令在真实室内环境中执行远程物体定位任务（例如“把一楼楼梯旁最下面的画带给我”），这是实现人机自然交互的关键挑战。
- 背景：现有视觉语言导航（VLN）任务仅要求导航到位置，不要求精确物体定位；指代表达（RefExp）任务仅处理单张图片中的物体，忽略导航步骤。REVERIE 将两者结合，要求智能体先导航到目标区域，再识别出指令引用的远程物体，更贴近实际机器人操作场景。
- 核心问题：当前方法（如 R2R、SelfMonitor、FAST-Short 等）无法有效处理远程物体指代，因为存在三大差异：目标物体在初始视角不可见、候选物体数量远多于单图任务、物体外观随视角变化剧烈。

## 二、论文提出的方法论
- 核心思想：提出“交互式导航-指针”（Interactive Navigator-Pointer）模型，让导航器（Navigator）和指针（Pointer）相互协作，指针为导航器提供物体级的视觉和语义线索，引导导航器更精准地停靠。
- 关键技术细节：
  - 导航器（Navigator）：基于 FAST-Short 的序列到序列 LSTM 架构，采用视觉-文本共注意力和回溯机制，将指针提供的增强特征用于动作选择。
  - 指针（Pointer）：采用 MAttNet，将指令分解为主体外观、位置、关系三个模块，计算每个候选物体与指令的匹配分数，选出 top-3 物体。
  - 交互模块（Interaction Module）：将指针选出的 top-3 物体的类别标签（经 Bi-LSTM 编码）和视觉特征（ResNet FC7 层平均）与原始全景特征拼接，作为导航器下一时刻的输入。公式为：\( v'_{t,k} = [v_{t,k}, x^o_{t,k}, v^o_{t,k}] \)。
- 损失函数：
  - 导航损失 \( \mathcal{L}_{\text{nav}} \)：动作选择的交叉熵损失 + 进度估计的均方误差损失。
  - 指代损失 \( \mathcal{L}_{\text{exp}} \)：基于三元组排序的损失，鼓励正确（物体，表达式）对的得分高于错误对。
  - 总损失：\( \mathcal{L} = \mathcal{L}_{\text{nav}} + \lambda_4 \mathcal{L}_{\text{exp}} \)（默认 λ₄=1.0）。

## 三、实验设计
- 数据集：基于 Matterport3D 仿真器构建的 REVERIE 数据集，包含 90 栋建筑、10,567 个全景图、4,140 个目标物体（489 类）、21,702 条人工标注指令（平均长度 18 词）。分为训练集（59 场景）、验证集（63 场景，含 seen/unseen）、测试集（16 场景，不公开标签）。
- 基准（Benchmark）：
  - 导航指标：成功率（Succ.）、Oracle 成功率、SPL、路径长度。
  - REVERIE 指标：正确输出目标物体边界框（IoU≥0.5）的比例。
- 对比方法：
  - 基线：Random、Shortest、R2R-TF、R2R-SF。
  - SOTA 导航方法：SelfMonitor、RCM、FAST-Short、FAST-Lan-Only（纯语言）。
  - 结合所有导航方法与 MAttNet 指针评估 REVERIE 成功率。
  - 额外实验：指代表达单独性能（在真实目标位置测试 MAttNet、CM-Erase、CNN-RNN 基线）。
  - 人类性能：通过 WebGL 界面让工人在测试集上执行任务。

## 四、资源与算力
- 文中未明确说明使用的 GPU 型号、数量或训练时长，仅提及“代码和数据集将会发布”。无法从文本中推断具体算力开销。

## 五、实验数量与充分性
- 实验数量：主要呈现了 1 个核心结果表（表 3，导航+指代联合评估）和 1 个指代表达单独结果表（表 4）。消融实验仅通过对比 FAST-Short 与提出的交互模型体现（Ours vs FAST-Short），未见详细的模块消融（如去掉交互、更改 top-k 等）。
- 充分性：实验覆盖了随机、最短路、多种 SOTA 方法，并在 seen/unseen/test 三个子集上汇报结果，同时与人类性能对比。但是消融实验数量偏少，且未分析超参数（如交互模块中 top-3 的敏感性、损失权重 λ₄ 的影响等）。
- 客观性与公平性：所有方法在同一仿真器上评估，指标定义清晰。但未报告多次运行的平均结果和标准差，可能存在随机性影响。

## 六、论文的主要结论与发现
- 核心结论：REVERIE 任务极具挑战性，现有方法在测试集上仅达到 7.07% 的成功率，远低于人类的 77.84%。
- 发现 1：简单组合导航器和指针效果不佳，交互式协作能显著提升（Ours 在测试集上达到 11.28%，相比非交互的 FAST-Short 的 7.07% 提升 4.21%）。
- 发现 2：导航在 REVERIE 上比传统 VLN 任务困难得多（SPL 从 R2R 上的 43% 跌至 6.17%），主要因为远程目标需要更长的语义推理。
- 发现 3：指代表达单独在真实目标位置评估时，SOTA 方法也仅约 50%，仍有 40% 差距到人类，说明物体识别和语言理解本身还未解决。
- 结论：REVERIE 是一个有意义且具有挑战性的基准，能够推动机器人的视觉语言理解与导航能力。

## 七、优点
- 任务设计创新：首次将远程物体导航与指代定位结合，更贴近实际机器人指令场景。
- 数据集高质量：基于真实建筑的三维扫描，指令自然多样（如包含空间关系、修饰语、共指等），且提供物体级边界框和类别标注。
- 模型设计合理：交互模块简单有效，将指针的 top-3 物体线索注入导航器，实现了导航与指代的互补。
- 开源与评估：仿真器和数据集将公开，并计划提供在线评测服务器，有利于后续研究对比。

## 八、不足与局限
- 实验覆盖不足：消融实验过于简化（仅对比有无交互模块），未深入分析各子模块（如 top-k 数量、视觉/文本特征融合方式）的贡献。
- 未报告统计显著性：所有结果仅列单一数值，未提供多次运行的均值和方差，无法评估模型稳定性。
- 偏差风险：指令收集时限制了“风格不限”，但仍可能存在语言分布偏差（如“bathroom”高频出现）；数据集仅包含 90 栋建筑，场景多样性有限。
- 应用限制：所有实验在仿真器中进行，未在真实机器人上验证；物体识别依赖于预定义的 3D 边界框，真实环境中物体检测更复杂。
- 资源信息缺失：未说明训练所需算力，不利于其他研究者复现或估计成本。

（完）
