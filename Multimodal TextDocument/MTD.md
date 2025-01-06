Multimodal Textbook for Vision-Language Pretraining

1. Introduction

This paper introduces a novel, high-quality multimodal dataset called a "multimodal textbook" designed to enhance Vision-Language Model (VLM) pretraining. The key innovation lies in curating this dataset from a large collection of instructional videos, offering a more natural, coherent, and knowledge-dense alternative to traditional image-text pair datasets and webpage-derived interleaved datasets. The research aims to address the shortcomings of current VLM training data, which often suffers from weak image-text relationships, low knowledge density, and poor logical coherence.

Key Problem Addressed:

Existing image-text paired datasets lack the naturalness and authenticity of comprehensive text corpora, limiting VLMs' in-context learning and chain-of-thought reasoning.
Webpage-centric interleaved datasets, while improving in-context learning, face issues like loose image-text relations, poor sequence logic, and sparse knowledge density.
Instructional videos, a rich and widely used resource for learning, remain underexploited in VLM training.
2. Main Themes and Key Ideas

Video-Centric Approach: The core concept is using instructional videos as the primary source of data. This offers inherent advantages in terms of visual-textual consistency and temporal coherence, making it suitable for creating a textbook-like structure. The authors state, "Compared to common videos, such as entertainment, sports, or TV-show, instructional videos exhibit greater textual-visual consistency and sequential frame coherence, making them ideal for creating a 'multimodal textbook'."
LLM-Driven Curation: The dataset creation process leverages Large Language Models (LLMs) at multiple stages. First, an LLM is used to develop a detailed knowledge taxonomy, guiding the collection of instructional videos. LLMs are also used to filter out low-quality videos based on their metadata and audio transcriptions. This allows for a systematic and automated approach to building the dataset.
Multi-Level Data Extraction and Filtering: A critical part of the pipeline is the multi-level approach for extracting knowledge from the videos:
Video-Level: Filtering low-quality or non-instructional videos using ASR transcripts and metadata analysis, identifying videos that have "Relevance", "Knowledge Density", and "Transcription Quality".
Clip-Level: Segmenting long videos into shorter clips based on ASR timestamps and discarding clips with insufficient visual knowledge, using VideoLlama2 to provide detailed captions for each clip and filtering based on the similarity between these captions and ASR.
Keyframe-Level: Extracting keyframes by comparing consecutive frame differences using the Structural Similarity Index (SSIM), and extracting text (OCR) from the keyframes using InternVL2-40B. This helps to capture the most salient visual content from the videos.
Image-Text Interleaved Format: The extracted keyframes and the corresponding texts (ASR transcripts and OCR text) are organized chronologically, creating an interleaved dataset. This closely aligns visual and textual information, better simulating the learning experience from textbooks. As stated in the paper, "The whole corpus is presented in an image-text interleaved format, where the text and images are more closely aligned, and the logical relations between images are also more coherent."
Knowledge-Rich Content: The multimodal textbook contains over 2.5 years of instructional videos, totaling 22,000 class hours, covering six fundamental subjects, including mathematics, physics, chemistry, earth science, engineering, and computer science. This focus on fundamental subjects aims to impart foundational knowledge to VLMs.
Improved In-Context Learning: VLMs pre-trained on the "textbook" show better in-context learning capabilities, leveraging both visual and textual cues from the provided few-shot examples. The paper states, "VLMs pre-trained on our textbook exhibit outstanding interleaved context awareness, leveraging visual and textual cues in their few-shot context for task solving."
3. Dataset Characteristics

Scale: The dataset comprises 6.5 million images (keyframes) and 0.75 billion text tokens (ASR and OCR) derived from 75,000 instructional videos.
Structure: The data is organized into 610,000 image-text interleaved samples, each containing an average of 10.7 keyframes and 1,297 text tokens.
Coherence: The images within each sample are highly coherent, often illustrating a single concept or process, leading to more than double the In-Sample Image SIML scores compared to other datasets such as MMC4 and OBELICS.
Knowledge Taxonomy: LLM proposed a four-level hierarchical taxonomy with 6 subjects, 55 courses and 3915 knowledge points.
4. Experiments and Results

Baselines: The research used LLaVA-1.5-7B and Idefics2-8B as base models for pretraining. The models were pre-trained on the multimodal textbook and compared against those trained on MMC4, MMC4-core-ff, and OBELICS datasets.
Evaluation Benchmarks: The pre-trained models were evaluated on VQA tasks (TextVQA and OKVQA), visual reasoning benchmarks (MathVista, MathVision, and MathVerse) and the ScienceQA-IMG dataset, covering general, OCR, mathematical, and scientific reasoning.
Key Findings:VLMs pre-trained on the multimodal textbook demonstrated significant improvements across all evaluation benchmarks, showing an average gain of +3.2%, +8.3%, +4.0%, and +4.6% in the 0-shot to 4-shot settings respectively.
The gains are particularly pronounced in knowledge- and reasoning-intensive tasks like ScienceQA and MathVista (+5.3% and +6.4% average improvement compared to OBELICS).
The models showed enhanced in-context learning capabilities.
The paper includes a "cheat test" experiment which clearly validates the effectiveness of the textbook, which resulted in significantly higher performance (+20%) over the MMC4 and OBELICS datasets.
The performance is better even after instruction tuning using a standard dataset, further validating the quality of the pre-training.
5. Ablation Studies

The authors conducted ablation studies to validate design decisions in their video-to-textbook pipeline:

ASR Refinement: Refining ASR transcripts with LLMs is crucial, as using raw ASR leads to a 4.9% performance drop.
OCR Integration: Incorporating OCR text extracted from keyframes is essential, resulting in a 2.3% performance drop without it.
Keyframe Extraction: The choice of keyframe extraction algorithm significantly impacts performance. SSIM based extraction provides superior results compared to pixel level and clip-based extraction.
6. Conclusion

The paper introduces a novel and effective methodology for creating high-quality multimodal pretraining data from instructional videos. The resulting multimodal textbook provides a coherent and knowledge-rich resource that enhances VLMs' in-context learning and reasoning capabilities, particularly in knowledge intensive tasks. The research highlights the benefits of video-centric, interleaved data for advancing VLMs. The authors conclude, "Experiments demonstrate its effectiveness, especially in enhancing VLMs’ in-context learning capabilities."

7. Limitations and Future Work

The authors acknowledge that the dataset may still contain redundant keyframes or low-quality texts despite filtering. They plan on improving the dataset's quality and knowledge density further.
The textbook currently focuses on understanding and text generation but they plan to expand it for omni-modal tasks in future.
8. Key Quotes

"Compared to image-text pair data, interleaved corpora enable Vision-Language Models (VLMs) to understand the world more naturally like humans."
"Our textbook is an openly accessible pre-training dataset with high-quality 6.5 million images interleaving with 0.75 billion texts."
"These more coherent interleaved context and better-aligned image-text sequences enable VLMs to better grasp foundational knowledge during the pretraining."
"Experiments show that VLMs pre-trained on our textbook achieve noticeable improvement on knowledge- and reasoning-intensive benchmarks, like MathVista, and ScienceQA."
"We observe an interesting phenomenon: even on general-domain benchmarks such as OKVQA and TextVQA, our textbook dataset yields modest improvements in few-shot settings."
In summary, the multimodal textbook represents a significant advancement in VLM pretraining by leveraging the structure, knowledge richness, and coherence of instructional videos. This approach is a promising step forward for creating more effective and capable vision-language models.