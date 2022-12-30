class Planet:
    def __init__(self, name, mass, radius, longitude, inclination, perihelion, distance, eccentricity, meanAnomaly, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.longitude = longitude
        self.inclination = inclination
        self.perihelion = perihelion
        self.distance = distance
        self.eccentricity = eccentricity
        self.meanAnomaly = meanAnomaly
        self.color = color
        self.position = [0, 0, 0]

    def getName(self):
        return self.name

    def getMass(self):
        return self.mass

    def getRadius(self):
        return self.radius

    def getLongitude(self, time):
        return self.longitude[0] + time *self.longitude[1]

    def getInclination(self, time):
        return self.inclination[0] + time * self.inclination[1]

    def getPerihelion(self, time):
        return self.perihelion[0] + time * self.perihelion[1]

    def getEntricity(self, time):
        return self.eccentricity[0] + time * self.perihelion[1]

    def getMeanAnomaly(self, time):
        return self.meanAnomaly[0] + time * self.meanAnomaly[1]

    def getDistance(self):
        return self.distance

    def getColor(self):
        return self.color

    def setPosition(self, positon):
        self.position = positon

    def getPosition(self):
        return self.position