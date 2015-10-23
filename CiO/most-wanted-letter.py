def checkio(l):
    l = sorted(l.lower())
    return max(filter(str.isalpha, l), key=l.count)
