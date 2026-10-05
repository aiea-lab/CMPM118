# Guide to Creating Project Onboarding Tasks

Use this ten-task sequence when creating or revising a project track. Each task should fit roughly one week (about ten hours). Tasks 1 and 2 cover shared lab and infrastructure onboarding; Tasks 3–10 develop project-specific skills.

1. Onboarding: use the shared [lab onboarding checklist](../1_onboarding.md).
2. Nautilus: use [2_nautilus.md](2_nautilus.md).
3. Math basics: customize [3_math_basics.md](3_math_basics.md).
4. Framework basics (e.g., CARLA or PyTorch): customize [4_framework_basics.md](4_framework_basics.md).
5. Topic basics 1 (e.g., CNNs for vision): customize [5_topic_basics_1.md](5_topic_basics_1.md).
6. Topic basics 2 (e.g., transformers): customize [6_topic_basics_2.md](6_topic_basics_2.md).
7. Advanced usage 1 — reproduce a project baseline: customize [7_advanced_usage_1.md](7_advanced_usage_1.md).
8. Advanced usage 2 — extend and evaluate the baseline: customize [8_advanced_usage_2.md](8_advanced_usage_2.md).
9. Paper reading and annotation: customize [9_paper_reading.md](9_paper_reading.md).
10. Interview or additional topics: customize [10_interview_or_additional_topics.md](10_interview_or_additional_topics.md).

Choose the mathematics, framework, and two foundational topics to match the project. The examples above are illustrative. Keep two distinct advanced-usage tasks: first establish a working baseline, then use it in a controlled extension or adaptation. Task 9 requires structured paper annotation. For Task 10, specify either the interview route or the additional-topic route before assigning it; students do not need to complete both.

Introduce the research question, project lead, communication channel, repository, and data in the project README. Incorporate repository setup into Task 4 rather than assigning a separate project-onboarding task.

The [offboarding checklist](../10_offboarding.md) remains an end-of-quarter requirement, separate from the ten learning tasks in this revised sequence. Existing project folders retain their earlier sequence until their leads revise them; do not assume their current task numbers match this guide.

## Design principles

Each task should contain:

- a single, observable learning objective;
- prerequisites and links to source material;
- a checklist of concrete actions in execution order;
- a deliverable with an explicit format, scope, and submission location;
- evaluation criteria that can be checked consistently;
- a fallback for unavailable hardware, failed experiments, or inaccessible data;
- resource-cleanup instructions for compute tasks.

Prefer public documentation over private Notion resources when available. Do not include Notion database fields such as `Status`, `Quarter`, template labels, emoji callouts, or duplicate project headings. State what evidence and analysis a submission must contain. Keep compute and reading workloads within the weekly time budget.

## Creating or revising a track

1. Create `onboarding/proj_<short_name>/` with a project `README.md`, or revise the existing track in place.
2. Link to the shared Task 1 and copy Tasks 2–10 from this folder.
3. Replace every bracketed placeholder, select project-specific resources and exercises, and remove inapplicable instructions. Specify prerequisites, evaluation criteria, and a workable fallback for each task.
4. In the project README, name the lead and communication channel; describe the research question, repository, data, and baseline; and link to the project page, reading list, and published papers. Use `Not currently available` for missing metadata.
5. List all ten tasks in order and link separately to the end-of-quarter offboarding checklist. When revising an existing track, replace superseded task files and update references so each number has one assignment.
6. Check numbering, relative links, expected runtime, compute requirements, and submission instructions.
7. Ask another project member to complete a dry run before assigning the track.

## Review checklist

- [ ] The README links to Task 1 and files numbered 2–10, with no duplicate numbers.
- [ ] Each H1 matches its filename and task number.
- [ ] The project README introduces the research question, people, communication channel, repository, and baseline.
- [ ] Task 3 teaches project-relevant mathematics; Task 4 teaches the required framework.
- [ ] Tasks 5 and 6 introduce two clearly identified foundational topics.
- [ ] Tasks 7 and 8 provide distinct advanced practice, with Task 8 building on Task 7.
- [ ] Task 9 requires structured annotation of a project paper.
- [ ] Task 10 specifies an interview or an additional topic and the corresponding deliverable.
- [ ] Offboarding is linked separately from the ten learning tasks.
- [ ] Resource links are accessible, and commands contain no credentials or machine-specific paths.
- [ ] Compute tasks explain how to stop or delete resources.
- [ ] Deliverables and evaluation criteria allow consistent grading.
- [ ] All placeholders are replaced and project metadata is current.
