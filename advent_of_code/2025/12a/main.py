import re
from typing import Iterator, Any
from utils import setup


def main(test_input: list[str]) -> Iterator[Any]:
    result = 0

    for line in test_input:
        if "x" in line:
            width, height, *presents = map(int, re.findall(r"\d+", line))
            result += (width // 3 * height // 3 >= sum(presents))
    yield result


if __name__ == "__main__":
    setup(main)
