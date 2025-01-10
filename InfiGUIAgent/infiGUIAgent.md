# InfiGUIAgent

## 1. Introduction & Problem Statement

### Emergence of GUI Agents
The paper highlights the growing importance of Graphical User Interface (GUI) agents for automating tasks on devices like computers and mobile phones. These agents, powered by Multimodal Large Language Models (MLLMs), have the potential to significantly boost productivity by interacting directly with interfaces.

### Limitations of Current MLLM-based GUI Agents
Existing agents, despite advancements, face significant challenges:

- **Limited Reasoning**: They struggle with multi-step reasoning and reflecting on past experiences, often leading to repetitive errors. The paper states:
  > "While many existing GUI Agents can perform basic single-step reasoning, they struggle to effectively leverage information from previous steps. This lack of reflection on past experiences can lead to repetitive errors during task execution."

- **Over-Reliance on Textual Annotations**: Many current agents depend on accessibility trees or Set-of-Marks, which represent the GUI through text, causing information loss, redundancy, and increased computational overhead. The paper notes:
  > "However, GUIs are inherently visual, and representing them primarily through text can lead to information loss or redundancy. Augmenting visual input with textual descriptions can also increase computational overhead."

- **Inconsistent Textual Representations**: The availability and consistency of textual representations vary across platforms, hindering real-world deployment.

### Proposed Solution: InfiGUIAgent
The paper introduces InfiGUIAgent, an MLLM-based GUI agent trained with a two-stage supervised fine-tuning (SFT) pipeline to overcome these limitations.

## 2. Core Contributions of InfiGUIAgent

### Two-Stage Supervised Fine-Tuning (SFT) Pipeline
The core of InfiGUIAgent is its two-stage training method:

- **Stage 1: Fundamental Abilities**
  - Focuses on enhancing basic skills like GUI understanding, grounding actions, and general knowledge.
  - Leverages diverse datasets and incorporates "Reference-Augmented Annotation" to better link visual elements and text.

- **Stage 2: Native Reasoning Abilities**
  - Integrates hierarchical reasoning and expectation-reflection reasoning, enabling agents to "natively" perform complex reasoning.
  - Synthesizes training data based on existing task trajectories.

### Native Reasoning Skills
The key novelty lies in the agent's ability to perform complex reasoning without explicit prompts:

- **Hierarchical Reasoning**: Involves a strategic layer (task decomposition) and a tactical layer (concrete action selection). The paper describes:
  > "Strategic layer is responsible for high-level task decomposition and sub-goal planning... Tactical layer handles the selection and grounding of concrete actions."

- **Expectation-Reflection Reasoning**: Promotes self-correction by having the agent predict outcomes and then reflect on the success/failure of its actions. The paper explains:
  > "Following each action, the agent generates expected outcomes which are used to be verified at the next step... The agent evaluates whether its actions achieved the expected results and generates a textual summary of the reflection."

### Competitive Performance
InfiGUIAgent demonstrates competitive performance on multiple GUI benchmarks, highlighting the importance of integrated native reasoning skills.

## 3. Methodology Details

### Stage 1: Training for Fundamental Abilities

- **Diverse Datasets**: The paper utilizes a variety of datasets covering GUI understanding, grounding, question answering, general knowledge, and tool use. Examples include Screen2Words, GUIEnv, ScreenQA, LLaVA-OneVision, and Glaive-function-calling.
- **Data Standardization**: Implements standardizing diverse data formats (e.g., HTML, high-resolution screens) into a common coordinate system.
- **Reference-Augmented Annotation**: A crucial element for linking GUI elements with text-based responses. It uses structured notation like:
  ```html
  <ref type="box" coords={"x1": x1, "y1": y1, "x2": x2, "y2": y2} note="GUI annotation"> corresponding text </ref>
  ```
  to provide precise spatial references.

### Stage 2: Training for Native Reasoning

- **Reasoning Skills Integration**: Trains agents to reason using hierarchical planning and self-reflection directly within the training data. The agent predicts an "expectation," performs an "action," and then generates a "reflection" on the success of the action.
- **Modular Action Space**: A standardized and categorized action space that allows for composable operations. Examples include "tap," "swipe," "scroll," and "input."
- **Reasoning Process Construction**: High-quality reasoning data is constructed using MLLMs based on existing trajectories. This includes generating:
  - Screenshot descriptions
  - Reflections on prior actions
  - Strategic and tactical reasoning
  - Expected outcomes

- **Agent-Environment Interface**: Models GUI interaction as a standard process where the agent observes a screen (state), takes an action, and transitions to the next state, incorporating the history of prior actions and reasoning.

## 4. Experimental Evaluation

### Benchmarks

The agent was evaluated on:

- **ScreenSpot**: A GUI grounding benchmark encompassing multiple platforms (mobile, desktop, web).
- **AndroidWorld**: A fully functional Android environment with a wide range of tasks. Importantly, the agent operates directly from raw pixel data, without any additional GUI metadata like Set-of-Marks (SoM) in this test.

### Performance Results

- **ScreenSpot**: InfiGUIAgent achieves competitive accuracy surpassing models like ShowUI and UGround. The paper states:
  > "InfiGUIAgent-2B achieves highest accuracy of 76.3%, surpassing several strong baselines..."

- **AndroidWorld**: InfiGUIAgent outperformed open-source models, achieving a higher success rate. The paper mentions:
  > "InfiGUIAgent-2B achieves an overall success rate of 0.09, outperforming open-source models..."

## 5. Key Takeaways and Conclusion

- **Importance of Native Reasoning**: The paper highlights the crucial role of native reasoning skills (hierarchical and expectation-reflection) in building more effective and robust GUI agents. These are not simply prompted but are built into the training data.
- **Effective Training Methodology**: The two-stage supervised fine-tuning method, coupled with reference-augmented annotation and the creative synthesis of reasoning data, leads to significant improvements.
- **Real-World Applicability**: The evaluation, conducted using raw screenshots, shows the model's applicability to real-world scenarios.
- **Future Directions**: While not explicitly stated, this research opens avenues for exploring more complex reasoning and adaptability in GUI agents, enhancing their usefulness for task automation.
