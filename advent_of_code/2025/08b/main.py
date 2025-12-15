from typing import Iterator, Any
from utils import setup
import numpy as np
from scipy.spatial.distance import cdist


def main(test_input: Iterator[str]) -> Iterator[Any]:
    points = np.array([
        [int(x) for x in line.split(",")]
        for line in test_input
    ])

    distances = cdist(points, points)

    # Build list of pairs of points sorted by distance
    pairs: dict[float, set[frozenset[int]]] = dict()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = distances[i, j]
            if distance:
                pairs.setdefault(distance, set()).add(frozenset((i, j)))

    result = connect_junctions(pairs, points)

    yield result


def connect_junctions(pairs: dict[float, set[frozenset[int]]], points: np.ndarray) -> int:
    graphs = [set([i]) for i in range(len(points))]
    min_distances = sorted(pairs.keys())

    for distance in min_distances:
        for p1, p2 in pairs[distance]:
            in_graphs = []
            for i, graph in enumerate(graphs):
                if p1 in graph or p2 in graph:
                    if {p1, p2} < graph:
                        # both points are already in a graph
                        break
                    in_graphs.append(i)
            else:
                if len(in_graphs) == 1:
                    graphs[in_graphs.pop()] |= {p1, p2}
                else:
                    a, b = in_graphs
                    graphs[a] |= graphs[b] | {p1, p2}
                    del graphs[b]

            if len(graphs) == 1:
                return points[p1][0] * points[p2][0]
    return points[p1][0] * points[p2][0]


if __name__ == "__main__":
    setup(main)
