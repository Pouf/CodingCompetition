# You are a duck sitting in the top left field of a W×H-sized lake.
# In every field of the lake is a different amount of food.
# Your duck is only allowed to move to the right or down.
# What is the maximum amount of food you can eat before reaching the bottom
# right field?

# This puzzle is a followup to The hungry duck - part 1
# This time you are swimming on bigger lakes. Performance is important.
# 0 < W,H <= 100
# 0 < Amount of food < 256
 

from itertools import product

W, H = map(int, input().split())
foods = [[int(j) for j in input().split()] for i in range(H)]

for i, j in product(reversed(range(H)), reversed(range(W))):
    down = foods[i+1][j] if i+1 < H else 0
    right = foods[i][j+1] if j+1 < W else 0
    foods[i][j] += max(down, right)

print(foods[0][0])