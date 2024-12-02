from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

class Rectangle():
    def __init__(self, length, width, height, center=(0.0, 0.0, 0.0), orientation=(0, 0, 0)):
        self.length = length
        self.width = width
        self.height = height
        self.center = np.array(center)  # (x, y, z)
        self.roll = orientation[0]
        self.pitch = orientation[1]
        self.yaw = orientation[2]
        
        # Create the vertices of the rectangle (assuming it's aligned to the axes initially)
        self.vertices = np.array([
            [-length/2+center[0], -width/2+center[1], -height/2+center[2]],
            [ length/2+center[0], -width/2+center[1], -height/2+center[2]],
            [ length/2+center[0],  width/2+center[1], -height/2+center[2]],
            [-length/2+center[0],  width/2+center[1], -height/2+center[2]],
            [-length/2+center[0], -width/2+center[1],  height/2+center[2]],
            [ length/2+center[0], -width/2+center[1],  height/2+center[2]],
            [ length/2+center[0],  width/2+center[1],  height/2+center[2]],
            [-length/2+center[0],  width/2+center[1],  height/2+center[2]]
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

        self.edges = set()
        # Loop through faces and extract edges
        for face in self.faces:
            for i in range(len(face)):
                # Get the current vertex and the next one (wrap around)
                start_vertex = face[i]
                end_vertex = face[(i + 1) % len(face)]
                # Create an edge as a sorted tuple (to avoid duplicate edges)
                edge = tuple(sorted([tuple(start_vertex), tuple(end_vertex)]))
                self.edges.add(edge)

    def updateFaces(self):
        self.faces = [
            [self.vertices[0], self.vertices[1], self.vertices[2], self.vertices[3]],
            [self.vertices[4], self.vertices[5], self.vertices[6], self.vertices[7]],
            [self.vertices[0], self.vertices[1], self.vertices[5], self.vertices[4]],
            [self.vertices[2], self.vertices[3], self.vertices[7], self.vertices[6]],
            [self.vertices[1], self.vertices[2], self.vertices[6], self.vertices[5]],
            [self.vertices[4], self.vertices[7], self.vertices[3], self.vertices[0]] 
        ]

    def setCenter(self, center):
        self.center = center

    def translate(self, translation: np.array):
        self.center += translation.flatten()
        translated_vertices = self.vertices + translation.flatten()
        self.vertices = translated_vertices
        self.faces = [
            [translated_vertices[0], translated_vertices[1], translated_vertices[2], translated_vertices[3]],  # Bottom
            [translated_vertices[4], translated_vertices[5], translated_vertices[6], translated_vertices[7]],  # Top
            [translated_vertices[0], translated_vertices[1], translated_vertices[5], translated_vertices[4]],  # Front
            [translated_vertices[2], translated_vertices[3], translated_vertices[7], translated_vertices[6]],  # Back
            [translated_vertices[1], translated_vertices[2], translated_vertices[6], translated_vertices[5]],  # Right
            [translated_vertices[4], translated_vertices[7], translated_vertices[3], translated_vertices[0]]   # Left
        ]
    
    def rotate(self, angle, axis, point=None):
        if point is None:
            point = self.center
        translated_verticies = self.vertices - point.flatten()
        angle = angle.item()
        if axis == 'x':
            rotation_matrix = np.array([
                [1, 0, 0],
                [0, np.cos(angle), -np.sin(angle)],
                [0, np.sin(angle), np.cos(angle)]
            ])
            self.roll += angle
        elif axis == 'y':
            rotation_matrix = np.array([
                [np.cos(angle), 0, np.sin(angle)],
                [0, 1, 0],
                [-np.sin(angle), 0, np.cos(angle)]
            ])
            self.pitch += angle
        elif axis == 'z':
            rotation_matrix = np.array([
                [np.cos(angle), -np.sin(angle), 0],
                [np.sin(angle), np.cos(angle), 0],
                [0, 0, 1]
            ])
            self.yaw += angle
        else:
            raise ValueError("Axis must be 'x', 'y', or 'z'.")
        rotated_vertices = np.dot(translated_verticies, rotation_matrix.T)
        self.vertices = rotated_vertices + point.flatten()
        self.updateFaces()

    def plot(self, ax, edge_color: str = 'r'):
        #  # Translate the vertices based on the rectangle's center
        # translated_vertices = self.vertices + np.transpose(self.center)
        
        # # Create the faces for the translated vertices
        # translated_faces = [
        #     [translated_vertices[0], translated_vertices[1], translated_vertices[2], translated_vertices[3]],  # Bottom
        #     [translated_vertices[4], translated_vertices[5], translated_vertices[6], translated_vertices[7]],  # Top
        #     [translated_vertices[0], translated_vertices[1], translated_vertices[5], translated_vertices[4]],  # Front
        #     [translated_vertices[2], translated_vertices[3], translated_vertices[7], translated_vertices[6]],  # Back
        #     [translated_vertices[1], translated_vertices[2], translated_vertices[6], translated_vertices[5]],  # Right
        #     [translated_vertices[4], translated_vertices[7], translated_vertices[3], translated_vertices[0]]   # Left
        # ]
        
        # Plot the rectangle using Poly3DCollection
        if edge_color == 'r':
            poly3d = Poly3DCollection(self.faces, linewidths=1, edgecolors=edge_color, alpha=0.25)
        else:
            poly3d = Poly3DCollection(self.faces, linewidths=1, edgecolors=edge_color, alpha=0,)
        ax.add_collection3d(poly3d)

    def perpendicular(self, v):
        """Returns a perpendicular vector to the given vector."""
        return np.array([-v[1], v[0], 0])

    def project_polygon(self, polygon, axis):
        """Projects the polygon vertices onto the axis and returns the min and max projections."""
        projections = [np.dot(vertex, axis) for vertex in polygon]
        return min(projections), max(projections)
    
    def overlap(self, proj1, proj2):
        """Checks if two projections overlap."""
        return max(proj1[0], proj2[0]) <= min(proj1[1], proj2[1])

    def checkCollision(self, other_rect: 'Rectangle'):
        """Checks if this box collides with another box using the Separating Axis Theorem."""
        # Get transformed vertices of both boxes
        vertices1 = self.vertices
        vertices2 = other_rect.vertices
        
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
