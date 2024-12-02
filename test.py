from Rectangle import Rectangle
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

rect1 = Rectangle(3.0, 3.0, 7.0)
rect1.plot(ax)

rect2 = Rectangle(3.0, 4.0, 1.0, center=(5.0, 0.0, 0.0))
rect2.plot(ax)

result = rect1.checkCollision(rect2)
print(result)

print(rect1.edges)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
limit = 10
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)
plt.show()