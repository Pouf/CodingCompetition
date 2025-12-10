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

    graphs = get_graphs(pairs, points)
    graphs.sort(key=len, reverse=True)

    yield len(graphs[0]) * len(graphs[1]) * len(graphs[2])


def get_graphs(pairs: dict[float, set[frozenset[int]]], points: np.ndarray) -> list[set[int]]:
    graphs = []
    min_distances = sorted(pairs.keys())
    connections = 0
    for distance in min_distances:
        for p1, p2 in pairs[distance]:
            for graph in graphs:
                if {p1, p2} < graph:
                    break
                if p1 in graph or p2 in graph:
                    graph |= {p1, p2}
                    connections += 1
                    break
            else:
                graphs.append({p1, p2})
                connections += 1
            if connections == len(points):
                return graphs
    return graphs


if __name__ == "__main__":
    setup(main)
