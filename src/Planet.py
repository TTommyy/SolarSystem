import Mass

class Planet:
    def __init__(self, name, mass, radius, eccentricity, distance, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.eccentricity = eccentricity
        self.distance = distance
        self.color = color
        self.position = [0, 0]

    def getName(self):
        return self.name

    def getMass(self):
        return self.mass

    def getRadius(self):
        return self.radius

    def getDistance(self):
        return self.distance

    def getColor(self):
        return self.color

    def setPosition(self, positon):
        self.position = positon

    def getPosition(self):
        return self.position