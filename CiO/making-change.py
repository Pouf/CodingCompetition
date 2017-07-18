def checkio(price, denominations):
    if price < min(denominations):
        return None
    m = [[0] * (price + 1) for _ in range(len(denominations) + 1)]
    for i in range(price + 1):
        m[0][i] = i

    for c in range(0, len(denominations)):
        for r in range(1, price + 1):
            if denominations[c] == r:
                m[c + 1][r] = 1
                if 0 < price - r < min(denominations):
                    return None

            elif denominations[c] < r:
                m[c + 1][r] = min(m[c][r], 1 + m[c + 1][r - denominations[c]])

            else:
                m[c + 1][r] = m[c][r]

    return m[-1][-1]
