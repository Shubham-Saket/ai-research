# Search-o1: Agentic Search-Enhanced Large Reasoning Models

## 1. Introduction & Problem Statement

### Context
The document focuses on Large Reasoning Models (LRMs), such as OpenAI's o1, which demonstrate impressive abilities in stepwise reasoning through large-scale reinforcement learning.

### Problem
- LRMs excel at logical coherence and breaking down complex problems, but their extended reasoning chains often suffer from **"knowledge insufficiency."**
- This results in frequent uncertainties and errors when LRMs lack the required knowledge within their parameters.

### Evidence of the Problem
- LRMs frequently decode "uncertain terms" like "perhaps" during reasoning, highlighting knowledge gaps.
- On average, "perhaps" appears over **30 times in a single reasoning process.**

### Challenges
- Incorporating retrieved documents disrupts reasoning coherence due to redundancy and LRMs' limited ability to process long contexts.
- Extended reasoning chains can lead to **overthinking** and error propagation due to knowledge gaps.

---

## 2. Proposed Solution: Search-o1 Framework

### Core Idea
Search-o1 enhances LRMs by integrating:
1. **Agentic Retrieval-Augmented Generation (RAG)**: Allows autonomous external knowledge retrieval during reasoning.
2. **Reason-in-Documents Module**: Refines retrieved knowledge for seamless integration into the reasoning chain.

### Agentic RAG
- The model generates search queries using special symbols `<|begin_search_query|>` and `<|end_search_query|>`.
- Relevant documents are retrieved and inserted into the reasoning process, enclosed in `<|begin_search_result|>` and `<|end_search_result|>`.

### Knowledge Refinement (Reason-in-Documents Module)
- Extracts concise and relevant information from retrieved documents.
- Ensures the logical flow of reasoning remains intact by integrating refined knowledge back into the chain.

---

## 3. Methodology Details

### Problem Formulation
Goal: Generate a logical reasoning chain (R) and final answer (a) by integrating:
- **Task Instructions (I)**  
- **Question (q)**  
- **Retrieved Documents (D)**  
`(I, q, D) → (R, a)`

### Inference Process
1. **Single Question**:  
   - Model generates reasoning steps and search queries when uncertainty arises.  
   - Retrieved documents are refined and reintegrated into the reasoning process.
2. **Batch Inference**:  
   - Batch processing optimizes token generation and knowledge refinement.

### Mathematical Formulation
- The reasoning process is expressed as a series of conditional probabilities:  
  `P(R, a | I, q, D) = ...` (Detailed in Section 3.1 of the paper).

---

## 4. Experimental Setup

### Datasets
- **Complex Reasoning Tasks**: GPQA, MATH500, AMC2023, AIME2024, LiveCodeBench.  
- **Open-Domain QA Tasks**: NQ, TriviaQA, HotpotQA, 2WikiMultihopQA, MuSiQue, Bamboogle.

### Baselines
- **Direct Reasoning** (no retrieval).  
- **Standard RAG** (retrieves documents based on the initial question).  
- **RAgent** (agentic retrieval without refinement).

### Model
- Implemented using the **QwQ-32B-Preview model** as the backbone LRM.

---

## 5. Key Results

1. **Superior Performance**:  
   - Significant improvements across reasoning and multi-hop QA tasks.
2. **Agentic Retrieval Effectiveness**:  
   - Outperforms standard RAG by dynamically addressing uncertainties.
3. **Reason-in-Documents Impact**:  
   - Maintains reasoning coherence while integrating relevant external knowledge.
4. **Scaling with Retrieved Documents**:  
   - Performs effectively with increasing document counts, often surpassing baselines.
5. **Human-Level Performance**:  
   - Matches or exceeds human experts in certain domains.

---

## 6. Conclusion

### Significance
Search-o1 addresses the **knowledge insufficiency** of LRMs by dynamically retrieving and refining external knowledge, enhancing reasoning accuracy and coherence.

### Impact
This framework enables the development of more reliable and versatile AI systems capable of solving complex problems.

---

## 7. Key Takeaways

- LRMs require external knowledge to tackle complex reasoning tasks.  
- Simple RAG is insufficient; **agentic retrieval** improves performance but introduces noise.  
- **Reason-in-Documents refinement** is essential for coherent reasoning.  
- The combination of **agentic retrieval** and **refined document injection** (Search-o1) significantly boosts performance in complex tasks.
