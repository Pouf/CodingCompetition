# You are given data to calculate viral potential, represented by a network of
# people ready to relay a message to more people.
# We can assume this network contains no cyclic relation. 
# For example, if person #1 has a relation with person #2 and if person #2 has
# a relation with person #3, then it is impossible for #3 to have a direct
# relation with #1.
 
# When an individual broadcasts a message, it is counted as a single step,
# meaning that the time it takes to broadcast the message is independant from
# the amount of people in direct relation with the individual. We will consider
# that this event will always take 1 hour. 


from math import ceil


n = int(input())
graph = {frozenset(input().split()) for _ in range(n)} # links
people = set().union(*graph) # everyone
stack = {min(people)} # random dude
goal = len(people)

while len(stack) < goal:
    prev = stack.copy()
    stack = stack.union(*(g for g in graph if stack & g))
    leaf = stack - prev

leaf = {leaf.pop()} # one of the last to be reached
steps = 0
while len(leaf) < goal:
    steps += 1
    leaf = leaf.union(*(g for g in graph if leaf & g))

print(ceil(steps/2))
