from functools import reduce
from operator import mul
from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    result = 0

    matrix = (
        (c for c in line.split() if c)
        for line in test_input
    )
    transposed = zip(*matrix)
    for line in transposed:
        *numbers_as_str, operator = line
        numbers = map(int, numbers_as_str)
        if operator == "+":
            result += sum(numbers)
        else:
            result += reduce(mul, numbers, 1)
    yield result


if __name__ == "__main__":
    setup(main)