import os


thisPath = os.path.dirname(__file__)
thisFile = os.path.basename(__file__)[0]
f = '{}/{}-large'.format(thisPath, thisFile)
if not os.path.isfile(f + '.in'):
  f = '{}/{}-small'.format(thisPath, thisFile)
  if not os.path.isfile(f + '.in'):
    f = '{}/{}-test'.format(thisPath, thisFile)
i = open(f + '.in', 'r')
o = open(f + '.out', 'w')
print(f)
T = int(i.readline())


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
