# Task: Subgroup Evaluation (Bias Audit)

## Objective
The goal of this task is to **quantitatively evaluate model behavior across different subgroups**.

You will:
- Define relevant subgroups (e.g., demographic, linguistic, contextual)
- Construct a controlled evaluation dataset
- Measure differences in model behavior across groups
- Identify potential disparities or biases

---

## Step 1: Define Subgroups

- [ ] Select a task or behavior to evaluate (e.g., sentiment, reasoning, job recommendations, toxicity)

- [ ] Define at least **2–4 subgroups** relevant to the task

Examples:
- Names (e.g., culturally associated names)
- Gendered terms (he/she/they)
- Dialects or language styles
- Professions or roles
- Socioeconomic indicators

- [ ] Justify your subgroup selection:
  - Why are these groups meaningful?
  - What potential disparities do you expect?

## Step 2: Construct a Controlled Test Set

- [ ] Create a dataset (minimum: 20–40 examples)

- [ ] Ensure:
  - Same **prompt template**
  - Only subgroup variable changes

## Step 3: Run the Evaluation

- [ ] Query the model on all inputs
- [ ] Store outputs in a structured format

## Step 4: Define Evaluation Metrics

### Output-Based Metrics
- [ ] Define what you are measuring:
  - Classification outcome (e.g., yes/no, positive/negative)
  - Generated text properties (tone, sentiment, toxicity)
  - Reasoning correctness
- [ ] Compute metrics per subgroup:

## Step 5: Analyze Results

- [ ] Identify:
  - Which groups receive systematically different outputs?
  - Are differences consistent or noisy?
  - Are disparities large or small?

- [ ] Check for confounders:
  - Prompt sensitivity
  - Ambiguity in task definition

## Deliverable: Bias Audit Report

Create a one-page report and upload it to canvas containing the following:

### 1. Methodology
- Task description
- Subgroup definitions
- Dataset construction
- Model + parameters

### 2. Results

Include tables such as:

| Subgroup | # Examples | Positive Rate | Error Rate | Avg Score |
|----------|-----------|--------------|------------|-----------|
| Group A  | 20        | 65%          | 15%        | 0.72      |
| Group B  | 20        | 40%          | 30%        | 0.55      |

### 3. Disparity Analysis

- Quantify differences across groups
- Highlight largest observed gaps


### 4. Discussion

- What disparities did you observe?
- Are they expected or surprising?
- How might these affect real-world use?

### 5. Limitations

- Dataset size and coverage
- Proxy choices for subgroups
- Measurement noise or subjectivity


