# Quiz 02 - letter_grade

Maps a numeric score to a letter grade (A, B, C, or F).
Raises ValueError for scores outside the valid range 0-100.

## Files

- `solution.py` - the `letter_grade(score)` function
- `test_solution.py` - boundary tests for each grade and the invalid input case

## How to run

    python -m pytest test_solution.py -v

## Sample output

    test_solution.py::test_boundary_a_grade PASSED
    test_solution.py::test_boundary_pass_fail PASSED
    test_solution.py::test_minimum_valid PASSED
    test_solution.py::test_maximum_valid PASSED
    test_solution.py::test_below_minimum_invalid PASSED
    5 passed in 0.03s
