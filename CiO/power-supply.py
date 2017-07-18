def power_supply(network, power_plants):
    network = [set(n) for n in network]
    nodes = set.union(*network)
    while power_plants:
        nodes -= set(power_plants.keys())
        power_plants = {list(n-{i})[0]: power_plants[i]-1 for n in network 
                        for i in power_plants if i in n and power_plants[i]}
    return nodes
