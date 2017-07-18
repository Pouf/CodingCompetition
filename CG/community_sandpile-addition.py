# A sandpile is a square matrix of natural numbers between 0 and 3,
# representing how many grains of sand there is on each square. To add two 
# sandpiles, just start by adding the two matrices element by element. Except
# the matrix you generate might not be a sandpile, if one of its element is
# higher than 3 you must transform this matrix into a sandpile, and this is how
# it is done :
# - If a square has 4 grains of sand or more, it "loses" four and distributes
#   it to its four neighbors (if the square touches an edge, the grain of sand
#   is lost)
# - Keep doing that to all the squares with 4 grains or more until all the
#   squares have 3 grains or less

# Example :

# 000   000   000    010
# 020 + 020 = 040 -> 101
# 000   000   000    010
 

N = range(int(input()))
A = {i + j*1j:int(z) for i in N for j, z in enumerate(input())}
B = {i + j*1j:int(z) for i in N for j, z in enumerate(input())}
cpile = {z: A[z] + B[z] for z in set(A)}

while any(i > 3 for i in cpile.values()):
    for z, val in cpile.items():
        if val > 3:
            cpile[z] -= 4
            for k in range(4):
                try:
                    cpile[z + 1j**k] += 1
                except KeyError:
                    pass

for i in N:
    line = ''.join(str(cpile[i + j*1j]) for j in N)
    print(line)