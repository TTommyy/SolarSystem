import Planet
import PlanetData.Mass
import PlanetData.Distance
import PlanetData.Eccentricity
import PlanetData.Inclination
import PlanetData.Longitude
import PlanetData.MeanAnomaly
import PlanetData.Perihelion
import PlanetData.Radius
import datetime
import time
import Rotation

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

    def addPlanet(self, name, mass, radius, longitude, inclination, perihelion, distance, eccentricity, meanAnomaly, color):
        self.planets.append(Planet.Planet( name, mass, radius, longitude, inclination, perihelion, distance, eccentricity, meanAnomaly, color))

    def getPlanets(self):
        return self.planets

    def clearPlanets(self):
        self.planets = []

    def resetTime(self):
        self.currentTime = self.intialTime

    def addDay(self):
        self.currentTime += datetime.timedelta(days=1)

    def createSunSolarSystem(self):
        self.setStar(Planet.Planet("Sun", PlanetData.Mass.SUN, 0, 0, 0, 0, 0, 0, 0, "yellow"))

        self.clearPlanets()
        self.addPlanet("Mercury", PlanetData.Mass.MERCURY, PlanetData.Radius.MERCURY, PlanetData.Longitude.MERCURY, PlanetData.Inclination.MERCURY, \
            PlanetData.Perihelion.MERCURY, PlanetData.Distance.MERCURY, PlanetData.Eccentricity.MERCURY, PlanetData.MeanAnomaly.MERCURY, "gray")
        self.addPlanet("Venus", PlanetData.Mass.VENUS, PlanetData.Radius.VENUS, PlanetData.Longitude.VENUS, PlanetData.Inclination.VENUS, \
            PlanetData.Perihelion.VENUS, PlanetData.Distance.VENUS, PlanetData.Eccentricity.VENUS, PlanetData.MeanAnomaly.VENUS, "orange")
        # self.addPlanet("Earth", Mass.EARTH, Radius.EARTH, Eccentricity.EARTH, Distance.EARTH, "blue")
        self.addPlanet("Mars",PlanetData.Mass.MARS, PlanetData.Radius.MARS, PlanetData.Longitude.MARS, PlanetData.Inclination.MARS, \
            PlanetData.Perihelion.MARS, PlanetData.Distance.MARS, PlanetData.Eccentricity.MARS, PlanetData.MeanAnomaly.MARS, "red")
        # self.addPlanet("Jupiter", Mass.JUPITER, Radius.JUPITER, Eccentricity.JUPITER, Distance.JUPITER, "orange")
        # self.addPlanet("Saturn", Mass.SATURN , Radius.SATURN, Eccentricity.SATURN, Distance.SATURN, "tan")
        # self.addPlanet("Uranus", Mass.URANUS, Radius.URANUS, Eccentricity.URANUS, Distance.URANUS, "lightblue")
        # self.addPlanet("Neptune", Mass.NEPTUNE, Radius.NEPTUNE, Eccentricity.NEPTUNE,  Distance.NEPTUNE, "blue")
        self.updatePositon()

    def updatePositon(self):
         for planet in self.planets:
            planet.setPosition(Rotation.Rotation.calc_planet_position(planet, self.star.getMass(), self.currentTime))
            print(planet.name + " to pos: " , planet.getPosition())


