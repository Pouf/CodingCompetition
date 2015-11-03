from math import acos, degrees


def checkio(a, b, c):
    if b+c>a and a+c>b and a+b>c:
        A = (b**2+c**2-a**2)/2/b/c
        B = (a**2+c**2-b**2)/2/a/c
        C = (a**2+b**2-c**2)/2/a/b
        angles = [round(degrees(acos(i))) for i in [A, B, C]]
        return sorted(angles)
    return [0,0,0]
