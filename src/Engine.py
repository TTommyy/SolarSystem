import SolarSystem
import turtle

SHAPE = "circle"
SCREEN_SIZE = 5000

class Engine:
    def __init__(self, solarSystem):
        self.solarSystem = solarSystem
        self.disConst = 40

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
            pl.goto(planet.getX() * self.disConst, planet.getY() * self.disConst)
            pl.s_planet = planet
            self.planets.append(pl)

    def updatePositon(self):
        for planet in self.planets:
            planet.goto(planet.s_planet.getX() * self.disConst, planet.s_planet.getY() * self.disConst)

    def draw(self):
        for planet in self.planets:
            planet.pendown()





