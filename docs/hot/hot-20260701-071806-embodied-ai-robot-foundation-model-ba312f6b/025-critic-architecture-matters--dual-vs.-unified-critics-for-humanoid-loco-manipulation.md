---
title: "Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation"
authors: "Mehmet Turan Yardımcı"
date: "2026-06-10"
pdf: "https://arxiv.org/pdf/2606.11891v1"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=google deepmind; query=(all:\"Field AI\" OR all:\"Intrinsic\" OR all:\"Google DeepMind\" OR all:\"NVIDIA\" OR all:\"Tesla\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "Multi-objective reinforcement learning for humanoid robots must coordinate locomotion and manipulation within a single policy. A natural design choice is whether to use a single (unified) critic that estimates the combined value of all objectives, or separate (dual) critics with disjoint reward signals. We present a controlled comparison on the Unitree G1 humanoid (23 active DoF) in NVIDIA Isaac Lab, training loco-manipulation policies through a sequential curriculum spanning 13 levels from stationary reaching to walking with variable-orientation targets. In standardized evaluation, dual-critic policies reach targets 3.5$\\times$ faster (6.5 vs. 22.6 simulation steps), achieve 2$\\times$ higher throughput (14.3 vs. 7.0 validated reaches per 1,000 steps), and attain higher validated reach rates (65.2% vs. 53.8%) compared to the unified-critic policy. Notably, additional anti-gaming reward mechanisms provide no further improvement beyond the architectural change alone (60.9% vs. 65.2%). These results have direct implications for the emerging paradigm of RL fine-tuning of imitation-learned policies: when refining a pre-trained manipulation policy with RL, a unified critic risks suppressing the learned behavior through competing locomotion gradients. These findings demonstrate that critic architecture is a primary - and often overlooked - design choice in multi-objective humanoid RL, with greater impact than reward engineering on reaching efficiency."
---

## 摘要

Multi-objective reinforcement learning for humanoid robots must coordinate locomotion and manipulation within a single policy. A natural design choice is whether to use a single (unified) critic that estimates the combined value of all objectives, or separate (dual) critics with disjoint reward signals. We present a controlled comparison on the Unitree G1 humanoid (23 active DoF) in NVIDIA Isaac Lab, training loco-manipulation policies through a sequential curriculum spanning 13 levels from stationary reaching to walking with variable-orientation targets. In standardized evaluation, dual-critic policies reach targets 3.5$\times$ faster (6.5 vs. 22.6 simulation steps), achieve 2$\times$ higher throughput (14.3 vs. 7.0 validated reaches per 1,000 steps), and attain higher validated reach rates (65.2% vs. 53.8%) compared to the unified-critic policy. Notably, additional anti-gaming reward mechanisms provide no further improvement beyond the architectural change alone (60.9% vs. 65.2%). These results have direct implications for the emerging paradigm of RL fine-tuning of imitation-learned policies: when refining a pre-trained manipulation policy with RL, a unified critic risks suppressing the learned behavior through competing locomotion gradients. These findings demonstrate that critic architecture is a primary - and often overlooked - design choice in multi-objective humanoid RL, with greater impact than reward engineering on reaching efficiency.

## 领衔机构

- google deepmind

## 机构

- google deepmind

## 来源信息

- Citations: 0
- Source: arXiv fallback
- Matched query: (all:"Field AI" OR all:"Intrinsic" OR all:"Google DeepMind" OR all:"NVIDIA" OR all:"Tesla") AND (all:"embodied AI" OR all:"robot foundation model" OR all:"vision-language-action model" OR all:"humanoid robot" OR all:"embodied intelligence" OR all:"vision-language-action" OR all:"robot learning" OR all:"physical AI")
- Company match: google deepmind
- DOI: 
- Source ID: http://arxiv.org/abs/2606.11891v1
- Link: http://arxiv.org/abs/2606.11891v1
