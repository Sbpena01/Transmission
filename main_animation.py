import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from Mainshaft import Mainshaft

# Create mainshaft object
mainshaft = Mainshaft(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
mainshaft.setAngularVelocity((np.pi/10, 0, np.pi / 6))  # Set angular velocity (rotation speed)
# mainshaft.setLinearVelocity((0, 0, 20))  # Optional: Set linear velocity if needed

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Animation update function
def update(frame):
    ax.cla()  # Clear the current axes to redraw
    mainshaft.step(1.0)  # Advance the simulation by one time step
    mainshaft.plot(ax)  # Plot the updated mainshaft

    # Set labels and axes limits (you can keep these fixed)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    limit = 400
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_zlim(-limit, limit)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=500)

# Show the animation
plt.show()
