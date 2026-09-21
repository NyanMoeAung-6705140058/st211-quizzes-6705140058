# Quiz 03 - validators

Email and age validation helpers.
- `validate_email(email)` returns True for valid emails, raises ValueError otherwise.
- `validate_age(age)` returns True for ages 0-150, raises ValueError for out-of-range values and TypeError for non-integers.

## Files

- `solution.py` - the `validate_email` and `validate_age` functions
- `test_positive.py` - valid inputs and boundary ages
- `test_negative.py` - invalid inputs that must raise

## How to run

    python -m pytest -v

## Sample output

    test_positive.py::test_valid_email_accepted PASSED
    test_positive.py::test_valid_email_with_subdomain PASSED
    test_positive.py::test_valid_age_accepted PASSED
    test_positive.py::test_boundary_ages_accepted PASSED
    test_negative.py::test_email_without_at_rejected PASSED
    test_negative.py::test_email_without_domain_rejected PASSED
    test_negative.py::test_negative_age_rejected PASSED
    test_negative.py::test_age_as_string_rejected PASSED
    8 passed in 0.05s
