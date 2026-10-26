# Task 4: Framework Basics — Gymnasium Environments

## Objective and prerequisites

Connect [Task 3's tabular RL concepts](3_rl_crash_course.ipynb) to Gymnasium, the maintained successor to Gym. Learn the environment interface, run a baseline policy, adapt your Q-learning update, and evaluate a configuration change. Allow 4–6 hours on a local CPU. Use text rendering; no GPU or vehicle simulator is required.

Read [Gymnasium basic usage](https://gymnasium.farama.org/introduction/basic_usage/), the [FrozenLake reference](https://gymnasium.farama.org/environments/toy_text/frozen_lake/), and [handling time limits](https://gymnasium.farama.org/tutorials/gymnasium_basics/handling_time_limits/).

## 1. Install and inspect

Create a virtual environment, activate it, and install `gymnasium` with `python -m pip install gymnasium`. On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install gymnasium
python -m pip freeze > requirements.txt
python --version
```

On Windows use `py -m venv .venv` and `.venv\Scripts\Activate.ps1`. Record the Python and Gymnasium versions and setup fixes. Keep `.venv/` out of Git.

Run this smoke test:

```python
import gymnasium as gym

with gym.make("FrozenLake-v1", map_name="4x4",
              is_slippery=False, render_mode="ansi",
              max_episode_steps=100) as env:
    observation, info = env.reset(seed=0)
    env.action_space.seed(0)
    print(env.observation_space, env.action_space)
    print(env.render())
    next_observation, reward, terminated, truncated, info = env.step(2)
    print(next_observation, reward, terminated, truncated, info)
```

Gymnasium returns two values from `reset` and five from `step`. Stop an episode on `terminated or truncated`; reset before continuing. Termination represents a task endpoint; truncation can represent an external time limit.

**Predict before running:** Where will action 2 take the agent? Which values represent state, immediate reward, and episode completion? Identify the action encoding, observation encoding, reward scheme, and terminal tiles from the reference. Compare them with your corridor in Task 3.

## 2. Implement an episode runner

Create `gym_basics.py` with `run_episode(env, policy, seed)`. Let `policy(observation)` return an action. Reset with the supplied seed and return a dictionary containing total reward, number of steps, and the final `terminated` and `truncated` flags. Record the trajectory separately for one episode, including state, action, reward, next state, and both flags. Reuse the runner for random and learned policies.

Add checks for valid actions and observations using each space's `contains` method. Demonstrate two controlled cases on the deterministic map:

- With `max_episode_steps=1`, move right once: the episode should truncate without reaching a terminal tile.
- With the normal time limit, move down then right into a hole: the episode should terminate.

Explain why a zero-reward episode need not be a timeout. Close environments when finished, including after an error.

## 3. Adapt Q-learning

Initialize a zero table sized from `env.observation_space.n` and `env.action_space.n`. Use Task 3's epsilon-greedy approach and Q-update, adapting the terminal handling:

```python
# Reset on either ending flag, but suppress bootstrapping only on termination.
target = reward if terminated else reward + gamma * max(Q[next_state])
Q[state][action] += alpha * (target - Q[state][action])
```

For this exercise, the time limit interrupts a continuing task, so bootstrap on truncation. Explain how that assumption differs from treating a fixed finite horizon as part of the task definition.

Train on the deterministic 4x4 map for 3,000 episodes per training seed, using alpha 0.1, gamma 0.99, and epsilon 0.2. Use seeds 0, 1, and 2 for three separate training runs. Seed your exploration generator and environment; initialize each table independently. Within a run, seed the initial reset, then let the environment's random stream advance rather than reseeding every episode identically. Resolve greedy ties reproducibly. Log episode returns and lengths.

Keep all settings in one configuration object or command-line arguments. Explain the difference between a framework's transition mechanics and the policy you implement.

## 4. Evaluate and change one configuration

Freeze each learned table. Evaluate its greedy policy for 100 episodes with reset seeds 1000–1099, without learning or exploratory actions. Evaluate a random-action baseline on the same episode seed list, also explicitly seeding its action sampler. These shared seeds support repeatable comparisons; policies may still consume randomness differently.

Repeat the full train/evaluate procedure with **only `is_slippery=True` changed**. Keep the map, budget, hyperparameters, and seed lists fixed. Do not tune on the evaluation results. Predict how the configuration change could affect success before running it.

Report this table with one row per configuration, policy, and training seed (use a dash for the random baseline's training seed):

| Slippery | Policy | Training seed | Episodes | Success rate | Mean return | Mean length | Truncation rate |
|---|---|---|---|---|---|---|---|

Define success as reaching the goal, not simply ending an episode. Include one trajectory and a plot or table summarizing training over fixed windows. Report variation across the three training seeds rather than just the best run. There is no required success threshold: a correctly implemented low-performing agent is a result to investigate. Check terminal handling, exploration, and reward sparsity before increasing the budget.

## Deliverable and evaluation

Submit code, `requirements.txt`, README commands, configuration, episode logs or summaries, and a 400–600 word report to Canvas under Deliverable 4. Include the smoke test, boundary-case checks, predictions, results, and limitations. Explain why FrozenLake performance is insufficient evidence about autonomous driving or language-based agents. Your script should run from a fresh checkout and close its environments.

Assessment considers correct interface use, terminal/truncation handling, reproducible comparisons, and honest interpretation rather than a target score. If installation is blocked, bring the error to a working session and use a Python environment with Gymnasium available. Submit setup evidence and clearly label any unexecuted parts; Task 3's handwritten corridor alone does not demonstrate the framework objective.

Tasks 5–9 still contain the vehicle-focused project sequence. Confirm project-specific simulator setup with the lead before starting that sequence; CARLA installation is no longer a prerequisite for Task 4.
