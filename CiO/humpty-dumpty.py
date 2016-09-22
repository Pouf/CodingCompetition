from math import pi, asin, atanh


def checkio(C, A):
    volume = pi*A**2*C/6
    if C == A:
        area = pi*C**2
    else:
        c, a = C/2, A/2
        if C > A:
            e = (1 - a**2/c**2)**.5
            area = 2*pi*a**2*(1+c*asin(e)/a/e)
        else:
            e = (1 - c**2/a**2)**.5
            area = 2*pi*a**2*(1+(1-e**2)*atanh(e)/e)
            
    return [volume, area]
