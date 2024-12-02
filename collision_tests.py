import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from itertools import combinations

def create_cuboid(center, size, rotation_matrix):
    """Create a cuboid with center, size (length, width, height), and rotation matrix"""
    # Define the vertices of a cuboid (8 points)
    half_size = np.array(size) / 2
    vertices = np.array([
        [x, y, z] for x in [-half_size[0], half_size[0]]
                    for y in [-half_size[1], half_size[1]]
                    for z in [-half_size[2], half_size[2]]
    ])
    
    # Apply the rotation and translation (center)
    vertices = np.dot(vertices, rotation_matrix.T) + center
    return vertices

def project_onto_axis(vertices, axis):
    """Project the vertices onto the axis and return the min and max projection"""
    projections = np.dot(vertices, axis)
    return np.min(projections), np.max(projections)

def overlap(proj1, proj2):
    """Check if two projections overlap"""
    return not (proj1[1] < proj2[0] or proj2[1] < proj1[0])

def cross_product(a, b):
    """Compute the cross product of two vectors"""
    return np.cross(a, b)

def check_collision(cuboid1, cuboid2):
    """Check if two cuboids are colliding using the Separating Axis Theorem"""
    # Get all edges of the cuboids
    edges1 = [
        cuboid1[1] - cuboid1[0], 
        cuboid1[2] - cuboid1[0], 
        cuboid1[4] - cuboid1[0], 
        cuboid1[3] - cuboid1[0], 
        cuboid1[5] - cuboid1[0], 
        cuboid1[6] - cuboid1[0]
    ]
    edges2 = [
        cuboid2[1] - cuboid2[0], 
        cuboid2[2] - cuboid2[0], 
        cuboid2[4] - cuboid2[0], 
        cuboid2[3] - cuboid2[0], 
        cuboid2[5] - cuboid2[0], 
        cuboid2[6] - cuboid2[0]
    ]
    
    # List of axes to test (all axes of cuboid1, cuboid2 and cross products of edges)
    axes = [
        [1,0,0],[0,1,0],[0,0,1],
        [-1,0,0],[0,-1,0],[0,0,-1]
    ] + [
        cross_product(edges1[i], edges2[j]) 
        for i in range(3) for j in range(3)
    ]
    
    # Check overlap projections for all axes
    for axis in axes:
        proj1 = project_onto_axis(cuboid1, axis)
        proj2 = project_onto_axis(cuboid2, axis)
        if not overlap(proj1, proj2):
            return False  # There is no overlap along this axis, so no collision
    
    return True  # If no separating axis was found, the cuboids are colliding


# Visualization and setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

center1 = np.array([0, 0, 0])
size1 = np.array([2, 2, 2])
rotation_matrix1 = np.eye(3)  # No rotation for simplicity

center2 = np.array([3, 3, 3])
size2 = np.array([2, 2, 2])
rotation_matrix2 = np.eye(3)  # No rotation for simplicity

# Generate the cuboids
cuboid1 = create_cuboid(center1, size1, rotation_matrix1)
cuboid2 = create_cuboid(center2, size2, rotation_matrix2)

# Check if cuboids are colliding
collision = check_collision(cuboid1, cuboid2)
collision_text = "Colliding!" if collision else "Not Colliding!"

# Plot cuboids
ax.scatter(cuboid1[:, 0], cuboid1[:, 1], cuboid1[:, 2], color="b")
ax.scatter(cuboid2[:, 0], cuboid2[:, 1], cuboid2[:, 2], color="r")

verts1 = [[cuboid1[i] for i in [0, 1, 5, 4]], [cuboid1[i] for i in [0, 3, 7, 4]], [cuboid1[i] for i in [0, 1, 3, 2]], [cuboid1[i] for i in [6, 7, 3, 2]]]
verts2 = [[cuboid2[i] for i in [0, 1, 5, 4]], [cuboid2[i] for i in [0, 3, 7, 4]], [cuboid2[i] for i in [0, 1, 3, 2]], [cuboid2[i] for i in [6, 7, 3, 2]]]
ax.add_collection3d(Poly3DCollection(verts1, color="b", linewidths=1, edgecolors="r", alpha=0.25))
ax.add_collection3d(Poly3DCollection(verts2, color="r", linewidths=1, edgecolors="b", alpha=0.25))

# Title
ax.set_title(f"Collision Check: {collision_text}")

plt.show()
