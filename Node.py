import numpy as np
class Node:
    def __init__(self, state: np.array, parent=None):
        self.state: np.array = state
        self.parent: 'Node' = parent
    
    def __str__(self):
        return (f"Position: {self.state[0].item()}, {self.state[1].item()}, {self.state[2].item()}. "
               f"Orientation: {self.state[3].item()}, {self.state[4].item()}, {self.state[5].item()}")

    def setParent(self, node: 'Node'):
        self.parent = node