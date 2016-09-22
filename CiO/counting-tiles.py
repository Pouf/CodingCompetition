from math import hypot


def checkio(radius):
    def inCircle(p, r):
        # a point is in a circle if distanceFromCenter < circleRadius
        n = sum(hypot(p[0]+x, p[1]+y) < r for x in [-.5, .5] for y in [-.5, .5])
        return n

    pos = [.5, 1.5]
    # starting point will be the diagonal squares: 
    # 4 partial and 4 * floor(radius / sqrt(2)) solid
    result = [radius//2**.5*4, 4]
    while 1:
        points = inCircle(pos, radius)
        if points == 0: return result
        result[points < 4] += 8
        up = points in [3, 4]
        pos = [pos[0]+[1, 0][up], pos[[0, 1][up]]+[2, 1][up]]
