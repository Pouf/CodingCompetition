# A finance company is carrying out a study on the worst stock investments and
# would like to acquire a program to do so. The program must be able to analyze
# a chronological series of stock values in order to show the largest loss that
# it is possible to make by buying a share at a given time t0 and by selling it
# at a later date t1. The loss will be expressed as the difference in value
# between t0 and t1. If there is no loss, the loss will be worth 0.


n, p = int(input()), 0
stock = [int(i) for i in input().split()]

for i in range(n - 1):
    down = stock[i]
    while i < n-1 and stock[i+1] < down:
        i+= 1
        p = max(p, down - stock[i])

print(-p)