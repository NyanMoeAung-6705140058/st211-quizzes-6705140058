# Lab 5: Parameterized and Data-Driven Testing

**Course:** 192-211 Automated Software Testing  
**Name:** Nyan Moe Aung  
**Student ID:** 6705140058

## Overview
This lab uses pytest to run one test with different inputs.

Topics:
- Basic parameterization
- Multiple parameter combinations
- Custom test IDs
- Expected failures with `xfail`
- Parametrized fixtures
- Data-driven tests using JSON and CSV

## Setup
Run in Git Bash on Windows:

```bash
mkdir -p ~/param-lab
cd ~/param-lab
python -m venv venv
source venv/Scripts/activate
python -m pip install pytest
```

## Run All Tests

```bash
python -m pytest -v
```

To display setup, teardown, and printed messages:

```bash
python -m pytest -v -s
```

## Expected Result

```text
55 passed, 1 xfailed
```

The expected failure checks `5 ** 2 == 20`. The actual answer is `25`, so the case is marked with `xfail`.

## Review Answers
1. Stacking 3 values and 4 values creates 12 tests.
2. Custom IDs make test results easier to understand.
3. A parametrized test affects one function. A parametrized fixture affects all tests that use it.
4. Non-programmers can add cases by editing CSV or JSON files without writing Python.
