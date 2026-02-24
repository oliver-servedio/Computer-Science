'''
Author: Oliver Servedio, Nick Triplett
Description: This script simulates the orbital dynamics of a three-body system consisting of a Sun-like star, an Earth-like planet, and a Trojan asteroid. The simulation utilizes Newton's Law of Universal Gravitation to calculate trajectories.
and their positions are updated using Newton's law of gravitation.
Instructor: Mr. Campbell, Ms. Iversen, Mr. Carr
Date: February 23, 2026
Bugs: Will drift over time due to a high value of delta t but remains stable for several orbits to the human eye
Log: 3.0 updated to include a trojan asteroid at the L4 point of the Earth-Sun system
'''

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from Planet_Class import planet

# Initial Stuff and Constants
G = 6.67E-11
M_SUN = 1.989e30
start_dist = 1.496e11
start_speed = 29780  # Speed for circular orbit

# 1. Create Sun and Earth
sun = planet(M_SUN, 6.96e8, 0, 0, 0, 0)
earth = planet(5.972e24, 6.371e6, 0, start_speed, start_dist, 0)

# 2. ORBITAL MATH: Place Trojan on the SAME ellipse
# Standard gravitational parameter; product of G and the central mass (Sun)
mu = G * M_SUN

# Semi-major axis: The average distance from the Sun, derived from the 
# vis-viva equation (total energy of the orbit)
a = 1 / (2/start_dist - start_speed**2 / mu)

# Eccentricity: Measures how "stretched" the ellipse is (0 = circle, <1 = ellipse)
# calculated by comparing starting distance to the semi-major axis
e = 1 - (start_dist / a)

# Semi-latus rectum: The distance from the focus (Sun) to the orbit
# measured perpendicular to the major axis; used to define the size of the ellipse
p = a * (1 - e**2)

# Angle for L4 Lagrange point
theta = math.pi / 3 

# Distance and velocity components at 60 degrees
r_t = p / (1 + e * math.cos(theta))
v_radial = math.sqrt(mu / p) * e * math.sin(theta)
v_transverse = math.sqrt(mu / p) * (1 + e * math.cos(theta))

# Convert Polar to Cartesian
t_x = r_t * math.cos(theta)
t_y = r_t * math.sin(theta)
t_vx = v_radial * math.cos(theta) - v_transverse * math.sin(theta)
t_vy = v_radial * math.sin(theta) + v_transverse * math.cos(theta)

# Create Trojan asteroid
trojan = planet(1e15, 1000, t_vx, t_vy, t_x, t_y)

# --- SIMULATION SETTINGS ---
X1, Y1, X3, Y3 = [earth.x], [earth.y], [trojan.x], [trojan.y]
dt = 2000  # Smaller timestep for elliptical accuracy

def step():
    # 1. Reset Accelerations
    sun.ax = sun.ay = earth.ax = earth.ay = trojan.ax = trojan.ay = 0

    # 2. Manual Gravity (Sun-Earth)
    dx_se, dy_se = sun.x - earth.x, sun.y - earth.y
    r_se = (dx_se**2 + dy_se**2)**0.5
    F_se = G * earth.mass * sun.mass / r_se**2
    earth.ax += (F_se * dx_se / r_se) / earth.mass
    earth.ay += (F_se * dy_se / r_se) / earth.mass
    sun.ax   -= (F_se * dx_se / r_se) / sun.mass
    sun.ay   -= (F_se * dy_se / r_se) / sun.mass

    # 3. Manual Gravity (Sun-Trojan)
    dx_st, dy_st = sun.x - trojan.x, sun.y - trojan.y
    r_st = (dx_st**2 + dy_st**2)**0.5
    F_st = G * trojan.mass * sun.mass / r_st**2
    trojan.ax += (F_st * dx_st / r_st) / trojan.mass
    trojan.ay += (F_st * dy_st / r_st) / trojan.mass
    sun.ax    -= (F_st * dx_st / r_st) / sun.mass
    sun.ay    -= (F_st * dy_st / r_st) / sun.mass

    # 4. Manual Gravity (Earth-Trojan)
    dx_et, dy_et = earth.x - trojan.x, earth.y - trojan.y
    r_et = (dx_et**2 + dy_et**2)**0.5
    F_et = G * earth.mass * trojan.mass / r_et**2
    earth.ax  -= (F_et * dx_et / r_et) / earth.mass
    earth.ay  -= (F_et * dy_et / r_et) / earth.mass
    trojan.ax += (F_et * dx_et / r_et) / trojan.mass
    trojan.ay += (F_et * dy_et / r_et) / trojan.mass

    # 5. Semi-Implicit Euler Update
    for p in [sun, earth, trojan]:
        p.vx += p.ax * dt
        p.vy += p.ay * dt
        p.x += p.vx * dt
        p.y += p.vy * dt

def animate(frame):
    plt.cla()
    
    # This section is commented out because it was just used to find 3 points that I could use to verify the stability of the trojan, as used in my answer to part 3.
    #         print("highest point:")
    #         print("earth", earth.x, earth.y)
    #         print("trojan", trojan.x, trojan.y)
    #         print("sun", sun.x, sun.y)
    #         print()

    #     # Lowest point
    #     if Y1[-2] < Y1[-3] and Y1[-2] < Y1[-1]:
    #         print("lowest point:")
    #         print("earth", earth.x, earth.y)
    #         print("trojan", trojan.x, trojan.y)
    #         print("sun", sun.x, sun.y)
    #         print()
        
    #     # Rightmost point
    #     if X1[-2] > X1[-3] and X1[-2] > X1[-1]:
    #         print("Rightmost point:")
    #         print("earth", earth.x, earth.y)
    #         print("trojan", trojan.x, trojan.y)
    #         print("sun", sun.x, sun.y)
    #         print()

    

    # Physics sub-stepping for smoothness
    for _ in range(20):
        step()

    # Adds the x and y positions to their respectful of earth and trojan
    X1.append(earth.x)
    Y1.append(earth.y)
    X3.append(trojan.x)
    Y3.append(trojan.y)



    # Drawing the little dotted triangle
    plt.plot([sun.x, earth.x, trojan.x, sun.x], 
             [sun.y, earth.y, trojan.y, sun.y], 
             color='gray', linestyle='--', alpha=0.3)

    # Plot Trails
    plt.plot(X1, Y1, color='blue', label="Earth Path")
    plt.plot(X3, Y3, color='green', label="Trojan Path")

    # Plot Bodies
    plt.plot(sun.x, sun.y, 'yo', markersize=12)    # Sun
    plt.plot(earth.x, earth.y, 'bo', markersize=8) # Earth
    plt.plot(trojan.x, trojan.y, 'go', markersize=4) # Trojan

    plt.axis('equal')
    plt.xlim(-5e11, 5e11)
    plt.ylim(-5e11, 5e11)
    plt.title("L4 Trojan Stability")

fig, ax = plt.subplots(figsize=(8,8))
ani = FuncAnimation(fig, animate, interval=1)
plt.show()