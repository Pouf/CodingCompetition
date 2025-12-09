from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    result = 0
    
    # -1-1j  -1  -1+1j
    #   -1j   X    +1j
    # +1-1j  +1  +1+1j
    stack = list()
    edges = dict()

    # Building DAG
    for x, row in enumerate(test_input):
        for y, symbol in enumerate(row):
            coords = x + y*1j
            if symbol in ("S", "."):
                if symbol == "S":
                    stack.append(coords)
                edges[coords] = [coords + 1]  # Down
            elif symbol == "^":
                edges[coords] = [
                    coords - 1j,  # Left
                    coords + 1j,  # Right
                ]

    # Going through DAG
    while stack:
        current = stack.pop()
        try:
            next_nodes = edges[current]
        except KeyError:  # Out of bounds !
            result += 1
        else:
            stack += next_nodes

    yield result


if __name__ == "__main__":
    setup(main)