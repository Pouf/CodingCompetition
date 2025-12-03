import typing
from utils import setup


def main(test_input: list[str]) -> typing.Iterator[typing.Any]:
    result = 0
    for line in test_input:
        batteries = list(line)
        best = max(batteries[:-1])
        position = batteries.index(best)
        remaining = batteries[position+1:]
        next_best = max(remaining)
        result += int(f"{best}{next_best}")
  
    yield result


if __name__ == "__main__":
    setup(main)
