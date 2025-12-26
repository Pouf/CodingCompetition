import re
from typing import Iterator, Any
from utils import setup
from z3 import IntVector, Optimize, Sum


def main(test_input: list[str]) -> Iterator[Any]:
    result = 0
    for line in test_input:
        _, *raw_buttons, raw_requirement = line.split()
        requirement = (int(x) for x in re.findall(r"\d+", raw_requirement))
        buttons = [[int(x) for x in re.findall(r"\d+", rb)] for rb in raw_buttons]
        B = IntVector("B", len(buttons))
        solver = Optimize()
        for i, req in enumerate(requirement):
            solver.add(Sum([B[j] for j, btn in enumerate(buttons) if i in btn]) == req)
        solver.add([b >= 0 for b in B])
        solver.minimize(Sum(B))
        solver.check()
        result += solver.model().eval(Sum(B)).as_long()
    yield result


if __name__ == "__main__":
    setup(main)
