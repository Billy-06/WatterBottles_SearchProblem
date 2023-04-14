from classes.Problem import Problem
from classes.Node import Node
from classes.Bottle import Bottle

# Define the WaterJug class
class WaterJug(Problem):
    def __init__(self, bottle1, bottle2, bottle3, goal, start=(0, 0)):
        super().__init__(start)
        self.bottle1: Bottle = bottle1
        self.bottle2: Bottle = bottle2
        self.bottle3: Bottle = bottle3
        self.goal = goal

    def actions(self, state):
        actions = []
        if state[0] < self.bottle1:
            actions.append("Fill Bottle 1")
        if state[1] < self.bottle2:
            actions.append("Fill Bottle 2")
        if state[1] < self.bottle3:
            actions.append("Fill Bottle 3")
        if state[0] > 0:
            actions.append("Empty Bottle 1")
        if state[1] > 0:
            actions.append("Empty Bottle 2")
        if state[1] > 0:
            actions.append("Empty Bottle 3")
        if state[0] > 0 and state[1] < self.bottle2:
            actions.append("Pour Jug 1 into Jug 2")
        if state[1] > 0 and state[0] < self.bottle1:
            actions.append("Pour Jug 2 into Jug 1")
        if state[1] > 0 and state[0] < self.bottle1:
            actions.append("Pour Jug 2 into Jug 1")
        return actions

    def result(self, state, action):
        if action == "Fill Jug 1":
            return (self.bottle1, state[1])
        elif action == "Fill Jug 2":
            return (state[0], self.bottle2)
        elif action == "Empty Jug 1":
            return (0, state[1])
        elif action == "Empty Jug 2":
            return (state[0], 0)
        elif action == "Pour Jug 1 into Jug 2":
            if state[0] + state[1] <= self.bottle2:
                return (0, state[0] + state[1])
            else:
                return (state[0] - (self.bottle2 - state[1]), self.bottle2)
        elif action == "Pour Jug 2 into Jug 1":
            if state[0] + state[1] <= self.bottle1:
                return (state[0] + state[1], 0)
            else:
                return (self.bottle1, state[1] - (self.bottle1 - state[0]))

    def goal_test(self, state):
        return state == self.goal

    def h(self, node: Node):
        return max(self.goal[0] - node.state[0], self.goal[1] - node.state[1])
