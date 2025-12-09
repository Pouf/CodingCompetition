from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    splits = 0
    
    # -1-1j  -1  -1+1j
    #   -1j   X    +1j
    # +1-1j  +1  +1+1j
    stack = set()
    edges = dict()

    # Building DAG
    for x, row in enumerate(test_input):
        for y, symbol in enumerate(row):
            coords = x + y*1j
            if symbol in ("S", "."):
                if symbol == "S":
                    stack.add(coords)
                edges[coords] = set(coords + 1)  # Down
            elif symbol == "^":
                edges[coords] = {
                    coords - 1j,  # Left
                    coords + 1j,  # Right
                }

    # Going through DAG
    while stack:
        current = stack.pop()
        next = edges[current]
        if len(next) == 2:
            splits += 1
        visited.add(current)
        stack = stack | next - visited

    yield splits


if __name__ == "__main__":
    setup(main)