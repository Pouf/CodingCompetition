from operator import sub
from itertools import combinations


def checkio(cakes):
    distance = lambda v: sum(v[i]**2 for i in range(2))**.5
    normalize = lambda v: ['{:.3f}'.format(v[i]/distance(v)) for i in range(2)]
    vectors = {}
    for a, b in combinations(sorted(cakes), 2):
        vect = list(map(sub, b,a))
        norm = str(normalize(vect))
        try:
            vectors[norm].append(a)
        except KeyError:
            vectors[norm] = [a]
        vectors[norm].append(b)
    vectors = {k:v for k, v in vectors.items() if len(v) > 2}
    linked, result = [], 0
    for k, v in vectors.items():
        s = [p for n,p in enumerate(v) if p not in v[:n]]
        for u in s:
            l = [u] + [v[i+1] for i, p in enumerate(v) if p == u and not i % 2]
            if len(l) > 2:
                if not any(all(e in o for e in l) for o in linked):
                    linked.append(l)
                    result += 1
    return result
