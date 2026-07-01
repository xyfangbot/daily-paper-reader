---
title: "Energy-Efficient Arm Reaching for a Humanoid Robot via Deep Reinforcement Learning with Identified Power Models"
authors: "Nestor N. Deniz, Simon Parsons, Fernando Auat Cheein"
date: "2026-06-14"
pdf: "https://arxiv.org/pdf/2606.15918v1"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=agility robotics; query=(all:\"Agility Robotics\" OR all:\"Unitree\" OR all:\"Apptronik\" OR all:\"1X Technologies\" OR all:\"Sanctuary AI\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "Humanoid robots performing in-field manipulation tasks, such as robotic apple harvesting, face severe energy constraints that directly limit the number of reaching motions that can be executed per battery charge. This paper presents an end-to-end, energy-aware reinforcement learning framework for the 7-degree-of-freedom left arm of the Unitree~G1 humanoid robot, combining a physics-based, experimentally identified electrical power model with a Soft Actor-Critic (SAC) policy trained in a Pinocchio-based rigid-body dynamics simulator. The RL policy operates on an incremental joint-position action space and is trained with a Hybrid Constellation Reward that combines a four-point end-effector constellation distance with a torque-norm energy proxy; after % $5\\times10^6$ training it reaches a $69.9\\%$ success rate over $1\\,000$ random targets in kinematic simulation, at a mean energy of \\SI{98.16}{\\joule} on successful episodes. Finally, on the physical Unitree~G1, the policy is validated over three independent 10-target batches, achieving a mean energy of $71.5 \\pm 48.3$\\,J, an end-effector position error of $2.64 \\pm 1.04$\\,cm, and an orientation error of $6.92 \\pm 1.33^\\circ$ -- within the \\SI{4}{\\centi\\metre}/$8.6^\\circ$ training tolerance. These results constitute a first step toward energy-aware reinforcement-learning-based arm reaching for humanoid robots."
---

## 摘要

Humanoid robots performing in-field manipulation tasks, such as robotic apple harvesting, face severe energy constraints that directly limit the number of reaching motions that can be executed per battery charge. This paper presents an end-to-end, energy-aware reinforcement learning framework for the 7-degree-of-freedom left arm of the Unitree~G1 humanoid robot, combining a physics-based, experimentally identified electrical power model with a Soft Actor-Critic (SAC) policy trained in a Pinocchio-based rigid-body dynamics simulator. The RL policy operates on an incremental joint-position action space and is trained with a Hybrid Constellation Reward that combines a four-point end-effector constellation distance with a torque-norm energy proxy; after % $5\times10^6$ training it reaches a $69.9\%$ success rate over $1\,000$ random targets in kinematic simulation, at a mean energy of \SI{98.16}{\joule} on successful episodes. Finally, on the physical Unitree~G1, the policy is validated over three independent 10-target batches, achieving a mean energy of $71.5 \pm 48.3$\,J, an end-effector position error of $2.64 \pm 1.04$\,cm, and an orientation error of $6.92 \pm 1.33^\circ$ -- within the \SI{4}{\centi\metre}/$8.6^\circ$ training tolerance. These results constitute a first step toward energy-aware reinforcement-learning-based arm reaching for humanoid robots.

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
- Source ID: http://arxiv.org/abs/2606.15918v1
- Link: http://arxiv.org/abs/2606.15918v1
