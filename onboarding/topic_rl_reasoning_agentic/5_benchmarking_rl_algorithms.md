# Task 5: Topic Basics 1 — Exploration and Tabular Learning

## Objective and prerequisites

Use [Task 4's Gymnasium runner and Q-learning implementation](4_gymnasium_basics.md) to investigate exploration. Compare two epsilon schedules with an equal training budget, freeze the resulting policies, and distinguish training returns from evaluation performance. Allow 4–6 hours on a local CPU; no CARLA, Box2D, or deep RL library is required.

Review [Gymnasium basic usage](https://gymnasium.farama.org/introduction/basic_usage/) and [handling time limits](https://gymnasium.farama.org/tutorials/gymnasium_basics/handling_time_limits/). Use the [FrozenLake reference](https://gymnasium.farama.org/environments/toy_text/frozen_lake/) to verify your environment configuration.

## 1. Specify the comparison

Keep the 4x4 map, `is_slippery=True`, a 100-step time limit, zero-initialized Q tables, alpha 0.1, and gamma 0.99. Train each agent for 5,000 episodes. Compare:

- Constant exploration: epsilon = 0.2.
- Decaying exploration: `epsilon = max(0.05, 1.0 - episode / 2500)`, with episodes numbered from zero.

Plot or tabulate epsilon at episodes 0, 1000, 2500, and 4999 before training. Explain what is held fixed, what changes, and why reducing exploration can improve observed training return without proving that the policy learned more.

Use training seeds 0–4 for five independently initialized runs per schedule. Within each run, seed the exploration generator and initial environment reset, then let their random streams advance. Shared seed IDs make the comparison repeatable but do not guarantee identical trajectories across schedules. Record all configurations and library versions.

## 2. Check the update before the experiment

For a transition with reward 0, old Q value 0.2, best next-state Q value 0.8, alpha 0.1, and gamma 0.99, calculate the updated value by hand for (a) an ordinary transition, (b) termination, and (c) external truncation. Turn these into three executable checks of your update function.

Retain Task 4's convention: reset after termination or truncation, but suppress bootstrapping only on termination. Verify that evaluation makes no Q-table updates and uses epsilon zero. Explain how your greedy tie-breaking rule affects an all-zero table.

## 3. Run and evaluate

For every schedule and training seed, record episode return, length, epsilon, and ending flags. Summarize training in non-overlapping 250-episode windows, retaining all windows rather than selecting the strongest interval.

After training, freeze the Q table and evaluate 200 episodes with reset seeds 10000–10199. Use the same list for every trained policy. Also evaluate a random-action baseline with an explicitly seeded action sampler on that list. These evaluation seeds must not be used to choose hyperparameters or stopping points.

Report one row per training run with success rate, mean return, mean length, and truncation rate. Then report each schedule's mean and standard deviation across its five run-level success rates. Keep variation across training runs separate from variation across episodes. Show the paired difference in success rate for each training seed; do not hide runs that failed to learn.

## 4. Interpret the result

Write a prediction before seeing results. Afterward, explain whether the data support it. Discuss sparse rewards, the exploration schedule, and why training/evaluation returns can differ. Include one unsuccessful trajectory and identify what the log establishes versus what remains a hypothesis.

Propose one follow-up experiment changing only a single factor; execution is optional. Do not tune your main comparison after inspecting the evaluation scores. No success threshold is required: implementation correctness and honest analysis matter more than a favorable result.

## Deliverable and evaluation

Submit code, configuration, dependencies, README commands, raw episode logs, summary tables, two training curves or equivalent window tables, and a 400–600 word report to Canvas under Deliverable 5. Include the hand calculations and executable update checks, training/evaluation distinction, variability, and one limitation of applying this toy result to vehicle control.

Assessment considers controlled comparisons, correct updates, seed handling, reproducibility, and supported conclusions. If runtime is a problem, reduce the episode budget equally for both schedules and all runs before the main experiment; document the reduction. If Gymnasium is unavailable, use an environment where it can be installed and record the setup issue rather than presenting unexecuted results. Task 6 retains the existing advanced vehicle-focused algorithm work; confirm simulator setup with the lead before beginning it.
