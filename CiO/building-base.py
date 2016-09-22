class Building():
    def __init__(self, S, W, l, L, h=10):
        self.S = S
        self.W = W
        self.l = l
        self.L = L
        self.h = h
        
​
    def corners(self):
        W = self.W
        S = self.S
        E = W + self.l
        N = S + self.L
        coords = {"north-west": [N, W], 
                  "north-east": [N, E], 
                  "south-west": [S, W], 
                  "south-east": [S, E]}
        return coords
​
    def area(self):
        return self.l * self.L
​
    def volume(self):
        return self.l * self.L * self.h
​
    def __repr__(self):
        return 'Building({}, {}, {}, {}, {})'.format(self.S, self.W, self.l, self.L, self.h)
