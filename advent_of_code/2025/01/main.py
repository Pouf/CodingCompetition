from __future__ import annotations
import collections
import typing
from utils import setup


if typing.TYPE_CHECKING:
    from typing import Iterator, Any


def main(test_input: list[str]) -> Iterator[Any]:
    dial = collections.deque(range(100))
    dial.rotate(50)
    positions = [dial[0]]
    for line in test_input:
        direction = 1 if line[0] == "L" else -1
        steps = int(line[1:])
        dial.rotate(direction * steps)
        positions.append(dial[0])
    yield positions.count(0)


if __name__ == "__main__":
    setup(main)
