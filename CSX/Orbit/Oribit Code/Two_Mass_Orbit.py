'''
Author: Oliver Servedio, Nick Triplett
Description: This program simulates the orbit of the earth around the sun and the suns movement using Newton's law of gravitation.
and their positions are updated using Newton's law of gravitation.
Instructor: Mr. Campbell, Ms. Iversen, Mr. Carr
Date: February 23, 2026
Bugs: Will drift over time due to a high value of delta t but remains stable for several orbits to the human eye
Log: 2.0 updated to include the sun's movement 
'''

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Planet_Class import planet

# Centrifugal constant
G = 6.67E-11    

# Initial separation
distance = 3e11

# Mass of planet
M1 = 5.972e24
# Mass of sun
M2 = 1.989e30

r = distance / 2
v = 12910

# 5.972e24, 6.371e6, 0, 29780, 1.496e11, 0
# Planet format = mass, radius, vx, vy, x, y
earth = planet(5.972e24, 6.371e6, 0, 35000, 1.496e11, 0)
sun = planet(1.989e30, 6.96e8, 0, 0, 0, 0)

# A list of the positions of X and Y
X1, Y1 = [earth.x], [earth.y]
X2, Y2 = [sun.x], [sun.y]


dt = 10000  # fixed timestep
total_time = 0 # Tracks seconds passed
orbit_detected = False

# Trail 
trail = True
def step():
    global total_time

    # Equations for each place in time
    # distance = the distance from the center of the sun to the center of the earth

    # Distance between the two stars for each value
    dx = sun.x - earth.x
    dy = sun.y - earth.y
    # The distance between the two stars using pythagorean theorem
    r = (dx**2 + dy**2)**0.5
    
    # Newtons law of gravitation
    F = G * earth.mass * sun.mass / r**2
    # X direction and Y direction forces
    Fx = F * dx / r
    Fy = F * dy / r

    # Makes forces into acceleration: 
    earth.ax = Fx / earth.mass
    earth.ay = Fy / earth.mass
    # Negative bc equal and opposite reaction
    sun.ax = -Fx / sun.mass
    sun.ay = -Fy / sun.mass

    # finds the new velocity
    earth.vx += earth.ax * dt
    earth.vy += earth.ay * dt
    sun.vx += sun.ax * dt
    sun.vy += sun.ay * dt

    # new x and y positions
    earth.x += earth.vx * dt
    earth.y += earth.vy * dt
    sun.x += sun.vx * dt
    sun.y += sun.vy * dt

    total_time += dt

trail = True
def animate(placeholder):
    # Clears the last point
    plt.cla()

    
    if len(X1) > 2:
    # Detects the highest, lowest, rightmost, and leftmost points in the orbit and prints their coordinates
        # Highest point
        if Y1[-2] > Y1[-3] and Y1[-2] > Y1[-1]:
            print("Highest point:")
            print("x =", X1[-2])
            print("y =", Y1[-2])
            print()

        # Lowest point
        if Y1[-2] < Y1[-3] and Y1[-2] < Y1[-1]:
            print("Lowest point:")
            print("x =", X1[-2])
            print("y =", Y1[-2])
            print()

        # Rightmost point
        if X1[-2] > X1[-3] and X1[-2] > X1[-1]:
            print("Rightmost point:")
            print("x =", X1[-2])
            print("y =", Y1[-2])
            print()

        # Leftmost point
        if X1[-2] < X1[-3] and X1[-2] < X1[-1]:
            print("Leftmost point:")
            print("x =", X1[-2])
            print("y =", Y1[-2])
            print()
    
    # Lets the simulation run faster without giving up accuracy by doing 5 steps for every frame of the animation
    for i in range(5):
        step()

        # Calculates the orbital period in days
        if len(Y1) > 0 and Y1[-1] < 0 and earth.y >= 0:
            days = total_time / (24 * 3600)
            print(f"Time: {days:.2f} Days")
            print("-" * 30)
            orbit_detected = True
    # Adds the x and y positions to their respectful of star 1
    X1.append(earth.x)
    Y1.append(earth.y)
    # Adds the x and y positions to their respectful of star 2
    X2.append(sun.x)
    Y2.append(sun.y)
    

    plt.plot(X1, Y1)
    plt.plot(X2, Y2)

    # the interval of time the values of the planet will increase by


    # The marker for the earth
    plt.plot(earth.x, earth.y, marker="o", markersize=7)
    # The marker for the sun
    plt.plot(sun.x, sun.y, marker="o", markersize=12)

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