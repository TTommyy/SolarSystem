import Planet
import Mass
import Eccentricity
import datetime
import time

class SolarSystem:
    def __init__(self, startYear, startMonth, startDay):
        self.star = None
        self.planets = []
        self.intialTime = datetime.date(startYear, startMonth, startDay)
        self.currentTime = self.intialTime
    
    def setStar(self, star):
        self.star = star

    def addPlanet(self, planet):
        self.planets.append(planet)

def createSunEarthSystem(solarSystem):
    solarSystem.star = Planet.Planet("Sun", Mass.SUN, Eccentricity.SUN,0,0)
    solarSystem.planets = []
    solarSystem.addPlanet(Planet.Planet("Earth", Mass.EARTH, Eccentricity.EARTH,300,100))