def checkio(m):
    return [tuple(-n for n in m[x])for x in range(len(m))]==list(zip(*m))
