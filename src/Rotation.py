# Class responsible for phisycal rotation simulation.

import math
from scipy.optimize import newton
import numpy as np

class Rotation:
    @staticmethod
    def kepler_equation(E, M, e):
        return E - e * np.sin(E) - M

    @staticmethod
    def log(planet, msg):
        print("Planet: " + planet.getName(), msg)

    @staticmethod
    def calc_planet_position(planet, sun_mass, date):

        # Calculate the moment of intrest (in accuracy to one day here)
        time = Rotation.calc_delta_time(date)
        Rotation.log(planet, [" Time ", time])

        # Get longtitude
        longitude = math.radians(planet.getLongitude(time))

        # Get inclination
        inclination = math.radians(planet.getInclination(time))

        # Get argument of perihelion
        perihelion = math.radians(planet.getPerihelion(time))

        # Get the planet Mean Distance from it's star
        a = planet.getDistance()

        # Get planet eccentricity
        eccentricity = planet.getEntricity(time)

        # Get planet mean anomaly
        M = math.radians(planet.getMeanAnomaly(time))

        # Calculate the gravitational constant
        # G = 6.674e-11  # m^3 / (kg * s^2)

        # Calculate the planet's mean anomaly
        # M = (math.sqrt(G * sun_mass) * time) / (a**1.5)

        # Calculate the planet's eccentric anomaly
        try:
            E = newton(Rotation.kepler_equation, M, args=(M, eccentricity))
            Rotation.log(planet, [" E ", E])
        except RuntimeError:
            Rotation.log(planet, " Exeption in newton metod occured")
            E = Rotation.solve_kepler_equation(M, eccentricity)
            Rotation.log(planet, [" E ", E])

        xv = a * (math.cos(E) - eccentricity)
        yv = a * (math.sqrt(1.0 - eccentricity ** 2) * math.sin(E))

        # Calculate the planet's true anomaly
        v = 2 * math.atan2(yv, xv)

        # Calculate the planet's distance from the sun
        r = math.sqrt(xv ** 2 + yv ** 2)

        # Rotate the planet's position in the x-y plane by the angle of the planet's longitude of the ascending node (N) and the angle of the planet's argument of perihelion (w)
        x = r * (math.cos(longitude) * math.cos(v + perihelion) - math.sin(longitude) * math.sin(v + perihelion) * math.cos(inclination))
        y = r * (math.sin(longitude) * math.cos(v + perihelion) + math.cos(longitude) * math.sin(v + perihelion) * math.cos(inclination))
        z = r * (math.sin(v + perihelion) * math.sin(inclination))

        return [x, y, z]

    @staticmethod
    def solve_kepler_equation(M, e):
        # Initialize the eccentric anomaly to the mean anomaly
        E = M
        # Iterate until the eccentric anomaly converges
        while True:
            # Calculate the difference between the current estimate of the eccentric anomaly and the mean anomaly
            diff = E - e * math.sin(E) - M

            # If the difference is small enough, return the eccentric anomaly
            if abs(diff) < 1e-6:
                return E

            # Update the eccentric anomaly using the difference
            E = E - diff / (1 - e * math.cos(E))





    @staticmethod
    def calc_delta_time(date):
        y = date.year
        m = date.month
        d = date.day
        return 367*y - 7 * ( y + (m+9)//12 ) // 4 - 3 * \
            ( ( y + (m-9)//7 ) // 100 + 1 ) // 4 + 275*m//9 + d - 730515
        # return 367*y - 7 * ( y + (m+9)//12 ) // 4 + 275*m//9 + d - 730530