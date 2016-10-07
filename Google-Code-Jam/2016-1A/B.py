import os
import sys


script = __file__
scriptPath = os.path.dirname(script)
scriptFile = os.path.basename(script)[0]
files = [f for f in os.listdir(scriptPath) if scriptFile in f and '.in' in f]
if '{}-large'.format(scriptFile) in str(files):
  size = 'large'
elif '{}-small'.format(scriptFile) in str(files):
  size = 'small'
elif '{}-test'.format(scriptFile) in str(files):
  size = 'test'
else:
  print('{}-test not found'.format(scriptFile))
  sys.exit()
latest = sorted(f for f in files if size in f)[-1][:-3]
f = '{}/{}'.format(scriptPath, latest)
i = open(f + '.in', 'r')
o = open(f + '.out', 'w')
print(f)
T = int(i.readline())

# https://code.google.com/codejam/contest/4304486/dashboard#s=p1
# Problem B. Rank and File

for x in range(T):
  N = int(i.readline())
  S = [int(s) for l in range(2 * N - 1) for s in i.readline().rstrip().split()]
  y = ' '.join(str(t) for t in sorted(set(s for s in S if S.count(s) % 2)))

  o.write('{}Case #{}: {}'.format(['', '\n'][x > 0], x + 1, y))

i.close()
o.close()
