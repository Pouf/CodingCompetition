from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    result = 0
    yield result


if __name__ == "__main__":
    setup(main)
