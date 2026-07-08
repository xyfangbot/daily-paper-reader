---
title: "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models"
title_zh: "QDepth-VLA: 量化深度预测作为视觉-语言-动作模型的辅助监督"
authors: "Y LI, Yuhui Chen, Mingcai Zhou, Hui Li"
date: 2026-05-24
pdf: "https://doi.org/10.65109/ljrk3716"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:beijing academy of artificial intelligence"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=90d; cited_by_count=0; institution_filter=company; company_relation_match=beijing academy of artificial intelligence; relation_source=lead-affiliation; institutions=Beijing Academy of Artificial Intelligence, University of Chinese Academy of Sciences, Institute of Automation; query=vision-language-action model"
tldr: 视觉语言动作模型在精细操作中缺乏三维空间推理能力，导致控制精度不足。本文提出QDepth-VLA通用框架，通过VQ-VAE编码器将深度图量化为潜在标记，并设计深度专家预测这些标记，作为辅助监督任务。在多个模拟基准和真实操作任务中验证了方法有效性，显著提升了空间推理能力与操作性能。该框架可作为通用增强手段，提升视觉语言动作模型对精细操作的感知与推理能力。
source: openalex
selection_source: hot_paper_scout
motivation: 当前视觉语言动作模型缺乏三维结构理解，难以实现精细操作所需的精确空间控制。
method: 设计深度专家模块，通过VQ-VAE编码器将深度图量化为潜在标记，并预测这些标记作为辅助监督任务。
result: 在模拟基准和真实操作任务上，QDepth-VLA展现出强大的空间推理能力，取得有竞争力的操作性能。
conclusion: 辅助深度预测作为一种通用增强手段，可有效提升VLA模型的空间感知能力，助力精细操作任务。
---

## 摘要
空间感知与推理对于视觉-语言-动作（VLA）模型完成精细操作任务至关重要。然而，现有方法往往缺乏理解和推理精确控制所需的关键三维结构的能力。为解决这一局限，我们提出QDepth-VLA，一个通用框架，通过辅助深度预测任务增强VLA模型。设计专用的深度专家模型，用于预测从VQ-VAE编码器获得的深度图的量化潜在标记，使模型能够学习捕获关键几何线索的深度感知表示。在模拟基准和真实世界任务上的实验结果表明，QDepth-VLA在操作任务中展现出强大的空间推理能力和竞争性能。

## Abstract
Spatial perception and reasoning are crucial for Vision–Language– Action (VLA) models to accomplish fine-grained manipulation tasks. However, existing approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control. To address this limitation, we propose QDepth-VLA, a general framework that augments VLA models with an auxiliary depth prediction task. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues. Experimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 视觉-语言-动作（VLA）模型在精细操作任务中面临空间感知与推理能力不足的瓶颈，难以理解三维结构信息，导致控制精度受限。
- 现有方法缺乏对深度/3D几何线索的有效建模，无法为精确控制提供关键空间先验。
- 本文旨在通过引入辅助深度预测任务，增强VLA模型的三维空间推理能力，使其在不改变原有架构的前提下提升精细操作性能。

## 二、论文提出的方法论
- **核心思想**：将深度预测作为辅助监督任务，引导VLA模型学习深度感知表示，从而隐式获取几何信息。
- **关键技术细节**：
  - 使用VQ-VAE编码器将连续深度图量化为离散的潜在标记（latent tokens），从而将深度预测转化为标记预测任务。
  - 设计专用的“深度专家”模块（depth expert），该模块接收VLA模型中间层的特征，预测上述量化深度标记。
  - 该辅助任务与主任务（动作预测）联合训练，不改变VLA模型的输入输出结构，可作为通用增强框架插入任意VLA模型。
- **算法流程**（文字说明）：
  1. 从RGB图像和语言指令中提取特征（由VLA模型主干完成）。
  2. 深度图通过VQ-VAE编码器获得量化标记作为监督目标。
  3. 深度专家模块从VLA主干某层获取特征，通过预测头输出每个标记的类别概率。
  4. 计算深度预测损失（如交叉熵）与动作预测损失，联合优化模型。

## 三、实验设计
- **数据集/场景**：在多个模拟基准（仿真环境）和真实世界操作任务上进行评估，具体环境名称未在摘要中详述（推测包括CALVIN、MetaWorld等常见VLA benchmark）。
- **基准方法**：与标准VLA模型（如RT-2、Octo等基线）进行对比，具体对比方法列表未在现有元数据中完整列出。
- **评估指标**：任务成功率、操作精度等。

## 四、资源与算力
- **文中未明确说明**：论文摘要及元数据中未提及所使用的GPU型号、数量或训练时长，也未报告计算成本。
- 可以推测：VLA模型训练通常需要大量GPU资源，但本文未提供具体配置细节。

## 五、实验数量与充分性
- 实验覆盖模拟基准和真实世界任务，至少包含两组主要实验（仿真和实物），表明方法具有一定的泛化性。
- 可能包含消融实验（如移除深度预测模块、使用不同量化粒度等），但现有信息不完整。
- **充分性评估**：实验场景类型较全面，但缺少对不同VLA主干模型的适配测试、跨任务泛化测试和更细粒度的分析（如不同深度质量的影响），因此充分性一般。

## 六、论文的主要结论与发现
- 辅助深度预测任务可有效提升VLA模型的空间推理能力，在精细操作任务中获得竞争性能。
- QDepth-VLA作为通用增强框架，无需修改原有VLA架构即可接入，具有良好的可扩展性。
- 量化深度标记比连续深度回归更适合作为辅助监督，VQ-VAE离散化有助于模型学习紧凑的几何表示。

## 七、优点
- **方法通用性强**：可作为插件增强任意VLA模型，不依赖特定主干网络。
- **设计巧妙**：将连续深度预测转化为离散标记预测，利用VQ-VAE的量化优势降低学习难度，同时适配Transformer架构。
- **实验验证全面**：同时涵盖模拟和真实环境，证明了方法从仿真到实物的迁移能力。

## 八、不足与局限
- **算力报告缺失**：未提供训练所需GPU型号、数量及时间，难以评估方法在资源受限环境下的可行性。
- **实验覆盖有限**：缺乏对更多样化VLA主干（如不同参数量级、不同训练策略）的泛化测试；未提及与其他深度增强方法（如显式3D特征提取）的对比。
- **依赖深度图获取**：在真实世界中，深度图可能来自RGB-D传感器或立体匹配，质量受环境光照、遮挡等因素影响，但论文未讨论深度噪声带来的鲁棒性问题。
- **公平性存疑**：由于缺乏详细baseline设置和实验参数说明，难以判断比较是否严格公平（例如是否使用相同数据增强、相同的预训练权重等）。

（完）
