from Transmission import Transmission
from Cylinder import Cylinder
import matplotlib.pyplot as plt
import numpy as np

class Part():
    def __init__(self, x: float, y: float, z: float, roll, pitch, yaw):    
        # Stores the state of the system as a 12x1 vector.
        # Stores the position, orientation, linear velocity, and angular velocity
        self.state = np.array((
            [x],  # Position
            [y],
            [z],
            [roll],  # Orientation
            [pitch],
            [yaw],
            [0.0],  # Linear Velocity
            [0.0],
            [0.0],
            [0.0],  # Angular Velocity
            [0.0],
            [0.0],
        ))
                
        # The mainshaft is basically a combination of 3D cylinders. This stores all the cylinders.
        self.cylinders: list[Cylinder] = list()
        self.createPart()
    
    
    
    def createPart(self):
        pass
    
    def getPosition(self):
        return (self.state[0], self.state[1], self.state[2])
    
    def getOrientation(self):
        return (self.state[3], self.state[4], self.state[5])
    
    def rotate(self, angle: float, axis: str):
        for cylinder in self.cylinders:
            cylinder.rotate(angle, axis, point=(self.state[0], self.state[1], self.state[2]))
    
    def translate(self, translation: tuple):
        for cylinder in self.cylinders:
            cylinder.translate(translation)
    
    def updateModel(self, diff: np.array):
        for cylinder in self.cylinders:
            cylinder.translate((diff[0], diff[1], diff[2]))
            rpy = [(diff[3], 'x'), (diff[4], 'y'), (diff[5], 'z')]
            for angle in rpy:
                cylinder.rotate(angle[0], angle[1], point=(self.state[0], self.state[1], self.state[2]))
            cylinder.updateBoundingBox(diff, self.state)
            
            
    def plot(self, ax: plt.Axes, show_bounding_boxes=False):
        for cylinder in self.cylinders:
            ax.plot_surface(cylinder.X, cylinder.Y, cylinder.Z, color='b', alpha=0.5, linewidth=1)
            if show_bounding_boxes:
                cylinder.bounding_box.plot(ax, edge_color='gray')
            
    def step(self, dt:float):
        F = np.array([
            [1, 0, 0, 0, 0, 0, dt, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, dt, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, dt, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, dt, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, dt, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, dt],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        ])
        new_state = F @ self.state
        diff = new_state - self.state
        self.state = new_state
        self.updateModel(diff)
    
    def setLinearVelocity(self, new_linear_velocity: tuple):
        if len(new_linear_velocity) != 3:
            raise ValueError("New Linear Velocity should be a length of 3")
        self.state[6] = new_linear_velocity[0]
        self.state[7] = new_linear_velocity[1]
        self.state[8] = new_linear_velocity[2]
        
    def setAngularVelocity(self, new_angular_velocity: tuple):
        if len(new_angular_velocity) != 3:
            raise ValueError("New Angular Velocity should be a length of 3")
        self.state[9] = new_angular_velocity[0]
        self.state[10] = new_angular_velocity[1]
        self.state[11] = new_angular_velocity[2]
    
    def checkCollision(self, object: Transmission):
        collision = list()
        for box in object.components:
            for cylinder in self.cylinders:
                result = box.checkCollision(cylinder.bounding_box)
                if result:
                    collision.append(box.name)
        if len(collision) != 0:
            print(collision)
            return True
        return False
