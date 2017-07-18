def super_root(number):
    acc = 1
    a, b = 0, 0
    while abs(b - number) > 0.001:
        if b < number:
            a += acc
        else:
            a -= acc
            acc /= 2
        b = a**a
    return a
