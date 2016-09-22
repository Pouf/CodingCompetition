def checkio(m):
    size = len(m)
    searched = [[0 for i in range(size)] for i in range(size)]
    def lookup(x, y, val):
        if not size > y >= 0 <= x < size or searched[x][y]:
            return 0
        current = m[x][y]
        if current == val:
            searched[x][y] = total = 1
            total += lookup(x-1, y, current)
            total += lookup(x+1, y, current)
            total += lookup(x, y-1, current)
            total += lookup(x, y+1, current)
            return total
        return 0
    total = max([lookup(x, y, m[x][y]), m[x][y]] for x in range(size) for y in range(size))
    return total
