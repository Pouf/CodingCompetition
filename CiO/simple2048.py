def move2048(state, move):
    rotCW = lambda d:[[v for v in r] for r in zip(*d[::-1])]
    rotCCW = lambda d:[[v for v in r] for r in list(zip(*d))[::-1]]
    sym = lambda d:[r[::-1] for r in d]
    transorm = {'right': ['sym', 'sym'],
             'up': ['rotCCW', 'rotCW'],
             'down': ['rotCW', 'rotCCW']}.get(move)

    # rotate or apply a symetry to the matrix, depending on the move
    new = eval('{}(state)'.format(transorm[0])) if transorm else state[:]

    for row in new:
        if 0 in row:
            while True:
                zero = row.index(0)
                if zero < 3 and set(row[zero:])-{0}:
                    # offset to the left
                    row[zero:] = row[zero+1:] + [0]
                else:
                    break
        for c, val in enumerate(row):
            if c == len(row)-1:
                continue
            if val == row[c+1]:
                if val == 1024:
                    return [['U','W','I','N']]*4
                # multiply by 2, skip the next, offset the others to the left
                row[c:] = [row[c]*2] + row[c+2:] + [0]

    new = eval('{}(new)'.format(transorm[1])) if transorm else new[:]
    
    try:
        # flatten the matrix, reverse it, look for the first zero
        lastZero = 15-sum(new, [])[::-1].index(0)
        new[lastZero//4][lastZero%4] = 2
    except:
        if new == state:
            return [['G','A','M','E'], ['O','V','E','R']]*2
    return new
