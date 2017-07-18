# Write a program that prints the temperature closest to 0 among input data.
# If two numbers are equally close to zero, positive integer has to be
# considered closest to zero (for instance, if the temperatures are -5 and 5,
# then display 5).


N = input()
T = [int(t) for t in input().split()]
T.sort(key=lambda t: (abs(t), t < 0))
print(T and T[0] or 0)