# Skynet's network is divided into several smaller networks, in each
# sub-network is a Skynet agent tasked with transferring information by moving
# from node to node along links and accessing gateways leading to other
# sub-networks.

# Your mission is to reprogram the virus so it will sever links in such a wa
# that the Skynet Agent is unable to access another sub-network thus preventing
# information concerning the presence of our virus to reach Skynet's central
# hub.

# For each test you are given:

# - A map of the network.
# - The position of the exit gateways.
# - The starting position of the Skynet agent.

# >>> Nodes can only be connected to up to a single gateway. <<<

# Each game turn:

# - First off, you sever one of the given links in the network.
# - Then the Skynet agent moves from one Node to another accessible Node.



nodes, l, e = [int(i) for i in input().split()]
links = {frozenset(input().split()) for i in range(l)}
exits = [input() for _ in range(e)]

while 1:
    skynet = input()
    danger = {frozenset([skynet, e]) for e in exits} & links
    print(*(danger or links).pop())
