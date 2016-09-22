def clock_angle(time):
    h, m = [int(i) for i in time.split(':')]
    h = (h%12)*30
    m = m*5.5
    return abs(h-m)//180 and 180-abs(h-m)%180 or abs(h-m)
