# Define the Sun and planets
sun = turtle.Turtle()
mercury = turtle.Turtle(mass=3.285 * 10**23, eccentricity=0.2056)
venus = turtle.Turtle(mass=4.867 * 10**24, eccentricity=0.0068)
earth = turtle.Turtle(mass=5.972 * 10**24, eccentricity=0.0167)
mars = turtle.Turtle(mass=6.39 * 10**23, eccentricity=0.0934)
jupiter = turtle.Turtle(mass=1.899 * 10**27, eccentricity=0.0484)
saturn = turtle.Turtle(mass=5.683 * 10**26, eccentricity=0.0542)
uranus = turtle.Turtle(mass=8.681 * 10**25, eccentricity=0.0472)
neptune = turtle.Turtle(mass=1.024 * 10**26, eccentricity=0.0086)



# Set the screen size and background color
turtle.screensize(1000, 1000)
turtle.bgcolor("black")

# Set the shapes and colors of the Sun and planets
sun.shape("circle")
sun.color("yellow")
mercury.shape("circle")
mercury.color("gray")
venus.shape("circle")
venus.color("orange")
earth.shape("circle")
earth.color("blue")
mars.shape("circle")
mars.color("red")
jupiter.shape("circle")
jupiter.color("orange")
saturn.shape("circle")
saturn.color("tan")
uranus.shape("circle")
uranus.color("lightblue")
neptune.shape("circle")
neptune.color("blue")

# Set the initial positions of the planets
sun.penup()
sun.goto(0, 0)

# Calculate the positions of the planets at time t = 0
time = 0
mercury_pos = calc_planet_position(mercury, sun.mass, mercury.initial_position, time)
venus_pos = calc_planet_position(venus, sun.mass, venus.initial_position, time)
earth_pos = calc_planet_position(earth, sun.mass, earth.initial_position, time)
mars_pos = calc_planet_position(mars, sun.mass, mars.initial_position, time)
jupiter_pos = calc_planet_position(jupiter, sun.mass, jupiter.initial_position, time)
saturn_pos = calc_planet_position(saturn, sun.mass, saturn.initial_position, time)
uranus_pos = calc_planet_position(uranus, sun.mass, uranus.initial_position, time)
neptune_pos = calc_planet_position(neptune, sun.mass, neptune.initial_position, time)

# Set the positions of the planets
mercury.penup()
mercury.goto(mercury_pos)

venus.penup()
venus.goto(venus_pos)