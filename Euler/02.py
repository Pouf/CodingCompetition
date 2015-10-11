# V1

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b
def euler02():
    result, n = 0, 0
    while True:
        f = fib(n)
        if f > 4000000:
            print(result)
            break
        elif not f % 2:
            result += fib(n)
        n += 1
euler02()


# better fib function

def fibonacci(n):
    return fib(n)[0]
def fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
           return (d, c + d)
print(fibonacci(1000000))
