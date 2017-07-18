# The Oods want to offer a present to one of them. The thing is, they all have
# different budgets to invest in this present. Of course, their unique wish is
# to find the fairest method that will determine the maximum budget that each
# Ood can afford.

# The Doctor decides to give a helping hand by creating a program. His idea is
# to check if the Oods have enough money to buy the present, and if so, to
# calculate how much each Ood should pay, according to their respective budget
# limit.

# The Doctor has in hand the list of maximum budgets for each Ood. The Doctor's
# aim is to share the cost very precisely. To respect the Oods democratic
# values and to select the best solution, the Doctor decides that:

# - no Ood can pay more than his maximum budget
# - the optimal solution is the one for which the highest contribution is minimal
# - if there are several optimal solutions, then the best solution is the
#   one for which the highest second contribution is minimal, and so on and so forth...

# Moreover, to facilitate the calculations, the Doctor wants each financial
# participation to be an integer of the local currency (nobody should give any cents).

  

N = int(input()) # participants
C = int(input()) # price
B = sorted([int(input()) for i in range(N)]) # budget of each participant
if sum(B) < C:
    print('IMPOSSIBLE')
else:
    result = []
    while B:
        avg = C // len(B)
        b, *B = B
        result.append(min(b, avg))
        C -= min(b, avg)
    print('\n'.join(map(str, result)))