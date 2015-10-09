def solve(i, d):
    C, I, prices = d
    C = int(C)
    prices = list(map(int, prices.split()))
    for p1, P1 in enumerate(prices[:-1]):
        remains = C-P1
        left = prices[p1+1:]
        if remains in left:
            result = [p1+1, p1+left.index(remains)+2]
            return i, ' '.join(map(str, result))
