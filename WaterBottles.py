"""
You have three water bottles. 

Bottle #1 (b1) can be filled with 10 litres, 
Bottle #2 (b2) with 6 litres, 
Bottle #3 (b3) with 5 litres of water respectively. 

There are no markings on the bottles so you cannot measure them if 
the bottles are filled less than their maximum capacity. Assuming that you 
have an UNLIMITED SUPPLY OF WATER, by filling or emptying these three 
bottles: 
    (i)   How would you get from the start state to the end state? 
    (ii)  What is the solution with the fewest steps? 

    
The code should be able to solve this problem for the following parameters: 

a)  Start: b1 = 10, b2 = 0, b3 = 0 
    End: b1 = 0, b2 = 5, b3 = 5 
 
b)  Start: b1 = 3, b2 = 0, b3 = 0 
    End: b1 = 0, b2 = 1, b3 = 0 

c)  Start: b1 = 2, b2 = 0, b3 = 2 
    End: b1 = 9, b2 = 0, b3 = 0 
 
b) Repeat (c) but now change the maximum of the bottles [(i) b1: 11, b2: 1 b3: 3].  

"""
from Problem import Problem
from Node import *
from Bottle import Bottle

import pydot
from IPython.display import Image, display


class WaterBottleProblem(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def actions(self, state):
        actions = []
        for bottle in state:
            if bottle.current_capacity < bottle.max_capacity:
                actions.append(("fill", bottle))
            if bottle.current_capacity > 0:
                actions.append(("empty", bottle))
            for other_bottle in state:
                if bottle != other_bottle:
                    if bottle.current_capacity > 0 and other_bottle.current_capacity < other_bottle.max_capacity:
                        actions.append(("pour", bottle, other_bottle))
        return actions

    def result(self, state, action):
        if action[0] == "fill":
            bottle = action[1]
            bottle.fill(bottle.max_capacity - bottle.current_capacity)
        elif action[0] == "empty":
            bottle = action[1]
            bottle.current_capacity = 0
        elif action[0] == "pour":
            bottle = action[1]
            other_bottle = action[2]
            other_bottle.fill(bottle.current_capacity)
            bottle.current_capacity = 0
        return state

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self):
        raise NotImplementedError


# 1. Using Breadth First Search
def breadth_first_search(problem: Problem) -> None:
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = QueueFrontier()
    frontier.add(node)
    explored = set()
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child)

    return None


# 2. Using Depth First Search
def depth_first_search(problem: Problem) -> None:
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = StackFrontier()
    frontier.add(node)
    explored = set()
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child)

    return None


# 3. Using Greedy Best First Search
def greedy_best_first_search(problem: Problem, h=None) -> None:
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueueFrontier()
    frontier.add(node, h(node.state))
    explored = set()
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child, h(child.state))
            elif frontier.contains_state(child.state) and frontier.get_priority(child.state) > h(child.state):
                frontier.add(child, h(child.state))

    return None


# 4. Using A* Search
def a_star_search(problem: Problem, h=None) -> None:
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueueFrontier()
    frontier.add(node, h(node.state))
    explored = set()
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child, h(child.state) + child.path_cost)
            elif frontier.contains_state(child.state) and frontier.get_priority(child.state) > h(child.state) + child.path_cost:
                frontier.add(child, h(child.state) + child.path_cost)

    return None


# 5. Using Iterative Deepening Search
def depth_limited_search(problem: Problem, limit: int) -> None:
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = StackFrontier()
    frontier.add(node)
    explored = set()
    while True:
        if frontier.empty():
            return "cutoff"
        node = frontier.remove()
        explored.add(node.state)
        if node.depth == limit:
            return "cutoff"
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child)

    return None


def iterative_deepening_search(problem: Problem) -> None:
    for depth in range(100):
        result = depth_limited_search(problem, depth)
        if result != "cutoff":
            return result


# 6. Using Recursive Best First Search
def recursive_best_first_search(problem: Problem, h=None) -> None:
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueueFrontier()
    frontier.add(node, h(node.state))
    explored = set()
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child, h(child.state))
            elif frontier.contains_state(child.state) and frontier.get_priority(child.state) > h(child.state):
                frontier.add(child, h(child.state))

    return None

# Define the Graph class


class Graph:
    def __init__(self, title, engine="dot"):
        self.title = title
        self.engine = engine
        self.graph = pydot.Dot(graph_type="digraph", label=title,
                               labelloc="t", fontsize="20", fontcolor="blue")

    def attr(self, name, value):
        self.graph.set(name, value)

    def node(self, name):
        self.graph.add_node(pydot.Node(name))

    def edge(self, source, target, label=None):
        self.graph.add_edge(pydot.Edge(source, target, label=label))

    def render(self, filename, view=False):
        self.graph.write(filename, format="png")
        if view:
            self.graph.write_png(filename)


# Define the WaterJug class
class WaterJug(Problem):
    def __init__(self, jug1, jug2, goal, start=(0, 0)):
        super().__init__(start)
        self.jug1 = jug1
        self.jug2 = jug2
        self.goal = goal

    def actions(self, state):
        actions = []
        if state[0] < self.jug1:
            actions.append("Fill Jug 1")
        if state[1] < self.jug2:
            actions.append("Fill Jug 2")
        if state[0] > 0:
            actions.append("Empty Jug 1")
        if state[1] > 0:
            actions.append("Empty Jug 2")
        if state[0] > 0 and state[1] < self.jug2:
            actions.append("Pour Jug 1 into Jug 2")
        if state[1] > 0 and state[0] < self.jug1:
            actions.append("Pour Jug 2 into Jug 1")
        return actions

    def result(self, state, action):
        if action == "Fill Jug 1":
            return (self.jug1, state[1])
        elif action == "Fill Jug 2":
            return (state[0], self.jug2)
        elif action == "Empty Jug 1":
            return (0, state[1])
        elif action == "Empty Jug 2":
            return (state[0], 0)
        elif action == "Pour Jug 1 into Jug 2":
            if state[0] + state[1] <= self.jug2:
                return (0, state[0] + state[1])
            else:
                return (state[0] - (self.jug2 - state[1]), self.jug2)
        elif action == "Pour Jug 2 into Jug 1":
            if state[0] + state[1] <= self.jug1:
                return (state[0] + state[1], 0)
            else:
                return (self.jug1, state[1] - (self.jug1 - state[0]))

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        return max(self.goal[0] - node.state[0], self.goal[1] - node.state[1])


# Visualisation of the search algorithms
def visualize_search(problem, node, title):
    # Create the graph
    graph = Graph(title=title, engine="neato")
    graph.attr("node", shape="circle")

    # Add the initial state
    graph.node(problem.initial)

    # Add the frontier
    frontier = QueueFrontier()
    frontier.add(node)
    while not frontier.empty():
        node = frontier.remove()
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if not frontier.contains_state(child.state):
                frontier.add(child)
                graph.edge(node.state, child.state, label=action)

    # Add the explored set
    explored = set()
    while not frontier.empty():
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                frontier.add(child)
                graph.edge(node.state, child.state, label=action)

    # Visualize the graph
    graph.view()


def main():
    # Create the bottles
    bottle1 = Bottle(10)
    bottle2 = Bottle(6)
    bottle3 = Bottle(5)

    # Create the problem
    problem = WaterBottleProblem(bottle1, bottle2, bottle3)

    # Test out the different search algorithms
    print("Breadth First Search:")
    solution = breadth_first_search(problem)
    print(solution.solution())
    print("Depth First Search:")
    solution = depth_first_search(problem)
    print(solution.solution())
    print("Greedy Best First Search:")
    solution = greedy_best_first_search(problem, h=problem.h)
    print(solution.solution())
    print("A* Search:")
    solution = a_star_search(problem, h=problem.h)
    print(solution.solution())
    print("Iterative Deepening Search:")
    solution = iterative_deepening_search(problem)
    print(solution.solution())
    print("Recursive Best First Search:")
    solution = recursive_best_first_search(problem, h=problem.h)
    print(solution.solution())

    # Visualize the search algorithms
    print("Visualizing Breadth First Search:")
    solution = breadth_first_search(problem)
    visualize_search(problem, solution, "Breadth First Search")
    print("Visualizing Depth First Search:")
    solution = depth_first_search(problem)
    visualize_search(problem, solution, "Depth First Search")
    print("Visualizing Greedy Best First Search:")
    solution = greedy_best_first_search(problem, h=problem.h)
    visualize_search(problem, solution, "Greedy Best First Search")
    print("Visualizing A* Search:")
    solution = a_star_search(problem, h=problem.h)
    visualize_search(problem, solution, "A* Search")
    print("Visualizing Iterative Deepening Search:")
    solution = iterative_deepening_search(problem)
    visualize_search(problem, solution, "Iterative Deepening Search")
    print("Visualizing Recursive Best First Search:")
    solution = recursive_best_first_search(problem, h=problem.h)
    visualize_search(problem, solution, "Recursive Best First Search")


# Test out the different search algorithms
if __name__ == "__main__":
    main()
