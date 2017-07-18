# An internet operator plans to connect a business park to the optical fiber
# network. The area to be covered is large and the operator is asking you to
# write a program that will calculate the minimum length of optical fiber cable
# required to connect all buildings.

# For the implementation of the works, the operator has technical constraints
# whereby it is forced to proceed in the following manner:
# A main cable will cross through the park from the West to the East (from the
# position x of the most westerly building to the position x of the most
# easterly building).

# For each building, a dedicated cable will connect from the building to the
# main cable by a minimal path (North or South). The minimum length will
# therefore depend on the position of the main cable.
  

from statistics import median

N = int(input())
buildings = (map(int, input().split()) for _ in range(N))
x, y = zip(*buildings)
med = int(median(y))
cable = max(x) - min(x) + sum(abs(med - n) for n in y)

print(cable)