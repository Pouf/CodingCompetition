import os
import sys

script = __file__
script_path = os.path.dirname(script)
script_file = os.path.basename(script)[0]
files = [f for f in os.listdir(script_path) if script_file in f and '.in' in f]
flat = str(files)
if script_file + '-large' in flat:
  size = 'large'
elif script_file + '-small' in flat:
  size = 'small'
elif script_file + '-test' in flat:
  size = 'test'
else:
  sys.exit(script_file + '-test not found')
latest = sorted(f for f in files if size in f)[-1][:-3]
f = '{}/{}'.format(script_path, latest)
print(f)
i = open(f + '.in', 'r')
o = open(f + '.out', 'w')
T = int(i.readline())

# https://code.google.com/codejam/contest/4304486/dashboard#s=p2
# Problem C. BFFs

for x in range(T):
    N = int(i.readline())
    F = list(map(int, i.readline().rstrip().split()))
    y = 0
    edges = [{kid + 1, BFF} for kid, BFF in enumerate(F)]
    print('\n', edges, '\n')
    paths = set()
    for start in range(N):
        start += 1
        check = []
        S = [start]
        while S:
            kid = S.pop()
            print(kid)
            if kid not in check:
                check.append(kid)
                for edge in edges:
                    if kid in edge:
                        BFF = (edge - {kid}).pop()
                        if BFF == start:
                            paths.add(len(S))
                        S.append(BFF)
    y = max(paths)
    o.write('{}Case #{}: {}'.format(['', '\n'][x > 0], x + 1, y))

i.close()
o.close()
