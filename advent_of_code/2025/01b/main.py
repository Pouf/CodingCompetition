import collections
from typing import Iterator, Any
from utils import setup


def main(test_input: list[str]) -> Iterator[Any]:
    dial = collections.deque(range(100))
    dial.rotate(50)
    result = 0
    for line in test_input:
        direction = 1 if line[0] == "L" else -1
        steps = int(line[1:])
        if direction == 1:
            result += ((100 - dial[0]) % 100 + steps) // 100
        else:
            result += (dial[0] + steps) // 100
        dial.rotate(direction * steps)

    yield result


if __name__ == "__main__":
    setup(main)
