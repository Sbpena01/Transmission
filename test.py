from Rectangle import Rectangle
from Cylinder import Cylinder
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cylin1 = Cylinder([0.0, 0.0, 0.0], 2.0, 4.0)
cylin2 = Cylinder([0.0, 0.0, 10.0], 4.0, 1.0)

ax.plot_surface(cylin1.X, cylin1.Y, cylin1.Z, color='b', alpha=0.5, linewidth=1)
cylin1.bounding_box.plot(ax, edge_color='gray')

ax.plot_surface(cylin2.X, cylin2.Y, cylin2.Z, color='r', alpha=0.5, linewidth=1)
cylin2.bounding_box.plot(ax, edge_color='gray')

result = cylin2.bounding_box.checkCollision(cylin1.bounding_box)
print(result)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
limit = 10
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)
plt.show()