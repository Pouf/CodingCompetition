from functools import reduce


def checkio(i):
    digits = str(i).replace('0','')
    result = reduce(lambda x, y: int(x)*int(y), digits)
    return int(result)
