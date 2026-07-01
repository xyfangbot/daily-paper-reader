---
title: "Trust Your Instincts: Confidence-Driven Test-Time RL for Vision-Language-Action Models"
authors: "Siyao Chen, Jiakang Yuan, Jiaxin Wang, Tao Chen"
date: "2026-06-29"
pdf: "https://arxiv.org/pdf/2606.29892v1"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=google deepmind; query=(all:\"Field AI\" OR all:\"Intrinsic\" OR all:\"Google DeepMind\" OR all:\"NVIDIA\" OR all:\"Tesla\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "Reinforcement learning (RL) has become indispensable for pushing Vision-Language-Action Models (VLAs) beyond static imitation learning. However, existing RL methods typically require external environmental feedback, relying on predefined success signals to guide policy updates. In this work, we show that VLA models possess useful internal evaluative capabilities: in discrete-action VLAs, trajectories with higher generation confidence are significantly more likely to succeed. Based on this observation, we introduce T^2VLA (Test-time VLA), an architecture-agnostic test-time RL framework that enables VLA models to achieve self-bootstrapping policy improvement. Instead of relying on external rewards, T^2VLA leverages trajectory-level similarity to high-confidence expert demonstrations as an intrinsic reward signal. In addition, we propose a Confidence-Driven Dual Expert Bootstrapping mechanism, which dynamically balances a Local Pseudo-Expert for exploration and a Global Expert Pool for training stability. Extensive experiments on the LIBERO and RoboTwin benchmarks show that T^2VLA consistently outperforms supervised baselines and approaches oracle RL performance with ground-truth rewards, achieving effective improvement without external reward feedback. Furthermore, T^2VLA adapts to distinct VLA paradigms, including both OpenVLA-OFT and the pi series."
---

## 摘要

Reinforcement learning (RL) has become indispensable for pushing Vision-Language-Action Models (VLAs) beyond static imitation learning. However, existing RL methods typically require external environmental feedback, relying on predefined success signals to guide policy updates. In this work, we show that VLA models possess useful internal evaluative capabilities: in discrete-action VLAs, trajectories with higher generation confidence are significantly more likely to succeed. Based on this observation, we introduce T^2VLA (Test-time VLA), an architecture-agnostic test-time RL framework that enables VLA models to achieve self-bootstrapping policy improvement. Instead of relying on external rewards, T^2VLA leverages trajectory-level similarity to high-confidence expert demonstrations as an intrinsic reward signal. In addition, we propose a Confidence-Driven Dual Expert Bootstrapping mechanism, which dynamically balances a Local Pseudo-Expert for exploration and a Global Expert Pool for training stability. Extensive experiments on the LIBERO and RoboTwin benchmarks show that T^2VLA consistently outperforms supervised baselines and approaches oracle RL performance with ground-truth rewards, achieving effective improvement without external reward feedback. Furthermore, T^2VLA adapts to distinct VLA paradigms, including both OpenVLA-OFT and the pi series.

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
- Source ID: http://arxiv.org/abs/2606.29892v1
- Link: http://arxiv.org/abs/2606.29892v1
