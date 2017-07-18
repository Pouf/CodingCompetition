# You will be given a integer N, your goal is to draw the highest truncated
# pyramid that contains N “bricks”.
# Each floor of a pyramid contains one brick more than the previous one.
# Each brick is a * and each floor begins at the left of the line.
# Be careful not to add spaces at the end of a line.
 

N = int(input())
pyramid = [1]

while sum(pyramid) != N:
    if sum(pyramid) < N:
        pyramid.append(pyramid[-1] + 1)
    else:
        pyramid = pyramid[1:]

print('\n'.join(i * '*' for i in pyramid))