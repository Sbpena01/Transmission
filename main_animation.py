import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from Part import Part
from Cylinder import Cylinder

# Create mainshaft object
part = Part(0.0, 0.0, 2.5, 0.0, 0.0, 0.0)
cylinder = Cylinder([0.0, 0.0, 2.5], 2.0, 4.0)
part.cylinders.append(cylinder)
# part.setAngularVelocity((0.0, np.pi/6, np.pi/2))
part.setLinearVelocity((0.0, 1.0, 0.0))

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Animation update function
def update(frame):
    ax.cla()  # Clear the current axes to redraw=
    part.plot(ax, show_bounding_boxes=True)
    print(part.cylinders[0].bounding_box.vertices)
    part.step(1.0)
    # Set labels and axes limits (you can keep these fixed)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    limit = 10
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_zlim(-limit, limit)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=500)

# Show the animation
plt.show()
