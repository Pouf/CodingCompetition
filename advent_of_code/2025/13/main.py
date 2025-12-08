from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    splits = 0
    
    # -1-1j  -1  -1+1j
    #   -1j   X    +1j
    # +1-1j  +1  +1+1j
    stack = set()
    floor_plan = dict()
    for x, row in enumerate(test_input):
        for y, symbol in enumerate(row):
            floor_plan[x+y*1j] = symbol
            if symbol == "S":
                stack.add(x+1 + y*1j})
    
    while stack:
        current = stack.pop()
        visited.add(current)
        if floor_plan[current] == ".":
            down = current + 1
            stack.add(down)
        next = floor_plan[down]
        if next == "^":
            left = current
        stack -= visited

    yield splits


if __name__ == "__main__":
    setup(main)