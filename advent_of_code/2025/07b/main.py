from functools import cache
from typing import Iterator, Any
from utils import setup


def main(test_input: list[str]) -> Iterator[Any]:
    nodes = tuple(test_input)
    start = (0, nodes[0].index("S"))
    yield get_nb_paths(start, nodes)


@cache
def get_nb_paths(start, nodes: tuple[str, ...]) -> int:
    neighbors = get_neighbors(start, nodes)
    if not neighbors:
        return 1
    return sum(
        get_nb_paths(node, nodes)
        for node in neighbors
    )


def get_neighbors(start: tuple[int, int], nodes: tuple[str, ...]) -> set[tuple[int, int]]:
    x, y = start
    try:
        symbol_below = nodes[x + 2][y]
    except IndexError:
        return set()

    if symbol_below == "^":
        down_left = (x + 2, y - 1)
        down_right = (x + 2, y + 1)
        return {down_left, down_right}

    else:  # `S` or `.`
        down = (x + 2, y)
        return {down}


if __name__ == "__main__":
    setup(main)