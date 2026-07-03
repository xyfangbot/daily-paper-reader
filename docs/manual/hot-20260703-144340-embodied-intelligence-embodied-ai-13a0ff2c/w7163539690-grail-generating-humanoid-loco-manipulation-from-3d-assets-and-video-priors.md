---
title: "GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors"
title_zh: GRAIL：从3D资产和视频先验生成人形全身操作
authors: "Tianyi Xie, Haotian Zhang, Jinhyung Park, Zi Wang, Bowen Wen, Jiefeng Li, Xueting Li, Qingwei Ben, Haoyang Weng, Yufei Ye, David Minor, Tingwu Wang, Chenfanfu Jiang, Sanja Fidler, Jan Kautz, Linxi Fan, Yuke Zhu, Zhengyi Luo, Umar Iqbal, Ye Yuan"
date: 2026-06-03
pdf: "https://doi.org/10.48550/arxiv.2606.05160"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:unitree"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=unitree; relation_source=abstract; query=humanoid robot policy"
tldr: "人形机器人全身操控和移动数据难以通过遥操作或动捕规模化扩展，GRAIL提出全虚拟数据生成流水线，组合3D资产与视频基础模型先验，在完全指定的3D配置下合成人-物交互视频，利用已知几何和度量信息恢复精确4D轨迹，重定向至机器人并训练物体/场景感知追踪器。仅使用生成数据训练的视觉策略在Unitree G1上实现拾取84%和爬楼梯90%真实成功率，证明虚拟生成可替代物理采集。"
source: openalex
selection_source: hot_paper_scout
motivation: 解决物理遥操作和动捕难以规模化的问题，无需重建环境或操作机器人即可获得多样演示。
method: 从已知3D配置生成视频，通过模型追踪、人体估计和交互优化重建度量4D轨迹，重定向后训练物体感知适配器和场景感知跟踪器。
result: "生成超20,000序列，真实世界拾取成功率84%，爬楼梯成功率90%。"
conclusion: 全虚拟数据生成能有效训练人形机器人复杂操控与移动策略，实现高效sim-to-real迁移。
---

## 摘要
扩展人形全身操作需要跨越不同物体、全身动作和场景几何的机器人兼容演示，但远程操作和动作捕捉难以规模化，因为每次采集都依赖于物理设置、穿戴传感器的演员和机器人操作。我们提出GRAIL，一个在部署前完全保持虚拟的数字生成流水线：它组合3D资产、模拟器就绪场景以及来自视频基础模型（VFM）的先验，无需重建物理环境或远程操作机器人即可合成交互。与重建无约束的野外视频不同，GRAIL从完全指定的3D配置开始，其中物体几何、相机参数、公制尺度、环境深度以及一个按机器人比例缩放的角色在视频生成前已知，并在重建过程中复用。这种特权设置更好地规范了4D恢复，使得基于模型的物体跟踪、人体运动估计和交互感知优化能够重建公制4D人-物交互（HOI）轨迹，减少了深度模糊和形态不匹配。我们将恢复的运动重定向到人形机器人，并训练互补的任务通用跟踪器：一个用于操作的物体感知潜在适配器和一个用于地形穿越的场景感知跟踪器。GRAIL生成了超过20,000个序列，涵盖抓取、物体操作、坐下和地形穿越。仅使用GRAIL生成的数据，我们通过从仿真到现实的流水线训练自我中心视觉策略，并将其部署在Unitree G1人形机器人上，在多种物体抓取上实现了84%的真实世界成功率，在爬楼梯上实现了90%的成功率。

## Abstract
Scaling humanoid loco-manipulation requires robot-compatible demonstrations across diverse objects, whole-body motions, and scene geometries, but teleoperation and motion capture are difficult to scale because each collection depends on physical setups, instrumented actors, and robot operation. We present GRAIL, a digital generation pipeline that remains fully virtual until deployment: it composes 3D assets, simulator-ready scenes, and priors from video foundation models (VFMs) to synthesize interactions without rebuilding physical environments or teleoperating the robot. Rather than reconstructing unconstrained in-the-wild videos, GRAIL starts from fully specified 3D configurations in which object geometry, camera parameters, metric scale, environment depth, and a robot-proportioned character are known before video generation and reused during reconstruction. This privileged setup better conditions 4D recovery, allowing model-based object tracking, human motion estimation, and interaction-aware optimization to reconstruct metric 4D human-object interaction (HOI) trajectories with reduced depth ambiguity and morphology mismatch. We retarget the recovered motions to a humanoid robot and train complementary task-general trackers: an object-aware latent adaptor for manipulation and a scene-aware tracker for terrain traversal. GRAIL produces over 20,000 sequences spanning pick-up, object manipulation, sitting, and terrain traversal. Using only GRAIL-generated data, we train egocentric visual policies through a sim-to-real pipeline and deploy them on a Unitree G1 humanoid, achieving 84\% real-world success on diverse object pick-up and 90\% success on stair-climbing.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 核心问题：人形机器人全身操控（loco-manipulation）需要大量机器人兼容的演示数据，涵盖多样物体、全身动作和场景几何；但遥操作和动作捕捉方法受限于物理设置、穿戴传感器的演员和专用机器人操作，难以规模化扩展。
- 研究背景：现有数据生成方法依赖物理环境重建或野外视频重建，存在深度模糊、形态不匹配、可扩展性差等问题；视频基础模型虽能生成高质量视频，但缺乏与机器人形态和仿真环境的精确对齐。
- 整体含义：GRAIL提出一种全虚拟数据生成流水线，在部署前保持完全虚拟，组合3D资产、仿真就绪场景和视频基础模型先验，合成人-物交互视频并恢复精准的度量4D轨迹，从而替代物理采集，为人形机器人视觉策略训练提供大规模、多样化演示数据。

## 二、论文提出的方法论
- 核心思想：从完全指定的3D配置出发（已知物体几何、相机参数、公制尺度、环境深度、按机器人比例缩放的角色），利用视频基础模型生成交互视频，再通过模型追踪和优化恢复度量4D人-物交互（HOI）轨迹；最后将人体运动重定向至人形机器人，并训练任务通用的物体感知和场景感知跟踪器。
- 关键技术细节：
  - 3D配置生成：组合已有3D资产（如物体、场景、角色），配置相机参数、光照和动画路径，生成完全已知的虚拟场景。
  - 视频生成：利用视频基础模型根据3D配置渲染出的初始帧和条件，生成后续视频帧，保持视觉一致性。
  - 4D轨迹重建：采用基于模型的方法进行物体跟踪（已知几何）和人体运动估计（机器人比例角色），结合交互感知优化减少深度模糊和形态不匹配，恢复公制尺度的HOI轨迹。
  - 运动重定向：将重建的人体运动重定向至Unitree G1人形机器人，适配机器人的动力学约束。
  - 跟踪器训练：训练物体感知潜在适配器（object-aware latent adaptor）用于操作任务，场景感知跟踪器（scene-aware tracker）用于地形穿越（如爬楼梯），两者均为任务通用型。
- 算法流程（文字说明）：(1) 组合3D资产和仿真场景；(2) 配置已知参数生成初始帧；(3) 使用VFM生成视频；(4) 基于已知3D配置进行物体追踪和人体运动估计；(5) 交互感知优化重建度量4D轨迹；(6) 重定向至机器人；(7) 训练视觉策略和跟踪器；(8) 部署至真实机器人。

## 三、实验设计
- 数据集/场景：GRAIL自身生成了超过20,000个序列，涵盖拾取、物体操作、坐下、地形穿越（如爬楼梯）等任务；场景使用多种3D资产组合，包括常见家居物体、家具和楼梯环境。
- Benchmark：没有使用公开标准benchmark，而是自行构建真实世界测试任务：不同物体拾取（diverse object pick-up）和爬楼梯（stair-climbing）。
- 对比方法：摘要未明确列出对比基线（如不使用GRAIL生成数据的空白对比或传统遥操作数据的效果），主要强调仅使用GRAIL生成数据训练的视觉策略在真实机器人上的成功率，但缺乏与其他数据生成方法的直接对比。

## 四、资源与算力
- 文中未明确说明使用的GPU型号、数量、训练时长等算力信息。
- 可推断：涉及视频基础模型推理、4D轨迹优化、策略训练等环节，通常需要高端GPU（如NVIDIA A100或类似），但具体配置和总计算成本未报告。

## 五、实验数量与充分性
- 实验数量：主要报告两个真实世界任务的成功率（物体拾取84%，爬楼梯90%）；数据生成规模为20,000+序列；未提及多项消融实验或不同配置的对比实验。
- 充分性与客观性：实验覆盖了两种典型的全身操作任务（操作和移动），数据量较大；但缺乏消融研究（如是否依赖于VFM质量、不同3D配置的影响、跟踪器设计的必要性等）、对比基线（与真实遥操作数据采集的效果对比）以及更大场景多样性的测试。因此实验设计偏少，充分性有限，但结果初步验证了全虚拟数据生成的有效性。

## 六、论文的主要结论与发现
- 全虚拟数据生成流水线GRAIL能有效替代物理采集，产生高质量的人-物交互演示数据。
- 利用完全指定的3D配置作为先验，可显著减小4D重建中的深度模糊和形态不匹配问题。
- 仅使用生成数据训练的自我中心视觉策略，在Unitree G1人形机器人上实现了有竞争力的真实世界成功率：多样物体拾取84%，爬楼梯90%。
- 结论：虚拟生成数据具备足够的真实性和多样性，可以成功实现从仿真到现实的迁移，为人形机器人全身操作策略训练提供可扩展方案。

## 七、优点
- 方法创新：全虚拟生成流水线避免了物理数据采集的瓶颈，无需重建环境或操作机器人，可无限扩展数据多样性。
- 技术亮点：利用已知3D配置作为特权信息，引导视频生成和4D重建，降低了深度估计和人体重建的不确定性；设计了任务通用的物体感知和场景感知跟踪器，增强策略的泛化性。
- 实验验证：在真实人形机器人上取得了高成功率，证明了sim-to-real迁移的有效性，且数据表明虚拟生成策略可与真实数据媲美。
- 开源倾向：提供项目页面和论文，可能开源代码或数据集，有利于社区复现和后续研究。

## 八、不足与局限
- 实验覆盖不足：仅测试了拾取和爬楼梯两个任务，未涉及更复杂的全身操作（如搬运重物、开门、多对象交互等），泛化能力有待验证。
- 缺乏对比基准：未与使用真实遥操作数据或其他数据生成方法训练的策略进行公平对比，难以量化GRAIL数据的相对优势。
- 依赖3D资产库：视频生成和4D恢复依赖预定义的3D资产，若资产库涵盖不全，生成内容可能受限，且与真实场景的视觉分布可能存在差距。
- 消融实验缺失：未系统分析各组件（如已知3D配置的重要程度、VFM选择、优化算法等）对最终性能的贡献。
- 算力成本未报告：难以评估该方法在资源消耗上的实际可用性，可能对计算资源要求较高。
- 应用限制：方法针对Unitree G1人形机器人，重定向和跟踪器设计可能不直接适配其他形态的机器人；真实世界成功率为统计结果，未报告失败案例的详细原因分析。

（完）
