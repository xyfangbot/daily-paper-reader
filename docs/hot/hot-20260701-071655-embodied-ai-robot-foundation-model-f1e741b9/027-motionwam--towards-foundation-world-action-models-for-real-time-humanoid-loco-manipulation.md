---
title: "MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation"
authors: "Jia Zheng, Teli Ma, Yudong Fan, Zifan Wang, Shuo Yang, Junwei Liang"
date: "2026-06-08"
pdf: "https://arxiv.org/pdf/2606.09215v1"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=agility robotics; query=(all:\"Agility Robotics\" OR all:\"Unitree\" OR all:\"Apptronik\" OR all:\"1X Technologies\" OR all:\"Sanctuary AI\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "World Action Models (WAMs) couple a video dynamics prior to the policy and have shown encouraging results on tabletop manipulation, but iterative denoising over high-dimensional video-action latents leaves them too slow for real-time humanoid loco-manipulation. The problem is compounded by the dominant hierarchical paradigm, in which a high-level manipulation policy controls only the upper body while a low-level controller tracks coarse base commands -- placing upper and lower body in inconsistent action spaces and reducing the legs to balance-preserving locomotion. We present MotionWAM, a real-time WAM that drives autonomous humanoid loco-manipulation from a single egocentric camera by conditioning the policy on the intermediate denoising features of a video world model. MotionWAM replaces the upper-lower split with a unified motion latent and predicts whole-body motion tokens that jointly cover locomotion, torso motion, height regulation, foot interaction, and hand manipulation in a single action space. A three-stage learning framework progressively adapts the video world model to egocentric visual dynamics and to the target humanoid embodiment. On nine real-world Unitree G1 tasks, MotionWAM runs in real time, substantially outperforms Vision-Language-Action (VLA) baselines fine-tuned on the same demonstrations by over 30% in overall success rate, and executes task-driven foot interaction that decoupled upper-lower policies cannot reach. Our results suggest that video-pretrained WAMs can be lifted from tabletop manipulation to coordinated, human-like whole-body humanoid control."
---

## 摘要

World Action Models (WAMs) couple a video dynamics prior to the policy and have shown encouraging results on tabletop manipulation, but iterative denoising over high-dimensional video-action latents leaves them too slow for real-time humanoid loco-manipulation. The problem is compounded by the dominant hierarchical paradigm, in which a high-level manipulation policy controls only the upper body while a low-level controller tracks coarse base commands -- placing upper and lower body in inconsistent action spaces and reducing the legs to balance-preserving locomotion. We present MotionWAM, a real-time WAM that drives autonomous humanoid loco-manipulation from a single egocentric camera by conditioning the policy on the intermediate denoising features of a video world model. MotionWAM replaces the upper-lower split with a unified motion latent and predicts whole-body motion tokens that jointly cover locomotion, torso motion, height regulation, foot interaction, and hand manipulation in a single action space. A three-stage learning framework progressively adapts the video world model to egocentric visual dynamics and to the target humanoid embodiment. On nine real-world Unitree G1 tasks, MotionWAM runs in real time, substantially outperforms Vision-Language-Action (VLA) baselines fine-tuned on the same demonstrations by over 30% in overall success rate, and executes task-driven foot interaction that decoupled upper-lower policies cannot reach. Our results suggest that video-pretrained WAMs can be lifted from tabletop manipulation to coordinated, human-like whole-body humanoid control.

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
- Source ID: http://arxiv.org/abs/2606.09215v1
- Link: http://arxiv.org/abs/2606.09215v1
