import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

from Cylinder import Cylinder
from Mainshaft import Mainshaft

# Parameters
radius = 1
height = 3
center = (1, 1, 1)  # Set the center of the cylinder
rotation_axis = 'y'  # Rotate around the z-axis
num_frames = 100  # Number of frames in the animation

# Create cylinder geometry
my_cylinder = Cylinder(center, radius, height)

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
angle = np.deg2rad(0)
    
# Rotate the cylinder
# X_rot, Y_rot, Z_rot = rotate_points(X, Y, Z, angle, rotation_axis)
my_cylinder.rotate(angle, rotation_axis)

# Translate the cylinder to the desired center
# cylinder.X += center[0]
# cylinder.Y += center[1]
# cylinder.Z += center[2]

# Plot the rotated cylinder
ax.plot_surface(my_cylinder.X, my_cylinder.Y, my_cylinder.Z, color='b', alpha=0.6)

# Set labels and axes limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-2, 5)
ax.set_ylim(-2, 5)
ax.set_zlim(-2, 2)


# Show the animation
plt.show()
