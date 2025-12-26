from typing import Iterator, Any
from utils import setup


def main(test_input: list[str]) -> Iterator[Any]:
    result = 0

    transposed = zip(*test_input)
    number = 0
    for line in transposed:
        *numbers_as_str, last_char = line
        try:
            new_number = int("".join(numbers_as_str).replace(" ", ""))
        except ValueError:
            continue
        if last_char.strip():
            result += number
            number = new_number
            operator = last_char.strip()
        else:
            if operator == "+":
                number += new_number
            else:
                number *= new_number
    result += number
    yield result



if __name__ == "__main__":
    setup(main)