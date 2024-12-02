import numpy as np
import random
from Mainshaft import Mainshaft
from Transmission import Transmission
class RRT:
    def __init__(self, mainshaft: Mainshaft, transmission: Transmission, start, goal, max_iterations=1000, step_size=0.1, goal_bias=0.5):
        self.mainshaft = mainshaft
        self.transmission = transmission
        self.start = start
        self.goal = goal
        self.max_iterations = max_iterations
        self.step_size = step_size
        self.goal_bias = goal_bias

        self.position_bound = 600
        self.orientation_bound = np.pi/3

    def getRandomState(self):
        random_state = np.array([
            [random.randint(-self.position_bound, self.position_bound)],
            [random.randint(-self.position_bound, self.position_bound)],
            [random.randint(-self.position_bound, self.position_bound)],
            [random.randint(-self.orientation_bound, self.orientation_bound)],
            [random.randint(-self.orientation_bound, self.orientation_bound)],
            [random.randint(-self.orientation_bound, self.orientation_bound)],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
        ])
        rand = Mainshaft(0, 0, 0, 0, 0, 0)
        rand.state=random_state
    
    def plan(self):
        pass
    
