# Your mission is to:
# - find the control room from which you will be able to deactivate the tracker beam
# - get back to your starting position once you've deactivated the tracker beam

# The structure is arranged as a rectangular maze composed of cells. Within the
# maze Kirk can go in any of the following directions: UP, DOWN, LEFT or RIGHT.

# Kirk is using his tricorder to scan the area around him but due to a disruptor
# field, he is only able to scan the cells located in a 5-cell wide square
# centered on him.

# Unfortunately, Spock was correct, there is a trap! Once you reach the control
# room an alarm countdown is triggered and you have only a limited number of
# rounds before the alarm goes off. Once the alarm goes off, Kirk is doomed...

# Kirk will die if any of the following happens:
# - Kirk's jetpack runs out of fuel. You have enough fuel for 1200 movements.
# - Kirk does not reach the starting position before the alarm goes off. The
# alarm countdown is triggered once the control room has been reached.
# - Kirk touches a wall or the ground: he is ripped apart by a mechanical trap.

# You will be successful if you reach the control room and get back to the
# starting position before the alarm goes off.

# A maze in ASCII format is provided as input. The character # represents a
# wall, the letter . represents a hollow space, the letter T represents your
# starting position, the letter C represents the control room and the character
# ? represents a cell that you have not scanned yet.


from itertools import product


# BFS search
def find_path(start, goal):
    valid = {(row, col) for row, col in it if maze[row][col] in '.T'+goal}
    stack = [[start]]
    visited = {start}
    while stack:
        path, *stack = stack
        py, px = path[-1]
        candidates = {(py+row, px+col) for row, col in neighbors} & valid - visited 
        for row, col in candidates:
            coords = row, col
            visited.add(coords)
            if maze[row][col] == goal:
                return [coords] + path[:0:-1]
            else:
                stack.append(path + [coords])


# absolute to relative coordinates
def move(path):
    row, col = path.pop()
    return neighbors[(row - y, col - x)]


# Rows, Columns, Alert countdown
R, C, A = map(int, input().split())
neighbors = {(-1,  0): 'UP',
             ( 1,  0): 'DOWN',
             ( 0, -1): 'LEFT',
             ( 0,  1): 'RIGHT'}

# create a tuple of coordinates for every point in the maze
it = list(product(range(R), range(C)))

while 1:
    y, x = map(int, input().split())
    try:
        T
    except:
        # start
        T = y, x
        command = ()
    maze = [input() for _ in range(R)]

    me_to_empty = find_path(start=(y, x), goal='?')
    if me_to_empty:
        print(move(me_to_empty))
    else:
        if not command:
            flat = ''.join(maze)
            if 'C' in flat:
                pos = flat.find('C')
                command = pos // C, pos % C
                C_to_T = []
                me_to_C = []
                alarm_triggered = 0

        if command and not C_to_T:
            C_to_T = find_path(start=command, goal='T')
    
        if C_to_T:
            if (y, x) == command:
                alarm_triggered = 1
            if alarm_triggered:
                print(move(C_to_T))
            else:
                if not me_to_C:
                    me_to_C = find_path(start=(y, x), goal='C')
                if me_to_C:
                    print(move(me_to_C))