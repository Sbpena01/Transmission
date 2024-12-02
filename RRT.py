import numpy as np
import random
from Mainshaft import Mainshaft
from Transmission import Transmission
from Node import Node
import matplotlib.pyplot as plt
import copy

class RRT:
    def __init__(self, mainshaft: Mainshaft, transmission: Transmission, goal: Node, max_iterations=5000,goal_bias=0.5,
                 max_sampling_attempts = 20, dt=0.25):
        self.mainshaft = mainshaft
        self.transmission = transmission
        self.goal = goal
        self.max_iterations = max_iterations
        self.max_sampling_attempts = max_sampling_attempts
        self.goal_bias = goal_bias
        self.dt = dt

        self.position_bound = 200
        self.orientation_bound = np.pi/3

        self.start_tree = [Node(self.mainshaft.state)]
        self.goal_tree = [self.goal]

    def getRandomState(self):
        result = True
        num_attempts = 0
        rand = Mainshaft(0, 0, 0, 0, 0, 0)
        while result and num_attempts < self.max_sampling_attempts:
            random_state = np.array([
                [random.randint(-self.position_bound, self.position_bound)],
                [random.randint(-self.position_bound, self.position_bound)],
                [random.randint(-self.position_bound, self.position_bound)],
                [random.uniform(-self.orientation_bound, self.orientation_bound)],
                [random.uniform(-self.orientation_bound, self.orientation_bound)],
                [random.uniform(-self.orientation_bound, self.orientation_bound)],
                [0],
                [0],
                [0],
                [0],
                [0],
                [0],
            ])
            rand.state=random_state
            result = rand.checkCollision(self.transmission)
            num_attempts += 1
        if not result:
            return Node(random_state)
    
    def calculateDistance(self, node1: Node, node2: Node):
        position_diff = np.linalg.norm(node1.state[:3] - node2.state[:3])
        return position_diff

    def getClosestNode(self, random_node: Node, tree):
        distances = [self.calculateDistance(random_node, node) for node in tree]
        return tree[np.argmin(distances)]

    def goTo(self, from_node: Node, to_node: Node):
        # As previously, update `state` progressively towards the goal
        state_diff = to_node.state - from_node.state
        temp = Mainshaft(from_node.state[0].item(), from_node.state[1].item(), from_node.state[2].item(),
                        from_node.state[3].item(), from_node.state[4].item(), from_node.state[5].item())
        temp.setLinearVelocity((state_diff[0], state_diff[1], state_diff[2]))
        temp.setAngularVelocity((state_diff[3], state_diff[4], state_diff[5]))

        current = from_node
        for _ in range(200):
            temp.step(self.dt)
            collision = temp.checkCollision(self.transmission)
            if collision:
                return current
            else:
                current.state = temp.state
                state_diff = to_node.state - current.state
                temp.setLinearVelocity((state_diff[0], state_diff[1], state_diff[2]))
                temp.setAngularVelocity((state_diff[3], state_diff[4], state_diff[5]))
        return current

    def plan(self):
        running = True
        num_iterations = 0
        max_connection_distance = 100
        path = None
        while running and num_iterations < self.max_iterations:
            num_iterations += 1
            print(num_iterations)
            # Run 'coin toss' to determine what node to explore: the goal or a randomly generated node
            coin_toss = random.uniform(0, 1)
            if coin_toss <= self.goal_bias:
                tree = 'goal'
                tree_to_extend = self.goal_tree
            else:
                tree = 'start'
                tree_to_extend = self.start_tree
            random_node = self.getRandomState()
            if random_node is None:
                continue
            # print(random_node)
            # Get nearest node
            nearest_node = self.getClosestNode(random_node, tree_to_extend)
            parent = copy.copy(nearest_node)  # Dude idk why I need this but nearest_node will create a ton of parents and I am unsure why
            new_node = self.goTo(nearest_node, random_node)
            new_node.setParent(parent)
            tree_to_extend.append(new_node)
            # Check connection distance
            if tree == 'goal':
                closest_node = self.getClosestNode(new_node, self.start_tree)
            if tree == 'start':
                closest_node = self.getClosestNode(new_node, self.goal_tree)
            distance_between_trees = self.calculateDistance(new_node, closest_node)
            if distance_between_trees <= max_connection_distance:
                print("WE CAN CONNECT THE TREES")
                path = self.createConnectedPath(closest_node, new_node)
        print(len(self.start_tree), len(self.goal_tree))
        return path

    def createConnectedPath(self, node1:Node, node2: Node):
        node1_path = []
        current = node1
        while current.parent is not None:
            node1_path.append(current)
            current = current.parent
        node2_path = []
        current = node2
        while current.parent is not None:
            node2_path.append(current)
            current = current.parent
        node2_path.reverse()
        return node1_path + node2_path


    def plotPath(self, ax: plt.Axes):
        goal_node = self.goal_tree.pop()
        start_node = self.start_tree.pop()
        while goal_node.parent is not None:
            ax.scatter(goal_node.state[0], goal_node.state[1], goal_node.state[2], color='r', s=5)
            goal_node = goal_node.parent
        while start_node.parent is not None:
            ax.scatter(start_node.state[0], start_node.state[1], start_node.state[2], color='r', s=5)
            start_node = start_node.parent

