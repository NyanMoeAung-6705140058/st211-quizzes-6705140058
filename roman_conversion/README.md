# Week 1: Roman Numeral Converter

Course: 192-211 Automated Software Testing  

## Student Information

- **Name:** Nyan Moe Aung
- **Student ID:** 6705140058

## Objective

Convert Roman numerals into integers and use automated tests to check normal, boundary, and invalid inputs.

## Project Files

- `roman.py` — Roman numeral conversion function.
- `test_roman.py` — Automated tests using pytest.

## Conversion Rules

| Symbol | Value |
|--------|-------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Symbols are normally added together. A smaller symbol before a larger symbol is subtracted.

Valid subtractive pairs: `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`.

This implementation accepts standard uppercase Roman numerals from **1 to 3999**.

## Usage

```python
from roman import convert

print(convert("I"))         # 1
print(convert("VI"))        # 6
print(convert("XIX"))       # 19
print(convert("MCMXCIV"))   # 1994
print(convert("MMXXVI"))    # 2026
```

Invalid Roman numeral strings raise `ValueError`. Non-string inputs raise `TypeError`.

## Install and Run Tests

Run these commands inside the project folder:

```bash
python -m pip install pytest
python -m pytest -v
```

## Test Coverage

The test suite includes 90 test cases covering:

- Lecture examples: `I` and `VI`.
- All seven basic symbols.
- Repeated symbols and additive notation.
- All six subtractive pairs.
- Mixed addition and subtraction.
- Boundary values and notation changes.
- Invalid ordering, repetition, and formatting.
- Non-string inputs.

Example test:

```python
import pytest
from roman import convert


@pytest.mark.parametrize(
    "number, expected",
    [
        ("I", 1),
        ("VI", 6),
        ("IV", 4),
        ("IX", 9),
        ("XIX", 19),
    ],
)
def test_convert(number, expected):
    assert convert(number) == expected
```

Expected result for the complete test suite:

```text
90 passed
```

## Learning Outcome

Systematic testing checks different input categories and boundaries. It gives better coverage than checking only a few examples.
