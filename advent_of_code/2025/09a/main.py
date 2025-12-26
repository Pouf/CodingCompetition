from typing import Iterator, Any
from utils import setup


def main(test_input: list[str]) -> Iterator[Any]:
    points = []
    for line in test_input:
        points.append(tuple(int(x) for x in line.split(",")))
    areas = (area(p1, p2) for i, p1 in enumerate(points) for p2 in points[i + 1 :])
    yield max(areas)


def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


if __name__ == "__main__":
    setup(main)
