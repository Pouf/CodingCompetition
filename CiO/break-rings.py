from itertools import *

def break_rings(rings):
    highest = max(chain.from_iterable(rings))
    for x in range(1, highest):
        for c in (combinations(range(1, highest+1), x)):
            if max([len(a-set(c)) for a in rings]) == 1:
                return x
