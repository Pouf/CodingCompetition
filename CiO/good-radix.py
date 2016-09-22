from itertools import chain


table = list(map(chr, chain(range(48, 58), range(65, 91))))


def checkio(number):
    kmin = max(table.index(n) for n in number) + 1
    solutions = [k for k in range(kmin, 37) if not int(number, k) % (k-1)]
    return min(solutions or [0])
