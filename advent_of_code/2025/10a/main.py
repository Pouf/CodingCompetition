import re
from functools import reduce
from itertools import combinations
from operator import xor
from typing import Iterator, Any
from utils import setup


def main(test_input: list[str]) -> Iterator[Any]:
    result = 0
    for line in test_input:
        diagram, *wirings, _ = line.split()
        bin_diagram = int(
            diagram
            .strip("[]")
            .replace(".", "0")
            .replace("#", "1"),
            base=2
        )
        bin_wirings = []
        for wire in wirings:
            positions = set(map(int, re.findall(r"\d+", wire)))
            bin_wire = (
                "1" if i in positions else "0"
                for i in range(len(diagram) - 2)
            )
            bin_wirings.append(int("".join(bin_wire), base=2))
        result += match_diagram(
            bin_diagram,
            bin_wirings
        )
    yield result


def match_diagram(diagram: int, wirings: list[int]) -> int:
    if diagram == 0:
        return 0
    for i in range(1, len(wirings) + 1):
        for comb in combinations(wirings, i):
            if reduce(xor, comb, 0) == diagram:
                return i
    return i


if __name__ == "__main__":
    setup(main)
