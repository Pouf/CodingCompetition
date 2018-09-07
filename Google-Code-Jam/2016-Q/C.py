import os
import sys


script = __file__
script_path = os.path.dirname(script)
script_file = os.path.basename(script)[0]
files = [f for f in os.listdir(script_path) if script_file in f and '.in' in f]
if '{}-large'.format(script_file) in str(files):
    size = 'large'
elif '{}-small'.format(script_file) in str(files):
    size = 'small'
elif '{}-test'.format(script_file) in str(files):
    size = 'test'
else:
    print('{}-test not found'.format(script_file))
    sys.exit()
latest = sorted(f for f in files if size in f)[-1][:-3]
f = '{}/{}'.format(script_path, latest)
i = open(f + '.in', 'r')
o = open(f + '.out', 'w')
print(f)
T = int(i.readline())

# https://code.google.com/codejam/contest/6254486/dashboard#s=p2
# Problem C. Coin Jam

from itertools import *
import numpy


def primesfrom2to(n):
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=numpy.bool)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[(k * k) // 3::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    return numpy.r_[2, 3, (3 * numpy.nonzero(sieve)[0] + 1) | 1]


primes = primesfrom2to(100)

for x in range(T):
    o.write('Case #{}:'.format(x + 1))
    N, J = map(int, i.readline().split())
    for j in product('01', repeat=int(N) - 2):
        y = '1{}1'.format(''.join(j))
        divs = []
        for base in range(2, 11):
            for d in primes:
                if not int(y, base) % d:
                    divs.append(str(d))
                    break
            else:
                break
        else:
            J -= 1
            o.write('\n{} {}'.format(y, ' '.join(divs)))
            if J == 0:
                break

i.close()
o.close()
