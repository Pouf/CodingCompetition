from utils import setup
from typing import Iterator, Any


def main(test_input: list[str]) -> Iterator[Any]:
    edges = dict()
    for line in test_input:
        node, value = line.split(": ")
        edges[node] = frozenset(value.split())

    stack = {"you"}
    complete_paths = set()
    while stack:
        path = stack.pop()
        node = path[-3:]
        for new_node in edges[node]:
            if new_node in path:
                continue
            new_path = f"{path}.{new_node}"
            if new_node == "out":
                print(path)
                complete_paths.add(path)
            stack.add(path)
    yield len(complete_paths)


if __name__ == "__main__":
    setup(main)
