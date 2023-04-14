from typing import List, Set, Dict, Tuple, Optional, Callable, Any, Union
from classes.Node import *
from classes.Problem import *
from classes.Graph import *
from classes.Bottle import *
from classes.WaterBottleProblem import *

# 1. Using Breadth First Search
def breadth_first_search(problem: Problem) -> int:
    node: Node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier: QueueFrontier = QueueFrontier()
    frontier.add(node)
    explored = set()
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            print(child.state)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                print(child.state)
                frontier.add(child)

    return None


# 2. Using Depth First Search
def depth_first_search(problem: Problem) -> None:
    node: Node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier: StackFrontier = StackFrontier()
    frontier.add(node)
    explored = set()
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child)

    return None


# 3. Using Greedy Best First Search
def greedy_best_first_search(problem: Problem, h=None) -> None:
    node: Node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier: PriorityQueueFrontier = PriorityQueueFrontier()
    frontier.add(node, h(node.state))
    explored = set()
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child, h(child.state))
            elif frontier.contains_state(child.state) and frontier.get_priority(child.state) > h(child.state):
                frontier.add(child, h(child.state))

    return None


# 4. Using A* Search
def a_star_search(problem: Problem, h=None) -> None:
    node: Node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier :PriorityQueueFrontier = PriorityQueueFrontier()
    frontier.add(node, h(node.state))
    explored = set()
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child, h(child.state) + child.path_cost)
            elif frontier.contains_state(child.state) and frontier.get_priority(child.state) > h(child.state) + child.path_cost:
                frontier.add(child, h(child.state) + child.path_cost)

    return None


# 5. Using Iterative Deepening Search
def depth_limited_search(problem: Problem, limit: int) -> None:
    node: Node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier: StackFrontier = StackFrontier()
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
            child = node.child_node(problem, action)
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
            child = node.child_node(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child, h(child.state))
            elif frontier.contains_state(child.state) and frontier.get_priority(child.state) > h(child.state):
                frontier.add(child, h(child.state))

    return None

# Define the Graph class




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
            child = node.child_node(problem, action)
            if not frontier.contains_state(child.state):
                frontier.add(child)
                graph.edge(node.state, child.state, label=action)

    # Add the explored set
    explored = set()
    while not frontier.empty():
        node = frontier.remove()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            if child.state not in explored and not frontier.contains_state(child.state):
                frontier.add(child)
                graph.edge(node.state, child.state, label=action)

    # Visualize the graph
    graph.view()


def main():
    # Create the bottles
    # Case 1: Start 
    bottle1 = Bottle(10)
    bottle1.current = 10
    bottle2 = Bottle(6)
    bottle2.current = 0
    bottle3 = Bottle(5)
    bottle3.current = 0
    # Case 1: Goal 
    # bottle4 = Bottle(10)
    # bottle4.current = 0
    # bottle5 = Bottle(6)
    # bottle5.current = 5
    # bottle6 = Bottle(5)
    # bottle6.current = 5

    # Case 2
    # bottle4 = Bottle(10)
    # bottle4.current = 10
    # bottle5 = Bottle(6)
    # bottle6 = Bottle(5)
    # bottle7 = Bottle(10)
    # bottle8 = Bottle(6)
    # bottle9 = Bottle(5)
    caseOne: Node = Node((bottle1, bottle2, bottle3))
    caseOneEnd: Tuple = ( 0, 5, 5 )

    caseTwo = (3, 0, 0)
    caseTwoEnd = (0, 1, 5)

    caseThree = (2, 0, 2)
    caseThreeEnd = (9, 0, 0)



    # Create the problem
    problem = WaterBottleProblem(caseOne, caseOneEnd)
    # problem = WaterBottleProblem(caseTwo, caseTwoEnd)
    # problem = WaterBottleProblem(caseThree, caseThreeEnd)

    # Test out the different search algorithms
    # print("Breadth First Search:")
    # solution = breadth_first_search(problem)
    # print(solution.solution())
    # print("Depth First Search:")
    # solution = depth_first_search(problem)
    # print(solution.solution())
    # print("Greedy Best First Search:")
    # solution = greedy_best_first_search(problem, h=problem.h)
    # print(solution.solution())
    # print("A* Search:")
    # solution = a_star_search(problem, h=problem.h)
    # print(solution.solution())
    # print("Iterative Deepening Search:")
    # solution = iterative_deepening_search(problem)
    # print(solution.solution())
    # print("Recursive Best First Search:")
    # solution = recursive_best_first_search(problem, h=problem.h)
    # print(solution.solution())

    # Visualize the search algorithms
    print("Visualizing Breadth First Search:")
    breadth_first_search(problem)
    # solution = breadth_first_search(problem)
    # visualize_search(problem, solution, "Breadth First Search")
    
    print("Visualizing Depth First Search:")
    depth_first_search(problem)
    # solution = depth_first_search(problem)
    # visualize_search(problem, solution, "Depth First Search")
    
    print("Visualizing Greedy Best First Search:")
    greedy_best_first_search(problem, h=problem.h)
    # visualize_search(problem, solution, "Greedy Best First Search")
    # solution = greedy_best_first_search(problem, h=problem.h)
    # visualize_search(problem, solution, "Greedy Best First Search")
    
    print("Visualizing A* Search:")
    a_star_search(problem, h=problem.h)
    # visualize_search(problem, solution, "A* Search")
    # solution = a_star_search(problem, h=problem.h)
    # visualize_search(problem, solution, "A* Search")
    print("Visualizing Iterative Deepening Search:")
    iterative_deepening_search(problem)
    # visualize_search(problem, solution, "Iterative Deepening Search")
    # solution = iterative_deepening_search(problem)
    # visualize_search(problem, solution, "Iterative Deepening Search")
    print("Visualizing Recursive Best First Search:")
    recursive_best_first_search(problem, h=problem.h)
    # visualize_search(problem, solution, "Recursive Best First Search")
    # solution = recursive_best_first_search(problem, h=problem.h)
    # visualize_search(problem, solution, "Recursive Best First Search")


# Test out the different search algorithms
if __name__ == "__main__":
    main()
