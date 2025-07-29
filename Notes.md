Seems to have several ways of executing eagle:

Several backend -> flashinfer, flashinfer-mla(doesn't support topk > 1) ...

using cuda graph or not
-> if yes it uses EAGLEDraftCudaGraphRunner

-> if not (can_cuda_graph == false)
    then directly init and call the backend without using (replaying) a cuda graph

### Summary of files:

#### Main Worker Classes

- python/sglang/srt/speculative/eagle_worker.py (980 lines)
    - Role: EAGLE worker implementation
    - Key Features: Draft generation, verification, tree building, CUDA graph optimization

#### Core Utilities
- python/sglang/srt/speculative/eagle_utils.py (1275 lines)
    - Role: Core EAGLE data structures and utilities
    - Key Classes: EagleDraftInput, EagleVerifyInput, EagleVerifyOutput
    - Key Functions: Token verification, tree traversal, grammar support, KV cache management
- python/sglang/srt/speculative/build_eagle_tree.py (428 lines)
    - Role: Tree construction and traversal for speculative decoding
    - Key Functions: build_tree_kernel_efficient(), tree mask generation, efficient tree building

#### CUDA Graph Optimization
- python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py (365 lines)
    - Role: CUDA graph capture and replay for draft model inference
    - Key Features: Pre-captured computation graphs for repeated operations
- python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py (379 lines)
    - Role: CUDA graph optimization for draft model extension operations
    - Key Features: Optimized extend operations after verification

#### Model Implementations
- python/sglang/srt/models/llama_eagle.py (150 lines)
    - Role: LLaMA model adapted for EAGLE speculative decoding
    - Key Features: Modified decoder layers, concatenated hidden states
- python/sglang/srt/models/llama_eagle3.py (250 lines)
    - Role: EAGLE3 model implementation with enhanced features
    - Key Features: Advanced EAGLE3 optimizations
- python/sglang/srt/models/qwen2_eagle.py (147 lines)
    - Role: Qwen2 model adapted for EAGLE speculative decoding
    - Key Features: Qwen2-specific EAGLE implementation

#### CUDA Kernels
- sgl-kernel/csrc/speculative/eagle_utils.cu (308 lines)
    - Role: CUDA kernel implementations for EAGLE operations
    - Key Functions: Tree building, token verification, efficient memory operations

#### Configuration
- python/sglang/srt/speculative/spec_info.py (28 lines)
    - Role: Speculative algorithm configuration and enums
    - Key Features: Algorithm type definitions