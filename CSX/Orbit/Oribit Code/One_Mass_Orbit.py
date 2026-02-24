import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Planet_Class import planet

# Centrifugal constant
G = 6.67E-11    
# mass of sun  
M_sun = 1.989e30

# 5.972e24, 6.371e6, 0, 29780, 1.496e11, 0
# Planet format = mass, radius, vx, vy, x, y
earth = planet(5.972e24, 6.371e6, 0, 35000, 1.496e11, 0)

# A list of the positions of X and Y
X = [earth.x]
Y = [earth.y]

time = 0
# Trail 
trail = True
def step():
    # Equations for each place in time
    # distance = the distance from the center of the sun to the center of the earth

    distance = (earth.x**2 + earth.y**2)**0.5

    earth.ax = (-G * M_sun * earth.x) / distance**3
    earth.ay = (-G * M_sun * earth.y) / distance**3

    earth.vx += earth.ax * time
    earth.vy += earth.ay * time

    earth.x += earth.vx * time
    earth.y += earth.vy * time

trail = True
def animate(placeholder):
    # Clears the last point
    plt.cla()

    global time

    step()

    # Adds the x and y positions to their respectful 
    X.append(earth.x)
    Y.append(earth.y)

    # the interval of time the values of the planet will increase by
    time += 30

    # if trail is true draw the previous trail values
    if trail:
        plt.plot(X, Y)

    # The marker for the earth
    plt.plot(X[-1], Y[-1], marker="o", markersize=8)
    # The marker for the sun
    plt.plot(0, 0, marker="o", markersize=12)

    plt.axis('equal')
    # The x dimensions of the chart
    plt.xlim(-3.6e11, 3.6e11)
    # The y dimensions of the chart
    plt.ylim(-3.6e11, 3.6e11)


fig, ax = plt.subplots()

# sets up the animation object
# animate is the function that updates the data and graph
# interval is the time in milliseconds between frames
ani = FuncAnimation(fig, animate, interval= 10)

# shows the graph
plt.show()