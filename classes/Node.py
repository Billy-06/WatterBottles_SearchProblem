from typing import List, Tuple, Union
from classes.Problem import *
# Define a Node class
# - A node is a state and a pointer to the parent node
# - The root node has no parent
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state: Tuple = state
        self.parent = parent
        self.action: List = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __lt__(self, node: object):
        # Compare nodes by path cost
        return self.path_cost < node.path_cost
    
    def __eq__(self, node: object):
        # Compare nodes by state
        return isinstance(node, Node) and self.state[0].current == node.state[0].current and self.state[1].current == node.state[1].current and self.state[2].current == node.state[2].current
    
    # make bottle accessible by index
    def __getitem__(self, index):
        return self.state[index]
    
    def __hash__(self) -> int:
        return hash(self.state)
    
    # Make the node iterable in order to check every bottle in the state
    def __iter__(self):
        return iter(self.state)

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem: Problem, action) -> object:
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action,
                         problem.path_cost(self.path_cost, self.state,
                                           action, next_state))
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


# Define a QueueFrontier class
# - A frontier is a queue of nodes
# - The queue is implemented using a Python list
# - The queue is FIFO
class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node: Node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return not self.frontier

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier.pop(0)
            return node

# Define a StackFrontier class
# - A frontier is a stack of nodes
# - The stack is implemented using a Python list
# - The stack is LIFO


class StackFrontier(QueueFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier.pop()
            return node


# Define a PriorityQueueFrontier class
# - A frontier is a priority queue of nodes
# - The priority queue is implemented using a Python list
# - The priority queue is ordered by the node's path_cost
# - The priority queue is FIFO when two nodes have the same path_cost
class PriorityQueueFrontier(QueueFrontier):
    def add(self, node: Node):
        for i, other in enumerate(self.frontier):
            if node.path_cost < other.path_cost:
                self.frontier.insert(i, node)
                break
        else:
            self.frontier.append(node)

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier.pop(0)
            return node
