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
        # Get the planet Mean Distance from it's star
        a = planet.getDistance()

        # Calculate the moment of intrest (in accuracy to one day here)
        time = Rotation.calc_delta_time(date)
        Rotation.log(planet, [" Time ", time])

        # Calculate the gravitational constant
        G = 6.674e-11  # m^3 / (kg * s^2)

        # Calculate the semi-major axis of the planet's orbit
        # a = initial_position  / (1 - (planet.mass / sun_mass)) # Deprecated due to complex number bug

        # Calculate the planet's mean anomaly
        M = (math.sqrt(G * sun_mass) * time) / (a**1.5)

        # Calculate the planet's eccentric anomaly
        #  E = Rotation.solve_kepler_equation(M, planet.eccentricity)
        try:
            E = newton(Rotation.kepler_equation, M, args=(M, planet.eccentricity))
            Rotation.log(planet, [" E ", E])
        except RuntimeError:
            Rotation.log(planet, " Exeption in newton biscecton metod occured")
            E = Rotation.solve_kepler_equation(M, planet.eccentricity)
            Rotation.log(planet, [" E ", E])


        # Calculate the planet's true anomaly
        v = 2 * math.atan2(math.sqrt(1 + planet.eccentricity) * math.sin(E/2), math.sqrt(1 - planet.eccentricity) * math.cos(E/2))

        # Calculate the planet's distance from the sun
        r = (a * (1 - (planet.eccentricity**2))) / (1 + (planet.eccentricity * math.cos(v)))

        # Calculate the planet's position in Cartesian coordinates
        x = r * math.cos(v)
        y = r * math.sin(v)

        return [x, y]

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
        # return 367*y - 7 * ( y + (m+9)//12 ) // 4 - 3 * \
        #     ( ( y + (m-9)//7 ) // 100 + 1 ) // 4 + 275*m//9 + d - 730515
        return 367*y - 7 * ( y + (m+9)//12 ) // 4 + 275*m//9 + d - 730530