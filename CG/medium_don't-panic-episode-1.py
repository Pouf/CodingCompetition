# You need to help Marvin and his clones (or is it the other way round?) reach
# the exit in order to help them escape the inside of the Infinite
# Improbability Drive.

# The drive has a rectangular shape of variable size. It is composed of several 
# floors (0 = lower floor) and each floor has several possible positions that
# the clones can occupy (0 = leftmost position, width - 1 = rightmost position)

# The goal is to save at least one clone in a limited amount of rounds.

# The details:

# - Clones appear from a unique generator at regular intervals, every three
#   game turns. The generator is located on floor 0. Clones exit the generator
#   heading towards the right.
# - Clones move one position per turn in a straight line, moving in their
#   current direction.
# - A clone is destroyed by a laser if it is goes below position 0 or beyond
#   position width - 1.
# - Elevators are scattered throughout the drive and can be used to move from
#   one floor to the one above. When a clone arrives on the location of an
#   elevator, it moves up one floor. Moving up one floor takes one game turn.
#   On the next turn, the clone continues to move in the direction it had
#   before moving upward.
# - On each game turn you can either block the leading clone - meaning the one
#   that got out the earliest - or do nothing.
# - Once a clone is blocked, you can no longer act on it. The next clone in
#   line takes the role of "leading clone" and can be blocked at a later time.
# - When a clone moves towards a blocked clone, it changes direction from left
#   to right or right to left. It also changes direction when getting out of
#   the generator directly on a blocked clone or when going up an elevator onto
#   a blocked clone.
# - If a clone is blocked in front of an elevator, the elevator can no longer
#   be used.
# - When a clone reaches the location of the exit, it is saved and disappears
#   from the area.

# Note: For this puzzle there is at most one elevator per floor.


*_, exit_y, exit_x, _, _, floors = input().split()
elevators = dict(input().split() for y in range(int(floors)))
elevators[exit_y] = exit_x

while 1:
    y, x, direction = input().split()
    if x != '-1':
        target = elevators.get(y, '')
        target_dir = 'RIGHT' if int(target) > int(x) else 'LEFT'
        if direction != target_dir and x != target:
            print('BLOCK')
            continue
    print("WAIT")