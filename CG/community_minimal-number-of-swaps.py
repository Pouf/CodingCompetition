# Given a list of 1 and 0, you must regroup all the 1 at the begin of the list
# in a minimum number of steps. A step is the interchange of two elements
# located at different positions.

# The expected result is the minimum number of steps required to obtain a
# sorted list.


input()
x = input().split()

steps = x[:x.count('1')].count('0')

print(steps)