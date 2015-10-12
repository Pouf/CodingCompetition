# Problem 05 - Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers # from
# 1 to 10 without any remainder. What is the smallest positive number that is 
# evenly divisible by all of the numbers from 1 to 20?

n = 2520
while True:
    n += 2520
    if not sum(n%x for x in range(2,21)):
        print(n)
        break
