from itertools import groupby

def total_cost(calls):
    total = 0
    for k,g in groupby(calls, lambda x:x[:10]):
        minutes = sum(-(-int(l[20:])//60) for l in g)
        total += (minutes, 2*minutes-100)[minutes>100]
    return total
