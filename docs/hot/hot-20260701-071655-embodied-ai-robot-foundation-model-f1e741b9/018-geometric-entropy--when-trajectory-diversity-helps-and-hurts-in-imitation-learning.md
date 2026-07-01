---
title: "Geometric Entropy: When Trajectory Diversity Helps and Hurts in Imitation Learning"
authors: "Qian Luo, Ruizhe Liu, Pei Zhou, Xunzhe Zhou, Yanchao Yang"
date: "2026-06-18"
pdf: "https://arxiv.org/pdf/2606.20871v1"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=google deepmind; query=(all:\"Field AI\" OR all:\"Intrinsic\" OR all:\"Google DeepMind\" OR all:\"NVIDIA\" OR all:\"Tesla\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "We study how trajectory-shape diversity in demonstrations affects imitation learning (IL) performance across models, tasks, and data scales. We introduce Geometric Entropy (H_G), a task-agnostic metric that quantifies the intrinsic diversity of transit trajectories after normalizing away extrinsic variation, such as goal pose and workspace scale, via target-frame alignment. Across multiple IL architectures and both simulated and real-robot contact-rich manipulation tasks, we observe a consistent inverted-U relationship between success and H_G: increasing geometric diversity improves robustness in low-diversity regimes but degrades performance once diversity induces strategy ambiguity. Moreover, the optimal entropy shifts toward lower values as task mastery increases through more data, easier tasks, or stronger priors, and for a pretrained vision-language-action model the trend becomes effectively monotonic decreasing. Practically, H_G enables fast pre-training auditing of demonstration datasets and offers a simple guideline for calibrating demonstrations toward the learnable regime."
---

## 摘要

We study how trajectory-shape diversity in demonstrations affects imitation learning (IL) performance across models, tasks, and data scales. We introduce Geometric Entropy (H_G), a task-agnostic metric that quantifies the intrinsic diversity of transit trajectories after normalizing away extrinsic variation, such as goal pose and workspace scale, via target-frame alignment. Across multiple IL architectures and both simulated and real-robot contact-rich manipulation tasks, we observe a consistent inverted-U relationship between success and H_G: increasing geometric diversity improves robustness in low-diversity regimes but degrades performance once diversity induces strategy ambiguity. Moreover, the optimal entropy shifts toward lower values as task mastery increases through more data, easier tasks, or stronger priors, and for a pretrained vision-language-action model the trend becomes effectively monotonic decreasing. Practically, H_G enables fast pre-training auditing of demonstration datasets and offers a simple guideline for calibrating demonstrations toward the learnable regime.

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
- Source ID: http://arxiv.org/abs/2606.20871v1
- Link: http://arxiv.org/abs/2606.20871v1
