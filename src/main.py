import SolarSystem
import Engine
import sys
import time

print("Dziala")

# Init
solarSystem = SolarSystem.SolarSystem(2000,1,1)
solarSystem.createSunSolarSystem()
engine = Engine.Engine(solarSystem)
engine.show()

# Lets go
while True:
    solarSystem.addDay()
    solarSystem.updatePositon()
    engine.updatePositon()
    time.sleep(0.1)
