---
title: "RGB: RL Guided Whole-Body MPPI for Humanoid Control"
authors: "Yunsoo Seo, Sol Choi, Euncheol Im, Myo Taeg Lim, Yisoo Lee"
date: "2026-06-23"
pdf: "https://arxiv.org/pdf/2606.25123v1"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=agility robotics; query=(all:\"Agility Robotics\" OR all:\"Unitree\" OR all:\"Apptronik\" OR all:\"1X Technologies\" OR all:\"Sanctuary AI\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "Humanoid robots require whole-body controllers that are both robust and precise in contact-rich environments. While deep reinforcement learning (RL) achieves robust stability, its behavior is tightly coupled to the training objective and command interface, making it difficult to add new feedback objectives without retraining. In this study, we propose an RL guided whole-body model predictive path integral (MPPI) framework that acts as an add-on feedback controller on top of a pretrained RL policy. Instead of using RL policy as the final controller, we use it as a sampling prior that biases MPPI rollouts toward dynamically feasible behaviors. Task objectives are specified through modular MPPI cost terms, and MPPI closes the loop by continuously correcting the RL prior online to satisfy these objectives without retraining the policy. Simulations on a 29-DoF Unitree G1 humanoid in MuJoCo demonstrate stable high-rate control (average 280~Hz). The proposed method improves task-level precision over a pure RL baseline under the same command interface. This is achieved by correcting systematic drift during straight walking and tracking additional whole-body reference signals imposed through the cost."
---

## 摘要

Humanoid robots require whole-body controllers that are both robust and precise in contact-rich environments. While deep reinforcement learning (RL) achieves robust stability, its behavior is tightly coupled to the training objective and command interface, making it difficult to add new feedback objectives without retraining. In this study, we propose an RL guided whole-body model predictive path integral (MPPI) framework that acts as an add-on feedback controller on top of a pretrained RL policy. Instead of using RL policy as the final controller, we use it as a sampling prior that biases MPPI rollouts toward dynamically feasible behaviors. Task objectives are specified through modular MPPI cost terms, and MPPI closes the loop by continuously correcting the RL prior online to satisfy these objectives without retraining the policy. Simulations on a 29-DoF Unitree G1 humanoid in MuJoCo demonstrate stable high-rate control (average 280~Hz). The proposed method improves task-level precision over a pure RL baseline under the same command interface. This is achieved by correcting systematic drift during straight walking and tracking additional whole-body reference signals imposed through the cost.

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
- Source ID: http://arxiv.org/abs/2606.25123v1
- Link: http://arxiv.org/abs/2606.25123v1
