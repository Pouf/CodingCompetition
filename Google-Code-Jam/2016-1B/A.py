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

# https://code.google.com/codejam/contest/11254486/dashboard
# Problem A. Getting the Digits

for x in range(T):
    y = ''
    S = i.readline().rstrip()

    def gotcha(s, num):
        for l in num:
            s = s.replace(l, '', 1)
        return s, str(["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX",
                       "SEVEN", "EIGHT", "NINE"].index(num))
    while 'Z' in S:
        S, z = gotcha(S, 'ZERO')
        y += z
    while 'W' in S:
        S, z = gotcha(S, 'TWO')
        y += z
    while 'U' in S:
        S, z = gotcha(S, 'FOUR')
        y += z
    while 'X' in S:
        S, z = gotcha(S, 'SIX')
        y += z
    while 'G' in S:
        S, z = gotcha(S, 'EIGHT')
        y += z
    while 'F' in S:
        S, z = gotcha(S, 'FIVE')
        y += z
    while 'H' in S:
        S, z = gotcha(S, 'THREE')
        y += z
    while 'O' in S:
        S, z = gotcha(S, 'ONE')
        y += z
    while 'S' in S:
        S, z = gotcha(S, 'SEVEN')
        y += z
    while 'I' in S:
        S, z = gotcha(S, 'NINE')
        y += z
    y = ''.join(sorted(y))
    o.write('{}Case #{}: {}'.format(['', '\n'][x > 0], x + 1, y))

i.close()
o.close()
