def color_map(region):
    # {'complex coords': country number} dict
    r = {i + j*1j: c for i, row in enumerate(region) for j, c in enumerate(row)}

    countries = max(sum(region, ())) + 1
    neighbors = {c: set() for c in range(countries)}

    for z in r:
        for k in range(4):
            try:
                if r[z + 1j**k] != r[z]:
                    neighbors[r[z]].add(r[z + 1j**k])
            except KeyError:
                pass

    colors = {c: [1,2,3,4] for c in neighbors}
    result = [0] * countries

    for country in neighbors:
        c = colors[country][0]
        result[country] = c
        for i in neighbors[country]:
            if c in colors[i]:
                colors[i].remove(c)

    return result
