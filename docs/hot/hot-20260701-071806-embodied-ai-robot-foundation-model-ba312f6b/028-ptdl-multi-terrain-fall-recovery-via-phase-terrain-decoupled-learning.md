---
title: "PTDL:Multi-Terrain Fall Recovery via Phase-Terrain Decoupled Learning"
authors: "Xiaoyu Xu, Zhiming Chen, Yuenan Zhao, Ran Song, Wei Zhang"
date: "2026-06-08"
pdf: "https://arxiv.org/pdf/2606.08922v1"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=agility robotics; query=(all:\"Agility Robotics\" OR all:\"Unitree\" OR all:\"Apptronik\" OR all:\"1X Technologies\" OR all:\"Sanctuary AI\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "Humanoid robots can fall on slopes, gravel, and uneven ground in unstructured environments. We target integrated fall recovery and locomotion: rebuilding balance from a fallen state using proprioception alone and resuming velocity-commanded walking at the fall site. Prior methods often stop at quasi-static rise, neglect the post-fall ground-contact phase, or, when trained on mixed terrains without separating recovery and locomotion phases or per-surface constraints, collapse to a single compromise get-up across surfaces. We propose Phase--Terrain Decoupled Learning (PTDL), which decouples training supervision along phase and terrain axes while deploying one proprioceptive policy. On the phase axis, projected-gravity-gated dual motion-prior discriminators and a probe-to-walk transition link post-fall recovery to commanded walking. On the terrain axis, terrain-stratified recovery shaping assigns surface-specific training supervision on flat ground, gravel, and slopes; terrain labels are training-only and withheld from policy observations, enabling implicit post-fall strategy selection at deployment. We validate PTDL on a 29-DoF Unitree G1 across flat ground, gravel, and slopes up to 20 degrees in simulation and on hardware, achieving stable cross-terrain recovery, smooth recovery-to-locomotion transitions, and differentiated post-fall rise behaviors under one deployed policy."
---

## 摘要

Humanoid robots can fall on slopes, gravel, and uneven ground in unstructured environments. We target integrated fall recovery and locomotion: rebuilding balance from a fallen state using proprioception alone and resuming velocity-commanded walking at the fall site. Prior methods often stop at quasi-static rise, neglect the post-fall ground-contact phase, or, when trained on mixed terrains without separating recovery and locomotion phases or per-surface constraints, collapse to a single compromise get-up across surfaces. We propose Phase--Terrain Decoupled Learning (PTDL), which decouples training supervision along phase and terrain axes while deploying one proprioceptive policy. On the phase axis, projected-gravity-gated dual motion-prior discriminators and a probe-to-walk transition link post-fall recovery to commanded walking. On the terrain axis, terrain-stratified recovery shaping assigns surface-specific training supervision on flat ground, gravel, and slopes; terrain labels are training-only and withheld from policy observations, enabling implicit post-fall strategy selection at deployment. We validate PTDL on a 29-DoF Unitree G1 across flat ground, gravel, and slopes up to 20 degrees in simulation and on hardware, achieving stable cross-terrain recovery, smooth recovery-to-locomotion transitions, and differentiated post-fall rise behaviors under one deployed policy.

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
- Source ID: http://arxiv.org/abs/2606.08922v1
- Link: http://arxiv.org/abs/2606.08922v1
