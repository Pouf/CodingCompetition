# Thor moves on a map which is 40 wide by 18 high. Note that the coordinates
# (X and Y) start at the top left! This means the most top left cell has the
# coordinates "X=0,Y=0" and the most bottom right one has the coordinates
# "X=39,Y=17".

# Once the program starts you are given:

# - lightX: the X position of the light of power that Thor must reach.
# - lightY: the Y position of the light of power that Thor must reach.
# - initialTX: the starting X position of Thor.
# - initialTY: the starting Y position of Thor.

 
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

up = light_y - initial_ty
right = light_x - initial_tx

v = 'NS'[up > 0]
h = 'WE'[right > 0]

up, right = abs(up), abs(right)

cut = min(up, right)
path = [v + h] * cut + [h] * (right - cut) + [v] * (up - cut)

while 1:
    print(path.pop())
