# TEMPLATE XAI_LLM Task 8: Finetuning LLMs on NLI

Status: Backlog
Quarter: winter26

# Neural Explanations (LLMs) Project

- This task can be completed either on Nautilus or on your own workstation
- The goal of this task is to finetune an Open LLMs on the NLI task, transforming the model into a classifier rather than a token-prediction model
    - We suggest to work on the same codebase you used in task 2/4
- [ ]  Choose an open model that supports finetuning for text classification (Note: BERT based models (e.g., BERT, RoBERTa, distilBERT) are not considered large language models)
    - [ ]  You can use the model you chose in the previous task if that model supports text classification
    - [ ]  We strongly suggest to use a model that implement AutoModelForSequenceClassification from HuggingFace [https://huggingface.co/docs/transformers/v4.57.1/en/model_doc/auto#transformers.AutoModelForSequenceClassification](https://huggingface.co/docs/transformers/v4.57.1/en/model_doc/auto#transformers.AutoModelForSequenceClassification) since there are plenty of guides/tutorials online
        - Hugging Face tutorials
            - [https://huggingface.co/docs/transformers/en/tasks/sequence_classification](https://huggingface.co/docs/transformers/en/tasks/sequence_classification)
            - [https://huggingface.co/learn/llm-course/chapter3/3](https://huggingface.co/learn/llm-course/chapter3/3)
        - Other Useful guides for finenuting:
            - https://medium.com/@noel.benji/optimizing-llms-for-classification-key-insights-strategies-67a80890ff4d
            - [https://kili-technology.com/blog/how-to-fine-tune-large-language-models-llms-with-kili-technology](https://kili-technology.com/blog/how-to-fine-tune-large-language-models-llms-with-kili-technology)
- [ ]  Finetune the model on NLI such that it achieves performance similar or better then the Bowman/LSTM model
- [ ]  Commit your changes to the github repo.

## Deliverables

- [ ]  Send a report summarizing what you learned in this tasks, what problems you faced, and describing your solutions to those problems
    - [ ]  In particular comment the difference in performance between your model and the previous ones and the modifications you had to do in the setup
- [ ]  Please include the link to the specific commits related to this task.