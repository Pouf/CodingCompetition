def checkio(board):
    r = range(3)
    lines = [set(l) for l in board]
    lines += [{board[a][i] for a in r} for i in r]
    lines += [{board[i][i] for i in r}, {board[i][2-i] for i in r}]
    for line in lines:
        if len(line) == 1 and '.' not in line:
            return line.pop()
    return 'D'
