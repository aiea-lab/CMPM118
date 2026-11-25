# Task 4: Framework Basics — Unit Tests and Continuous Integration

## Objective and prerequisites

Turn your [Task 3](3_python_crash_course.ipynb) experiment-analysis functions into a tested Python module, then run the tests automatically with GitHub Actions. Learn how tests encode behavior, how failures help locate a bug, and how continuous integration (CI) checks a fresh checkout. Allow 4–6 hours. Use your own task repository; no paid services or compute cluster are needed.

Read the [pytest getting-started guide](https://docs.pytest.org/en/stable/getting-started.html) and GitHub's [Python CI guide](https://docs.github.com/en/actions/tutorials/build-and-test-code/python).

## 1. Extract a reusable module

Use this layout at the root of your task repository:

```text
analysis.py
requirements-dev.txt
tests/
    test_analysis.py
.github/
    workflows/
        tests.yml
README.md
```

Move `average`, `parse_runs`, `compare_runs`, and `build_report` into `analysis.py`, keeping their Task 3 contracts. Include their imports. Importing the module must not run a report, print results, or depend on notebook variables. Put any command-line demonstration behind `if __name__ == "__main__":`.

Create an isolated environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
python -m pip freeze > requirements-dev.txt
python --version
```

On Windows use `py -m venv .venv` and `.venv\Scripts\Activate.ps1` in PowerShell. Record your Python and pytest versions. Do not commit `.venv/`, `__pycache__/`, or `.pytest_cache/`; add them to `.gitignore`. The requirements file should capture the clean test environment, not packages from unrelated work.

## 2. Write tests from contracts

Put this starter in `tests/test_analysis.py`:

```python
import pytest
from analysis import average


def test_average_of_known_values():
    assert average([2, 4, 9]) == pytest.approx(5)


def test_empty_average_is_an_error():
    with pytest.raises(ValueError):
        average([])
```

Run `python -m pytest -q` from the repository root. **Predict:** What happens if your file is named `checks.py` instead of `test_analysis.py`? Explain how pytest discovers tests and why an import error differs from a failing assertion.

Write at least **12 independently collected test cases** across all four functions, counting the starter cases. Use `@pytest.mark.parametrize` for at least one related family of cases and a fixture for a small reusable CSV input. Cover:

- Numeric behavior, empty input, and floating-point comparison.
- Required CSV headers; malformed scores, NaN/infinity, and out-of-range scores.
- Duplicate run keys, including an invalid row followed by a valid row with the same key.
- Matched seeds, unmatched seeds, and the absence of any shared seed.
- Input immutability and invariance to accepted-record ordering.
- An integrated report containing the expected accepted count, rejected row numbers, and paired comparison.

A parametrized case counts separately, but repeating one assertion with different constants does not replace coverage of these behaviors. Use independently calculated expected values. Avoid asserting a function's result equals another call to the same function.

## 3. Show that the tests detect a bug

First obtain a passing local run. Then deliberately introduce **two bugs**, one at a time: for example, accept a duplicate key or reverse the sign of a paired difference. Predict which test should fail, run the suite, and record the actual failure. Restore the correct implementation after each experiment. If a bug survives, add a test that catches the missing behavior.

Explain why a green suite is evidence about covered cases rather than proof of correctness for every input.

## 4. Run the suite in CI

Create `.github/workflows/tests.yml` in your task repository using this baseline:

```yaml
name: Python tests
on: [push, pull_request]
permissions:
  contents: read
jobs:
  tests:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install test dependencies
        run: python -m pip install -r requirements-dev.txt
      - name: Run tests
        run: python -m pytest -q
```

Push your working branch and inspect the Actions logs. Explain each step, why the Python versions are quoted, and why CI installs dependencies again. Confirm both matrix jobs run successfully.

On a practice branch, commit one of your demonstrated bugs, observe a failing CI run, then fix it and show the passing run. Keep the default branch working. Do not disable tests or mark the intentional failure as expected to make CI pass. This workflow tests code; deployment is outside this assignment.

## Deliverable and evaluation

Submit a repository link, links or screenshots for failing and passing CI runs, local pytest output, and a 400–600 word report to Canvas under Deliverable 4. Include exact setup commands, versions, a table mapping behaviors to tests, the two bug experiments, and one remaining testing limitation. A fresh checkout must reproduce the local suite using `python -m pip install -r requirements-dev.txt` and `python -m pytest -q`.

Assessment considers behavior coverage, failure diagnosis, isolation from notebook state, and reproducibility locally and in CI. If GitHub Actions is unavailable, submit the workflow and clean-environment local output for both Python versions where available. Document what you could run; do not describe local output as an observed CI result. Ask the project lead about unavailable Python versions rather than inventing results.
