def simple_areas(*args):
    if len(args) == 1:
        a = args[0]**2*.78539816
    elif len(args) == 2:
        a = args[0]*args[1]
    elif len(args) == 3:
        s = sum(args) / 2
        a = (s*(s-args[0])*(s-args[1])*(s-args[2]))**.5
    return int((a * 100) + .5) / 100
