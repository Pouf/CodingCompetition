import os, sys

script = __file__
scriptPath = os.path.dirname(script)
scriptFile = os.path.basename(script)[0]
files = [f for f in os.listdir(scriptPath) if scriptFile in f and '.in' in f]
flat = str(files)
if scriptFile + '-large' in flat:
	size = 'large'
elif scriptFile + '-small' in flat:
	size = 'small'
elif scriptFile + '-test' in flat:
	size = 'test'
else:
	sys.exit(scriptFile + '-test not found')
latest = sorted(f for f in files if size in f)[-1][:-3]
f = '{}/{}'.format(scriptPath, latest)
print(f)
I = open(f + '.in', 'r')
O = open(f + '.out', 'w')
T = int(I.readline())


# def dfs(edges, kid, check):
# 	check += [kid]
# 	print(kid, check)
# 	for edge in edges:
# 		if kid == edge[0]:
# 			BFF = edge[1]
# 			if BFF == start:
# 				paths.add(len(check))
# 			if BFF not in check:
# 				dfs(edges, BFF, check)

for x in range(T):
	N = int(I.readline())
	F = list(map(int, I.readline().rstrip().split()))
	y = 0
	edges = [{kid+1, BFF} for kid, BFF in enumerate(F)]
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
	O.write('{}Case #{}: {}'.format(['', '\n'][x > 0], x+1, y))

I.close()
O.close()