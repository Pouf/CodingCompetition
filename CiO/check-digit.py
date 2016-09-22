def checkio(data):
    total = 0
    for i, d in enumerate(c for c in reversed(data) if c.isalnum()):
        e = ord(d) - 48
        total += [sum(divmod(e*2, 10)), e][i%2]
    final = [0, 10 - total % 10][bool(total % 10)]
    return [str(final), total]
