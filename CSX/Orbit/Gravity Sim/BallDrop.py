from ballClass import ball

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Two lists that store X and Y positions
X = [0]
Y = [0]

t = 0                                   # Time
v = 15                                  # Initial Velo


def animate(i):
    # Begins by clearing all previous information from the graph
    plt.cla()

    global t
    global v
    global Y

    delta = (v*t)-((9.8/2)*(t*t))

    Y.append(Y[-1]+delta)

    t += .250

    if delta < -100:
        t = 0
        Y = [0]
    print(delta)
    print(Y[-1])
    

    

    plt.plot(X[-1], Y[-1], marker="o", markersize=8)

    # Sets display
    plt.axis('equal')
    plt.axis([-200, 200, -200, 200])

fig, ax = plt.subplots()


# sets up the animation object
# plt.gcf() uses the current figure
# animate is the function that updates the data and graph
# interval is the time in milliseconds between frames
ani = FuncAnimation(plt.gcf(), animate, interval=250)

plt.show()