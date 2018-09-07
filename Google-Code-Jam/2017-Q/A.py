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
F = '{}/{}'.format(script_path, latest)
I = open(F + '.in', 'r')
O = open(F + '.out', 'w')
print(F)
T = int(I.readline())  # nb of test cases

# https://code.google.com/codejam/contest/3264486/dashboard
# Problem A. Oversized Pancake Flipper


transtab = str.maketrans('+-', '-+')

for x in range(T):
    S, K = I.readline().rstrip().split()
    K = int(K)
    y = 0
    for i in range(len(S)):
        if '-' in S:
            if S[i] == '-' and i + K <= len(S):
                S = S[:i] + S[i:][:K].translate(transtab) + S[i+K:]
                y += 1
        else:
            break
    if '-' in S:
        y = 'IMPOSSIBLE'

    result = '{}Case #{}: {}'.format('\n' if x else '', x + 1, y)
    # print(result)
    O.write(result)

I.close()
O.close()
