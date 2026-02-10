def x_position(x, Vx, delta):       #x postion 
    new_x = x + Vx*delta            #find the new x postion 
    return new_x

def y_position(y, Vy, delta):
    new_y = y + Vy * delta
    return new_y

def Ax_value(x, y, host_mass, g):
    new_Ax = -1 * g * host_mass * x/(x**2 + y**2)**1.5
    return new_Ax

def Ay_value(x, y, host_mass, g):
    new_Ay = -1 * g * host_mass * y/(x**2 + y**2)**1.5
    return new_Ay

def Vx_value(Vx, Ax, delta):
    new_Vx = Vx + Ax * delta
    return new_Vx

def Vy_value(Vy, Ay, delta):
    new_Vy = Vy + Ay * delta
    return new_Vy