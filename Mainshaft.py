from Cylinder import Cylinder

class Mainshaft():
    def __init__(self, x: float, y: float, z: float, theta: float):
        self.center_x = x
        self.center_y = y
        self.center_z = z
        self.theta = theta
        
        self.v = 0.0  # Linear Velocity
        self.w = 0.0  # Angular Velocity
        
        # The mainshaft is basically a combination of 3D cylinders. This stores all the cylinders.
        self.cylinders: list[Cylinder] = list()
        self.createShaft()
    
    def createShaft(self):
        self.cylinders.append(Cylinder((self.center_x, self.center_y, self.center_z), 72, 660))
        self.cylinders.append(Cylinder((-98,0,0), 180, 384))
        self.cylinders.append(Cylinder((67,0,0), 260, 50))
        self.cylinders.append(Cylinder((1,0,0), 239, 60))
        self.cylinders.append(Cylinder((-54,0,0), 240, 50))
        self.cylinders.append(Cylinder((-120,0,0), 212, 50))
        self.cylinders.append(Cylinder((-216,0,0), 239, 60))
        