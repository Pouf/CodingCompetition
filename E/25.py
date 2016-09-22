# Problem 25 - 1000-digit Fibonacci number
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000
# digits?
from math import log10, ceil
def fibDigits(n):
    sq = 5**.5
    result =  ceil((n-1+log10(sq))/log10((1+sq)/2))
    return result
print(fibDigits(1000))
