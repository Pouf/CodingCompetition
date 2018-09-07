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

# https://code.google.com/codejam/contest/4304486/dashboard#s=p0
# Problem A. The Last Word

for x in range(T):
    S = list(i.readline().rstrip())
    y = S[0]
    for s in S[1:]:
        y = max(y + s, s + y)

    o.write('{}Case #{}: {}'.format(['', '\n'][x > 0], x + 1, y))

i.close()
o.close()
