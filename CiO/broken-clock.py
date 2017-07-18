from datetime import datetime


def broken_clock(starting_time, wrong_time, error_description):
    t1, t2 = [datetime.strptime(t, '%H:%M:%S') for t in [starting_time, wrong_time]]

    x, unit1, _, y, unit2 = error_description.split()
    x, y = [int(n) for n in [x, y]]
    conv = {'s': 1, 'm': 60, 'h': 3600}
    x *= conv.get(unit1[0])
    y *= conv.get(unit2[0])
    return (t1 + (t2 - t1) * y / (x + y)).strftime('%X')
