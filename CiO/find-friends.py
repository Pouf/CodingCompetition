def check_connection(network, first, second):
    friends = {first}
    network = list(network)
    while friends:
        ditch = friends.pop()
        for couple in list(network):
            if ditch in couple:
                if second in couple:
                    return True
                network.remove(couple)
                friends.add(couple.replace(ditch, '').replace('-', ''))
    return False
