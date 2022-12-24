import Planet
import Mass
import Eccentricity
import datetime
import time
import Rotation
import Distance
import Radius

class SolarSystem:
    def __init__(self, startYear = 2000, startMonth = 1, startDay = 1):
        self.star = None
        self.planets = []
        self.intialTime = datetime.date(startYear, startMonth, startDay)
        self.currentTime = self.intialTime

    def setStar(self, star):
        self.star = star
        self.star.setPosition([0, 0])

    def getStar(self):
        return self.star

    def addPlanet(self, name, mass, radius, eccentricity, distance, color):
        self.planets.append(Planet.Planet(name, mass, radius, eccentricity, distance, color))

    def getPlanets(self):
        return self.planets

    def clearPlanets(self):
        self.planets = []

    def resetTime(self):
        self.currentTime = self.intialTime

    def addDay(self):
        self.currentTime += datetime.timedelta(days=1)

    def createSunSolarSystem(self):
        self.setStar(Planet.Planet("Sun", Mass.SUN, Radius.SUN, Eccentricity.SUN, 0, "yellow"))

        self.clearPlanets()
        self.addPlanet("Mercury", Mass.MERCURY, Radius.MERCURY, Eccentricity.MERCURY, Distance.MERCURY, "gray")
        self.addPlanet("Venus", Mass.VENUS, Radius.VENUS, Eccentricity.VENUS, Distance.VENUS, "orange")
        self.addPlanet("Earth", Mass.EARTH, Radius.EARTH, Eccentricity.EARTH, Distance.EARTH, "blue")
        self.addPlanet("Mars", Mass.MARS, Radius.MARS, Eccentricity.MARS, Distance.MARS, "red")
        # self.addPlanet("Jupiter", Mass.JUPITER, Radius.JUPITER, Eccentricity.JUPITER, Distance.JUPITER, "orange")
        # self.addPlanet("Saturn", Mass.SATURN , Radius.SATURN, Eccentricity.SATURN, Distance.SATURN, "tan")
        # self.addPlanet("Uranus", Mass.URANUS, Radius.URANUS, Eccentricity.URANUS, Distance.URANUS, "lightblue")
        # self.addPlanet("Neptune", Mass.NEPTUNE, Radius.NEPTUNE, Eccentricity.NEPTUNE,  Distance.NEPTUNE, "blue")
        self.updatePositon()

    def updatePositon(self):
         for planet in self.planets:
            planet.setPosition(Rotation.Rotation.calc_planet_position(planet, self.star.getMass(), self.currentTime))
            print(planet.name + " to pos: " , planet.getPosition())


