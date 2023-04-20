from typing import List, Set, Dict, Tuple, Optional, Callable, Any, Union
from classes.Node import *
from classes.Problem import *
from classes.Graph import *
from classes.Bottle import *
from classes.WaterBottleProblem import *
from tkinter import *

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
            if child not in explored and not frontier.contains_state(child):
                if problem.goal_test(child):
                    return child.state
                frontier.add(child.state)
            # If the child node has been discovered but not explored, check if the child node
            # has a lower depth than the node in the frontier
            elif frontier.contains_state(child.state):
                for i in frontier.frontier:
                    if i.state == child.state:
                        if i.depth > child.depth:
                            frontier.add(child.state)
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

    # The loop continues until the frontier is empty
    while True:
        if frontier.empty():
            print("Frontier is empty")
            return None
        node = frontier.remove()
        explored.add(node)
        # The actions function returns the set of all possible actions that can be performed
        # on the bottles at a given state
        for action in problem.actions(node):
            child = node.child_node(problem, action)
            print(child)
            # The child node is added to the frontier if it has not been explored or discovered
            # The child node is returned if it is the goal state
            # The child node contains three bottles, check that bottles with similar current volume
            # have not been explored or discovered
            if child not in explored and not frontier.contains_state(child):
                if problem.goal_test(child):
                    print(f"Goal state reached: {child.state}")
                    return child.state
                frontier.add(child)
            # If the child node has been discovered but not explored, check if the child node
            # has a lower depth than the node in the frontier
            elif frontier.contains_state(child):
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
        explored.add(node)
        for action in problem.actions(node):
            child = node.child_node(problem, action)
            if child not in explored and not frontier.contains_state(child):
                if problem.goal_test(child):
                    return child.state
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
            if child not in explored and not frontier.contains_state(child):
                if problem.goal_test(child):
                    return child.state
                frontier.add(child, h(child.state) + child.path_cost)
            elif frontier.contains_state(child.state) and frontier.get_priority(child.state) > h(child.state) + child.path_cost:
                frontier.add(child, h(child.state) + child.path_cost)

    return None


# 5. Using Deep Limited Search
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
            if child not in explored and not frontier.contains_state(child):
                if problem.goal_test(child):
                    return child.state
                frontier.add(child)

    return None

# 6. Using Iterative Deepening Search
def iterative_deepening_search(problem: Problem) -> None:
    for depth in range(100):
        result = depth_limited_search(problem, depth)
        if result != "cutoff":
            return result


# 7. Using Recursive Best First Search
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
                if problem.goal_test(child):
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

# This is a TKinter window with buttons to run the search algorithms and display the results
# The window should also display the current state of the search algorithms
# Includes an input box to allow the user to enter the initial state of the problem
# Includes a drop down menu to allow the user to select the search algorithm to use
# Includes a drop down menu to allow the user to select the heuristic function to use
# Includes a drop down menu to allow the user to select the problem to solve
def showOnTkinter():
    # Create the window
    window = Tk()
    window.title("Search Algorithms")

    # Create the frame
    frame = Frame(window, width=600, height=500)
    frame.grid(row=0, column=0)

    # Create the title
    title = Label(frame, text="Search Algorithms")
    title.grid(row=0, column=0, columnspan=2)

    # Create the initial state label
    initial_state_label = Label(frame, text="Initial State:")
    initial_state_label.grid(row=1, column=0)

    # Create the initial state entry
    initial_state_entry = Entry(frame, width=50)
    initial_state_entry.grid(row=1, column=1)

    # Create the search algorithm label
    search_algorithm_label = Label(frame, text="Search Algorithm:")
    search_algorithm_label.grid(row=3, column=0)

    # Create the search algorithm drop down menu
    search_algorithm = StringVar(frame)
    search_algorithm.set("Breadth First Search")
    search_algorithm_menu = OptionMenu(frame, search_algorithm, "Breadth First Search", "Depth First Search",
                                       "Greedy Best First Search", "A* Search", "Iterative Deepening Search",
                                       "Recursive Best First Search")
    search_algorithm_menu.grid(row=3, column=1)

    # Create the heuristic function label
    heuristic_function_label = Label(frame, text="Heuristic Function:")
    heuristic_function_label.grid(row=4, column=0)

    # Create the heuristic function drop down menu
    heuristic_function = StringVar(frame)
    heuristic_function.set("Built-in")
    heuristic_function_menu = OptionMenu(frame, heuristic_function, "Built-in")
    heuristic_function_menu.grid(row=4, column=1)

    # Create the problem label
    problem_label = Label(frame, text="Problem:")
    problem_label.grid(row=5, column=0)

    # Create the problem drop down menu
    problem = StringVar(frame)
    problem.set("Water Bottles")
    problem_menu = OptionMenu(frame, problem, "Water Bottles")
    problem_menu.grid(row=5, column=1)

    # Create the run seaech algorithm function
    def run_search_algorithm(initial_state, search_algorithm, heuristic_function, problem):
        # Create the problem
        if problem == "Water Bottles":
            initial = list(initial_state)
            initial = [int(x) for x in initial]
            initial_state =  [Bottle(y) for y in initial]
            initial_state = tuple(initial_state)
            initial_state = Node(initial_state)
            problem = WaterBottleProblem(initial_state)

        # Create the search algorithm
        if search_algorithm == "Breadth First Search":
            search_algorithm = breadth_first_search(problem)
        elif search_algorithm == "Depth First Search":
            search_algorithm = depth_first_search(problem)
        elif search_algorithm == "Greedy Best First Search":
            if heuristic_function == "Built-in":
                search_algorithm = lambda problem: greedy_best_first_search(problem, problem.h)
        elif search_algorithm == "A* Search":
            if heuristic_function == "Built-in":
                search_algorithm = lambda problem: a_star_search(problem, problem.h)
        elif search_algorithm == "Iterative Deepening Search":
            search_algorithm = iterative_deepening_search(problem)
        elif search_algorithm == "Recursive Best First Search":
            if heuristic_function == "Built-in":
                search_algorithm = lambda problem: recursive_best_first_search(problem, problem.h)

        # Create the node
        node = search_algorithm(problem)

        # Visualize the search
        visualize_search(problem, node, search_algorithm.__name__)

        # Display the output
        output_text.delete("1.0", "end")
        output_text.insert("1.0", node.solution())

        # Display the frontier
        frontier_text.delete("1.0", "end")
        frontier_text.insert("1.0", node.frontier())

    # Create the run button
    run_button = Button(frame, text="Run")
    run_button.bind("<Button-1>", lambda event: run_search_algorithm(initial_state_entry.get(), search_algorithm.get(),
                                                                    heuristic_function.get(), problem.get()))
    run_button.grid(row=1, column=3, columnspan=2)

    # Create the output label
    output_label = Label(frame, text="Output:")
    output_label.grid(row=6, column=0, columnspan=2)

    # Create the output text box
    output_text = Text(frame, width=50, height=5)
    output_text.grid(row=7, column=0, columnspan=2)

    # Create the frontier label
    frontier_label = Label(frame, text="Frontier:")
    frontier_label.grid(row=8, column=0, columnspan=2)

    # Create the frontier text box
    frontier_text = Text(frame, width=50, height=5)
    frontier_text.grid(row=9, column=0, columnspan=2)

    # Create the explored label
    explored_label = Label(frame, text="Explored:")
    explored_label.grid(row=10, column=0, columnspan=2)

    # Create the explored text box
    explored_text = Text(frame, width=50, height=5)
    explored_text.grid(row=11, column=0, columnspan=2)

    # Create the graph label
    graph_label = Label(frame, text="Graph:")
    graph_label.grid(row=12, column=0, columnspan=2)

    # Create the graph canvas
    graph_canvas = Canvas(frame, width=500, height=100)
    graph_canvas.grid(row=13, column=0, columnspan=2)

    # Run the mainloop
    window.mainloop()


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
    bfs_problem = WaterBottleProblem(caseOne, caseOneEnd)
    problem2 = WaterBottleProblem(caseTwo, caseTwoEnd)
    problem3 = WaterBottleProblem(caseThree, caseThreeEnd)
    print("Case 1: Start")
    breadth_first_search(bfs_problem)
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
    depth_first_search(problem2)
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
