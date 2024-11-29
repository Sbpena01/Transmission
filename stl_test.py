import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Load the STL file
stl_mesh = mesh.Mesh.from_file('primary_shaft.stl')

# Set up the figure and axis for 3D plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a collection of the faces (triangles) using Poly3DCollection
faces = Poly3DCollection(stl_mesh.vectors, facecolors='blue', linewidths=0.5, edgecolors='k', alpha=0.75)

# Add the faces to the plot
ax.add_collection3d(faces)

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Adjust the aspect ratio and limits
ax.auto_scale_xyz(stl_mesh.x, stl_mesh.y, stl_mesh.z)

# Show the plot
plt.show()
