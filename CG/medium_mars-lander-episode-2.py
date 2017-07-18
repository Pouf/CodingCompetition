# The goal for your program is to safely land the "Mars Lander" shuttle.

# This puzzle is the second level of the "Mars Lander" trilogy. The controls
# are the same as the previous level but you must now control the angle in
# order to succeed.

# Built as a game, the simulator puts Mars Lander on a limited zone of Mars sky.
# The zone is 7000m wide and 3000m high.

# There is a unique area of flat ground on the surface of Mars, which is at
# least 1000 meters wide.
# Every second, depending on the current flight parameters (location, speed,
# fuel ...), the program must provide the new desired tilt angle and thrust
# power of Mars Lander:
# Angle goes from -90° to 90° . Thrust power goes from 0 to 4 .
 
# The game simulates a free fall without atmosphere. Gravity on Mars is
# 3.711 m/s² . For a thrust power of X, a push force equivalent to X m/s² is
# generated and X liters of fuel are consumed. As such, a thrust power of 4 in
# an almost vertical position is needed to compensate for the gravity on Mars.

# For a landing to be successful, the ship must:

# - land on flat ground
# - land in a vertical position (tilt angle = 0°)
# - vertical speed must be limited ( ≤ 40m/s in absolute value)
# - horizontal speed must be limited ( ≤ 20m/s in absolute value)


points = [input().split() for _ in range(int(input()))]
for i, (x, y) in enumerate(points):
    if y == points[i+1][1]:
        start, end, alt = int(x), int(points[i+1][0]), int(y)
        mid = (start + end) / 2
        break

while 1:
    x, y, h_speed, v_speed, *_ = [int(i) for i in input().split()]
    power = 4
    rotate = -20 if x < mid else 20
    if v_speed > 0:
        power = 0
    if abs(h_speed) > 80:
        rotate *= -1
    if abs(x - mid) < 1300:
        if abs(h_speed) > 10:
            rotate = 60 if h_speed > 0 else -60
        else:
            rotate = 0
            if v_speed >= -36:
                power = 0
        if y - alt < 90:
            rotate = 0

    print(rotate, power)
