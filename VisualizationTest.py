import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from Cylinder import Cylinder  # Assuming you have a Cylinder class

# Parameters
radius = 1
height = 3
center = (0, 0, 0)  # Set the center of the cylinder
rotation_axis = 'y'  # Rotate around the y-axis
num_frames = 100  # Number of frames in the animation

# Create cylinder geometry
my_cylinder = Cylinder(center, radius, height)

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to update the rotation angle and redrawing the plot
def update(frame):
    ax.cla()  # Clear the current axes
    angle = np.deg2rad(10)  # Update the rotation angle
    my_cylinder.rotate(angle, rotation_axis, point=(2,0,1))  # Rotate the cylinder
    ax.plot_surface(my_cylinder.X, my_cylinder.Y, my_cylinder.Z, color='b', alpha=0.6)
    
    # Set labels and axes limits
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-2, 5)
    ax.set_ylim(-2, 5)
    ax.set_zlim(-2, 2)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
