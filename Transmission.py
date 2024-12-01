from Cylinder import Cylinder
from Rectangle import Rectangle
import matplotlib.pyplot as plt

class Transmission():
    def __init__(self):
        self.center = (0,0,0)
        self.components = list()
        self.components.append(Rectangle(60, 420, 650, position=(150,0,-170)))
        self.components.append(Rectangle(660, 420, 60, position=(-150, 0, -525)))
        self.components.append(Rectangle(60, 420, 650, position=(150-600,0,-170)))
        
    def plot(self, ax: plt.Axes):
        for part in self.components:
            part.plot(ax)
