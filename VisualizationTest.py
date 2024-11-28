import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

def create_cylinder(radius, height, resolution=100):
    """
    Create a parametric cylinder surface.
    :param radius: radius of the cylinder
    :param height: height of the cylinder
    :param resolution: number of points to discretize the circle
    :return: x, y, z coordinates of the cylinder surface
    """
    theta = np.linspace(0, 2*np.pi, resolution)
    z = np.linspace(-height / 2, height / 2, resolution)
    theta, Z = np.meshgrid(theta, z)
    
    X = radius * np.cos(theta)
    Y = radius * np.sin(theta)
    Z = Z

    return X, Y, Z

def rotate_points(X, Y, Z, angle, axis):
    """
    Rotate the points around a given axis.
    :param X, Y, Z: 3D coordinates of points to rotate
    :param angle: rotation angle in radians
    :param axis: axis of rotation ('x', 'y', or 'z')
    :return: rotated coordinates X_rot, Y_rot, Z_rot
    """
    # Rotation matrix for rotation around x, y, or z axis
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

    # Apply rotation matrix to each point
    points = np.vstack([X.ravel(), Y.ravel(), Z.ravel()])
    rotated_points = np.dot(rotation_matrix, points).T

    # Reshape back to the original shape
    X_rot, Y_rot, Z_rot = rotated_points[:, 0].reshape(X.shape), rotated_points[:, 1].reshape(Y.shape), rotated_points[:, 2].reshape(Z.shape)
    
    return X_rot, Y_rot, Z_rot

def update_plot(frame, X, Y, Z, center, rotation_axis, num_frames, ax):
    """
    Update the plot for each frame of the animation.
    :param frame: current frame number (0 to num_frames-1)
    :param X, Y, Z: Coordinates of the cylinder
    :param center: (x, y, z) tuple to move the cylinder to
    :param rotation_axis: Axis to rotate around ('x', 'y', or 'z')
    :param num_frames: Total number of frames in the animation
    :param ax: 3D axis to plot on
    :return: updated plot
    """
    # Calculate the rotation angle for the current frame
    angle = (frame / (num_frames - 1)) * 2 * np.pi  # Interpolate angle from 0 to 2π
    
    # Rotate the cylinder
    X_rot, Y_rot, Z_rot = rotate_points(X, Y, Z, angle, rotation_axis)
    
    # Translate the cylinder to the desired center
    X_rot += center[0]
    Y_rot += center[1]
    Z_rot += center[2]
    
    # Clear the previous plot
    ax.cla()
    
    # Plot the rotated cylinder
    ax.plot_surface(X_rot, Y_rot, Z_rot, color='b', alpha=0.6)
    
    # Set labels and axes limits
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-2, 5)
    ax.set_ylim(-2, 5)
    ax.set_zlim(-2, 2)
    
    return ax,

# Parameters
radius = 1
height = 3
center = (2, 2, 0)  # Set the center of the cylinder
rotation_axis = 'x'  # Rotate around the z-axis
num_frames = 100  # Number of frames in the animation

# Create cylinder geometry
X, Y, Z = create_cylinder(radius, height)

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the animation
ani = FuncAnimation(fig, update_plot, frames=num_frames, fargs=(X, Y, Z, center, rotation_axis, num_frames, ax), interval=100)

# Show the animation
plt.show()
