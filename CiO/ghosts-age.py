def checkio(B00):
    BO0, B0O, BOO = 1, 1, 0
    while B00 != 10000:
        BOO += 1
        if BOO == B0O:
            B00 += B0O
            BO0, B0O = B0O, BO0+B0O
        else:
            B00 -= 1
    return BOO
