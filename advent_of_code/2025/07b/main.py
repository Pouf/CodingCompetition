from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    result = 0

    # Building DAG
    test_input = list(test_input)
    for x, row in enumerate(test_input):
        if x % 2:
            continue  # Skip useless empty rows
        for y, symbol in enumerate(row):
            if symbol == "S":
                start = (x, y)

    visited: set[complex] = set()
    stack = set(start)

    # DAG traversal
    while stack:
        current = stack.pop()
        neighbors = get_neighbors
        elif symbol_below is None:
            result += 1

    yield result

def get_neighbors(coords, nodes):
    x, y = coords
    down = 
    symbol_below = floor_plan.get(down)
    if symbol_below in ("S", "."):
            stack.append(down)
        elif symbol_below == "^":
            down_left = down - 1j
            down_right = down + 1j
            stack += [down_left, down_right]
    

if __name__ == "__main__":
    setup(main)