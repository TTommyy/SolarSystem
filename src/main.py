import turtle
import math
import time
import SolarSystem
import Rotation
import Mass
import sys

# Set the screen size and background color
turtle.screensize(1000, 1000)
turtle.bgcolor("black")

solarSystem = SolarSystem.SolarSystem(2000,1,1)
SolarSystem.createSunEarthSystem(solarSystem)

sun = turtle.Turtle()
earth = turtle.Turtle()

sun.shape("circle")
sun.color("yellow")
earth.shape("circle")
earth.color("blue")

sun.goto(0,0)
earth.goto(Rotation.calc_planet_position(solarSystem.planets[0], Mass.SUN, 0))

i = 3600
while True:
    time.sleep(0.1)
    earth.goto(Rotation.calc_planet_position(solarSystem.planets[0], Mass.SUN, i))
    i = i + 3600
