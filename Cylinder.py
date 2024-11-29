import numpy as np

class Cylinder():
    def __init__(self, center: tuple[int], radius: float, height: float, resolution=100):
        # Create the theta and x coordinates for the cylinder (horizontal orientation)
        theta = np.linspace(0, 2 * np.pi, resolution)
        x = np.linspace(-height / 2, height / 2, resolution)
        theta, X = np.meshgrid(theta, x)  # Meshgrid creates a grid for θ (angular) and x (length)

        # Store the center of the cylinder
        self.center = center
        
        # Parametric equations for the horizontal cylinder's coordinates
        self.X = X + center[0]  # X coordinate (x moves along the length of the cylinder)
        self.Y = radius * np.cos(theta) + center[1]  # Y coordinate (radius * cos(theta) for the circle)
        self.Z = radius * np.sin(theta) + center[2]  # Z coordinate (radius * sin(theta) for the circle)
        
    def rotate(self, angle: float, axis: str):
        """
        Rotate the cylinder around its center.
        :param angle: The angle by which to rotate (in radians)
        :param axis: The axis to rotate around ('x', 'y', or 'z')
        """
        # Step 1: Translate the cylinder so its center is at the origin
        X_translated = self.X - self.center[0]
        Y_translated = self.Y - self.center[1]
        Z_translated = self.Z - self.center[2]

        # Step 2: Rotation matrix for rotation around x, y, or z axis
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
        self.X = rotated_X + self.center[0]
        self.Y = rotated_Y + self.center[1]
        self.Z = rotated_Z + self.center[2]
