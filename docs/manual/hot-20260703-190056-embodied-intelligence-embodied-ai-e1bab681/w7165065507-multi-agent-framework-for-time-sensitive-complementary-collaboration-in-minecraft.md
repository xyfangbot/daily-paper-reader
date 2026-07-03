---
title: Multi-agent Framework for Time-Sensitive Complementary Collaboration in Minecraft
title_zh: Minecraft中时间敏感互补协作的多智能体框架
authors: "Juheon Yi, Yi-Xiang Wang, Xiaoyi Zhang, Ye Lu"
date: 2026-06-14
pdf: "https://arxiv.org/pdf/2606.15684"
tags: ["query:热点论文筛选", "query:综合方向", "query:具身智能公司相关", "paper:OpenAlex", "company:microsoft research"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=microsoft research; relation_source=lead-affiliation; institutions=Microsoft Research Asia (China); query=generalist robot policy"
tldr: 针对现实协作中智能体异构、强制协作、动态环境和实时约束等特性，基于Minecraft构建了时间敏感互补协作基准TickingCollabBench。开发了TickingCollab框架，抽象原始API并支持YAML声明式任务规范。提出可行性感知自动生成管道，由LLM起草任务配置并由验证器过滤无效项。评估显示LLM在动态部分可观测环境下因协调困难频繁失败，远不及全知预言机。
source: openalex
selection_source: hot_paper_scout
motivation: 现有基准缺乏对动态环境下异构智能体实时互补协作的评估，需要更真实的Minecraft测试场景。
method: 基于Minecraft构建TickingCollab框架，使用YAML声明式任务规范，并设计可行性感知自动化基准生成管道，由LLM起草配置、验证器过滤。
result: LLM在动态环境和部分可观测条件下，因语言延迟和异构性导致协调失败，性能显著低于全局知识预言机。
conclusion: 该基准揭示了LLM在实时协作中的根本局限，为多智能体协同研究提供了新挑战。
---

## 摘要
我们提出了TickingCollabBench，一个基于Minecraft的多智能体基准，用于一类新型的时间敏感互补协作任务。该基准反映了真实世界协作的四个核心特征：智能体异质性、强制协作、动态环境以及带有失败风险的严格实时约束。为实现这一目标，我们开发了TickingCollab框架，支持生成多样的动态环境，并抽象Minecraft的原始API，以便通过声明式YAML任务规范来组合这些事件。在此基础上，我们设计了一个可行性感知的自动基准生成流程，其中大语言模型生成结构多样的任务配置，可行性验证器利用近似约束过滤无效配置。评估表明，在部分可观测性和智能体异质性下的协调中，语言延迟和固有困难导致大语言模型在动态环境中频繁失败，且远不及全局知识预言机。

## Abstract
We present TickingCollabBench, a Minecraft-based multi-agent benchmark for a novel class of time-sensitive complementary collaboration tasks. Our benchmark reflects four core characteristics of real-world collaboration: agent heterogeneity, mandatory collaboration, dynamic environments, and strict real-time constraints with failure risks. To enable this, we develop the TickingCollab framework, which supports the generation of diverse dynamic environments and abstracts Minecraft's primitive APIs to enable declarative YAML task specifications for composing these events. Building on this, we design a feasibility-aware automated benchmark generation pipeline, where an LLM drafts structurally diverse task configurations and feasibility verifier filters out invalid ones using approximate constraints. Evaluations demonstrate that lang latency and inherent difficulty of coordinating under partial observability and agent heterogeneity cause LLMs to frequently fail under dynamic environments and fall significantly short of a global-knowledge oracle.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- **现实协作需求**：真实世界多智能体协作（如救灾机器人、个人设备协同）需处理：部分可观测性、异构能力、严格时间约束和失败风险。
- **现有基准不足**：Minecraft多智能体基准（如MineLand、TeamCraft、MineCollab）大多缺乏动态环境、不强制协作、无实时失败惩罚，或仅同质智能体。
- **本文目标**：构建一个新的Minecraft基准 TickingCollabBench，系统评估大语言模型（LLM）在“时间敏感互补协作”中的表现，填补动态异构实时协同评估空白。

## 二、论文提出的方法论
- **核心思想**：
  - 定义时间敏感互补协作任务的四个特性：智能体异构性（H）、强制协作必要性（N）、环境动态性（D）、严格时间失效（τ）。
  - 提供声明式YAML接口，无需Minecraft API编程即可定义任务。
- **关键技术细节**：
  - **TickingCollab框架**：
    - 动态环境管理器：自动注入运行时动态事件（如熔岩波、怪物生成/消失）。
    - 任务编排器：支持同步（固定时间步）和异步（实时）两种执行模式，隔离推理准确性与延迟影响。
    - 多智能体运行时：模块化智能体核心与通信管理，支持灵活协调逻辑。
  - **自动基准生成管道**：
    - LLM根据用户模板和参数空间起草多样化配置。
    - 可行性验证器：利用近似约束（如时间裕度α、β、γ）过滤不可行配置，确保任务可解且难度可控。
- **协作难度度量**：
  - H：平均配对属性差异（连续/集合属性）。
  - N：总工作量/单智能体最大吞吐量的比值（>1表示强制协作）。
  - D：环境状态变化次数/仿真时长。
  - τ：任务失败时间窗口（如危机到达时间、方块最短寿命）。

## 三、实验设计
- **数据集与场景**：
  - 基准 TickingCollabBench 包含三个任务套件：
    1. **Prepare for a Crisis**：建造避难所应对危机（熔岩/水/雪）。
    2. **Mine Vanishing Blocks**：在方块消失前挖掘指定类型与数量。
    3. **Raid a Boss**：击败Boss及其动态生成的小兵。
  - 共生成634个有效任务配置（225+219+190）。
- **基准对比**：
  - **预言机（Oracle）**：拥有全局真实信息和人工调度规则（非LLM），作为上界。
  - **TickingCollabAgent**基线：两种协调策略：
    - **集中式（Centralized）**：单一主智能体聚合所有观测进行联合规划。
    - **分布式（Distributed）**：各智能体独立规划，通过“提议-等待-行动”协商协议协调。
- **实验变量**：
  - 两个LLM后端：GPT-5.1、DeepSeek-R1。
  - 两种执行模式：同步（忽略推理延迟） vs 异步（实时运行）。
  - 消融：团队规模（2-8个智能体）、系统成本（消息数、推理次数、token用量、耗时）、协调开销。

## 四、资源与算力
- **硬件平台**：Ubuntu 22.04.5，AMD EPYC 9V84 CPU（80逻辑核），629 GiB RAM。
- **LLM后端**：托管于Azure AI Foundry（GPT-5.1和DeepSeek-R1），未提及GPU型号、数量或训练时长（因模型为现成API）。
- **仿真环境**：Minecraft Java Edition 1.19，Fabric服务器（loader v0.14.18），Mineflayer 4.14.0。
- **说明**：论文未报告具体训练或推理的GPU资源使用详情。

## 五、实验数量与充分性
- **实验规模**：
  - 三个任务，634个配置，两个LLM，两种协调策略，两种执行模式 → 共约 634×2×2×2 = 约5072次试验（实际可能因时间限制部分抽样）。
  - 消融实验：团队规模（4组）、系统成本（4项指标）、协调开销（步级分析）。
- **充分性评价**：
  - 积极：覆盖多种难度维度、对比了预言机和基线、分离了同步/异步影响，消融探究了规模与延迟瓶颈。
  - 局限性：仅测试两种简单协调策略；未探索更复杂的通信拓扑或规划算法；任务数量有限（3种），生成配置虽多但同质任务较多。

## 六、论文的主要结论与发现
- **LLM在动态实时协作中表现差**：异步模式下平均成功率极低（如GPT-5.1集中式异步成功率：危机0.15、挖掘0.05、突袭0.06），主要因API延迟约20秒/次远快于环境失效时间。
- **集中式优于分布式**：同步模式下集中式成功率更高（如GPT-5.1危机0.42 vs 分布式0.24），因分布式通信和推理开销大。
- **远不及预言机**：即使同步模式，集中式仍与预言机差距大（预言机危机0.91、挖掘0.80、突袭0.59），表明部分可观测性和异构性复杂。
- **团队规模影响**：挖掘和突袭任务中增加智能体提高吞吐量，但危机任务中增加智能体所需避难材料增多导致成功率下降。
- **系统成本开销大**：分布式下消息量、推理次数、token用量、耗时随团队规模急剧增长，接近超时。
- **协调开销瓶颈**：集中式存在大量等待空闲（因推理延迟），分布式因协商占用大量规划步骤。

## 七、优点
- **基准创新性**：首个专注“时间敏感互补协作”的Minecraft基准，量化四个关键协作维度（H、N、D、τ）。
- **声明式任务接口**：无需Minecraft API编程，YAML描述降低使用门槛。
- **自动生成管道**：LLM+可行性验证器，高效生成多样化可通过控制难度，避免手工设计。
- **双执行模式**：同步模式隔离推理准确性，异步模式评估实时性，便于诊断瓶颈。
- **全面评估**：包含多个LLM、多种协调拓扑、消融实验，提供细致的系统成本分析。

## 八、不足与局限
- **观测模态局限**：仅使用距离限制的结构化语义传感器，未涉及第一人称视觉/多模态输入。
- **环境交互简单**：支持但未充分利用复杂交互（如负重系统、区域buff/debuff）。
- **基线策略简单**：仅评估集中式和简单分布式，未探索更高效的通信拓扑或规划算法（如基于图的搜索）。
- **任务多样性有限**：三个任务虽覆盖不同场景，但同质程度高（均基于Minecraft世界），可能无法完全反映真实复杂协作。
- **算力资源未完全透明**：未报告GPT-5.1/DeepSeek-R1具体GPU型号和推理延迟分布，影响可复现性。
- **可行性验证近似性**：使用α、β、γ裕度，但未系统研究其对任务难度分布的影响，可能引入筛选偏差。

（完）
