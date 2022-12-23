import Mass

class Planet:
    def __init__(self, name, mass, radius, eccentricity, x, y, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.eccentricity = eccentricity
        self.x = x
        self.y = y
        self.color = color

    def setPosition(self, position):
        self.x = position[0]
        self.y = position[1]

    def getPosition(self):
        return [self.x, self.y]

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getMass(self):
        return self.mass

    def getColor(self):
        return self.color
