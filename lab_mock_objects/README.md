# Lab: Understanding Mock Objects

**Name:** Nyan Moe Aung  
**Student ID:** 6705140058  
**Course:** 192-211 Automated Software Testing

## Overview

This repository contains the six original exercises from the **Understanding Mock Objects** lab.

The exercises use Python’s `unittest.mock.Mock` and pytest to demonstrate default mock behavior, fixed return values, simulated exceptions, sequential responses, and function-based behavior.

## Exercise Files

| File | Description | Expected behavior |
|---|---|---|
| `test_mock_basics.py` | Creates a mock and calls an undefined method. | The method returns another `Mock` object. |
| `test_return_value.py` | Configures a fixed return value. | `get_status()` returns `"OK"`. |
| `test_side_effect_exception.py` | Configures a mock to raise an exception. | `login()` raises `ValueError`, which `pytest.raises()` checks. |
| `test_side_effect_list.py` | Uses a list to provide sequential responses. | Three calls return `"A"`, `"B"`, and `"C"`. |
| `test_side_effect_function.py` | Assigns a function to `side_effect`. | `calculate(5)` executes `double(5)` and returns `10`. |
| `test_comparison.py` | Demonstrates repeated calls with a fixed return value. | Each call to `fetch()` returns `"STATIC"`. |

## Requirements

- Python 3
- pytest

`unittest.mock` is included in Python’s standard library.

## Installation

Download or clone this repository and open its folder in VS Code.

Open **Terminal → New Terminal**, then install pytest:

```bash
python -m pip install pytest
```

## Run All Six Exercises

Run the following command from the folder containing the six test files:

```bash
python -m pytest -v -s
```

Expected result:

```text
6 passed
```

The `-v` option displays detailed test results. The `-s` option displays output from `print()`.

## Run Each Exercise Separately

```bash
python -m pytest test_mock_basics.py -v -s
```

```bash
python -m pytest test_return_value.py -v -s
```

```bash
python -m pytest test_side_effect_exception.py -v -s
```

```bash
python -m pytest test_side_effect_list.py -v -s
```

```bash
python -m pytest test_side_effect_function.py -v -s
```

```bash
python -m pytest test_comparison.py -v -s
```

On Windows, if the `python` command is unavailable but the Python launcher is installed, replace `python` with `py`.

## Key Concepts

### Basic Mock Objects

An unrestricted `Mock` dynamically creates child mocks for ordinary attributes. Calling a mock method returns another mock by default.

### `return_value`

`return_value` specifies a fixed result for a mock call when no active `side_effect` overrides it.

### `side_effect` as an Exception

Assigning an exception to `side_effect` makes the mock raise that exception when called. A test passes when `pytest.raises()` correctly expects it.

### `side_effect` as a List

Each call returns the next item from the list. Calling again after the sequence is exhausted raises `StopIteration`.

### `side_effect` as a Function

The mock passes its arguments to the assigned function and uses the function’s result.

## Scope

This repository includes the six original exercise versions. The lab’s experimental changes can be performed by editing these files and rerunning the relevant tests.
