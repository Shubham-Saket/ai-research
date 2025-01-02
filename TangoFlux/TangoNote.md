# TANGOFLUX: Super Fast and Faithful Text to Audio Generation with Flow Matching and CLAP-Ranked Preference Optimization

## Authors
- Chia-Yu Hung  
- Navonil Majumder  
- Zhifeng Kong  
- Ambuj Mehrish  
- Rafael Valle  
- Bryan Catanzaro  
- Soujanya Poria  

## Affiliations
- Singapore University of Technology and Design (SUTD)  
- NVIDIA  

## Abstract
TANGOFLUX is an efficient Text-to-Audio (TTA) generative model with 515M parameters, capable of generating up to 30 seconds of 44.1kHz audio in just 3.7 seconds on a single A40 GPU. The model addresses the challenge of aligning TTA models by introducing the CLAP-Ranked Preference Optimization (CRPO) framework, which iteratively generates and optimizes preference data to enhance TTA alignment. TANGOFLUX achieves state-of-the-art performance across both objective and subjective benchmarks.

---

## Key Contributions
1. **TANGOFLUX Model**:  
   A small and fast TTA model based on rectified flow that achieves state-of-the-art performance using fully non-proprietary training data.

2. **CRPO Framework**:  
   A novel strategy to generate audio preference data and align rectified flow, demonstrating superior performance over other audio preference datasets.

3. **Open Source**:  
   The authors publicly release the code and model weights to foster further research in TTA generation.

---

## Methodology
### Audio Encoding
- Uses a VAE from Stable Audio Open to encode stereo audio waveforms at 44.1kHz into audio latent representations.

### Model Conditioning
- Employs textual and duration conditioning to control the event presence and length of the generated audio.

### Model Architecture
- Combines MMDiT and DiT blocks, resulting in a model with 515M parameters.

### Flow Matching
- Utilizes rectified flows for training, which are more robust to noise scheduler choices.

### CRPO
- Leverages the CLAP model as a proxy reward model to rank generated audios and construct preference datasets for optimization.

---

## Experiments
### Training
- Pretrained on Wavcaps for 80 epochs and fine-tuned on the AudioCaps training set for 65 additional epochs.

### Datasets
- Uses open-source data from Wavcaps and AudioCaps for training, and constructs a preference dataset using CRPO.

### Evaluation
- Evaluated on the AudioCaps test set and an out-of-distribution dataset with complex prompts.

---

## Results
### Objective Metrics
- TANGOFLUX outperforms prior TTA models in terms of FDopenl3, CLAPscore, and Inception Score (IS), with notable efficiency gains.

### Subjective Evaluation
- Demonstrates superior performance in overall audio quality (OVL) and relevance to text input (REL) based on human evaluations.

### Inference Time
- Achieves high-quality outputs with lower computational requirements, making it an efficient choice for scenarios where inference time is critical.

---

## Conclusion
TANGOFLUX is a fast and efficient TTA model that produces high-quality audio aligned with user prompts. The CRPO framework enhances the model's performance, making it a practical and scalable solution for text-to-audio generation.

---

## References
The paper includes references to various works on TTA generation, alignment methods, and flow matching frameworks.
