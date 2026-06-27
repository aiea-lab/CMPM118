# TEMPLATE SENN Task 8: Error Correction

Status: Backlog
Quarter: winter26

# Self-Explainable Deep Neural Networks Project

- [ ]  For each of the 20 wrong predictions selected in the previous task, identify (if possible) a memory set that corrects the prediction for that input (i.e., identify a strategy to select the memory set).
    - **!!Important**:
        - The memory set **cannot** exploit the labels of the samples you want to correct (e.g., if the correct class is “9”, you cannot feed a memory set containing only samples from class “9” based on prior knowledge of the correct class)
        - The memory set can be chosen manually (based on your criteria), automatically (e.g., clustering), or randomly (e.g., using balanced/unbalanced set). You are free to select them as you prefer as long as you do not use the label information of the samples you want to correct (but you can use the labels information associated with the memory set samples!) and you use the same criteria/ strategy for all the samples
    - Do you believe it is possible to design a general strategy to correct most of the predictions?
    - How many predictions are you able to change?
- [ ]  Test at least 2 different strategies if at least one of them work and 3 if none of them work
- [ ]  Commit your changes to the github repo.

Useful links:

- Sklearn set of neighbors: [https://scikit-learn.org/stable/api/sklearn.neighbors.html](https://scikit-learn.org/stable/api/sklearn.neighbors.html)
- SkLearn clustering: [https://scikit-learn.org/stable/modules/clustering.html](https://scikit-learn.org/stable/modules/clustering.html)
- Pytorch Sampler: [https://pytorch.org/docs/stable/data.html#data-loading-order-and-sampler](https://pytorch.org/docs/stable/data.html#data-loading-order-and-sampler)

## Deliverables

- Write a report describing your experiments and your analysis. Please include the link to the specific commits related to this task. Please comment on the feasibility of a unified strategy, any patterns you observe, etc.
    - If you were not able to find any strategy or any memory set able to change the predictions, please describe all your experiments, all the strategies you tried, and provide your reasoning/hypothesis on why you believe designing such a strategy is unfeasible (supported by facts/observations). And then describe the difference between the two Memory Wrap variants
    - No Max length limit for this report