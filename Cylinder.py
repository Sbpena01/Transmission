import numpy as np

class Cylinder():
    def __init__(self, center: list[float], radius: float, height: float, resolution=100):
        # Create the theta and x coordinates for the cylinder (horizontal orientation)
        theta = np.linspace(0, 2 * np.pi, resolution)
        x = np.linspace(-height / 2, height / 2, resolution)
        theta, X = np.meshgrid(theta, x)  # Meshgrid creates a grid for θ (angular) and x (length)

        # Store the center of the cylinpoint
        self.center = center
        
        # Parametric equations for the horizontal cylinder's coordinates
        self.X = X + center[0]  # X coordinate (x moves along the length of the cylinder)
        self.Y = radius * np.cos(theta) + center[1]  # Y coordinate (radius * cos(theta) for the circle)
        self.Z = radius * np.sin(theta) + center[2]  # Z coordinate (radius * sin(theta) for the circle)
    
    def translate(self, translation: tuple):
        self.center[0] = translation[0]
        self.center[1] = translation[1]
        self.center[2] = translation[2]
        self.X += translation[0]
        self.Y += translation[1]
        self.Z += translation[2]
    
    def rotate(self, angle: float, axis: str, point: tuple = None):
        if point is None:
            point = self.center
        if len(point) != 3:
            raise ValueError("Point should be an (x, y, z) tuple.")
        # Step 1: Translate the cylinder so its center is at the origin
        X_translated = self.X - point[0]
        Y_translated = self.Y - point[1]
        Z_translated = self.Z - point[2]

        # Step 2: Rotation matrix for rotation around x, y, or z axis
        angle = angle[0]
        rotation_matrix = None
        if axis == 'x':
            rotation_matrix = np.array([[1, 0, 0],
                                        [0, np.cos(angle), -np.sin(angle)],
                                        [0, np.sin(angle), np.cos(angle)]])
        elif axis == 'y':
            rotation_matrix = np.array([[np.cos(angle), 0, np.sin(angle)],
                                        [0, 1, 0],
                                        [-np.sin(angle), 0, np.cos(angle)]])
        elif axis == 'z':
            rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                        [np.sin(angle), np.cos(angle), 0],
                                        [0, 0, 1]])

        # Step 3: Apply the rotation to the translated points
        points = np.vstack([X_translated.ravel(), Y_translated.ravel(), Z_translated.ravel()])
        rotated_points = np.dot(rotation_matrix, points).T

        # Step 4: Reshape the rotated points back to the original shape
        rotated_X, rotated_Y, rotated_Z = rotated_points[:, 0].reshape(self.X.shape), rotated_points[:, 1].reshape(self.Y.shape), rotated_points[:, 2].reshape(self.Z.shape)

        # Step 5: Translate the cylinder back to its original position
        self.X = rotated_X + point[0]
        self.Y = rotated_Y + point[1]
        self.Z = rotated_Z + point[2]
