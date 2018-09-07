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
I = open(F + '.in', 'r')
O = open(F + '.out', 'w')
print(F)
T = int(I.readline())  # nb of test cases

# https://code.google.com/codejam/contest/8294486/dashboard
# Problem A. 


for x in range(T):
    D, N = map(int, I.readline().rstrip().split())
    horses = [tuple(map(int, I.readline().split())) for _ in range(N)]
    slowpoke = max((D-K)/S for K, S in horses)
    y = D/slowpoke

    result = '{}Case #{}: {}'.format('\n' if x else '', x + 1, y)
    print(result)
    O.write(result)

I.close()
O.close()
