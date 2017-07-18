# You must create a program that echoes a Triforce of a given size N.

# - A triforce is made of 3 identical triangles
# - A triangle of size N should be made of N lines
# - A triangle's line starts from 1 star, and earns 2 stars each line
# - Take care, a . must be located at the top/left to avoid automatic trimming

# For example, a Triforce of size 3 will look like:

# .    *
#     ***
#    *****
#   *     *
#  ***   ***
# ***** *****

# Another example, a Triforce of size 5 will look like:

# .        *
#         ***
#        *****
#       *******
#      *********
#     *         *
#    ***       ***
#   *****     *****
#  *******   *******
# ********* *********



N = int(input())
width = 4 * N - 1

for div in [1, 2]:
    for line in range(N):
        qty = 2 * line + 1
        result = div * ('*' * qty).center(width // div + 1)
        if not line and div == 1:
            result = result.replace(' ', '.', 1)
        print(result.rstrip())