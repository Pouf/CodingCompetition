def count_gold(pyramid):
    paths = list(pyramid[-1])
    for v in pyramid[-2::-1]:
        for i,g in  enumerate(v):
            paths[i] = max(paths[i]+g, paths[i+1]+g)
        paths.pop()
    return paths[0]
