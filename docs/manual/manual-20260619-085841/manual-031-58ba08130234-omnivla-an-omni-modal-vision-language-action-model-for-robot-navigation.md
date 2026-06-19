---
title: "OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation"
title_zh: OmniVLA：用于机器人导航的全模态视觉-语言-动作模型
authors: "Noriaki Hirose, Catherine Glossop, Dhruv Shah, Sergey Levine"
date: 2026-06-19
pdf: assets/manual-pdfs/manual-20260619-085841/031-2025_hirose_omnivla-4378c132-58ba08130234.pdf
tags: ["query:手动上传", "paper:PDF", "query:Omni-modal", "query:Vision-Language-Action", "query:Navigation", "query:Robot Foundation Model", "query:Goal Conditioning"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有机器人导航策略多基于单模态目标，难以适应现实世界中语言、坐标、视觉等多种指令的灵活组合。本文提出OmniVLA，采用高容量视觉-语言-动作骨干，通过随机模态融合策略同时学习2D位姿、自我图像和自然语言三种目标模态及其组合。模型在未见环境、稀缺模态和新颖语言指令上均展现出强泛化能力，性能超越各模态专家模型，为构建可扩展的全模态机器人基础模型提供了新路径。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1824, \"height\": 353, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 893, \"height\": 503, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 889, \"height\": 249, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 610, \"height\": 239, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1180, \"height\": 241, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 738, \"height\": 227, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 895, \"height\": 424, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1804, \"height\": 258, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 894, \"height\": 420, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 896, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 522, \"height\": 239, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 526, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260619-085841-manual-031-58ba08130234-omnivla-an-omni-modal-vision-language-action-model-for-robot-navigation/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 895, \"height\": 241, \"label\": \"Table\"}]"
motivation: 现有导航策略仅支持单模态目标，无法像人类一样灵活组合语言、坐标、视觉等自然表达，限制了现实适应性。
method: 基于VLA骨干，采用随机模态融合策略，联合训练2D位姿、自我图像和自然语言三种目标模态及其组合。
result: OmniVLA在未知环境、稀缺模态和新颖语言指令上表现优异，性能超越各单模态专家模型。
conclusion: 提供了一种可微调至新任务和模态的全模态导航基础模型，为机器人基础模型的规模化发展奠定了基础。
---

## 摘要
人类在导航至目的地时，能够灵活地解读和组合不同的目标规范，例如语言指令、空间坐标或视觉参考。相比之下，大多数现有的机器人导航策略仅在单一模态上训练，限制了它们在现实世界场景中的适应性，而在这些场景中不同形式的目标规范既自然又互补。本文提出了一种用于机器人基础模型的训练框架，能够为基于视觉的导航实现全模态目标条件设定。我们的方法利用高容量的视觉-语言-动作（VLA）骨干网络，通过随机模态融合策略，采用三种主要目标模态进行训练：2D姿态、自我中心图像和自然语言，以及它们的组合。这一设计不仅扩展了可用数据集的池子，还鼓励策略发展更丰富的几何、语义和视觉表征。得到的模型OmniVLA在未见环境中展现出强大的泛化能力，对稀缺模态的鲁棒性，以及遵循新颖自然语言指令的能力。我们证明OmniVLA在多种模态上优于专家基线模型，并为微调至新模态和新任务提供了灵活的基础。我们相信OmniVLA为广泛泛化和灵活的导航策略迈出了一步，并为构建全模态机器人基础模型提供了一条可扩展的路径。

## Abstract
Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination. In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and complementary. In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation. Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as their combinations, through a randomized modality fusion strategy. This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations. The resulting model, OmniVLA, achieves strong generalization to unseen environments, robustness to scarce modalities, and the ability to follow novel natural language instructions. We demonstrate that OmniVLA outperforms specialist baselines across modalities and offers a flexible foundation for fine-tuning to new modalities and tasks. We believe OmniVLA provides a step toward broadly generalizable and flexible navigation policies, and a scalable path for building omni-modal robotic foundation models.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有机器人导航策略通常仅支持单一模态的目标规范（如仅有语言、2D位姿或自我图像），无法像人类一样灵活组合多种信息（如同时使用GPS坐标、地标图像和语言指令）。这限制了机器人在真实复杂场景中的适应性，因为不同任务和环境需要不同的目标表达方式。
- **研究动机**：人类导航时天然会融合视觉、空间和语义信息，而机器人缺乏这种跨模态理解能力。作者希望通过训练一个全模态（omni-modal）的导航策略，使其能够同时处理语言、2D位姿和自我图像三种目标模态及其任意组合，从而提升泛化能力、鲁棒性和用户友好性。
- **整体含义**：这项工作旨在构建一个通用导航基础模型，能够利用来自多个数据源的大规模多模态数据，学习到丰富的几何、语义和视觉表征，从而在未见环境、稀缺模态和新颖语言指令上实现强泛化，并为后续微调至新任务和新模态提供基础。

## 二、论文提出的方法论
- **核心思想**：基于高容量视觉-语言-动作（VLA）骨干网络（OpenVLA-7B），通过随机模态融合策略联合训练三种目标模态（2D位姿、自我图像、自然语言）及其组合，使模型学习跨模态表征。
- **关键技术细节**：
  1. **架构设计**：在OpenVLA基础上修改，添加视觉编码器（DINOv2+SigLIP）处理当前图像，并为每种目标模态（2D位姿投影器、目标图像编码器、语言令牌）添加投影层，将各模态映射到共享令牌空间，输入LLM骨干（Llama 2 7B）。动作头输出N步动作序列。
  2. **模态丢失（Modality Dropout）**：训练时随机选择可用模态的子集作为条件输入，并构建注意力掩码屏蔽未使用或不可用的模态令牌。这使模型学会在不同模态组合下推理，提高对缺失模态的鲁棒性。
  3. **训练数据混合**：整合13个公开数据集，涵盖10种不同机器人平台，总时长约9500小时。包括GNM混合物、LeLaN混合物、Frodobots-2K和BDD-V。对部分数据使用合成动作标签（如MBRA重注释、NoMaD生成）。
  4. **训练目标**：采用模仿学习损失 `J_il = (1/N)Σ(a_ref - a_hat)^2`，对LeLaN数据额外增加目标接近损失 `J_obj` 和动作平滑正则 `J_sm`。
  5. **LoRA微调**：对OpenVLA基座使用LoRA（仅训练5%参数）以平衡模型大小和训练稳定性。
  6. **轻量版OmniVLA-edge**：基于ViNT（50M参数）构建，使用EfficientNet-B0、ResNet、CLIP等，采用早期融合策略。
- **算法流程**：每步训练从混合数据集中批量采样，按比例（LeLaN:GNM:Frodobots:BDD-V=4:1:1:1）选取样本。对每个样本随机选择可用模态子集，构造输入和注意力掩码，前向传播计算损失并更新可训练参数（LLM骨干及投影层）。

## 三、实验设计
- **数据集与环境**：
  - 训练数据：GNM混合（62小时）、LeLaN混合（128.7小时）、Frodobots-2K（700小时）、BDD-V（8680小时），总计约9500小时，10种平台（轮式、四足、汽车等）。
  - 评测环境：办公室、厨房、入口大厅、公园、人行道等多种室内外场景，共40余种，部分设置障碍物。
- **评测任务**：
  1. 语言条件导航（含OOD语言指令）
  2. 自我图像条件导航（使用拓扑记忆方法）
  3. 2D位姿条件导航（GPS定位，目标距离25-100米）
  4. 多模态组合导航（同时提供位姿和语言指令）
  5. 新模态适应（卫星图像条件导航）
- **对比基线**：包括7种方法：CoW（CLIP+OWL-ViT）、LeLaN、CounterfactualVLA、MBRA-pose/Image、NoMaD、ViNT、以及将OmniVLA配方应用于SmolVLA和MiniVLA的版本。
- **评估指标**：成功率（SR）、部分进展（Prog.）、语言行为遵循率（Behavior）、简单/复杂场景下成功率（SRS/SRC）。

## 四、资源与算力
- **训练硬件**：使用8块H100 GPU训练OmniVLA（7B模型）。每GPU批大小7，梯度累积4步，有效批大小224。
- **LoRA**：仅5%参数可训练，以最大化批大小和稳定训练。
- **其他模型**：OmniVLA-edge（50M）和SmolVLA/MiniVLA变体在相似设置下训练，但具体GPU细节未详细给出。
- **训练时长**：论文未明确给出总训练时间，但指出利用大规模数据集（9500小时）进行训练。

## 五、实验数量与充分性
- **实验数量**：
  - 单模态对比实验（表II）：涵盖语言、2D位姿、图像三种条件，分别报告SR、Prog.、Behavior等指标。
  - 消融实验（表III）：在OmniVLA-edge上比较单模态训练 vs 全模态训练，并评估卫星图像新模态适配（0.57→0.83）。
  - 多模态组合实验（表IV）：10种环境下同时使用2D位姿和OOD语言指令。
  - 微调实验（表V）：使用1.2小时新环境下数据微调后评估。
  - 跨本体实验：在VizBot、Unitree Go1上测试语言导航。
- **充分性与公平性**：
  - 对比基线使用作者原始代码和检查点，确保公平。
  - 实验覆盖室内外、有无障碍物、不同距离、不同语言指令风格（ID和OOD）。
  - 但未报告所有基线的完整变体（如CoW需要深度估计，增加了不公平因素）。
  - 消融实验主要在OmniVLA-edge上运行，未在7B模型上做完整消融（可能限于计算资源）。
  - 总体实验设计较为全面，但语言导航的OOD难度控制可能不够系统（仅给出定性示例）。

## 六、论文的主要结论与发现
1. **全模态训练优于单模态**：OmniVLA在所有三种模态上均超过各自专家基线（表II），如在语言任务上SR=0.73 vs LeLaN的0.43；在2D位姿任务上SR=0.95 vs MBRA-pose的0.86。
2. **多模态融合带来更强泛化**：OmniVLA能够同时跟随位姿和语言指令（表IV），SR=0.80，而单模态基线无法处理组合。
3. **大模型容量重要**：OmniVLA（7B）显著优于SmolVLA（500M）和MiniVLA（1B），尤其在语言理解和跟随上差距巨大。
4. **可高效适配新模态和新环境**：仅用1.2小时新数据微调即可将卫星图像导航成功率从0.57提升至0.83；利用CounterfactualVLA数据微调后语言行为提升。
5. **跨本体泛化**：在VizBot和Go1上零样本部署成功。

## 七、优点
- **方法创新性**：首次在导航领域实现端到端全模态VLA，统一处理语言、图像和位姿三种目标规范及其组合。
- **数据规模与多样性**：整合超过9500小时、10种平台的数据，是已知最大的导航策略预训练数据集，覆盖丰富场景。
- **稳健的模态丢失机制**：通过随机模态丢失和注意力掩码，有效应对训练数据中模态不平衡和缺失问题，提升策略鲁棒性。
- **高效的微调能力**：LoRA仅训练5%参数即可达到高性能，且在新模态、新环境、新语言领域上微调迅速。
- **全面的实验评估**：覆盖多种模态、组合情况、跨本体、新模态适应、微调效果等，与多个强基线对比，结果具有说服力。
- **开源承诺**：将释放模型权重和训练代码，促进社区研究。

## 八、不足与局限
- **语言导航的局限性**：训练数据中的语言提示主要为“move toward X”类型，OOD评测中行为遵循任务设计较简单，且模型在复杂多步指令（如NaVILA所需）上完全失败（得分为0）。更系统的OOD评测和更多样化的语言数据仍是改进方向。
- **图像条件导航依赖拓扑记忆**：超越近距离（>3米）时需要外部拓扑图，限制了纯端到端的便利性。
- **实验覆盖的偏差风险**：主要在Frodobots ERZ平台上测试跨本体，其他平台仅做定性演示；未在更多不同尺寸/重量的机器人上定量评估。
- **消融实验的粒度不足**：主要消融在OmniVLA-edge（50M）上完成，7B模型的消融（如不同模态组合、不同训练数据比例）未充分展开，可能受限于计算成本。
- **BDD-V数据集的处理**：使用自定义MBRA模型生成动作，存在近似误差，且高速车辆数据与低速机器人差距大，可能带来迁移噪声。
- **实时性限制**：7B模型推理需要高端GPU（如RTX 4090），难以在低成本机器人上部署；轻量版OmniVLA-edge性能仍有明显差距（尤其在语言任务上）。

（完）
