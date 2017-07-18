# There are 4 lanes on the bridge road and 1 to 4 bikes to control. There can
# only be one moto per lane and they are always vertically aligned.

# Each game turn, you can send a single instruction to every bike. Since  the
# bikes operate on the same frequency, they will all synchronize on the
# commands you send them.

# The possible commands are:
# - SPEED to speed up by 1.
# - SLOW to slow down by 1.
# - JUMP to jump.
# - WAIT to go straight on.
# - UP to send all motorbikes one lane up.
# - DOWN to send all motorbikes one lane down.

# The starting speeds of the bikes are synced, and can be 0. After every game
# turn, the bikes will move a number of squares equal to their current speed
# across the X axis.

# The UP and DOWN instructions will make the bikes move across the Y axis i
# addition to the movement across the X axis (Y = 0 corresponds to the highest
# lane). If a motorbike is prevented from moving up or down by the bridge's
# guard rails, none of the bikes will move on the Y axis that turn.

# When a motorbike goes in a straight line and does not jump, if there is a
# hole between the current position and the next position (after the move),
# then the motorbike is lost forever. For example, if X=2 and S=3, the next
# position of the bike will have X=5: if there is a hole in X=3, X=4 or X=5,
# the bike will be destroyed.

# Going up or down will put you at risk of falling in any hole situated in the
# black zone (consider the holes on the current and next lane):
# - The mission is a success if the minimum amount of required bikes gets to
# the far side of the bridge.
# - You fail if too many motorbikes fall into holes.
# - You fail if the motorbikes do not cross the entire bridge after 50 turns.


from itertools import product


M = int(input())
input()
road = [input() for _ in range(4)]
end = len(road[0])
ACTIONS = ['SPEED', 'UP', 'DOWN', 'JUMP', 'SLOW']

while 1:
    speed = int(input())
    bikes = [list(map(int, input().split())) for i in range(M)]
    heuristics = {k: 0 for k in product(ACTIONS, ACTIONS, ACTIONS, ACTIONS)}
    for k in heuristics:
        t_speed = speed
        t_alive = [b[:] for b in bikes if b[2]]
        x = t_alive[0][0]
        for action in k:
            if t_alive:
                if action == 'SPEED':
                    t_speed += 1
                    for _, y, a in t_alive:
                        if '0' in road[y][x+1:min(end, x+t_speed+1)]:
                            t_alive.remove([_, y, a])
                        else:
                            heuristics[k] += 1
                elif action == 'SLOW':
                    t_speed -= 1
                    if t_speed > 1:
                        for _, y, a in t_alive:
                            if '0' in road[y][x+1:min(end, x+t_speed+1)]:
                                t_alive.remove([_, y, a])
                            else:
                                heuristics[k] += 1
                    else:
                        heuristics[k] -= 10
                elif action == 'UP':
                    if t_alive[0][1]:
                        for i, (_, y, a) in enumerate(t_alive):
                            if '0' in road[y][x+1:min(end, x+t_speed)] + road[y-1][x+1:min(end, x+t_speed+1)]:
                                t_alive.remove([_, y, a])
                            else:
                                t_alive[i] = [x, y-1, 1]
                                heuristics[k] += 1
                    else:
                        action = 'JUMP'
                elif action == 'DOWN':
                    if t_alive[-1][1] < len(road)-1:
                        for i, (_, y, a) in enumerate(t_alive):
                            if '0' in road[y][x+1:min(end, x+t_speed)] + road[y+1][x+1:min(end, x+t_speed+1)]:
                                t_alive.remove([_, y, a])
                            else:
                                t_alive[i] = [x, y+1, 1]
                                heuristics[k] += 1
                    else:
                        action = 'JUMP'
                elif action == 'JUMP':
                    for _, y, a in t_alive:
                        if x + t_speed < end and road[y][x+t_speed] == '0':
                            t_alive.remove([_, y, a])
                        else:
                            heuristics[k] += 1
                x += t_speed
            
    best = max(heuristics, key=lambda k:(heuristics[k], -ACTIONS.index(k[0])))
    print(best[0])