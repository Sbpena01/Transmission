from Part import Part
from Cylinder import Cylinder

class Mainshaft(Part):
    def __init__(self, x, y, z, roll, pitch, yaw):
        super().__init__(x, y, z, roll, pitch, yaw)
        
    def createPart(self):
        self.cylinders.append(Cylinder([self.state[0].item(), self.state[1].item(), self.state[2].item()], 36, 660))
        self.cylinders.append(Cylinder([-98.0,0.0,0], 90, 384))
        self.cylinders.append(Cylinder([67.0,0.0,0.0], 130, 50))
        self.cylinders.append(Cylinder([1.0,0.0,0.0], 120, 60))
        self.cylinders.append(Cylinder([-54.0,0.0,0.0], 120, 50))
        self.cylinders.append(Cylinder([-120.0,0.0,0.0], 106, 50))
        self.cylinders.append(Cylinder([-216.0,0.0,0.0], 120, 60))
    
