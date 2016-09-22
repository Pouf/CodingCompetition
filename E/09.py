# Problem 09 - Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, 
# for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
from itertools import combinations
def specialPythagoreanTriplet(n):
    for a, b, c in combinations(range(1000), 3):
        if a + b + c == 1000 and a*a + b*b == c*c:
            return a*b*c
    return 'no answer sry'
print(specialPythagoreanTriplet(1000))
a=lambda b:(1000**2-2000*b)/(2000-2*b)
for x in range(1000):
    if x+a(x)+(x**2+a(x)**2)**.5==1000 and a(x)>0:
        res = x*a(x)*(x**2+a(x)**2)**.5
        if res == int(res):
            print(res)
