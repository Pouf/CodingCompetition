from functools import cache
from typing import Iterator, Any
from utils import setup


def main(test_input: list[str]) -> Iterator[Any]:
    global edges
    edges = {"out": frozenset()}
    for line in test_input:
        node, value = line.split(": ")
        edges[node] = frozenset(value.split())
    svr_dac_fft_out = get_nb_paths("svr", "dac") * get_nb_paths("dac", "fft") * get_nb_paths("fft", "out")
    svr_fft_dac_out = get_nb_paths("svr", "fft") * get_nb_paths("fft", "dac") * get_nb_paths("dac", "out")
    yield svr_dac_fft_out + svr_fft_dac_out


@cache
def get_nb_paths(start, goal) -> int:
    return start == goal or sum(
        get_nb_paths(node, goal)
        for node in edges[start]
    )


if __name__ == "__main__":
    setup(main)
