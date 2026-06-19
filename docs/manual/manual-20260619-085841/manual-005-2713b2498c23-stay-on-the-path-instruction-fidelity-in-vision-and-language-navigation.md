---
title: "Stay on the Path: Instruction Fidelity in Vision-and-Language Navigation"
title_zh: 遵循路径：视觉与语言导航中的指令忠诚度
authors: "Vihan Jain, Gabriel Magalhaes, Alexander Ku, Ashish Vaswani, Eugene Ie, Jason Baldridge"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/005-2019_jain_r4r_cls-74efbccb-2713b2498c23.pdf
tags: ["query:手动上传", "paper:PDF", "query:Vision-and-Language Navigation", "query:Instruction Fidelity", "query:Coverage weighted by Length Score (CLS)", "query:Room-for-Room (R4R)", "query:Path Coverage"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 视觉语言导航任务中，现有评估指标只关注目标完成，忽略了指令遵循。本文提出新的CLS指标，通过路径覆盖和长度加权来评估指令遵循度，并构建了更具挑战性的R4R数据集。实验表明，奖励指令遵循的代理在指令执行上显著优于仅关注目标完成的代理。该工作强调了语言理解在VLN中的核心地位，为未来研究提供了更合理的评估基准。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-005-2713b2498c23-stay-on-the-path-instruction-fidelity-in-vision-and-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 758, \"height\": 382, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-005-2713b2498c23-stay-on-the-path-instruction-fidelity-in-vision-and-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 658, \"height\": 347, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-005-2713b2498c23-stay-on-the-path-instruction-fidelity-in-vision-and-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1633, \"height\": 409, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-005-2713b2498c23-stay-on-the-path-instruction-fidelity-in-vision-and-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 714, \"height\": 318, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-005-2713b2498c23-stay-on-the-path-instruction-fidelity-in-vision-and-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 867, \"height\": 369, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-005-2713b2498c23-stay-on-the-path-instruction-fidelity-in-vision-and-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1609, \"height\": 668, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-005-2713b2498c23-stay-on-the-path-instruction-fidelity-in-vision-and-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1566, \"height\": 659, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-005-2713b2498c23-stay-on-the-path-instruction-fidelity-in-vision-and-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1572, \"height\": 528, \"label\": \"Table\"}]"
motivation: 现有VLN评估指标偏向目标完成，无法反映指令遵循能力，需要更准确的评估方法。
method: 提出CLS指标，结合路径覆盖和长度加权评估指令遵循；通过拼接最短路径构建R4R数据集。
result: 使用CLS和R4R评估表明，奖励指令遵循的代理在指令执行上优于仅关注目标完成的代理。
conclusion: 指令遵循对VLN至关重要，CLS和R4R能更有效地评估代理的语言理解能力。
---

## 摘要
学习与表征的进步重新激发了将语言与其他模态连接的工作。一个特别令人兴奋的方向是视觉与语言导航（VLN），其中智能体解释自然语言指令和视觉场景，以在环境中移动并到达目标。尽管最近取得了进展，但当前研究仍不清楚语言理解在此任务中扮演多大角色，特别是因为主流评估指标侧重于目标完成而非与指令对应的动作序列。在这里，我们强调了Room-to-Room数据集（Anderson等，2018b）当前指标的不足，并提出了一种新指标——长度加权覆盖分数（CLS）。我们还指出，数据集中现有的路径并不理想于评估指令遵循，因为它们是最短直达目标的路径。我们将现有短路径连接起来，形成更具挑战性的扩展路径，从而创建了一个新数据集Room-for-Room（R4R）。利用R4R和CLS，我们证明因指令遵循而获得奖励的智能体优于专注于目标完成的智能体。

## Abstract
Advances in learning and representations have reinvigorated work that connects language to other modalities. A particularly exciting direction is Vision-and-Language Navigation (VLN), in which agents interpret natural language instructions and visual scenes to move through environments and reach goals. Despite recent progress, current research leaves unclear how much of a role language understanding plays in this task, especially because dominant evaluation metrics have focused on goal completion rather than the sequence of actions corresponding to the instructions. Here, we highlight shortcomings of current metrics for the Room-to-Room dataset (Anderson et al., 2018b) and propose a new metric, Coverage weighted by Length Score (CLS). We also show that the existing paths in the dataset are not ideal for evaluating instruction following because they are direct-to-goal shortest paths. We join existing short paths to form more challenging extended paths to create a new data set, Room-for-Room (R4R). Using R4R and CLS, we show that agents that receive rewards for instruction fidelity outperform agents that focus on goal completion.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：现有视觉与语言导航（VLN）任务的主要评估指标（如成功率、SPL）只关注智能体是否到达最终目标位置，忽视了智能体是否遵循自然语言指令给出的完整路径。这使得语言理解在VLN中的实际作用被低估。
- **核心问题**：
  - R2R数据集中的参考路径均为“最短直达目标”路径，导致“完成目标”与“遵循指令路径”高度耦合，无法区分智能体是真的理解指令还是仅仅利用环境漏洞冲向目标。
  - 即使智能体完全忽略指令（如直接走最短路径到目标），在现有指标下仍可获得高分（如SPL完美满分），这削弱了语言通道的作用。
- **整体含义**：为了让语言理解在VLN中发挥应有作用，需要设计能衡量路径遵循度的新指标，并构建包含更长、更多曲折路径的数据集，从而迫使智能体真正依赖语言指令。

## 二、论文提出的方法论
- **核心思想**：用路径覆盖和长度加权来量化智能体轨迹与参考路径的吻合度，同时通过拼接短路径生成更长的、非最短路径的数据集，使指令遵循成为必要条件。
- **关键技术细节**：
  1. **CLS指标**：由路径覆盖（PC）和长度分数（LS）的乘积构成。
     - PC(P, R) = (1/|R|) Σ_r∈R exp(-d(r, P)/d_th)，衡量参考路径每个节点被智能体路径覆盖的程度（指数衰减距离）。
     - LS(P, R) = EPL / (EPL + |EPL - PL(P)|)，其中EPL = PC(P, R) · PL(R)，惩罚路径长度偏离期望最优长度。
     - CLS满足五个期望特性：路径相似性度量、软惩罚、唯一最优解、尺度不变性、计算可行性。
  2. **R4R数据集**：将R2R中终点与另一条路径起点距离小于阈值d_th的两条短路径拼接，形成更长的参考路径，每条拼接路径对应多个人工指令的组合。
  3. **奖励设计**：
     - 目标导向奖励（基线）：每一步奖励接近目标距离减少，最终奖励成功到达。
     - 忠诚度导向奖励：仅在终止时给予成功奖励 + CLS(s1…T, R)分数，鼓励遵循参考路径。
  4. **学习框架**：基于强化学习（REINFORCE），先使用行为克隆（BC）进行策略初始化，再交替进行BC与策略梯度更新，并在训练中逐渐减少BC批次比例。
- **算法流程**：动作选择采用双向LSTM编码语言 + 视觉注意力池化 + 双线性点积预测动作概率；策略梯度使用优势函数和折扣回报。

## 三、实验设计
- **数据集**：
  - R2R（Room-to-Room）：原有数据集，含短的最短路径。
  - R4R（Room-for-Room）：本文构造的扩展数据集，路径更长（平均20.6米 vs 9.9米）、更曲折。
  - 两个验证集：Validation Seen（与训练集环境重叠）、Validation Unseen（全新环境）。
- **Benchmark**：
  - 基线模型：Random（随机游走）、Speaker-Follower（Fried et al., 2018）、RCM（Wang et al., 2019，本文复现）。
  - 对比方法：目标导向奖励（仅优化目标到达）vs. 忠诚度导向奖励（优化目标到达 + CLS）。
- **实验组**：
  - 在R2R和R4R上分别评估PL、NE、SR、SPL、CLS。
  - 消融实验：使用完整指令、仅用最后5个token、不使用指令，观察性能变化。
  - 额外分析：对比不同奖励函数下指令移除对CLS的影响。
- **公平性**：所有模型采用相同的框架、超参数设置，保证对比公平；随机基线基于分布采样，减少偶然性。

## 四、资源与算力
- 论文未明确说明使用的GPU型号、数量及训练时长。
- 作者单位是Google Research，推测使用了内部大规模计算集群，但公开文本中缺少具体算力信息。

## 五、实验数量与充分性
- **实验总数**：在R2R和R4R两个数据集上，共报告了约14行结果（表3、表4），包含多种模型变体和消融。
- **充分性评估**：
  - 消融实验覆盖了指令的完整性（完整、部分、无），有效验证了语言的作用。
  - 对比了多种指标（NE、SR、SPL、CLS），全面展示了不同维度性能。
  - 随机基线提供了下界参考。
  - 缺点是缺乏与更多最新VLN模型（如后续提出的BERT-based模型）的对比，且奖励函数中CLS的权重未进行详细网格搜索。
- **客观性**：通过复现RCM模型并与原论文结果比对，确认了基线的可靠性；随机基线采用大样本（100万条轨迹），统计稳定。

## 六、论文的主要结论与发现
- **CLS比SPL更能反映指令遵循**：在R4R上，目标导向的智能体SPL更高（10.2% vs 7.7%），但CLS更低（20.4% vs 34.6%），说明SPL不能惩罚偏离路径的行为。
- **忠诚度导向奖励大幅提升路径遵循**：在R4R Validation Unseen上，CLS从20.4%提升到34.6%，导航误差NE从8.45m降至8.08m。
- **语言指令的作用可被量化**：当仅提供最后5个token时，目标导向智能体CLS不变（20.4%），而忠诚度导向智能体CLS从34.6%下降到25.3%，表明前者根本不依赖语言，后者更依赖完整指令。
- **R2R数据集低估语言理解的重要性**：在R2R上两种奖励的CLS相近（61.1% vs 60.2%），说明短的最短路径使智能体无需真正理解指令。
- **未来空间大**：最佳模型在R4R上CLS仅34.6%，NE为8.08m，远高于人类水平（R2R NE 1.61m），说明还有很大提升空间。

## 七、优点
- **指标创新**：CLS首次将路径覆盖和长度加权结合，满足五个期望特性，简单可计算，且可分解PC和LS便于后续改进。
- **数据集构建巧妙**：利用已有R2R路径拼接，无需额外人工标注，自动生成大量长路径，成本低且可扩展。
- **实验设计严谨**：通过指令消融实验直接证明指令依赖程度，区分了“到达目标”和“遵循路径”两种能力。
- **开源代码**：提供R2R-to-R4R转换代码，促进可复现研究。
- **动机清晰**：明确指出现有评估的偏差，并提出实际解决方案，对后续VLN研究有重要指导意义。

## 八、不足与局限
- **R4R路径拼接的局限性**：拼接路径时可能引入不自然的转折（连接处最短路径段C），指令组合是直接拼接，可能缺乏连贯性。
- **CLS依赖预计算距离矩阵**：计算d(r, P)需要图中所有节点对的最短距离，在大规模环境中可能成为瓶颈（O(EV+V²logV)）。
- **实验对比不够全面**：仅对比了RCM和Speaker-Follower，未与更先进的预训练模型（如VLN-BERT、PREVALENT）对比，挑战性尚显不足。
- **奖励设计偏向稀疏**：忠诚度奖励仅在终止时给出，可能导致学习效率低；虽然提及可以加入塑造项，但未实验验证。
- **未进行超参数敏感性分析**：d_th（CLS中的衰减常数）和拼接阈值d_th的选择可能影响结果，但未深入探讨。
- **应用局限性**：所有实验均在模拟环境中进行（Matterport3D），未验证真实机器人场景下的泛化性。
- **忽略视觉特征的影响**：消融仅针对语言，未分析不同视觉编码器或特征提取方式对CLS的影响。

（完）
