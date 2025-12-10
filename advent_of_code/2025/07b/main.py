from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    """
    Directions:
    -1-1j  -1  -1+1j
      -1j   X    +1j
    +1-1j  +1  +1+1j
    """
    result = 0
    floor_plan = dict()
    stack: list[complex] = []

    # Building nodes
    for x, row in enumerate(test_input):
        if x % 2:
            continue  # Skip useless empty rows
        for y, symbol in enumerate(row):
            coords = x//2 + y*1j
            floor_plan[coords] = symbol
            if symbol == "S":
                stack.append(coords)

    # DAG traversal
    while stack:
        current = stack.pop()
        down = current + 1
        symbol_below = floor_plan.get(down)
        if symbol_below in ("S", "."):
            stack.append(down)
        elif symbol_below == "^":
            down_left = down - 1j
            down_right = down + 1j
            stack += [down_left, down_right]
        elif symbol_below is None:
            result += 1

    yield result


if __name__ == "__main__":
    setup(main)