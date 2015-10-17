from functools import reduce


def checkio(i):
    digits = str(i).replace('0','')
    result = reduce(lambda x, y: int(x)*int(y), digits)
    return int(result)



golf=lambda n:(n%10or 1)*golf(n//10)if n else 1
