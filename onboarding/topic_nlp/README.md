# NLP

Learn to investigate what language models predict, what their internal representations capture, and where their explanations fall short. You will study natural language inference, test lexical shortcuts, and evaluate model behavior using reproducible experiments. The project connects these skills to analyzing and explaining individual neurons in language models.

- **Lead:** Leilani H. Gilpin
- **Project page:** [Explaining LLM Failures](https://aiea-lab.github.io/project/xaillm/)
- **Related lab project:** [Neuron Explanations](https://aiea-lab.github.io/project/neuron_expl/)
- **Reading list:** [Reading list](#reading-list)
- **Published papers:** [Published papers](#published-papers)

## What you will learn

- Understand natural language inference and identify shallow lexical heuristics.
- Read neuron explanations critically and distinguish descriptive explanations from causal evidence.
- Run and evaluate language-model experiments with reproducible inputs and metrics.

## Getting started

Read the shared [Task 1: Lab Onboarding](../1_onboarding.md) and the [onboarding overview](../README.md). Tasks 2–4 introduce the existing project code and Nautilus workflow. Task 5 includes a local standard-library baseline that can be completed without cluster access. Tasks 6–9 use language-model tooling; check each assignment for model, environment, and compute requirements. Follow Task 5's specific LLM-use restriction for the paper summary.

## Tasks

Complete the tasks in numerical order. Preserve Task 4 outputs for the optional model-output analysis in Task 5; if they are unavailable, use its documented paper-based alternative and identify proposed tests clearly.

| Task | Assignment |
|---|---|
| 1 | [Lab Onboarding](../1_onboarding.md) |
| 2 | [Nautilus](2_nautilus.md) |
| 3 | [Neuron Explanations for LLMs Onboarding](3_project_onboarding.md) |
| 4 | [Run the Code on Nautilus](4_run_the_code_nautilus.md) |
| 5 | [Natural Language Inference and Lexical Heuristics](5_read_the_reference_paper.md) |
| 6 | [Open LLMs](6_open_llms.md) |
| 7 | [Open LLMs on NLI](7_open_llms_on_nli.md) |
| 8 | [Finetuning LLMs on NLI](8_finetuning_llms_on_nli.md) |
| 9 | [Explaining LLM Neurons](9_explaining_llm_neurons.md) |
| End of quarter | [Shared Task 10: Offboarding](../10_offboarding.md) |

## Deliverables

Submit the artifacts requested in each assignment to its Canvas deliverable. For code-based work, include setup and reproduction commands, versions, configurations, and output evidence. For reading-based work, include passage references and distinguish the authors' claims from your interpretation. Follow each task's specific format, evaluation criteria, and fallback instructions.

## Reading list

- Jesse Mu and Jacob Andreas. [Compositional Explanations of Neurons](https://arxiv.org/abs/2006.14032). NeurIPS 2020.
- David Bau et al. [Network Dissection: Quantifying Interpretability of Deep Visual Representations](https://openaccess.thecvf.com/content_cvpr_2017/html/Bau_Network_Dissection_Quantifying_CVPR_2017_paper.html). CVPR 2017.

## Published papers

The lab website does not currently list a publication specifically for the LLM branch of this project. The papers above provide the project’s methodological foundation.
