# The game is played on a rectangular grid with a given size. Some cells
# contain power nodes. The rest of the cells are empty.

# The goal is to find, when they exist, the horizontal and vertical neighbors
# of each node.

# To do this, you must find each (x1,y1) coordinates containing a node, and
# display the (x2,y2) coordinates of the next node to the right, and the
# (x3,y3) coordinates of the next node to the bottom within the grid.

# If a neighbor does not exist, you must output the coordinates -1 -1 instead
# of (x2,y2) and/or (x3,y3).


from itertools import product


W = int(input())
H = int(input())
grid = [input() for row in range(H)]
for j, i in product(range(W), range(H)):
    if grid[i][j] == '0':
        nodes = [j, i]
        right = [[j+k+1, i] for k in range(W-j-1) if grid[i][j+k+1] == '0']
        botto = [[j, i+k+1] for k in range(H-i-1) if grid[i+k+1][j] == '0']
        nodes.extend(right and right[0] or [-1, -1])
        nodes.extend(botto and botto[0] or [-1, -1])
        print(*nodes)
