import numpy as np

class Cylinder():
    def __init__(self, center: list[float], radius: float, height: float, resolution=100):
        """
        Initializes a horizontal cylinder.
        
        Args:
        - center (list[float]): The center of the cylinder (x, y, z).
        - radius (float): The radius of the cylinder.
        - height (float): The height (length) of the cylinder along the x-axis.
        - resolution (int): The resolution of the cylinder (number of points).
        """
        # Create the theta and x coordinates for the cylinder
        theta = np.linspace(0, 2 * np.pi, resolution)
        x = np.linspace(-height / 2, height / 2, resolution)
        theta, X = np.meshgrid(theta, x)  # Meshgrid creates a grid for θ (angular) and x (length)

        # Store the center of the cylinder
        self.center = np.array(center)

        # Parametric equations for the horizontal cylinder's coordinates
        self.X = X + center[0]  # X coordinate (x moves along the length of the cylinder)
        self.Y = radius * np.cos(theta) + center[1]  # Y coordinate (radius * cos(theta) for the circle)
        self.Z = radius * np.sin(theta) + center[2]  # Z coordinate (radius * sin(theta) for the circle)

    def translate(self, translation: tuple):
        """
        Translates the cylinder by the given (x, y, z) tuple.
        
        Args:
        - translation (tuple): The translation vector (dx, dy, dz).
        """
        self.center += np.array(translation)
        self.X += translation[0]
        self.Y += translation[1]
        self.Z += translation[2]

    def rotate(self, angle: float, axis: str, point: tuple = None):
        """
        Rotates the cylinder around a specific axis and point.
        
        Args:
        - angle (float): The angle in radians to rotate the cylinder.
        - axis (str): The axis of rotation ('x', 'y', or 'z').
        - point (tuple, optional): The point to rotate around (defaults to the cylinder's center).
        """
        if point is None:
            point = self.center  # Default rotation point is the cylinder's center
        if len(point) != 3:
            raise ValueError("Point should be a (x, y, z) tuple.")

        # Step 1: Translate the cylinder so its center is at the origin
        X_translated = self.X - point[0]
        Y_translated = self.Y - point[1]
        Z_translated = self.Z - point[2]

        # Step 2: Define the rotation matrix based on the chosen axis
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
        else:
            raise ValueError("Invalid axis. Choose from 'x', 'y', or 'z'.")

        # Step 3: Apply the rotation to the translated points
        points = np.vstack([X_translated.ravel(), Y_translated.ravel(), Z_translated.ravel()])
        rotated_points = np.dot(rotation_matrix, points).T

        # Step 4: Reshape the rotated points back to the original shape
        rotated_X, rotated_Y, rotated_Z = rotated_points[:, 0].reshape(self.X.shape), rotated_points[:, 1].reshape(self.Y.shape), rotated_points[:, 2].reshape(self.Z.shape)

        # Step 5: Translate the cylinder back to its original position
        self.X = rotated_X + point[0]
        self.Y = rotated_Y + point[1]
        self.Z = rotated_Z + point[2]

    def plot(self, ax):
        """
        Plots the cylinder on a 3D axis using matplotlib.
        
        Args:
        - ax: The matplotlib 3D axis object.
        """
        # Plot the surface of the cylinder
        ax.plot_surface(self.X, self.Y, self.Z, color='b', alpha=0.5)




import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a cylinder
cylinder = Cylinder(center=[0, 0, 0], radius=5, height=10, resolution=100)

# Translate the cylinder by (5, 5, 0)
cylinder.translate((5, 5, 0))

# Rotate the cylinder 45 degrees around the z-axis
cylinder.rotate(np.radians(45), 'z')

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the cylinder
cylinder.plot(ax)

# Show the plot
plt.show()
