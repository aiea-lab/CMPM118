# Task 5: Topic Basics 1 — Build a Reproducible Analysis Tool

## Objective and prerequisites

Build on [Task 4's tested module and CI](4_testing_and_ci.md) by turning your experiment analysis into a command-line tool. Practice separating computation from file I/O, defining interface contracts, and testing the complete user workflow. Allow 4–6 hours. Use Python's standard library plus your existing pytest setup.

Read the official [argparse documentation](https://docs.python.org/3/library/argparse.html) and [pytest temporary-file guide](https://docs.pytest.org/en/stable/how-to/tmp_path.html).

## 1. Specify the interface before coding

Keep `analysis.py` and its existing contracts. Add `analyze.py` with this interface, run from your repository root:

```bash
python analyze.py runs.csv --baseline baseline --candidate candidate --output report.json
```

Create `main(argv=None)` returning an exit status, and call it with `raise SystemExit(main())` inside a main guard. Use argparse for help and argument validation. Separate reading, computing, and writing so importing either module has no side effects.

Define and document these behaviors:

- Success writes a UTF-8 JSON report using `build_report`, sorted keys, indentation of 2, and `allow_nan=False`, and returns status 0. Preserve the report schema from Task 4.
- Invalid command-line arguments return status 2 through argparse. Invalid CSV headers, no matched seeds, decoding errors, and file I/O errors produce a concise message on stderr and return status 1.
- Rejected individual CSV rows remain in the report's audit trail; they do not make the whole command fail if valid matched runs remain.
- Refuse to overwrite an existing output file, and refuse an input/output path collision. Leave existing files unchanged. Output parent directories must already exist; report a useful error otherwise.

**Predict:** Which errors belong to argument parsing, data validation, and file access? Why might catching every exception hide a programming defect?

## 2. Implement a small end-to-end example

Create `examples/runs.csv` with two valid matched seeds for each method, one unmatched run, and one rejected record. Calculate the expected accepted count, rejection row number, paired differences, and mean difference by hand before running your tool. Keep this tiny fixture in the repository.

Use `pathlib` for paths and context managers for files. For an output file that must not already exist, consider exclusive creation mode (`"x"`). Complete parsing and analysis before opening the output; remove a newly created partial output if serialization or writing fails. Avoid deleting any pre-existing file. Explain your ordering choices.

Run the documented command, inspect the report, and verify that it matches your independent calculation. Then reorder the valid data rows and explain which output fields should remain invariant and which audit-trail fields may change.

## 3. Test the public workflow

Keep Task 4's unit tests. Add at least eight integration cases using pytest's `tmp_path` and subprocesses. Invoke the tool with `sys.executable` so tests use the current Python environment. Check exit status, stdout/stderr, and file contents where appropriate.

Cover success, help, a missing required argument, missing input, invalid headers, no shared seeds, an existing output, and input/output collision. Include a rejected-row case in the successful report. For failure cases, verify that no new report was created and that existing content was preserved. Avoid depending on your working directory or home directory.

Use the same test command locally and in your existing CI matrix. Add one regression case based on a real bug encountered while implementing the CLI. Explain the behavior it protects.

## 4. Change one design decision

On a practice branch or as a documented patch, change the overwrite policy to permit replacement only when an explicit `--overwrite` flag is supplied. Predict which contracts and tests must change. Demonstrate one updated test that protects the default behavior and one that permits replacement with the flag. Keep your final default conservative and document whether you retained the optional flag.

## Deliverable and evaluation

Submit a repository link, runnable command, example input and expected report, passing local and CI evidence, and a 400–600 word report to Canvas under Deliverable 5. Explain module responsibilities, error handling, the design comparison, one regression, and one remaining limitation. Include versions and installation instructions sufficient for a fresh checkout.

Assessment considers correct behavior at the command-line boundary, preservation of the analysis contracts, meaningful integration tests, and reproducibility. If hosted CI is unavailable, submit the workflow and local output, clearly identifying what was executed. No additional service is required to complete the tool itself.
