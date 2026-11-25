# Task 4: Framework Basics — Build a Prolog Knowledge Base

## Objective and prerequisites

Turn the facts and rules from [Task 3](3_symbolic_crash_course.ipynb) into an executable knowledge base (KB) using SWI-Prolog. Learn to load a program, ask queries with variables, inspect explanations, and test rules. Allow 4–6 hours. A local CPU is sufficient; no language model, API key, or Python bridge is required.

## 1. Set up the framework

Install [SWI-Prolog](https://www.swi-prolog.org/Download.html) for your operating system. Read the [quick start](https://www.swi-prolog.org/pldoc/man?section=quickstart) and [PlUnit testing guide](https://www.swi-prolog.org/pldoc/doc_for?object=section(%27packages/plunit.html%27)). Record `swipl --version`, your operating system, and installation steps in a README.

Create `kb.pl`, `kb_tests.pl`, and `README.md` in your own task repository. Keep these files for Task 5.

## 2. Run and explain a small KB

Put this worked example in `kb.pl`:

```prolog
registered(lee).
registered(sam).
completed_training(lee).

eligible(Person) :-
    registered(Person),
    completed_training(Person).

access(Person) :- eligible(Person).
```

Lowercase names are atoms, capitalized names are variables, `:-` introduces a rule, and the comma joins conditions. Clauses end with a period. These are explicit policy assumptions, not claims that a policy is fair.

Load the file with `swipl -s kb.pl`. At the prompt, enter the queries below without the displayed `?-` prompt. Predict each result before running it:

```prolog
?- access(lee).
?- access(sam).
?- access(Person).
```

Press `;` to request another solution when offered. Explain the difference between asking about an individual and finding substitutions for a variable. Use `trace.` followed by `access(lee).` to inspect the derivation; leave tracing with `notrace.` and exit with `halt.`. Record a short explanation of the proof in your own words.

## 3. Extend the knowledge base

Model a fictional lab's access policy using at least **12 ground facts**, **four people**, **two resources**, and **four rule clauses**. Include the worked example in these totals. Add facts such as `requires_training(printer).` and `trained_for(lee, printer).`, then define `can_use(Person, Resource)` so that it checks registration, resource-specific training, and at least one additional explicit condition of your choice. Document the policy in plain language before writing it in Prolog.

Include one registered person missing a training record, one person allowed to use one resource but not another, and one person with multiple routes to the same derived conclusion. Query all authorized person–resource pairs; explain any duplicate answers and show a unique sorted answer set using `setof/3` or `findall/3` followed by `sort/2`.

Avoid recursion for this first KB. Do not infer permission from missing evidence. Compare Prolog's goal-directed rule execution with Task 3's repeated forward-chaining passes: do they derive the same positive access claims for the original example?

## 4. Test and revise a rule

Start `kb_tests.pl` with this example:

```prolog
:- use_module(library(plunit)).
:- consult('kb.pl').

:- begin_tests(access_policy).
test(lee_has_access) :- access(lee).
test(sam_not_derived, [fail]) :- access(sam).
:- end_tests(access_policy).
```

From the directory containing both files, run:

```bash
swipl -q -s kb_tests.pl -g "run_tests,halt" -t "halt(1)"
```

Add at least six more tests, including a successful resource query, a missing prerequisite, different permissions for two resources, and the complete set of answers to a variable query. Check behavior rather than the order in which clauses happen to appear. For multiple proofs, use an answer-set check or PlUnit's nondeterminism options deliberately.

Change one policy rule, predict which tests should change, and run the suite. Explain a resulting failure, revise the expected behavior only if the policy truly changed, then restore or document the final policy. Submit evidence of both runs.

## 5. Interpret the limits

Write 300–400 words explaining why failure to prove `access(sam)` is not evidence of an explicit real-world prohibition. What would be needed to represent an explicit denial? Identify a missing-record scenario, who could correct it, and how someone could contest a decision. Explain what a proof trace establishes and what it cannot establish about the input facts.

## Deliverable and evaluation

Submit a repository link and a short PDF or Markdown report to Canvas under Deliverable 4. Include the three files, setup and exact run commands, your policy specification, predicted and observed query results, trace explanation, before/after test evidence, and reflection. Your README must let another student reproduce the queries and tests from a fresh checkout.

Assessment considers correctness of rules and answer sets, meaningful tests, reproducibility, and interpretation of missing evidence. If installation is blocked, use [SWISH](https://swish.swi-prolog.org/) to run the same facts, rules, and queries in a browser; save the source and output and document any testing differences. Distinguish observed results from expected ones.
