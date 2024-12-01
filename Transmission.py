from Cylinder import Cylinder
from Rectangle import Rectangle
import matplotlib.pyplot as plt

class Transmission():
    def __init__(self):
        self.center = (0,0,0)
        self.components = list()
        # Left Side Face
        # self.components.append(Rectangle(60, 420, 650, position=(150,0,-170)))
        self.components.append(Rectangle(60, 420, 90, position=(150,0,125)))
        self.components.append(Rectangle(60, 130, 160, position=(150,145,0)))
        self.components.append(Rectangle(60, 130, 160, position=(150,-145,0)))
        self.components.append(Rectangle(60, 420, 400, position=(150,0,-280)))


        # Right Side Face
        self.components.append(Rectangle(60, 420, 90, position=(-450,0,125)))
        self.components.append(Rectangle(60, 130, 160, position=(-450,145,0)))
        self.components.append(Rectangle(60, 130, 160, position=(-450,-145,0)))
        self.components.append(Rectangle(60, 420, 400, position=(-450,0,-280)))
        
        # Bottom Face
        self.components.append(Rectangle(660, 420, 60, position=(-150, 0, -450)))

        # Front Face
        self.components.append(Rectangle(660, 60, 650, position=(-150, 180, -155)))

        # Back Face
        self.components.append(Rectangle(660, 60, 650, position=(-150, -180, -155)))
    def plot(self, ax: plt.Axes):
        for part in self.components:
            part.plot(ax)
