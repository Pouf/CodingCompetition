# write a program that will make it possible to foresee the path that Bender
# follows. To do so, you are given the logic for the new intelligence with
# which Bender has been programmed as well as a map of the city.

# The 9 rules of the new Bender system:

# - Bender starts from the place indicated by the @ symbol on the map and headsSOUTH.
# - Bender finishes his journey and dies when he reaches the suicide booth marked $.
# - Obstacles that Bender may encounter are represented by # or X.
# - When Bender encounters an obstacle, he changes direction using the following
#   priorities: SOUTH, EAST, NORTH and WEST. So he first tries to go SOUTH, if
#   he cannot, then he will go EAST, if he still cannot, then he will go NORTH,
#   and finally if he still cannot, then he will go WEST.
# - Along the way, Bender may come across path modifiers that will instantaneously
#   make him change direction. The S modifier will make him turn SOUTH from then
#   on, E, to the EAST, N to the NORTH and W to the WEST.
# - The circuit inverters (I on map) produce a magnetic field which will reverse
#   the direction priorities that Bender should choose when encountering an obstacle.
#   Priorities will become WEST, NORTH, EAST, SOUTH. If Bender returns to an inverter
#   I, then priorities are reset to their original state (SOUTH, EAST, NORTH, WEST).
# - Bender can also find a few beers along his path (B on the map) that will give
#   him strength and put him in “Breaker” mode. Breaker mode allows Bender to destroy
#   and automatically pass through the obstacles represented by the character X (only
#   the obstacles X). When an obstacle is destroyed, it remains so permanently and
#   Bender maintains his course of direction. If Bender is in Breaker mode and passes
#   over a beer again, then he immediately goes out of Breaker mode. The beers remain
#   in place after Bender has passed.
# - 2 teleporters T may be present in the city. If Bender passes over a teleporter,
#   then he is automatically teleported to the position of the other teleporter and
#   he retains his direction and Breaker mode properties.
# - Finally, the space characters are blank areas on the map (no special behavior
#   other than those specified above).

# Your program must display the sequence of moves taken by Bender according to
# the map provided as input.

# The map is divided into lines (L) and columns (C). The contours of the map
# are always unbreakable # obstacles. The map always has a starting point @ and
# a suicide booth $.

# If Bender cannot reach the suicide booth because he is indefinitely looping,
# then your program must only display LOOP.
  

import sys
            

L = int(input().split()[0])
graph = {i + j*1j: c for i in range(L) for j, c in enumerate(input())}
z = [c for c in graph if graph[c] == '@'][0]
T = {c for c in graph if graph[c] == 'T'}
beered = inverted = k = 0
visited, instructions = [], []
i = 1

while i:
    val = graph[z]
    if val in 'SENW':
        k = 'SENW'.index(val)
    else:
        walls = '#X'[:2-beered]
        if graph[z + 1j**k] in walls:
            k = inverted * 3
        while graph[z + 1j**k] in walls:
            k += inverted * -2 + 1
    z += 1j**k
    visited.append(z)
    if visited.count(z) > 6:
        print('LOOP')
        sys.exit()
    instructions.append(['SOUTH', 'EAST', 'NORTH', 'WEST'][k])

    action = {'I': "inverted = not inverted",
              'B': "beered = not beered",
              'T': "z = (T - set([z])).pop()",
              'X': "graph[z] = ' '",
              '$': "i = 0"}.get(graph[z], '')
    exec(action)

print('\n'.join(instructions))
