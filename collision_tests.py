import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def vector_distance(v1, v2):
    """Calculate the Euclidean distance between two points in 3D space."""
    return np.linalg.norm(v1 - v2)

def check_cylinder_collision(center1, radius1, height1, center2, radius2, height2):
    """Check if two cylinders collide based on their center, radius, and height."""
    
    # Check if vertical extents (heights) overlap
    z1_min = center1[2] - height1 / 2
    z1_max = center1[2] + height1 / 2
    z2_min = center2[2] - height2 / 2
    z2_max = center2[2] + height2 / 2
    
    # If the z-ranges of the two cylinders do not overlap, no collision
    if z1_max < z2_min or z2_max < z1_min:
        return False
    
    # Check if the horizontal distance between centers is less than the sum of their radii
    horizontal_distance = np.linalg.norm(center1[:2] - center2[:2])  # x and y distance
    if horizontal_distance < (radius1 + radius2):
        return True  # Colliding
    else:
        return False  # Not colliding

# Define two cylinders (center, radius, height)
center1 = np.array([0, 0, 5])  # center of cylinder 1
radius1 = 1  # radius of cylinder 1
height1 = 5  # height of cylinder 1

center2 = np.array([3, 0, 6])  # center of cylinder 2
radius2 = 1  # radius of cylinder 2
height2 = 5  # height of cylinder 2

# Check if the cylinders are colliding
collision = check_cylinder_collision(center1, radius1, height1, center2, radius2, height2)

# Visualize the result
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a mesh grid for the theta values (for the cylinder's circular cross-sections)
theta = np.linspace(0, 2 * np.pi, 100)

# Create the z values for both cylinders (from center - height/2 to center + height/2)
z1 = np.linspace(center1[2] - height1 / 2, center1[2] + height1 / 2, 100)
z2 = np.linspace(center2[2] - height2 / 2, center2[2] + height2 / 2, 100)

# Create the 2D mesh for the X and Y coordinates using the theta values
theta_grid1, z_grid1 = np.meshgrid(theta, z1)
theta_grid2, z_grid2 = np.meshgrid(theta, z2)

# Parametrize the circular cross-section of both cylinders (X, Y)
X1 = radius1 * np.cos(theta_grid1)
Y1 = radius1 * np.sin(theta_grid1)

X2 = radius2 * np.cos(theta_grid2)
Y2 = radius2 * np.sin(theta_grid2)

# Plot Cylinder 1
ax.plot_surface(X1 + center1[0], Y1 + center1[1], z_grid1, color='b', alpha=0.5)

# Plot Cylinder 2
ax.plot_surface(X2 + center2[0], Y2 + center2[1], z_grid2, color='r', alpha=0.5)

# Set plot limits
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([0, 10])

# Display the plot
plt.title(f"Cylinders Collide: {collision}")
plt.show()
