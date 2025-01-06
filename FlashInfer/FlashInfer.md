# FlashInfer - An Efficient and Customizable Attention Engine for LLM Inference

## 1. Introduction & Motivation

### Core Problem:
Large Language Models (LLMs) rely heavily on the attention mechanism, which is computationally intensive, especially during inference (serving). As LLMs grow, efficient GPU attention kernels are critical for low latency and high throughput.

### Challenges in LLM Serving:
- **Workload Diversity:** LLM serving involves diverse attention patterns (prefill, batched decoding, prefix reuse, tree decoding), variable query lengths, and KV-caches. A static solution cannot handle this variability.
- **Hardware Heterogeneity:** Modern GPUs need customized attention operators to fully utilize memory and compute capabilities. Efficient storage formats (paged attention, radix trees) and hardware-specific pipelines are required. There is a growing need to accommodate diverse attention mechanisms in modern LLMs such as grouped attention heads, specialized masks, and custom score calculations.

### FlashInfer Solution:
FlashInfer is presented as a customizable and efficient attention engine specifically designed for LLM serving. It addresses these challenges through:
1. **Unified KV-Cache Format:** Uses a block-sparse format for handling diverse KV-cache storage, optimizing memory access, and reducing redundancy.
2. **Customizable Attention Template:** Allows adaptation to different attention variants using Just-In-Time (JIT) compilation.
3. **Dynamic Scheduling:** A load-balanced algorithm adjusts to dynamic user requests while remaining compatible with CUDAGraph, which requires static configurations.
4. **Integration:** FlashInfer is designed to integrate into existing LLM serving frameworks such as SGLang, vLLM, and MLC-Engine.

### Key Results:
FlashInfer demonstrates significant performance boosts in various scenarios:
- Up to **69% inter-token latency reduction** compared to compiler backends.
- Up to **30% latency reduction** for long-context inference.
- **17% speedup** for LLM serving with parallel generation.

### Key Contributions:
1. **Flexible block-sparse and composable formats** addressing KV-Cache storage heterogeneity for efficient memory management and access.
2. Development of a **customizable attention template** accommodating diverse attention variants, ensuring high-performance execution via JIT compilation.
3. Design of a **dynamic scheduling framework** managing input dynamism while remaining compatible with CUDAGraph, maximizing hardware utilization.
4. Comprehensive evaluation demonstrating substantial improvements in kernel and end-to-end performance.

## 2. Background

### FlashAttention:
FlashInfer builds upon FlashAttention (and later FlashAttention2 & 3), which reduce memory usage during the forward pass by avoiding materializing the full attention matrix in GPU global memory. FlashAttention's operational intensity is proportional to the query length, further improved by Grouped Query Attention (GQA).

### Attention Composition:
FlashInfer adopts the "Attention State" concept, a tuple of attention output and attention scale, allowing for associative and commutative partial-attention computations. This reduces memory usage and improves hardware efficiency.

### Block/Vector Sparsity:
FlashInfer utilizes Block Compressed Sparse Row (BSR) format. This format groups non-zero elements into contiguous matrices, improving register reuse efficiency and compatibility with GPU hardware matrix multiplication units.

## 3. FlashInfer Design

### Unified KV-Cache Storage (Block-Sparse Matrix):
- FlashInfer uses Block-Sparse Row (BSR) to represent paged attention, radix trees, and other sparse attention mechanisms.
- **Query and output matrices** are efficiently stored as ragged tensors without padding to support compact packing.
- BSR with adjustable block sizes offers fine-grained sparsity control.

### Composable Formats:
FlashInfer decomposes the KV-cache into multiple BSR formats based on prior knowledge, improving memory access efficiency.

### Compute Abstraction (CUDA/CUTLASS):
- Includes optimizations such as enhanced loading of sparse tiles into shared memory and configurable tile sizes.
- Supports efficient LDGSTS instructions for 128B width to maximize memory bandwidth.

### JIT Compiler for Attention Variants:
- Provides a customizable programming interface for implementing attention variants.
- Uses JIT compilation to generate highly optimized block-sparse implementations.

### Dynamism-Aware Runtime:
- **Load-Balanced Scheduling:** Minimizes SM idle time by evenly distributing workloads.
- **CUDAGraphs Compatibility:** Attention and contraction kernels use persistent kernel with fixed grid sizes for performance optimization.

## 4. Evaluation

### End-to-End LLM Serving:
- Compared with Triton and TensorRT-LLM using ShareGPT and synthetic datasets.
- Results: Consistent ITL speedup, competitive performance on variable workloads, and reduced end-to-end latency.

### Kernel Performance (Input Dynamism):
- Dynamic scheduler outperforms FlashAttention under uniform and skewed sequence length distributions.

### Customizability (Long-Context Inference):
- Reduced end-to-end latency by up to **30%** with specialized fused kernels.

### Composable Formats for Parallel Generation:
- Consistent speedups for parallel degrees between 4 and 32.

## 5. Related Work
FlashInfer builds on prior work in attention optimization, including FlashAttention, FlashDecoding, and LeanAttention. It integrates with existing LLM serving systems like Orca and SGLang.

## 6. Conclusion & Future Work
FlashInfer addresses the challenges of workload variability, hardware heterogeneity, and memory access bottlenecks in LLM serving. Future directions include:
- Compiling higher-level DSLs to attention specifications.
- Exploring deterministic turnstile accumulation.
- Enhancing sparse gathering with TMA for large block sizes.

## 7. Appendix Highlights
- **Head Group Fusion:** Optimized mapping for grouped-query attention.
- **Memory Management:** Efficient handling of page-locked host and device workspace buffers.
- **FP8-FP16 Mixed Precision:** Mixed precision attention kernels for reduced memory usage.
