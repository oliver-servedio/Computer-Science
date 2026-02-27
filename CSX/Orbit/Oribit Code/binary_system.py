'''
Author: Oliver Servedio, Nick Triplett
Description: This program simulates the orbit of the two starts around their common center of mass using Newton's law of gravitation.
# Instructor: Mr. Campbell, Ms. Iversen, Mr. Carr
# Date: February 23, 2026
Bugs: Will drift over time due to a high value of delta t but remains stable for several orbits to the human eye
Log: 2.1 updated to include two stars orbiting each other, with the same mass and velocity but opposite directions
'''
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Planet_Class import planet

# Centrifugal constant
G = 6.67E-11    


# Star masses
# Initial separation
distance = 3e11

M1 = 1.5e30
M2 = 1.5e30
r = distance / 2

v = 12910

# 5.972e24, 6.371e6, 0, 29780, 1.496e11, 0
# Planet format = mass, radius, vx, vy, x, y
star1 = planet(M1, 7e8, 0, v, -distance/2, 0)
star2 = planet(M2, 7e8, 0, -v, distance/2, 0)
# A list of the positions of X and Y
X1, Y1 = [star1.x], [star1.y]
X2, Y2 = [star2.x], [star2.y]

dt = 50000  # fixed timestep

time = 0
# Trail 
trail = True
def step():
    # Equations for each place in time
    # distance = the distance from the center of the sun to the center of the earth

    # Distance between the two stars for each value
    dx = star2.x - star1.x
    dy = star2.y - star1.y
    # The distance between the two stars using pythagorean theorem
    r = (dx**2 + dy**2)**0.5
    
    # Newtons law of gravitation
    F = G * star1.mass * star2.mass / r**2
    # X direction and Y direction forces
    Fx = F * dx / r
    Fy = F * dy / r

    # Makes forces into acceleration: 
    star1.ax = Fx / star1.mass
    star1.ay = Fy / star1.mass
    # Negative bc equal and opposite reaction
    star2.ax = -Fx / star2.mass
    star2.ay = -Fy / star2.mass

    # finds the new velocity
    star1.vx += star1.ax * dt
    star1.vy += star1.ay * dt
    star2.vx += star2.ax * dt
    star2.vy += star2.ay * dt

    # new x and y positions
    star1.x += star1.vx * dt
    star1.y += star1.vy * dt
    star2.x += star2.vx * dt
    star2.y += star2.vy * dt

trail = True
def animate(placeholder):
    # Clears the last point
    plt.cla()

    global time

    step()
    # Adds the x and y positions to their respectful of star 1
    X1.append(star1.x)
    Y1.append(star1.y)
    # Adds the x and y positions to their respectful of star 2
    X2.append(star2.x)
    Y2.append(star2.y)

    plt.plot(X1, Y1)
    plt.plot(X2, Y2)

    # the interval of time the values of the planet will increase by
    time += 30

    # if trail is true draw the previous trail values
    # if trail:
    #     plt.plot(X, Y)

    # The marker for the earth
    plt.plot(star1.x, star1.y, marker="o", markersize=10)
    # The marker for the sun
    plt.plot(star2.x, star2.y, marker="o", markersize=10)

    plt.axis('equal')
    # The x dimensions of the chart
    plt.xlim(-3.6e11, 3.6e11)
    # The y dimensions of the chart
    plt.ylim(-3.6e11, 3.6e11)


fig, ax = plt.subplots()

# sets up the animation object
# animate is the function that updates the data and graph
# interval is the time in milliseconds between frames
ani = FuncAnimation(fig, animate, interval= .5)

# shows the graph
plt.show()