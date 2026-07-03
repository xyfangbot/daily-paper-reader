---
title: OpenMP GPU Acceleration and Portability of TRIMEG-C1 for Electromagnetic Gyrokinetic Simulations in Tokamak Plasmas
title_zh: 用于托卡马克等离子体中电磁回旋动理学模拟的TRIMEG-C1的OpenMP GPU加速与可移植性
authors: "Giorgio Daneri, Zhixin Lu, M Hoelzl, Luca Venerando Greco, Edoardo Carra"
date: 2026-06-23
pdf: "https://arxiv.org/pdf/2606.24327"
tags: ["query:热点论文筛选", "query:topic", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; query=B-spline trajectory generation"
tldr: 托卡马克等离子体电磁不稳定性模拟通常依赖回旋动理学粒子云方法，计算量巨大。TRIMEG-C1采用高阶C1有限元以降低网格分辨率需求，为在多种GPU平台上加速，本文基于OpenMP框架实现了NVIDIA和AMD GPU的代码移植，将粒子推动与粒子到网格操作适应于GPU架构。利用混合MPI-OpenMP并行，通过超额订阅GPU资源评估效率。在双AMD MI300A APU系统上，粒子推动核相比双AMD 9754 CPU获得约9倍加速，并正确再现了ITG模的线性增长率和二维模式结构。该工作验证了OpenMP卸载在高阶回旋动理学模拟中的可移植性，为未来大规模电磁不稳定性研究提供了高效计算方案。
source: openalex
selection_source: hot_paper_scout
motivation: 为加速未来回旋动理学物理研究，实现TRIMEG-C1代码在多种GPU架构（NVIDIA和AMD）上的可移植加速。
method: 采用OpenMP框架进行GPU卸载，将粒子推动和粒子到网格操作适配到NVIDIA和AMD GPU，结合混合MPI-OpenMP并行。
result: 在2个AMD MI300A APU上粒子推动核相比2个CPU获得约9倍加速，且正确模拟了ITG模的能量增长率和二维结构。
conclusion: 实现了跨平台GPU加速，验证了OpenMP卸载在高阶回旋动理学模拟中的有效性，提升了可移植性和计算效率。
---

## 摘要
基于三角网格的回旋动理学代码TRIMEG-C1采用粒子云方法求解回旋动理学方程，以模拟托卡马克等离子体中的电磁不稳定性。TRIMEG-C1使用高阶C1有限元方法，能够在比C0方法更低的网格分辨率下捕捉精确的物理特性。在这项工作中，我们专注于在多个图形处理单元（GPU）架构上实现可移植性实现，以加速TRIMEG-C1代码，用于未来的物理研究。选择OpenMP框架作为不同硬件平台上GPU卸载的加速框架，具体针对NVIDIA和AMD GPU。粒子推进过程以及粒子到网格的运算已适配为在GPU上执行。与2个AMD 9754 CPU相比，在2个AMD MI300A APU（加速处理单元）上，粒子推进核获得了约9倍的加速。此外，通过过度订阅GPU资源，评估了混合MPI-OpenMP卸载并行化的效率。使用GPU实现模拟了离子温度梯度（ITG）模式，并通过比较能量增长率和二维模式结构的物理结果验证了其正确性。

## Abstract
The Triangular mesh-based gyrokinetic code TRIMEG-C1 solves the gyrokinetic equations using the particle-in-cell scheme to simulate electromagnetic instabilities in tokamak plasmas. TRIMEG-C1 utilizes a high-order C1 finite element method, which captures the accurate physics with lower grid resolution than the C0 method. In this work, we focus on achieving a portable implementation on multiple graphics processing unit (GPU) architectures to accelerate the TRIMEG-C1 code for future physics studies. The OpenMP framework is chosen as the acceleration framework for GPU offloading on different hardware platforms, specifically, NVIDIA and AMD GPUs. The particle pushing procedure, as well as particle-to-grid operations have been adapted for GPU execution. A speedup of $\approx9$ for the particle pusher kernel is achieved on 2 AMD MI300A APUs (Accelerated Processing Unit) compared with 2 AMD 9754 CPUs. In addition, the efficiency of hybrid MPI-OpenMP offloading parallelization was assessed by oversubscribing GPU resources. The Ion Temperature Gradient (ITG) mode was simulated using the GPU implementation, and its correctness was verified by comparing the physics results in terms of the energy growth rate and the two-dimensional mode structures.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 托卡马克等离子体中的电磁不稳定性模拟需要高计算成本，尤其是基于粒子云（PIC）的回旋动理学代码。TRIMEG-C1采用高阶C1有限元方法，可在较低网格分辨率下保持精度，但计算瓶颈仍突出。
- 现代超算中GPU加速是提升大规模PIC模拟效率的关键，但不同HPC集群（NVIDIA和AMD GPU）需要可移植的加速方案。OpenMP是当前唯一支持两者且改动最小的Fortran GPU卸载框架。
- 论文核心目标是实现TRIMEG-C1在NVIDIA和AMD GPU上的可移植加速，验证其正确性和性能，为未来大规模物理研究提供计算基础。

## 二、论文提出的方法论
- **核心思想**：使用OpenMP编译器指令将计算密集的粒子推动（particle push）和网格-粒子（G2P）操作卸载到GPU，保持代码可移植性。
- **关键技术细节**：
  - 粒子推动核：循环遍历所有标记粒子，每个粒子独立求解回旋运动方程，包含B样条插值、场量插值等约3000行代码。采用`!$omp target teams distribute parallel do`指令将整个循环作为单一kernel。
  - 内存管理：预分配设备内存，静态数据结构一次性传输；对动态数组（如包围盒-三角形映射）采用展平（flatten）为1D数组策略，避免重复传输。
  - 编译器限制处理：针对`amdflang`和`nvfortran`的不足（如不支持多态、类型绑定过程、动态数组一致性），进行了代码重构：移除多态、手动内联、将局部数组改为编译时固定大小、修改B样条库以避免竞态条件。
  - 混合MPI-OpenMP并行：每个MPI进程对应一个GPU上下文，通过时间分片串行执行kernel；评估超额订阅GPU资源时的性能退化。
- **公式/算法流程**（文字说明）：采用混合变量/回拉方案处理矢量势；粒子运动方程包含平衡场和扰动场项；通过δf方法求解分布函数扰动；密度和电流投影到有限元网格后求解准中性方程和安培定律。

## 三、实验设计
- **数据集/场景**：
  - Cyclone base case：低β极限下模拟ITG模式，等离子体芯部参数，采用简化环形几何。
  - TCV-X21 case：更真实的偏滤器位形，模拟非线性静电ITG不稳定性，包含分界面。
- **Benchmark**：以原始CPU版本在TOK集群（2×AMD EPYC 9754，256核）上的结果为基准，对比GPU版本。
- **对比方法**：不对比其他加速框架（如CUDA Fortran、Kokkos等），主要对比CPU版本与GPU版本在不同硬件上的性能（Viper MI300A、Raven A100、Pitagora H100）和物理结果（增长率、二维模式结构、能量时间演化）。
- **验证方式**：在相同输入下，执行GPU和CPU内核并逐元素比较输出（消除FMA差异后可达机器精度）；物理验证通过n-scan（toroidal mode number扫描）和模式结构对比。

## 四、资源与算力
- 明确列出了使用的计算节点配置：
  - **Viper**：2×AMD MI300A APU（每组24核，128 GB HBM），无独立CPU，统一内存。
  - **Raven**：Intel Xeon 8360Y (36核) + 4×NVIDIA A100 (40 GB)。
  - **Pitagora**：2×Intel Xeon 6548Y (72核) + 4×NVIDIA H100 (94 GB)。
  - **TOK**：2×AMD EPYC 9754 (128核/CPU，共256核)，CPU-only。
- 训练/仿真时长：文中进行了单步性能测试（如32×10^6粒子），未报告完整长时间物理模拟的总时长；强可扩展性分析中运行了10个时间步。具体时长未给出，仅给出kernel执行时间（秒级）。

## 五、实验数量与充分性
- **性能实验**：
  - 单kernel分析：在不同MPI进程数（1、2、4、8、16、max）下测量粒子推动及三个小kernel（回拉、密度计算、分布函数插值）的加速比，使用10^6粒子。
  - 扩展大负载：32×10^6粒子下比较Viper和Pitagora vs TOK。
  - 强可扩展性：1~16个节点，32×10^6电子+10^6离子，运行10时间步。
  - 性能退化实验：在Viper、Raven、Pitagora上针对不同MPI进程数（从1到最大可用）测量kernel时间。
- **物理验证实验**：
  - Cyclone case：扫描n=6,10,14,18，比较增长率、二维模式结构、能量时间演化。
  - TCV-X21 case：扫描n=2,4,6,8,10，比较增长率、非线性饱和水平、二维结构。
- **充分性评价**：实验覆盖了不同硬件平台、不同问题规模、不同物理场景，性能测量多次取平均，物理验证包括线性与非线性特征。但未进行大规模长时间物理模拟（如数万时间步）以验证长期稳定性；未进行多节点弱可扩展性测试；未与其他GPU加速框架（如OpenACC、CUDA Fortran）做横向性能对比。整体较为充分但仍有提升空间。

## 六、论文的主要结论与发现
- 成功实现TRIMEG-C1在NVIDIA和AMD GPU上的可移植加速，OpenMP卸载框架有效。
- 粒子推动kernel在Viper（AMD MI300A）和Pitagora（NVIDIA H100）上相比CPU版本（TOK，256核）获得约9倍加速（32×10^6粒子规模）；三个小kernel加速比在5.7~9之间（不同平台略有差异）。
- GPU加速与MPI并行可良好协同，强可扩展性良好，性能不随节点数增加显著退化。
- 物理结果验证：Cyclone case和TCV-X21 case中，GPU版本再现了CPU版本的ITG线性增长率和二维模式结构，误差在可接受范围（大部分<7%）。
- 代码移植面临编译器限制、外部库不兼容、竞态条件等挑战，需大量重构和调试，最终方案仍存在少量代码分歧（如NVIDIA平台需固定数组大小）。

## 七、优点
- **可移植性优先**：选择OpenMP卸载使得单套源码即可编译运行于NVIDIA和AMD GPU，避免多套后端维护。
- **深入解决编译器限制**：系统总结了`amdflang`和`nvfortran`的常见问题及解决方法（如多态回避、动态数组展平、局部数组修改等），为类似工作提供参考。
- **全面的性能评估**：覆盖不同硬件、不同MPI进程数、不同问题规模，分析了超额订阅下的性能退化，并给出强可扩展性分析。
- **物理正确性验证充分**：通过两个标准案例的n-scan、能量增长率和模式结构对比，确认GPU实现未引入物理错误。
- **代码开源与可复现**：论文详细描述了修改细节和编译器选项，便于复现。

## 八、不足与局限
- **性能受限于OpenMP抽象**：无法直接使用GPU共享内存（LDS），寄存器压力高导致占用率降低；编译器优化有限，kernel性能难以达到手写CUDA/HIP水平。
- **代码可维护性下降**：为绕过编译器限制，部分代码使用了非惯用写法（如固定数组大小、移除多态），导致GPU与CPU版本存在代码分歧，增加维护成本。
- **实验覆盖不够全面**：
  - 未进行多节点弱可扩展性分析（问题规模随节点数线性增加）。
  - 未进行长时间（如数千时间步）物理模拟验证数值稳定性。
  - 未与OpenACC、CUDA Fortran等框架进行直接性能对比，可移植性代价未量化。
- **外部库依赖问题**：B样条库存在竞态条件和同步bug，需修改库内部实现，且问题在NVIDIA和AMD上表现不一致，降低了可移植性承诺。
- **物理验证存在小偏差**：由于浮点运算硬件差异和线性求解器数值敏感性，GPU结果与CPU结果在某些n值下误差超过10%（如TCV n=10），虽在可接受范围但需后续改进。
- **未应用更先进的优化**：如异步数据流、CUDA graphs、overlapping计算与通信等未讨论。

（完）
