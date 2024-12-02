from Cylinder import Cylinder
from Rectangle import Rectangle
import matplotlib.pyplot as plt
import numpy as np

class Transmission():
    def __init__(self):
        self.center = (0,0,0)
        self.components = list[Rectangle]()
        # Left Side Face
        self.components.append(Rectangle(60, 420, 90, center=(150,0,125)))
        self.components.append(Rectangle(60, 130, 160, center=(150,145,0)))
        self.components.append(Rectangle(60, 130, 160, center=(150,-145,0)))
        self.components.append(Rectangle(60, 420, 400, center=(150,0,-280)))


        # Right Side Face
        self.components.append(Rectangle(60, 420, 90, center=(-450,0,125)))
        self.components.append(Rectangle(60, 130, 160, center=(-450,145,0)))
        self.components.append(Rectangle(60, 130, 160, center=(-450,-145,0)))
        self.components.append(Rectangle(60, 420, 400, center=(-450,0,-280)))
        
        # Bottom Face
        self.components.append(Rectangle(660, 420, 60, center=(-150, 0, -450)))

        # Front Face
        self.components.append(Rectangle(660, 60, 650, center=(-150, 180, -155)))

        # Back Face
        self.components.append(Rectangle(660, 60, 650, center=(-150, -180, -155)))

    def plot(self, ax: plt.Axes):
        for part in self.components:
            part.plot(ax)

    def checkForCollision(self, cylinder: Cylinder):
        # Calculate cylinder bounding box
        cylinder