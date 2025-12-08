from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    result = 0

    DIRECTIONS = (
        -1-1j, -1, -1+1j,
          -1j,       +1j,
        +1-1j, +1, +1+1j,
    )
    result = 0
    floor_plan = dict()
    for x, row in enumerate(test_input):
        for y, symbol in enumerate(row):
            floor_plan[x+y*1j] = symbol == "@"

    
    yield result



if __name__ == "__main__":
    setup(main)