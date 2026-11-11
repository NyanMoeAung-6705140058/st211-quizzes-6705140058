# Lab 6: Mocking and Test Doubles

**Course:** 192-211 Automated Software Testing  
**Student:** Nyan Moe Aung  
**Student ID:** 6705140058  

## Overview

This lab uses Python, pytest, and unittest.mock to test code without calling real external services. The examples control weather data, replace a payment gateway, prevent real emails, verify method calls, simulate network failures, test retries, and fix the time during a test.

## Learning Objectives

- Create Mock objects and configure return values.
- Use side_effect with a list, an exception, or a function.
- Replace dependencies using patch and patch.object.
- Check how often a method was called and which arguments it received.
- Verify that invalid payment amounts do not trigger a charge.
- Test successful retries and failure after all attempts.

## Files

| File | Purpose |
| --- | --- |
| weather.py | Provides temperatures and describes four weather conditions. |
| payment.py | Defines PaymentGateway and OrderProcessor, including positive-amount validation. |
| notifications.py | Defines email sending and user notification functions. |
| date_utils.py | Provides the year and a report name. |
| retry.py | Retries a payment when ConnectionError occurs. |
| test_problem.py | Shows a weak test that only checks the list of possible weather descriptions. |
| test_solution_preview.py | Tests hot and freezing weather using controlled temperatures. |
| test_mock_basics.py | Tests configured return values, arbitrary calls, and mock attributes. |
| test_payment.py | Tests order processing with an injected mock gateway. |
| test_return_value.py | Tests UserService with a database mock returning Alice. |
| test_return_values.py | Tests a sequence of return values. |
| test_notifications.py | Tests notification without sending a real email. |
| test_date_utils.py | Patches the year to test the report name. |
| test_weather_decorator.py | Uses a patch decorator to test pleasant weather. |
| test_patch_method.py | Replaces PaymentGateway.charge using patch.object. |
| test_verify_calls.py | Checks calls, arguments, and call counts. |
| test_verify_payment.py | Checks the payment amount and prevents charging invalid amounts. |
| test_mock_exceptions.py | Tests a gateway network failure. |
| test_retry.py | Tests success after retries and failure after three attempts. |
| test_mock_time.py | Tests a fixed timestamp. |
| test_side_effect_func.py | Uses a function to double the supplied number. |
| README.md | Explains the lab, commands, and review answers. |

## Setup and Run

Keep all the Python files together in the lab_06 folder. Open a terminal in that folder.

Create a virtual environment:

```bash
python -m venv venv
```

Activate it in Windows Git Bash:

```bash
source venv/Scripts/activate
```

On Linux or macOS, use:

```bash
source venv/bin/activate
```

Install pytest:

```bash
python -m pip install pytest
```

Run all tests:

```bash
python -m pytest -v
```

Run one test file:

```bash
python -m pytest test_retry.py -v
```

unittest.mock is included with Python and does not need a separate installation.

## Expected Results and Verification

The complete file set above contains **24 tests**. The expected result is **24 passed** after using the corrected four-condition weather.py. The last shared test output showed 22 passed and 2 failed before that correction; a successful final run has not yet been provided. Run the command above and keep the actual terminal output or a screenshot as evidence.

The final weather.py must support Freezing, Cold, Pleasant, and Hot. The simpler two-condition slide example does not support the hot and freezing tests. Keep the original payment.py validation so zero or negative amounts are rejected before the gateway is called.

## Review Questions and Answers

### 1. Why should you mock a payment gateway in tests? Give two distinct reasons.

A mock prevents tests from charging real money. It also makes tests fast and repeatable because they do not depend on an internet connection or a working payment service.

### 2. What is the difference between return_value and side_effect?

return_value returns the same configured answer on each call. side_effect can raise an exception, return a sequence of answers, or calculate an answer using a function.

### 3. Module app does import requests and calls requests.get. What do you patch?

Patch `app.requests.get` because that is where the code under test looks up the dependency.

### 4. Why can a mistyped assertion method make a test pass, and how do you prevent it?

Mocks can create missing attributes automatically, so an unprotected typo may call another mock instead of checking anything. Modern Mock rejects many names beginning with assert by default; use valid assertion methods and spec_set or autospec where appropriate to check interfaces and signatures.

### 5. Name one thing you should NOT mock, and say why.

Do not mock the function you are testing because the test would check the mock instead of the real logic. Simple pure functions can usually be tested directly because they are already fast and predictable.

## What I Learned

Mocking lets me control dependencies so I can test one part of a program at a time. I learned to check both returned values and interactions, including failures, retries, and calls that must not happen. When patching, I must replace the name where the code uses it.

## Upload Notes

Upload the Python source files and this README.md to lab_06. Do not upload venv, __pycache__, or .pytest_cache. Replace the earlier weather.py with the corrected four-condition version.
