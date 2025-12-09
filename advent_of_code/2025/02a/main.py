import typing
from utils import setup


def main(test_input: list[str]) -> typing.Iterator[typing.Any]:
    result = 0
    for line in test_input:
        ranges = line.split(",")
        for range_boundaries in ranges:
            start, stop = map(int, range_boundaries.split("-"))
            for nb in range(start, stop + 1):
                id_ = str(nb)
                length = len(id_)
                if length % 2:
                    continue
                if id_ == 2 * id_[:length // 2]:
                    result += nb

    yield result


if __name__ == "__main__":
    setup(main)
