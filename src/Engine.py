import SolarSystem
import turtle

SHAPE = "circle"
SCREEN_SIZE = 5000

class Engine:
    def __init__(self, solarSystem):
        self.solarSystem = solarSystem
        self.disConst = 80

    def show(self):
        turtle.screensize(SCREEN_SIZE, SCREEN_SIZE)
        turtle.bgcolor("black")
        s_star = self.solarSystem.getStar()
        # Handle star
        self.star = turtle.Turtle()
        self.star.shape(SHAPE)
        self.star.color(s_star.getColor())
        self.star.penup()
        self.star.goto(s_star.getPosition())
        # Handle planets
        self.planets = []
        for planet in self.solarSystem.getPlanets():
            pl = turtle.Turtle()
            pl.shape(SHAPE)
            pl.color(planet.getColor())
            pl.penup()
            pl.s_planet = planet
            self.planets.append(pl)
        self.updatePositon()

    def updatePositon(self):
        for planet in self.planets:
            planet.goto( planet.s_planet.getPosition()[0] * self.disConst, planet.s_planet.getPosition()[1] * self.disConst)

    def draw(self):
        for planet in self.planets:
            planet.pendown()





