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
latest = sorted(f for f in files if size in f)[0][:-3]
f = '{}/{}'.format(scriptPath, latest)
i = open(f + '.in', 'r')
o = open(f + '.out', 'w')
print(f)
T = int(i.readline())

# https://code.google.com/codejam/contest/6254486/dashboard#s=p3
# Problem D. Fractiles

for x in range(T):
  K, C, S = map(int, i.readline().split())
  y = ' '.join(str(i + 1) for i in range(S))
  o.write('{}Case #{}: {}'.format(['', '\n'][x > 0], x + 1, y))

i.close()
o.close()
