# A sheet of paper is folded several times. The goal is to determine how many
# layers of paper are visible from one side of the obtained folding.

# Folding motions are:
# R for Right: take the right side and fold it on the left side.
# L for Left: take the left side and fold it on the right side.
# U for Up: take the high side and fold it on the low side.
# D for Down: take the low side and fold it on the high side.


order = list(input())
side = input()

opposite, result = 1, 1

while order:
    ply, *order = order
    if ply == side:
        opposite += result
        result = 1
    elif ply == 'RULD'['LDRU'.find(side)]:
        result += opposite
        opposite = 1
    else:
        result *= 2
        opposite *= 2

print(result)