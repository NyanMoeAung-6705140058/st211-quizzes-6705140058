# Quiz 01 - BankAccount

A BankAccount class with deposit and withdraw.
Raises ValueError for non-positive amounts and for withdrawing more than the balance.

## Files

- `solution.py` - the BankAccount class
- `test_solution.py` - basic deposit tests
- `test_independent.py` - deposit and withdraw tested with fresh accounts
- `test_named.py` - named tests for deposit and withdraw behavior

## How to run

    python -m pytest -v

## Sample output

    test_solution.py::test_deposit_increases_balance PASSED
    test_named.py::test_deposit_positive_amount_increases_balance PASSED
    test_named.py::test_deposit_negative_amount_raises_value_error PASSED
    test_named.py::test_withdraw_more_than_balance_raises_value_error PASSED
    test_named.py::test_withdraw_exact_balance_leaves_zero PASSED
    5 passed in 0.05s
