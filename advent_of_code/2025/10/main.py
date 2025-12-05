import typing
from utils import setup
from collections import deque


def main(test_input: list[str]) -> typing.Iterator[typing.Any]:
    result = 0
    ranges = set()
    for line in test_input:
        try:
            start, stop = map(int, line.split("-"))
            ranges.add((start, stop + 1))
        except ValueError:
            break

    sorted_ranges = deque(sorted(ranges))
    while sorted_ranges:
        start, stop = sorted_ranges.popleft()
        # print(f"==>> {start}-{stop}")
        while sorted_ranges:
            next_start, next_stop = sorted_ranges[0]
            # print(f"==>> next {next_start}-{next_stop} {next_start <= stop}")
            if next_start <= stop:
                stop = max(stop, next_stop)
                sorted_ranges.popleft()
            else:
                break
        # print(f"==>> stop - start: {stop - start}")
        result += stop - start
    # print(f"==>> result: {result}")

    yield result


if __name__ == "__main__":
    setup(main)
