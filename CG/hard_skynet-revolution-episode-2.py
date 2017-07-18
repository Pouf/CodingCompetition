# Skynet is responding to your intrusion and has activated additional defenses:
# - Most of the links have been reinforced: your virus no longer has the
#   possibility to destroy a link between two ordinary nodes, it can now only
#   sever links leading to gateways. If it attempts to cut a link between two
#   ordinary nodes it will be detected and deleted.
# - Nodes may now be connected to up to two gateways!


N, L, E = map(int, input().split())
links = [map(int, input().split()) for i in range(L)]
exits = {int(input()) for i in range(E)} # gateway nodes

nodes = {k:set() for k in range(N)}
for n1, n2 in links:
    nodes[n1].add(n2)
    nodes[n2].add(n1)

def risky_link(node):
    was_here = {node}
    bugs, new_bugs = {node:0}, {}
    while bugs:
        bug, step = bugs.popitem()
        nbugs = nodes[bug]-was_here
        gates = nbugs & exits
        if len(gates)>step:
            return gates.pop(), bug
        was_here |= nbugs-gates
        step += (len(gates)==0)
        for n in nbugs-gates: new_bugs[n] = step
        if not bugs: 
            bugs, new_bugs = new_bugs, {}
    for e in exits:
        if nodes[e]: return e, nodes[e].pop()


while 1:
    skynet = int(input())
    n1, n2 = risky_link(skynet)
    nodes[n1].discard(n2)
    nodes[n2].discard(n1)
    print(n1, n2)
