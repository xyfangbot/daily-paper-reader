---
title: "Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving"
authors: "Liang Su"
date: "2026-06-18"
pdf: "https://arxiv.org/pdf/2606.20537v1"
source: arXiv fallback
selection_source: hot_paper_scout
tags: ["query:具身智能", "paper:arXiv", "paper:Hot", "institution:具身智能公司领衔"]
score: 0
evidence: "arXiv fallback; company_match=google deepmind; query=(all:\"Field AI\" OR all:\"Intrinsic\" OR all:\"Google DeepMind\" OR all:\"NVIDIA\" OR all:\"Tesla\") AND (all:\"embodied AI\" OR all:\"robot foundation model\" OR all:\"vision-language-action model\" OR all:\"humanoid robot\" OR all:\"embodied intelligence\" OR all:\"vision-language-action\" OR all:\"robot learning\" OR all:\"physical AI\")"
abstract: "Mainstream LLM serving systems reuse prefix work mainly through paged or radix key-value (KV) caches. This is highly effective for high-throughput, high-concurrency serving, but it manages only one positional fragment of execution state: the KV cache. We study the opposite regime: low-latency, small-batch, on-device physical-AI serving, where interactive LLM agents, speech systems, and robot policies repeatedly branch, reset, interrupt, and re-enter under tight responsiveness budgets. We introduce execution-state capsules, a graph-bound checkpoint and restore mechanism for the complete restorable state at a committed boundary. FlashRT is a white-box, backend-facing kernel runtime whose evaluated NVIDIA CUDA backend runs captured graph plans over contiguous static buffers with no block-table indirection. Because the live state is a closed set of named buffers, a capsule can snapshot, restore, fork, or roll back the whole execution boundary, including KV, recurrent state, convolution state, MTP state, and metadata. This moves reuse from token-addressed KV fragments to graph-bound execution-state boundaries. On an RTX 5090, capsule restore is byte-exact at the stored-state level and token-identical under greedy decode. A KV-only ablation diverges, showing that recurrent state is load-bearing. GPU-resident snapshot and restore are sub-millisecond, and TTFT speedup over cold prefill grows from 3.9x at 2k tokens to 27x at 16k tokens. On Jetson AGX Thor and DGX Spark, the same correctness and structural properties hold. Capsules are not a replacement for high-throughput KV-cache serving; they define a complementary latency-first serving point for explicit execution-state reuse."
---

## 摘要

Mainstream LLM serving systems reuse prefix work mainly through paged or radix key-value (KV) caches. This is highly effective for high-throughput, high-concurrency serving, but it manages only one positional fragment of execution state: the KV cache. We study the opposite regime: low-latency, small-batch, on-device physical-AI serving, where interactive LLM agents, speech systems, and robot policies repeatedly branch, reset, interrupt, and re-enter under tight responsiveness budgets. We introduce execution-state capsules, a graph-bound checkpoint and restore mechanism for the complete restorable state at a committed boundary. FlashRT is a white-box, backend-facing kernel runtime whose evaluated NVIDIA CUDA backend runs captured graph plans over contiguous static buffers with no block-table indirection. Because the live state is a closed set of named buffers, a capsule can snapshot, restore, fork, or roll back the whole execution boundary, including KV, recurrent state, convolution state, MTP state, and metadata. This moves reuse from token-addressed KV fragments to graph-bound execution-state boundaries. On an RTX 5090, capsule restore is byte-exact at the stored-state level and token-identical under greedy decode. A KV-only ablation diverges, showing that recurrent state is load-bearing. GPU-resident snapshot and restore are sub-millisecond, and TTFT speedup over cold prefill grows from 3.9x at 2k tokens to 27x at 16k tokens. On Jetson AGX Thor and DGX Spark, the same correctness and structural properties hold. Capsules are not a replacement for high-throughput KV-cache serving; they define a complementary latency-first serving point for explicit execution-state reuse.

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
- Source ID: http://arxiv.org/abs/2606.20537v1
- Link: http://arxiv.org/abs/2606.20537v1
