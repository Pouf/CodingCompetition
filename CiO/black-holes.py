from itertools import combinations
from math import pi, acos, hypot


def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])

def area(r):
    return pi*r**2

def checkio(data):
    blackHoles = [list(bh) for bh in data]
    while 1:
        for bh in sorted(combinations(blackHoles, 2), key=lambda c: dist(*c)):
            d = dist(*bh)
            skinny, fatty = sorted(bh, key=lambda B: B[2])
            r, R = skinny[2], fatty[2]
            s1, s2 = map(area, [r, R])
            if d+r < R:
                # skinny is inside fatty
                i = s1
            elif d < R+r < R+R:
                # the blackholes intersect
                i = r**2*acos((d**2+r**2-R**2)/2/d/r) + \
                    R**2*acos((d**2-r**2+R**2)/2/d/R) - \
                    ((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R))**.5/2
            else:
                # no intersection
                i = 0
            if i/s1 >= .55 and s2/s1 >= 1.2:
                fatty[2] = ((s2+s1)/pi)**.5
                blackHoles.remove(skinny)
                break
        else:
            return blackHoles
