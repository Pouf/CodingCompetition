def checkio(numbers):
    paths = [[numbers[0]]]
    while True:
        p = paths.pop(0)
        for c in set(numbers)-set(p):
            if sum(x!=y for x, y in zip(str(p[-1]), str(c))) == 1:
                if c == numbers[-1]:
                    return p + [c]
                paths.append(p + [c])
