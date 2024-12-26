# Lyra: Efficient Multi-Modality Integration in Omni-Cognition

The paper introduces innovative methodologies for multi-modal integration, particularly leveraging formulas and mathematical strategies. Below are key formulas and concepts used in Lyra:
Challenges Addressed:

Limited Speech Integration: Existing omni-models often overlook the integration of speech with other modalities, leading to suboptimal performance in speech-related tasks.

High Training Costs: Developing comprehensive MLLMs typically requires substantial computational resources and extensive datasets.

Long-Context Processing: Handling long speech inputs and maintaining coherence across extended contexts remain challenging for current models.

Proposed Solutions and Techniques:

Leveraging Open-Source Models with Multi-Modality LoRA:

Lyra utilizes existing open-source large models combined with a proposed multi-modality Low-Rank Adaptation (LoRA) technique.
This approach reduces training costs and data requirements by adapting pre-trained models to handle multiple modalities efficiently.
Latent Multi-Modality Regularizer and Extractor:

A latent multi-modality regularizer is employed to strengthen the relationships between speech and other modalities.
This technique enhances model performance by ensuring coherent integration across different types of data inputs.
High-Quality Extensive Dataset:

The construction of a comprehensive dataset comprising 1.5 million multi-modal (language, vision, audio) samples and 12,000 long speech samples.
This dataset enables Lyra to effectively handle complex, long speech inputs and achieve robust omni-cognition.
Performance and Efficiency:

Lyra achieves state-of-the-art results across various benchmarks, including vision-language, vision-speech, and speech-language tasks.
It operates with fewer computational resources and less training data compared to other omni-models, enhancing its suitability for latency-sensitive and long-context multi-modality applications.

Most of the speech or video tokens are not relevant to text token hence the Latent Multimodality extractor. 
Concretely, insteadof applying this strategy toevery layer, they implemented a block-based manner. Suppose the LLM consists of mn layers; divide them into blocks of
 m layers each, resulting in n blocks. At the final layer of each block,we apply our following information extraction
 strategy,which evaluates the similarity between the attention scores of tokens from each modality and the question text tokens.

There is a growing trend toward processing longer single-modality content, such as long text and long video, in Multi-modal Large Language Models (MLLMs). However, current MLLMs struggle with long speech due to limitations in speech encoders. Models like Intern-Omni, VITA, and LLaMA-Omni, which use Whisper-like encoders, can only process short audio inputs (around 30 seconds), while more complex encoders can handle up to one minute. The main challenge lies in the lack of long speech datasets and proper preprocessing methods.
To address this, the paper introduces the first Speech Fine-Tuning (SFT) dataset for long speech understanding. This dataset consists of approximately 12,000 long-form audio recordings (ranging from several minutes to two hours) sourced from diverse YouTube content, including interviews, speeches, and informational videos. The recordings cover a wide range of topics, such as humanities, current events, technology, and society. These audio files were paired with related transcripts, and question-answer pairs were generated using a Large Language Model (LLM) to encourage a comprehensive understanding of long speech content.
A key challenge in processing long speech was the limitation of the speech encoder. Inspired by image segmentation methods like LLaVA-NeXT, a new approach was adopted to improve the encoder's handling of long audio. For instance, a 30-second audio clip encoded by the Whisper-v3 encoder results in 1,500 tokens, but for a two-hour audio clip, this would lead to 360,000 tokens, which is beyond typical processing capacity. To manage this, compression techniques were applied to speech tokens.
Experimental results showed that a higher number of tokens improved performance up to a certain point, but beyond that, the gains were limited. Balancing computational cost and performance, the model was optimized to handle long speech cases using 300 compressed tokens.

## 1. Low-Rank Adaptation (LoRA) for Multi-Modality
LoRA optimizes pretrained models for new tasks without updating all model parameters. In Lyra, it adapts the model for multi-modality.

### Formula for LoRA Adaptation:
\[
W' = W + \Delta W \quad \text{where} \quad \Delta W = A \cdot B
\]
- \( W \): Original weight matrix of the pretrained model.
- \( \Delta W \): Low-rank update matrix.
- \( A \): Matrix of size \( d \times r \) (rank-reduced transformation).
- \( B \): Matrix of size \( r \times k \) (low-dimensional projection).

By keeping \( r \) small, the number of parameters is significantly reduced, ensuring efficient adaptation for vision, speech, and language modalities.

## 2. Latent Multi-Modality Regularizer
This regularizer enforces the alignment between modalities like speech, vision, and language in a shared latent space. The aim is to minimize the discrepancy across modalities.

### Formula for Regularization:
\[
\mathcal{L}_{\text{reg}} = \frac{1}{N} \sum_{i=1}^{N} \| f(x_i^{\text{mod1}}) - f(x_i^{\text{mod2}}) \|^2
\]
- \( f \): Encoding function mapping input \( x_i \) to the latent space.
- \( x_i^{\text{mod1}}, x_i^{\text{mod2}} \): Inputs from different modalities (e.g., speech and vision).
- \( N \): Number of training samples.

This loss ensures that embeddings from different modalities are closely aligned, improving multimodal coherence.

## 3. Cross-Modality Attention Mechanism
Lyra integrates speech, vision, and language using a cross-attention mechanism.

### Formula for Attention:
\[
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right) V
\]
- \( Q \): Query matrix derived from one modality (e.g., speech).
- \( K \): Key matrix from another modality (e.g., vision).
- \( V \): Value matrix aligned with \( K \).
- \( d_k \): Dimensionality of \( K \).

This mechanism ensures contextual information from one modality influences the processing of another.

## 4. Long Speech Context Handling
Lyra incorporates a temporal convolutional network (TCN) for efficient long-context processing in speech.

### Formula for TCN Output:
\[
y_t = \sum_{i=0}^{k-1} w_i \cdot x_{t-i}
\]
- \( y_t \): Output at time \( t \).
- \( x_{t-i} \): Input at a time lag \( i \).
- \( w_i \): Weight for the \( i \)-th lag.
- \( k \): Kernel size of the convolution.

The use of dilated convolutions extends the receptive field, enabling the model to capture long-term dependencies in speech.

## 5. Optimization Objective
Lyra combines multiple losses to train the model.

### Total Loss:
\[
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{reg}} + \mathcal{L}_{\text{task-specific}}
\]
- \( \mathcal{L}_{\text{task-specific}} \): Loss specific to downstream tasks (e.g., speech recognition, image captioning).

---

By combining these mathematical approaches, Lyra achieves efficient and robust multimodal cognition.
