import typing
from utils import setup


def main(test_input: list[str]) -> typing.Iterator[typing.Any]:
    result = 0
    for bank in test_input:
        best = max(bank[:-1])
        position = bank.index(best)
        bank = bank[position + 1:]
        next_best = max(bank)
        joltage = f"{best}{next_best}"
        result += int(joltage)
  
    yield result


if __name__ == "__main__":
    setup(main)
