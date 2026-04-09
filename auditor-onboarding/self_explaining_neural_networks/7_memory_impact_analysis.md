# TEMPLATE SENN Task 7: Memory Impact Analysis

Status: Backlog
Quarter: winter26

# Self-Explainable Deep Neural Network Project

- [ ]  Modify the script to generate memory images such that the script can test a single image (or batch of images) with different memory set
- [ ]  For each of the 20 selected wrong predictions,
    - [ ]  use a memory set consisting only of samples associated with the correct class and test the prediction.
        - Does this correct the predictions? For how many? What are your thoughts?
    - [ ]  test as many **random** memory sets as possible until you find one that corrects the original predictions and analyze the identified memory sets
        - Do you see any patterns?  Can you identify why this specific random memory sets help the model?
        - NOTE: it is possible some images are not able to be corrected even with after a large number of random sets. If this occurs, include an analysis of why you believe this happens, particuarly considering the diferences of the memory wrap and baseline memory models.
- [ ]  Analyze the results
    - [ ]  What do you observe?
    - [ ]  Are there any changes in the explanation or the prediction outcome? How many?
    - [ ]  Do you observe any pattern?
- [ ]  Commit your changes to the github repo.

## Deliverables

- [ ]  Submit your analysis of the results and observations. Please include at least a couple of examples that support your analysis. Please include the link to the specific commits you used for this task.