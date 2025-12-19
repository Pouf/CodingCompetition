from utils import setup
from typing import Iterator, Any


def main(test_input: list[str]) -> Iterator[Any]:
    result = 0
    for line in test_input:
        result += 1
    yield result


if __name__ == "__main__":
    setup(main)
