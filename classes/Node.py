"""

Description of the Node class
-----------------------------

The __init__ method initializes a node object with the given state, which is a tuple 
containing the current amount of water in each bottle, parent node, action taken to 
reach the current state, and path_cost, which is the cost to reach this node from the 
start node. If the node has a parent, the depth of the node is set as the depth of its 
parent plus 1.

The __lt__ method compares two nodes by their path_cost. This method is used by search 
algorithms to decide which node to expand next.

The __eq__ method compares two nodes by their state. This method is used to check 
whether a node has already been explored and whether the current state matches the 
goal state.

The __getitem__ method allows accessing the bottle objects within the state by index.

The __hash__ method returns a hash of the node's state. This method is used to store 
nodes in a hash table, making it faster to check whether a node has been explored before.

The __iter__ method makes the node iterable, allowing for iterating over the bottles 
in the state.

The expand method takes a problem object as an argument and returns a list of child 
nodes that can be reached from the current node.

The child_node method takes a problem object and an action as arguments and returns a 
new child node obtained by applying the action to the current node.

The solution method returns a list of actions taken to reach the current node from the 
start node.

The path method returns a list of nodes from the start node to the current node, allowing 
for tracing the path taken to reach the current node.

"""

from typing import List, Tuple, Union
from classes.Problem import *

# Define a Node class
# - A node is a state and a pointer to the parent node
# - The root node has no parent
class Node:
    # Initialize the node with the given state
    # - The state is a tuple of bottle objects
    # - The parent is the parent node containing the previous state
    # - The action is the action taken to reach the current state from the parent state
    # - The path_cost is the cost to reach the current state from the start state
    def __init__(self, state, parent=None, action=None, path_cost=0):
        # state is a tuple of bottle objects
        self.state: Tuple = state
        self.parent = parent
        self.action: List = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __len__(self) -> int:
        return len(self.state)

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

    def expand(self, problem: Problem) -> List[object]:
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


"""

Description of the QueueFrontier class
--------------------------------------

QueueFrontier is a data structure used to keep track of nodes during a search process. 
The class represents a queue, which is a first-in-first-out (FIFO) data structure.

The __init__ method initializes an empty list self.frontier which will be used as the 
queue.

The add method takes a Node object and appends it to the end of the list self.frontier, 
representing the back of the queue.

The contains_state method takes a state as an argument and returns True if there is a 
node in the queue with that state, otherwise False. This is achieved by iterating through 
the frontier list and checking if the state of each node in the list is equal to the 
provided state.

The empty method returns True if the frontier list is empty, otherwise False.

The remove method removes and returns the first node in the queue (i.e., the node at the 
front of the list). If the queue is empty, an exception is raised.

"""

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



"""

Description of the StackFrontier class (Extends QueueFrontier)
--------------------------------------------------------------

StackFrontier is a data structure used to keep track of nodes during a search process.
The class represents a stack, which is a last-in-first-out (LIFO) data structure.

The __init__ method initializes an empty list self.frontier which will be used as the
stack.

The add method takes a Node object and appends it to the end of the list self.frontier,
representing the top of the stack.

The contains_state method takes a state as an argument and returns True if there is a
node in the stack with that state, otherwise False. This is achieved by iterating through
the frontier list and checking if the state of each node in the list is equal to the
provided state.

The empty method returns True if the frontier list is empty, otherwise False.

The remove method removes and returns the last node in the stack (i.e., the node at the
top of the list). If the stack is empty, an exception is raised.

"""
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


"""

Description of the PriorityQueueFrontier class (Extends QueueFrontier)
----------------------------------------------------------------------

PriorityQueueFrontier is a data structure used to keep track of nodes during a search
process. The class represents a priority queue, which is a queue in which each element
has a priority associated with it. In this case, the priority of each node is its path
cost.

The __init__ method initializes an empty list self.frontier which will be used as the
priority queue.

The add method takes a Node object and inserts it into the list self.frontier in order
of increasing path cost. If two nodes have the same path cost, the node that was added
first is placed first in the list.

The contains_state method takes a state as an argument and returns True if there is a
node in the priority queue with that state, otherwise False. This is achieved by iterating
through the frontier list and checking if the state of each node in the list is equal to
the provided state.

The empty method returns True if the frontier list is empty, otherwise False.

The remove method removes and returns the first node in the priority queue (i.e., the
node at the front of the list). If the priority queue is empty, an exception is raised.

"""

# Define a PriorityQueueFrontier class
# - A frontier is a priority queue of nodes
# - The priority queue is implemented using a Python list
# - The priority queue is ordered by the node's path_cost
# - The priority queue is FIFO when two nodes have the same path_cost
class PriorityQueueFrontier(QueueFrontier):
    def add(self, node: Node, priority: int):
        self.frontier.append((priority, node))

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier.pop(0)
            return node


