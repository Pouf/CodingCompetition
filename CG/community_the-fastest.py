# Your program must judge results of marathon runners and choose the best one.

# The result of each runner is represented as HH:MM:SS, where HH is hours, MM
# is minutes and SS is seconds.

# You are given N results and the smallest time is the best.
 

N = int(input())
print(min(input() for _ in range(N)))