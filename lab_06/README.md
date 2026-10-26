# Lab 6: Mocking and Test Doubles

This project contains the Python examples from pages 1–26 of the **Mocking and Test Doubles** lab for **192-211 Automated Software Testing**, International College, Siam University.

The examples demonstrate how mocks replace unpredictable dependencies, provide controlled return values, and help test application logic.

## Requirements

- Python 3
- pytest
- Git Bash on Windows

`unittest.mock` is included with Python and requires no separate installation.

## Files

| File | Purpose |
|---|---|
| `weather.py` | Generates a random temperature and returns a weather description. |
| `test_problem.py` | Demonstrates a weak test that checks whether the description is one of four allowed values. |
| `test_solution_preview.py` | Uses `patch()` to test specific temperatures and their expected descriptions. |
| `test_mock_basics.py` | Demonstrates mock return values, arbitrary method calls, and stored attributes. |
| `payment.py` | Demonstrates dependency injection with a payment gateway and an order processor. |

## Setup on Windows Using Git Bash

Open Git Bash in the project folder.

Create a virtual environment:

```bash
py -m venv venv
```

If Python is available through `python` instead of `py`, use:

```bash
python -m venv venv
```

Activate the environment:

```bash
source venv/Scripts/activate
```

Install pytest:

```bash
python -m pip install pytest
```

## Run the Tests

Run all tests included in pages 1–26:

```bash
python -m pytest test_problem.py test_solution_preview.py test_mock_basics.py -v
```

The expected result is **6 passed**:

| Test file | Number of tests |
|---|---:|
| `test_problem.py` | 1 |
| `test_solution_preview.py` | 2 |
| `test_mock_basics.py` | 3 |

## Weather Example

`get_temperature()` generates a random integer between −10 and 40.

`describe_weather()` converts the temperature into a description:

| Temperature | Description |
|---|---|
| Below 0 | `Freezing` |
| 0 to below 15 | `Cold` |
| 15 to below 25 | `Pleasant` |
| 25 or above | `Hot` |

The test in `test_problem.py` checks only whether the result is an allowed description. It cannot verify a specific branch because the temperature is random.

`test_solution_preview.py` replaces `weather.get_temperature` using `patch()`. This allows the tests to verify that 30 returns `Hot` and −5 returns `Freezing` consistently.

## Mock Basics

`test_mock_basics.py` demonstrates three capabilities:

- **Controlled return values:** `return_value` specifies what a mocked method returns.
- **Arbitrary method calls:** A basic `Mock` accepts calls without requiring method implementations.
- **Stored attributes:** Values can be assigned to a mock and read back.

The arbitrary-call example contains no assertion. It demonstrates that the calls are accepted without raising an exception.

## Payment Example

`payment.py` defines two classes:

- `PaymentGateway` represents an external payment service. Its `charge()` method raises `NotImplementedError` because no real payment integration is provided.
- `OrderProcessor` receives a gateway through its constructor. Its `process()` method rejects amounts of zero or less, calls the gateway for positive amounts, and formats the returned result.

Passing the gateway into `OrderProcessor` is called **dependency injection**. It allows a test to provide a mock gateway with a controlled response.

Pages 1–26 introduce this implementation. The payment test begins on page 27.

## Key Learning Points

- Mocks help isolate application logic from external dependencies.
- Patching randomness makes tests repeatable.
- Precise assertions provide stronger checks than checking a list of possible results.
- Dependency injection makes collaborators easier to replace during testing.
- Patch a dependency where the code under test looks it up.
