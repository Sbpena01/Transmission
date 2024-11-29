from Part import Part
from Cylinder import Cylinder

class Mainshaft(Part):
    def __init__(self, x, y, z, roll, pitch, yaw):
        super().__init__(x, y, z, roll, pitch, yaw)
        
    def createPart(self):
        self.cylinders.append(Cylinder([self.state[0], self.state[1], self.state[2]], 72, 660))
        self.cylinders.append(Cylinder([-98,0,0], 180, 384))
        self.cylinders.append(Cylinder([67,0,0], 260, 50))
        self.cylinders.append(Cylinder([1,0,0], 239, 60))
        self.cylinders.append(Cylinder([-54,0,0], 240, 50))
        self.cylinders.append(Cylinder([-120,0,0], 212, 50))
        self.cylinders.append(Cylinder([-216,0,0], 239, 60))
    
