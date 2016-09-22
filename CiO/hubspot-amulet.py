import itertools


def checkio(m):
    for a, b, c in itertools.product(range(-180,181), repeat=3):
        if not (a + b*m[1][0] + c*m[2][0])%360:
            if (a*m[0][1] + b + c*m[2][1])%360 == 225:
                if (a*m[0][2] + b*m[1][2] + c)%360 == 315:
                    return [a, b, c]
