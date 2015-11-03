def checkio(x):
    cd = ''
    # once x < 10, stop factorising as it would add digits to the final result
    # go backward, we need the least amount of digits
    # start again at 9 as soon as a divisor is found
    # if no divisor was found, it is either a prime number or the smallest divisor is > 10
    n = 9
    while x > 10 and n > 1:
        if x % n == 0:
            if x//n == 10:
                n -= 1
            else:
                cd += str(n)
                x = x//n
                n = 9
        else:
            n -= 1
    if x > 9:
        return 0
    else:
        cd += str(x)
    return int(''.join(sorted(cd)))
