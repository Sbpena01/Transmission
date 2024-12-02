import numpy as np
class RRT:
    def __init__(self, start, goal, max_iterations=1000, step_size=0.1, goal_bias=0.5):
        self.start = start
        self.goal = goal
        self.max_iterations = max_iterations
        self.step_size = step_size
        self.goal_bias = goal_bias

        self.position_bound = 1000
        self.orientation_bound = np.pi/3