import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Box:
    def __init__(self, length, width, height, center=(0.0, 0.0, 0.0), orientation=(0, 0, 0)):
        self.length = length
        self.width = width
        self.height = height
        self.center = np.array(center)  # (x, y, z)
        self.roll = orientation[0]  # rotation about x-axis (in radians)
        self.pitch = orientation[1]  # rotation about y-axis (in radians)
        self.yaw = orientation[2]  # rotation about z-axis (in radians)
        
        # Create the vertices of the rectangle (aligned to the axes initially)
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
        
        # Apply rotation and translation
        self.apply_transformation()

    def rotation_matrix(self, roll, pitch, yaw):
        """Generates a 3D rotation matrix for roll, pitch, and yaw angles (in radians)."""
        # Rotation matrix for X (roll)
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(roll), -np.sin(roll)],
            [0, np.sin(roll), np.cos(roll)]
        ])
        
        # Rotation matrix for Y (pitch)
        Ry = np.array([
            [np.cos(pitch), 0, np.sin(pitch)],
            [0, 1, 0],
            [-np.sin(pitch), 0, np.cos(pitch)]
        ])
        
        # Rotation matrix for Z (yaw)
        Rz = np.array([
            [np.cos(yaw), -np.sin(yaw), 0],
            [np.sin(yaw), np.cos(yaw), 0],
            [0, 0, 1]
        ])
        
        # Combined rotation matrix
        R = Rz @ Ry @ Rx
        return R

    def apply_transformation(self):
        """Applies the rotation and translation to the box vertices."""
        # Get the rotation matrix
        rotation = self.rotation_matrix(self.roll, self.pitch, self.yaw)
        
        # Rotate each vertex
        rotated_vertices = np.dot(self.vertices, rotation.T)
        
        # Translate the vertices by the center position
        self.transformed_vertices = rotated_vertices + self.center
        
    def get_transformed_vertices(self):
        """Returns the transformed vertices after rotation and translation."""
        return self.transformed_vertices

    def plot(self, ax, color='b'):
        """Plots the box on a 3D axis."""
        # Define faces using indices into the vertices
        faces = [
            [self.transformed_vertices[0], self.transformed_vertices[1], self.transformed_vertices[2], self.transformed_vertices[3]],  # Bottom
            [self.transformed_vertices[4], self.transformed_vertices[5], self.transformed_vertices[6], self.transformed_vertices[7]],  # Top
            [self.transformed_vertices[0], self.transformed_vertices[1], self.transformed_vertices[5], self.transformed_vertices[4]],  # Front
            [self.transformed_vertices[2], self.transformed_vertices[3], self.transformed_vertices[7], self.transformed_vertices[6]],  # Back
            [self.transformed_vertices[1], self.transformed_vertices[2], self.transformed_vertices[6], self.transformed_vertices[5]],  # Right
            [self.transformed_vertices[4], self.transformed_vertices[7], self.transformed_vertices[3], self.transformed_vertices[0]]   # Left
        ]
        
        # Plot each face
        poly3d = Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='r', alpha=.25)
        ax.add_collection3d(poly3d)
        
        # Set plot limits
        ax.set_xlim([self.center[0] - self.length, self.center[0] + self.length])
        ax.set_ylim([self.center[1] - self.width, self.center[1] + self.width])
        ax.set_zlim([self.center[2] - self.height, self.center[2] + self.height])

    def dot_product(self, v1, v2):
        """Returns the dot product of two vectors."""
        return np.dot(v1, v2)
    
    def perpendicular(self, v):
        """Returns a perpendicular vector to the given vector."""
        return np.array([-v[1], v[0], 0])

    def project_polygon(self, polygon, axis):
        """Projects the polygon vertices onto the axis and returns the min and max projections."""
        projections = [self.dot_product(vertex, axis) for vertex in polygon]
        return min(projections), max(projections)

    def overlap(self, proj1, proj2):
        """Checks if two projections overlap."""
        return max(proj1[0], proj2[0]) <= min(proj1[1], proj2[1])

    def sat_collision(self, other_box):
        """Checks if this box collides with another box using the Separating Axis Theorem."""
        # Get transformed vertices of both boxes
        vertices1 = self.get_transformed_vertices()
        vertices2 = other_box.get_transformed_vertices()
        
        # Check all edges of both boxes for separating axes
        for i in range(len(vertices1)):
            p1 = vertices1[i]
            p2 = vertices1[(i + 1) % len(vertices1)]  # Next vertex (wrap around)
            
            # Find edge vector
            edge = p2 - p1
            
            # Get perpendicular axis to the edge
            axis = self.perpendicular(edge)
            
            # Project both polygons onto the axis
            proj1 = self.project_polygon(vertices1, axis)
            proj2 = self.project_polygon(vertices2, axis)
            
            # If projections do not overlap, there is no collision
            if not self.overlap(proj1, proj2):
                return False
        
        # Check all edges of the other box
        for i in range(len(vertices2)):
            p1 = vertices2[i]
            p2 = vertices2[(i + 1) % len(vertices2)]  # Next vertex (wrap around)
            
            # Find edge vector
            edge = p2 - p1
            
            # Get perpendicular axis to the edge
            axis = self.perpendicular(edge)
            
            # Project both polygons onto the axis
            proj1 = self.project_polygon(vertices1, axis)
            proj2 = self.project_polygon(vertices2, axis)
            
            # If projections do not overlap, there is no collision
            if not self.overlap(proj1, proj2):
                return False
        
        # If projections overlap on all axes, the boxes collide
        return True

# Example usage
box1 = Box(length=2, width=3, height=4, center=(1, 2, 3), orientation=(np.pi/4, np.pi/4, np.pi/4))  # Box 1
box2 = Box(length=2, width=3, height=4, center=(3, 6, 5), orientation=(np.pi/4, np.pi/4, np.pi/4))  # Box 2

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot box 1 and box 2
box1.plot(ax, color='b')
box2.plot(ax, color='g')

# Collision check
collision = box1.sat_collision(box2)
print("Collision Detected:", collision)

# Show plot
plt.show()
