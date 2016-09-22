import fractions
from itertools import permutations

def solve(i, d):
    F, d = d
    N, F = F.split()
    N = int(N)
    F = fractions.Fraction(F).limit_denominator(100)
    top, bot = F.numerator, F.denominator
    bF = '1'*top + '0'*(bot-top)
    indexes = []
    for r in range(1, 3):
        sBF = bF*r
        possibilities = set([''.join(p) for p in permutations(sBF)])
        for p in possibilities:
            if p in d:
                indexes.append(d.index(p))
    return i, min(indexes or [0])


# solve(5, ['15 0.333333', '000000000011000'])