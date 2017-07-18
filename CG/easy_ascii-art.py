# ASCII art allows you to represent forms by using characters. To be precise,
# in our case, these forms are words. For example, the word "MANHATTAN" could
# be displayed as follows in ASCII art:
 
# # #  #  ### # #  #  ### ###  #  ###
# ### # # # # # # # #  #   #  # # # #
# ### ### # # ### ###  #   #  ### # #
# # # # # # # # # # #  #   #  # # # #
# # # # # # # # # # #  #   #  # # # #
 
# ​Your mission is to write a program that can display a line of text in ASCII
# art in a style you are given as input.

 
L = int(input())
H = int(input())
T = input().upper()

for i in range(H):
    row = input()
    for letter in T:
        index = ord(letter) - ord('A') if letter.isalpha() else 26
        print(row[index*L:][:L], end='')
    print('')