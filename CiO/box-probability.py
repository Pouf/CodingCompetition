def checkio(marbles, step):
    w, T = marbles.count('w'), len(marbles)
    for turn in range(1, step):
        w = T*w + T**turn - 2*w
    return w/T**step  
