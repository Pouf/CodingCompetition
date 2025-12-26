from typing import Iterator, Any
from utils import setup


def main(test_input: list[str]) -> Iterator[Any]:
    result = 0
    for bank in test_input:
        joltage = ""
        for n in range(12):
            best = max(bank[:-12 + n + 1 or None])
            position = bank.index(best)
            bank = bank[position+1:]
            joltage += best
        result += int(joltage)
  
    yield result


if __name__ == "__main__":
    setup(main)
