import pytest

from roman import convert


# The two checks shown in the lecture.
def test_lecture_examples():
    assert convert("I") == 1
    assert convert("VI") == 6


# Each basic symbol.
@pytest.mark.parametrize(
    "number, expected",
    [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
    ],
)
def test_single_symbols(number, expected):
    assert convert(number) == expected


# Repeated symbols and different symbols added together.
@pytest.mark.parametrize(
    "number, expected",
    [
        ("II", 2),
        ("III", 3),
        ("XX", 20),
        ("XXX", 30),
        ("CC", 200),
        ("CCC", 300),
        ("MM", 2000),
        ("MMM", 3000),
        ("VII", 7),
        ("VIII", 8),
        ("XVI", 16),
        ("LX", 60),
        ("CL", 150),
        ("MD", 1500),
    ],
)
def test_additive_notation(number, expected):
    assert convert(number) == expected


# All six valid subtractive pairs.
@pytest.mark.parametrize(
    "number, expected",
    [
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
    ],
)
def test_subtractive_notation(number, expected):
    assert convert(number) == expected


# Combinations of addition and subtraction.
@pytest.mark.parametrize(
    "number, expected",
    [
        ("XIX", 19),
        ("XXIV", 24),
        ("XLIV", 44),
        ("XCIX", 99),
        ("CDXLIV", 444),
        ("CMXCIX", 999),
        ("MCMXCIV", 1994),
        ("MMXXVI", 2026),
    ],
)
def test_mixed_notation(number, expected):
    assert convert(number) == expected


# Minimum, maximum, and values around notation changes.
@pytest.mark.parametrize(
    "number, expected",
    [
        ("I", 1),
        ("III", 3),
        ("IV", 4),
        ("V", 5),
        ("VIII", 8),
        ("IX", 9),
        ("X", 10),
        ("XXXIX", 39),
        ("XL", 40),
        ("XLI", 41),
        ("LXXXIX", 89),
        ("XC", 90),
        ("XCI", 91),
        ("CCCXCIX", 399),
        ("CD", 400),
        ("CDI", 401),
        ("DCCCXCIX", 899),
        ("CM", 900),
        ("CMI", 901),
        ("MMMCMXCVIII", 3998),
        ("MMMCMXCIX", 3999),
    ],
)
def test_boundaries(number, expected):
    assert convert(number) == expected


# Invalid ordering, repetition, characters, and formatting.
@pytest.mark.parametrize(
    "number",
    [
        "",
        "VX",
        "XXC",
        "IIII",
        "VV",
        "XXXX",
        "LL",
        "CCCC",
        "DD",
        "MMMM",
        "IL",
        "IC",
        "ID",
        "IM",
        "XD",
        "XM",
        "IIV",
        "IVIV",
        "IXIX",
        "CMCM",
        "ABC",
        "123",
        "iv",
        " IV",
        "IV ",
        "I V",
        "IV\n",
    ],
)
def test_invalid_numerals(number):
    with pytest.raises(ValueError, match="Invalid Roman numeral"):
        convert(number)


# Inputs that are not strings.
@pytest.mark.parametrize(
    "number",
    [
        None,
        123,
        4.0,
        ["I"],
        {"I": 1},
        True,
    ],
)
def test_non_string_inputs(number):
    with pytest.raises(
        TypeError,
        match="Roman numeral must be a string",
    ):
        convert(number)