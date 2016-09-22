import itertools

class Friends:
    def __init__(self, connections):
        self.connections = connections
        self.connections = list(self.connections)

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        return set(itertools.chain(*self.connections))

    def connected(self, name):
        return set(list(set(a)-{name})[0] for a in self.connections if {name}<=set(a))
