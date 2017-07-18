# Batman will look for the hostages on a given building by jumping from one
# window to another using his grapnel gun. Batman's goal is to jump to the
# window where the hostages are located in order to disarm the bombs.
# Unfortunately he has a limited number of jumps before the bombs go off...

# Before each jump, the heat-signature device will provide Batman with the
# direction of the bombs based on Batman current position:

#     U (Up)
#     UR (Up-Right)
#     R (Right)
#     DR (Down-Right)
#     D (Down)
#     DL (Down-Left)
#     L (Left)
#     UL (Up-Left)

# Your mission is to program the device so that it indicates the location of
# the next window Batman should jump to in order to reach the bombs' room as
# soon as possible.

# Buildings are represented as a rectangular array of windows, the window in
# the top left corner of the building is at index (0,0).

# For some tests, the bombs' location may change from one execution to the
# other: the goal is to help you find the best algorithm in all cases.


[W, H], _ = [int(i) for i in input().split()], input()
bx, by = [int(i) for i in input().split()]
bomb = {'R':0, 'L':W, 'D':0, 'U':H}

while 1:
    bomb_dir = input()
    for d in bomb_dir:
        bomb[d] = by if d in 'UD' else bx
    bx = (bomb['R'] + bomb['L']) // 2
    by = (bomb['U'] + bomb['D']) // 2

    print(bx, by)
