from typing import Iterator, Any
from utils import setup
from ast import literal_eval
from functools import reduce
from operator import xor
drom itertools import combinations


def main(test_input: Iterator[str]) -> Iterator[Any]:
    result = ""
    for line in test_input:
        diagram, *wirings, _ = line.split()
        bin_diagram = int(
            diagram
            .strip("[]")
            .replace(".", "0")
            .replace("#", "1"),
            base=2
        )
        base = "0" * (len(diagram) - 2)
        print(base)
        bin_wirings = []
        for wire in wirings:
            bin_wire = base
            for pos in literal_eval(wiring):
                bin_wire[pos] = 1
            bin_wirings.append(int(bin_wire, base=2))
        result += match_diagram(bin_diagram, bin_wirings)


def match_diagram(diagram, wirings) -> int:
    if diagram == 0:
        return 0
    for i in range(1, len(wirings)):
        for comb in combinations(wirings):
            if reduce(xor, comb, 1) == diagram:
                return i


if __name__ == "__main__":
    setup(main)
