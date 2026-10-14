import re


def convert(number: str) -> int:
    if not isinstance(number, str):
        raise TypeError("Roman numeral must be a string")

    pattern = (
        r"M{0,3}"
        r"(CM|CD|D?C{0,3})"
        r"(XC|XL|L?X{0,3})"
        r"(IX|IV|V?I{0,3})"
    )

    if not number or re.fullmatch(pattern, number) is None:
        raise ValueError("Invalid Roman numeral")

    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0

    for index, symbol in enumerate(number):
        value = values[symbol]

        if (
            index + 1 < len(number)
            and value < values[number[index + 1]]
        ):
            total -= value
        else:
            total += value

    return total