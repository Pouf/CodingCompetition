# You have been given the responsibility of developing the contact manager. In
# the specifications, there are two points in particular that catch your
# attention:

# 1. Intelligent Assistance for entering numbers
# The numbers corresponding to the first digits entered will be displayed to
# the user almost instantly.

# 2. Number storage optimization
# First digits which are common to the numbers should not be duplicated in the
# memory.

# Your task is to write a program that displays the number of items (which are
# numbers) required to store a list of telephone numbers with the structure
# presented above.
  

n = int(input())
numbers = [input() for _ in range(n)]
stack = set(numbers)

for n in numbers:
    for i in range(1, len(n)):
        stack.add(n[:i])

print(len(stack))