from typing import Iterator, Any
from utils import setup
from shapely import Point, Polygon


def main(test_input: Iterator[str]) -> Iterator[Any]:
    points = []
    for line in test_input:
        points.append(Point(*(int(x) for x in line.split(","))))
    polygon = Polygon([point for point in points])
    areas = []
    for point in points:
        for other_point in points:
            if point == other_point:
                continue
            rectangle = Polygon([
                (point.x, point.y),
                (point.x, other_point.y),
                (other_point.x, other_point.y),
                (other_point.x, point.y),
            ])
            if polygon.contains(rectangle):
                areas.append(area(point, other_point))
    yield max(areas)


def area(p1: Point, p2: Point) -> int:
    return int((abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1))


if __name__ == "__main__":
    setup(main)
