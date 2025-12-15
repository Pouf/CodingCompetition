from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    result = ""
    for line in test_input:
        result += line
    yield result


if __name__ == "__main__":
    setup(main)
