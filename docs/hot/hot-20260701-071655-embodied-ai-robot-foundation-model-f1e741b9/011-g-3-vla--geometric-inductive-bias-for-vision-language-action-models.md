---
title: "G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models"
authors: "Yue Peng, Yongzhe Zhao, Artur Habuda, Khuyen Pham, Yanheng Zhu, Tran Nguyen Le, Fares Abu-Dakka, Li Guo"
date: "2026-06-23"
pdf: "https://arxiv.org/pdf/2606.24472v1"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=google deepmind; query=(all:\"Field AI\" OR all:\"Intrinsic\" OR all:\"Google DeepMind\" OR all:\"NVIDIA\" OR all:\"Tesla\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "Vision-language-action (VLA) models have made rapid progress in generalist robot manipulation by harnessing semantic knowledge from pretrained vision-language backbones, but their visual tokens remain grounded in 2D image coordinates rather than the calibrated geometry of the robot's cameras -- a mismatch especially pronounced in multi-camera setups, where views are coupled by known intrinsics and extrinsics yet processed as independent images. We propose G$^3$VLA, a camera-aware geometric module that injects calibrated structure into the visual-token stream of a pretrained VLA without altering its action space or imitation objective, combining intrinsic-conditioned ray embeddings, projective positional encoding (PRoPE), and bidirectional cross-view fusion. Geometric supervision is provided either from ground-truth point maps when available, or from confidence-gated $π^3$X teacher predictions, requiring no depth sensors or manual annotations. Instantiated on $π_0$, G$^3$VLA yields consistent gains across the LIBERO suites, RoboCasa24, RoboTwin2.0, and real-robot settings, with the largest improvements on spatially and object-sensitive tasks. We further validate on $π_{0.5}$ and GR00T 1.5, with results suggesting that geometric transfer is most effective when geometry-aware tokens have direct access to the action generation pathway. Our project page is at https://sites.google.com/view/g3vla"
---

## 摘要

Vision-language-action (VLA) models have made rapid progress in generalist robot manipulation by harnessing semantic knowledge from pretrained vision-language backbones, but their visual tokens remain grounded in 2D image coordinates rather than the calibrated geometry of the robot's cameras -- a mismatch especially pronounced in multi-camera setups, where views are coupled by known intrinsics and extrinsics yet processed as independent images. We propose G$^3$VLA, a camera-aware geometric module that injects calibrated structure into the visual-token stream of a pretrained VLA without altering its action space or imitation objective, combining intrinsic-conditioned ray embeddings, projective positional encoding (PRoPE), and bidirectional cross-view fusion. Geometric supervision is provided either from ground-truth point maps when available, or from confidence-gated $π^3$X teacher predictions, requiring no depth sensors or manual annotations. Instantiated on $π_0$, G$^3$VLA yields consistent gains across the LIBERO suites, RoboCasa24, RoboTwin2.0, and real-robot settings, with the largest improvements on spatially and object-sensitive tasks. We further validate on $π_{0.5}$ and GR00T 1.5, with results suggesting that geometric transfer is most effective when geometry-aware tokens have direct access to the action generation pathway. Our project page is at https://sites.google.com/view/g3vla

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
- Source ID: http://arxiv.org/abs/2606.24472v1
- Link: http://arxiv.org/abs/2606.24472v1
