from typing import Iterator, Any
from utils import setup


def main(test_input: list[str]) -> Iterator[Any]:
    result = 0
    while test_input:
        result += 1
    yield result


if __name__ == "__main__":
    setup(main)
