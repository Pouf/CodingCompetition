def count_inversion(sequence):
    inversions = 0
    for i,v in enumerate(sequence):
        for k in sequence[:i]:
            if k > v:
                inversions += 1
    return inversions
