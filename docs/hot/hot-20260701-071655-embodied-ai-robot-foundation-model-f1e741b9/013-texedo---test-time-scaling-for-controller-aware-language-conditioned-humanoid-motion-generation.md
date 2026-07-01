---
title: "TEXEDO : Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation"
authors: "Jianuo Cao, Yuxin Chen, Yuzhen Song, Masayoshi Tomizuka, Chenran Li, Thomas Tian"
date: "2026-06-22"
pdf: "https://arxiv.org/pdf/2606.22998v2"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=agility robotics; query=(all:\"Agility Robotics\" OR all:\"Unitree\" OR all:\"Apptronik\" OR all:\"1X Technologies\" OR all:\"Sanctuary AI\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "Text-conditioned motion generation is a promising interface for programming humanoid robots, yet current generators are often trained on human motion datasets retargeted to robot morphologies. Although such data provides rich semantic and kinematic priors, it fails to capture the nuances of whole-body tracking controllers, including balance, contact dynamics, actuation limits, and controller-specific failure modes. As a result, generated motions can be semantically plausible but difficult or impossible for the robot to execute. We introduce TEXEDO, a test-time scaling framework for humanoid motion generation that improves motion quality without requiring a stronger underlying generator. Given a text prompt, TEXEDO samples multiple candidate motions from a pretrained text-conditioned generator and selects the best motion that is both executable and task-aligned. The reward model combines a dynamic feasibility verifier, distilled from whole-body tracking rollouts to predict physical executability, with a semantic alignment verifier that measures text-motion alignment in a learned co-embedding space. Our pipeline treats dynamic feasibility as a hard constraint and semantic alignment as the selection objective within the feasible set. Through large-scale simulation studies and real-world deployment on a Unitree G1 humanoid robot, we show that TEXEDO consistently improves both tracking fidelity and text alignment. These results demonstrate that grounded verification is an effective path toward deployable language-guided humanoid motion generation. Project website: https://jianuocao.github.io/TEXEDO/"
---

## 摘要

Text-conditioned motion generation is a promising interface for programming humanoid robots, yet current generators are often trained on human motion datasets retargeted to robot morphologies. Although such data provides rich semantic and kinematic priors, it fails to capture the nuances of whole-body tracking controllers, including balance, contact dynamics, actuation limits, and controller-specific failure modes. As a result, generated motions can be semantically plausible but difficult or impossible for the robot to execute. We introduce TEXEDO, a test-time scaling framework for humanoid motion generation that improves motion quality without requiring a stronger underlying generator. Given a text prompt, TEXEDO samples multiple candidate motions from a pretrained text-conditioned generator and selects the best motion that is both executable and task-aligned. The reward model combines a dynamic feasibility verifier, distilled from whole-body tracking rollouts to predict physical executability, with a semantic alignment verifier that measures text-motion alignment in a learned co-embedding space. Our pipeline treats dynamic feasibility as a hard constraint and semantic alignment as the selection objective within the feasible set. Through large-scale simulation studies and real-world deployment on a Unitree G1 humanoid robot, we show that TEXEDO consistently improves both tracking fidelity and text alignment. These results demonstrate that grounded verification is an effective path toward deployable language-guided humanoid motion generation. Project website: https://jianuocao.github.io/TEXEDO/

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
- Source ID: http://arxiv.org/abs/2606.22998v2
- Link: http://arxiv.org/abs/2606.22998v2
