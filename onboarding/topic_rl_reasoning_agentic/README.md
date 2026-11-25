# RL and Reasoning + Agentic

Learn how agents make decisions from states, actions, and rewards, and how to evaluate whether a learned policy improves on a baseline. You will implement tabular reinforcement learning, use Gymnasium environments, and compare exploration strategies through controlled experiments. These foundations prepare you to investigate failures and robustness in autonomous-vehicle simulations.

- **Lead:** Leilani H. Gilpin
- **Project page:** [Robust Autonomous Vehicles](https://aiea-lab.github.io/project/robustavs/)
- **Reading list:** [Reading list](#reading-list)
- **Published papers:** [Published papers](#published-papers)

## What you will learn

- Model states, actions, rewards, and discounted returns.
- Train and evaluate tabular agents through the Gymnasium interface.
- Design controlled comparisons before moving to vehicle-focused RL research.

## Getting started

Read the shared [Task 1: Lab Onboarding](../1_onboarding.md) and the [onboarding overview](../README.md). Tasks 3–5 run on a local CPU. Task 3 uses the Python standard library; Tasks 4–5 use Gymnasium. Later tasks introduce additional RL libraries and vehicle environments. Confirm simulator and compute requirements with the project lead before starting Tasks 6–9.

## Tasks

Complete the tasks in numerical order. Tasks 3–5 provide the introductory sequence; Tasks 6–9 retain the existing vehicle-focused project activities.

| Task | Assignment |
|---|---|
| 1 | [Lab Onboarding](../1_onboarding.md) |
| 2 | [Nautilus](2_nautilus.md) |
| 3 | [Reinforcement Learning Basics](3_project_onboarding.md) |
| 4 | [Gymnasium Environments](4_gymnasium_basics.md) |
| 5 | [Exploration and Tabular Learning](5_benchmarking_rl_algorithms.md) |
| 6 | [Learn RL Algorithms](6_learning_rl_algorithms.md) |
| 7 | [Learning More RL Algorithms](7_learning_more_rl_algorithms.md) |
| 8 | [RL Refinement](8_rl_refinement.md) |
| 9 | [RL Testing Framework](9_rl_testing_framework.md) |
| End of quarter | [Shared Task 10: Offboarding](../10_offboarding.md) |

## Deliverables

Submit the artifacts requested in each assignment to its Canvas deliverable. For code-based work, include setup and reproduction commands, versions, configurations, and output evidence. For reading-based work, include passage references and distinguish the authors' claims from your interpretation. Follow each task's specific format, evaluation criteria, and fallback instructions.

## Reading list

- John Schulman et al. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347).
- Tuomas Haarnoja et al. [Soft Actor-Critic](https://arxiv.org/abs/1801.01290).
- Timothy P. Lillicrap et al. [Continuous Control with Deep Reinforcement Learning](https://arxiv.org/abs/1509.02971).
- Volodymyr Mnih et al. [Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602).
- Volodymyr Mnih et al. [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783).

## Published papers

- Oliver Chang, Kay Vargas, Leilani H. Gilpin, and Daniel J. Fremont. [Reinforcement Learning for Falsification of Dynamic Driving Scenarios](https://aiea-lab.github.io/publication/reinforcement-learning-for-falsification-of-dynamic-driving-scenarios-2026/). AAMAS 2026.
- Oliver Chang and Leilani H. Gilpin. [Dynamically Introspective Action Advising](https://aiea-lab.github.io/publication/dynamically-introspective-action-advising-2026/). CoLLAs 2026.
