# you're asked to develop a program capable of performing basic arithmetical
# operations between two mayan numbers.

# The mayan numerical system contains 20 numerals going from 0 to 19. Here's an
# ASCII example of their representation:
# 0    1    2    3    4    5    6    7    8    9   
# .oo. o... oo.. ooo. oooo .... o... oo.. ooo. oooo
# o..o .... .... .... .... ---- ---- ---- ---- ----
# .oo. .... .... .... .... .... .... .... .... ....
# .... .... .... .... .... .... .... .... .... ....

# 10   11   12   13   14   15   16   17   18   19
# .... o... oo.. ooo. oooo .... o... oo.. ooo. oooo
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
# .... .... .... .... .... ---- ---- ---- ---- ----

# A mayan number is divided into vertical sections. Each section contains a
# numeral (from 0 to 19) representing a power of 20. The lowest section
# corresponds to 200, the one above to 201 and so on.

# Thereby, the example below is : (12 x 20 x 20) + (0 x 20) + 5 = 4805
# oo..
# ----
# ----  12
# ....
# 
# .oo.
# o..o
# .oo.  0
# ....
# 
# ....
# ----
# ....  5
# ....

# To spice the problem up, the mayans used several dialects, and the graphical
# representation of the numerals could vary from one dialect to another.
 
# The representation of the mayan numerals will be given as the input of your
# program in the form of ASCII characters. You will have to display the result
# of the operation between the two given mayan numbers. The possible operations
# are *, /, +, -


def chunk(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def maya_to_int():
    r = [input() for i in [0] * int(input())]
    r = reversed(chunk(r, H))
    r = [num.index(n)*B**i for i, n in enumerate(r)]
    return sum(r)

L, H, B = *[int(i) for i in input().split()], 20
num = [input() for i in range(H)]
num = [[num[i][j*L:][:L] for i in range(H)] for j in range(B)]

r = int(eval('{0}{2}{1}'.format(maya_to_int(), maya_to_int(), input())))
out = []
while r:
    out = num[r % B] + out
    r //= B
print(*out or num[0], sep='\n')