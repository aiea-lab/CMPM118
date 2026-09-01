# Guide to Creating Project Onboarding Tasks

Each onboarding track contains ten weekly tasks. Tasks 1, 2, and 10 are shared:

1. Lab onboarding: [`../1_onboarding.md`](../1_onboarding.md)
2. Nautilus onboarding: use [`2_nautilus.md`](2_nautilus.md) as the source template
3. Project onboarding: customize [`3_project_onboarding.md`](3_project_onboarding.md)
4. Reproduce a baseline: customize [`4_reproduce_a_baseline.md`](4_reproduce_a_baseline.md)
5. Paper annotation: customize [`5_paper_annotation.md`](5_paper_annotation.md)
6. Extend the baseline: customize [`6_extend_the_baseline.md`](6_extend_the_baseline.md)
7. Evaluate an extension: customize [`7_evaluate_the_extension.md`](7_evaluate_the_extension.md)
8. Analyze failures: customize [`8_failure_analysis.md`](8_failure_analysis.md)
9. Propose a research direction: customize [`9_research_proposal.md`](9_research_proposal.md)
10. Lab offboarding: [`../10_offboarding.md`](../10_offboarding.md)

The seven project-specific templates are suggestions, not a required research sequence. A project lead may replace Tasks 4–9 when another progression better fits the project, but Task 3 should remain project onboarding and Task 5 should remain a paper annotation.

## Design principles

Each task should be achievable in roughly one week and should contain:

- a single, observable learning objective;
- prerequisites and links to stable source material;
- a checklist of concrete actions in the order students should perform them;
- a deliverable with an explicit format, scope, and submission location;
- evaluation criteria that can be checked consistently;
- a fallback path for unavailable hardware, failed experiments, or inaccessible data;
- safety and resource-cleanup instructions where applicable.

Prefer public documentation over links to private Notion pages. Do not include Notion database fields such as `Status`, `Quarter`, template labels, emoji callouts, or duplicate project headings. Avoid phrases such as “write about what you did”; state what evidence and analysis the submission must contain.

## Creating a new track

1. Create `onboarding/proj_<short_name>/` and add a project `README.md`.
2. Copy Tasks 2–9 from this folder into it.
3. Replace every bracketed placeholder and remove instructions that do not apply.
4. In the project README, name the lead and link to the project page, reading list, and published papers. Use `Not currently available` rather than inventing missing metadata.
5. Check numbering, relative links, expected runtime, compute requirements, and submission instructions.
6. Ask another project member to complete a dry run before assigning the track.

## Review checklist

- [ ] Files are named `2_...md` through `9_...md`, with no duplicate numbers.
- [ ] The H1 title matches the filename and task number.
- [ ] Task 3 introduces the project, repository, communication channel, and baseline.
- [ ] Task 5 requires structured annotation of a project paper.
- [ ] Every external link is still accessible.
- [ ] Commands do not contain credentials or machine-specific paths.
- [ ] Compute tasks explain how to stop or delete resources.
- [ ] Deliverables are specific enough for two reviewers to grade consistently.
- [ ] The project README metadata is current.

