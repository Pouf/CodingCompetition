# You are a duck sitting in the top left field of a W×H-sized lake. In every
# field of the lake is a different amount of food. Your duck is only allowed to
# move to the right or down. What is the maximum amount of food you can eat
# before reaching the bottom right field?

# In part 1 you only swim in small lakes where you don't have to care about
# timeouts.


from itertools import product

w, h = map(int, input().split())
foods = [[int(j) for j in input().split()] for i in range(h)]

for i, j in product(reversed(range(h)), reversed(range(w))):
    down = foods[i+1][j] if i+1 < h else 0
    right = foods[i][j+1] if j+1 < w else 0
    foods[i][j] += max(down, right)

print(foods[0][0])