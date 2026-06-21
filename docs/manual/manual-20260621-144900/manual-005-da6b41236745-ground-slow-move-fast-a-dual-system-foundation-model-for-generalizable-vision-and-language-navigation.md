---
title: "GROUND SLOW, MOVE FAST: A DUAL-SYSTEM FOUNDATION MODEL FOR GENERALIZABLE VISION-AND-LANGUAGE NAVIGATION"
title_zh: 慢思考，快行动：面向泛化视觉语言导航的双系统基础模型
authors: "Meng Wei, Chenyang Wan, Jiaqi Peng, Xiqian Yu, Yuqiang Yang, Delin Feng, Wenzhe Cai, Chenming Zhu, Tai Wang, Jiangmiao Pang, Xihui Liu"
date: 2026-06-21
pdf: "https://arxiv.org/pdf/2512.08186v1"
arxiv_id: 2512.08186v1
arxiv_url: "https://arxiv.org/abs/2512.08186v1"
manual_pdf_url: assets/manual-pdfs/manual-20260621-144900/005-2025_wei_dualvln-fdc5b499-da6b41236745.pdf
tags: ["query:手动上传", "paper:PDF", "paper:arXiv:2512.08186v1", "query:Vision-and-Language Navigation", "query:Dual-System", "query:Foundation Model", "query:Diffusion Policy", "query:Large Vision-Language Model"]
score: 10.0
evidence: 用户手动上传 PDF
tldr: 现有视觉语言导航方法依赖端到端管道，导致碎片化动作和高延迟，难以应对动态障碍。DualVLN提出双系统基础模型：System 2以VLM全局规划器缓慢接地，预测中期路径点；System 1以扩散Transformer策略快速移动，生成平滑轨迹。解耦训练保留VLM泛化性，实现鲁棒实时控制。在VLN基准和真实实验中超越先前方法，展现长程规划和实时适应性。
source: manual
selection_source: manual_upload
figures_json: "[{\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1396, \"height\": 755, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1436, \"height\": 545, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1289, \"height\": 473, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1420, \"height\": 629, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1446, \"height\": 382, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1452, \"height\": 324, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1432, \"height\": 567, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1444, \"height\": 375, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1448, \"height\": 333, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 581, \"height\": 423, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1457, \"height\": 985, \"label\": \"Figure\"}, {\"url\": \"assets/figures/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1456, \"height\": 949, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1455, \"height\": 1024, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1455, \"height\": 631, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1125, \"height\": 252, \"label\": \"Table\"}, {\"url\": \"assets/tables/manual/manual-manual-20260621-144900-manual-005-da6b41236745-ground-slow-move-fast-a-dual-system-foundation-model-for-generalizable-vision-and-language-navigation/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1309, \"height\": 269, \"label\": \"Table\"}]"
motivation: 克服端到端VLN方法中碎片化动作、高延迟和动态障碍规避难题。
method: 双系统设计：System 2 VLM规划器预测路径点，System 1扩散Transformer策略生成平滑轨迹，解耦训练保留泛化。
result: 在所有VLN基准测试中超越先前方法，真实环境实验验证长程规划与实时适应性。
conclusion: DualVLN通过双系统协同实现可泛化的视觉语言导航，兼顾高层推理与低层执行。
---

## 摘要
尽管近期的大规模视觉语言模型（VLM）在视觉语言导航（VLN）中提升了泛化能力，但现有方法通常依赖端到端流水线，将视觉语言输入直接映射为短视的离散动作。这种设计往往导致运动碎片化、高延迟，并难以应对动态障碍物规避等现实挑战。本文提出DualVLN，这是首个双系统VLN基础模型，将高层推理与低层动作执行协同整合。系统2是一个基于VLM的全局规划器，通过基于图像的推理预测中期航点目标，实现“慢思考”。系统1是一个轻量级的多模态条件扩散Transformer策略，利用系统2的显式像素目标和隐式特征生成平滑且准确的轨迹，实现“快行动”。双系统设计在复杂动态环境中实现了鲁棒的实时控制和自适应局部决策。通过解耦训练，VLM保持了其泛化能力，同时系统1实现了可解释且有效的局部导航。DualVLN在所有VLN基准测试中优于先前方法，真实世界实验证明了其在动态环境中鲁棒的长期规划能力和实时适应性。

## Abstract
While recent large vision-language models (VLMs) have improved generalization in vision-language navigation (VLN), existing methods typically rely on end-to-end pipelines that map vision-language inputs directly to short-horizon discrete actions. Such designs often produce fragmented motions, incur high latency, and struggle with real-world challenges like dynamic obstacle avoidance. We propose DualVLN, the first dual-system VLN foundation model that synergistically integrates high-level reasoning with low-level action execution. System 2, a VLM-based global planner, 'grounds slowly' by predicting mid-term waypoint goals via image-grounded reasoning. System 1, a lightweight multi-modal conditioning Diffusion Transformer policy, 'moves fast' by leveraging both explicit pixel goals and latent features from System 2 to generate smooth and accurate trajectories. The dual-system design enables robust real-time control and adaptive local decision-making in complex, dynamic environments. By decoupling training, the VLM retains its generalization, while System 1 achieves interpretable and effective local navigation. DualVLN outperforms prior methods across all VLN benchmarks and real-world experiments demonstrate robust long-horizon planning and real-time adaptability in dynamic environments.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 现有视觉语言导航（VLN）方法大多采用端到端流水线，将视觉语言输入直接映射为短视的离散动作（如移动0.25米），导致运动碎片化、高延迟，难以在真实世界中应对动态障碍物规避。
- 大型视觉语言模型（VLMs）虽具强泛化能力，但若直接用于连续动作预测，会因频繁调用大模型而产生高延迟，且缺乏高层规划与低层控制的显式协调。
- 作者提出首个双系统VLN基础模型DualVLN，将高层推理（慢思考）与低层动作执行（快行动）解耦，旨在兼顾VLM的泛化能力与实时控制所需的敏捷性，并实现动态障碍物规避。

## 二、论文提出的方法论
- **核心思想**：采用双系统架构，System 2（慢系统）基于VLM进行全局规划，预测中期航点（像素坐标）；System 1（快系统）基于扩散Transformer生成平滑连续轨迹，并利用System 2的显式像素目标和隐式潜变量作为条件。
- **关键技术细节**：
  - **System 2**：基于Qwen-VL-2.5 (7B) 微调，执行“最远像素航点接地”任务；同时具备自导视角调整能力（如转头、低头），在预测像素目标前主动寻找有信息量的视角。
  - **System 1**：轻量级扩散Transformer（DiT），输入包括低频潜变量（来自System 2）和高频RGB图像（异步更新），通过自注意力融合历史与当前视觉特征，并用Q-Former压缩为32个token；采用流匹配（Flow Matching）训练，预测轨迹速度。
  - **双系统连接**：System 2生成像素目标文本后，追加可学习的潜变量查询（latent queries）提取隐式目标特征，作为System 1的条件；System 2冻结，仅训练潜变量查询和System 1。
  - **解耦训练**：System 2先训练（全参数微调），System 1基于System 2的输出数据训练（冻结System 2），实现专业化分工，保留VLM泛化性。
- **流程**：System 2以2Hz运行，输出像素目标和潜变量；System 1以30Hz运行，结合最新RGB图像生成32个密集航点组成的轨迹，由MPC控制器执行；异步推理确保连续和平滑导航。

## 三、实验设计
- **数据集与场景**：
  - **VLN-CE**：基于Matterport3D的R2R-CE和RxR-CE基准，模拟连续室内导航。
  - **VLN-PE**：基于物理真实仿真平台（Unitree H1人形机器人），引入轨迹长度、摔倒率、卡住率等指标。
  - **Social-VLN**：作者自建基准，在R2R-CE基础上沿真实轨迹布置多个人形动态障碍物（Habitat 3.0），评估社交感知与任务恢复能力；新增人类碰撞率（HCR）指标。
  - **真实世界实验**：在轮式（Turtlebot4）、四足（Unitree Go2）、人形（Unitree G1）机器人上，测试走廊（易）、卧室（中）、办公室（难）三种场景，每场景20轮。
- **对比方法**：包括多传感器方法（CMA、ETPNav等）、仅RGB方法（NaVid、NaVILA、UniNaVid、StreamVLN等）、以及VLN-PE上的RDP、Seq2Seq等。
- **主要指标**：NE（导航误差）、SR（成功率）、OSR（最佳成功率）、SPL（路径加权成功率）、nDTW（标准化动态时间规整）；VLN-PE额外有TL（轨迹长度）、FR（摔倒率）、StR（卡住率）；Social-VLN增加HCR。

## 四、资源与算力
- 论文未明确说明训练System 2（QwenVL 7B全参数微调）和System 1（DiT）所需的确切GPU型号、数量及总训练时长。
- 仅提供训练步骤：System 2训练14000步（batch size 128）；System 1训练15000步（batch size 128）。
- 真实世界推理在一台RTX 4090上运行，显存占用20GB；System 2利用KV-cache将推理时间从1.1s降至0.7s，System 1使用TensorRT在0.03s内并行生成32条轨迹。
- 训练数据：System 2使用StreamVLN的数据配方；System 1收集了76.3万条社交导航轨迹（来自60个MP3D场景）用于Social-VLN训练。

## 五、实验数量与充分性
- 实验数量较为充分，覆盖三大仿真基准（VLN-CE、VLN-PE、Social-VLN）和真实世界跨机器人平台测试。
- 消融实验包括：影响显式像素目标与隐式潜变量的作用（图7）；替换System 1为其他端到端扩散策略（表4）；数据规模缩放分析（图9）；像素目标与轨迹的一致性分析（图10）。
- 对比方法覆盖面广，包括多传感器方法、VLM-free方法、视频LLM方法，且在同一基准上公平比较（部分基线带有*标记，使用航点预测器）。
- 实验客观性：在标准验证未见分集（Val-Unseen）上评估，避免过拟合训练场景；Social-VLN基准首次提出，对比了适合的低延迟基线StreamVLN。
- 总体评价：实验设计全面，消融充分，对比公平，但真实世界实验仅20次/场景，样本量较小。

## 六、论文的主要结论与发现
- DualVLN在所有VLN基准上均达到新最优：VLN-CE（R2R Val-Unseen SR 64.3%，SPL 58.5%）、VLN-PE（SR 51.6%）、Social-VLN（SR 37.2%），显著超越先前所有RGB-only方法和多传感器方法。
- 双系统解耦训练至关重要：端到端联合训练（w/o Sys.2 Train）导致性能下降（SR从64.3%降至55.2%），说明显式中间像素目标有助于保持VLM泛化。
- 显式像素目标和隐式潜变量互补：仅用像素目标（w/o Latent Goal）SR降至62.2%，仅用隐式潜变量（w/o Pixel Goal）SR降至60.9%，两者联合使用效果最佳。
- System 1数据缩放效率高：仅需System 2数据的10%即可达到近饱和性能，说明低层控制任务相对简单。
- 像素目标与轨迹一致性好：大多数轨迹点朝向像素目标方向，且最终接近目标。
- 真实世界鲁棒性：在不同机器人平台、静态与动态环境中，DualVLN均能选择正确像素目标并规划安全轨迹，优于NaVid、NaVILA、StreamVLN。

## 七、优点
- **架构创新**：首次将双系统（慢-快）思想系统化应用于VLN，实现显式高层规划与低层控制的解耦，兼顾泛化与实时性。
- **训练策略简洁有效**：分阶段训练（先训练System 2，再冻结System 2训练System 1），避免端到端训练导致的泛化下降；潜变量查询机制实现信息流自适应。
- **泛化能力强**：仅靠第一人称RGB（无需深度、里程计、全景图）即超越多传感器方法；零样本迁移至VLN-PE和真实世界不同机器人平台。
- **可解释性**：显式像素目标使System 2的规划可可视化；注意力图显示模型从全局语义逐步聚焦到目标像素。
- **新增Social-VLN基准**：弥补了动态障碍物评估的空白，推动社会感知导航研究。
- **实验全面**：涵盖仿真、真实世界、多机器人、多基准、多消融，验证充分。

## 八、不足与局限
- **计算资源未明确**：未说明训练System 2（7B VLM全参数微调）所需的GPU数量和时长，不利于复现和资源评估。
- **真实世界实验规模有限**：每个场景仅20次试验，统计显著性受限；仅测试了单一光照、室内环境，未涉及户外或更复杂动态场景。
- **Social-VLN基准仍不成熟**：自身方法在该基准上SR仅37.2%，HCR为35.4%，说明动态障碍规避能力仍有很大提升空间；训练数据（763K）仅覆盖60个MP3D场景，泛化性存疑。
- **对像素目标误差的鲁棒性有上限**：消融表明System 1对小偏移鲁棒，但对大方向错误或语义错误（如近障碍时）表现不佳（图8），实际部署中可能因视角调整失败导致错误目标。
- **依赖VLM的接地能力**：System 2的像素目标预测依赖Qwen-VL的空间接地能力，若VLM在复杂场景（如遮挡、非正面视角）下接地不准确，整体性能可能受限。
- **仅支持2D像素目标**：未考虑3D环境中的高度信息或绝对坐标，可能在需要精确3D定位的任务中表现不足。

（完）
