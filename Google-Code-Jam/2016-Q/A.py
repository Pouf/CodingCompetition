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

# https://code.google.com/codejam/contest/6254486/dashboard#s=p0
# Problem A. Counting Sheep

import string


for t in range(T):
  left = set(string.digits)
  iN = N = int(i.readline().rstrip())
  left -= set(str(N))
  while left:
    iN += N
    left -= set(str(iN))
    if iN == N:
      result = 'INSOMNIA'
      break
  else:
    result = iN
  o.write('Case #{}: {}{}'.format(t + 1, result, ['\n', ''][t == T - 1]))

i.close()
o.close()
