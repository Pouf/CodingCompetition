from typing import Iterator, Any
from utils import setup
from shapely import Point, Polygon


def main(test_input: Iterator[str]) -> Iterator[Any]:
    points = []
    for line in test_input:
        points.append(Point(*(int(x) for x in line.split(","))))
    polygon = Polygon(points)
    areas = (
        area(p1, p2) for i, p1 in enumerate(points) for p2 in points[i + 1 :]
        if polygon.contains(Polygon([
            p1,
            (p1.x, p2.y),
            p2,
            (p2.x, p1.y),
        ]))
    )
    yield max(areas)


def area(p1: Point, p2: Point) -> int:
    return int((abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1))


if __name__ == "__main__":
    setup(main)
