---
title: Automatic personalized limbed robot design from media inputs
title_zh: 基于媒体输入的自动个性化有肢机器人设计
authors: "Gang Chen, Moji Shi, Yu Xing, Marija Popović, Javier Alonso-Mora, Lei Zhang, Jiangmiao Pang"
date: 2026-06-09
pdf: "https://www.nature.com/articles/s44182-026-00101-3_reference.pdf"
tags: ["query:热点论文筛选", "query:机构产出", "query:科技公司/研究机构产出", "paper:OpenAlex", "company:shanghai artificial intelligence laboratory"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=shanghai artificial intelligence laboratory; relation_source=lead-affiliation; institutions=Shanghai Artificial Intelligence Laboratory, Delft University of Technology; query=robot"
tldr: 腿式机器人设计通常需要专业工程师投入大量精力。本文提出基于分解-优化-组装(DOA)的自动框架，结合生成式AI和3D打印，让非专家从文本或图像等媒体输入在几分钟到几小时内获得个性化设计。输出包含选定电机和可打印机械部件，通过求解执行器、几何与结构密度优化问题处理设计空间与制造细节。实验以图像输入生成了Centaur机器人，并展示了多种腿式机器人设计，降低了设计门槛。
source: openalex
selection_source: hot_paper_scout
motivation: 现有腿式机器人设计依赖专家经验且耗时长，缺乏让非专家快速参与的方法。
method: 提出了DOA框架，将设计分解为执行器、几何和结构密度联合优化问题，并集成生成式AI与3D打印。
result: 基于图像输入成功设计并制造了Centaur机器人，同时生成了多种不同形态的腿式机器人设计。
conclusion: 该框架使非专家能快速从媒体输入获得可制造的个性化腿式机器人，简化了传统设计流程。
---

## 摘要
设计有肢机器人是一项复杂的多学科任务，通常需要经验丰富的工程师投入大量精力。本文提出了一种基于分解-优化-组装（DOA）的新型自动机器人设计框架来应对这一挑战。我们的框架使非专业人士能够在几分钟到几小时内，根据文本和图像等媒体输入创建个性化的有肢机器人设计。该系统利用生成式AI和3D打印的最新进展，生成与输入媒体描述相匹配的设计。输出包括选定的电机和可3D打印的机械部件，这些部件可组装成一个有肢机器人。为了处理庞大的设计空间以及制造和装配中的复杂细节，我们制定并解决了一系列涉及执行器、几何形状和结构密度的优化问题。我们通过基于图像输入设计和制造一个半人马机器人来验证所提出的系统。此外，我们通过生成多种多样的有肢机器人设计来展示该系统的通用性和有效性。

## Abstract
Designing limbed robots is a complex, multidisciplinary task that typically requires substantial effort from experienced engineers. In this paper, we present a novel automatic robot design framework based on Decomposition-Optimization-Assembling (DOA) to address this challenge. Our framework enables non-experts to create personalized limbed robot designs from media inputs, such as text and images, within minutes to a few hours. Our system leverages recent advances in generative AI and 3D printing to produce designs that match the descriptions provided in the input media. The output consists of selected motors and 3D-printable mechanical components that can be assembled into a limbed robot. To handle the large design space and intricate details in fabrication and assembly, we formulate and solve a series of optimization problems involving actuators, geometry, and structural density. We validate the proposed system by designing and fabricating a Centaur robot based on an image input. Furthermore, we demonstrate the system’s versatility and effectiveness through the generation of a wide variety of limbed robot designs.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 有肢机器人（如四足、人形）设计是复杂、耗时的多学科任务，通常需要机械、电气、工业设计等领域的专业工程师投入大量精力。
- 现有自动设计方法存在两大局限：一是设计空间受限，仅优化少数参数或使用预定义模块；二是忽略制造和装配细节，难以直接输出可制造机器人。
- 生成式AI（文本/图像→3D模型）的发展使非专家能获得高质量3D模型，但如何将其转化为功能机器人仍待解决。
- 论文旨在实现“从媒体输入（文本/图像）自动生成可制造的有肢机器人”，让非专家在分钟到小时级别内获得个性化设计，降低门槛。

## 二、论文提出的方法论
- **核心思想**：提出“分解-优化-组装”（Decomposition-Optimization-Assembling, DOA）框架，将设计过程分为三个自动阶段，集成生成式AI与3D打印。
- **技术流程**：
  1. **预处理**：通过文本/图像到3D模型生成工具（如Meshy）得到初始网格，并用姿态估计模型（如Bite）或用户界面设定初始关节配置（位置、自由度、运动轴，均为旋转关节）。
  2. **网格分解**：将初始网格体素化后，根据关节位置和特征点，将体素分配到各个连杆（如大腿、小腿、身体），获得体素地图。
  3. **执行器优化**：针对每个自由度选择电机（种类、位置、方向），建立混合整数非线性优化问题，目标函数包含运动学对齐成本、网格覆盖成本，约束包含扭矩约束和干涉约束。使用遗传算法求解。
  4. **几何优化**：分为三个子步骤——网格扩展（为电机添加安装壳）、关键体素搜索（用A*算法确保电机壳与连杆连接）、运动干涉移除（采样关节角度，删除碰撞的可移除体素）。最后用Marching Cubes重建网格。
  5. **密度优化**：对每个连杆填充六折板晶格超材料，优化相对密度以最小化重量，同时满足冯·米塞斯应力约束（通过有限元分析FEA自动计算）。使用梯度下降搜索求解。
  6. **装配细节处理**：设计燕尾榫连接件连接电机与连杆，搜索最佳榫槽方向避免干涉，必要时使用布尔运算去除干涉。
- **关键公式/算法**：
  - 执行器优化：目标函数 min Σ( w1||p-p̂||² + w2(1 - |n·n̂|/(||n||·||n̂||)) + w3 Σ min(SDF(s_l),0) )，约束为扭矩和干涉不等式。
  - 密度优化：min ||ρ||²，约束为σ_vm(ρ) ≤ σ_vm_max(ρ)，ρ∈(0,1]。

## 三、实验设计
- **数据集**：
  - **定量实验**：从Stanford Dogs数据集随机选取100张图像作为输入，使用Bite模型生成初始网格和关节（标准12自由度四足配置），归一化宽度至20 cm，体素大小1 cm。
  - **定性实验**：多种输入模态（文本、图像、3D模型），包括游戏角色“Lynel”等，体素大小0.5 cm。
- **评估指标**：
  - 有条件成功率（自动评估：所有连杆能否分配可用电机、网格在干涉移除后保持水密、通过FEA验证）
  - 时间消耗
  - 形状相似度（最终网格与初始网格的点云平均距离）
  - 平均相对密度
- **对比方法**：论文未与其他自动设计系统进行对比，而是自我评估成功率、时间、相似度等。

## 四、资源与算力
- 论文中明确说明：所有自动设计过程在一台配备AMD R9-5900X CPU的计算机上运行，未提及GPU型号或数量。
- 对于Lynel机器人（19自由度，体素0.5 cm），完整设计耗时约8小时。
- 对于四足机器人（12自由度，体素1 cm），平均每轮约8.5分钟，成功设计平均耗时20.4分钟；若体素提高到0.5 cm，每轮约22.5分钟。
- 时间主要消耗在执行器优化（遗传算法）和密度优化（FEA）步骤。

## 五、实验数量与充分性
- **定量实验**：100张Stanford Dogs图像，每张最多进行8轮缩放尝试，共产生约800次设计尝试。结果分析包括成功率、时间分布、失败原因、形状相似度、密度分布等，统计较为充分。
- **消融/对比实验**：未进行传统消融实验（如去掉某优化步骤的影响），而是通过失败原因分析（59.4%因FEA不满足、其次为电机不可用或网格损坏）间接说明各步骤作用。
- **定性实验**：展示了7种不同输入（4个文本、2个图像、1个3D模型）的设计结果，并实际制造了1个Centaur机器人并测试行走。
- **充分性评价**：实验覆盖了多种输入类型和复杂度，定量统计较全面，但缺乏与基线方法的直接对比（如与手动设计或现有计算设计系统对比），公平性方面存在一定不足。

## 六、论文的主要结论与发现
- 提出的DOA框架能从文本/图像输入自动生成可3D打印的功能性有肢机器人，非专家可在分钟至数小时内完成设计。
- 在100个四足机器人设计中，从第1轮到第8轮的有条件成功率从36%升至92%，平均每2.39轮成功；平均每轮8.5分钟，成功设计平均20.4分钟。
- 大多数失败由FEA约束不满足导致（薄壁部分或干涉移除后变得过薄）。
- 设计形状与输入相似度高（平均点距<1 cm），且通过密度优化使连杆轻量化（平均相对密度<0.15）。
- 实际制造的Centaur机器人（约15 kg）能够行走并做出多种姿态，验证了系统输出可制造性。

## 七、优点
- **自动从抽象媒体输入生成机器人**：结合生成式AI与优化，无需用户具备机械设计专业知识。
- **处理制造和装配细节**：通过几何优化、密度优化、燕尾榫连接、干涉检查等，输出可直接3D打印和组装。
- **设计空间大**：基于网格分解而非预定义模块，能生成多样化形状。
- **效率较高**：多数设计在分钟级完成，且轻量化程度好。
- **开放获取**：代码和材料公开在GitHub。

## 八、不足与局限
- **依赖输入质量**：初始网格质量由生成式AI决定，几何伪影会传播到后续步骤。
- **仅支持旋转关节**：无法处理线性或更复杂关节类型，限制了机构多样性。
- **成功率受限**：约8%的最终失败率（即使多轮缩放），主要来源于薄壁部件的FEA不满足或电机不可用。
- **缺乏对比实验**：未与现有计算设计系统（如RoboGrammar、Interactive Robogami）进行定量比较，难以评估相对优劣。
- **手动设计连接件**：燕尾榫连接件需针对每种电机手动设计，未完全自动化。
- **控制器设计未集成**：当前使用简单控制器，无法实现复杂运动。

（完）
