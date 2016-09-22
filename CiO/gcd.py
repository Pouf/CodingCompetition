from fractions import gcd


def greatest_common_divisor(*args):
    result, *args = args
    for n in args:
        result = gcd(result, n)
    return result
