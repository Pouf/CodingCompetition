from math import sin, cos, acos, hypot, degrees, pi
from operator import mul


def find_enemy(you, dir, enemy):
    x, y = zip(you, enemy)
    x = [ord(L)-65 for L in x]
    y = [int(n) + x[i] % 2 / 2 for i, n in enumerate(y)]
    u = [(x[1] - x[0]) * sin(pi/3), y[1] - y[0]]
    a = {'N': pi, 'NE': pi*2/3, 'SE': pi/3, 'S': 0, 'SW': pi*5/3,
         'NW': pi*4/3}.get(dir)
    v = [sin(a), cos(a)]
    angle = degrees(acos(sum(map(mul, u, v)) / hypot(*u)))
    if angle < 59.9:
        result = ['F']
    elif angle < 120.1:
        left = u[0] * v[1] - u[1] * v[0] > 0
        result = [['R', 'L'][left]]
    else:
        result = ['B']
    dist = abs(u[0] / sin(pi/3))
    dist += max(0, abs(u[1]) - dist * .5)
    result.append(round(dist))
    return result
