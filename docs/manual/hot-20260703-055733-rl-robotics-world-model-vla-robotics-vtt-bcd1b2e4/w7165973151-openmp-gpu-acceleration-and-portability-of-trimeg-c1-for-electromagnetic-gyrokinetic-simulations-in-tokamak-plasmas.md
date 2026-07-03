---
title: OpenMP GPU Acceleration and Portability of TRIMEG-C1 for Electromagnetic Gyrokinetic Simulations in Tokamak Plasmas
title_zh: 面向托卡马克等离子体中电磁回旋动理学模拟的TRIMEG-C1代码的OpenMP GPU加速与可移植性
authors: "Giorgio Daneri, Zhixin Lu, M Hoelzl, Luca Venerando Greco, Edoardo Carra"
date: 2026-06-23
pdf: "https://arxiv.org/pdf/2606.24327"
tags: ["query:热点论文筛选", "query:topic", "query:具身智能公司相关", "paper:OpenAlex", "company:nvidia"]
score: 7.5
evidence: "hot-paper-scout: OpenAlex; window=30d; cited_by_count=0; institution_filter=company; company_relation_match=nvidia; relation_source=abstract; query=B-spline trajectory generation"
tldr: 托卡马克等离子体电磁不稳定性模拟需高计算量，TRIMEG-C1使用高阶C1有限元法但计算密集。本文采用OpenMP框架在NVIDIA和AMD GPU上实现粒子推动与网格操作的便携加速。在2个AMD MI300A APU上相比2个AMD 9754 CPU获得约9倍加速，成功模拟离子温度梯度模式并验证正确性。该工作为未来大规模回旋动理学模拟提供了高效跨平台方案。
source: openalex
selection_source: hot_paper_scout
motivation: 加速TRIMEG-C1代码，实现多GPU架构便携性，以高效模拟托卡马克等离子体中的电磁不稳定性。
method: 采用OpenMP框架在NVIDIA和AMD GPU上卸载粒子推动与粒子-网格操作，结合混合MPI-OpenMP并行化。
result: 在2个AMD MI300A APU上粒子推动器加速约9倍，正确模拟ITG模式的能量增长率和二维结构。
conclusion: 成功实现TRIMEG-C1在多GPU上的便携加速并验证正确性，为电磁回旋动理学模拟奠定高效基础。
---

## 摘要
基于三角网格的回旋动理学代码TRIMEG-C1采用粒子云方法求解回旋动理学方程，以模拟托卡马克等离子体中的电磁不稳定性。TRIMEG-C1利用高阶C1有限元方法，相比于C0方法能在较低网格分辨率下捕获精确的物理信息。本文工作聚焦于在多种图形处理器（GPU）架构上实现可移植的加速方案，以提升TRIMEG-C1代码在未来物理研究中的性能。我们选择OpenMP框架作为在不同硬件平台（特别是NVIDIA和AMD GPU）上进行GPU卸载的加速框架。粒子推进过程以及粒子到网格的操作已适配GPU执行。与2颗AMD 9754 CPU相比，在2颗AMD MI300A APU（加速处理单元）上粒子推进器内核获得了约9倍的加速比。此外，通过超额订阅GPU资源评估了混合MPI-OpenMP卸载并行化的效率。利用GPU实现模拟了离子温度梯度（ITG）模，并通过比较能量增长率与二维模结构的物理结果验证了其正确性。

## Abstract
The Triangular mesh-based gyrokinetic code TRIMEG-C1 solves the gyrokinetic equations using the particle-in-cell scheme to simulate electromagnetic instabilities in tokamak plasmas. TRIMEG-C1 utilizes a high-order C1 finite element method, which captures the accurate physics with lower grid resolution than the C0 method. In this work, we focus on achieving a portable implementation on multiple graphics processing unit (GPU) architectures to accelerate the TRIMEG-C1 code for future physics studies. The OpenMP framework is chosen as the acceleration framework for GPU offloading on different hardware platforms, specifically, NVIDIA and AMD GPUs. The particle pushing procedure, as well as particle-to-grid operations have been adapted for GPU execution. A speedup of $\approx9$ for the particle pusher kernel is achieved on 2 AMD MI300A APUs (Accelerated Processing Unit) compared with 2 AMD 9754 CPUs. In addition, the efficiency of hybrid MPI-OpenMP offloading parallelization was assessed by oversubscribing GPU resources. The Ion Temperature Gradient (ITG) mode was simulated using the GPU implementation, and its correctness was verified by comparing the physics results in terms of the energy growth rate and the two-dimensional mode structures.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、论文的核心问题与整体含义（研究动机和背景）
- 托卡马克等离子体中的电磁不稳定性（如离子温度梯度模）的模拟需要大量计算资源，传统CPU实现难以满足大规模、多尺度模拟的需求。
- TRIMEG-C1是基于三角网格的高阶C1有限元回旋动理学粒子云代码，已在物理验证中表现出色，但其计算瓶颈限制了物理研究的规模，特别是粒子推进和粒子-网格操作占模拟总时间的40%左右。
- 现代高性能计算集群中GPU加速已成为主流，但不同集群使用不同GPU架构（NVIDIA和AMD），代码可移植性成为关键挑战。MPCDF的Viper集群基于AMD MI300A APU，Raven和Pitagora集群基于NVIDIA A100/H100，因此需要一种能在两类硬件上高效运行的统一方案。

## 二、论文提出的方法论
- **核心思想**：利用OpenMP卸载框架，在保持代码最小改动的前提下，将TRIMEG-C1中计算密集的粒子推进内核及粒子到网格操作移植到NVIDIA和AMD GPU上，实现可移植的加速。
- **关键技术细节**：
  - 采用`!$omp target teams distribute parallel do`指令将整个粒子循环包装成单一GPU内核，暴露大量并行度。
  - 预分配GPU设备内存，避免运行时分配开销；静态数据结构一次性传输到GPU。
  - 针对B样条插值库进行修改：将线程共享的临时数组改为局部自动数组（避免竞态条件），将可扩展类型（class）改为非多态类型（type），以绕过编译器限制（nvfortran不支持动态类型和类型绑定过程）。
  - 将AoS结构展平为两个一维数组，简化GPU映射并避免每次内核调用时的复杂传输。
  - 在NVIDIA平台上，将B样条库中运行时确定大小的临时数组改为编译时最大尺寸（12），以消除因自动分配导致的性能开销。
  - 对AMD平台启用统一共享内存（USM），减少显式数据拷贝；对NVIDIA平台使用编译标志关闭融合乘加（FMA）以消除数值差异。
- **公式与算法流程**（文字说明）：
  - 粒子运动方程基于回旋中心坐标系下的归一化方程，包括平衡场和扰动场的贡献，涉及B*有效磁场、回旋平均等。
  - 扰动分布函数δf沿轨迹演化，通过场量插值和权重计算得到对密度和电流的贡献。
  - 准中性方程和平行安培定律通过PETSc求解，理想欧姆定律用于计算δA∥的辛克部分。

## 三、实验设计
- **使用的数据集/场景**：
  1. **Cyclone基例**（低β极限下的ITG模）：采用简化环形托卡马克几何，归一化离子回旋半径ρ*=1/60，mi/me=100，关闭回旋平均，βN=0.004。模拟8×10⁶电子标记和2.5×10⁵离子标记，径向网格点数Nr=16（n=2时）或32（其他n）。
  2. **TCV-X21案例**（非线性静电ITG不稳定性）：真实偏滤器位形包括分离面，ρref=1 cm（非标称值0.3539 cm），Bref=0.90727 T。模拟10⁶电子标记和2.5×10⁵离子标记。
- **Benchmark与对比**：
  - 性能基准：CPU版本运行在TOK集群（2颗AMD EPYC 9754，每颗128核）上；GPU版本运行在Viper（2颗AMD MI300A APU）、Raven（4×A100）、Pitagora（4×H100）上。
  - 对比方法：仅对比CPU vs GPU实现，未与其他GPU编程模型（如CUDA Fortran、HIP、Kokkos）进行性能比较。
- **实验内容**：
  - 单个内核（粒子推进器、回拉处理、密度计算、分布函数插值）的性能测试，问题尺寸10⁶电子，变化MPI进程数（1,2,4,8,16,最大值）。
  - 大规模问题（32×10⁶电子）在Viper和Pitagora上与TOK对比。
  - 强扩展性测试：1至16个GPU节点，模拟32×10⁶电子和10⁶离子，运行10个时间步。
  - 物理正确性验证：在Cyclone案例中扫描环向模数n=6,10,14,18；在TCV案例中扫描n=2,4,6,8,10。比较能量增长率γ和二维模结构。

## 四、资源与算力
- **GPU集群**：
  - Viper：2颗AMD MI300A APU（每颗24核、128 GB HBM），共2个APU。
  - Raven：Intel Xeon 8360Y（36核）×2 + 4×NVIDIA A100（40 GB）。
  - Pitagora：2×Intel 6548Y（72核/CPU） + 4×NVIDIA H100（94 GB）。
- **CPU集群**：
  - TOK：2颗AMD EPYC 9754（128核/CPU），共256核。
- **编译工具**：amdflang 22.0/23.2，nvfortran 25.1。
- **算力说明**：未明确给出训练时长，仅给出单次内核执行时间。例如，10⁶电子粒子推进器在单MPI进程下Viper GPU耗时0.0478秒，TOK CPU耗时29.65秒；32×10⁶电子时Viper GPU耗时0.363秒，TOK CPU耗时3.22秒。

## 五、实验数量与充分性
- **实验数量**：
  - 单个内核性能测试：粒子推进器在3个GPU集群上各进行了6种MPI配置（1,2,4,8,16,最大值）的测试；3个小内核（回拉+密度+插值）类似，共约6组×2类型×3集群=36组+大规模测试2组（32×10⁶）+强扩展1组（5节点数点）。
  - 物理验证：Cyclone案例4个n值，TCV案例5个n值，每组对比CPU和GPU的生长率；另外提供了n=14（Cyclone）和n=4（TCV）的能量时间演化图和二维模结构对比。
  - 强扩展性：1、2、4、8、16节点共5组。
- **充分性**：
  - 性能测试覆盖了从小规模（10⁶）到较大规模（32×10⁶）的问题，以及单节点多MPI进程的过度订阅场景，结果充分展示了不同硬件上的加速比和扩展性。
  - 物理验证覆盖了低β和高β、简化几何和真实几何、线性阶段和部分非线性阶段，但仅限ITG模，未涉及其他不稳定性（如TEM、KBM）或电磁全模型。
  - 实验未与OpenACC、CUDA Fortran等替代方案直接对比，因此无法判断OpenMP的相对优劣。

## 六、论文的主要结论与发现
- 成功利用OpenMP卸载框架将TRIMEG-C1的粒子推进内核和网格到粒子操作移植到NVIDIA（A100、H100）和AMD（MI300A）GPU上，实现了代码可移植性。
- 在32×10⁶电子的大规模问题下，粒子推进器在Viper和Pitagora上均获得约9倍的加速比（对比256核CPU）；在小规模问题（10⁶电子）下加速比最高可达743倍（单MPI进程），但受限于MPI并行度，全节点使用时加速比降至5.7~8.8。
- 混合MPI-OpenMP卸载的扩展性良好：强扩展测试表明GPU实现随节点数增加表现稳定，但整体性能提升受限于CPU主导的粒子到网格（P2G）阶段。
- 物理验证表明，GPU实现能正确复现Cyclone和TCV案例的ITG模线性增长率（差异大多在3%以内，最高约10%）和二维模结构，非线性饱和水平一致。

## 七、优点
- **可移植性**：选择了OpenMP这一唯一同时支持NVIDIA和AMD GPU的Fortran兼容方案，避免了代码分叉，是实际HPC环境下的务实选择。
- **解决编译器限制**：针对nvfortran和amdflang的多个限制（不支持多态、动态数组、类型绑定过程等）提出了具体工作区，如展平AoS、改为非多态类型、使用编译期尺寸数组等，系统性地总结了移植经验，对同类工作有参考价值。
- **性能分析详尽**：提供了单内核、全节点、强扩展等多个层次的性能数据，并剖析了寄存器压力、L1/L2缓存命中率、指令混合等底层指标（sec. 4.3），解释了性能瓶颈。
- **物理验证扎实**：在两种典型案例（Cyclone基例和TCV实际位形）上进行了n扫描，验证了线性增长率和非线性饱和，并分析了数值差异（FMA、随机初始化）的非本质性。

## 八、不足与局限
- **编译器依赖性强**：OpenMP卸载在不同编译器间的行为不一致（如nvfortran与amdflang对相同代码的优化效果差异大），导致需要平台特定修改（如NVIDIA上手动设置数组尺寸），增加了维护负担。
- **性能上限受CPU瓶颈限制**：混合MPI-OpenMP模式下，CPU部分（如P2G操作、线性求解）无法利用GPU，导致整体加速比受限；强扩展测试中GPU实现优势随节点数增加减弱。
- **实验覆盖有限**：仅专注于ITG模，未验证电磁全模型（如回拉混合变量方案）或其他不稳定性；未与OpenACC或CUDA Fortran进行直接性能对比，无法证明OpenMP是最优选择。
- **缺乏非线性长时间模拟验证**：TCV案例仅展示了线性到非线性饱和的初步结果，未进行长时间湍流统计（如热通量）的对比。
- **数值精度问题**：在NVIDIA平台上无法通过关闭FMA完全消除数值差异（仍存在~10⁻¹⁴量级差异），可能影响对低β或高精度要求的模拟。
- **应用限制**：单节点最大粒子数受GPU内存限制（Viper上约64×10⁶），且MPI进程数超过24时会出现OOM错误。

（完）
