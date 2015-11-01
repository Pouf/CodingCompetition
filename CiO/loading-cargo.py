from itertools import combinations


def checkio(data):
    sums = set(sum(c) for n in range(len(data)) for c in combinations(data, n+1))
    diffs = set(abs(sum(data) - 2*s) for s in sums)
    return min(diffs)
