import typing
from utils import setup


def main(test_input: list[str]) -> typing.Iterator[typing.Any]:
    DIRECTIONS = (
        -1-1j, -1, -1+1j,
          -1j,        1j,
         1-1j,  1,  1+1j,
    )
    result = 0
    floor_plan = dict()
    for x, row in enumerate(test_input):
        for y, symbol in enumerate(row):
            floor_plan[x+y*1j] = symbol == "@"

    modified = True
    while modified:
        modified = False
        for coords, value in floor_plan.items():
            if not value:
                continue
            nb_rolls_around = sum(
                floor_plan.get(coords + direction, 0)
                for direction in DIRECTIONS)
            if nb_rolls_around < 4:
                floor_plan[coords] = 0
                result += 1
                modified = True
  
    yield result


if __name__ == "__main__":
    setup(main)
