import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


trail = True

# Two lists that store X and Y positions
X = [0]
Y = [0]

# Animations function
# Runs every time the screen needs to be updated
# You need one argument for the function to operate properly
def animate(i):
    # Begins by clearing all previous information from the graph
    plt.cla()
    # Generate one step - the function being modeled is y = x^2
    X.append(X[-1]+0.1)
    Y.append(X[-1]**2)

    # if trail is true draw the previous trail values
    if trail:
        plt.plot(X, Y)
    
    # Plots single point
    plt.plot(X[-1], Y[-1], marker="o", markersize=8)

    # Sets display
    plt.axis('equal')
    plt.axis([-20, 20, -20, 20])


fig, ax = plt.subplots()


# sets up the animation object
# plt.gcf() uses the current figure
# animate is the function that updates the data and graph
# interval is the time in milliseconds between frames
ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.show()