import Mass

class Planet:
    def __init__(self, name, mass, eccentricity, x, y):
        self.name = name
        self.mass = mass
        self.eccentricity = eccentricity
        self.x = x
        self.y = y
    
    def setPositon(self, position):
        self.x = position[0]
        self.y = position[1]

    def getPosition(self):
        return [self.x, self.y]
    
    def getX(self):
        return self.x
