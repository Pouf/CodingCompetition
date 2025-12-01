from __future__ import annotations
import typing
from utils import setup


if typing.TYPE_CHECKING:
    from typing import Iterator, Any


def main(test_input: list[str]) -> Iterator[Any]:
    base = 100
    position = 50
    result = 0
    for line in test_input:
        direction = 1 if line[0] == "R" else -1
        steps = int(line[1:])
        if direction == 1:
            result += (position + steps) // 100
        else:
            result += ((100 - position) % 100 + steps) // 100
        position = (position + direction * steps) % base

    yield result


if __name__ == "__main__":
    setup(main)
