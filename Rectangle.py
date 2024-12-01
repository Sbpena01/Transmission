from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

class Rectangle():
    def __init__(self, length, width, height, position=(0, 0, 0), orientation=(0, 0, 0)):
        self.length = length
        self.width = width
        self.height = height
        self.position = np.array(position)  # (x, y, z)
        self.orientation = np.array(orientation)  # (roll, pitch, yaw)
        
        # Create the vertices of the rectangle (assuming it's aligned to the axes initially)
        self.vertices = np.array([
            [-length/2, -width/2, -height/2],
            [ length/2, -width/2, -height/2],
            [ length/2,  width/2, -height/2],
            [-length/2,  width/2, -height/2],
            [-length/2, -width/2,  height/2],
            [ length/2, -width/2,  height/2],
            [ length/2,  width/2,  height/2],
            [-length/2,  width/2,  height/2]
        ])
        
        # Initialize the faces of the rectangle (6 faces for a box)
        self.faces = [
            [self.vertices[0], self.vertices[1], self.vertices[2], self.vertices[3]],  # Bottom
            [self.vertices[4], self.vertices[5], self.vertices[6], self.vertices[7]],  # Top
            [self.vertices[0], self.vertices[1], self.vertices[5], self.vertices[4]],  # Front
            [self.vertices[2], self.vertices[3], self.vertices[7], self.vertices[6]],  # Back
            [self.vertices[1], self.vertices[2], self.vertices[6], self.vertices[5]],  # Right
            [self.vertices[4], self.vertices[7], self.vertices[3], self.vertices[0]]   # Left
        ]

    def translate(self, translation):
        self.position += np.array(translation)
        self.vertices += self.position
    
    def rotate(self, angle, axis):
        # You can add rotation logic here, for now, let's assume we just translate without rotating
        pass

    def plot(self, ax):
         # Translate the vertices based on the rectangle's position
        translated_vertices = self.vertices + self.position
        
        # Create the faces for the translated vertices
        translated_faces = [
            [translated_vertices[0], translated_vertices[1], translated_vertices[2], translated_vertices[3]],  # Bottom
            [translated_vertices[4], translated_vertices[5], translated_vertices[6], translated_vertices[7]],  # Top
            [translated_vertices[0], translated_vertices[1], translated_vertices[5], translated_vertices[4]],  # Front
            [translated_vertices[2], translated_vertices[3], translated_vertices[7], translated_vertices[6]],  # Back
            [translated_vertices[1], translated_vertices[2], translated_vertices[6], translated_vertices[5]],  # Right
            [translated_vertices[4], translated_vertices[7], translated_vertices[3], translated_vertices[0]]   # Left
        ]
        
        # Plot the rectangle using Poly3DCollection
        poly3d = Poly3DCollection(translated_faces, linewidths=1, edgecolors='r', alpha=0.25)
        ax.add_collection3d(poly3d)
