# At the start of each game turn, you are given the height of the 8 mountains
# from left to right.
# By the end of the game turn, you must fire on the highest mountain by
# outputting its index (from 0 to 7).

# Firing on a mountain will only destroy part of it, reducing its height. Your
# ship descends after each pass.  

 
while 1:
    h = {input(): i for i in range(8)}
    print(h[max(h)])
