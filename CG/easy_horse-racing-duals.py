# Casablanca’s hippodrome is organizing a new type of horse racing: duals.
# During a dual, only two horses will participate in the race. In order for
# the race to be interesting, it is necessary to try to select two horses with
# similar strength.

# Write a program which, using a given number of strengths, identifies the two
# closest strengths and shows their difference with an integer (≥ 0).

 
N = int(input())
P = sorted(int(input()) for i in range(N))
D = min(P[i+1] - P[i] for i in range(len(P) - 1))
print(D)