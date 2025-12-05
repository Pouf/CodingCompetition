import typing
from utils import setup


def main(test_input: list[str]) -> typing.Iterator[typing.Any]:
    result = 0

    ranges = set()
    for line in test_input:
        try:
            start, stop = map(int, line.split("-"))
            ranges.add((start, stop + 1))
        except ValueError:  # Empty line
            break

    sorted_ranges = sorted(ranges, reverse=True)
    while sorted_ranges:
        start, stop = sorted_ranges.pop()
        while sorted_ranges:
            next_start, next_stop = sorted_ranges[-1]
            if next_start <= stop:
                stop = max(stop, next_stop)
                sorted_ranges.pop()
            else:
                break
        result += stop - start

    yield result


if __name__ == "__main__":
    setup(main)
