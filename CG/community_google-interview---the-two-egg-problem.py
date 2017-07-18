# A building has N floors. One of the floors is the highest floor an egg can be
# dropped from without breaking. If an egg is dropped from above that floor, it
# will break. If it is dropped from that floor or below, it will be completely
# undamaged and you can drop the egg again.

# You are given two identical eggs, find the minimal number of drops it will
# take in the worst case to find out the highest floor from which an egg will
# not break.


floors, n = int(input()), 1

while (pow(n, 2) + n) / 2 < floors:
    n += 1

print(n)