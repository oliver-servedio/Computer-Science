# Make a class with properties of Planets
# Mass, Radius, Initial Velo X and Y,Placement X and Y 

class planet:

    def __init__(self, mass, radius, vx, vy, x, y):

        self.mass = mass                            # The mass of the planet
        self.radius = radius                        # The Radius of the planet
        self.vx = vx                                # The initial velo in the x direction
        self.vy = vy                                # The initial velo in the y direction
        self.x = x                                  # The position of x
        self.y= y                                   # The position of y
        self.ax = 0                                 # The acceleration value of x
        self.ay = 0                                 # The acceleration value of y


    