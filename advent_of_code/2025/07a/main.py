from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    splits = 0
    
    # -1-1j  -1  -1+1j
    #   -1j   X    +1j
    # +1-1j  +1  +1+1j
    stack = set()
    edges = dict()
    visited = set()

    # Building DAG
    for x, row in enumerate(test_input):
        for y, symbol in enumerate(row):
            coords = x + y*1j
            if symbol in ("S", "."):
                if symbol == "S":
                    stack.add(coords)
                edges[coords] = set([coords + 1])  # Down
            elif symbol == "^":
                edges[coords] = {
                    coords - 1j,  # Left
                    coords + 1j,  # Right
                }

    # Going through DAG
    while stack:
        current = stack.pop()
        visited.add(current)
        try:
            next_nodes = edges[current]
        except KeyError:
            continue
        if len(next_nodes) == 2:
            splits += 1
        stack = stack | next_nodes - visited

    yield splits


if __name__ == "__main__":
    setup(main)