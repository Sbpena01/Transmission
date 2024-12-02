import matplotlib.pyplot as plt
from Mainshaft import Mainshaft
from Transmission import Transmission
from Rectangle import Rectangle
from Cylinder import Cylinder
import numpy as np

mainshaft = Mainshaft(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
mainshaft.setLinearVelocity((0, 0, 200))
mainshaft.setAngularVelocity((0, np.pi/3, np.pi/4))
mainshaft.step(1.0)

transmission = Transmission()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Visualize
# transmission.plot(ax)
mainshaft.plot(ax, show_bounding_boxes=True)
# print(mainshaft.cylinders[0].bounding_box.edges)

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
