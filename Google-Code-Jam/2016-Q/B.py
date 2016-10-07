import os


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
  print('pas trouvé')
  exit
latest = sorted(f for f in files if size in f)[0][:-3]
f = '{}/{}'.format(scriptPath, latest)
i = open(f + '.in', 'r')
o = open(f + '.out', 'w')
print(f)
T = int(i.readline())

# https://code.google.com/codejam/contest/6254486/dashboard#s=p1
# Problem B. Revenge of the Pancakes

for x in range(T):
  S = list(i.readline().rstrip())
  y = 0
  while '-' in S:
    i = 1
    while i < len(S) and S[i] == S[0]:
      i += 1
    S = [['+', '-'][p == '+'] for p in reversed(S[:i])] + S[i:]
    y += 1

  o.write('Case #{}: {}{}'.format(x + 1, y, ['\n', ''][x == T - 1]))

i.close()
o.close()
