def checkio(c, n):
    c = min(c, n)
    order = ''.join(map(str, range(n))) * 2
    return ','.join(order[i:][:c] for i in range(0, n*2, c))
