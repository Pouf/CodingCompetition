import typing
from utils import setup


def main(test_input: list[str]) -> typing.Iterator[typing.Any]:
    result = 0
    ranges = set()
    for line in test_input:
        if "-" in line:
            start, stop = map(int, line.split("-"))
            ranges.add(range(start, stop + 1))
        else:
            try:
                is_fresh = any(int(line) in fresh_range for fresh_range in ranges)
                result += int(is_fresh)
            except ValueError:
                continue

    yield result


if __name__ == "__main__":
    setup(main)
