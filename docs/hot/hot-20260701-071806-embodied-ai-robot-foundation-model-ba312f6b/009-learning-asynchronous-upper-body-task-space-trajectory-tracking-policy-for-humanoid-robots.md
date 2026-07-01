---
title: "Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots"
authors: "Yumeng Liu, Dongqi Wang, Jiyu Yu, Yijun Fan, Rong Xiong, Yue Wang"
date: "2026-06-24"
pdf: "https://arxiv.org/pdf/2606.25706v1"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=agility robotics; query=(all:\"Agility Robotics\" OR all:\"Unitree\" OR all:\"Apptronik\" OR all:\"1X Technologies\" OR all:\"Sanctuary AI\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "High-level humanoid planners often output sparse task-space, low-rate trajectories, whereas whole-body controllers run at high frequency. This creates temporal asynchrony between the planning and execution, and structural incompleteness for full-body control. We propose an asynchronous upper body task-space tracking framework for humanoids. A student policy is initialized by teacher-student distillation, conditioned on the full cached future trajectory and an execution-time index, and trained with a sliding-window global reward to reduce frame drift without explicit frame estimation. For task-specific post-training, an MPC module completes sparse references into floating-base and upper-body guidance, while action- and FK level self-guidance constrain policy drift. Simulation and Unitree G1 hardware experiments show improved tracking under low update rates, stronger performance than synchronous and decoupled baselines, and safer adaptation to out-of-distribution motions."
---

## 摘要

High-level humanoid planners often output sparse task-space, low-rate trajectories, whereas whole-body controllers run at high frequency. This creates temporal asynchrony between the planning and execution, and structural incompleteness for full-body control. We propose an asynchronous upper body task-space tracking framework for humanoids. A student policy is initialized by teacher-student distillation, conditioned on the full cached future trajectory and an execution-time index, and trained with a sliding-window global reward to reduce frame drift without explicit frame estimation. For task-specific post-training, an MPC module completes sparse references into floating-base and upper-body guidance, while action- and FK level self-guidance constrain policy drift. Simulation and Unitree G1 hardware experiments show improved tracking under low update rates, stronger performance than synchronous and decoupled baselines, and safer adaptation to out-of-distribution motions.

## 领衔机构

- agility robotics

## 机构

- agility robotics

## 来源信息

- Citations: 0
- Source: arXiv fallback
- Matched query: (all:"Agility Robotics" OR all:"Unitree" OR all:"Apptronik" OR all:"1X Technologies" OR all:"Sanctuary AI") AND (all:"embodied AI" OR all:"robot foundation model" OR all:"vision-language-action model" OR all:"humanoid robot" OR all:"embodied intelligence" OR all:"vision-language-action" OR all:"robot learning" OR all:"physical AI")
- Company match: agility robotics
- DOI: 
- Source ID: http://arxiv.org/abs/2606.25706v1
- Link: http://arxiv.org/abs/2606.25706v1
