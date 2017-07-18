# The program must output the given map, making the # fall to the bottom of the
# grid.

# The map is composed of '.' and '#'.

# INPUT:
# Line 1 : Two integers: The map width width and height height.
# height next lines : width characters: (. or #).

# OUTPUT:
# height lines : width characters where the # are at the bottom of the grid.

# CONSTRAINTS:
# 0 < width < 100
# 0 < height < 10

# EXAMPLE:
# Input
# 17 5
# ...#...#.#.#...#.
# .#..#...#....#...
# ..........#......
# ..###...###..##..
# #################
# Output
# .................
# .................
# ...##...###..#...
# .####..#####.###.
# #################
 

w, h = [int(i) for i in input().split()]
grid = [input() for _ in range(h)]
grid_CCW = zip(*reversed(grid))
grid_CCW = (sorted(line) for line in grid_CCW)
grid = reversed(list(zip(*grid_CCW)))
for line in grid:
    print(''.join(line))