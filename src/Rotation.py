import math

def calc_planet_position(planet, sun_mass, time):

    initial_position = planet.getX()

    # Calculate the gravitational constant
    G = 6.674 * 10**-11  # m^3 / (kg * s^2)

    # Calculate the semi-major axis of the planet's orbit
    a = initial_position / (1 - (planet.mass / sun_mass))

    # Calculate the planet's mean anomaly
    M = (math.sqrt(G * sun_mass) * time) / (a**1.5)

    # Calculate the planet's eccentric anomaly
    E = solve_kepler_equation(M, planet.eccentricity)

    # Calculate the planet's true anomaly
    v = 2 * math.atan2(math.sqrt(1 + planet.eccentricity) * math.sin(E/2), math.sqrt(1 - planet.eccentricity) * math.cos(E/2))

    # Calculate the planet's distance from the sun
    r = (a * (1 - (planet.eccentricity**2))) / (1 + (planet.eccentricity * math.cos(v)))

    # Calculate the planet's position in Cartesian coordinates
    x = r * math.cos(v)
    y = r * math.sin(v)

    return [x, y]

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