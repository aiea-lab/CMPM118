# TEMPLATE SENN Task 5: Read the Reference Paper

Status: Backlog
Quarter: winter26

# Self-Explainable Deep Neural Network Project

- [ ]  Read the paper https://link.springer.com/article/10.1007/s10489-022-03886-6
    
    Note: It is **not required to read the entire paper** (it is encouraged tho!)
    
    - Mandatory:
        - Section 1 (Introduction)
        - Section 3 (Method)
            - 3.2 and 3.3 are mandatory
                - They are the most important sections! Try to understand them!
            - 3.1 is optional but can help you better understand 3.2 and 3.3. It is perfectly normal if some equations are hard to understand. It is not expected or required to fully understand everything in section 3.1.
        - Section 4 (Results)
            - Read only
                - 4.3 (intro)
                - 4.3.1 (example-based explanations)
                - 4.3.2 (counterfactuals)
        - Section 6 (Conclusion)
    - Optional: all the other sections! They are not necessary for this project but reading them may be useful for your future!

## Deliverables
As you read each section answer the following questions. All questions do not need to be answered perfectly we 
just want to make sure you are engaging with the paper and learning to focus on the important parts. Being able to read and understand a paper is extremely important in research, so for your first paper we will guide you to the parts you should focus on. **Note:** most questions can be answered in 1 sentence.


**Important:** No LLMs are allowed! The only allowed usage is for grammar checks (style improvements are not allowed)

---

### Section 1 (Introduction)
1. Write a brief summary of the introduction in your own words.

---

### Section 3 (Method)

**3.2**
1. Why might the author(s) prefer a sparsemax over a softmax for the content-based attention mechanism?
2. What are the two inputs to the classifier and what do they represent?

**3.3**
1. In this setting, what is a counterfactual image?
2. In this setting, what is an example image?
3. What is the point of looking at counterfactuals and examples?

---

### Section 4 (Results)

**4.3**
1. What is the base network used to gather these results, and why do you think results are similar for other models?
2. What can used memory samples tell us about the model's representation of classes? What do you think the internal representation of a model is?

**4.3.1**
1. Bias detection: Explain how the dataset is biased. What will this bias allow the model to do differently when making predictions that the unbiased dataset does not?
2. Quality estimation: In this section, what is the author trying to determine the quality of? What are the findings?

**4.3.2**
1. Understanding prediction reliability: What do counterfactuals tell us about model prediction certainty, and why do counterfactuals signal this?
2. Quality estimation: Why are autoencoders being used? What does reconstruction tell us about how well an image represents a class?

---

### Section 6 (Conclusion)
1. Brainstorm one or two real-world applications where you could see this method being useful, and briefly explain why.