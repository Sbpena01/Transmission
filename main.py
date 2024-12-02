import matplotlib.pyplot as plt
from Mainshaft import Mainshaft
from Transmission import Transmission
from Node import Node
from RRT import RRT
import numpy as np


mainshaft = Mainshaft(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
# mainshaft.setLinearVelocity((0, 100.0, 0))
# mainshaft.setAngularVelocity((0, np.pi/3, np.pi/4))
# mainshaft.step(1.0)

transmission = Transmission()

goal_state = np.array([[0],[400.0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]])
goal_node = Node(goal_state)
rrt = RRT(mainshaft, transmission, goal_node)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Visualize
transmission.plot(ax)
mainshaft.plot(ax, show_bounding_boxes=True)
result = mainshaft.checkCollision(transmission)

rrt_result = rrt.plan()
rrt.plotPath(ax)

# Set labels and axes limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
limit = 600
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)

# Show the animation
plt.show()
