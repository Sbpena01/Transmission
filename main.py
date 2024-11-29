import matplotlib.pyplot as plt
from Mainshaft import Mainshaft

mainshaft = Mainshaft(0.0, 0.0, 0.0, 0.0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the rotated cylinder
for cylinder in mainshaft.cylinders:
    ax.plot_surface(cylinder.X, cylinder.Y, cylinder.Z, color='b', alpha=1, linewidth=0.1)

# Set labels and axes limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
limit = 400
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)

# Show the animation
plt.show()
