# TEMPLATE LLM Task 10: Natural Language To Prolog Fine-Tuning

Status: Backlog
Labels: Auditor, Intern
Quarter: Spring 25

<aside>
🖊️ Your goal for this week is to fine-tune a LLM for natural language to Prolog conversion.

</aside>

- [ ]  Read about LoRA Adapters (and other types of adapters): [https://huggingface.co/docs/peft/conceptual_guides/adapter](https://huggingface.co/docs/peft/conceptual_guides/adapter)
- [ ]  Download the natural language-to-Prolog dataset (which you will use to perform the fine-tuning):
    
    [dataset.csv](10_nl_to_prolog_fine_tuning_files/dataset.csv)
    
- [ ]  Recommendations
    - [ ]  Use NVIDIA A10 GPUs (or RTX A6000, A100, L40S, etc. if necessary) on Nautilus
    - [ ]  [https://huggingface.co/JetBrains/Mellum-4b-base](https://huggingface.co/JetBrains/Mellum-4b-base) and [https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) might be a good starting points for the base model
    - [ ]  [https://huggingface.co/docs/peft/en/index](https://huggingface.co/docs/peft/en/index)
    - [ ]  [https://huggingface.co/docs/trl/index](https://huggingface.co/docs/trl/index)
- [ ]  Perform the fine-tuning using LoRA Adapters. You are training adapters to convert 1) natural  language contexts to Prolog knowledge bases and 2) natural language questions to Prolog queries
    - [ ]  Training
        - [ ]  Use around 2,800 cases for training
        - [ ]  Think about how to structure the dataset to train the adapters for converting to both Prolog knowledge bases and Prolog queries
        - [ ]  You might have to experiment with hyperparameters (like rank dimension, lora alpha, etc.)
        - [ ]  If you are exceeding GPU VRAM, try techniques like gradient checkpointing, reducing batch size, and using a smaller base model
    - [ ]  Inference
        - [ ]  Perform inference on around 200 cases
        - [ ]  You will need to merge your trained adapters with the base model, which will yield the fine-tuned model
    - [ ]  Evaluation
        - [ ]  Your fine-tuned model must achieve a syntax validity (use `pyswip`) of at least 50% for both Prolog knowledge bases and Prolog queries

# Deliverable

- Write one page about your process, what you tried, and results
- Present your writeup in one of the status meetings