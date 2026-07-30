# Datalog Tutorial
Auditor Task 5
Spring 2025

Datalog is a simple logic language. It stores facts. It uses rules to find answers.

# Step 1: Basic Rules
* Names of real things must start with a lowercase letter. Example: `alice` or `engineering`.
* Placeholders must start with a capital letter. Example: `X` or `Y`.
* Facts are true statements.
* Rules are "If-Then" statements. They find new answers.

# Step 2: Code File
Create a file named `company.dl`. Paste these 10 facts and 1 rule into it:

```datalog
employee(alice, engineering).
employee(bob, engineering).
employee(charlie, finance).
employee(david, finance).
employee(eve, marketing).

manager(sarah, engineering).
manager(james, finance).
manager(elena, marketing).

project(alpha, engineering).
project(beta, finance).

works_on(X, P) :- employee(X, D), project(P, D).
```

# Step 3: Run Questions
You can ask the system questions. 

* Question 1: Who works in engineering?
  ```datalog
  ?- employee(X, engineering).
  ```
  Output: `X = alice`, `X = bob`.

* Question 2: Who works on project alpha?
  ```datalog
  ?- works_on(X, alpha).
  ```
  Output: `X = alice`, `X = bob`. The system uses the rule to find this.

# Step 4: How AI Helps
AI turns regular English sentences into code. It uses three steps:
1. The user asks: "Who works on project alpha?"
2. The AI finds the word `alpha`. It matches it to the `works_on` rule.
3. The AI writes the code: `?- works_on(X, alpha).`

