def can_pass(matrix, first, second):
    d = matrix[first[0]][first[1]]
    m = {i+1j*j for i, row in enumerate(matrix) for j, n in enumerate(row) if n == d}
    stack = {complex(*first)}

    while stack:
        m -= stack
        stack = {z+1j**k for z in stack for k in range(4)} & m
        if complex(*second) in stack:
            return 1
