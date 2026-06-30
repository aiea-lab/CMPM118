# Task: Reproduce a Reported Limitation

## Objective
The goal of this task is to move from **reading model documentation → empirically verifying claims**.

You will:
- Identify a **reported limitation** from a model card
- Design an experiment to **reproduce the limitation**
- Quantify its **frequency and severity**

## Step 1: Select a Limitation

- [ ] Choose **one limitation** from a model card (from Task 2).

Examples:
- Bias in outputs (e.g., gender, race, profession)
- Hallucinations (incorrect factual claims)
- Failure in reasoning (logical inconsistency)
- Unsafe or policy-violating outputs

- [ ] Clearly restate the limitation in your own words:
  - What is the failure mode?
  - Under what conditions does it occur?

## Step 2: Define an Evaluation Setup

### Inputs / Prompts
- [ ] Design a set of **test prompts** (minimum: 10–20)

Prompts should:
- Target the specific limitation
- Be varied but controlled (e.g., same structure, different entities)

### Experimental Variables
- [ ] Define what you are varying:
  - Input phrasing
  - Demographic attributes
  - Context

- [ ] Keep other factors fixed:
  - Model version
  - Temperature (recommend: 0 or low)
  - Prompt structure

## Step 3: Run the Experiment

- [ ] Query the model using your prompt set
- [ ] Collect outputs in a structured format (CSV, JSON, or table)

## Step 4: Define Metrics

### Frequency
- [ ] Measure how often the limitation occurs:
  - % of outputs exhibiting the issue
### Severity
- [ ] Define a simple severity scale (e.g., 1–3 or 1–5)

Example:
- 1 = mild issue (subtle bias or ambiguity)
- 2 = moderate issue (clear bias or incorrect reasoning)
- 3 = severe issue (harmful, unsafe, or clearly wrong)

- [ ] Assign a severity score to each output

## Step 5: Analyze Results

- [ ] Aggregate results:
  - Frequency of failures
  - Average severity
  - Patterns across inputs

- [ ] Identify:
  - When does the model fail most?
  - Are there systematic patterns?

---

## Deliverable: Experiment Report

Create a report on your findings and upload it to canvas.  The report should include the following: 

### 1. Methodology
- Selected limitation
- Prompt design
- Experimental setup (model, parameters)

### 2. Results

Include a table like:

| Prompt Type | # Trials | # Failures | Failure Rate | Avg Severity |
|------------|--------|-----------|-------------|--------------|
| Profession A | 10 | 4 | 40% | 2.1 |
| Profession B | 10 | 7 | 70% | 2.5 |


### 3. Discussion

- Did you successfully reproduce the limitation?
- How consistent was the failure?
- What patterns did you observe?
- Do your findings align with the model card?

### 4. Limitations

- Small sample size?
- Subjectivity in severity scoring?
- Prompt sensitivity?

