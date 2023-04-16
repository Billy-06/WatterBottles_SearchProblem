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
        print("Breadth First Search Goal state reached:")
        print("=====================================================")
        print(node.state)
        return node
    
    # The frontier is a queue that contains the nodes that have been discovered but not yet explored
    # The frontier is initialized with the initial node
    frontier: QueueFrontier = QueueFrontier()
    frontier.add(node)
    # The explored set contains the states that have been explored
    explored = set()

    # The loop continues until the frontier is empty
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        # The actions function returns the set of all possible actions that can be performed
        # on the bottles at a given state
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            print(child.state)
            # The child node is added to the frontier if it has not been explored or discovered
            # The child node is returned if it is the goal state
            # The child node contains three bottles, check that bottles with similar current volume
            # have not been explored or discovered
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child)
            # If the child node has been discovered but not explored, check if the child node
            # has a lower depth than the node in the frontier
            elif frontier.contains_state(child.state):
                for i in frontier.frontier:
                    if i.state == child.state:
                        if i.depth > child.depth:
                            frontier.add(child)
                            break
                        else:
                            break

            # if child.state

    return None


# 2. Using Depth First Search
def depth_first_search(problem: Problem) -> None:
    node: Node = Node(problem.initial)
    if problem.goal_test(node.state):
        print("Depth First Search Goal state reached:")
        print("=====================================================")
        print(node.state)
        return node
    
    # The frontier is a stack that contains the nodes that have been discovered but not yet explored
    frontier: StackFrontier = StackFrontier()
    frontier.add(node)
    # The explored set contains the states that have been explored
    explored = set()

    print("Before the loop")
    # The loop continues until the frontier is empty
    while True:
        print("in the loop")
        if frontier.empty():
            print("Frontier is empty")
            return None
        node = frontier.remove()
        explored.add(node.state)
        print(child.state)
        # The actions function returns the set of all possible actions that can be performed
        # on the bottles at a given state
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            print(child.state)
            # The child node is added to the frontier if it has not been explored or discovered
            # The child node is returned if it is the goal state
            # The child node contains three bottles, check that bottles with similar current volume
            # have not been explored or discovered
            if child.state not in explored and not frontier.contains_state(child.state):
                if problem.goal_test(child.state):
                    return child
                frontier.add(child)
            # If the child node has been discovered but not explored, check if the child node
            # has a lower depth than the node in the frontier
            elif frontier.contains_state(child.state):
                for i in frontier.frontier:
                    if i.state == child.state:
                        if i.depth > child.depth:
                            frontier.add(child)
                            break
                        else:
                            break

            # if child.state

    return None


# 3. Using Greedy Best First Search
def greedy_best_first_search(problem: Problem, h=None) -> None:
    node: Node = Node(problem.initial)
    if problem.goal_test(node.state):
        print("Greedy Best First Search Goal state reached")
        print("=====================================================")
        print(node.state)
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
                frontier.add(child, h(child.state))
            elif frontier.contains_state(child.state) and frontier.get_priority(child.state) > h(child.state):
                frontier.add(child, h(child.state))

    return None


# 4. Using A* Search
def a_star_search(problem: Problem, h=None) -> None:
    node: Node = Node(problem.initial)
    if problem.goal_test(node.state):
        print("A* Search Goal state reached:")
        print(node.state)
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
        print("Depth Limited Search Goal state reached:")
        print("=====================================================")
        print(node.state)
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
        print("Recursive Best First Search Goal state reached:")
        print("=====================================================")
        print(node.state)
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
    bottle3 = Bottle(6)
    bottle3.current = 0
    bottle2 = Bottle(5)
    bottle2.current = 0
    caseOne: Node = Node((bottle1, bottle2, bottle3))
    caseOneEnd: Tuple = ( 0, 5, 5 )

    bottle4 = Bottle(10)
    bottle4.current = 3
    bottle5 = Bottle(6)
    bottle5.current = 0
    bottle6 = Bottle(5)
    bottle6.current = 0
    caseTwo: Node = Node((bottle4, bottle5, bottle6))
    caseTwoEnd = (0, 1, 5)

    bottle7 = Bottle(10)
    bottle7.current = 2
    bottle8 = Bottle(6)
    bottle8.current = 0
    bottle9 = Bottle(5)
    bottle9.current = 2
    caseThree: Node = Node((bottle7, bottle8, bottle9))
    caseThreeEnd = (9, 0, 0)



    # Visualize the search algorithms
    print()
    # Create the problem
    print("Visualizing Breadth First Search:")
    problem = WaterBottleProblem(caseOne, caseOneEnd)
    problem2 = WaterBottleProblem(caseTwo, caseTwoEnd)
    problem3 = WaterBottleProblem(caseThree, caseThreeEnd)
    print("Case 1: Start")
    breadth_first_search(problem)
    # print("Case 2: Start")
    # breadth_first_search(problem2)
    # print("Case 3: Start")
    # breadth_first_search(problem3)


    
    
    print()
    print("Visualizing Depth First Search:")
    # Create the problem
    problem = WaterBottleProblem(caseOne, caseOneEnd)
    problem2 = WaterBottleProblem(caseTwo, caseTwoEnd)
    problem3 = WaterBottleProblem(caseThree, caseThreeEnd)
    print("Case 1: Start")
    depth_first_search(problem)
    # print("Case 2: Start")
    # depth_first_search(problem2)
    # print("Case 3: Start")
    # depth_first_search(problem3)

    print()
    print("Visualizing Greedy Best First Search:")
    problem = WaterBottleProblem(caseOne, caseOneEnd)
    problem2 = WaterBottleProblem(caseTwo, caseTwoEnd)
    problem3 = WaterBottleProblem(caseThree, caseThreeEnd)
    print("Case 1: Start")
    greedy_best_first_search(problem, h=problem.h)
    # print("Case 2: Start")
    # greedy_best_first_search(problem2, h=problem2.h)
    # print("Case 3: Start")
    # greedy_best_first_search(problem3, h=problem3.h)

    print()
    print("Visualizing A* Search:")
    problem = WaterBottleProblem(caseOne, caseOneEnd)
    problem2 = WaterBottleProblem(caseTwo, caseTwoEnd)
    problem3 = WaterBottleProblem(caseThree, caseThreeEnd)
    print("Case 1: Start")
    a_star_search(problem, h=problem.h)
    # print("Case 2: Start")
    # a_star_search(problem2, h=problem2.h)
    # print("Case 3: Start")
    # a_star_search(problem3, h=problem3.h)


    print()
    print("Visualizing Iterative Deepening Search:")
    iterative_deepening_search(problem)

    print()
    print("Visualizing Recursive Best First Search:")
    recursive_best_first_search(problem, h=problem.h)


# Test out the different search algorithms
if __name__ == "__main__":
    main()
