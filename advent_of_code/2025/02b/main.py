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
                limit = length // 2
                for divisor in range(1, limit + 1):
                    if length % divisor:
                        continue
                    dividend = length // divisor
                    if id_ == dividend * id_[:divisor]:
                        result += nb
                        break
    yield result


if __name__ == "__main__":
    setup(main)
