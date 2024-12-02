import numpy as np
class Node:
    def __init__(self, state: np.array, parent=None):
        self.state: np.array = state
        self.parent: 'Node' = parent
    
    def setParent(self, node: 'Node'):
        self.parent = node