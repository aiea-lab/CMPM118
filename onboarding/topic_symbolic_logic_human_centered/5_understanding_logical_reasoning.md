# Task 5: Topic Basics 1 — Recursive Rules and Explanations

## Objective and prerequisites

Extend [Task 4's Prolog KB](4_build_your_own_kb.md) with multi-step prerequisite reasoning. Distinguish direct facts from derived relations, inspect alternative proofs, and test missing-information behavior. Allow 4–6 hours using SWI-Prolog and PlUnit. No LLM or paid API is required.

Use the [SWI-Prolog quick start](https://www.swi-prolog.org/pldoc/man?section=quickstart) and [Learn Prolog Now!](https://lpn.swi-prolog.org/) sections on recursion and lists. The [tabling guide](https://www.swi-prolog.org/pldoc/man?section=tabling) is an optional extension for cyclic relations, not a prerequisite.

## 1. Trace a recursive relation

Create a separate `prerequisites.pl` file and load this example:

```prolog
prerequisite(advanced_lab, safety).
prerequisite(advanced_lab, equipment).
prerequisite(equipment, orientation).

requires(Course, Requirement) :-
    prerequisite(Course, Requirement).
requires(Course, Requirement) :-
    prerequisite(Course, Intermediate),
    requires(Intermediate, Requirement).
```

The first rule is the base case; the second follows another edge. Use only a finite **acyclic** prerequisite graph for the required task. Before running, predict the answers to `requires(advanced_lab, R)` and `requires(safety, R)`. Obtain a unique sorted set with `setof/3`. Explain what happens when `setof/3` has no solutions, and compare it with `findall/3`.

Trace the proof for `requires(advanced_lab, orientation)`. Draw the chain of supporting facts and distinguish a direct prerequisite from a transitive one. Query failure does not establish an explicit real-world denial.

## 2. Connect the relation to your KB

Add at least eight prerequisite facts involving at least six training modules, a chain of three edges, and a diamond with two routes to one prerequisite. Keep the graph acyclic. Include at least three fictional people with different completion records; retain Task 4's registration and resource permissions.

Implement these predicates and document their intended meaning:

- `missing_requirements(Person, Course, Missing)`: a sorted list of all transitive prerequisites without a completion fact for that person. Return `[]` when none are missing, including for a course with no prerequisites. Use it with ground person and course arguments; document this mode.
- `ready(Person, Course)`: succeeds when the person is registered and has no missing prerequisite records. This is readiness to take a course, not a claim that they completed it.
- `requirement_path(Course, Requirement, Path)`: produces a list of nodes for a supporting path, including both endpoints. Enumerate alternative paths on the diamond.

Explain how collecting all requirements before checking completion differs from succeeding on just one completed prerequisite. State explicitly that the readiness rule treats missing records as unmet requirements for this fictional policy.

## 3. Test the reasoning

Add at least eight PlUnit cases: a direct relation, a multi-step relation, both diamond paths, no prerequisites, a fully ready person, a missing prerequisite, an unregistered person, and the complete unique prerequisite set. Keep existing Task 4 tests passing. Check answer sets rather than incidental solution order.

Change one prerequisite fact in a separate file or fresh Prolog session. Predict which paths, missing lists, and readiness answers should change. Compare before/after results and explain one case that stays unchanged. Keep the final KB and tests consistent; do not silently change expected results to hide a regression.

Run from the directory containing your test file, for example:

```bash
swipl -q -s kb_tests.pl -g "run_tests,halt" -t "halt(1)"
```

**Optional extension:** Add a cycle only in a separate copy. Explain the risk to ordinary recursive execution before running it. Investigate tabling or a visited-node path implementation; do not leave an unbounded recursive query running.

## Deliverable and evaluation

Submit source, tests, README commands and versions, a graph diagram, predicted/observed query table, and a 400–600 word concept report to Canvas under Deliverable 5. Explain base and recursive cases, duplicate proofs, the policy's use of missing evidence, and one way an incorrect completion record could be contested.

Assessment considers correct recursive relations, complete answer sets, useful explanation paths, tests, and faithful interpretation of assumptions. If local SWI-Prolog is unavailable, use [SWISH](https://swish.swi-prolog.org/) and preserve source and query evidence, documenting test differences. Paper reimplementation is deferred; this task establishes the reasoning skills needed to evaluate such systems.
