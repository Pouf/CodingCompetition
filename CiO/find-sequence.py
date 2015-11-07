from collections import Counter


def checkio(mat):
    # get a list of numbers that appear at least 4 times in the matrix
    # then start with the most common number
    l = len(mat)
    mat = sum(mat, [])
    mostWanted = [i[0] for i in Counter(mat).most_common() if i[1] > 3]

    for i in mostWanted:
        # filter unnecessary checks
        indices = [j for j, x in enumerate(mat) if x == i]
        for j in indices:
            if mat[j] == i:
                if j < (l-3)*l:
                    # vertical
                    if (mat[j+l], mat[j+2*l], mat[j+3*l]) == (i, i, i): return True
                    # diagonal, top-left to bottom-right
                    if j % l < l-3 and (mat[j+l+1], mat[j+2*l+2], mat[j+3*l+3]) == (i, i, i): return True
                    # diagonal, top-right to bottom-left
                    if j % l > l-3 and (mat[j+l-1], mat[j+2*l-2], mat[j+3*l-3]) == (i, i, i): return True
                # horizontal
                if j % l < l-3 and (mat[j+1], mat[j+2], mat[j+3]) == (i, i, i): return True
    return False
